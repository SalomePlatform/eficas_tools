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
"""
# Modules Python
import string
from Tkinter import *
import Pmw

# Modules Eficas
import images

class TOOLBAR:
  def __init__(self,appli,parent):
      # parent représente l'objet graphique parent
      self.parent=parent
      # appli représente l'objet application parent
      self.appli=appli
      self.balloon = None
      self.l_boutons_a_activer = []
      self.barreboutons=Frame(self.parent,relief='ridge',bd=2)
      self.barreboutons.pack(anchor='nw',expand=0,fill=X)
      # bouton Infos à l'extrême droite de la barre des boutons
      b = Button(self.barreboutons,
                 image = images.get_image('About24'),
                 command = self.view_infos)
      b.pack(side='right')
      texte = "Infos EFICAS"
      b.bind("<Enter>",lambda e,s=self,but=b,t=texte : s.affiche_balloon(e,but,t,pos='right'))
      b.bind("<Leave>", self.efface_balloon)

  def inactive_boutons(self):
      """
      Inactive les boutons de la liste self.l_boutons_a_activer
      --> cette méthode est appelée dès qu'il n'y a pas de JDC courant
      """
      for but in self.l_boutons_a_activer:
          but.configure(state='disabled')

  def active_boutons(self):
      """
      Active les boutons de la liste self.l_boutons_a_activer
      --> cette méthode est appelée dès qu'il y a un JDC courant
      """
      for but in self.l_boutons_a_activer:
          but.configure(state='normal')

  def affiche_balloon(self,event,bouton,bulle,pos='left'):
      """
      Affiche le balloon bulle associé au bouton bouton
      """
      etat = bouton.cget('state')
      if etat != 'normal' : return
      geom = bouton.winfo_geometry()
      l_args = string.split(geom,'+')
      x = eval(l_args[1])+event.x+10
      self.balloon = Label(self.parent,
                           text = bulle,
                           background="yellow",
                           borderwidth=2,
                           relief='ridge')
      if pos == 'left':
          self.balloon.place(in_=self.parent,x=x,y=32)
      else:
          self.balloon.place(in_=self.parent,x=x,y=32,anchor='ne')

  def efface_balloon(self,event=None):
      """
      Efface le balloon courant
      """
      if self.balloon :
          self.balloon.destroy()
          self.balloon = None

  def view_infos(self):
      """
      Permet d'afficher des infos sur la session courante d'EFICAS
      """
      self.fen_infos = Pmw.Dialog(self.parent,
                                  title = 'Informations session EFICAS',
                                  buttons = ('Fermer',),
                                  command = self.close_infos)
      self.fen_infos.withdraw()
      texte_infos = self.appli.get_texte_infos()
      Label(self.fen_infos.interior(),
            text = texte_infos,
            anchor='center').pack(side='top',anchor='center')
      self.fen_infos.activate(geometry = 'centerscreenalways')

  def close_infos(self,lbl):
      """
      Ferme la fenêtre des infos
      """
      self.fen_infos.destroy()

  def creer_boutons_appli_composant(self,l_boutons,appli_composant):
      for bouton in l_boutons :
          if not bouton :
              # on veut afficher un bouton vide (=espace entre boutons)
              Button(self.barreboutons,
                     image = images.get_image('Sep'),
                     state='disabled',
                     relief = 'flat').pack(side='left')
              continue
          nom_fic,commande,texte,statut = bouton
          commande=getattr(appli_composant,commande)
          b = Button(self.barreboutons,
                     image = images.get_image(nom_fic),
                     command = commande,
                     relief='flat')
          b.pack(side='left')
          b.bind("<Enter>",lambda e,s=self,but=b,t=texte : s.affiche_balloon(e,but,t))
          b.bind("<Leave>", self.efface_balloon)
          if statut != 'always':
              self.l_boutons_a_activer.append(b)

      # inactive les boutons qui doivent l'être tant qu'aucun JDC courant
      self.inactive_boutons()


