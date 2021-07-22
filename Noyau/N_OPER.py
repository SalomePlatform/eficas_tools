# coding=utf-8
# Copyright (C) 2007-2021   EDF R&D
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
    Ce module contient la classe de definition OPER
    qui permet de spécifier les caractéristiques d'un opérateur
"""

from __future__ import absolute_import
import types
import traceback

from . import N_ENTITE
from . import N_ETAPE
from . import nommage


class OPER(N_ENTITE.ENTITE):

    """
     Classe pour definir un opérateur

     Cette classe a trois attributs de classe

     - class_instance qui indique la classe qui devra etre utilisée
             pour créer l'objet qui servira à controler la conformité d'un
             opérateur avec sa définition

     - label qui indique la nature de l'objet de définition (ici, OPER)

     - nommage qui est un module Python qui fournit la fonctionnalité de nommage

     et les attributs d'instance suivants :

     - nom   : son nom

     - op   : le numéro d'opérateur

     - sd_prod : le type de concept produit. C'est une classe ou une fonction qui retourne
                       une classe

     - reentrant : vaut 'n' ou 'o'. Indique si l'opérateur est réentrant ou pas. Un opérateur
                         réentrant peut modifier un concept d'entrée et le produire comme concept de sortie

     - repetable : vaut 'n' ou 'o'. Indique si l'opérateur est répetable ou pas. Un opérateur
                         non répétable ne doit apparaitre qu'une fois dans une exécution. C'est du ressort
                         de l'objet gérant le contexte d'exécution de vérifier cette contrainte.

     - fr   : commentaire associé en francais

     - docu : clé de documentation associée

     - regles : liste des règles associées

     - op_init : cet attribut vaut None ou une fonction. Si cet attribut ne vaut pas None, cette
                       fonction est exécutée lors des phases d'initialisation de l'étape associée.

     - niveau : indique le niveau dans lequel est rangé l'opérateur. Les opérateurs peuvent etre
                      rangés par niveau. Ils apparaissent alors exclusivement dans leur niveau de rangement.
                      Si niveau vaut None, l'opérateur est rangé au niveau global.

     - entites : dictionnaire dans lequel sont stockés les sous entités de l'opérateur. Il s'agit
                       des entités de définition pour les mots-clés : FACT, BLOC, SIMP. Cet attribut
                       est initialisé avec args, c'est à dire les arguments d'appel restants.


    """
    class_instance = N_ETAPE.ETAPE
    label = 'OPER'
    nommage = nommage

    def __init__(self, nom, op=None, sd_prod=None, reentrant='n', repetable='o', fr="",ang="",fenetreIhm=None,
                 docu="", regles=(), op_init=None, niveau = None, UIinfo=None, **args):
        """
           Méthode d'initialisation de l'objet OPER. Les arguments sont utilisés pour initialiser
           les attributs de meme nom
        """
        self.nom = nom
        self.op = op
        self.sd_prod = sd_prod
        self.reentrant = reentrant
        self.fr = fr
        self.ang = ang
        self.repetable = repetable
        self.docu = docu
        self.fenetreIhm= fenetreIhm
        if type(regles) == tuple:
            self.regles = regles
        else:
            self.regles = (regles,)
        # Attribut op_init : Fonction a appeler a la construction de l
        # operateur sauf si == None
        self.op_init = op_init
        self.entites = args
        current_cata = CONTEXT.getCurrentCata()
        if niveau == None:
            self.niveau = None
            current_cata.enregistre(self)
        else:
            self.niveau = current_cata.getNiveau(niveau)
            self.niveau.enregistre(self)
        self.UIinfo = UIinfo
        self.affecter_parente()
        self.checkDefinition(self.nom)
        self.txtNomComplet=""
        self.dejaPrepareDump=False

    def __call__(self, reuse=None, nomXML=None,**args):
        """
            Construit l'objet ETAPE a partir de sa definition (self),
            puis demande la construction de ses sous-objets et du concept produit.
        """
        if nomXML == None : nomsd = self.nommage.getNomConceptResultat(self.nom)
        else : nomsd = nomXML
        etape = self.class_instance(oper=self, reuse=reuse, args=args)
        etape.MCBuild()
        while etape.doitEtreRecalculee == True :
            etape.doitEtreRecalculee = False
            etape.deepUpdateConditionBlocApresCreation()
            etape.reConstruitResteVal()
            etape.state='modified'
            #print ('on recalcule la validite depuis N_OPER')
        #   etape.isValid(cr='oui')
        etape.metAJourNomASSD(nomsd)
        return etape.buildSd(nomsd)

    def make_objet(self, mc_list='oui'):
        """
             Cette méthode crée l'objet ETAPE dont la définition est self sans
              l'enregistrer ni créer sa sdprod.
             Si l'argument mc_list vaut 'oui', elle déclenche en plus la construction
             des objets MCxxx.
        """
        etape = self.class_instance(oper=self, reuse=None, args={})
        if mc_list == 'oui':
            etape.MCBuild()
        return etape

    def verifCata(self):
        """
            Méthode de vérification des attributs de définition
        """
        self.checkRegles()
        self.checkFr()
        self.checkReentrant()
        self.checkDocu()
        self.checkNom()
        self.checkOp(valmin=0)
        self.verifCataRegles()

    def supprime(self):
        """
            Méthode pour supprimer les références arrières susceptibles de provoquer
            des cycles de références
        """
        self.niveau = None
