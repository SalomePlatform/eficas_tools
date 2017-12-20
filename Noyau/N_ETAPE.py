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
    Ce module contient la classe ETAPE qui sert a verifier et a executer
    une commande
"""

# Modules Python
from __future__ import absolute_import
from __future__ import print_function
try :
   from builtins import str
except :
   pass
import types
import sys
import os
import linecache
import traceback
from copy import copy

# Modules EFICAS
from . import N_MCCOMPO
from .N_Exception import AsException
from . import N_utils
from .N_utils import AsType
from .N_ASSD import ASSD


class ETAPE(N_MCCOMPO.MCCOMPO):

    """
       Cette classe herite de MCCOMPO car ETAPE est un OBJECT composite

    """
    nature = "OPERATEUR"

    # L'attribut de classe codex est utilise pour rattacher le module de calcul eventuel (voir Build)
    # On le met a None pour indiquer qu'il n'y a pas de module de calcul
    # rattache
    codex = None

    def __init__(self, oper=None, reuse=None, args={}, niveau=4):
        """
        Attributs :
         - definition : objet portant les attributs de definition d'une etape de type operateur. Il
                        est initialise par l'argument oper.
         - reuse : indique le concept d'entree reutilise. Il se trouvera donc en sortie
                   si les conditions d'execution de l'operateur l'autorise
         - valeur : arguments d'entree de type mot-cle=valeur. Initialise avec l'argument args.
        """
        self.definition = oper
        self.reuse = reuse
        self.valeur = args
        self.nettoiargs()
        self.parent = CONTEXT.get_current_step()
        self.etape = self
        self.nom = oper.nom
        self.idracine = oper.label
        self.appel = N_utils.callee_where(niveau)
        self.mc_globaux = {}
        self.sd = None
        self.actif = 1
        self.makeRegister()
        self.icmd = None

    def makeRegister(self):
        """
        Initialise les attributs jdc, id, niveau et realise les
        enregistrements necessaires
        """
        if self.parent:
            self.jdc = self.parent.getJdcRoot()
            self.id = self.parent.register(self)
            self.niveau = None
        else:
            self.jdc = self.parent = None
            self.id = None
            self.niveau = None

    def nettoiargs(self):
        """
           Cette methode a pour fonction de retirer tous les arguments egaux a None
           de la liste des arguments. Ils sont supposes non presents et donc retires.
        """
        for k in list(self.valeur.keys()):
            if self.valeur[k] == None:
                del self.valeur[k]

    def McBuild(self):
        """
           Demande la construction des sous-objets et les stocke dans l'attribut
           mc_liste.
        """
        self.mc_liste = self.build_mc()

    def buildSd(self, nom):
        """
           Construit le concept produit de l'operateur. Deux cas
           peuvent se presenter :

             - le parent n'est pas defini. Dans ce cas, l'etape prend en charge la creation
               et le nommage du concept.

             - le parent est defini. Dans ce cas, l'etape demande au parent la creation et
               le nommage du concept.

        """
        self.sdnom = nom
        try:
            if self.parent:
                sd = self.parent.create_sdprod(self, nom)
                if type(self.definition.op_init) == types.FunctionType:
                    self.definition.op_init(*(
                        self, self.parent.g_context))
            else:
                sd = self.getSdProd()
                # On n'utilise pas self.definition.op_init car self.parent
                # n'existe pas
                if sd != None and self.reuse == None:
                    # On ne nomme le concept que dans le cas de non reutilisation
                    # d un concept
                    sd.set_name(nom)
        except AsException as e:
            raise AsException("Etape ", self.nom, 'ligne : ', self.appel[0],
                              'fichier : ', self.appel[1], e)
        except EOFError:
            raise
        except:
            l = traceback.format_exception(
                sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
            raise AsException("Etape ", self.nom, 'ligne : ', self.appel[0],
                              'fichier : ', self.appel[1] + '\n',
                              ''.join(l))

        self.Execute()
        return sd

    def Execute(self):
        """
           Cette methode est un point d'entree prevu pour realiser une execution immediatement
           apres avoir construit les mots cles et le concept produit.
           Par defaut, elle ne fait rien. Elle doit etre surchargee dans une autre partie du programme.
        """
        return

    def getSdProd(self):
        """
            Retourne le concept resultat de l'etape
            Deux cas :
                     - cas 1 : sd_prod de oper n'est pas une fonction
                       il s'agit d'une sous classe de ASSD
                       on construit le sd a partir de cette classe
                       et on le retourne
                     - cas 2 : il s'agit d'une fonction
                       on l'evalue avec les mots-cles de l'etape (mc_liste)
                       on construit le sd a partir de la classe obtenue
                       et on le retourne
        """
        if type(self.definition.sd_prod) == types.FunctionType:
            d = self.creeDictValeurs(self.mc_liste)
            try:
                sd_prod = self.definition.sd_prod(*(), **d)
            except EOFError:
                raise
            except Exception as exc:
                if CONTEXT.debug:
                    traceback.print_exc()
                raise AsException("impossible d affecter un type au resultat:",
                                  str(exc))
        else:
            sd_prod = self.definition.sd_prod
        # on teste maintenant si la SD est reutilisee ou s'il faut la creer
        if self.definition.reentrant != 'n' and self.reuse:
            # Le concept produit est specifie reutilise (reuse=xxx). C'est une erreur mais non fatale.
            # Elle sera traitee ulterieurement.
            self.sd = self.reuse
        else:
            self.sd = sd_prod(etape=self)
            # Si l'operateur est obligatoirement reentrant et reuse n'a pas ete specifie, c'est une erreur.
            # On ne fait rien ici. L'erreur sera traiter par la suite.
        # precaution
        if self.sd is not None and not isinstance(self.sd, ASSD):
            raise AsException("""
