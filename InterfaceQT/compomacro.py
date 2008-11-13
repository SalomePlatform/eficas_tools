# -*- coding: utf-8 -*-

# Modules Python
import os,sys,string
import types
import traceback
from qt import *

# Modules Eficas
from Editeur import Objecttreeitem
import compooper
import browser
import typeNode


class MACRONode(browser.JDCNode,typeNode.PopUpMenuNode):         
    def getPanel(self):
      from   monMacroPanel import MonMacroPanel
      return MonMacroPanel (self,parent=self.editor )
    
    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)
        
    
class MACROTreeItem(compooper.EtapeTreeItem):
#  """ Cette classe hérite d'une grande partie des comportements
#      de la classe compooper.EtapeTreeItem
#  """
    itemNode=MACRONode

# ------------------------------------
#  Classes necessaires à INCLUDE
# ------------------------------------

class INCLUDETreeItemBase(MACROTreeItem):

    def __init__(self,appli, labeltext, object, setfunction):    
       MACROTreeItem.__init__(self,appli, labeltext, object, setfunction)

    def iscopiable(self):
       return 0


class INCLUDENode(browser.JDCNode,typeNode.PopUpMenuNode):    
    def getPanel(self):
      from   monIncludePanel import MonIncludePanel
      return MonIncludePanel (self,parent=self.editor )

    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)
      self.menu.insertItem( qApp.translate('Browser','Edit'), self.makeEdit )
      
    def makeEdit(self):    #,appli,node
        if self.item.object.text_converted == 0:
                # Le texte du fichier inclus n'a pas pu etre converti par le module convert
                msg="Le fichier de commande n'a pas pu etre converti pour etre editable par Eficas\n\n"
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
      from   monPoursuitePanel import MonPoursuitePanel
      return MonPoursuitePanel (self,parent=self.editor )

    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)
      self.menu.insertItem( qApp.translate('Browser','Edit'), self.makeEdit )

    def makeEdit(self):    #,appli,node
        if self.item.object.text_converted == 0:
                msg="Le fichier de commande n'a pas pu etre converti pour etre editable par Eficas\n\n"
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
#  Classes necessaires à INCLUDE MATERIAU
# ----------------------------------------
    

class MATERIAUNode(MACRONode):

    def getPanel(self):
      from   monMacroPanel import MonMacroPanel
      return MonMacroPanel (self,parent=self.editor )

    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)
      self.menu.insertItem( qApp.translate('Browser','View'), self.makeView )

    def makeView(self) :
      if hasattr(self.item.object,'fichier_ini') and self.item.object.fichier_ini==None:
         QMessageBox.information( self, "Include vide","L'include doit etre correctement initialisé pour etre visualisé")
         return
      f = open(self.item.object.fichier_ini, "rb")
      texte = f.read()
      f.close()
      from desVisu import DVisu
      monVisu=DVisu(parent=self.editor,fl=Qt.WType_Dialog)
      monVisu.TB.setText(texte)
      monVisu.show()

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
   elif object.nom == "INCLUDE":
      return INCLUDETreeItem(appli, labeltext, object, setfunction)
   elif object.nom == "POURSUITE":
      return POURSUITETreeItem(appli, labeltext, object, setfunction)
   else:
      return MACROTreeItem(appli, labeltext, object, setfunction)

import Accas
objet=Accas.MACRO_ETAPE
    

