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
import traceback
from Tkinter import *
import Pmw
import string
from widgets import showerror

import Objecttreeitem
import panels
import fontes

Fonte_Commentaire = fontes.standard_italique

class COMMANDE_COMMPanel(panels.OngletPanel):
  """
  Classe servant � d�finir le panel associ� � une commande commentaris�e
  """
  def init(self):
    """
    Initialise les frame des panneaux contextuels relatifs � une commande commentaris�e
    """
    panneau=Frame(self)
    panneau.pack(expand=1,fill='both')
    self.make_buttons()
    self.makeCOMMPage(panneau)

  def makeCOMMPage(self,page):
    """
    Cr�e la page qui permet d'afficher et d'�diter le texte de la commande commentaris�e
    """
    self.frame_valeur = Frame(page)
    self.frame_valeur.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05,anchor='nw')
    self.widget_text = Pmw.ScrolledText(self.frame_valeur,
                                        borderframe=1,
                                        labelpos='n',
                                        label_text = 'Texte de la commande\n ')
    self.widget_text.pack(side='top',expand=1,fill='both')
    self.widget_text.configure(hscrollmode='dynamic',
                               vscrollmode='dynamic')
    self.display_valeur()

  def make_buttons(self):
    """
    Cr�e les boutons du panneau
    """
    self.bouton_sup.place_forget()
    self.bouton_doc.place_forget()
    self.bouton_val = Button(self.fr_but,text='Valider',command=self.change_valeur,width=14)
    self.bouton_ann = Button(self.fr_but,text='Annuler',command=self.display_valeur,width=14)
    self.bouton_unc = Button(self.fr_but,text='D�commentariser',command=self.uncomment,width=14)

    self.bouton_val.place(relx=0.1,rely=0.5,relheight=1,relwidth=0.20,anchor='center')
    self.bouton_ann.place(relx=0.30,rely=0.5,relheight=1,relwidth=0.20,anchor='center')
    self.bouton_sup.place(relx=0.50,rely=0.5,relheight=1,relwidth=0.20,anchor='center')
    self.bouton_unc.place(relx=0.75,rely=0.5,relheight=1,relwidth=0.25,anchor='center')

  def change_valeur(self):
    """
    Stocke la nouvelle valeur donn�e par l'utilisateur comme valeur de la commande commentaris�e
    """
    if self.parent.modified == 'n' : self.parent.init_modif()
    new_valeur = self.widget_text.get()
    self.node.item.set_valeur(new_valeur)
    self.node.update()

  def display_valeur(self):
    """
    Affiche dans self.widget_text la valeur de la commande commentaris�e
    (annule d'�ventuelles modifications faite par l'utilisateur)
    """
    self.widget_text.settext(self.node.item.get_valeur())

  def uncomment(self):
      """
      R�alise la d�commentarisation de self
      """
      try:
          pos=self.node.parent.children.index(self.node)
          commande,nom = self.node.item.uncomment()
          self.node.parent.children[pos].select()
      except Exception,e:
          showerror("Erreur !",str(e))
          return
      #self.parent.appli.bureau.JDCDisplay_courant.ReplaceObjectNode(self.node,commande,nom)
    
class COMMANDE_COMMTreeItem(Objecttreeitem.ObjectTreeItem):
    panel = COMMANDE_COMMPanel

    def init(self):
      self.setfunction = self.set_valeur

    def GetIconName(self):
      """
      Retourne le nom de l'ic�ne associ�e au noeud qui porte self,
      d�pendant de la validit� de l'objet
      NB : une commande commentaris�e est toujours valide ...
      """
      if self.isvalid():
          return "ast-green-percent"
      else:
          return "ast-red-percent"

    def GetLabelText(self):
        """ Retourne 3 valeurs :
        - le texte � afficher dans le noeud repr�sentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return 'commande commentaris�e',Fonte_Commentaire,None

    def get_valeur(self):
      """
      Retourne la valeur de la commande commentaris�e cad son texte
      """
      return self.object.get_valeur() or ''
    
    def GetText(self):
        texte = self.object.valeur
        texte = string.split(texte,'\n')[0]
        if len(texte) < 25 :
            return texte
        else :
            return texte[0:24]

    def set_valeur(self,valeur):
      """
      Afefcte valeur � l'objet commande commentaris�e
      """
      self.object.set_valeur(valeur)
      
    def GetSubList(self):
      """
      Retourne la liste des fils de self
      """
      return []

    def uncomment(self):
      """
      Demande � l'objet commande commentaris�e de se d�commentariser.
      Si l'op�ration s'effectue correctement, retourne l'objet commande
      et �ventuellement le nom de la sd produite, sinon l�ve une exception
      """
      try:
        commande,nom = self.object.uncomment()
      except Exception,e:
        traceback.print_exc()
        raise e
      return commande,nom
  
import Accas
treeitem =COMMANDE_COMMTreeItem
objet = Accas.COMMANDE_COMM    
