# -*- coding: utf-8 -*-

import types
import traceback

import compofact
import browser
import typeNode

from Editeur     import Objecttreeitem
from Noyau.N_OBJECT import ErrorObj
#import compoerror


class Node(browser.JDCNode,typeNode.PopUpMenuNodeMinimal):
    def getPanel(self):
        """        
        """    
        if self.item.isMCList() :
           if self.item.ajout_possible():
              from monMCListAjoutPanel import MonMCListAjoutPanel
              return MonMCListAjoutPanel(self,parent=self.editor)
           else :
              print "MCList"
        elif self.item.isMCFact() :
           from monMCFactPanel import MonMCFactPanel
           return MonMCFactPanel(self,parent=self.editor)
        else :
           print "MCList"

    def createPopUpMenu(self):
        typeNode.PopUpMenuNodeMinimal.createPopUpMenu(self)


    #def doPaste(self,node_selected):
    #    objet_a_copier = self.item.get_copie_objet()
    #    child=node_selected.doPasteMCF(objet_a_copier)
        #print "doPaste",child
    #    return child

    #def doPasteMCF(self,objet_a_copier):
    #    child=None
        # le noeud courant est une MCList
    #    if self.item.isMCList() :
    #      child = self.append_child(objet_a_copier,pos='first',retour='oui')

        # le noeud courant est un MCFACT
    #    elif self.item.isMCFact() :
          # le noeud selectionne est un MCFACT dans une MCList
    #      if self.parent.item.isMCList():
    #         child = self.parent.append_child(objet_a_copier, pos=self.item, retour='oui')

          # le noeud MCFACT selectionne n'est pas dans une MCList
    #      else:
    #         child = self.parent.append_child(objet_a_copier,retour='oui')

    #    else:
    #      QMessageBox.information( self, "Copie impossible",
    #               "Vous ne pouvez coller le mot-clé facteur copié à ce niveau de l'arborescence !")          
    #      self.editor.affiche_infos("Copie refusée")

    #    return child

class MCListTreeItem(Objecttreeitem.SequenceTreeItem,compofact.FACTTreeItem):
    """ La classe MCListTreeItem joue le role d'un adaptateur pour les objets
        du noyau Accas instances de la classe MCLIST.
        Elle adapte ces objets pour leur permettre d'etre intégrés en tant que
        noeuds dans un arbre graphique (voir treewidget.py et ObjectTreeItem.py).
        Cette classe délègue les appels de méthode et les accès
        aux attributs à l'objet du noyau soit manuellement soit 
        automatiquement (voir classe Delegate et attribut object).
    """
    itemNode=Node

    def init(self):
        # Si l'objet Accas (MCList) a moins d'un mot cle facteur
        # on utilise directement ce mot cle facteur comme delegue
        self.updateDelegate()

    def updateDelegate(self):
        if len(self._object) > 1:
           self.setdelegate(self._object)
        else:
           self.setdelegate(self._object.data[0])

    def panel(self,jdcdisplay,pane,node):
        """ Retourne une instance de l'objet panneau associe a l'item (self)
            Si la liste ne contient qu'un mot clé facteur, on utilise le panneau
            FACTPanel.
            Si la liste est plus longue on utilise le panneau MCLISTPanel.
        """
        if len(self._object) > 1:
           return MCLISTPanel(jdcdisplay,pane,node)
        elif isinstance(self._object.data[0],ErrorObj):
           return compoerror.ERRORPanel(jdcdisplay,pane,node)
        else:
           return compofact.FACTPanel(jdcdisplay,pane,node)

    def IsExpandable(self):
        if len(self._object) > 1:
           return Objecttreeitem.SequenceTreeItem.IsExpandable(self)
        else:
           return compofact.FACTTreeItem.IsExpandable(self)

    def GetSubList(self):
        self.updateDelegate()
        if len(self._object) <= 1:
           self._object.data[0].alt_parent=self._object
           return compofact.FACTTreeItem.GetSubList(self)

        liste=self._object.data
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
              def setfunction(value, object=obj):
                  object=value
              item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj, setfunction)
              sublist[pos]=item
              #Attention : on ajoute une information supplementaire pour l'actualisation de 
              # la validite. L'attribut parent d'un MCFACT pointe sur le parent de la MCLISTE
              # et pas sur la MCLISTE elle meme ce qui rompt la chaine de remontee des
              # informations de validite. alt_parent permet de remedier a ce defaut.
              obj.alt_parent=self._object
           pos=pos+1

        self.sublist=sublist
        return self.sublist

    def GetIconName(self):
        if self._object.isvalid():
            return "ast-green-los"
        elif self._object.isoblig():
            return "ast-red-los"
        else:
            return "ast-yel-los"

    def get_docu(self):
        """ Retourne la clef de doc de l'objet pointé par self """
        return self.object.get_docu()    

    def iscopiable(self):
        if len(self._object) > 1:
           return Objecttreeitem.SequenceTreeItem.iscopiable(self)
        else:
           return compofact.FACTTreeItem.iscopiable(self)

    def isMCFact(self):
        """
        Retourne 1 si l'objet pointé par self est un MCFact, 0 sinon
        """
        return len(self._object) <= 1

    def isMCList(self):
        """
        Retourne 1 si l'objet pointé par self est une MCList, 0 sinon
        """
        return len(self._object) > 1
        
    def get_copie_objet(self):
        return self._object.data[0].copy()

    def additem(self,obj,pos):
        #print "compomclist.additem",obj,pos
        if len(self._object) <= 1:
           return compofact.FACTTreeItem.additem(self,obj,pos)

        o= self.object.addentite(obj,pos)
        return o

    def suppitem(self,item):
        """
        Retire un objet MCFACT de la MCList (self.object) 
        """
        #print "compomclist.suppitem",item
        obj=item.getObject()
        if len(self._object) <= 1:
           return compofact.FACTTreeItem.suppitem(self,item)

        if self.object.suppentite(obj):
           if len(self._object) == 1: self.updateDelegate()     
           message = "Mot-clef " + obj.nom + " supprime"
           self.appli.affiche_infos(message)
           return 1
        else:
           self.appli.affiche_infos('Impossible de supprimer ce mot-clef',Qt.red)
           return 0

            
import Accas
objet = Accas.MCList    

def treeitem(appli,labeltext,object,setfunction):
  """ Factory qui produit un objet treeitem adapte a un objet 
      Accas.MCList (attribut objet de ce module)
  """
  return MCListTreeItem(appli,labeltext,object,setfunction)
