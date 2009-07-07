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
import prefs 

from qt import *

from desPlusieursInto import DPlusInto
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiquePlusieurs

# Import des panels

class MonPlusieursIntoPanel(DPlusInto,QTPanel,SaisieValeur):
  """
  Classe d�finissant le panel associ� aux mots-cl�s qui demandent
  � l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discr�tes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        QTPanel.__init__(self,node,parent)
        DPlusInto.__init__(self,parent,name,fl)
        self.politique=PolitiquePlusieurs(node,parent)
        SaisieValeur.BuildLBValeurs(self)
        self.listeValeursCourantes=self.node.item.GetListeValeurs()
        SaisieValeur.RemplitPanel(self,self.listeValeursCourantes)
        QObject.connect(self.listBoxVal, SIGNAL("doubleClicked(QListBoxItem*)" ), self.Ajout1Valeur )
        self.InitCommentaire()

  def BOkPourListePressed(self):
        if self.listeValeursCourantes == [] :
           self.editor.affiche_infos("Pas de validation d un groupe vide")
           return
        self.node.item.set_valeur(self.listeValeursCourantes)
	self.editor.affiche_infos("Valeur Accept�e")

  def BSupPressed(self):
        QTPanel.BSupPressed(self)

  def ViewDoc(self):
      QTPanel.ViewDoc(self)

  def Sup1Valeur(self):
        index=self.LBValeurs.currentItem()
        self.LBValeurs.removeItem(self.LBValeurs.currentItem())
        listeVal=[]
        i=0
        for valeur in self.listeValeursCourantes :
                if i != index : listeVal.append(valeur)
                i = i+1
        self.listeValeursCourantes=listeVal
        SaisieValeur.RemplitPanel(self,self.listeValeursCourantes)
          
  def Ajout1Valeur(self):
        liste=[]
        if self.listBoxVal.currentText().latin1() == None : return
        liste.append(self.listBoxVal.currentText().latin1())
        index=self.LBValeurs.currentItem() + 1
        if index==0 : index = -1
        listeVal=[]
        for valeur in self.listeValeursCourantes :
                listeVal.append(valeur)
        validite,comm,comm2,listeRetour=self.politique.AjoutValeurs(liste,index,listeVal) 
	self.Commentaire.setText(comm2)
        if not validite :
		self.editor.affiche_infos(comm)
        else:
           l1=self.listeValeursCourantes[:index]
           l3=self.listeValeursCourantes[index:]
           for valeur in listeRetour:
               self.LBValeurs.insertItem(QString(str(valeur)),index)
               self.LBValeurs.setCurrentItem(index)
               index=index+1
           self.listeValeursCourantes=l1+listeRetour+l3
        SaisieValeur.RemplitPanel(self,self.listeValeursCourantes)

  def InitCommentaire(self):
        commentaire=""
        mc = self.node.item.get_definition()
        d_aides = { 'TXM' : 'cha�nes de caract�res',
                  'R'   : 'r�els',
                  'I'   : 'entiers',
                  'C'   : 'complexes'}
        type = mc.type[0]
        if not d_aides.has_key(type) :
           if mc.min == mc.max:
               commentaire="Entrez "+str(mc.min)+" valeurs "
           else :
               commentaire="Entrez entre "+str(mc.min)+" et "+str(mc.max)+" valeurs "
        else :
           if mc.min == mc.max:
               commentaire="Entrez "+str(mc.min)+" "+d_aides[type]
           else :
               commentaire="Entrez entre "+str(mc.min)+" et "+str(mc.max)+" "+d_aides[type]
        aideval=self.node.item.aide()
        commentaire=commentaire + "\n" + aideval
        self.Commentaire.setText(QString(commentaire))
