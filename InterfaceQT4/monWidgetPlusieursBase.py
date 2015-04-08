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

from feuille                import Feuille
from desWidgetPlusieursBase import Ui_WidgetPlusieursBase 
from politiquesValidation   import PolitiquePlusieurs
from qtSaisie               import SaisieValeur
from gereListe              import GereListe
from gereListe              import LECustom

dicoLongueur={2:95,3:125,4:154,5:183,6:210}
hauteurMax=253

class MonWidgetPlusieursBase (Ui_WidgetPlusieursBase,Feuille,GereListe):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        #print "MonWidgetPlusieursBase", nom
        self.inInit=True
        self.indexDernierLabel=0
        self.listeAffichageWidget=[]
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        GereListe.__init__(self)
        self.connect(self.BSelectFichier,SIGNAL("clicked()"), self.selectInFile)

        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        if self.monSimpDef.max != "**"  and self.monSimpDef.max < 7: 
           hauteur=dicoLongueur[self.monSimpDef.max]
           self.resize(self.width(),hauteur)
           self.setMinimumHeight(hauteur)
           if self.monSimpDef.max == self.monSimpDef.min : self.setMaximumHeight(hauteur)
        else :
           self.resize(self.width(),hauteurMax)
           self.setMinimumHeight(hauteurMax)
        self.parentQt.commandesLayout.insertWidget(1,self)
        self.maCommande.listeAffichageWidget.append(self.lineEditVal1)
        self.AAfficher=self.lineEditVal1
        self.inInit=False


  def setValeurs(self):
       print "je passe dans SetValeur"
       self.vScrollBar = self.scrollArea.verticalScrollBar()
       self.politique=PolitiquePlusieurs(self.node,self.editor)
       # construction du min de valeur a entrer
       if self.monSimpDef.max == "**" : aConstruire=7
       else                           : aConstruire=self.monSimpDef.max
       for i in range(1,aConstruire):
           self.ajoutLineEdit()
       qApp.processEvents()
       self.scrollArea.ensureWidgetVisible(self.lineEditVal1)
       self.listeValeursCourantes=self.node.item.GetListeValeurs()
       index=1
       for valeur in self.listeValeursCourantes :
           val=self.politique.GetValeurTexte(valeur)
           nomLineEdit="lineEditVal"+str(index)
           if hasattr(self,nomLineEdit) : 
              courant=getattr(self,nomLineEdit)
              courant.setText(str(val))
           else :
              self.ajoutLineEdit(val)
           index=index+1
       # ajout d'une ligne vide ou affichage commentaire
       if self.indexDernierLabel < self.monSimpDef.max  : self.ajoutLineEdit()
       else : self.scrollArea.setToolTip('nb max de valeurs atteint')
       #self.vScrollBar.triggerAction(QScrollBar.SliderToMinimum)
       

  def ajoutLineEdit(self,valeur=None):
      self.indexDernierLabel=self.indexDernierLabel+1
      nomLineEdit="lineEditVal"+str(self.indexDernierLabel)
      if hasattr(self,nomLineEdit) : 
         self.indexDernierLabel=self.indexDernierLabel-1
         return
      nouveauLE = LECustom(self.scrollArea,self,self.indexDernierLabel)
      self.verticalLayoutLE.insertWidget(self.indexDernierLabel-1,nouveauLE)
      nouveauLE.setText("")
      if self.indexDernierLabel % 2 == 1 : nouveauLE.setStyleSheet("background:rgb(210,210,210)")
      else :	                           nouveauLE.setStyleSheet("background:rgb(235,235,235)")
      nouveauLE.setFrame(False)
      self.connect(nouveauLE,SIGNAL("returnPressed()"),self.changeValeur)
      setattr(self,nomLineEdit,nouveauLE)
      self.listeAffichageWidget.append(nouveauLE)
      self.etablitOrdre()
      if valeur != None : nouveauLE.setText(str(valeur))
      # deux lignes pour que le ensureVisible fonctionne
      self.estVisible=nouveauLE
      if self.inInit==False :QTimer.singleShot(1, self.rendVisibleLigne)

  def etablitOrdre(self):
      i=0
      while(i +1 < len(self.listeAffichageWidget)):
         self.listeAffichageWidget[i].setFocusPolicy(Qt.StrongFocus)
         self.setTabOrder(self.listeAffichageWidget[i],self.listeAffichageWidget[i+1])
         i=i+1
      # si on boucle on perd l'ordre



  def rendVisibleLigne(self):
      #PNPNP
      return
      qApp.processEvents()
      self.estVisible.setFocus()
      self.scrollArea.ensureWidgetVisible(self.estVisible,0,0)
      

  def finCommentaire(self):
        commentaire=""
        mc = self.node.item.get_definition()
        d_aides = { 'TXM' : 'chaines de caracteres',
                  'R'   : 'reels',
                  'I'   : 'entiers',
                  'C'   : 'complexes'}
        type = mc.type[0]
        if not d_aides.has_key(type) :
           if mc.min == mc.max:
               commentaire=tr("Entrez ")+str(mc.min)+tr(" valeurs ")
           else :
               commentaire=tr("Entrez entre ")+str(mc.min)+tr(" et ")+str(mc.max)+tr(" valeurs ")
        else :
           if mc.min == mc.max:
               commentaire=tr("Entrez ")+str(mc.min)+" "+tr(d_aides[type])
           else :
               commentaire=tr("Entrez entre ")+str(mc.min)+(" et  ")+str(mc.max) +" " +tr(d_aides[type])
        aideval=self.node.item.aide()
        commentaire=commentaire + "   " + QString.toUtf8(QString(aideval))
        return str(commentaire)

  def ajout1Valeur(self,valeur=None):
        if valeur == None : return
        liste,validite=SaisieValeur.TraiteLEValeur(self,str(valeur))
        if validite == 0 : return
        if liste ==[]    : return
        listeVal=[]
        for valeur in self.listeValeursCourantes : listeVal.append(valeur)
        validite,comm,comm2,listeRetour=self.politique.AjoutValeurs(liste,-1,listeVal)
        if (comm2 != "" and comm != None) : return comm2
        if validite : 
           self.listeValeursCourantes=self.listeValeursCourantes+listeRetour
           if len(self.listeValeursCourantes) > self.monSimpDef.min :
              self.node.item.set_valeur(self.listeValeursCourantes)
              self.reaffiche()
           return None
        else :
           return(comm2+" "+comm)
        


  def changeValeur(self,changeDePlace=True):
      print 'ds chge valeur'
      donneFocus=None
      derniereValeur=None
      self.listeValeursCourantes = []
      for i in range (1, self.indexDernierLabel+1):
          nomLineEdit="lineEditVal"+str(i)
          courant=getattr(self,nomLineEdit)
          valeur=courant.text()
          if valeur != None and valeur != "" : 
             commentaire=self.ajout1Valeur(valeur)
             if (commentaire != None ):
                 self.editor.affiche_infos(commentaire,Qt.red)
                 courant.setText("")
                 donneFocus=courant
          elif donneFocus==None : donneFocus=courant
      nomDernierLineEdit="lineEditVal"+str(self.indexDernierLabel)
      dernier=getattr(self,nomDernierLineEdit)
      derniereValeur=dernier.text()
      if changeDePlace:
         if donneFocus != None : 
           donneFocus.setFocus()
           self.scrollArea.ensureWidgetVisible(donneFocus)
         elif self.indexDernierLabel < self.monSimpDef.max  : 
           self.ajoutLineEdit()
      if  self.indexDernierLabel == self.monSimpDef.max  :
        self.editor.affiche_infos('nb max de valeurs atteint')
      if self.listeValeursCourantes == [] : return
      min,max = self.node.item.GetMinMax()
      if len(self.listeValeursCourantes) > max : return
      if len(self.listeValeursCourantes) < min : return
      self.node.item.set_valeur(self.listeValeursCourantes)
      self.setValide()
      self.reaffiche()

          

# Avertissement quand on quitte le widget
