#@ MODIF compomclist Editeur  DATE 02/07/2001   AUTEUR D6BHHJP J.P.LEFEBVRE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
from Tkinter import *
import Pmw
import Objecttreeitem
import panels

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
            Button(self,text="AJOUTER",command=self.ajout_occurrence).place(relx=0.5,rely=0.6,anchor='center')
            #Button(self,text="NON",command=None).place(relx=0.6,rely=0.6,anchor='center')

    def ajout_occurrence(self,event=None):
        self.node.parent.append_child(self.node.item.get_nom())

class MCListTreeItem(Objecttreeitem.SequenceTreeItem):
    panel = MCLISTPanel

    def get_docu(self):
        """ Retourne la cl� de doc de l'objet point� par self """
        return self.object.get_docu()    

    def isMCFact(self):
        """
        Retourne 1 si l'objet point� par self est un MCFact, 0 sinon
        """
        return 0

    def isMCList(self):
        """
        Retourne 1 si l'objet point� par self est une MCList, 0 sinon
        """
        return 1
	
    def additem(self,obj,pos):
        """
	Ajoute un objet MCFACT � la MCList (self.object) � la position pos
	"""
	self.object.init_modif()
	obj.verif_existence_sd()
	obj.reparent(self.object.parent)
	self.object.insert(pos,obj)
        item = self.make_objecttreeitem(self.appli, obj.nom + ":", obj)
        return item  

    def suppitem(self,item):
        """
	Retire un objet MCFACT de la MCList (self.object) 
	"""
        self.object.init_modif()
        self.object.remove(item.object)
        # la liste peut �tre retourn�e vide !
        message = "Mot-cl� " + item.object.nom + " supprim�"
        self.appli.affiche_infos(message)
        return 1
	    
import Accas
treeitem = MCListTreeItem
objet = Accas.MCList    

