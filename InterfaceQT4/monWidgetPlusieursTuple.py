# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
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
import string,types,os

# Modules Eficas
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

from feuille               import Feuille
from politiquesValidation  import PolitiquePlusieurs
from qtSaisie              import SaisieValeur
from gereListe             import GereListe
from gereListe             import LECustom
from Tuple2                import Ui_Tuple2
from Tuple3                import Ui_Tuple3


class TupleCustom :
  def __init__(self,tailleTuple,parent,parentQt,index):
      QWidget.__init__(self,parent)
      self.setupUi(self)
      self.tailleTuple=tailleTuple
      self.parent=parent
      self.parentQt=parentQt
      self.valeur=None
      self.index=index

      for i in range(self.tailleTuple):
         nomLE="lineEditVal_"+str(i+1)
         courant=getattr(self,nomLE)
         courant.num=index
         courant.dansUnTuple=True
         self.connect(courant,SIGNAL("returnPressed()"),self.valueChange)


  def valueChange(self):
      listeVal=[]
    
      for i in range(self.tailleTuple):
         nomLE="lineEditVal_"+str(i+1)
         courant=getattr(self,nomLE)
         val=str(courant.text())
         if str(val)=="" or val==None : 
            courant.setFocus()
            return
         try :
             valeur=eval(val,{})
         except :
           try :
             d=self.parentQt.objSimp.jdc.get_contexte_avant(self.parentQt.objSimp. etape)
             valeur=eval(val,d)
           except :
             valeur=val
         listeVal.append(valeur)
      self.valeur=listeVal
      self.parentQt.changeValeur()


  def setValeur(self,value):
      listeVal=[]
      valeurNulle=True
      for i in range(self.tailleTuple):
         nomLE="lineEditVal_"+str(i+1)
         courant=getattr(self,nomLE)
         try :
           if str(value[i]) != "" : valeurNulle=False
         except :
           pass
         
         courant.setText(str(value[i]))
         val=str(courant.text())
         try :
           valeur=eval(val,{})
         except :
           try :
             d=self.parentQt.objSimp.jdc.get_contexte_avant(self.parentQt.objSimp. etape)
             valeur=eval(val,d)
           except :
             valeur=val
         listeVal.append(valeur)
      if  valeurNulle == True : self.valeur=None
      else                    : self.valeur=listeVal

  def getValeur(self):
      return self.valeur

  def clean(self):
      self.valeur=None
      for i in range(self.tailleTuple):
         nomLE="lineEditVal_"+str(i+1)
         courant=getattr(self,nomLE)
         courant.setText("")

class TupleCustom2(QWidget,Ui_Tuple2,TupleCustom):
  def __init__(self,tailleTuple,parent,parentQt,index):
      TupleCustom.__init__(self,tailleTuple,parent,parentQt,index)

class TupleCustom3(QWidget,Ui_Tuple3,TupleCustom):
  def __init__(self,tailleTuple,parent,parentQt,index):
      TupleCustom. __init__(self,tailleTuple,parent,parentQt,index)
      
# ---------------------------- #


class MonWidgetPlusieursTuple(Feuille,GereListe):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        self.indexDernierLabel=0
        self.NumLineEditEnCours=0
        self.nomLine="TupleVal"
        self.listeAffichageWidget=[]
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        GereListe.__init__(self)
        self.politique=PolitiquePlusieurs(self.node,self.editor)
        self.parentQt.commandesLayout.insertWidget(-1,self)

  def ajoutLineEdit(self,valeur=None,inInit=False):
      self.indexDernierLabel=self.indexDernierLabel+1
      nomLineEdit=self.nomLine+str(self.indexDernierLabel)
      if hasattr(self,nomLineEdit) :
         self.indexDernierLabel=self.indexDernierLabel-1
         return

      if self.nbValeurs == 2 : nouveauLE = TupleCustom2(self.nbValeurs,self.scrollArea,self,self.indexDernierLabel)
      else                   : nouveauLE = TupleCustom3(self.nbValeurs,self.scrollArea,self,self.indexDernierLabel)
                 
      self.verticalLayoutLE.insertWidget(self.indexDernierLabel-1,nouveauLE)
      setattr(self,nomLineEdit,nouveauLE)
      if valeur != None : nouveauLE.setValeur(valeur)

      self.listeAffichageWidget.append(nouveauLE.lineEditVal_1)
      self.listeAffichageWidget.append(nouveauLE.lineEditVal_2)
      if self.nbValeurs == 3 : self.listeAffichageWidget.append(nouveauLE.lineEditVal_3)
      self.etablitOrdre()

      # deux lignes pour que le ensureVisible fonctionne
      self.estVisible=nouveauLE.lineEditVal_1
      if inInit==False :QTimer.singleShot(1, self.rendVisibleLigne)

  def etablitOrdre(self):
      i=0
      while(i +1 < len(self.listeAffichageWidget)):
         self.listeAffichageWidget[i].setFocusPolicy(Qt.StrongFocus)
         self.setTabOrder(self.listeAffichageWidget[i],self.listeAffichageWidget[i+1])
         i=i+1


  def setValeurs(self):
       valeurs=self.node.item.get_valeur()
       min,max=self.node.item.GetMinMax()
       if max == "**" or max > 5 : aCreer=5
       else : aCreer=max 

       if valeurs == () or valeurs == None :
          for i in range(aCreer): self.ajoutLineEdit(inInit=True)
          return

       for v in valeurs:
           self.ajoutLineEdit(v,inInit=True)

       for i in range(len(valeurs),aCreer) : self.ajoutLineEdit(inInit=True)

  def rendVisibleLigne(self):
      qApp.processEvents()
      self.estVisible.setFocus(True)
      self.scrollArea.ensureWidgetVisible(self.estVisible,0,0)

   
  def changeValeur(self,changeDePlace=False,oblige=True):
      #Pour compatibilite signature
      aLeFocus=self.focusWidget()
      listeComplete=[]

      libre=False
      for i in range(self.indexDernierLabel) :
          nom=self.nomLine+str(i+1)
          courant=getattr(self,nom)
          valeurTuple=courant.valeur
          if valeurTuple == None or valeurTuple== "": 
             libre=True
             continue
          validite,comm,comm2,listeRetour= self.politique.AjoutTuple(valeurTuple,listeComplete)
          if not validite:
             if comm2 != '' : comm += " " + comm2
             self.editor.affiche_infos(comm+" "+str(self.objSimp.definition.validators.typeDesTuples),Qt.red)
             return
          listeComplete.append(tuple(courant.valeur))
      if listeComplete == [] : listeComplete=None
      self.node.item.set_valeur(listeComplete)

      if changeDePlace : return
      min,max=self.node.item.GetMinMax()
      if self.indexDernierLabel == max  : self.editor.affiche_infos(tr('Nb maximum de valeurs atteint'))
      if self.indexDernierLabel < max and libre==False :
          self.ajoutLineEdit()
          self.listeAffichageWidget[-2].setFocus(True)
      else :
         try :
           qApp.processEvents()
           w=self.listeAffichageWidget[self.listeAffichageWidget.index(aLeFocus)+1]
           w.setFocus(True)
           self.scrollArea.ensureWidgetVisible(w,0,0)
         except :
           pass
          
