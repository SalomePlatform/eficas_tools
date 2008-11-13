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
"""
   Ce module contient les classes permettant de d�finir les objets graphiques
   repr�sentant un objet de type PARAMETRE, cad le panneau et l'item de l'arbre
   d'EFICAS
"""

# import modules Python
from Tkinter import *
import Pmw
import string

# import modules EFICAS
from Editeur import Objecttreeitem
import panels
import fontes


Fonte_PARAMETRE = fontes.standard_italique
Fonte_TITRE = fontes.standard_gras_souligne


class PARAMPanel(panels.OngletPanel):
  """
  Classe servant � construire le panneau associ� � un param�tre.
  C'est au moyen de ce panneau que l'utilisateur peut acc�der
  aux nom et valeur du param�tre en vue �ventuellement de les
  modifier.
  """

  def init(self):
    """
    Initialise les frame des panneaux contextuels relatifs � un PARAMETRE
    """
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    nb.pack(fill = 'both', expand = 1)
    self.nb=nb
    nb.add('Parametre', tab_text='Valeur Param�tre')
    nb.add('Commande', tab_text='Nouvelle Commande')
    nb.add('Commentaire',tab_text='Param�tre/Commentaire')
    self.makeParametrePage(nb.page("Parametre"))
    self.makeCommandePage(nb.page("Commande"))
    self.makeParamCommentPage_for_etape(nb.page("Commentaire"))
    nb.tab('Parametre').focus_set()
    nb.setnaturalsize()
    self.make_buttons()
    self.enlevebind()
    self.creebind()
    
  def makeParametrePage(self,page):
    """
    Cr�e la page qui permet d'afficher et d'�diter le texte du PARAMETRE
    """
    self.frame_valeur = Frame(page)
    #self.frame_valeur.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05,anchor='nw')
    self.frame_valeur.pack(expand=1)
    # affichage du titre du panneau
    self.titre = StringVar()
    self.titre.set("PARAMETRE "+self.node.item.get_nom())
    #Label(self.frame_valeur,textvariable=self.titre,font=Fonte_TITRE).place(relx=0.5,rely=0.1,anchor='n')
    Label(self.frame_valeur,textvariable=self.titre,font=Fonte_TITRE).grid(row=0,columnspan=2,padx=5,pady=5)
    # cr�ation des labels et entries associ�s aux nom et valeur du param�tre
    #Label(self.frame_valeur,text= 'Nom du param�tre : ').place(relx=0.,rely=0.3)
    Label(self.frame_valeur,text= 'Nom du param�tre : ').grid(row=1,sticky=W,padx=5,pady=5)
    self.entry_nom = Entry(self.frame_valeur)
    #Label(self.frame_valeur,text= 'Valeur du param�tre : ').place(relx=0.,rely=0.5)
    Label(self.frame_valeur,text= 'Valeur du param�tre : ').grid(row=2,sticky=W,padx=5,pady=5)
    self.entry_val = Entry(self.frame_valeur)
    # binding sur entry_nom
    self.entry_nom.bind("<Return>",lambda e,s=self : s.entry_val.focus())
    self.entry_val.bind("<Return>",lambda e,s=self : s.change_valeur())
    self.entry_nom.bind("<KP_Enter>",lambda e,s=self : s.entry_val.focus())
    self.entry_val.bind("<KP_Enter>",lambda e,s=self : s.change_valeur())
    # affichage des entries
    #self.entry_nom.place(relx=0.35,rely=0.3,relwidth=0.3)
    self.entry_nom.grid(row=1,column=1,sticky=W,padx=5,pady=5)
    #self.entry_val.place(relx=0.35,rely=0.5,relwidth=0.5)
    self.entry_val.grid(row=2,column=1,sticky=W,padx=5,pady=5)
    # affichage d'une phrase d'aide
    aide = """
    Un retour de chariot dans une zone de saisie vous permet de v�rifier si
    la valeur que vous avez entr�e est valide.
    Ce n'est qu'apr�s avoir appuy� sur le bouton Valider que les nouvelles
    valeurs seront effectivement prises en compte
    """
    #Label(self.frame_valeur,text=aide).place(relx=0.5,rely=0.65,anchor='n')
    Label(self.frame_valeur,text=aide).grid(row=3,columnspan=2,padx=5,pady=5)
    self.frame_valeur.columnconfigure(1,weight=1)
    # affichage des nom et valeur du param�tre
    self.display_valeur()
    self.entry_nom.focus()

  def make_buttons(self):
    """
    Cr�e les boutons du panneau
    """
    #self.bouton_sup.place_forget()
    #self.bouton_doc.place_forget()
    #self.bouton_val = Button(self.fr_but,text='Valider',command=self.change_valeur,width=14)
    #self.bouton_ann = Button(self.fr_but,text='Annuler',command=self.display_valeur,width=14)
    #self.bouton_val.place(relx=0.25,rely=0.5,relheight=0.8,anchor='center')
    #self.bouton_ann.place(relx=0.50,rely=0.5,relheight=0.8,anchor='center')
    #self.bouton_sup.place(relx=0.75,rely=0.5,relheight=0.8,anchor='center')

    self.bouton_sup.pack_forget()
    self.bouton_doc.pack_forget()
    self.bouton_val = Button(self.fr_but,text='Valider',command=self.change_valeur)
    self.bouton_ann = Button(self.fr_but,text='Annuler',command=self.display_valeur)
    self.bouton_val.pack(side='left',padx=5, pady=5)
    self.bouton_ann.pack(side='left',padx=5, pady=5)
    self.bouton_sup.pack(side='right',padx=5, pady=5)

  def change_valeur(self):
    """
    Stocke la nouvelle valeur donn�e par l'utilisateur comme valeur du PARAMETRE
    """
    if self.parent.modified == 'n' : self.parent.init_modif()
    new_nom = self.entry_nom.get()
    new_val = self.entry_val.get()
    self.node.item.set_nom(new_nom)
    self.node.item.set_valeur(new_val)
    self.node.update()
    self.display_valeur()
    
  def display_valeur(self):
    """
    Affiche dans self.widget_text la valeur de l'objet PARAMETRE
    (annule d'�ventuelles modifications faite par l'utilisateur)
    """
    self.entry_nom.delete(0,END)
    self.entry_val.delete(0,END)
    self.titre.set('PARAMETRE '+self.node.item.get_nom())
    self.entry_nom.insert(END,self.node.item.get_nom())
    self.entry_val.insert(END,self.node.item.get_valeur())

