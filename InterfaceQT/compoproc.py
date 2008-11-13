# -*- coding: utf-8 -*-
from Editeur     import Objecttreeitem
import compooper
import browser
import typeNode

from qt import *

class Node(browser.JDCNode,typeNode.PopUpMenuNode):
    def getPanel(self):
        from monMacroPanel import MonMacroPanel
        return MonMacroPanel(self,parent=self.editor)

    def createPopUpMenu(self):
        typeNode.PopUpMenuNode.createPopUpMenu(self)


class ProcEtapeTreeItem(compooper.EtapeTreeItem):
    itemNode=Node
  
import Accas
treeitem = ProcEtapeTreeItem
objet = Accas.PROC_ETAPE    

