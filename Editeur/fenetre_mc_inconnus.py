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
from Tkinter import *
import copy

# Modules Eficas
from centerwindow import centerwindow

class fenetre_mc_inconnus :
    """
       Cette classe sert à construire la fenêtre qui apparaît dans EFICAS 
       lorsque des mots-clés inconnus ont été trouvés dans le fichier de 
       commandes que l'on est en train de lire
    """
    def __init__(self,l_mc):
       self.l_mc = l_mc
       self.fenetre = Toplevel()
       self.fenetre.geometry("400x400+0+0")
       self.fenetre.title("Mots-clés inconnus dans le fichier de commandes")
       self.init()
       self.init_frames()
       self.init_label()
       self.init_liste_mc()
       self.init_boutons()
       centerwindow(self.fenetre)

    def init(self) :
       """
       Initialise les structures de données
       """
       self.new_l_mc = []
       for mc in self.l_mc :
           self.new_l_mc.append(copy.copy(mc))
       self.mc_courant = None
       self.var_quit = IntVar(0)
       self.entry_courante = None
	       
    def init_frames(self):
       """
       Création des 2 frames devant contenir le label et la liste des MC inconnus 
       """
       self.frame1 = Frame(self.fenetre)
       self.frame2 = Frame(self.fenetre)
       self.frame3 = Frame(self.fenetre)
       self.frame1.place(relx=0,rely=0,relheight=0.2,relwidth=1)
       self.frame2.place(relx=0,rely=0.2,relheight=0.6,relwidth=1)
       self.frame3.place(relx=0,rely=0.8,relheight=0.2,relwidth=1)
    
    def init_label(self):
       """
       Affichage du label dans la zone concernée
       """
       txt = " Un ou plusieurs mots-clés inconnus ont été trouvés dans le fichier de commandes."
       txt = txt + "En cliquant sur leur nom, vous pourrez soit corriger l'orthographe soit supprimer ce mot-clé"
       self.fenetre.update_idletasks()
       Label(self.frame1,
             text = txt,
	     wraplength = int(self.frame1.winfo_width()*0.8),
	     justify = 'center').place(relx=0.5,rely=0.5,anchor='center')   
    
    
    def init_liste_mc(self):
       """
       Affiche les mots-clés à modifier ou supprimer  
       """
       i=0
       self.widgets=[]
       for mc in self.l_mc :
           # mc est une liste :
           # mc contient comme premiers arguments l'étape et éventuellement les blocs, mcfact ...
	   # et contient comme 2 derniers éléments le nom du mot-clé et sa valeur
	   path_mc = self.get_path(mc[0:-2])
	   nom_mc  = mc[-2]
	   lab=Label(self.frame2,text = path_mc)
	   lab.grid(row=i,column=1,sticky=W)
	   e = Entry(self.frame2)
	   e.grid(row=i,column=0,sticky=W)
	   e.insert(END,nom_mc)
	   e.bind("<Button-1>",lambda event,en=e,m=mc,s=self : s.select_mc(m,en))
	   e.bind("<Return>",lambda e,s=self : s.modifie_mc())
	   e.configure(relief='flat',state='disabled')
           self.widgets.append((e,lab))
           i=i+1

    def init_boutons(self):
        """
	Construit les boutons Modifier,Supprimer et Fermer 
	Les deux premiers sont inactifs tant qu'aucun mot-clé n'est sélectionné
	"""
	self.b_mod = Button(self.frame3,
	                    text = "Modifier",
			    disabledforeground = 'grey35',
			    state='disabled',
			    command = self.modifie_mc)
	self.b_sup = Button(self.frame3,
	                    text = "Supprimer",
			    disabledforeground = 'grey35',
			    state='disabled',
			    command = self.supprime_mc)
	self.b_quit = Button(self.frame3,
	                    text = "Fermer",
			    command = self.quit)
	self.b_mod.place(relx=0.25,rely=0.5,anchor='center')
	self.b_sup.place(relx=0.50,rely=0.5,anchor='center')
	self.b_quit.place(relx=0.75,rely=0.5,anchor='center')
	    		    
    def wait_new_list(self):
        """
	Cette méthode rend cette toplevel bloquante.
	Dès que la variable var_quit est modifiée, on continue l'exécution de cette
	méthode (et on quitte)
	"""
	self.fenetre.wait_variable(self.var_quit)
	self.fenetre.destroy()
	return self.new_l_mc
			   
    def get_path(self,l_o):
        """
	Construit la chaîne de caractère contenant le chemin d'accès complet du mot-clé
	"""
	txt = ''
	for o in l_o :
	   txt = txt + o.nom+'/'
	# on enlève le dernier slash en trop
	txt = txt[0:-1]
	return txt    
    
    def select_mc(self,mc,entry):
        """
	Enregistre le mot-clé passé en argument comme mot-clé courant
	Active les boutons Modifier et Supprimer
	"""
	self.desactive_entry()
	self.mc_courant     = mc
	self.entry_courante = entry
	self.active_boutons()
	self.active_entry()

    def modifie_mc(self):
        """
	Modifie le nom du mot-clé en prenant la nouvelle valeur lue dans entry_courante
	"""
	new_nom_mc = self.entry_courante.get()
	index = self.l_mc.index(self.mc_courant)
	new_mc = self.new_l_mc[index]
	new_mc[-2] = new_nom_mc
	objet_pere = self.mc_courant[-3]
	
	self.desactive_boutons()
	self.desactive_entry()

    def supprime_mc(self):
        """
	Supprime le mot-clé courant de la liste
	"""
	index = self.l_mc.index(self.mc_courant)
	self.new_l_mc[index] = None
        e,lab=self.widgets[index]
        e.grid_remove()
        lab.grid_remove()
	self.desactive_boutons()
	self.desactive_entry()	
	
    def desactive_boutons(self):
        """
	Désactive les boutons Modifier et Supprimer
	"""
	self.b_mod.configure(state='disabled')
	self.b_sup.configure(state='disabled')
		
    def active_boutons(self):
        """
	Active les boutons Modifier et Supprimer
	"""
	self.b_mod.configure(state='normal')
	self.b_sup.configure(state='normal')

    def desactive_entry(self):
        """
	Désactive l'entry courante si elle existe
	"""
	if self.entry_courante :
	   self.entry_courante.configure(state='disabled',relief='flat')
	   
    def active_entry(self):
        """
	Active l'entry courante si elle existe
	"""
	if self.entry_courante :
	   self.entry_courante.configure(state='normal',relief='sunken')
	   	   
    def quit(self):
        """
	Permet de fermer la fenêtre
	"""
	self.var_quit.set(1)

if __name__ == '__main__':
   fenetre_mc_inconnus(('toto','titi'))
