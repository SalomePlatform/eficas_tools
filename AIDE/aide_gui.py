# -*- coding: utf-8 -*-
"""
Ce module génère l'IHM permettant d'accéder à l'aide en ligne d'une application(ex: EFICAS)
Il analyse l'objet index passé en argument et génére automatiquement en conséquence le menu
avec liens hyper texte
"""

from Tkinter import *

class AIDE_GUI:
   """
   Classe définissant l'IHM de l'appli d'aide
   """
   def __init__(self,objet,master=None):
      self.objet = objet
      self.master = master
      self.init()
      self.init_window()
      self.init_frames()
      self.init_buttons()
      self.init_text()
      
   def init(self):
      """
      Initialise les structures de données utlisées par l'objet
      """
      self.padx = [0,0,0,0]
      self.padx[0] = 0
      self.padx[1] = 30
      self.padx[2] = 50
      self.historique = []   
      
   def init_window(self):
      """
      Initialise la fenêtre mère de l'appli
      """
      fenetre = Toplevel()
      if self.master :
         self.fenetre = fenetre
      else:
         self.fenetre = fenetre.master
	 fenetre.destroy()
      self.fenetre.title(self.objet.titre)
      self.fenetre.geometry("700x700+50+50")
      self.fenetre.resizable(1,1)
      #self.fenetre.minsize(600,800)
      #self.fenetre.maxsize(900,800)
      self.fenetre.protocol("WM_DELETE_WINDOW",self.quit)
      self.fenetre.update()
      	 
   def init_frames(self):
      """
      Initialise les frames principales de l'appli
      """
      self.frame1 = Frame(self.fenetre,relief='flat',bd=2)
      self.frame2 = Frame(self.fenetre,relief='flat',bd=2)
      self.frame1.grid(row=0,column=0,sticky='news')
      self.frame2.grid(row=1,column=0,sticky='news')
      self.fenetre.grid_columnconfigure(0,weight=1,minsize=0)
      self.fenetre.grid_rowconfigure(1,minsize=30)
      self.fenetre.grid_rowconfigure(0,weight=1,minsize=0)
      
   def init_buttons(self):
      """
      Crée les boutons dans le bas de la fenêtre
      """
      self.b_retour = Button(self.frame2,text = "Précédent",command=self.go_back)
      self.b_retour.place(relx=0.33,rely=0.5,anchor='center')
      Button(self.frame2,text="Fermer",command=self.quit).place(relx=0.66,rely=0.5,anchor='center') 
      

   def init_text(self):
      """
      Construit le widget Text qui accueillera l'index et les fichiers
      """
      self.scroll_v = Scrollbar(self.frame1)
      self.scroll_v.grid(row=0,column=1,rowspan=2,sticky='nesw')
      self.scroll_h = Scrollbar(self.frame1,orient='horizontal')
      self.scroll_h.grid(row=1,column=0,rowspan=2,sticky='nesw')
      self.canvas = Canvas(self.frame1,
                           bg='white',
			   relief='sunken',
			   scrollregion=(0,0,1000,1000),
			   yscrollcommand=self.scroll_v.set,
			   xscrollcommand=self.scroll_h.set)
      self.canvas.grid(row=0,column=0,sticky='nesw')
      self.scroll_v.configure(command=self.canvas.yview)
      self.scroll_h.configure(command=self.canvas.xview)
      self.frame1.grid_columnconfigure(0,weight=1,minsize=0)
      self.frame1.grid_rowconfigure(0,weight=1,minsize=0)
      self.frame1.grid_rowconfigure(1,minsize=10)
      self.frame1.grid_columnconfigure(1,minsize=10)

   def build(self):
      """
      Lance la construction dynamique de l'index en hyper texte
      """
      self.frame1.update_idletasks()
      largeur = self.frame1.winfo_width()
      self.canvas.create_rectangle(0,0,1,1,outline='white')
      self.y_courant = 0
      # Construction du titre encadré d'une bordure
      titre = self.canvas.create_text(int(largeur/2),50,anchor='center',text=self.objet.titre,font="Helvetica 12 bold")
      bbox = self.canvas.bbox(titre)
      bordure = self.canvas.create_rectangle(bbox[0]-5,bbox[1]-5,bbox[2]+5,bbox[3]+5,
                                             outline = 'black',
					     fill = 'grey75')
      self.canvas.lower(bordure)				     
      self.y_courant += 100
      # Construction des items
      for item in self.objet.l_items :
          self.build_item(item,0)
      # Affichage du texte dans le fichier associé (s'il existe)
      if self.objet.fichier :
         try:
	    texte=open(self.objet.fichier,'r').read()
         except:
            texte="Fichier %s inaccessible" % self.objet.fichier
	 self.canvas.create_text(10,self.y_courant+20,
	                         text=texte,
				 anchor='nw')
      # Configuration dynamique des boutons
      self.config_boutons()
      #
      self.canvas.config(scrollregion=self.canvas.bbox('all'))
      
   def config_boutons(self):
      """
      Activation du bouton précédent s'il y a lieu
      """
      if self.historique : 
         self.b_retour.config(state='normal')
      else :
         self.b_retour.config(state='disabled')
      
   def build_item(self,item,padx):
      """
      Affiche l'item dans le menu décalé de padx
      """
      l = Label(self.canvas,
                text=item.titre,
		foreground = 'blue',
		background='white',
		font="Helvetica 12 bold")
      l.bind("<Button-1>",lambda e,s=self,o=item : s.update_objet(o))
      l.bind("<Enter>",lambda e,s=self,o=l : s.select_label(o))
      l.bind("<Leave>",lambda e,s=self,o=l : s.deselect_label(o))
      self.canvas.create_window(self.padx[padx],self.y_courant,window=l,anchor='w')
      self.y_courant += 20
      for sub_item in item.l_items :
          self.build_item(sub_item,padx+1)
      
   def show_file(self,fichier):
      """
      Affiche le fichier passé en argument
      """
      print "on veut afficher :",fichier

   def select_label(self,label):
      """
      Callback invoqué lorsque le label passé en argument est sélectionné
      """
      label.config(fg='white',bg='blue')

   def deselect_label(self,label):
      """
      Callback invoqué lorsque le label passé en argument est sélectionné
      """
      label.config(bg='white',fg='blue')      

   def go_back(self):
      """
      Affiche l'item précédent
      """
      self.update_objet(self.historique[-1])
      self.historique = self.historique[0:-1]
      # Configuration dynamique des boutons
      self.config_boutons()
      
   def update_objet(self,new_objet):
      """
      Cette méthode remplace l'objet courant par new_objet.
      Elle vide le widget text et affiche le nouvel objet
      """
      if not self.historique : 
         self.historique.append(self.objet)
      elif new_objet is not self.historique[-1] :
         self.historique.append(self.objet)
      self.objet = new_objet 
      self.canvas.delete('all')
      self.build()
                       
   def quit(self):
      """
      Ferme l'appli Aide
      """
      self.fenetre.destroy()     
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
