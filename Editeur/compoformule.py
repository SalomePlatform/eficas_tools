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
repr�sentant un objet de type FORMULE, cad le panneau et l'item de l'arbre
d'EFICAS
"""

# import modules Python
from Tkinter import *
import Pmw
import string

# import modules EFICAS
import widgets
import panels
import fontes
import compooper

Fonte_TITRE = fontes.standard_gras_souligne


class FORMULEPanel(panels.OngletPanel):
  """
  Classe servant � construire le panneau associ� � un param�tre.
  C'est au moyen de ce panneau que l'utilisateur peut acc�der
  aux nom et valeur du param�tre en vue �ventuellement de les
  modifier.
  """

  def init(self):
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    nb.pack(fill = 'both', expand = 1)
    self.nb=nb
    nb.add('Formule', tab_text='D�finition Formule')
    nb.add('Commande', tab_text='Nouvelle Commande')
    nb.add('Commentaire',tab_text='Param�tre/Commentaire')
    self.makeFormulePage(nb.page("Formule"))
    self.makeCommandePage(nb.page("Commande"))
    self.makeParamCommentPage_for_etape(nb.page("Commentaire"))
    nb.tab('Formule').focus_set()
    nb.setnaturalsize()
    
  def makeFormulePage(self,page):
    """
    Cr�e la page qui permet d'afficher et d'�diter le texte de la FORMULE
    """
    self.frame_valeur = Frame(page)
    self.frame_valeur.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05,anchor='nw')
    # affichage du titre du panneau
    self.titre = StringVar()
    self.titre.set("FORMULE "+self.node.item.get_nom())

    self.entry_nom = Entry(self.frame_valeur)
    Label(self.frame_valeur,textvariable=self.titre,font=Fonte_TITRE).place(relx=0.5,rely=0.,anchor='n')
    # cr�ation des labels et entries associ�s aux nom, type retourn�, arguments et corps de la FORMULE
    
    Label(self.frame_valeur,text= 'Nom de la formule : ').place(relx=0.,rely=0.1)
    Label(self.frame_valeur,text= 'Arguments : ').place(relx=0.,rely=0.40)
    self.entry_arg = Entry(self.frame_valeur)
    Label(self.frame_valeur,text= 'Expression : ').place(relx=0.,rely=0.65)
    self.entry_exp = Entry(self.frame_valeur)

    # binding sur les entries
    self.entry_nom.bind("<Return>",self.verif_nom)
    self.entry_arg.bind("<Return>",self.verif_arguments)
    self.entry_exp.bind("<Return>",self.verif_corps)
    # affichage des entries
    self.entry_nom.place(relx=0.35,rely=0.10,relwidth=0.2)
    self.entry_arg.place(relx=0.35,rely=0.40,relwidth=0.4)

    # affichage d'une phrase d'aide pour les arguments
    aide = """Entrer les arguments sous la forme
de VARIABLES s�par�es par des virgules (,)
Exemple X,Y,Z """
    Label(self.frame_valeur,text=aide, justify="l").place(relx=0.5,rely=0.47,anchor='n') 

    self.entry_exp.place(relx=0.35,rely=0.65,relwidth=0.60)
    # affichage d'une phrase d'aide pour l'expression
    aide = """Un retour de chariot dans une zone de saisie vous permet de v�rifier si
