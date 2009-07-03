# -*- coding: utf-8 -*-

from Editeur     import Objecttreeitem
from Extensions  import commentaire 
import browser

class Node(browser.JDCNode):

    def getPanel(self):
        from monRacinePanel import MonRacinePanel
        return MonRacinePanel(self,parent=self.editor)


    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)

class NIVEAUTreeItem(Objecttreeitem.ObjectTreeItem):
  itemNode=Node

  def isactif(self):
      return self.object.isactif()
    
  def IsExpandable(self):
      return 1
    
  def GetLabelText(self):
      """ Retourne 3 valeurs :
        - le texte a  afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
      """
      if self.isactif():
          fonte = Fonte_Niveau
      else :
          fonte = Fonte_Niveau_inactif
      return self.labeltext,fonte,None
    
  def GetIconName(self):
      if self.isactif():
          if self.object.isvalid():
              return "ast-green-text"
          else:
              return "ast-red-text"
      else:
          return "ast-white-text"
  
  def keys(self):
      if self.object.etapes_niveaux != []:
          return range(len(self.object.etapes_niveaux))
      else:
          return range(len(self.object.etapes))

  def GetSubList(self):
    sublist=[]
    for key in self.keys():
      if self.object.etapes_niveaux != []:
          liste = self.object.etapes_niveaux
      else:
          liste = self.object.etapes
      try:
        value = liste[key]
      except KeyError:
        continue
      def setfunction(value, key=key, object=liste):
        object[key] = value
      item =self.make_objecttreeitem(self.appli,value.ident() + " : ", value, setfunction)
      sublist.append(item)
    return sublist

  def additem(self,name,pos):
      if isinstance(name,Objecttreeitem.TreeItem) :
          cmd=self.object.addentite(name.getObject(),pos)
      else :
          cmd = self.object.addentite(name,pos)
      item = self.make_objecttreeitem(self.appli,cmd.nom + " : ", cmd)
      return item

  def suppitem(self,item) :
    # item = item de l'ETAPE à supprimer du JDC
    # item.getObject() = ETAPE ou COMMENTAIRE
    # self.object = JDC
    itemobject=item.getObject()
    if self.object.suppentite(itemobject):
       if isinstance(item.object,commentaire.COMMENTAIRE):
          message = "Commentaire supprimé"
       else :
          message = "Commande " + itemobject.nom + " supprimée"
       self.appli.affiche_infos(message)
       return 1
    else:
       self.appli.affiche_infos("Pb interne : impossible de supprimer cet objet")
       return 0

  def GetText(self):
      return ''

    
import Accas
treeitem = NIVEAUTreeItem
objet = Accas.ETAPE_NIVEAU    
