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
Ce module contient les classes permettant de définir les objets graphiques
représentant un objet de type FORMULE, cad le panneau et l'item de l'arbre
d'EFICAS
"""

# import modules Python
from Tkinter import *
import Pmw

# import modules EFICAS
from Editeur import widgets
from Editeur import compoformule
from Editeur import fontes
import ongletpanel

Fonte_TITRE = fontes.standard_gras_souligne

class FORMULEPanel(ongletpanel.OngletPanel ,compoformule.FORMULEPanel):
  """
  Classe servant à construire le panneau associé à un paramètre.
  C'est au moyen de ce panneau que l'utilisateur peut accéder
  aux nom et valeur du paramètre en vue éventuellement de les
  modifier.
  """

  def makeFormulePage(self,page):
    """
    Crée la page qui permet d'afficher et d'éditer le texte de la FORMULE
    """
    self.frame_valeur = Frame(page)
    self.frame_valeur.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05,anchor='nw')
    # affichage du titre du panneau
    self.titre = StringVar()
    self.titre.set("FORMULE "+self.node.item.get_nom())
    Label(self.frame_valeur,textvariable=self.titre,font=Fonte_TITRE).place(relx=0.5,rely=0.,anchor='n')
    # création des labels et entries associés aux nom, type retourné, arguments et corps de la FORMULE
    Label(self.frame_valeur,text= 'Nom de la formule : ').place(relx=0.,rely=0.1)
    self.entry_nom = Entry(self.frame_valeur)
    Label(self.frame_valeur,text= 'Type retourné : ').place(relx=0.,rely=0.25)
    self.option_menu_typ = Pmw.OptionMenu(self.frame_valeur,labelpos='w',
                                          label_text='',
                                          items = self.node.item.get_liste_types_autorises())
    self.option_menu_typ.place(relx=0.33,rely=0.23)
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
TYPE : VARIABLE séparés par des virgules (,)
Exemple REEL:INST,ENTIER:COEF """
    Label(self.frame_valeur,text=aide, justify="l").place(relx=0.5,rely=0.47,anchor='n') 

    self.entry_exp.place(relx=0.35,rely=0.65,relwidth=0.60)
    # affichage d'une phrase d'aide pour l'expression
    aide = """Un retour de chariot dans une zone de saisie vous permet de vérifier si
la valeur que vous avez entrée est valide.
Ce n'est qu'après avoir appuyé sur le bouton Valider que les nouvelles
valeurs seront effectivement prises en compte."""
    Label(self.frame_valeur,text=aide).place(relx=0.5,rely=0.75,anchor='n')

    # affichage des nom, type retourné, arguments et corps de la FORMULE
    self.display_valeur()
    # affichage des boutons
    self.make_buttons()
    # entry_nom prend le focus
    self.entry_nom.focus()

  def change_valeur(self):
    """
    Stocke la nouvelle FORMULE décrite par l'utilisateur
    """
    if self.parent.modified == 'n' : self.parent.init_modif()
    # on récupère les nouveaux nom, type retourné, arguments et corps de la FORMULE
    new_nom = self.entry_nom.get()
    new_typ = self.option_menu_typ.getcurselection()
    new_arg = self.entry_arg.get()
    new_exp = self.entry_exp.get()
    # on essaie de les stocker
    test,erreur = self.node.item.save_formule(new_nom,new_typ,new_arg,new_exp)
    if test :
        # on a pu stocker les nouveaux paramètres : il faut rafraîchir l'affichage
        self.node.update()
        self.display_valeur()
        self.parent.appli.affiche_infos("FORMULE %s modifiée" %self.node.item.get_nom())
    else:
        # la formule est incorrecte : on affiche les erreurs
        widgets.showerror("Formule incorrecte",erreur)
        self.parent.appli.affiche_infos("FORMULE %s non modifiée" %self.node.item.get_nom())
    
  def display_valeur(self):
    """
    Affiche dans self.widget_text de la valeur de l'objet FORMULE
    (annule d'éventuelles modifications faite par l'utilisateur)
    """
    # on efface tout texte affiché dans les entries
    self.entry_nom.delete(0,END)
    self.entry_arg.delete(0,END)
    self.entry_exp.delete(0,END)
    # on rafraîchit le titre du panneau
    self.titre.set('FORMULE '+self.node.item.get_nom())
    # on insére les nouveaux nom, type retourné, arguments et corps de la FORMULE
    nom = self.node.item.get_nom()
    if nom != '':
        self.entry_nom.insert(END,nom)
    type = self.node.item.get_type()
    if type :
        self.option_menu_typ.invoke(type)
    args = self.node.item.get_args()
    if args:
        self.entry_arg.insert(END,args)
    corps = self.node.item.get_corps()
    if corps :
        self.entry_exp.insert(END,self.node.item.get_corps())

  def verif_corps(self,event=None):
        """
        Lance la vérification du corps de formule présent dans entry_exp
        """
        new_nom = self.entry_nom.get()
        new_typ = self.option_menu_typ.getcurselection()
        new_arg = self.entry_arg.get()
        new_exp = self.entry_exp.get()
        if new_exp == '':
            test,erreur = 0,"Aucune expression fournie !"
        else:
            test,erreur = self.node.item.verif_formule((new_nom,new_typ,new_arg,new_exp))
 
        if not test:
            widgets.showerror("Corps de FORMULE invalide",erreur)
            self.entry_exp.focus()
            self.entry_exp.selection_range(0,END)
            self.parent.appli.affiche_infos("Corps de FORMULE invalide")
        else:
            self.parent.appli.affiche_infos("Corps de FORMULE valide")
            

class FORMULETreeItem(compoformule.FORMULETreeItem):
    """
    Classe servant à définir l'item porté par le noeud de l'arbre d'EFICAS
    qui représente la FORMULE
    """
    panel = FORMULEPanel

# ---------------------------------------------------------------------------
#       Méthodes permettant la modification et la lecture des attributs
#       du paramètre = API graphique de la FORMULE pour Panel et EFICAS
# ---------------------------------------------------------------------------

    def get_args(self):
      """
      Retourne les arguments de la FORMULE
      """
      args = self.object.arguments
      if args :
          return self.object.arguments[1:-1] #on enlève les parenthèses ouvrante et fermante
      else:
          return None

    def get_corps(self):
      """
      Retourne le corps de la FORMULE
      """
      return self.object.corps

    def save_formule(self,new_nom,new_typ,new_arg,new_exp):
      """
      Vérifie si (new_nom,new_typ,new_arg,new_exp) définit bien une FORMULE 
      licite :
          - si oui, stocke ces paramètres comme nouveaux paramètres de la 
            FORMULE courante et retourne 1
          - si non, laisse les paramètres anciens de la FORMULE inchangés et 
            retourne 0
      """
      test,erreur = self.object.verif_formule(formule=(new_nom,new_typ,new_arg,
                                                       new_exp))
      if test :
          # la formule est bien correcte : on sauve les nouveaux paramètres
          self.object.update(formule=(new_nom,new_typ,new_arg,new_exp))
      return test,erreur

# ---------------------------------------------------------------------------
#          Accès aux méthodes de vérification de l'objet FORM_ETAPE
# ---------------------------------------------------------------------------

    def verif_formule(self,formule):
        """
        Lance la vérification de FORMULE passée en argument
        """
        return self.object.verif_formule(formule=formule)

import Accas
treeitem =FORMULETreeItem
objet = Accas.FORM_ETAPE

Accas.FORM.itemeditor=FORMULETreeItem

