# -*- coding: utf-8 -*-
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
#
# Modules Python
from __future__ import absolute_import
try :
   from builtins import str
   from builtins import range
   from builtins import object
except : pass

import types,os,sys

from PyQt5.QtGui     import QIcon 
from PyQt5.QtWidgets import QApplication, QMessageBox, QScrollArea
from PyQt5.QtCore    import QTimer, QSize, Qt

# Modules Eficas
from Extensions.i18n import tr

from InterfaceQT4.feuille                import Feuille
from desWidgetPlusieursBase              import Ui_WidgetPlusieursBase 
from InterfaceQT4.politiquesValidation   import PolitiquePlusieurs
from InterfaceQT4.qtSaisie               import SaisieValeur
from InterfaceQT4.gereListe              import GereListe
from InterfaceQT4.gereListe              import GerePlie
from InterfaceQT4.gereListe              import LECustom

dicoLongueur = {2:90,3:100,4:123,5:145,6:160,float('inf'):200}
hauteurMaxFenetre = 200
nbMinimumDeQLineEdit=7

class MonWidgetPlusieursBase (Ui_WidgetPlusieursBase,Feuille,GereListe,GerePlie):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        #print ('MonWidgetPlusieursBase', nom)
        self.inFocusOutEvent      = False
        self.changeUnLineEdit     = False
        self.nomLine              = "lineEditVal"
        self.inInit               = True # pour l affichage quand on cree le lineEdit
        self.indexDernierLabel    = 0
        self.numLineEditEnCours   = 0
        self.changeUnLineEdit     = None
        self.listeAffichageWidget = []
        self.dictLE               = {}
        self.politique  = PolitiquePlusieurs(node,parentQt)
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        GereListe.__init__(self)
        self.gereIconePlier()
        self.BSelectFichier.clicked.connect(self.selectInFile)

        if sys.platform[0:5]!="linux":
          repIcon   = self.node.editor.appliEficas.repIcon
          fichierUp = os.path.join(repIcon, 'arrow_up.png')
          iconUp    = QIcon(fichierUp)
          self.RBHaut.setIcon(iconUp)
          self.RBHaut.setIconSize(QSize(32, 32))
          fichierDown = os.path.join(repIcon, 'arrow_down.png')
          iconDown    = QIcon(fichierDown)
          self.RBBas.setIcon(iconArrowDown)
          fichierExp = os.path.join(repIcon, 'file-explorer.png')
          iconExp    = QIcon(fichierExp)
          self.BSelectFichier.setIcon(iconExp)
          self.BSelectFichier.setIconSize(QSize(32, 32))

        iconMoins = QIcon (self.repIcon+"/MoinsBleu.png")
        self.RBMoins.setIcon(iconMoins)
        iconPlus = QIcon(self.repIcon+"/PlusBleu.png")
        self.RBPlus.setIcon(iconPlus)
        iconLoupe =QIcon(self.repIcon+"/verre-loupe-icone-6087-64.png")
        self.RBVoisListe.setIcon(iconLoupe)


        self.vScrollBar = self.scrollArea.verticalScrollBar()

        if self.monSimpDef.max < 7 : 
            hauteurMax = dicoLongueur[self.monSimpDef.max]
            self.RBVoisListe.close()
            self.RBMoins.close()
            self.RBPlus.close()
            aConstruire = self.monSimpDef.max
        else : 
            hauteurMax  = hauteurMaxFenetre
            aConstruire = nbMinimumDeQLineEdit
        self.setMinimumHeight(hauteurMax)

        for i in range(1,aConstruire): self.ajoutLineEdit()
        self.parentQt.commandesLayout.insertWidget(-1,self)

        self.maCommande.listeAffichageWidget.append(self.lineEditVal1)
        self.AAfficher = self.lineEditVal1
        self.inInit    = False
        # PNPN a completer __ si tuple le type des tuples sinon le tuple
        self.finCommentaireListe()
        self.monCommentaireLabel.setText(self.finCommentaireListe())
        self.scrollArea.leaveEvent = self.leaveEventScrollArea



  def setValeurs(self):
  # uniquement appele a l initialisation.
  # les lineEdit ont deja ete crees
       self.listeValeursCourantes=self.node.item.getListeValeurs()
       index=1
       for valeur in self.listeValeursCourantes :
           val = self.politique.getValeurTexte(valeur)
           nomLineEdit = "lineEditVal"+str(index)
           if hasattr(self,nomLineEdit) : 
              courant = getattr(self,nomLineEdit)
              if 'R' in self.objSimp.definition.type and str(val) != repr(val) :  courant.setText(repr(val))
              else    :  courant.setText(str(val))
           else :
              self.ajoutLineEdit(val)
           index=index+1
       if self.indexDernierLabel < self.monSimpDef.max  : self.ajoutLineEdit()
       

  def ajoutLineEdit(self,valeur=None,):
      #print ('ajoutLineEdit, monWidgetPlusieursBase', self.indexDernierLabel)
      self.indexDernierLabel=self.indexDernierLabel+1
      nomLineEdit="lineEditVal"+str(self.indexDernierLabel)
      if hasattr(self,nomLineEdit) : 
         #print ('ajoutLineEdit, monWidgetPlusieursBase', self.indexDernierLabel)
         self.indexDernierLabel=self.indexDernierLabel-1
         return
      nouveauLE = LECustom(self.scrollArea,self,self.indexDernierLabel)
      self.verticalLayoutLE.insertWidget(self.indexDernierLabel-1,nouveauLE)
      nouveauLE.setText("")
      if self.indexDernierLabel % 2 == 1 : nouveauLE.setStyleSheet("background:rgb(210,210,210)")
      else :	                           nouveauLE.setStyleSheet("background:rgb(235,235,235)")
      nouveauLE.setFrame(False)
      # fait dans le init pour pouvoir passer le numero du LE mai 20
      #nouveauLE.returnPressed.connect(self.changeValeur)

      setattr(self,nomLineEdit,nouveauLE)
      self.listeAffichageWidget.append(nouveauLE)
      self.etablitOrdre()
      if valeur != None : 
         nouveauLE.setText(str(valeur))
         self.dictLE[self.indexDernierLabel] = valeur
      else : 
         self.dictLE[self.indexDernierLabel] = None
      # deux lignes pour que le ensureVisible fonctionne
      self.estVisible=nouveauLE
      if self.inInit==False :QTimer.singleShot(1, self.rendVisibleLigne)
      #print ('ajoutLineEdit, monWidgetPlusieursBase', self.indexDernierLabel)

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
        #import traceback
        #traceback.print_stack()
        if valeur == None : return
        liste,validite=SaisieValeur.TraiteLEValeur(self,str(valeur))
        if validite == 0 : return
        if liste ==[]    : return
        listeVal=[]
        for valeur in self.listeValeursCourantes : listeVal.append(valeur)
        validite,comm,comm2,listeRetour=self.politique.ajoutValeurs(liste,-1,listeVal)
        if (comm2 != "" and comm != None) : return comm2
        if validite : 
           self.listeValeursCourantes=self.listeValeursCourantes+listeRetour
           if len(self.listeValeursCourantes) > self.monSimpDef.min :
              self.node.item.setValeur(self.listeValeursCourantes)
              self.reaffiche()
           return None
        else :
           return(comm2+" "+comm)
        
  def reaffiche(self):
      # A priori, on ne fait rien
      pass

                
  def ajoutNValeur(self,liste):
  #----------------------------
  # attention quand on charge par un fichier, on ne peut pas se contenter d ajouter N fois 1 valeur
  # car alors le temps de verification devient prohibitif  reconstructution et verification a 
  # chaque valeur. d ou l ajout de ajoutNTuple a politique plusieurs

           
        listeFormatee=list(liste)

        min,max=self.node.item.getMinMax()
        if self.objSimp.valeur == None : listeComplete = listeFormatee
        else                           : listeComplete = self.objSimp.valeur + listeFormatee

        if len(listeComplete) > max : 
           texte=tr("Nombre maximum de valeurs ")+str(max)+tr(" atteint")
           self.editor.afficheInfos(texte,Qt.red)
           return

        validite,comm,comm2 = self.politique.ajoutNTuple(listeComplete)
        if not validite : 
           self.editor.afficheInfos(comm2,Qt.red)
           return

        self.politique.recordValeur(listeComplete)

        indexDernierRempli=0
        while ( indexDernierRempli < len(liste) ) :
         texte=liste[indexDernierRempli]
         if indexDernierRempli < self.indexDernierLabel:
            nomLineEdit="lineEditVal"+str(indexDernierRempli+1)
            courant=getattr(self,nomLineEdit)
            courant.setText(str(texte))
         else : 
            self.ajoutLineEdit(texte)
         indexDernierRempli = indexDernierRempli + 1
        

  def changeValeur(self,changeDePlace=True,oblige=False,numero=None):
      #print ('monWidgetPlusieursBase changeValeur')
      self.changeUnLineEdit = False
      donneFocus=None
      derniereValeur=None
      self.listeValeursCourantes = []
      fin=self.indexDernierLabel

      for i in range (1, self.indexDernierLabel+1):
          nomLineEdit="lineEditVal"+str(i)
          courant=getattr(self,nomLineEdit)
          valeur=courant.text()
          if valeur != None and valeur != "" : 
             # c est ce qui est long mais permet d avoir 
             # une bonne connaissance des erreurs
             # et de traiter le changede place
             commentaire=self.ajout1Valeur(valeur)
             if (commentaire != None ):
                 self.editor.afficheInfos(commentaire,Qt.red)
                 courant.setText("")
                 donneFocus=courant
                 self.reaffiche()
                 return
             else :
                 self.editor.afficheInfos("")
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
      min,max = self.node.item.getMinMax()
      if len(self.listeValeursCourantes) < self.monSimpDef.min  :
        self.editor.afficheInfos(tr('nb min de valeurs : ')+str( self.monSimpDef.min))
      if len(self.listeValeursCourantes) < min and oblige==True: return
      if len(self.listeValeursCourantes) > max : return
      self.node.item.setValeur(self.listeValeursCourantes)
      #print (self.listeValeursCourantes)
      if len(self.listeValeursCourantes) == self.monSimpDef.max  :
        self.editor.afficheInfos(tr('nb max de valeurs atteint'))
      self.setValide()
      self.reaffiche()

          
  def leaveEventScrollArea(self,event):
      #print ('monWidgetPlusBase leaveEventScrollArea', self.changeUnLineEdit)
      if self.changeUnLineEdit : self.changeValeur(changeDePlace=False)
      QScrollArea.leaveEvent(self.scrollArea,event)




