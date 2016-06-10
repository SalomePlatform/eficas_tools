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
from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtWidgets  import QCheckBox, QScrollBar, QFrame, QApplication, QLabel
    from PyQt5.QtWidgets  import QSizePolicy,QSpacerItem
    from PyQt5.QtGui  import QPalette, QFont
    from PyQt5.QtCore import Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *

from Extensions.i18n import tr

from feuille                import Feuille
from desWidgetPlusieursInto import Ui_WidgetPlusieursInto 
from politiquesValidation   import PolitiquePlusieurs
from qtSaisie               import SaisieValeur
from gereListe              import GerePlie
from gereListe              import GereListe

class MonWidgetPlusieursInto (Ui_WidgetPlusieursInto,Feuille,GerePlie,GereListe):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        print "MonWidgetPlusieursInto", nom, self
        self.index=1
        self.alpha=0
        self.listeCB=[]
        self.listeCbRouge=[]
        self.listeValeursCourantes=node.item.GetListeValeurs()
        if self.listeValeursCourantes == None : self.listeValeursCourantes=[]

        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        GereListe.__init__(self)

        self.parentQt.commandesLayout.insertWidget(-1,self)
        if monEnvQT5 : self.CBCheck.stateChanged.connect(self.changeTout)
        else         : self.connect(self.CBCheck, SIGNAL('stateChanged(int)'),self.changeTout)

        self.gereIconePlier()
        self.editor.listeDesListesOuvertes.add(self.node.item)
        self.inhibe=False
        self.finCommentaireListe()

        if self.listeAAfficher== None or self.listeAAfficher==[] : 
            spacerItem = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            self.CBLayout.addItem(spacerItem)
            nouveauCommentaire=QLabel()
            maPolice= QFont("Times", 16)
            nouveauCommentaire.setFont(maPolice);
            nouveauCommentaire.setText(tr('Pas de valeurs possibles'))
            self.CBLayout.addWidget(nouveauCommentaire)
            spacerItem2 = QSpacerItem(40, 70, QSizePolicy.Fixed, QSizePolicy.Minimum)
            self.CBLayout.addItem(spacerItem2)

        # try except si la liste des possibles est vide
        # prevoir qqchose
        try :
          self.maCommande.listeAffichageWidget.append(self.lineEditVal1)
        except :
          pass


  def changeTout(self,int):
       if self.inhibe : return
       self.inhibe=True
       if not(self.CBCheck.isChecked()) : 
          min,max = self.node.item.GetMinMax()
          if max < len(self.listeAAfficher) :
             commentaire=tr('impossible de tout selectionner : max =')+str(max)
             self.editor.affiche_infos(commentaire,Qt.red)
             self.inhibe=False
             return
          for i in range(len(self.listeAAfficher)):
              nomCB="lineEditVal"+str(i+1)
              courant=getattr(self,nomCB)
              courant.setChecked(True)
          self.CBCheck.setChecked(False)
       else :
          for i in range(len(self.listeAAfficher)):
              nomCB="lineEditVal"+str(i+1)
              courant=getattr(self,nomCB)
              courant.setChecked(False)
          self.CBCheck.setChecked(True)
       self.inhibe=False
       self.changeValeur()

  def setValeurs(self):
       self.listeValeursCourantes =self.node.item.get_valeur()
       if self.listeValeursCourantes ==  None : self.listeValeursCourantes=[]
       #print "ds set Valeur", self.listeValeursCourantes, self.node.item.get_valeur()
       self.politique=PolitiquePlusieurs(self.node,self.editor)
       self.vScrollBar = self.scrollArea.verticalScrollBar()

       if hasattr(self.node.item.definition.validators,'set_MCSimp'):
            obj=self.node.item.getObject()
            self.node.item.definition.validators.set_MCSimp(obj)
            if self.node.item.isvalid() == 0 :
               liste=[]
               for item in self.listeValeursCourantes:
                   if self.node.item.definition.validators.verif_item(item)==1:
                      liste.append(item)
               self.listeAAfficher=self.node.item.get_liste_possible(liste)
            else: 
               self.listeAAfficher=self.node.item.get_liste_possible([])
       else :
               self.listeAAfficher=self.node.item.get_liste_possible([])

       if self.objSimp.wait_assd() : 
          self.listeAAfficher=self.node.item.get_sd_avant_du_bon_type()
       if self.listeAAfficher== None or self.listeAAfficher==[] : self.listeAAfficher=[]

       if len(self.listeAAfficher)*20 > 400 : self.setMinimumHeight(400)
       else : self.setMinimumHeight(len(self.listeAAfficher)*30)

       self.PourEtreCoche=[]
       if self.objSimp.wait_assd() : 
          for concept in self.listeValeursCourantes: self.PourEtreCoche.append(concept.nom)
       else :
          for val in self.listeValeursCourantes: self.PourEtreCoche.append(val)

       maListe=[]
       for  i in self.listeAAfficher: maListe.append(i)  
       if self.alpha==1 : maListe.sort()
       for i in range(1,len(maListe)+1): self.ajoutCB(i)

       self.inhibe=True
       for i in range(len(maListe)):
           nomCB="lineEditVal"+str(i+1)
           courant=getattr(self,nomCB)
           courant.setText(str(maListe[i]))
           if maListe[i] in self.PourEtreCoche : courant.setChecked(True)
           else                                : courant.setChecked(False)

           if monEnvQT5 : courant.toggled.connect(self.changeValeur)
           else         : self.connect(courant,SIGNAL("toggled(bool)"),self.changeValeur)
       self.inhibe=False

       self.vScrollBar.triggerAction(QScrollBar.SliderToMinimum)
       

  def ajoutCB(self,index,valeur=None):
      nomCB="lineEditVal"+str(index)
      if hasattr(self,nomCB) : return
      nouveauCB = QCheckBox(self.scrollArea)
      #self.CBLayout.addWidget(nouveauCB)
      self.CBLayout.insertWidget(index-1,nouveauCB)
      #QApplication.processEvents()
      self.listeCB.append(nouveauCB)
      nouveauCB.setText("")
      if index % 2 == 1 : nouveauCB.setStyleSheet("background:rgb(210,210,210)")
      else :	                    nouveauCB.setStyleSheet("background:rgb(240,240,240)")
      self.vScrollBar.triggerAction(QScrollBar.SliderToMaximum)
      nouveauCB.setFocus()
      setattr(self,nomCB,nouveauCB)
      

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
           return None
        else :
           return(comm2+" "+comm)
        


  def changeValeur(self):
      if self.inhibe == True: return
      self.noircirResultatFiltre()
      self.listeValeursCourantesAvant=self.listeValeursCourantes
      self.listeValeursCourantes = []

      for i in range (1,len(self.listeAAfficher)+1):
          nomLineEdit="lineEditVal"+str(i)
          courant=getattr(self,nomLineEdit)
          if not (courant.isChecked()):continue
          valeur=courant.text()
          if valeur != None and valeur != "" : 
             commentaire=self.ajout1Valeur(valeur)
             if (commentaire != None ): 
                 self.editor.affiche_infos(commentaire,Qt.red)
                 self.listeValeursCourantesAvant=self.listeValeursCourantes
                 self.setValeurs()

      min,max = self.node.item.GetMinMax()
      if len(self.listeValeursCourantes) < min : 
         self.editor.affiche_infos(tr("Nombre minimal de valeurs : ") + str(min),Qt.red)
      elif len(self.listeValeursCourantes) > max : 
         self.editor.affiche_infos(tr("Nombre maximal de valeurs : ") + str(max),Qt.red)

      if self.listeValeursCourantes== [] :  self.node.item.set_valeur(None)
      else : self.node.item.set_valeur(self.listeValeursCourantes)

      self.setValide()
      self.reaffiche()


  def prepareListeResultatFiltre(self):
      filtre=str(self.LEFiltre.text())
      for cb in self.listeCB:
          texte=cb.text() 
          if texte.find(filtre) == 0 :
            palette = QPalette(Qt.red)
	    palette.setColor(QPalette.WindowText,Qt.red)
	    cb.setPalette(palette)
            t=cb.text()
            cb.setText(t)
            self.listeCbRouge.append(cb)

  def prepareListeResultat(self):
      self.clearAll()
      self.setValeurs()

  def clearAll(self):
      for cb in self.listeCB :
         cb.setText("")


