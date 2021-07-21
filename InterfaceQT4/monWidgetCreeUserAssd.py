# -*- coding: utf-8 -*-
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
#
# Modules Python
from __future__ import absolute_import
import types,os


# Modules Eficas
from Extensions.i18n import tr
from .monWidgetSimpTxt  import MonWidgetSimpTxt
from .monWidgetPlusieursBase import MonWidgetPlusieursBase
from copy import copy,deepcopy
from PyQt5.QtCore import Qt


      
class MonWidgetCreeUserAssd ( MonWidgetSimpTxt):
  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
      MonWidgetSimpTxt. __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
      #self.lineEditVal.returnPressed.connect(self.LEValeurAjouteDsPossible)

  def LEvaleurPressed(self):
      try :
        if str(self.lineEditVal.text())=="" or str(self.lineEditVal.text())==None : return
      except : pass
      valeurEntree = str(self.lineEditVal.text())
      if valeurEntree == self.oldValeurTexte : return
      if self.oldValeurTexte == ""  : enCreation = True
      else                          : enCreation = False
      if enCreation : validite,commentaire=self.objSimp.creeUserASSDetSetValeur(valeurEntree)
      else          : validite,commentaire=self.objSimp.renommeSdCree(valeurEntree)
      if not enCreation : self.node.updateNodeTexte()
      #PNPNPN -- signal update sur les fils ou ?
      if commentaire != "" :
         if validite : 
            self.editor.afficheCommentaire(commentaire)
            self.oldValeurTexte = self.lineEditVal.text()
         else  : 
            self.editor.afficheInfos(commentaire,Qt.red)
            self.lineEditVal.setText("")
            self.oldValeurTexte=""
      self.parentQt.propageChange(self.objSimp.definition.type[0])
      
       
class MonWidgetCreeListeUserAssd ( MonWidgetPlusieursBase):
  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
      MonWidgetPlusieursBase. __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
      
  def ajout1Valeur(self,valeur=None):
      if not valeur in list(self.dictValeurs.keys()):
         validite,commentaire=self.objSimp.creeUserASSDetSetValeur(valeur)
         MonWidgetPlusieursBase.ajout1Valeur(self,valeur)

  def changeValeur(self,changeDePlace=False,oblige=False,numero=None):
      #print ('dans changeValeur du CreeUserAssd', changeDePlace,numero)
      self.changeUnLineEdit=False
      if numero==None : 
           self.echangeDeuxValeurs()
           return
      valeur = self.lineEditEnEdition.text()
      #print (valeur)
      if numero in list(self.dictLE.keys()) :
         oldValeurUserAssd = self.dictLE[numero] 
         if oldValeurUserAssd == None or oldValeurUserAssd == "" : enCreation = True
         else : enCreation = False
      else                         : 
         enCreation     = True
         oldValeurUserAssd =  ""
      #print ('je traite')
      if enCreation : validite, objASSD, commentaire=self.objSimp.creeUserASSD(valeur)
      elif oldValeurUserAssd.nom == valeur : return
      else :  
         validite, commentaire=self.node.item.renommeSdCreeDsListe(oldValeurUserAssd,valeur)
         nomDernierLineEdit="lineEditVal"+str(numero+1)
         dernier=getattr(self,nomDernierLineEdit)
         dernier.setFocus()
         return
  
      if commentaire != "" and not validite:
            self.editor.afficheInfos(commentaire,Qt.red)
            self.lineEditEnEdition.setText("")
            return
      # on relit tout pour tenir compte des lignes blanches 
      liste=[]
      for i in range (1, self.indexDernierLabel+1):
          if i == numero : liste.append(objASSD)
          if i in list(self.dictLE.keys()) :
             if self.dictLE[i] != None and self.dictLE[i] != "" : liste.append(self.dictLE[i])
      self.node.item.object.state='changed'
      validite=self.node.item.setValeur(liste)
      self.setValide()
      validite=self.node.item.isValid()
      if validite : 
         self.dictLE[numero] = objASSD
         self.node.item.rattacheUserASSD(objASSD)
         if self.indexDernierLabel < len(liste)  : self.ajoutLineEdit()
         nomDernierLineEdit="lineEditVal"+str(numero+1)
         self.listeValeursCourantes=liste
         dernier=getattr(self,nomDernierLineEdit)
         dernier.setFocus()
      else : 
         self.editor.afficheInfos('ajout impossible' ,Qt.red)
         if objASSD : objASSD.supprime()
         self.lineEditEnEdition.setText("")
      self.parentQt.propageChange(self.objSimp.definition.type[0])


  def leaveEventScrollArea(self,event):
      pass

  def echangeDeuxValeurs(self):
      self.changeUnLineEdit=False
      obj1=self.dictLE[self.num1] 
      obj2=self.dictLE[self.num2] 
      self.dictLE[self.num1]=obj2
      self.dictLE[self.num2]=obj1
      nomLineEdit=self.nomLine+str(self.num1)
      courant=getattr(self,nomLineEdit)
      if self.dictLE[self.num1] != None : courant.setText(self.dictLE[self.num1].nom)
      else : courant.setText("")
      nomLineEdit=self.nomLine+str(self.num2)
      courant=getattr(self,nomLineEdit)
      if self.dictLE[self.num2] != None : courant.setText(self.dictLE[self.num2].nom)
      else : courant.setText("")
      liste=[]
      for i in list(self.dictLE.keys()): 
             if self.dictLE[i] != None and self.dictLE[i] != "" : liste.append(self.dictLE[i])
      validite=self.node.item.setValeur(liste)
      courant.setFocus(True)

  def descendLesLignes(self):
      self.changeUnLineEdit=False
      if self.numlineEditEnCours==self.indexDernierLabel : return
      nouvelleValeur=None
      for i in range (self.numlineEditEnCours+1, self.indexDernierLabel):
             valeurAGarder=self.dictLE[i]
             self.dictLE[i]=nouvelleValeur
             nomLineEdit=self.nomLine+str(i)
             courant=getattr(self,nomLineEdit)
             if nouvelleValeur != None : courant.setText(nouvelleValeur.nom)
             else : courant.setText("")
             nouvelleValeur=valeurAGarder
      

  def moinsPushed(self):
     if self.numlineEditEnCours == 0 : return
     if self.indexDernierLabel == 0 : return
     objASSD=self.dictLE[self.numlineEditEnCours]
     if objASSD : objASSD.supprime()
     self.lineEditEnEdition.setText("")

     #self.dictLE.pop(self.numlineEditEnCours)
     for i in range (self.numlineEditEnCours, self.indexDernierLabel-1):
             self.dictLE[i]= self.dictLE[i+1]
             nomLineEdit=self.nomLine+str(i)
             courant=getattr(self,nomLineEdit)
             if self.dictLE[i] != None : courant.setText(self.dictLE[i].nom)
             else : courant.setText("")
     nomLineEdit=self.nomLine+str(self.indexDernierLabel)
     courant=getattr(self,nomLineEdit)
     courant.setText("")
     self.dictLE[self.indexDernierLabel]=None
     liste=[]
     for i in list(self.dictLE.keys()): 
          if self.dictLE[i] != None and self.dictLE[i] != "" : liste.append(self.dictLE[i])
     validite=self.node.item.setValeur(liste)

