# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
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

from desPlusieursBase import Ui_DPlusBase
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiquePlusieurs
from Extensions.i18n import tr


class DPlusBase (Ui_DPlusBase,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       if hasattr(parent,"leLayout"):
          parent.leLayout.removeWidget(parent.leLayout.widgetActive)
          parent.leLayout.widgetActive.close()
          parent.leLayout.addWidget(self)
          parent.leLayout.widgetActive=self
       else:
          parent.partieDroite=QWidget()
          parent.leLayout=QGridLayout(parent.partieDroite)
          parent.leLayout.addWidget(self)
          parent.addWidget(parent.partieDroite)
          parent.leLayout.widgetActive=self
       self.setupUi(self)
       self.appliEficas=parent.appliEficas
       self.RepIcon=parent.appliEficas.RepIcon
       icon = QIcon(self.RepIcon+"/arrow_left.png")
       self.BAjout1Val.setIcon(icon)
       icon2 = QIcon(self.RepIcon+"/arrow_right.png")
       self.BSup1Val.setIcon(icon2)

# Import des panels

class MonPlusieursBasePanel(DPlusBase,QTPanel,SaisieValeur):
  """
  Classe definissant le panel associe aux mots-cles qui demandent
  a l'utilisateur de choisir une liste de valeurs parmi une liste de valeurs
  discretes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonPlusieursBasePanel"
        QTPanel.__init__(self,node,parent)
        DPlusBase.__init__(self,parent,fl)
        self.politique=PolitiquePlusieurs(node,parent)
        self.BuildLBValeurs()
        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        self.InitCommentaire()
        self.detruitBouton()
        self.connecterSignaux()

  def connecterSignaux(self) :
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPourListePressed)
        self.connect(self.bParam,SIGNAL("clicked()"),self.BParametresPressed)
        self.connect(self.bImport,SIGNAL("clicked()"),self.BImportPressed)
        self.connect(self.BAjout1Val,SIGNAL("clicked()"),self.Ajout1Valeur)
        self.connect(self.BSup1Val,SIGNAL("clicked()"),self.Sup1Valeur)
        self.connect(self.LEValeur,SIGNAL("returnPressed()"),self.LEValeurPressed)
        self.connect(self.BSalome,SIGNAL("clicked()"),self.BSalomePressed)
        self.connect(self.BView2D,SIGNAL("clicked()"),self.BView2DPressed)


  def detruitBouton(self):
        icon3 = QIcon(self.RepIcon+"/image240.png")
        self.BSalome.setIcon(icon3)
        mc = self.node.item.get_definition()
        type = mc.type[0]
        if not(('grma' in repr(type)) or ('grno' in repr(type))) or not(self.editor.salome) :
           self.BSalome.close()
           self.BView2D.close()


  def BuildLBValeurs(self):
       # redefinit en raison de l heritage par monFonctionPanel
        SaisieValeur.BuildLBValeurs(self)

  def BOkPourListePressed(self):
        self.editor.init_modif()
        if self.listeValeursCourantes == [] :
           self.editor.affiche_infos("Aucune Valeur",Qt.red)
           return
        min,max = self.node.item.GetMinMax()
        if len(self.listeValeursCourantes) > max :
            commentaire=tr("La liste comporte trop d elements : la cardinalite maximale est ")+ str(max)
            self.editor.affiche_infos(commentaire,Qt.red)
            return 
        if len(self.listeValeursCourantes) < min :
            commentaire=tr("La liste ne comporte pas suffisament d elements : la cardinalite minimale est ")+ str(min)
            self.editor.affiche_infos(commentaire,Qt.red)
            return 

        self.node.item.set_valeur(self.listeValeursCourantes)
	self.editor.affiche_infos(tr("Valeur Acceptee"))


  def BParametresPressed(self):
        QTPanel.BParametresPressed(self)

  def LEValeurPressed(self):
        self.Ajout1Valeur()

  def Sup1Valeur(self):
        index=self.LBValeurs.currentRow()
        if index < 0 : return
        if self.LBValeurs.isItemSelected(self.LBValeurs.item(index)) == 0 : return
        self.LEValeur.setText(self.LBValeurs.item(index).text())
        self.LBValeurs.takeItem(index)
        listeVal=[]
        i=0
        for valeur in self.listeValeursCourantes :
                if i != index : listeVal.append(valeur)
                i = i+1
        self.LBValeurs.setCurrentItem(self.LBValeurs.item(index -1))
        self.listeValeursCourantes=listeVal
          

  def Ajout1Valeur(self,valeur=None):
        if valeur == None :
           valeur=str(self.LEValeur.text())

        liste,validite=SaisieValeur.TraiteLEValeur(self,valeur)
        if validite == 0 : return
        if liste ==[]    : return

        indexCourant=self.LBValeurs.currentRow()
        if ( (self.LBValeurs.isItemSelected(self.LBValeurs.item(indexCourant )) == 0) 
           and (indexCourant > 0 )):
           index=0
        else :
           index=self.LBValeurs.currentRow() + 1

        listeVal=[]
        for valeur in self.listeValeursCourantes :
                listeVal.append(valeur)
        validite,comm,comm2,listeRetour=self.politique.AjoutValeurs(liste,index,listeVal) 
        if len(comm2) > 40:
           restant=comm2
           comm2=""
           while len(restant) > 40 :
                 comm2=comm2+restant[0:40]+"\n"
                 restant=restant[41:]
           comm2+=restant 
	self.Commentaire.setText(comm2)
        if not validite :
		self.editor.affiche_infos(comm,Qt.red)
        else:
           self.LEValeur.setText(QString(""))
           l1=self.listeValeursCourantes[:index]
           l3=self.listeValeursCourantes[index:]
           for valeur in listeRetour:
               val=self.politique.GetValeurTexte(valeur)
               self.LBValeurs.insertItem(index,QString(str(val)))
               item=self.LBValeurs.item(index)
               item.setSelected(1)
               self.LBValeurs.setCurrentItem(item)
               index=index+1
           self.listeValeursCourantes=l1+listeRetour+l3
	   self.editor.affiche_infos(tr("Valeurs Ajoutées"))

  def AjoutNValeur(self,liste) :
      for val in liste :
	self.Ajout1Valeur(val)

  def BImportPressed(self):
        init=QString( self.editor.CONFIGURATION.savedir)
        fn = QFileDialog.getOpenFileName(self.node.appliEficas, 
                                         tr("Fichier de donnees"),
                                         init,
                                         tr('Tous les  Fichiers (*)',))
        if fn == None : return
        if fn == "" : return
        ulfile = os.path.abspath(unicode(fn))
        self.editor.CONFIGURATION.savedir=os.path.split(ulfile)[0]

        from monSelectVal import MonSelectVal
        MonSelectVal(file=fn,parent=self).show()

  def InitCommentaire(self):
        commentaire=""
        mc = self.node.item.get_definition()
        d_aides = { 'TXM' : 'chaines de caractères',
                  'R'   : 'réels',
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
        self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))

  def BSalomePressed(self):

        self.LEValeur.setText(QString(""))
        self.Commentaire.setText(QString(""))
        genea=self.node.item.get_genealogie()
        kwType = None
        for e in genea:
            if "GROUP_NO" in e: kwType = "GROUP_NO"
            if "GROUP_MA" in e: kwType = "GROUP_MA"

        #print "BkwType",kwType
        selection, commentaire = self.appliEficas.selectGroupFromSalome(kwType,editor=self.editor)
        if commentaire !="" :
            self.Commentaire.setText(QString.fromUtf8(QString(commentaire)))
        monTexte=""
        if selection == [] : return
        for geomElt in selection: 
            monTexte=geomElt+","
        monTexte= monTexte[0:-1]
        self.LEValeur.setText(QString(monTexte))

  def BView2DPressed(self):
        valeur=self.LEValeur.text()
        if valeur == QString("") :
           if self.LBValeurs.currentItem() != None :
              valeur=self.LBValeurs.currentItem().text()
        if valeur == QString("") : return
        valeur = str(valeur)
        if valeur :
           ok, msgError = self.appliEficas.displayShape(valeur)
           if not ok:
              self.editor.affiche_infos(msgError,Qt.red)