la valeur que vous avez entr�e est valide.
Ce n'est qu'apr�s avoir appuy� sur le bouton Valider que les nouvelles
valeurs seront effectivement prises en compte."""
    Label(self.frame_valeur,text=aide).place(relx=0.5,rely=0.75,anchor='n')

    # affichage des nom, type retourn�, arguments et corps de la FORMULE
    self.display_valeur()
    # affichage des boutons
    self.make_buttons()
    # entry_nom prend le focus
    self.entry_nom.focus()

  def make_buttons(self):
    """
    Cr�e les boutons du panneau
    """
    self.bouton_sup.place_forget()
    self.bouton_doc.place_forget()
    self.bouton_val = Button(self.fr_but,text='Valider',command=self.change_valeur,width=14)
    self.bouton_ann = Button(self.fr_but,text='Annuler',command=self.display_valeur,width=14)

    self.bouton_val.place(relx=0.15,rely=0.5,relheight=0.8,anchor='center')
    self.bouton_ann.place(relx=0.40,rely=0.5,relheight=0.8,anchor='center')
    self.bouton_sup.place(relx=0.65,rely=0.5,relheight=0.8,anchor='center')
    self.bouton_doc.place(relx=0.90,rely=0.5,relheight=0.8,anchor='center')

  def change_valeur(self):
    """
    Stocke la nouvelle FORMULE d�crite par l'utilisateur
    """
    if self.parent.modified == 'n' : self.parent.init_modif()
    # on r�cup�re les nouveaux nom, type retourn�, arguments et corps de la FORMULE
    new_nom = self.entry_nom.get()
    new_typ="REEL" 
    new_arg = self.entry_arg.get()
    new_exp = self.entry_exp.get()
    self.verif_arguments()
    self.verif_corps()
    # on essaie de les stocker
    test,erreur = self.node.item.save_formule(new_nom,new_typ,new_arg,new_exp)
    if test :
        # on a pu stocker les nouveaux param�tres : il faut rafra�chir l'affichage
        self.node.update()
        self.display_valeur()
        self.parent.appli.affiche_infos("FORMULE %s modifi�e" %self.node.item.get_nom())
    else:
        # la formule est incorrecte : on affiche les erreurs
        widgets.showerror("Formule incorrecte",erreur)
        self.parent.appli.affiche_infos("FORMULE %s non modifi�e" %self.node.item.get_nom())
    
  def display_valeur(self):
    """
    Affiche dans self.widget_text de la valeur de l'objet FORMULE
    (annule d'�ventuelles modifications faite par l'utilisateur)
    """
    # on efface tout texte affich� dans les entries
    self.entry_nom.delete(0,END)
    self.entry_arg.delete(0,END)
    self.entry_exp.delete(0,END)
    # on rafra�chit le titre du panneau
    self.titre.set('FORMULE '+self.node.item.get_nom())
    # on ins�re les nouveaux nom, type retourn�, arguments et corps de la FORMULE
    nom = self.node.item.get_nom()
    if nom != '':
        self.entry_nom.insert(END,nom)
    args = self.node.item.get_args()
    if args:
        texte_args=""
	for i in args :
	    if texte_args != "" :
	       texte_args = texte_args +","
	    texte_args=texte_args + i
        self.entry_arg.insert(END,texte_args)
    corps = self.node.item.get_corps()
    if corps :
        self.entry_exp.insert(END,self.node.item.get_corps())

  def verif_nom(self,event=None):
        """
        Lance la v�rification du nom pr�sent dans entry_nom
        """
        nom = self.entry_nom.get()
        if nom == '':
            test,erreur = 0,"Aucun nom fourni !"
        else:
            test,erreur = self.node.item.verif_nom(nom)
        if not test:
            widgets.showerror("Nom invalide",erreur)
            self.entry_nom.focus()
            self.entry_nom.selection_range(0,END)
            self.parent.appli.affiche_infos("%s n'est pas un nom valide pour une FORMULE" %nom)
        else:
            self.parent.appli.affiche_infos("%s est un nom valide pour une FORMULE" %nom)
            self.entry_arg.focus()

  def verif_arguments(self,event=None):
        """
        Lance la v�rification des arguments pr�sents dans entry_arg
        """
        arguments = self.entry_arg.get()
        if arguments == '' :
            test,erreur = 0,"Aucun argument fourni"
        else:
            test,erreur = self.node.item.verif_arguments(arguments)
        if not test:
            widgets.showerror("Argument(s) invalide(s)",erreur)
            self.entry_arg.focus()
            self.entry_arg.selection_range(0,END)
            self.parent.appli.affiche_infos("Argument(s) invalide(s) pour une FORMULE")
        else:
            self.parent.appli.affiche_infos("Argument(s) valide(s) pour une FORMULE")
            self.entry_exp.focus()

  def verif_corps(self,event=None):
        """
        Lance la v�rification du corps de formule pr�sent dans entry_exp
        """
	new_nom = self.entry_nom.get()
	new_typ="REEL"
        new_arg = self.entry_arg.get()
        new_exp = self.entry_exp.get()
        if new_exp == '':
            test,erreur = 0,"Aucune expression fournie !"
        else:
            test,erreur = self.node.item.verif_formule_python((new_nom,new_typ,new_arg,new_exp))
 
        if not test:
            widgets.showerror("Corps de FORMULE invalide",erreur)
            self.entry_exp.focus()
            self.entry_exp.selection_range(0,END)
            self.parent.appli.affiche_infos("Corps de FORMULE invalide")
        else:
            self.parent.appli.affiche_infos("Corps de FORMULE valide")
            
class FORMULETreeItem(compooper.EtapeTreeItem):
    """
    Classe servant � d�finir l'item port� par le noeud de l'arbre d'EFICAS
    qui repr�sente la FORMULE
    """
    panel = FORMULEPanel

    def init(self):
      self.setfunction = self.set_valeur

# ---------------------------------------------------------------------------
#                   API de FORMULE pour l'arbre 
# ---------------------------------------------------------------------------
    def GetSubList(self):
      """
      Retourne la liste des fils de self
      On consid�re que FORMULE n'a pas de fils
      --> modification par rapport � MACRO classique
      """
      # dans EFICAS on ne souhaite pas afficher les mots-cl�s fils de FORMULE
      # de fa�on traditionnelle
      return []

    def GetIconName(self):
      """
      Retourne le nom de l'ic�ne � afficher dans l'arbre
      Ce nom d�pend de la validit� de l'objet
      """
      if self.object.isactif():
	self.object.state="modified"
        if self.object.isvalid():
          return "ast-green-square"
        else:
          return "ast-red-square"
      else:
        return "ast-white-text"

    def GetLabelText(self):
      """ Retourne 3 valeurs :
      - le texte � afficher dans le noeud repr�sentant l'item
      - la fonte dans laquelle afficher ce texte
      - la couleur du texte
      """
      if self.object.isactif():
        # None --> fonte et couleur par d�faut
        return self.labeltext,None,None
      else:
        return self.labeltext,fontes.standard_italique,None
    
# ---------------------------------------------------------------------------
#       M�thodes permettant la modification et la lecture des attributs
#       du param�tre = API graphique de la FORMULE pour Panel et EFICAS
# ---------------------------------------------------------------------------

    def get_nom(self):
      """
      Retourne le nom de la FORMULE
      """
      return self.object.get_nom()

    def get_type(self):
      """
      Retourne le type de la valeur retourn�e par la FORMULE
      """
      return self.object.type_retourne

    def get_args(self):
      """
      Retourne les arguments de la FORMULE
      """
      args=""
      for mot in self.object.mc_liste:
	  if mot.nom == 'NOM_PARA':
	     args=mot.valeur
	     break
      if args :
          if args[0] == "(" and args[-1] ==")":
	     args=args[1:-1]
      return args

    def get_corps(self):
      """
      Retourne le corps de la FORMULE
      """
      corps=""
      for mot in self.object.mc_liste:
	  if mot.nom == 'VALE':
	     corps=mot.valeur
	     break
      return corps


    def get_liste_types_autorises(self):
      """
         Retourne la liste des types autorises pour les valeurs de sortie 
         d'une FORMULE
      """
      return self.object.l_types_autorises

    def save_formule(self,new_nom,new_typ,new_arg,new_exp):
      """
      V�rifie si (new_nom,new_typ,new_arg,new_exp) d�finit bien une FORMULE 
      licite :
          - si oui, stocke ces param�tres comme nouveaux param�tres de la 
            FORMULE courante et retourne 1
          - si non, laisse les param�tres anciens de la FORMULE inchang�s et 
            retourne 0
      """
      test,erreur = self.object.verif_formule_python(formule=(new_nom,new_typ,new_arg,
                                                       new_exp))
      if test :
          # la formule est bien correcte : on sauve les nouveaux param�tres
          test=self.object.update_formule_python(formule=(new_nom,new_typ,new_exp,new_arg))
      return test,erreur

# ---------------------------------------------------------------------------
#          Acc�s aux m�thodes de v�rification de l'objet FORM_ETAPE
# ---------------------------------------------------------------------------

    def verif_nom(self,nom):
        """
        Lance la v�rification du nom pass� en argument
        """
        return self.object.verif_nom(nom)

    def verif_arguments(self,arguments):
        """
        Lance la v�rification des arguments pass�s en argument
        """
        return self.object.verif_arguments('('+arguments+')')

    def verif_formule(self,formule):
        """
        Lance la v�rification de FORMULE pass�e en argument
        """
	return self.object.verif_formule(formule=formule)


    def verif_formule_python(self,formule):
        """
        Lance la v�rification de FORMULE pass�e en argument
        """
	return self.object.verif_formule_python(formule=formule)

import Accas
treeitem =FORMULETreeItem
objet = Accas.FORM_ETAPE