Impossible de typer le resultat !
Causes possibles :
   Utilisateur : Soit la valeur fournie derrière "reuse" est incorrecte,
                 soit il y a une "," a la fin d'une commande precedente.
   Developpeur : La fonction "sd_prod" retourne un type invalide.""")
        return self.sd

    def getType_produit(self):
        try:
            return self.getType_produit_brut()
        except:
            return None

    def getType_produit_brut(self):
        """
            Retourne le type du concept resultat de l'etape
            Deux cas :
              - cas 1 : sd_prod de oper n'est pas une fonction
                il s'agit d'une sous classe de ASSD
                on retourne le nom de la classe
              - cas 2 : il s'agit d'une fonction
                on l'evalue avec les mots-cles de l'etape (mc_liste)
                et on retourne son resultat
        """
        if type(self.definition.sd_prod) == types.FunctionType:
            d = self.creeDictValeurs(self.mc_liste)
            sd_prod = self.definition.sd_prod(*(), **d)
        else:
            sd_prod = self.definition.sd_prod
        return sd_prod

    def get_etape(self):
        """
           Retourne l'etape a laquelle appartient self
           Un objet de la categorie etape doit retourner self pour indiquer que
           l'etape a ete trouvee
        """
        return self

    def supprime(self):
        """
           Methode qui supprime toutes les references arrières afin que l'objet puisse
           etre correctement detruit par le garbage collector
        """
        N_MCCOMPO.MCCOMPO.supprime(self)
        self.jdc = None
        self.appel = None
        for name in dir(self):
            if name.startswith('_cache_'):
                setattr(self, name, None)
        if self.sd:
            self.sd.supprime()

    def __del__(self):
        pass

    def getCreated_sd(self):
        """Retourne la liste des sd reellement produites par l'etape.
        Si reuse est present, `self.sd` a ete creee avant, donc n'est pas dans
        cette liste."""
        if not self.reuse and self.sd:
            return [self.sd, ]
        return []

    def isActif(self):
        """
           Indique si l'etape est active (1) ou inactive (0)
        """
        return self.actif

    def setCurrentStep(self):
        """
            Methode utilisee pour que l etape self se declare etape
            courante. Utilise par les macros
        """
        cs = CONTEXT.get_current_step()
        if self.parent != cs:
            raise AsException("L'etape courante", cs.nom, cs,
                              "devrait etre le parent de", self.nom, self)
        else:
            CONTEXT.unsetCurrentStep()
            CONTEXT.setCurrentStep(self)

    def resetCurrentStep(self):
        """
              Methode utilisee par l'etape self qui remet son etape parent comme
              etape courante
        """
        cs = CONTEXT.get_current_step()
        if self != cs:
            raise AsException("L'etape courante", cs.nom, cs,
                              "devrait etre", self.nom, self)
        else:
            CONTEXT.unsetCurrentStep()
            CONTEXT.setCurrentStep(self.parent)

    def issubstep(self, etape):
        """
            Cette methode retourne un entier indiquant si etape est une
            sous etape de self ou non
            1 = oui
            0 = non
            Une etape simple n'a pas de sous etape
        """
        return 0

    def getFile(self, unite=None, fic_origine='', fname=None):
        """
            Retourne le nom du fichier correspondant a un numero d'unite
            logique (entier) ainsi que le source contenu dans le fichier
        """
        if self.jdc:
            return self.jdc.getFile(unite=unite, fic_origine=fic_origine, fname=fname)
        else:
            if unite != None:
                if os.path.exists("fort." + str(unite)):
                    fname = "fort." + str(unite)
            if fname == None:
                raise AsException("Impossible de trouver le fichier correspondant"
                                  " a l unite %s" % unite)
            if not os.path.exists(fname):
                raise AsException("%s n'est pas un fichier existant" % unite)
            fproc = open(fname, 'r')
            text = fproc.read()
            fproc.close()
            text = text.replace('\r\n', '\n')
            linecache.cache[fname] = 0, 0, text.split('\n'), fname
            return fname, text

    def accept(self, visitor):
        """
           Cette methode permet de parcourir l'arborescence des objets
           en utilisant le pattern VISITEUR
        """
        visitor.visitETAPE(self)

    def updateContext(self, d):
        """
            Cette methode doit updater le contexte fournit par
            l'appelant en argument (d) en fonction de sa definition
        """
        if type(self.definition.op_init) == types.FunctionType:
            self.definition.op_init(*(self, d))
        if self.sd:
            d[self.sd.nom] = self.sd

    def copy(self):
        """ Methode qui retourne une copie de self non enregistree auprès du JDC
            et sans sd
        """
        etape = copy(self)
        etape.sd = None
        etape.state = 'modified'
        etape.reuse = None
        etape.sdnom = None
        etape.etape = etape
        etape.mc_liste = []
        for objet in self.mc_liste:
            new_obj = objet.copy()
            new_obj.reparent(etape)
            etape.mc_liste.append(new_obj)
        return etape

    def copy_reuse(self, old_etape):
        """ Methode qui copie le reuse d'une autre etape.
        """
        if hasattr(old_etape, "reuse"):
            self.reuse = old_etape.reuse

    def copy_sdnom(self, old_etape):
        """ Methode qui copie le sdnom d'une autre etape.
        """
        if hasattr(old_etape, "sdnom"):
            self.sdnom = old_etape.sdnom

    def reparent(self, parent):
        """
            Cette methode sert a reinitialiser la parente de l'objet
        """
        self.parent = parent
        self.jdc = parent.getJdcRoot()
        self.etape = self
        for mocle in self.mc_liste:
            mocle.reparent(self)
        if self.sd and self.reuse == None:
            self.sd.jdc = self.jdc

    def get_cmd(self, nomcmd):
        """
            Methode pour recuperer la definition d'une commande
            donnee par son nom dans les catalogues declares
            au niveau du jdc
            Appele par un ops d'une macro en Python
        """
        return self.jdc.get_cmd(nomcmd)

    def copy_intern(self, etape):
        """
            Methode permettant lors du processus de recopie de copier
            les elements internes d'une etape dans une autre
        """
        return

    def full_copy(self, parent=None):
        """
           Methode permettant d'effectuer une copie complète
           d'une etape (y compris concept produit, elements internes)
           Si l'argument parent est fourni, la nouvelle etape
           aura cet objet comme parent.
        """
        new_etape = self.copy()
        new_etape.copy_reuse(self)
        new_etape.copy_sdnom(self)
        if parent:
            new_etape.reparent(parent)
        if self.sd:
            new_sd = self.sd.__class__(etape=new_etape)
            new_etape.sd = new_sd
            if self.reuse == None:
                new_etape.parent.NommerSdprod(new_sd, self.sd.nom)
            else:
                new_sd.set_name(self.sd.nom)
        new_etape.copy_intern(self)
        return new_etape

    def reset_jdc(self, new_jdc):
        """
           Reinitialise le nommage du concept de l'etape lors d'un changement de jdc
        """
        if self.sd and self.reuse == None:
            self.parent.NommerSdprod(self.sd, self.sd.nom)

    def is_include(self):
        """Permet savoir si on a affaire a la commande INCLUDE
        car le comportement de ces macros est particulier.
        """
        return self.nom.startswith('INCLUDE')

    def sd_accessible(self):
        """Dit si on peut acceder aux "valeurs" (jeveux) de l'ASSD produite par l'etape.
        """
        if CONTEXT.debug:
            print(('`- ETAPE sd_accessible :', self.nom))
        return self.parent.sd_accessible()

    def get_concept(self, nomsd):
        """
            Methode pour recuperer un concept a partir de son nom
        """
        # pourrait etre appelee par une commande fortran faisant appel a des fonctions python
        # on passe la main au parent
        return self.parent.get_concept(nomsd)
