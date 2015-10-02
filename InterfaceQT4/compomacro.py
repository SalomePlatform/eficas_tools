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
import os,sys,string
import types
import traceback

# Modules Eficas
from Editeur import Objecttreeitem
from Extensions.i18n import tr
import compooper
import browser
import typeNode
from PyQt4.QtGui import QAction
from PyQt4.QtCore import Qt, SIGNAL, QVariant


class MACRONode(browser.JDCNode,typeNode.PopUpMenuNode):         
    
    def getPanel(self):
      from   monWidgetCommande import MonWidgetCommande
      return MonWidgetCommande (self,self.editor ,self.item.object)


    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)
      if ("AFFE_CARA_ELEM" in self.item.get_genealogie()) and self.editor.salome:
           self.ViewElt = QAction(tr('View3D'),self.tree)
           self.tree.connect(self.ViewElt,SIGNAL("triggered()"),self.view3D)
           self.ViewElt.setStatusTip(tr("affiche dans Geom les elements de structure"))
           self.menu.addAction(self.ViewElt)
           if self.item.isvalid() :
              self.ViewElt.setEnabled(1)
           else:
              self.ViewElt.setEnabled(0)

    def view3D(self) :
        from Editeur import TroisDPal
        troisD=TroisDPal.TroisDPilote(self.item,self.editor.appliEficas)
        troisD.envoievisu()

        

    
class MACROTreeItem(compooper.EtapeTreeItem):
#  """ Cette classe hérite d'une grande partie des comportements
#      de la classe compooper.EtapeTreeItem
#  """
    itemNode=MACRONode

# ------------------------------------
#  Classes necessaires a INCLUDE
# ------------------------------------

class INCLUDETreeItemBase(MACROTreeItem):

    def __init__(self,appli, labeltext, object, setfunction):    
       MACROTreeItem.__init__(self,appli, labeltext, object, setfunction)

    def iscopiable(self):
       return 0


class INCLUDENode(browser.JDCNode,typeNode.PopUpMenuNode):    

    def getPanel(self):
      from   monWidgetCommande import MonWidgetCommande
      return MonWidgetCommande (self,self.editor ,self.item.object)

    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)
      
    def makeEdit(self):    #,appli,node
        if self.item.object.text_converted == 0:
                # Le texte du fichier inclus n'a pas pu etre converti par le module convert
                msg=tr("Le fichier de commande n'a pas pu etre converti pour etre editable par Eficas\n\n")
                msg=msg+self.item.object.text_error
                return
    
        if not hasattr(self.item.object,"jdc_aux") or self.item.object.jdc_aux is None:
               #L'include n'est pas initialise
               self.item.object.build_include(None,"")
    
        # On cree un nouvel onglet dans le bureau
        self.editor.vm.displayJDC( self.item.object.jdc_aux , self.item.object.jdc_aux.nom )
     

class INCLUDETreeItem(INCLUDETreeItemBase):
    itemNode=INCLUDENode
    

# ------------------------------------
#  Classes necessaires à POURSUITE
# ------------------------------------
    
class POURSUITENode(browser.JDCNode, typeNode.PopUpMenuNode):    

    def getPanel(self):
      from   monWidgetCommande import MonWidgetCommande
      return MonWidgetCommande (self,self.editor ,self.item.object)

    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)

    def makeEdit(self):    #,appli,node
        if self.item.object.text_converted == 0:
                msg=tr("Le fichier de commande n'a pas pu etre converti pour etre editable par Eficas\n\n")
                msg=msg+self.item.object.text_error
                return
    
        if not hasattr(self.item.object,"jdc_aux") or self.item.object.jdc_aux is None:
            text="""DEBUT()
                    FIN()"""
            self.object.build_poursuite(None,text)
    
        # On cree un nouvel onglet dans le bureau
        self.editor.vm.displayJDC( self.item.object.jdc_aux , self.item.object.jdc_aux.nom)
    
class POURSUITETreeItem(INCLUDETreeItemBase):
  itemNode=POURSUITENode


# ----------------------------------------
#  Classes necessaires a INCLUDE MATERIAU
# ----------------------------------------
    

class MATERIAUNode(MACRONode):

    def getPanel(self):
      from   monWidgetCommande import MonWidgetCommande
      return MonWidgetCommande (self,self.editor ,self.item.object)

    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)

    def makeView(self) :
      if hasattr(self.item.object,'fichier_ini') and self.item.object.fichier_ini==None:
         QMessageBox.information( self,tr("Include vide"),tr("L'include doit etre correctement initialise pour etre visualise"))
         return
      f = open(self.item.object.fichier_ini, "rb")
      texte = f.read()
      f.close()
      from desVisu import DVisu
      monVisuDialg=DVisu(parent=self.editor.appliEficas,fl=0)
      monVisuDialg.TB.setText(texte)
      monVisuDialg.show()


class INCLUDE_MATERIAUTreeItem(INCLUDETreeItemBase):
    itemNode=MATERIAUNode

# ------------------------------------
# TreeItem
# ------------------------------------
    

def treeitem(appli, labeltext, object, setfunction=None):
   """ Factory qui retourne l'item adapte au type de macro : 
       INCLUDE, POURSUITE, MACRO
   """
   if object.nom == "INCLUDE_MATERIAU":
      return INCLUDE_MATERIAUTreeItem(appli, labeltext, object, setfunction)
   elif object.nom == "INCLUDE" or object.nom== "DICTDATA":
      return INCLUDETreeItem(appli, labeltext, object, setfunction)
   elif object.nom == "POURSUITE":
      return POURSUITETreeItem(appli, labeltext, object, setfunction)
   else:
      return MACROTreeItem(appli, labeltext, object, setfunction)

import Accas
objet=Accas.MACRO_ETAPE
    

