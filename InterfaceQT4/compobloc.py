# -*- coding: utf-8 -*-

from PyQt4 import *
from PyQt4.QtGui import *
from Editeur     import Objecttreeitem

import compofact
import browser
import typeNode


class Node(browser.JDCNode,typeNode.PopUpMenuNodeMinimal):
    def getPanel(self):
        """        
        """    
        from monMCFactPanel import MonMCFactPanel
        return MonMCFactPanel(self,parent=self.editor)

    def createPopUpMenu(self):
        typeNode.PopUpMenuNodeMinimal.createPopUpMenu(self)



class BLOCTreeItem(compofact.FACTTreeItem):
  itemNode=Node

  def get_objet(self,name) :
      for v in self.object.mc_liste:
          if v.nom == name : return v
      return None
    
  def iscopiable(self):
    return 0


import Accas
treeitem = BLOCTreeItem
objet = Accas.MCBLOC   