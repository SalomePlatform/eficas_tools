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

from desWidgetFormule import Ui_WidgetFormule
from gereIcones import FacultatifOuOptionnel
from determine import monEnvQT5

if monEnvQT5:
   from PyQt5.QtWidgets  import QWidget
   from PyQt5.QtGui import QIcon
   from PyQt5.QtCore import Qt
else :
   from PyQt4.QtGui import *
   from PyQt4.QtCore import *


from Extensions.i18n import tr
import Accas 
import os
import string

    
# Import des panels

class MonWidgetFormule(QWidget,Ui_WidgetFormule,FacultatifOuOptionnel):
  """
  """
  def __init__(self,node,editor,etape):
      #print "MonWidgetFormule ", self
      QWidget.__init__(self,None)
      self.node=node
      self.node.fenetre=self
      self.editor=editor
      self.appliEficas=self.editor.appliEficas
      self.repIcon=self.appliEficas.repIcon
      self.setupUi(self)
      
 
      self.setIconePoubelle()
      self.setIconesGenerales()
      self.setValeurs()
      self.setValide()

     
      if monEnvQT5 :
         #if self.editor.code in ['MAP','CARMELCND','CF'] : self.bCatalogue.close()
         if self.editor.code in ['MAP','CARMELCND'] : self.bCatalogue.close()
         else : self.bCatalogue.clicked.connect(self.afficheCatalogue)
         #if self.editor.code in ['Adao','MAP','CF'] : 
         if self.editor.code in ['Adao','MAP'] : 
               self.bAvant.close()
               self.bApres.close()
         else : 
               self.bAvant.clicked.connect(self.afficheAvant)
               self.bApres.clicked.connect(self.afficheApres)
         self.LENom.returnPressed.connect(self.nomChange)
         self.LENomFormule.returnPressed.connect(self.NomFormuleSaisi)
         self.LENomsArgs.returnPressed.connect(self.argsSaisis)
         self.LECorpsFormule.returnPressed.connect(self.FormuleSaisie)
      else : 
         if self.editor.code in ['MAP','CARMELCND'] : self.bCatalogue.close()
         else : self.connect(self.bCatalogue,SIGNAL("clicked()"), self.afficheCatalogue)
         if self.editor.code in ['Adao','MAP'] : 
               self.bAvant.close()
               self.bApres.close()
         else : 
               self.connect(self.bAvant,SIGNAL("clicked()"), self.afficheAvant)
               self.connect(self.bApres,SIGNAL("clicked()"), self.afficheApres)
         self.connect(self.LENom,SIGNAL("returnPressed()"),self.nomChange)
         self.connect(self.LENomFormule,SIGNAL("returnPressed()"),self.NomFormuleSaisi)
         self.connect(self.LENomsArgs,SIGNAL("returnPressed()"),self.argsSaisis)
         self.connect(self.LECorpsFormule,SIGNAL("returnPressed()"),self.FormuleSaisie)


   
      self.racine=self.node.tree.racine
      self.monOptionnel=None
      self.editor.fermeOptionnel()
      #print "fin init de widget Commande"
      

  def donnePremier(self):
      self.listeAffichageWidget[0].setFocus(7)


  def setValeurs(self):
        self.LENomFormule.setText(self.node.item.get_nom())
        self.LECorpsFormule.setText(self.node.item.get_corps())
        texte_args=""
        if self.node.item.get_args() != None :
            for i in self.node.item.get_args() :
                if texte_args != "" : texte_args = texte_args +","
                texte_args=texte_args + i
        self.LENomsArgs.setText(texte_args)


  def nomChange(self):
      nom = str(self.LENom.text())
      self.LENomFormule.setText(nom)
      self.NomFormuleSaisi()


  def afficheCatalogue(self):
      if self.editor.widgetOptionnel != None : self.monOptionnel.hide()
      self.racine.affichePanneau()
      if self.node : self.node.select()
      else : self.racine.select()

  def afficheApres(self):
       self.node.selectApres()

  def afficheAvant(self):
       self.node.selectAvant()

  def setValide(self):
      if not(hasattr (self,'RBValide')) : return
      icon = QIcon()
      if self.node.item.object.isvalid() :
         icon=QIcon(self.repIcon+"/ast-green-ball.png")
      else :
         icon=QIcon(self.repIcon+"/ast-red-ball.png")
      if self.node.item.GetIconName() == "ast-yellow-square" :
         icon=QIcon(self.repIcon+"/ast-yel-ball.png")
      self.RBValide.setIcon(icon)


  def NomFormuleSaisi(self):
      nomFormule = str(self.LENomFormule.text())
      if nomFormule == '' : return
      self.LENom.setText(nomFormule)
      test,erreur = self.node.item.verif_nom(nomFormule)
      if test :
         commentaire=nomFormule+tr(" est un nom valide pour une FORMULE")
         self.editor.affiche_infos(commentaire)
      else :
         commentaire=nomFormule+tr(" n'est pas un nom valide pour une FORMULE")
         self.editor.affiche_infos(commentaire,Qt.red)
         return
      if str(self.LENomsArgs.text()) != "" and  str(self.LECorpsFormule.text())!= "" : self.BOkPressedFormule()
      self.LENomsArgs.setFocus(7)

  def argsSaisis(self):
      arguments = str(self.LENomsArgs.text())
      if arguments == '' : return
      test,erreur = self.node.item.verif_arguments(arguments)
      if test:
         commentaire=tr("Argument(s) valide(s) pour une FORMULE")
         self.editor.affiche_infos(commentaire)
      else:
         commentaire=tr("Argument(s) invalide(s) pour une FORMULE")
         self.editor.affiche_infos(commentaire,Qt.red)
      if str(self.LECorpsFormule.text()) != "" and  str(self.LENomFormule.text())!= "" : self.BOkPressedFormule()
      self.LECorpsFormule.setFocus(7)

  def FormuleSaisie(self):
      nomFormule = str(self.LENomFormule.text())
      arguments  = str(self.LENomsArgs.text())
      expression = str(self.LECorpsFormule.text())
      if expression == '' : return
      test,erreur = self.node.item.verif_formule_python((nomFormule,"REEL",arguments,expression))

      if test:
         commentaire=tr("Corps de FORMULE valide")
         self.editor.affiche_infos(commentaire)
      else:
         commentaire=tr("Corps de FORMULE invalide")
         self.editor.affiche_infos(commentaire,Qt.red)
      if str(self.LENomsArgs.text()) != "" and  str(self.LENomFormule.text())!= "" : self.BOkPressedFormule()

  def BOkPressedFormule(self):
      #print dir(self)
      #if self.parent.modified == 'n' : self.parent.init_modif()

      nomFormule = str(self.LENomFormule.text())
      test,erreur = self.node.item.verif_nom(nomFormule)
      if not test :
         self.editor.affiche_infos(erreur,Qt.red)
         return

      arguments  = str(self.LENomsArgs.text())
      test,erreur = self.node.item.verif_arguments(arguments)
      if not test :
         self.editor.affiche_infos(erreur,Qt.red)
         return

      expression = str(self.LECorpsFormule.text())
      test,erreur = self.node.item.verif_formule_python((nomFormule,"REEL",arguments,expression))
      if not test :
         self.editor.affiche_infos(erreur,Qt.red)
         return

      test=self.node.item.object.update_formule_python(formule=(nomFormule,"REEL",arguments,expression))
      test,erreur = self.node.item.save_formule(nomFormule,"REEL",arguments,expression)
      if test :
         #self.node.update_texte()
         #self.node.update_label()
         #self.node.update_node()
         self.node.onValid()
         self.node.update_valid()
         commentaire = "Formule saisie"
         self.editor.affiche_infos(commentaire)
      else:
         commentaire ="Formule incorrecte : " + erreur
         self.editor.affiche_infos(commentaire,Qt.red)
      self.editor.init_modif()
