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

      #self.creer_boutons()

  def creer_boutons(self):
      self.l_boutons = (('New24',self.appli.newJDC,"Création d'un nouveau fichier",'always'),
                        ('Open24',self.appli.openJDC,"Ouverture d'un fichier existant",'always'),
                        ('Save24',self.appli.saveJDC,"Sauvegarde du fichier courant",'always'),
                        ('Zoom24',self.appli.visuJDC,"Visualisation du fichier de commandes",'always'),
                        None,
                        ('Copy24',self.appli.copy,"Copie l'objet courant",'jdc'),
                        ('Cut24',self.appli.cut,"Coupe l'objet courant",'jdc'),
                        ('Paste24',self.appli.paste,"Colle l'objet copié après l'objet courant",'jdc'),
                        None,
                        ('Delete24',self.appli.delete,"Supprime l'objet courant",'jdc'),
                        ('Help24',self.appli.view_doc,"Documentation de l'objet courant",'jdc')
                        )
      # liste des boutons à activer quand statut != 'always'
      self.l_boutons_a_activer = [] 

      for bouton in self.l_boutons :
          if not bouton :
              # on veut afficher un bouton vide (=espace entre boutons)
              Button(self.barreboutons,
                     image = images.get_image('New24'),
                     relief = 'flat').pack(side='left')
              continue
          nom_fic,commande,texte,statut = bouton
          b = Button(self.barreboutons,
                     image = images.get_image(nom_fic),
                     command = commande,
                     relief='flat')
          b.pack(side='left')
          b.bind("<Enter>",lambda e,s=self,but=b,t=texte : s.affiche_balloon(e,but,t))
          b.bind("<Leave>", self.efface_balloon)
          if statut != 'always':
              self.l_boutons_a_activer.append(b)
      # bouton Infos à l'extrême droite de la barre des boutons
      b = Button(self.barreboutons,
                 image = images.get_image('About24'),
                 command = self.view_infos)
      b.pack(side='right')
      texte = "Infos EFICAS"
      b.bind("<Enter>",lambda e,s=self,but=b,t=texte : s.affiche_balloon(e,but,t,pos='right'))
      b.bind("<Leave>", self.efface_balloon)
      # inactive les boutons qui doivent l'être tant qu'aucun JDC courant
      self.inactive_boutons()

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

  def creer_boutons_extension(self,l_boutons,extension):
      for bouton in l_boutons :
          if not bouton :
              # on veut afficher un bouton vide (=espace entre boutons)
              Button(self.barreboutons,
                     image = images.get_image('New24'),
                     relief = 'flat').pack(side='left')
              continue
          nom_fic,commande,texte,statut = bouton
          commande=getattr(extension,commande)
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


