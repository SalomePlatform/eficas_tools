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
# Modules Eficas

from desWidgetParam import Ui_WidgetParam
from gereIcones import FacultatifOuOptionnel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException
import Accas 
import os, re
import string
import types

pattern_name       = re.compile(r'^[^\d\W]\w*\Z')

    
# Import des panels

class MonWidgetParam(QWidget,Ui_WidgetParam,FacultatifOuOptionnel):
  """
  """
  def __init__(self,node,editor,commentaire):
      QWidget.__init__(self,None)
      self.node=node
      self.node.fenetre=self
      self.setupUi(self)
      self.editor=editor
      self.setIconePoubelle()
      self.remplit()
      if self.editor.code in ['MAP','CARMELCND'] : self.bCatalogue.close()
      else : self.connect(self.bCatalogue,SIGNAL("clicked()"), self.afficheCatalogue)
      self.connect(self.lineEditVal,SIGNAL("returnPressed()"),self.LEValeurPressed)
      self.connect(self.lineEditNom,SIGNAL("returnPressed()"),self.LENomPressed)
      self.connect(self.bAvant,SIGNAL("clicked()"), self.afficheAvant)
      self.connect(self.bApres,SIGNAL("clicked()"), self.afficheApres)
      self.connect(self.bVerifie,SIGNAL("clicked()"), self.verifiePressed)
      self.editor.affiche_infos("")


       
  def afficheCatalogue(self):
      self.node.tree.racine.affichePanneau()
      if self.node : self.node.select()
      else : self.node.tree.racine.select()

  def remplit(self):
      nom=self.node.item.get_nom()
      self.lineEditNom.setText(nom)

      valeur=self.node.item.get_valeur()
      if valeur == None : 
         self.lineEditVal.clear()
      elif type(valeur) == types.ListType :
         texte="["
         for l in valeur :
           texte=texte+str(l) +","
         texte=texte[0:-1]+"]"
         self.lineEditVal.setText(texte)
      else :
         self.lineEditVal.setText(str(valeur))


  def donnePremier(self):
      self.lineEditVal.setFocus(7)

  def LEValeurPressed(self):
      if self.verifiePressed() == False :
         QMessageBox.warning( self,tr( "Modification Impossible"),tr( "le parametre n'est pas valide"))
      nom=str(self.lineEditNom.text())
      val=str(self.lineEditVal.text())
      self.node.item.set_nom(nom)
      self.node.item.set_valeur(val)
      self.node.update_texte()
      self.node.update_node_valid()

  def LENomPressed(self):
      self.LEValeurPressed()

  def verifiePressed(self):
        nomString=str(self.lineEditNom.text())
        if not pattern_name.match(nomString) : 
           self.LECommentaire.setText(nomString + tr(" n est pas un identifiant correct"))
           return False

        valString=str(self.lineEditVal.text())

        contexte={}
        exec "from math import *" in contexte
        jdc=self.node.item.get_jdc()
        for p in jdc.params :
           try:
              tp=p.nom+'='+str(repr(p.valeur))
              exec tp  in contexte
           except exc :
              pass

        monTexte=nomString+"="+valString
        try :
          exec monTexte in contexte
        except (ValueError,TypeError, NameError,RuntimeError,ZeroDivisionError),  exc:
          self.LECommentaire.setText(tr("Valeur incorrecte: ")+unicode (exc))
          return False
        except :
          self.LECommentaire.setText(tr("Valeur incorrecte "))
          return False

        self.LECommentaire.setText(tr("Valeur correcte "))
        return True

  def afficheApres(self):
       self.node.selectApres()

  def afficheAvant(self):
       self.node.selectAvant()


