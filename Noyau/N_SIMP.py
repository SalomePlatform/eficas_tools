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


""" Ce module contient la classe de definition SIMP
    qui permet de spécifier les caractéristiques des mots clés simples
"""

from __future__ import absolute_import
import types

from Noyau import N_ENTITE
from Noyau import N_MCSIMP


class SIMP(N_ENTITE.ENTITE):

    """
     Classe pour definir un mot cle simple

     Cette classe a deux attributs de classe

     - class_instance qui indique la classe qui devra etre utilisée
             pour créer l'objet qui servira à controler la conformité d'un
             mot-clé simple avec sa définition

     - label qui indique la nature de l'objet de définition (ici, SIMP)

    """
    class_instance = N_MCSIMP.MCSIMP
    label = 'SIMP'

    def __init__(self, typ,ang="", fr="", statut='f', into=None, intoSug = None,siValide = None, defaut=None,
                 min=1, max=1, homo=1, position='local',
                 val_min=float('-inf'), val_max=float('inf'), docu="", validators=None,
                 sug=None,fenetreIhm=None):
        """
            Un mot-clé simple est caractérisé par les attributs suivants :
            - type : cet attribut est obligatoire et indique le type de valeur attendue
            - fr : chaîne documentaire en français
            - statut : obligatoire ou facultatif ou caché
            - into : valeurs autorisées
            - intoSug : valeurs possibles mais des valeurs autres du bon type peuvent etre entrees par l utilsateur
            - defaut : valeur par défaut
            - min : nombre minimal de valeurs
            - max : nombre maximal de valeurs
            - homo : un certatin nb de choses qui il faut redispacher ailleurs (information, constant)
            - ang : doc
            - position : si global, le mot-clé peut-être lu n'importe où dans la commande
            - val_min : valeur minimale autorisée
            - val_max : valeur maximale autorisée
            - docu : clef sur de la documentation utilisateur
            - sug : valeur suggere
            - fenetreIhm=None 
        """
        #print (self)
        #import traceback
        #traceback.print_stack()
        #print (self)
        N_ENTITE.ENTITE.__init__(self, validators)
        # Initialisation des attributs
        if type(typ) == tuple:
            self.type = typ
        else:
            self.type = (typ,)
        self.fr = fr
        self.statut = statut
        self.into = into
        self.intoSug = intoSug
        self.siValide = siValide
        self.defaut = defaut
        self.min = min
        self.max = max
        self.homo = homo
        self.position = position
        self.val_min = val_min
        self.val_max = val_max
        self.docu = docu
        self.sug = sug
        self.ang=ang
        if self.max     == '**' : self.max     = float('inf')
        if self.val_max == '**' : self.val_max = float('inf')
        if self.min     == '**' : self.min     = float('-inf')
        if self.val_min == '**' : self.val_min = float('-inf')
        self.fenetreIhm=fenetreIhm
        #self.creeT_SIMP()

    def verifCata(self):
        """
            Cette methode sert à valider les attributs de l'objet de définition
            de la classe SIMP
        """
        self.checkMinMax()
        self.checkFr()
        self.checkStatut()
        self.checkHomo()
        self.checkInto()
        self.checkPosition()
        self.checkValidators()

    def __call__(self, val, nom, parent=None, objPyxbDeConstruction = None):
        """
            Construit un objet mot cle simple (MCSIMP) a partir de sa definition (self)
            de sa valeur (val), de son nom (nom) et de son parent dans l arboresence (parent)
        """
        return self.class_instance(nom=nom, definition=self, val=val, parent=parent, objPyxbDeConstruction=objPyxbDeConstruction)

#    def creeT_SIMP(self):
#        from Efi2Xsd.readerEfficas import monSIMP
#        from Efi2Xsd.mapDesTypes import dictSIMPEficasXML
#        self.objXML=monSIMP()
#        for nomEficasArg in dictSIMPEficasXML :
#           argu=getattr(self,nomEficasArg)
#           nomXMLarg=dictSIMPEficasXML[nomEficasArg]
#           if not isinstance(nomXMLarg, (list, tuple)) :
#              print(nomXMLarg, argu)
              #if nomEficasArg  in listeParamDeTypeTypeAttendu:
              #   typeAttendu = self.typ
#                 
#              setattr(self.objXML, nomXMLarg, argu)
           


# for nomXMLArg in dir(self) :
#          if nomXMLArg in self.dictATraiter :
#              nomEficasArg=self.dictATraiter[nomXMLArg]
#              argu=getattr(self,nomXMLArg)
#              if argu==None : continue
#
#              if type(nomEficasArg) == types.DictionaryType:
#                 for nomXML in list(nomEficasArg.keys()):
#                      arguDecoupe=getattr(argu,nomXML)
#                      nomEficasDecoupe=nomEficasArg[nomXML]
#                      if arguDecoupe == None : continue
#                      self.dictArgsEficas[nomEficasDecoupe]=arguDecoupe
#              else :
#                self.dictArgsEficas[nomEficasArg] = argu
#
# 
#        
#       
#
