# -*- coding: utf-8 -*-

from Editeur import Objecttreeitem
import browser


class Node(browser.JDCNode):
    def getPanel(self):
        """
        """
        from monRacinePanel import MonRacinePanel
        return MonRacinePanel(self,parent=self.editor)



class JDCTreeItem(Objecttreeitem.ObjectTreeItem):
  itemNode=Node
  
  def IsExpandable(self):
    return 1

  def GetText(self):
      return  "    "

  def GetLabelText(self):
      # None --> fonte et couleur par défaut
      return self.object.nom,None,None

  def get_jdc(self):
    """
    Retourne l'objet pointé par self
    """
    return self.object
  
  def GetIconName(self):
    if self.object.isvalid():
      return "ast-green-square"
    else:
      return "ast-red-square"

  def keys(self):
      if self.object.etapes_niveaux != []:
          return range(len(self.object.etapes_niveaux))
      else:
          return range(len(self.object.etapes))

  def additem(self,name,pos):
      cmd = self._object.addentite(name,pos)
      return cmd

  def suppitem(self,item) :
    # item             = item de l'ETAPE à supprimer du JDC
    # item.getObject() = ETAPE ou COMMENTAIRE
    # self.object      = JDC

    itemobject=item.getObject()
    if self.object.suppentite(itemobject):
       if itemobject.nature == "COMMENTAIRE" :
          message = "Commentaire supprimé"
       else :
          message = "Commande " + itemobject.nom + " supprimée"
       self.appli.affiche_infos(message)
       return 1
    else:
       self.appli.affiche_infos("Pb interne : impossible de supprimer cet objet",Qt.red)
       return 0

  def GetSubList(self):
    """
       Retourne la liste des items fils de l'item jdc.
       Cette liste est conservee et mise a jour a chaque appel
    """
    if self.object.etapes_niveaux != []:
        liste = self.object.etapes_niveaux
    else:
        liste = self.object.etapes
    sublist=[None]*len(liste)
    # suppression des items lies aux objets disparus
    for item in self.sublist:
       old_obj=item.getObject()
       if old_obj in liste:
          pos=liste.index(old_obj)
          sublist[pos]=item
       else:
          pass # objets supprimes ignores
    # ajout des items lies aux nouveaux objets
    pos=0
    for obj in liste:
       if sublist[pos] is None:
          # nouvel objet : on cree un nouvel item
          item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj)
          sublist[pos]=item
       pos=pos+1

    self.sublist=sublist
    return self.sublist

  def get_l_noms_etapes(self):
      """ Retourne la liste des noms des étapes de self.object"""
      return self.object.get_l_noms_etapes()

  def get_liste_cmd(self):
      listeCmd = self.object.niveau.definition.get_liste_cmd()
      return listeCmd

import Accas
treeitem =JDCTreeItem
objet = Accas.JDC    
