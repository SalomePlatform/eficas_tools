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
from Tkinter import *
import Pmw
import string

import Objecttreeitem
import panels
import fontes

Fonte_Commentaire = fontes.standard_italique

class COMMPanel(panels.OngletPanel):
  
  def init(self):
    """
    Initialise les frame des panneaux contextuels relatifs à un COMMENTAIRE
    """
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    nb.pack(fill = 'both', expand = 1)
    self.nb=nb
    nb.add('TexteComm', tab_text='Texte Commentaire')
    nb.add('Commande', tab_text='Nouvelle Commande')
    nb.add('Commentaire',tab_text='Paramètre/Commentaire')
    self.makeCOMMPage(nb.page("TexteComm"))
    self.makeCommandePage(nb.page("Commande"))
    self.makeParamCommentPage_for_etape(nb.page("Commentaire"))
    nb.tab('TexteComm').focus_set()
    nb.setnaturalsize()
    
  def makeCOMMPage(self,page):
    """
    Crée la page qui permet d'afficher et d'éditer le texte du commentaire
    """
    self.frame_valeur = Frame(page)
    self.frame_valeur.place(relwidth=0.9,relheight=0.9,relx=0.05,rely=0.05,anchor='nw')
    self.widget_text = Pmw.ScrolledText(self.frame_valeur,
                                        borderframe=1,
                                        labelpos='n',
                                        label_text = 'Texte du commentaire\n ')
    self.widget_text.pack(side='top',expand=1,fill='both')
    self.widget_text.configure(hscrollmode='dynamic',
                               vscrollmode='dynamic')
    self.make_buttons()
    self.display_valeur()

  def make_buttons(self):
    """
    Crée les boutons du panneau
    """
    self.bouton_sup.place_forget()
    self.bouton_doc.place_forget()
    self.bouton_val = Button(self.fr_but,text='Valider',command=self.change_valeur,width=14)
    self.bouton_ann = Button(self.fr_but,text='Annuler',command=self.display_valeur,width=14)

    self.bouton_val.place(relx=0.25,rely=0.5,relheight=0.8,anchor='center')
    self.bouton_ann.place(relx=0.50,rely=0.5,relheight=0.8,anchor='center')
    self.bouton_sup.place(relx=0.75,rely=0.5,relheight=0.8,anchor='center')


  def change_valeur(self):
    """
    Stocke la nouvelle valeur donnée par l'utilisateur comme valeur du commentaire
    """
    if self.parent.modified == 'n' : self.parent.init_modif()
    new_valeur = self.widget_text.get()
    self.node.item.set_valeur(new_valeur)
    self.node.update()

  def display_valeur(self):
    """
    Affiche dans self.widget_text la valeur de l'objet commentaire
    (annule d'éventuelles modifications faite par l'utilisateur)
    """
    t=self.node.item.get_valeur()
    try:
        self.widget_text.settext(unicode(t))
    except:
        # Si probleme avec unicode
        self.widget_text.settext(t)
    
class COMMTreeItem(Objecttreeitem.ObjectTreeItem):
    panel = COMMPanel

    def init(self):
      self.setfunction = self.set_valeur

    def GetIconName(self):
      """
      Retourne le nom de l'icône associée au noeud qui porte self,
      dépendant de la validité de l'objet
      NB : un commentaire est toujours valide ...
      """
      return "ast-white-percent"

    def GetLabelText(self):
        """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return 'commentaire',Fonte_Commentaire,None

    def get_valeur(self):
      """
      Retourne la valeur de l'objet Commentaire cad son texte
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
      Afefcte valeur à l'objet COMMENTAIRE
      """
      self.object.set_valeur(valeur)
      
    def GetSubList(self):
      """
      Retourne la liste des fils de self
      """
      return []


    def get_objet_commentarise(self):
       """
           La méthode get_objet_commentarise() de la classe compocomm.COMMTreeItem
           surcharge la méthode get_objet_commentarise de la classe Objecttreeitem.ObjectTreeItem
           elle a pour but d'empecher l'utilisateur final de commentariser un commentaire.
       """
       raise Exception( 'Citoyen : tu peux "commentariser" une commande MAIS PAS UN COMMENTAIRE' )
  
import Extensions
treeitem =COMMTreeItem
objet = Extensions.commentaire.COMMENTAIRE    
