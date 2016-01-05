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
from qtSaisie      import SaisieValeur
from monPlusieursBasePanel import MonPlusieursBasePanel

from PyQt4.QtGui  import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

# Import des panels

class MonFonctionPanel(MonPlusieursBasePanel):
#  Classe definissant le panel associe© aux mots-cles qui demandent
#  a l'utilisateur de choisir une seule valeur parmi une liste de valeurs
#  discretes
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonFonctionPanel"
        self.node=node
        self.SetNbValeurs()
        MonPlusieursBasePanel.__init__(self,node,parent,name,fl)

  def SetNbValeurs(self):
        self.nbValeurs = 1
        if self.node.item.wait_tuple()== 1 :
           for a in self.node.item.definition.type :
               try :
                   self.nbValeurs = a.ntuple
                   break
               except :
                   pass
        genea=self.node.item.get_genealogie()
        self.nbValeursASaisir=self.nbValeurs
        if "VALE" in genea: self.nbValeurs=2
        if "VALE_C" in genea: self.nbValeurs=3


  def DecoupeListeValeurs(self,liste):
        #decoupe la liste des valeurs en n ( les x puis les y)
        l_valeurs=[]
        if ((len(liste)% self.nbValeursASaisir != 0 and (len(liste)% self.nbValeurs))):
            message=tr("La cardinalite n'est pas correcte, la derniere valeur est ignoree")
            #self.Commentaire.setText(QString(commentaire)) 
            self.editor.affiche_infos(message,Qt.red)
        i=0
        while ( i < len(liste) ) :
            try :
              t=tuple(liste[i:i+self.nbValeurs])
              i=i+self.nbValeurs
            except:
              t=tuple(liste[i:len(liste)])
            l_valeurs.append(t)
        return l_valeurs

  def BuildLBValeurs(self,listeValeurs=None):
        self.LBValeurs.clear()
        if listeValeurs== None :
           listeValeurs=self.node.item.GetListeValeurs()
        if self.node.item.wait_tuple()== 1 :
	      listeATraiter=listeValeurs
              for valeur in listeATraiter:
                  str_valeur=str(valeur)
                  self.LBValeurs.addItem(str_valeur)
        else : 
	      for valeur in self.DecoupeListeValeurs(listeValeurs):
                   if type(valeur) == types.TupleType:
                       TupleEnTexte="("
                       for val in valeur :
                           TupleEnTexte = TupleEnTexte + str(self.politique.GetValeurTexte(val)) +", "
                       TupleEnTexte = TupleEnTexte[0:-2] +")"
                       self.LBValeurs.addItem(TupleEnTexte)
                   else :
                       self.LBValeurs.addItem(QString(str(valeur)))


  def  ajout1Valeur(self,liste=[]):
        # Pour etre appele a partir du Panel Importer (donc plusieurs fois par AjouterNValeur)
        validite=1
        if liste == [] :
           if self.node.item.wait_tuple()== 1 :
              liste=SaisieValeur.TraiteLEValeurTuple(self)
              if liste == [''] : return
           else :
              liste,validite=SaisieValeur.TraiteLEValeur(self)
              if validite == 0 : return
        if liste ==[]    : return

        if (self.node.item.wait_tuple()== 1 and len(liste) != self.nbValeurs):
            commentaire  = QString(str(liste)) 
            commentaire += QString(tr(" n est pas un tuple de ")) 
            commentaire += QString(str(self.nbValeursASaisir)) 
            commentaire += QString(tr(" valeurs"))
	    self.LEValeur.setText(QString(str(liste)))
            self.editor.affiche_infos(commentaire,Qt.red)
            return

        if self.node.item.wait_tuple()== 1 :
              liste2=tuple(liste)
              liste=liste2

        index=self.LBValeurs.currentRow()
        if ((self.LBValeurs.isItemSelected(self.LBValeurs.item(index )) == 0) and (index > 0 )):
           index=0
        else :
           index=self.LBValeurs.currentRow() + 1
        indexListe=index*self.nbValeurs
        if index == 0 : indexListe=len(self.listeValeursCourantes)

        listeVal=[]
        for valeur in self.listeValeursCourantes :
                listeVal.append(valeur)
        if self.node.item.wait_tuple()== 1 :
             indexListe = index
             validite,comm,comm2,listeRetour=self.politique.AjoutTuple(liste,index,listeVal)
        else :
             validite,comm,comm2,listeRetour=self.politique.AjoutValeurs(liste,index,listeVal)
        self.Commentaire.setText(QString.fromUtf8(QString(comm2)))
        if not validite :
                self.editor.affiche_infos(comm,Qt.red)
        else:
           self.LEValeur.setText(QString(""))
           l1=self.listeValeursCourantes[:indexListe]
           l3=self.listeValeursCourantes[indexListe:]
           if self.node.item.wait_tuple()== 1 :
	      listeATraiter=listeRetour
           else : 
              listeATraiter=self.DecoupeListeValeurs(listeRetour)
           for valeur in  listeATraiter :
               if type(valeur) == types.TupleType:
                  TupleEnTexte="("
                  for val in valeur :
                      TupleEnTexte = TupleEnTexte + str(self.politique.GetValeurTexte(val)) +", "
                  str_valeur = TupleEnTexte[0:-2] +")"
               else :
                  str_valeur=str(valeur)
               self.LBValeurs.insertItem(index,str_valeur)
               item=self.LBValeurs.item(index)
               item.setSelected(1)
               self.LBValeurs.setCurrentItem(item)
               index=index+1
           self.listeValeursCourantes=l1+listeRetour+l3
           self.BuildLBValeurs(self.listeValeursCourantes)


  def ajoutNValeur(self,liste) :
        if len(liste)%self.nbValeurs != 0 :
           texte="Nombre de valeur incorrecte"
           #self.Commentaire.setText(texte)
           self.editor.affiche_infos(texte,Qt.red)
           return
        listeDecoupee=self.DecoupeListeValeurs(liste)
        for vals in listeDecoupee :
            self.ajout1Valeur(vals)
           
  def Sup1Valeur(self):
        index=self.LBValeurs.currentRow()
        if index == None : return
        removed_item = self.LBValeurs.takeItem(index)
        text = removed_item.text()[1:-1] # Remove the parenthesis
        self.LEValeur.setText(text)
        listeVal=[]
        indexInterdit=[]
        for i in range(self.nbValeurs):
            indexAOter=index*self.nbValeurs + i
            indexInterdit.append(indexAOter)
        if self.node.item.wait_tuple()== 1 :
           indexInterdit=[index]

        i=0
        for valeur in self.listeValeursCourantes :
            if not (i in indexInterdit) : 
                listeVal.append(valeur)
            i = i+1
        self.listeValeursCourantes=listeVal
        listeValeurs=self.listeValeursCourantes

      
