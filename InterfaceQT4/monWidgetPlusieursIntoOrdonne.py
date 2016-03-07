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
import string,types,os,sys

# Modules Eficas
from feuille                import Feuille
from desWidgetPlusieursIntoOrdonne import Ui_WidgetPlusieursIntoOrdonne 
from politiquesValidation   import PolitiquePlusieurs
from qtSaisie               import SaisieValeur
from gereListe              import GereListe
from gereListe              import GerePlie
from gereListe              import LECustom
from gereListe              import MonLabelListeClic

from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets  import Qicon, QScrollbar, QFrame, QApplication
    from PyQt5.QtCore import QTimer, QSize, Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import 


class MonWidgetPlusieursIntoOrdonne (Ui_WidgetPlusieursIntoOrdonne, Feuille,GereListe,GerePlie):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        #print "MonWidgetPlusieursInto", nom, self
        self.nomLine="LEResultat"
        self.listeLE=[]
        self.ouAjouter=0
        self.NumLineEditEnCours=0
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parent,commanme)
        GereListe.__init__(self)
        self.finCommentaireListe()
        self.gereIconePlier()
        try :
          self.maCommande.listeAffichageWidget.append(self.lineEditVal1)
        except :
          # cas ou on ne peut rien ajouter
          pass 
        self.prepareListeResultat()
        self.adjustSize()
        if sys.platform[0:5]!="linux":
          repIcon=self.node.editor.appliEficas.repIcon
          fichier=os.path.join(repIcon, 'arrow_up.png')
          icon = QIcon(fichier)
          self.RBHaut.setIcon(icon)
          self.RBHaut.setIconSize(QSize(32, 32))
          fichier2=os.path.join(repIcon, 'arrow_down.png')
          icon2 = QIcon(fichier2)
          self.RBBas.setIcon(icon2)
        self.parentQt.commandesLayout.insertWidget(-1,self)

       
  def prepareListeResultat(self):
       print "prepareListeResultat"
       for i in self.listeLE: i.close()
       self.listeLE=[]
       self.vScrollBar = self.scrollArea.verticalScrollBar()
       listeValeursCourantes=self.node.item.GetListeValeurs()
       if hasattr(self.node.item.definition.validators,'set_MCSimp'):
            obj=self.node.item.getObject()
            self.node.item.definition.validators.set_MCSimp(obj)
            if self.node.item.isvalid() == 0 :
               liste=[]
               for item in listeValeursCourantes:
                   if self.node.item.definition.validators.verif_item(item)==1: liste.append(item)
               self.listeAAfficher=self.node.item.get_liste_possible(liste)
            else: 
               self.listeAAfficher=self.node.item.get_liste_possible([])
       else :
            self.listeAAfficher=self.node.item.get_liste_possible(listeValeursCourantes)

       if self.listeAAfficher==[] : 
          self.ajoutLE(0)
          return
       if len(self.listeAAfficher)*20 > 400 : self.setMinimumHeight(400)
       else : self.setMinimumHeight(len(self.listeAAfficher)*30)

       self.politique=PolitiquePlusieurs(self.node,self.editor)
       for i in range(1,len(self.listeAAfficher)+1): self.ajoutLE(i)
       for i in range(len(self.listeAAfficher)):
           nomLE="lineEditVal"+str(i+1)
           courant=getattr(self,nomLE)
           courant.setText(str(self.listeAAfficher[i]))
       self.vScrollBar.triggerAction(QScrollBar.SliderToMinimum)
       
      
  def setValeurs(self):
       listeValeursCourantes=self.node.item.GetListeValeurs()
       if self.monSimpDef.max == "**" : aConstruire=7
       else                           : aConstruire=self.monSimpDef.max
       if len(listeValeursCourantes) > aConstruire : aConstruire=len(listeValeursCourantes)
       for i in range(1,aConstruire+1): self.ajoutLEResultat(i)
       self.indexDernierLabel=aConstruire
       index=1
       for val in listeValeursCourantes :
          nomLE="LEResultat"+str(index)
          courant=getattr(self,nomLE)
          courant.setText(str(val))
          courant.setReadOnly(True)
          index=index+1
       self.prepareListeResultat()

  def moinsPushed(self):
      self.ouAjouter=self.ouAjouter-1
      GereListe.moinsPushed(self)
      self.setValeurs()


  def ajoutLEResultat (self,index,valeur=None):
      nomLE="LEResultat"+str(index)
      if hasattr(self,nomLE) : return
      nouveauLE = LECustom(self.scrollAreaRE,self,index)
      nouveauLE.setFrame(False)
      self.CBChoisis.insertWidget(self.ouAjouter,nouveauLE)
      self.ouAjouter=self.ouAjouter+1
      nouveauLE.setText("")
      nouveauLE.setReadOnly(True)
      if index % 2 == 1 : nouveauLE.setStyleSheet("background:rgb(210,210,210)")
      else :	          nouveauLE.setStyleSheet("background:rgb(240,240,240)")
      self.vScrollBarRE = self.scrollAreaRE.verticalScrollBar()
      self.vScrollBarRE.triggerAction(QScrollBar.SliderToMaximum)
      setattr(self,nomLE,nouveauLE)
      self.estVisibleRE=nouveauLE
      if valeur != None : 
         nouveauLE.setText(valeur)
      
  def ajoutLE(self,index,valeur=None):
      nomLE="lineEditVal"+str(index)
      nouveauLE = MonLabelListeClic(self)
      #self.CBLayout.addWidget(nouveauLE)
      self.CBLayout.insertWidget(index -1,nouveauLE)
      self.listeLE.append(nouveauLE)
      nouveauLE.setFrameShape(QFrame.NoFrame)
      QApplication.processEvents()
      nouveauLE.setText("")
      if index % 2 == 1 : nouveauLE.setStyleSheet("background:rgb(210,210,210)")
      else :	          nouveauLE.setStyleSheet("background:rgb(240,240,240)")
      self.vScrollBar.triggerAction(QScrollBar.SliderToMaximum)
      nouveauLE.setFocus()
      setattr(self,nomLE,nouveauLE)
      
  def ajoutLineEdit(self):
      self.ajoutLEResultat (self.indexDernierLabel)


  def traiteClicSurLabelListe(self,valeur):
        if valeur == None : return
        liste,validite=SaisieValeur.TraiteLEValeur(self,str(valeur))
        if validite == 0 : return
        if liste ==[]    : return
        listeVal=[]

        listeValeursCourantes=self.node.item.GetListeValeurs()
        min,max = self.node.item.GetMinMax()
        if len(listeValeursCourantes) +1 > max : 
           self.editor.affiche_infos(tr("Nombre maximal de valeurs : ") + str(max),Qt.red)
           return
        else :
           self.editor.affiche_infos(tr(""))

        affiche=False
        for i in range(1,self.indexDernierLabel+1):
           nomLE="LEResultat"+str(i)
           courant=getattr(self,nomLE)
           if str(courant.text())==str("") : 
              courant.setText(valeur)
              courant.setReadOnly(True)
              affiche=True
              self.estVisibleRE=courant
              QTimer.singleShot(1, self.rendVisibleLigneRE)
              break
          
        if affiche == False:
           self.indexDernierLabel = self.indexDernierLabel+1
           self.ajoutLEResultat (self.indexDernierLabel,str(valeur))
           self.vScrollBarRE.triggerAction(QScrollBar.SliderToMaximum)
           QTimer.singleShot(1, self.rendVisibleLigneRE)
        self.changeValeur()
        self.setValeurs()

  def changeValeur(self,changeDePlace=False,oblige=False):
