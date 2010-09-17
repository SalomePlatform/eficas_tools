# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
# Modules Python
import string,types,os

# Modules Eficas
from qtSaisie      import SaisieValeur
from monPlusieursBasePanel import MonPlusieursBasePanel

from PyQt4.QtGui  import *
from PyQt4.QtCore import *

# Import des panels

class MonFonctionPanel(MonPlusieursBasePanel):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
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
        if "VALE" in genea:
            self.nbValeurs=2
        if "VALE_C" in genea:
            self.nbValeurs=3


  def DecoupeListeValeurs(self,liste):
        #decoupe la liste des valeurs en n ( les x puis les y)
        l_valeurs=[]
        if (len(liste)% self.nbValeurs != 0):
            message="La cardinalité n'est pas correcte, la dernière valeur est ignorée"
            #self.Commentaire.setText(QString(commentaire)) 
            self.editor.affiche_infos(message,Qt.red)
        i=0
        while ( i < (len(liste) - self.nbValeurs + 1)) :
            t=tuple(liste[i:i+self.nbValeurs])
            l_valeurs.append(t)
            i=i+self.nbValeurs
        return l_valeurs

  def BuildLBValeurs(self):
        self.LBValeurs.clear()
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
                       print TupleEnTexte
                       self.LBValeurs.addItem(TupleEnTexte)
                   else :
                       self.LBValeurs.addItem(QString(str(valeur)))


  def  Ajout1Valeur(self,liste=[]):
        # Pour être appele a partir du Panel Importer (donc plusieurs fois par AjouterNValeur)
        validite=1
        if liste == [] :
           if self.node.item.wait_tuple()== 1 :
              liste=SaisieValeur.TraiteLEValeurTuple(self)
              if liste == [''] : return
           else :
              liste,validite=SaisieValeur.TraiteLEValeur(self)
              if validite == 0 : return
        if liste ==[]    : return

        if len(liste) != self.nbValeurs :
            commentaire  = QString(str(liste)) 
            commentaire += QString(" n est pas un tuple de ") 
            commentaire += QString(str(self.nbValeurs)) 
            commentaire += QString(" valeurs")
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


  def AjoutNValeur(self,liste) :
        if len(liste)%self.nbValeurs != 0 :
           texte="Nombre de valeur incorrecte"
           #self.Commentaire.setText(texte)
           self.editor.affiche_infos(texte,Qt.red)
           return
        listeDecoupee=self.DecoupeListeValeurs(liste)
        for vals in listeDecoupee :
            self.Ajout1Valeur(vals)
           
  def Sup1Valeur(self):
        index=self.LBValeurs.currentRow()
        if index == None : return
        self.LBValeurs.takeItem(index)
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

      