class PARAMTreeItem(Objecttreeitem.ObjectTreeItem):
    """
    Classe servant � d�finir l'item port� par le noeud de l'arbre d'EFICAS
    qui repr�sente le PARAMETRE
    """
    panel = PARAMPanel

    def init(self):
      self.setfunction = self.set_valeur

# ---------------------------------------------------------------------------
#                   API du PARAMETRE pour l'arbre 
# ---------------------------------------------------------------------------

    def GetIconName(self):
      """
      Retourne le nom de l'ic�ne associ�e au noeud qui porte self,
      d�pendant de la validit� de l'objet
      NB : un PARAMETRE est toujours valide ...
      """
      if self.isactif():
          if self.isvalid():
              return "ast-green-square"
          else:
              return "ast-red-square"
      else:
          return "ast-white-square"

    def GetLabelText(self):
        """ Retourne 3 valeurs :
        - le texte � afficher dans le noeud repr�sentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return 'Param�tre',Fonte_PARAMETRE,None

    def GetText(self):
      """
      Retourne le texte � afficher apr�s le nom de la commande (ici apr�s 'param�tre')
      Ce texte est tronqu� � 25 caract�res
      """
      texte = repr(self.object)
      texte = string.split(texte,'\n')[0]
      if len(texte) < 25 :
          return texte
      else :
          return texte[0:24]+'...'

    def GetSubList(self):
      """
      Retourne la liste des fils de self
      """
      return []
    
# ---------------------------------------------------------------------------
#       M�thodes permettant la modification et la lecture des attributs
#       du param�tre = API graphique du PARAMETRE pour Panel et EFICAS
# ---------------------------------------------------------------------------

    def get_valeur(self):
      """
      Retourne la valeur de l'objet PARAMETRE cad son texte
      """
      if self.object.valeur is None: return ''
      else: return self.object.valeur 

    def get_nom(self):
      """
      Retourne le nom du param�tre
      """
      return self.object.nom

    def set_valeur(self,new_valeur):
      """
      Affecte valeur � l'objet PARAMETRE
      """
      self.object.set_valeur(new_valeur)

    def set_nom(self,new_nom):
      """
      Renomme le param�tre
      """
      self.object.set_nom(new_nom)
      #self.object.set_attribut('nom',new_nom)

    def get_fr(self):
      """
      Retourne le fr associ� au param�tre, cad la bulle d'aide pour EFICAS
      """
      return "D�finition d'un param�tre"
    
import Extensions.parametre
treeitem =PARAMTreeItem
objet = Extensions.parametre.PARAMETRE