#PN les 2 arg sont pour que la signature de ma fonction soit identique a monWidgetPlusieursBase
        listeVal=[]
        for i in range(1,self.indexDernierLabel+1):
           nomLE="LEResultat"+str(i)
           courant=getattr(self,nomLE)
           valeur=courant.text()
           if str(valeur)=="" : continue
           liste,validite=SaisieValeur.TraiteLEValeur(self,str(valeur))
           listeVal.append(str(valeur))

        validite,comm,comm2,listeRetour=self.politique.AjoutValeurs(listeVal,-1,[])
        

        listeValeursCourantes=self.node.item.GetListeValeurs()
        min,max = self.node.item.GetMinMax()
        if len(listeValeursCourantes) < min : 
           self.editor.affiche_infos(tr("Nombre minimal de valeurs : ") + str(min),Qt.red)
        else :
           self.editor.affiche_infos("")
    
        if len(listeRetour) == 0 :
           self.node.item.set_valeur(None)
        elif validite :
           self.node.item.set_valeur(listeRetour)
        else :
           commentaire=comm+" "+comm2
           self.editor.affiche_infos(commentaire,Qt.red)
        self.setValide()
#
  def rendVisibleLigneRE(self):
      QApplication.processEvents()
      self.estVisibleRE.setFocus()
      self.scrollArea.ensureWidgetVisible(self.estVisibleRE,0,0)
#


