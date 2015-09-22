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
from desWidgetPlusieursInto import Ui_WidgetPlusieursInto 
from politiquesValidation   import PolitiquePlusieurs
from qtSaisie               import SaisieValeur
#from gereListe              import GereListe

class MonWidgetPlusieursInto (Ui_WidgetPlusieursInto,Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        #print "MonWidgetPlusieursInto", nom, self
        self.index=1
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.connect(self.CBCheck, SIGNAL('stateChanged(int)'),self.change)
        # try except si la liste des possibles est vide
        # prevoir qqchose
        try :
          self.maCommande.listeAffichageWidget.append(self.lineEditVal1)
        except :
          pass


  def change(self,int):
       if self.CBCheck.isChecked() : 
          for i in range(len(self.listeAAfficher)):
              nomCB="lineEditVal"+str(i+1)
              courant=getattr(self,nomCB)
              courant.setChecked(True)
       else :
          min,max = self.node.item.GetMinMax()
          for i in range(len(self.listeAAfficher)):
              nomCB="lineEditVal"+str(i+1)
              courant=getattr(self,nomCB)
              courant.setChecked(False)

  def setValeurs(self):
       self.listeValeursCourantes=self.node.item.GetListeValeurs()
       if hasattr(self.node.item.definition.validators,'set_MCSimp'):
            obj=self.node.item.getObject()
            self.node.item.definition.validators.set_MCSimp(obj)
            if self.node.item.isvalid() == 0 :
               liste=[]
               for item in self.listeValeursCourantes:
                   if self.node.item.definition.validators.verif_item(item)==1:
                      liste.append(item)
               self.listeAAfficher=self.node.item.get_liste_possible(liste)
               #print self.listeAAfficher
            else: 
               self.listeAAfficher=self.node.item.get_liste_possible([])
       else :
               self.listeAAfficher=self.node.item.get_liste_possible([])

       self.PourEtreCoche=self.listeValeursCourantes
       if self.objSimp.wait_assd() : 
          self.listeAAfficher=self.node.item.get_sd_avant_du_bon_type()
          self.PourEtreCoche=[]
          for concept in self.listeValeursCourantes:
              self.PourEtreCoche.append(concept.nom)
       if len(self.listeAAfficher)*20 > 400 : self.setMinimumHeight(400)
       else : self.setMinimumHeight(len(self.listeAAfficher)*30)
       self.adjustSize()
       self.vScrollBar = self.scrollArea.verticalScrollBar()
       self.politique=PolitiquePlusieurs(self.node,self.editor)
       self.indexListe=1
       for i in range(1,len(self.listeAAfficher)+1): self.ajoutCB(i)
       for i in range(len(self.listeAAfficher)):
           nomCB="lineEditVal"+str(i+1)
           courant=getattr(self,nomCB)
           courant.setText(str(self.listeAAfficher[i]))
           #if self.monSimpDef.into[i] in self.listeValeursCourantes : 
           if self.listeAAfficher[i] in self.PourEtreCoche : 
              courant.setChecked(True)
           self.connect(courant,SIGNAL("toggled(bool)"),self.changeValeur)
       self.vScrollBar.triggerAction(QScrollBar.SliderToMinimum)
       

  def ajoutCB(self,index,valeur=None):
      #print "ajoutCB ", index
      nomCB="lineEditVal"+str(index)
      if hasattr(self,nomCB) : return
      nouveauCB = QCheckBox(self.scrollArea)
      self.CBLayout.addWidget(nouveauCB)
      qApp.processEvents()
      nouveauCB.setText("")
      if index % 2 == 1 : nouveauCB.setStyleSheet("background:rgb(210,210,210)")
      else :	                    nouveauCB.setStyleSheet("background:rgb(240,240,240)")
      self.vScrollBar.triggerAction(QScrollBar.SliderToMaximum)
      nouveauCB.setFocus()
      setattr(self,nomCB,nouveauCB)
      

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
        #print "________________"
        #print self
        #print self.node
        #print self.node.item
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
           return None
        else :
           return(comm2+" "+comm)
        


  def changeValeur(self):
      self.listeValeursCourantesAvant=self.listeValeursCourantes
      self.listeValeursCourantes = []
      #print "changeValeur ____________" , self.monSimpDef.into, len(self.monSimpDef.into)
      for i in range (1,len(self.listeAAfficher)+1):
          nomLineEdit="lineEditVal"+str(i)
          courant=getattr(self,nomLineEdit)
          if not (courant.isChecked()):continue
          valeur=courant.text()
          if valeur != None and valeur != "" : 
             commentaire=self.ajout1Valeur(valeur)
             if (commentaire != None ):
                 self.editor.affiche_infos(commentaire,Qt.red)
                 courant.setText("")
      min,max = self.node.item.GetMinMax()
      if len(self.listeValeursCourantes) < min : 
         self.editor.affiche_infos(tr("Nombre minimal de valeurs : ") + str(min),Qt.red)
      elif len(self.listeValeursCourantes) > max : 
         self.editor.affiche_infos(tr("Nombre maximal de valeurs : ") + str(max),Qt.red)
      else :
         self.editor.affiche_infos(tr(""))
      if self.listeValeursCourantes== [] : self.listeValeursCourantes=None
      self.node.item.set_valeur(self.listeValeursCourantes)
      self.setValide()
      self.reaffiche()


