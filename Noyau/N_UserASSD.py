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

"""

from __future__ import absolute_import
from __future__ import print_function
try :
  from builtins import object
except : pass
import traceback
import sys

from .N_ASSD import ASSD

class UserASSD(ASSD):
    """
       Classe de base pour definir des types de structures de donnees definie par 
       l utilisateur
       equivalent d un concept ASSD pour un SIMP ou un FACT
       Attention : le parent est a None au debut  et non le MC createur que l on ne connait pas
       Lorsqu on ecrit le jdc, n ecrit nom=UserASSD()
       le parent est le SIMP qui cree l objet
       a la lecture si la classe commence par un majuscule on fait le boulot dans MCSIMP, sinon dans
       l init de parametre car le parsing considere qu on a un parametre
    """

    def __init__(self,nom='sansNom'):
       self.nom    = nom
       self.jdc    = CONTEXT.getCurrentJdC()
       self.parent = None 
       self.initialiseValeur()
       self.utilisePar = set()
       if self.nom  != 'sansNom' : self.id = self.jdc.regSD(self)
       else : self.id = None
       self.ptr_sdj   = None


    def initialiseParent(self, parent):
       #print ('je passe initialiseParent pour : ', self, parent)
       self.parent= parent

    def initialiseNom(self,nom):
       #print ('je passe initialiseNom pour : ', self, nom)
       for (i,j)  in self.jdc.sdsDict.items() :
          if j == self : 
             del(self.jdc.sdsDict[i])
       self.jdc.sdsDict[nom]=self
       self.nom=nom
       if self.nom != 'sansNom' and self.id ==None : self.id = self.jdc.regSD(self)

    def initialiseValeur(self,valeur=None):
       self.valeur=valeur

    def ajoutUtilisePar(self,mc):
       self.utilisePar.add(mc)

    def enleveUtilisePar(self,mc):
       try : self.utilisePar.remove(mc)
       except : pass

    def renomme(self,nouveauNom):
       self.jdc.delConcept(self.nom)
       self.jdc.sdsDict[nouveauNom] = self
       self.setName(nouveauNom)
       #print ('je suis dans renomme',nouveauNom, self.nom)
       #print (self.utilisePar)
       for mc in (self.utilisePar):
           mc.demandeRedessine()
       

    def deleteReference(self):
       print ('dans deleteReference')
       for MC in self.utilisePar : 
           # le delete est appele en cascade par toute la hierachie
           # du mcsimp (au cas ou on detruise le fact ou le proc)
           # du coup pas beau
           try :
              if type(MC.valeur) in (list,tuple): 
                 MC.valeur=list(MC.valeur)
                 while MC in MC.valeur: MC.valeur.remove(self)
                 if MC.valeur == [] : MC.Valeur = None
              else : MC.valeur=None
              MC.state='changed'
              MC.isValid()
              #MC.demandeRedessine()
              self.jdc.delConcept(self.nom)
           except :
              pass

    def getEficasAttribut(self, attribut):
       #print ('je suis dans getEficasAttr', attribut)
       if self.parent == None : return None
       #print ('apres if')
       # parent est le SIMP donc c est bien parent.parent
       try : 
          valeur = self.parent.parent.getMocle(attribut)
       except :
          valeur = None
       #print (valeur)
       return valeur
       
        
    def supprime(self):
        self.deleteReference()
        ASSD.supprime(self)
        
