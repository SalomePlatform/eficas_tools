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
import traceback

class MCLISTPanel(panels.Panel):
    def init(self):
        test_ajout = self.node.item.ajout_possible()
        nom_mcfact = self.node.item.get_nom()
        if test_ajout:
            texte = "Pour ajouter une autre occurrence du mot-cl� facteur %s, cliquez ci-dessous" %nom_mcfact
        else:
            texte = "Vous ne pouvez pas ajouter une autre occurrence du mot-cl� facteur %s ?" %nom_mcfact
        self.label = Label(self,text = texte)
        self.label.place(relx=0.5,rely=0.4,anchor='center')
        if test_ajout:
            self.but=Button(self,text="AJOUTER",command=self.ajout_occurrence)
            self.but.place(relx=0.5,rely=0.6,anchor='center')
            #Button(self,text="NON",command=None).place(relx=0.6,rely=0.6,anchor='center')

    def ajout_occurrence(self,event=None):
        self.node.parent.append_child(self.node.item.get_nom())

import compofact
import treewidget
class Node(treewidget.Node):
    def doPaste(self,node_selected):
        objet_a_copier = self.item.get_copie_objet()
        child=node_selected.doPaste_MCF(objet_a_copier)
        #print "doPaste",child
        return child

    def doPaste_MCF(self,objet_a_copier):
        if self.item.isMCList() :
          # le noeud courant est une MCList
          child = self.append_child(objet_a_copier,pos='first',retour='oui')
          #child = self.parent.append_child(objet_a_copier,pos='first',retour='oui')
        elif self.item.isMCFact() :
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
                   "Vous ne pouvez coller le mot-cl� facteur copi� � ce niveau de l'arborescence !")
          self.appli.affiche_infos("Copie refus�e")
          child=None
        #print "doPaste_MCF",child
        return child

    def replace_enfant(self,item):
        """ Retourne le noeud fils � �ventuellement remplacer """
        raise "OBSOLETE"
        if self.item.isMCList():return None
        return self.get_node_fils(item.get_nom())

    def verif_condition(self):
        raise "OBSOLETE"
        if self.item.isMCList():
           self.children[-1].verif_condition()
        else:
           treewidget.Node.verif_condition(self)

    def after_delete(self):
        """ Dans le cas d'une MCList il faut v�rifier qu'elle n'est pas vide
            ou r�duite � un seul �l�ment suite � une destruction
        """
        raise "OBSOLETE"
        # self repr�sente une MCList
        if len(self.item) == 0 :
            # la liste est vide : il faut la supprimer
            self.delete()
        elif len(self.item) == 1:
            # il ne reste plus qu'un �l�ment dans la liste
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
            Supprime child des enfants de self, tous les id associ�s
            ET l'objet associ�
        """
        raise "OBSOLETE"
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
	Elle adapte ces objets pour leur permettre d'etre int�gr�s en tant que
	noeuds dans un arbre graphique (voir treewidget.py et ObjectTreeItem.py).
	Cette classe d�l�gue les appels de m�thode et les acc�s
	aux attributs � l'objet du noyau soit manuellement soit 
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
            Si la liste ne contient qu'un mot cl� facteur, on utilise le panneau
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
        """ Retourne la cl� de doc de l'objet point� par self """
        return self.object.get_docu()    

    def iscopiable(self):
	if len(self._object) > 1:
	   return Objecttreeitem.SequenceTreeItem.iscopiable(self)
	else:
	   return compofact.FACTTreeItem.iscopiable(self)

    def isMCFact(self):
        """
        Retourne 1 si l'objet point� par self est un MCFact, 0 sinon
        """
	return len(self._object) <= 1

    def isMCList(self):
        """
        Retourne 1 si l'objet point� par self est une MCList, 0 sinon
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
           message = "Mot-cl� " + obj.nom + " supprim�"
           self.appli.affiche_infos(message)
           return 1
        else:
           self.appli.affiche_infos('Impossible de supprimer ce mot-cl�')
           return 0

	    
import Accas
objet = Accas.MCList    

def treeitem(appli,labeltext,object,setfunction):
  """ Factory qui produit un objet treeitem adapte a un objet 
      Accas.MCList (attribut objet de ce module)
  """
  return MCListTreeItem(appli,labeltext,object,setfunction)
