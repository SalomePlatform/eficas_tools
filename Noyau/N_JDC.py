# coding=utf-8
# Copyright (C) 2007-2017   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com


"""
   Ce module contient la classe JDC qui sert a interpreter un jeu de commandes
"""

# Modules Python
from __future__ import absolute_import
from __future__ import print_function
try :
   from builtins import str
   from builtins import range
except : pass
import os
import traceback
import types
import sys
import linecache

# Modules EFICAS
from . import N_OBJECT
from . import N_CR
from .N_Exception import AsException, InterruptParsingError
from .N_ASSD import ASSD
from .strfunc import get_encoding
from six.moves import range


MemoryErrorMsg = """MemoryError :

En general, cette erreur se produit car la memoire utilisee hors du fortran
(jeveux) est importante.

Causes possibles :
   - le calcul produit de gros objets Python dans une macro-commande ou
     dans le jeu de commande lui-meme,
   - le calcul appelle un solveur (MUMPS par exemple) ou un outil externe
     qui a besoin de memoire hors jeveux,
   - utilisation de jeveux dynamique,
   - ...

Solution :
   - distinguer la memoire limite du calcul (case "Memoire totale" de astk)
     de la memoire reservee a jeveux (case "dont Aster"), le reste etant
     disponible pour les allocations dynamiques.
"""


