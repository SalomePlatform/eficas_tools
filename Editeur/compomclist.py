# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
import types
from Tkinter import *
import Pmw
import Objecttreeitem
import panels

class MCLISTPanel(panels.Panel):
    def init(self):
        test_ajout = self.node.item.ajout_possible()
        nom_mcfact = self.node.item.get_nom()
        if test_ajout:
            texte = "Pour ajouter une autre occurrence du mot-clé facteur %s, cliquez ci-dessous" %nom_mcfact
        else:
            texte = "Vous ne pouvez pas ajouter une autre occurrence du mot-clé facteur %s ?" %nom_mcfact
        self.label = Label(self,text = texte)
        self.label.place(relx=0.5,rely=0.4,anchor='center')
        if test_ajout:
            Button(self,text="AJOUTER",command=self.ajout_occurrence).place(relx=0.5,rely=0.6,anchor='center')
            #Button(self,text="NON",command=None).place(relx=0.6,rely=0.6,anchor='center')

    def ajout_occurrence(self,event=None):
        self.node.parent.append_child(self.node.item.get_nom())


import compofact
import treewidget
class Node(treewidget.Node):
    def doPaste(self,node_selected):
        objet_a_copier = self.item.get_copie_objet()
        child=node_selected.doPaste_MCF(objet_a_copier)
        return child

    def doPaste_MCF(self,objet_a_copier):
        if self.item.isMCList() :
          # le noeud courant est une MCList
          child = self.parent.append_child(objet_a_copier,pos='first',retour='oui')
        elif self.item.isMCFact():
          # le noeud courant est un MCFACT
          if self.parent.item.isMCList():
             # le noeud selectionne est un MCFACT dans une MCList
             child = self.parent.append_child(objet_a_copier,
                                              pos=self.item,
                                              retour='oui')
          else:
             # le noeud MCFACT selectionne n'est pas dans une MCList
             child = self.parent.append_child(objet_a_copier,retour='oui')
        else:
          showinfo("Copie impossible",
                   "Vous ne pouvez coller le mot-clé facteur copié à ce niveau de l'arborescence !")
          self.appli.affiche_infos("Copie refusée")
          child=None
        return child

    def replace_enfant(self,item):
        """ Retourne le noeud fils à éventuellement remplacer """
        if self.item.isMCList():return None
        return self.get_node_fils(item.get_nom())

    def verif_condition(self):
        if self.item.isMCList():
           self.children[-1].verif_condition()
        else:
           treewidget.Node.verif_condition(self)

    def after_delete(self):
        """ Dans le cas d'une MCList il faut vérifier qu'elle n'est pas vide
            ou réduite à un seul élément suite à une destruction
        """
        # self représente une MCList
        if len(self.item) == 0 :
            # la liste est vide : il faut la supprimer
            self.delete()
        elif len(self.item) == 1:
            # il ne reste plus qu'un élément dans la liste
            noeud = self.children[0]
            # maintenant l'item mclist gere tout seul ce
            # changement
            self.delete_node_child(noeud)
            self.children=noeud.children or []
            self.state=noeud.state
        else :
            return

    def delete_child(self,child):
        """
            Supprime child des enfants de self, tous les id associés
            ET l'objet associé
        """
        if self.item.isMCList():
           if self.item.suppitem(child.item):
              self.delete_node_child(child)
              self.after_delete()
              return 1
           else :
              return 0
        else:
           if self.item.suppitem(child.item):
              self.delete_node_child(child)
              return 1
           else :
              return 0


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
	else:
	   return compofact.FACTPanel(jdcdisplay,pane,node)

    def IsExpandable(self):
	if len(self._object) > 1:
	   return Objecttreeitem.SequenceTreeItem.IsExpandable(self)
	else:
	   return compofact.FACTTreeItem.IsExpandable(self)

    def GetSubList(self):
        self.updateDelegate()
	if len(self._object) > 1:
	   return Objecttreeitem.SequenceTreeItem.GetSubList(self)
	else:
	   return compofact.FACTTreeItem.GetSubList(self)

    def GetIconName(self):
        if self._object.isvalid():
            return "ast-green-los"
        elif self._object.isoblig():
            return "ast-red-los"
        else:
            return "ast-yel-los"

    def get_docu(self):
        """ Retourne la clé de doc de l'objet pointé par self """
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
	
    def additem(self,obj,pos):
        """
	Ajoute un objet MCFACT à la MCList (self.object) à la position pos
	"""
	if len(self._object) <= 1:
	   return compofact.FACTTreeItem.additem(self,obj,pos)

        if type(obj)==types.StringType :
          # on est en mode création d'un motcle
          raise "traitement non prevu"

        if not self._object.ajout_possible():
           return None

        if self._object.nom != obj.nom:
           return None

	self.object.init_modif()
	obj.verif_existence_sd()
	obj.reparent(self.object.parent)
	self.object.insert(pos,obj)
	self.object.fin_modif()

        item = self.make_objecttreeitem(self.appli, obj.nom + ":", obj)
        return item  

    def suppitem(self,item):
        """
	Retire un objet MCFACT de la MCList (self.object) 
	"""
        obj=item.getObject()
	if len(self._object) <= 1:
	   return compofact.FACTTreeItem.suppitem(self,item)

        self.object.init_modif()
        self.object.remove(obj)
	if len(self._object) == 1:
           self.updateDelegate()
        message = "Mot-clé " + obj.nom + " supprimé"
        self.appli.affiche_infos(message)
        return 1
	    
import Accas
objet = Accas.MCList    

def treeitem(appli,labeltext,object,setfunction):
  """ Factory qui produit un objet treeitem adapte a un objet 
      Accas.MCList (attribut objet de ce module)
  """
  return MCListTreeItem(appli,labeltext,object,setfunction)
