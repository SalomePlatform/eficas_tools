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

from determine import monEnvQT5
if monEnvQT5:
    from PyQt5.QtCore import Qt
else :
    from PyQt4.QtGui  import *
    from PyQt4.QtCore import *

# Modules Eficas
from Extensions.i18n import tr

from feuille               import Feuille
from politiquesValidation  import PolitiqueUnique
from qtSaisie              import SaisieValeur


class MonWidgetSimpTuple(Feuille):

  def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
        Feuille.__init__(self,node,monSimpDef,nom,objSimp,parentQt,commande)
        self.politique=PolitiqueUnique(self.node,self.editor)
        self.parentQt.commandesLayout.insertWidget(-1,self)
        self.setFocusPolicy(Qt.StrongFocus)

  def setValeurs(self):
       valeur=self.node.item.get_valeur()
       for i in range(self.nbValeurs) :
           nomLineEdit="lineEditVal"+str(i+1)
           courant=getattr(self,nomLineEdit)
           if valeur !=None: courant.setText(str(valeur[i]))
           setattr(self,nomLineEdit,courant)
           if monEnvQT5: courant.returnPressed.connect(self.valeursPressed)
           else : self.connect(courant,SIGNAL("returnPressed()"),self.valeursPressed)

  def valeursPressed(self):
      aLeFocus=self.focusWidget()
      self.editor.affiche_infos("")
      texteValeur=""
      for i in range(self.nbValeurs) :
          nomLineEdit="lineEditVal"+str(i+1)
          courant=getattr(self,nomLineEdit)
          if courant.text()=="" or courant.text()==None :
             courant.setFocus(True)
             return 
          s=str(courant.text())
          if hasattr(self.objSimp.definition.validators, 'typeDesTuples'):
           if self.objSimp.definition.validators.typeDesTuples[i] == "R" :
             if (s.find('.')== -1 and s.find('e')== -1 and s.find('E')==-1) : 
                 s=s+'.0'
                 courant.setText(s)
           if self.objSimp.definition.validators.typeDesTuples[i] == "TXM" :
             if s[0]!='"' and s[0] != "'": 
                if s[-1]=="'": s="'"+s
                else :         s='"'+s
             if s[-1]!='"' and s[-1] != "'": 
                if s[0]=="'": s=s+"'"
                else :        s=s+'"'
             courant.setText(s)
          texteValeur+=str(courant.text())
          if i+1 != self.nbValeurs : texteValeur+=','
      validite,commentaire=self.politique.RecordValeur(texteValeur)
      if not validite:self.editor.affiche_infos(commentaire+" "+str(self.objSimp.definition.validators.typeDesTuples),Qt.red)

      # Passage au champ suivant
      nom=aLeFocus.objectName()[11:]
      i=nom.toInt()[0]+1
      if i == self.nbValeurs +1 : i=1
      nomLineEdit="lineEditVal"+str(i)
      courant=getattr(self,nomLineEdit)
      courant.setFocus(True)
          
         
