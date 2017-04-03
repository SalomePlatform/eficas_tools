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
from __future__ import absolute_import
try :
   from builtins import str
   from builtins import range
   from builtins import object
except : pass

import types,os,sys

from six.moves import range
from PyQt5.QtGui     import QIcon 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore    import QTimer, QSize, Qt

# Modules Eficas
from Extensions.i18n import tr

from .feuille                import Feuille
from desWidgetPlusieursBase import Ui_WidgetPlusieursBase 
from .politiquesValidation   import PolitiquePlusieurs
from .qtSaisie               import SaisieValeur
from .gereListe              import GereListe
from .gereListe              import GerePlie
from .gereListe              import LECustom

dicoLongueur={2:95,3:125,4:154,5:183,6:210,float('inf'):210}
hauteurMax=253

class MonWidgetPlusieursBase (Ui_WidgetPlusieursBase,Feuille,GereListe,GerePlie):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        #print "MonWidgetPlusieursBase", nom
        self.nomLine="lineEditVal"
        self.inInit=True
        self.indexDernierLabel=0
        self.NumLineEditEnCours=0
        self.listeAffichageWidget=[]
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        GereListe.__init__(self)
        self.gereIconePlier()
        self.BSelectFichier.clicked.connect(self.selectInFile)

        if sys.platform[0:5]!="linux":
          repIcon=self.node.editor.appliEficas.repIcon
          fichier=os.path.join(repIcon, 'arrow_up.png')
          icon = QIcon(fichier)
          self.RBHaut.setIcon(icon)
          self.RBHaut.setIconSize(QSize(32, 32))
          fichier2=os.path.join(repIcon, 'arrow_down.png')
          icon2 = QIcon(fichier2)
          self.RBBas.setIcon(icon2)
          fichier3=os.path.join(repIcon, 'file-explorer.png')
          icon3 = QIcon(fichier2)
          self.BSelectFichier.setIcon(icon3)
          self.BSelectFichier.setIconSize(QSize(32, 32))

        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        self.monSimpDef.max = 3
        if self.monSimpDef.max != "**"  and self.monSimpDef.max < 7: 
           hauteurMax=dicoLongueur[self.monSimpDef.max]
        else :
           hauteurMax=220
        #   if self.monSimpDef.max == self.monSimpDef.min : self.setMaximumHeight(hauteur)
        self.resize(self.width(),hauteurMax)
        self.setMinimumHeight(hauteurMax)
        self.finCommentaireListe()
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.maCommande.listeAffichageWidget.append(self.lineEditVal1)
        self.AAfficher=self.lineEditVal1
        self.inInit=False


  def setValeurs(self):
       self.vScrollBar = self.scrollArea.verticalScrollBar()
       self.politique=PolitiquePlusieurs(self.node,self.editor)
       # construction du min de valeur a entrer
       self.monSimpDef.max = 3
       if self.monSimpDef.max == "**"  : aConstruire=7
       elif self.monSimpDef.max == float('inf'): aConstruire=7
       else                            : aConstruire=self.monSimpDef.max
       print ('1,aConstruire', aConstruire)

       for i in range(1,aConstruire):
           self.ajoutLineEdit()
       QApplication.processEvents()
       self.scrollArea.ensureWidgetVisible(self.lineEditVal1)
       self.listeValeursCourantes=self.node.item.GetListeValeurs()
       index=1
       for valeur in self.listeValeursCourantes :
           val=self.politique.GetValeurTexte(valeur)
           nomLineEdit="lineEditVal"+str(index)
           if hasattr(self,nomLineEdit) : 
              courant=getattr(self,nomLineEdit)
              if 'R' in self.objSimp.definition.type and str(val) != repr(val) :  courant.setText(repr(val))
              else                     :  courant.setText(str(val))
           else :
              self.ajoutLineEdit(val)
           index=index+1
       # ajout d'une ligne vide ou affichage commentaire
       if self.indexDernierLabel < self.monSimpDef.max  : self.ajoutLineEdit()
       else : self.scrollArea.setToolTip('nb max de valeurs atteint')
       #self.adjustSize()
       #self.vScrollBar.triggerAction(QScrollBar.SliderToMinimum)
       

  def ajoutLineEdit(self,valeur=None,):
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
      nouveauLE.returnPressed.connect(self.changeValeur)
      setattr(self,nomLineEdit,nouveauLE)
      self.listeAffichageWidget.append(nouveauLE)
      self.etablitOrdre()
      if valeur != None : nouveauLE.setText(str(valeur))
      # deux lignes pour que le ensureVisible fonctionne
      self.estVisible=nouveauLE
      if self.inInit==False :QTimer.singleShot(1, self.rendVisibleLigne)
      #if donneLeFocus==True : nouveauLE.setFocus()

  def etablitOrdre(self):
      i=0
      while(i +1 < len(self.listeAffichageWidget)):
         self.listeAffichageWidget[i].setFocusPolicy(Qt.StrongFocus)
         self.setTabOrder(self.listeAffichageWidget[i],self.listeAffichageWidget[i+1])
         i=i+1
      # si on boucle on perd l'ordre


  def rendVisibleLigne(self):
      QApplication.processEvents()
      self.estVisible.setFocus()
      self.scrollArea.ensureWidgetVisible(self.estVisible,0,0)
      

  def finCommentaire(self):
      return self.finCommentaireListe()

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
        
  def reaffiche(self):
      # A priori, on ne fait rien
      pass

  def ajoutNValeur(self,liste) :
      for val in liste :
         i=1
         ajoute=False
         while i <  self.indexDernierLabel+1:
            nomLineEdit="lineEditVal"+str(i)
            courant=getattr(self,nomLineEdit)
            valeur=courant.text()
            if valeur == None or valeur == "" :
              ajoute=True
              courant.setText(str(val))
              commentaire=self.ajout1Valeur(val)
              if (commentaire != None ):
                 self.editor.affiche_infos(commentaire,Qt.red)
                 courant.setText("")
              break
            else : 
              i=i+1
         if ajoute : continue
         self.ajoutLineEdit(valeur=str(val))
         self.changeValeur()
                

  def changeValeur(self,changeDePlace=True,oblige=False):
      donneFocus=None
      derniereValeur=None
      self.listeValeursCourantes = []
      fin=self.indexDernierLabel
      for i in range (1, fin):
          nomLineEdit="lineEditVal"+str(i)
          courant=getattr(self,nomLineEdit)
          valeur=courant.text()
          lval=valeur.split(',')
          if len (lval) > 1 : 
             courant.setText(lval[0])
             self.ajoutNValeur(lval[1:])
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
                 self.reaffiche()
                 return
             else :
                 self.editor.affiche_infos("")
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
      if self.listeValeursCourantes == [] : return
      min,max = self.node.item.GetMinMax()
      if len(self.listeValeursCourantes) < self.monSimpDef.min  :
        self.editor.affiche_infos(tr('nb min de valeurs : ')+str( self.monSimpDef.min))
      if len(self.listeValeursCourantes) < min and oblige==True: return
      if len(self.listeValeursCourantes) > max : return
      self.node.item.set_valeur(self.listeValeursCourantes)
      if len(self.listeValeursCourantes) == self.monSimpDef.max  :
        self.editor.affiche_infos(tr('nb max de valeurs atteint'))
      self.setValide()
      self.reaffiche()

          
  def entreListe(self,listeDeValeur,index):
             self.entreListe(lval, i)

# Avertissement quand on quitte le widget
