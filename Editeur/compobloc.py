#@ MODIF compobloc Editeur  DATE 02/07/2001   AUTEUR D6BHHJP J.P.LEFEBVRE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
from Tkinter import *
import Pmw

import Objecttreeitem
import compofact


class BLOCTreeItem(compofact.FACTTreeItem):
  panel = compofact.FACTPanel

  def get_objet(self,name) :
      for v in self.object.mc_liste:
          if v.nom == name : return v
      return None
    
  def additem(self,name,pos):
      if isinstance(name,Objecttreeitem.ObjectTreeItem) :
          mcent=self.object.addentite(name.object,pos=pos)
      else :
          mcent = self.object.addentite(name,pos=pos)
      if mcent == 0 :
        # on ne peut ajouter l'élément de nom name
        return 0
      self.expandable=1
      def setfunction(value, object=mcent):
          object.setval(value)
      item = self.make_objecttreeitem(self.appli,mcent.nom + " : ", mcent, setfunction)
      return item

  def iscopiable(self):
    return 0
  
import Accas
treeitem = BLOCTreeItem
objet = Accas.MCBLOC   