class JDC(N_OBJECT.OBJECT):

    """
       Cette classe interprete un jeu de commandes fourni sous
       la forme d'une chaine de caractères

       Attributs de classe :

       Attributs d'instance :

    """
    nature = "JDC"
    CR = N_CR.CR
    exec_init = """
import Accas
from Accas import _F
from Accas import *
NONE = None
"""

    from .N_utils import SEP

    def __init__(self, definition=None, procedure=None, cata=None,
                 cata_ord_dico=None, parent=None,
                 nom='SansNom', appli=None, context_ini=None, **args):
        self.procedure = procedure
        self.definition = definition
        self.cata = cata
        if type(self.cata) != tuple and cata != None:
            self.cata = (self.cata,)
        self._build_reserved_kw_list()
        self.cata_ordonne_dico = cata_ord_dico
        self.nom = nom
        self.appli = appli
        self.parent = parent
        self.context_ini = context_ini
        # On conserve les arguments supplementaires. Il est possible de passer
        # des informations globales au JDC par ce moyen. Il pourrait etre plus
        # sur de mettre en place le mecanisme des mots-cles pour verifier la
        # validite des valeurs passees.
        # Ceci reste a faire
        # On initialise avec les parametres de la definition puis on
        # update avec ceux du JDC
        self.args = self.definition.args
        self.args.update(args)
        self.nstep = 0
        self.nsd = 0
        self.par_lot = 'OUI'
        self.par_lot_user = None
        if definition:
            self.regles = definition.regles
            self.code = definition.code
        else:
            self.regles = ()
            self.code = "CODE"
        #
        #  Creation de l objet compte rendu pour collecte des erreurs
        #
        self.cr = self.CR(debut="CR phase d'initialisation",
                          fin="fin CR phase d'initialisation")
        # on met le jdc lui-meme dans le context global pour l'avoir sous
        # l'etiquette "jdc" dans le fichier de commandes
        self.g_context = {'jdc': self}
        # Dictionnaire pour stocker tous les concepts du JDC (acces rapide par
        # le nom)
        self.sds_dict = {}
        self.etapes = []
        self.index_etapes = {}
        self.mc_globaux = {}
        self.current_context = {}
        self.condition_context = {}
        self.index_etape_courante = 0
        self.UserError = "UserError"
        self.alea = None
        # permet transitoirement de conserver la liste des etapes
        self.hist_etape = False

    def compile(self):
        """
           Cette methode compile la chaine procedure
           Si des erreurs se produisent, elles sont consignees dans le
           compte-rendu self.cr
        """
        try:
            if self.appli != None:
                self.appli.afficheInfos(
                    'Compilation du fichier de commandes en cours ...')
            # Python 2.7 compile function does not accept unicode filename, so we encode it
            # with the current locale encoding in order to have a correct
            # traceback
            encoded_filename = self.nom.encode(get_encoding())
            self.proc_compile = compile(
                self.procedure, encoded_filename, 'exec')
        except SyntaxError as e:
            if CONTEXT.debug:
                traceback.print_exc()
            l = traceback.format_exception_only(SyntaxError, e)
            self.cr.exception("Compilation impossible : " + ''.join(l))
        except MemoryError as e:
            self.cr.exception(MemoryErrorMsg)
        except SystemError as e:
            erreurs_connues = """
Causes possibles :
 - offset too large : liste trop longue derrière un mot-cle.
   Solution : liste = (valeurs, ..., )
              MOT_CLE = *liste,
"""
            l = traceback.format_exception_only(SystemError, e)
            l.append(erreurs_connues)
            self.cr.exception("Compilation impossible : " + ''.join(l))
        return

    def exec_compile(self):
        """
           Cette methode execute le jeu de commandes compile dans le contexte
           self.g_context de l'objet JDC
        """
        CONTEXT.setCurrentStep(self)
        # Le module nommage utilise le module linecache pour acceder
        # au source des commandes du jeu de commandes.
        # Dans le cas d'un fichier, on accède au contenu de ce fichier
        # Dans le cas d'une chaine de caractères il faut acceder
        # aux commandes qui sont dans la chaine
        import linecache
        linecache.cache[self.nom] = 0, 0, self.procedure.split('\n'), self.nom
        try:
            exec(self.exec_init, self.g_context)
            for obj_cata in self.cata:
                if type(obj_cata) == types.ModuleType:
                    init2 = "from " + obj_cata.__name__ + " import *"
                    exec(init2, self.g_context)

            # Initialisation du contexte global pour l'evaluation des conditions de BLOC
            # On utilise une copie de l'initialisation du contexte du jdc
            self.condition_context = self.g_context.copy()

            # Si l'attribut context_ini n'est pas vide, on ajoute au contexte global
            # le contexte initial (--> permet d'evaluer un JDC en recuperant un contexte
            # d'un autre par exemple)
            if self.context_ini:
                self.g_context.update(self.context_ini)
                # Update du dictionnaire des concepts
                for sdnom, sd in list(self.context_ini.items()):
                    if isinstance(sd, ASSD):
                        self.sds_dict[sdnom] = sd

            if self.appli != None:
                self.appli.afficheInfos(
                    'Interpretation du fichier de commandes en cours ...')
            # On sauve le contexte pour garder la memoire des constantes
            # En mode edition (EFICAS) ou lors des verifications le contexte
            # est recalcule
            # mais les constantes sont perdues
            self.const_context = self.g_context
            exec(self.proc_compile, self.g_context)

            CONTEXT.unsetCurrentStep()
            if self.appli != None:
                self.appli.afficheInfos('')

        except InterruptParsingError:
            # interrupt the command file parsing used by FIN to ignore the end
            # of the file
            pass

        except EOFError:
            # Exception utilise pour interrompre un jeu
            # de commandes avant la fin
            # Fonctionnement normal, ne doit pas etre considere comme une
            # erreur
            CONTEXT.unsetCurrentStep()
            self.affiche_fin_exec()
            self.traiter_fin_exec('commande')

        except AsException as e:
            # une erreur a ete identifiee
            if CONTEXT.debug:
                traceback.print_exc()
            # l'exception a ete recuperee avant (ou, comment ?),
            # donc on cherche dans le texte
            txt = str(e)
            if txt.find('MemoryError') >= 0:
                txt = MemoryErrorMsg
            self.cr.exception(txt)
            CONTEXT.unsetCurrentStep()

        except NameError as e:
            etype, value, tb = sys.exc_info()
            l = traceback.extract_tb(tb)
            s = traceback.format_exception_only("Erreur de nom", e)[0][:-1]
            msg = "erreur de syntaxe,  %s ligne %d" % (s, l[-1][1])
            if CONTEXT.debug:
                traceback.print_exc()
            self.cr.exception(msg)
            CONTEXT.unsetCurrentStep()

       # except self.UserError as exc_val:
       #     self.traiter_user_exception(exc_val)
       #     CONTEXT.unsetCurrentStep()
       #     self.affiche_fin_exec()
       #     self.traiter_fin_exec('commande')

        except:
            # erreur inattendue
            # sys_exc_typ,sys_exc_value,sys_exc_frame = sys_exc.info()
            # (tuple de 3 elements)
            if CONTEXT.debug:
                traceback.print_exc()

            traceback.print_exc()

            exc_typ, exc_val, exc_fr = sys.exc_info()
            l = traceback.format_exception(exc_typ, exc_val, exc_fr)
            self.cr.exception(
                "erreur non prevue et non traitee prevenir la maintenance " + '\n' + ''.join(l))
            del exc_typ, exc_val, exc_fr
            CONTEXT.unsetCurrentStep()

    def affiche_fin_exec(self):
        """
           Cette methode realise l'affichage final des statistiques de temps
           apres l'execution de toutes
           les commandes en mode commande par commande ou par lot
           Elle doit etre surchargee pour en introduire un
        """
        return

    def traiter_fin_exec(self, mode, etape=None):
        """
           Cette methode realise un traitement final apres l'execution de toutes
           les commandes en mode commande par commande ou par lot
           Par defaut il n'y a pas de traitement. Elle doit etre surchargee
           pour en introduire un
        """
        print ( "FIN D'EXECUTION %s %s" %s( mode, etape))

    def traiter_user_exception(self, exc_val):
        """Cette methode realise un traitement sur les exceptions utilisateur
           Par defaut il n'y a pas de traitement. La methode doit etre
           surchargee pour en introduire un.
        """
        return

    def register(self, etape):
        """
           Cette methode ajoute etape dans la liste des etapes : self.etapes
           et retourne un numero d'enregistrement
        """
        self.etapes.append(etape)
        self.index_etapes[etape] = len(self.etapes) - 1
        return self.g_register(etape)

    def o_register(self, sd):
        """
           Retourne un identificateur pour concept
        """
        self.nsd = self.nsd + 1
        nom = sd.idracine + self.SEP + repr(self.nsd)
        return nom

    def g_register(self, etape):
        """
            Retourne un identificateur pour etape
        """
        self.nstep = self.nstep + 1
        idetape = etape.idracine + self.SEP + repr(self.nstep)
        return idetape

    def create_sdprod(self, etape, nomsd):
        """
            Cette methode doit fabriquer le concept produit retourne
            par l'etape etape et le nommer.

            Elle est appelee a l'initiative de l'etape
            pendant le processus de construction de cette etape :
            methode __call__ de la classe CMD (OPER ou MACRO)

            Ce travail est realise par le contexte superieur
            (etape.parent) car dans certains cas, le concept ne doit
            pas etre fabrique mais l'etape doit simplement utiliser
            un concept preexistant.

            Deux cas possibles :
                    - Cas 1 : etape.reuse != None : le concept est reutilise
                    - Cas 2 : l'etape appartient a une macro qui a declare un
                            concept de sortie qui doit etre produit par cette
                            etape.
            Dans le cas du JDC, le deuxième cas ne peut pas se produire.
        """
        sd = etape.getSdProd()
        if sd != None and (etape.definition.reentrant == 'n' or etape.reuse is None):
            # ATTENTION : On ne nomme la SD que dans le cas de non reutilisation
            # d un concept. Commande non reentrante ou reuse absent.
            self.NommerSdprod(sd, nomsd)
        return sd

    def NommerSdprod(self, sd, sdnom, restrict='non'):
        """
            Nomme la SD apres avoir verifie que le nommage est possible : nom
            non utilise
            Si le nom est deja utilise, leve une exception
            Met le concept cree dans le concept global g_context
        """
        o = self.sds_dict.get(sdnom, None)
        if isinstance(o, ASSD):
            raise AsException("Nom de concept deja defini : %s" % sdnom)
        if sdnom in self._reserved_kw:
            raise AsException(
                "Nom de concept invalide. '%s' est un mot-cle reserve." % sdnom)

        # Ajoute a la creation (appel de reg_sd).
        self.sds_dict[sdnom] = sd
        sd.set_name(sdnom)

        # En plus si restrict vaut 'non', on insere le concept dans le contexte
        # du JDC
        if restrict == 'non':
            self.g_context[sdnom] = sd

    def reg_sd(self, sd):
        """
            Methode appelee dans l __init__ d un ASSD lors de sa creation
            pour s enregistrer
        """
        return self.o_register(sd)

    def deleteConceptAfterEtape(self, etape, sd):
        """
            Met a jour les etapes du JDC qui sont après etape suite a
            la disparition du concept sd
        """
        # Cette methode est definie dans le noyau mais ne sert que pendant
        # la phase de creation des etapes et des concepts. Il n'y a aucun
        # traitement particulier a realiser.
        # Dans d'autres conditions, il faut surcharger cette methode
        return

    def supprime(self):
        N_OBJECT.OBJECT.supprime(self)
        for etape in self.etapes:
            etape.supprime()

    def clean(self, netapes):
        """Nettoie les `netapes` dernières etapes de la liste des etapes."""
        if self.hist_etape:
            return
        for i in range(netapes):
            e = self.etapes.pop()
            jdc = e.jdc
            parent = e.parent
            e.supprime()
            e.parent = parent
            e.jdc = jdc
            del self.index_etapes[e]

    def getFile(self, unite=None, fic_origine='', fname=None):
        """
            Retourne le nom du fichier correspondant a un numero d'unite
            logique (entier) ainsi que le source contenu dans le fichier
        """
        if self.appli:
            # Si le JDC est relie a une application maitre, on delègue la
            # recherche
            return self.appli.getFile(unite, fic_origine)
        else:
            if unite != None:
                if os.path.exists("fort." + str(unite)):
                    fname = "fort." + str(unite)
            if fname == None:
                raise AsException("Impossible de trouver le fichier correspondant"
                                  " a l unite %s" % unite)
            if not os.path.exists(fname):
                raise AsException("%s n'est pas un fichier existant" % fname)
            fproc = open(fname, 'r')
            text = fproc.read()
            fproc.close()
            text = text.replace('\r\n', '\n')
            linecache.cache[fname] = 0, 0, text.split('\n'), fname
            return fname, text

    def set_par_lot(self, par_lot, user_value=False):
        """
        Met le mode de traitement a PAR LOT
        ou a COMMANDE par COMMANDE
        en fonction de la valeur du mot cle PAR_LOT et
        du contexte : application maitre ou pas

        En PAR_LOT='NON', il n'y a pas d'ambiguite.
        d'analyse et juste avant la phase d'execution.
        `user_value` : permet de stocker la valeur choisie par l'utilisateur
        pour l'interroger plus tard (par exemple dans `getContexte_avant`).
        """
        if user_value:
            self.par_lot_user = par_lot
        if self.appli == None:
            # Pas d application maitre
            self.par_lot = par_lot
        else:
            # Avec application maitre
            self.par_lot = 'OUI'

    def accept(self, visitor):
        """
           Cette methode permet de parcourir l'arborescence des objets
           en utilisant le pattern VISITEUR
        """
        visitor.visitJDC(self)

    def interact(self):
        """
            Cette methode a pour fonction d'ouvrir un interpreteur
            pour que l'utilisateur entre des commandes interactivement
        """
        CONTEXT.setCurrentStep(self)
        try:
            # Le module nommage utilise le module linecache pour acceder
            # au source des commandes du jeu de commandes.
            # Dans le cas d'un fichier, on accède au contenu de ce fichier
            # Dans le cas de la console interactive, il faut pouvoir acceder
            # aux commandes qui sont dans le buffer de la console
            import linecache
            import code
            console = code.InteractiveConsole(
                self.g_context, filename="<console>")
            linecache.cache["<console>"] = 0, 0, console.buffer, "<console>"
            banner = """***********************************************
*          Interpreteur interactif %s
***********************************************""" % self.code
            console.interact(banner)
        finally:
            console = None
            CONTEXT.unsetCurrentStep()

    def getContexte_avant(self, etape):
        """
           Retourne le dictionnaire des concepts connus avant etape
           On tient compte des commandes qui modifient le contexte
           comme DETRUIRE ou les macros
           Si etape == None, on retourne le contexte en fin de JDC
        """
        # L'etape courante pour laquelle le contexte a ete calcule est
        # memorisee dans self.index_etape_courante
        # XXX on pourrait faire mieux dans le cas PAR_LOT="NON" : en
        # memorisant l'etape
        # courante pendant le processus de construction des etapes.
        # Si on insère des commandes (par ex, dans EFICAS), il faut prealablement
        # remettre ce pointeur a 0
        # self.current_context.items() if isinstance(v, ASSD)])
        if self.par_lot_user == 'NON':
            d = self.current_context = self.g_context.copy()
            if etape is None:
                return d
            # retirer les sd produites par 'etape'
            sd_names = [sd.nom for sd in etape.getCreated_sd()]
            for nom in sd_names:
                try:
                    del d[nom]
                except KeyError:
                    from warnings import warn
                    warn(
                        "concept '%s' absent du contexte de %s" % (
                            nom, self.nom),
                        RuntimeWarning, stacklevel=2)
            return d
        if etape:
            index_etape = self.index_etapes[etape]
        else:
            index_etape = len(self.etapes)
        if index_etape >= self.index_etape_courante:
            # On calcule le contexte en partant du contexte existant
            d = self.current_context
            if self.index_etape_courante == 0 and self.context_ini:
                d.update(self.context_ini)
            liste_etapes = self.etapes[self.index_etape_courante:index_etape]
        else:
            d = self.current_context = {}
            if self.context_ini:
                d.update(self.context_ini)
            liste_etapes = self.etapes

        for e in liste_etapes:
            if e is etape:
                break
            if e.isActif():
                e.updateContext(d)
        self.index_etape_courante = index_etape
        return d

    def get_global_contexte(self):
        """Retourne "un" contexte global ;-)"""
        # N'est utilise que par INCLUDE (sauf erreur).
        # g_context est remis a {} en PAR_LOT='OUI'. const_context permet
        # de retrouver ce qui y a ete mis par exec_compile.
        # Les concepts n'y sont pas en PAR_LOT='OUI'. Ils sont ajoutes
        # par get_global_contexte de la MACRO.
        d = self.const_context.copy()
        d.update(self.g_context)
        return d

    def getContexte_courant(self, etape_courante=None):
        """
           Retourne le contexte tel qu'il est (ou 'sera' si on est en phase
           de construction) au moment de l'execution de l'etape courante.
        """
        if etape_courante is None:
            etape_courante = CONTEXT.get_current_step()
        return self.getContexte_avant(etape_courante)

    def get_concept(self, nomsd):
        """
            Methode pour recuperer un concept a partir de son nom
        """
        co = self.getContexte_courant().get(nomsd.strip(), None)
        if not isinstance(co, ASSD):
            co = None
        return co

    def get_concept_by_type(self, nomsd, typesd, etape):
        """
            Methode pour recuperer un concept a partir de son nom et de son type.
            Il aura comme père 'etape'.
        """
        assert issubclass(typesd, ASSD), typesd
        co = typesd(etape=etape)
        co.set_name(nomsd)
        co.executed = 1
        return co

    def del_concept(self, nomsd):
        """
           Methode pour supprimer la reference d'un concept dans le sds_dict.
           Ne detruire pas le concept (different de supprime).
        """
        try:
            del self.sds_dict[nomsd.strip()]
        except:
            pass

    def get_cmd(self, nomcmd):
        """
            Methode pour recuperer la definition d'une commande
            donnee par son nom dans les catalogues declares
            au niveau du jdc
        """
        for cata in self.cata:
            if hasattr(cata, nomcmd):
                return getattr(cata, nomcmd)

    def append_reset(self, etape):
        """
           Ajoute une etape provenant d'un autre jdc a la liste des etapes
           et remet a jour la parente de l'etape et des concepts
        """
        self.etapes.append(etape)
        self.index_etapes[etape] = len(self.etapes) - 1
        etape.reparent(self)
        etape.reset_jdc(self)

    def sd_accessible(self):
        """On peut acceder aux "valeurs" (jeveux) des ASSD si le JDC est en PAR_LOT="NON".
        """
        if CONTEXT.debug:
            print((' `- JDC sd_accessible : PAR_LOT =', self.par_lot))
        return self.par_lot == 'NON'

    def _build_reserved_kw_list(self):
        """Construit la liste des mots-cles reserves (interdits pour le
        nommage des concepts)."""
        self._reserved_kw = set()
        for cat in self.cata:
            self._reserved_kw.update(
                [kw for kw in dir(cat) if len(kw) <= 8 and kw == kw.upper()])
        self._reserved_kw.difference_update(
            ['OPER', 'MACRO', 'BLOC', 'SIMP', 'FACT', 'FORM',
             'GEOM', 'MCSIMP', 'MCFACT'])
