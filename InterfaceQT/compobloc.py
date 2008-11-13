# -*- coding: utf-8 -*-

from qt import *
from Editeur     import Objecttreeitem

import compofact
import browser


class Node(browser.JDCNode):
    def getPanel(self):
        """        
        """    
        from monMCFactPanel import MonMCFactPanel
        return MonMCFactPanel(self,parent=self.editor)


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
