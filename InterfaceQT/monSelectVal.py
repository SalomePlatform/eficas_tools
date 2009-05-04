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
# Modules Eficas

from desSelectVal import DSelVal
from qt import *

# Import des panels

class MonSelectVal(DSelVal):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,file,parent,name = None,fl = 0):
        self.FonctPanel=parent
        DSelVal.__init__(self,parent,name,Qt.WType_Dialog)
        self.dictSepar={}
        self.separateur=" "
        self.texte=" "
        self.textTraite=""
        self.file=str(file)
        self.readVal()
        self.initVal()

  def readVal(self):
        if self.file == "" : return
        f = open(self.file, "rb")
        self.texte = f.read()
        f.close()

  def initVal(self):
        self.TBtext.clear()
        self.TBtext.setText(self.texte)
        self.dictSepar["virgule"]=","
        self.dictSepar["point-virgule"]=";"
        self.dictSepar["espace"]=" "

  def SeparateurSelect(self,numero):
        monBouton=self.BGSeparateur.find(numero)
        self.separateur=self.dictSepar[str(monBouton.text())]
        
  def BImportSelPressed(self):
        text=str(self.TBtext.selectedText())
        self.textTraite=text
        if self.textTraite == "" : return
        self.Traitement()
        
  def BImportToutPressed(self):
        self.textTraite=self.texte
        self.Traitement()

  def Traitement(self):
        import string
        if self.textTraite[-1]=="\n" : self.textTraite=self.textTraite[0:-1]
        self.textTraite=string.replace(self.textTraite,"\n",self.separateur)
        liste1=self.textTraite.split(self.separateur)
        liste=[]
        for val in liste1 :
            if val != '' and val != ' ' and val != self.separateur :
               val=str(val)
               try :
                 val2=eval(val,{})
                 liste.append(val)
               except :
                 pass
        self.FonctPanel.AjoutNValeur(liste) 
