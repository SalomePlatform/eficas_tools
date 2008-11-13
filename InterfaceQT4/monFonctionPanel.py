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
  Classe d�finissant le panel associ� aux mots-cl�s qui demandent
  � l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discr�tes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonFonctionPanel"
        self.node=node
        self.SetNbValeurs()
        MonPlusieursBasePanel.__init__(self,node,parent,name,fl)

  def SetNbValeurs(self):
        genea=self.node.item.get_genealogie()
        if "VALE" in genea:
            self.nbValeurs=2
        if "VALE_C" in genea:
            self.nbValeurs=3


  def DecoupeListeValeurs(self,liste):
        #decoupe la liste des valeurs en n ( les x puis les y)
        l_valeurs=[]
        if (len(liste)% self.nbValeurs != 0):
            message="La cardinalit� n'est pas correcte, la derni�re valeur est ignor�e"
            #self.Commentaire.setText(QString(commentaire)) 
            self.editor.affiche_infos(commentaire)
        for i in range(len(liste)/ self.nbValeurs) :
            if (self.nbValeurs==2):
              t=(liste[i*self.nbValeurs], liste[i*self.nbValeurs+1])
            else:
              t=(liste[i*self.nbValeurs], liste[i*self.nbValeurs+1], liste[i*self.nbValeurs+2])
            l_valeurs.append(t)
        return l_valeurs

  def BuildLBValeurs(self):
        self.LBValeurs.clear()
        listeValeurs=self.node.item.GetListeValeurs()
        for valeur in self.DecoupeListeValeurs(listeValeurs):
               if (self.nbValeurs==2):
                    str_valeur=str(valeur[0])+","+str(valeur[1])
               else:
                    str_valeur=str(valeur[0])+","+str(valeur[1])+","+str(valeur[2])
               self.LBValeurs.addItem(str_valeur)

  def  Ajout1Valeur(self,liste=[]):
        # Pour �tre appele a partir du Panel Importer (donc plusieurs fois par AjouterNValeur)
        if liste == [] :
           liste,validite=SaisieValeur.TraiteLEValeur(self)
        else :
           validite=1
        if validite == 0 : return
        if liste ==[]    : return

        if len(liste) != self.nbValeurs :
            commentaire  = QString(str(liste)) 
            commentaire += QString(" n est pas un tuple de ") 
            commentaire += QString(str(self.nbValeurs)) 
            commentaire += QString(" valeurs")
	    self.LEValeur.setText(QString(str(liste)))
            self.editor.affiche_infos(commentaire)
            return

        index=self.LBValeurs.currentRow()
        if ((self.LBValeurs.isItemSelected(self.LBValeurs.item(index )) == 0) and (index > 0 )):
           index=0
        else :
           index=self.LBValeurs.currentRow() + 1
        indexListe=index*self.nbValeurs
        if index == 0 : 
           indexListe=len(self.listeValeursCourantes)
        listeVal=[]
        for valeur in self.listeValeursCourantes :
                listeVal.append(valeur)
        validite,comm,comm2,listeRetour=self.politique.AjoutValeurs(liste,index,listeVal)
        self.Commentaire.setText(comm2)
        if not validite :
                self.editor.affiche_infos(comm)
        else:
           self.LEValeur.setText(QString(""))
           l1=self.listeValeursCourantes[:indexListe]
           l3=self.listeValeursCourantes[indexListe:]
           for valeur in  self.DecoupeListeValeurs(listeRetour) :
               if (self.nbValeurs==2):
                    str_valeur=str(valeur[0])+","+str(valeur[1])
               else:
                    str_valeur=str(valeur[0])+","+str(valeur[1])+","+str(valeur[2])
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
           self.editor.affiche_infos(texte)
           return
        listeDecoupee=self.DecoupeListeValeurs(liste)
        for vals in listeDecoupee :
            self.Ajout1Valeur(vals)
           

  def Sup1Valeur(self):
        index=self.LBValeurs.currentRow()
        if index == None : return
        self.LBValeurs.takeItem(index)
        listeVal=[]
        i=0
        for valeur in self.listeValeursCourantes :
                if self.nbValeurs == 2 :
                   if (i != index*2 and i != index*2+1 ) : listeVal.append(valeur)
                elif self.nbValeurs == 3 :
                   if (i != index*3 and i != index*3+1 and i != index*3 +2) : listeVal.append(valeur)
                else :
                   print "aiiiiiiiiiiiiiiiiiieeee"
                i = i+1
        self.listeValeursCourantes=listeVal
        listeValeurs=self.listeValeursCourantes

