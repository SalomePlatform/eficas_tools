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
# ----------------------------------------------------------
#   Cette classe sert � d�finir les widgets utilis�s par
#          EFICAS
# ----------------------------------------------------------

import Tkinter
from Tkinter import *
import Pmw
import os,sys,re,string
import types,fnmatch
import traceback
from tkFileDialog import *
from tkMessageBox import showinfo,askyesno,showerror,askretrycancel

import fontes

from Editeur.utils import save_in_file
from centerwindow import centerwindow

from Noyau.N_utils import repr_float
from Accas import AsException

# Surcharge de la fonction askyesno qui retourne un resultat errone en Python 2.3 avec Tk 8.4
# et Tkinter.wantobject==1
import tkMessageBox
def askyesno(title=None, message=None, **options):
    "Ask a question; return true if the answer is yes"
    s = tkMessageBox._show(title, message, tkMessageBox.QUESTION, tkMessageBox.YESNO, **options)
    if s == tkMessageBox.YES:return 1
    if s == tkMessageBox.NO:return 0
    if s:return 1
    return 0

    
class Fenetre :
    """ Cette classe permet de cr�er une fen�tre Toplevel dans laquelle
        on peut afficher un texte et qui permet de le sauver"""
    def __init__(self,appli,titre="",texte="",wrap=WORD,width=100,height=30):
        self.appli=appli
        if self.appli.test==1 : return
        self.fenetre = Toplevel()
        self.fenetre.withdraw()
        #self.fenetre.configure(width = 800,height=500)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
        self.fenetre.title("Visualisation du "+titre)
        self.texte = string.replace(texte,'\r\n','\n')
        self.titre = titre
        fonte=fontes.standardcourier10
        # d�finition des frames
        self.frame_texte = Frame(self.fenetre)
        self.frame_boutons = Frame(self.fenetre)
        # d�finition de la zone texte et du scrollbar
        self.zone_texte = Text(self.frame_texte,font=fonte,wrap=wrap,
                               height=height,width=width)
        self.zone_texte.bind("<Key-Prior>", self.page_up)
        self.zone_texte.bind("<Key-Next>", self.page_down)
        self.zone_texte.bind("<Key-Up>", self.unit_up)
        self.zone_texte.bind("<Key-Down>", self.unit_down)
        self.scroll_v = Scrollbar (self.frame_texte,command = self.zone_texte.yview)
        #self.scroll_h = Scrollbar (self.frame_texte,command = self.zone_texte.xview)
        self.scroll_v.pack(side='right',fill ='y')
        #self.scroll_h.pack(side='bottom',fill ='x')
        self.zone_texte.pack(side='top',fill='both',expand=1,padx=5,pady=10)
        self.zone_texte.configure(yscrollcommand=self.scroll_v.set)
        # d�finition des boutons
        self.but_quit = Button(self.frame_boutons,text = "Fermer",command=self.quit,
                                default='active')
        self.but_save = Button(self.frame_boutons,text = "Sauver",command = self.save)
        self.but_quit.pack(side='left',padx=25, pady=5)
        self.but_save.pack(side='right',padx=25, pady=5)
        self.frame_boutons.pack(side='bottom',padx=5,pady=5)
        self.frame_texte.pack(side='top',fill='both',expand=1,padx=5,pady=5)
        self.zone_texte.focus_set()
        self.fenetre.bind('<Return>',self.quit) #dismiss window

        # affichage du texte
        self.affiche_texte(self.texte)
        self.zone_texte.config(state=DISABLED)
        centerwindow(self.fenetre)
        self.fenetre.deiconify()

    def page_up(self,event):
        event.widget.yview_scroll(-1, "page")
        return "break" #Pour eviter la propagation de l'evenement a la fenetre principale
    def page_down(self,event):
        event.widget.yview_scroll(1, "page")
        return "break" #Pour eviter la propagation de l'evenement a la fenetre principale
    def unit_up(self,event):
        event.widget.yview_scroll(-1, "unit")
        return "break" #Pour eviter la propagation de l'evenement a la fenetre principale
    def unit_down(self,event):
        event.widget.yview_scroll(1, "unit")
        return "break" #Pour eviter la propagation de l'evenement a la fenetre principale

    def wait(self):
        self.fenetre.grab_set()
        self.zone_texte.focus_set()
        self.fenetre.wait_window(self.fenetre)

    def quit(self,event=None):
        self.fenetre.destroy()
        return "break" #Pour eviter la propagation de l'evenement a la fenetre principale

    def efface_scroll(self):
        """ Efface le scroll lorsqu'il n'est pas n�cessaire : ne marche pas"""
        self.scroll_v.pack_forget()
        #self.scroll_h.pack_forget()

    def affiche_texte(self,texte):
        """ Affiche le texte dans la fen�tre """
        if texte != "" :
            self.zone_texte.insert(END,texte)
            self.fenetre.update_idletasks()
            curline = int(self.zone_texte.index("insert").split('.')[0])
            if curline < int(self.zone_texte["height"]):
              self.efface_scroll()

    def save(self):
        """ Permet de sauvegarder le texte dans un fichier dont on a demand� le nom
        � l'utilisateur """
        file = asksaveasfilename(parent=self.fenetre,defaultextension = '.comm',
                               #initialdir = self.appli.CONFIGURATION.rep_user,
                               initialdir = self.appli.CONFIGURATION.savedir,
                               title="Sauvegarde du "+self.titre)
        if file :
            if not save_in_file(file,self.texte,None) :
                showerror("Sauvegarde impossible",
                       "Impossible de sauvegarder le texte dans le fichier sp�cifi�\n"+
                          "V�rifiez les droits d'�criture",parent=self.fenetre)
            else:
                showinfo("Sauvegarde effectu�e","Sauvegarde effectu�e dans le fichier %s" %file,parent=self.fenetre)

    def destroy(self):
        try :
           self.fenetre.destroy()
        except :
           pass

class FenetreSurLigneWarning(Fenetre):

    def affiche_texte(self,texte):
        """ Affiche le texte dans la fen�tre """
        ligne=0
        if texte != "" :
           texte_cr=texte.splitlines()
           for l in texte_cr:
                ligne=ligne+1
                l=l+"\n"
                self.zone_texte.insert(END,l)
                if (l.find("WARNING") > -1) or (l.find("ERROR") > -1) : 
                   self.zone_texte.tag_add( "Rouge", str(ligne)+".0", "end-1c" )
                   self.zone_texte.tag_config("Rouge", foreground='red')
           try:
                self.fenetre.update_idletasks()
                x0,y0,x1,y1 = self.zone_texte.bbox(END)
                if (y1-y0) < 300 : self.efface_scroll()
           except:
                pass

class FenetreYesNo(Fenetre):
    def __init__(self,appli,titre="",texte="",yes="Yes",no="No"):
        self.appli=appli
        self.fenetre = Toplevel()
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
        self.fenetre.title(titre)
        self.texte = string.replace(texte,'\r\n','\n')
        self.titre = titre
        fonte=fontes.standardcourier10
        # d�finition des frames
        self.frame_texte = Frame(self.fenetre)
        self.frame_boutons = Frame(self.fenetre)
        # d�finition de la zone texte et du scrollbar
        self.zone_texte = Text(self.frame_texte,font=fonte)
        self.zone_texte.bind("<Key-Prior>", self.page_up)
        self.zone_texte.bind("<Key-Next>", self.page_down)
        self.zone_texte.bind("<Key-Up>", self.unit_up)
        self.zone_texte.bind("<Key-Down>", self.unit_down)
        self.scroll_v = Scrollbar (self.frame_texte,command = self.zone_texte.yview)
        #self.scroll_h = Scrollbar (self.frame_texte,command = self.zone_texte.xview)
        self.scroll_v.pack(side='right',fill ='y')
        #self.scroll_h.pack(side='bottom',fill ='x')
        self.zone_texte.pack(side='top',fill='both',expand=1,padx=5,pady=10)
        self.zone_texte.configure(yscrollcommand=self.scroll_v.set)
        # d�finition des boutons
        self.but_yes = Button(self.frame_boutons,text = yes,command=self.yes)
        self.but_no = Button(self.frame_boutons,text = no,command = self.no)
        self.but_yes.pack(side="left",padx=5,pady=5)
        self.but_no.pack(side="left",padx=5,pady=5)
        self.frame_boutons.pack(side="top",padx=5,pady=5)
        # affichage du texte
        self.affiche_texte(self.texte)
        self.frame_texte.pack(side="top",fill='both',padx=5,pady=5,expand=1)
        centerwindow(self.fenetre)

    def yes(self):
        self.result=1
        self.quit()

    def no(self):
        self.result=0
        self.quit()

class FenetreDeSelection(Fenetre):
    """ Classe d�riv�e de Fen�tre permettant la r�cup�ration d'une zone de texte s�lectionn�e.
        Cette classe est utilis�e pour affecter une liste de valeurs � un mot-cl�.
    """
    def __init__(self,panel,item,appli,titre="",texte="",cardinal=1):
        Fenetre.__init__(self,appli,titre=titre,texte=texte,width=20,height=15)

        self.cardinal=cardinal
        #self.fenetre.configure(width = 320,height=400)
        self.panel = panel
        self.item = item
        self.fenetre.title(titre)
        self.but_save.configure(text="Ajouter",command=self.traite_selection)
        # s�parateur par d�faut
        self.separateur = ';'
        # cr�ation de la zone de saisie du s�parateur
        l_separateurs_autorises = self.get_separateurs_autorises()
        self.choix_sep = Pmw.ComboBox(self.frame_boutons,
                                      label_text = "S�parateur :",
                                      labelpos = 'w',
                                      listheight = 100,
                                      selectioncommand = self.choose_separateur,
                                      scrolledlist_items = l_separateurs_autorises)
        self.choix_sep.component('entry').configure(width=6)
        self.choix_sep.grid(row=0,rowspan=2,padx=5,pady=5)
        #self.choix_sep.selectitem(self.separateur)
        # Replacement
        self.but_quit.pack_forget()
        self.but_save.pack_forget()
        self.but_all  = Button(self.frame_boutons,text = "Tout S�lectionner", command=self.tout)
        self.but_save.grid(row=1,column=1,padx=5,pady=5)
        self.but_quit.grid(row=1,column=2,padx=5,pady=5)
        self.but_all.grid(row=0,column=1,columnspan=2,padx=5,pady=5)
        self.choose_separateur('espace')
        centerwindow(self.fenetre)
     

    def get_separateurs_autorises(self):
        """
        Retourne la liste des s�parateurs autoris�s
        """
        return ['espace',';',',']

    def choose_separateur(self,nom_sep):
        """
        Affecte � self.separateur le caract�re s�parateur correspondant � nom_sep
        """
        if nom_sep == 'espace' :
            self.separateur = ' '
        else:
            self.separateur = nom_sep
        
    def tout(self):
        liste=[]
        texte=self.texte.splitlines()
        for l in texte :
            for mot in string.split(l,self.separateur):
               if mot != '' and mot != ' ' and mot != self.separateur :
                  liste.append(mot)
        self.traite_selection(liste)

    def traite_selection(self,liste=None):
        """ Cette m�thode effectue tous les traitements n�cessaires pour v�rifier
            et affecter la liste de valeurs � l'objet r�pr�sent� par self.item
        """
        # R�cup�re la liste des chaines de caract�res de la zone s�lectionn�e
        message=""
        if liste == None:
           message,liste = self.recupere_liste()
        if self.test_probleme(message,"S�lectionnez des donn�es") == 0:
            return
        # V�rifie que le nombre de donn�es est dans les limites attendues
        message = self.verif_liste(liste)
        if self.test_probleme(message,"V�rifiez le nombre de donn�es") == 0:
            return
        # Cr�e une liste de valeurs du type attendu
        message,liste_valeurs = self.creation_liste_valeurs(liste)
        if self.test_probleme(message,"V�rifiez le type des donn�es") == 0:
            return
        # V�rifie que chaque valeur est dans le domaine exig�
        message = self.verif_valeurs(liste_valeurs)
        if self.test_probleme(message,"V�rifiez le domaine des valeurs") == 0:
            return
        # Ajoute les valeurs dans la liste de valeurs du mot-cl�
        if self.cardinal != 1 :
           nb=self.cardinal
           l_valeurs=[]
           # a ameliorer
           if (len(liste_valeurs)%nb != 0):
                message="La cardinalit� n'est pas correcte"
                self.test_probleme(message,"On attend des tuples")
                return
           for i in range(len(liste_valeurs)/nb) :
               if (nb==2):
                   t=(liste_valeurs[i*nb], liste_valeurs[i*nb+1])
               elif (nb ==3):
                   t=(liste_valeurs[i*nb], liste_valeurs[i*nb+1], liste_valeurs[i*nb+2])
               else :
                  print "probleme : prevenir la maintenance Eficas"
                  return
               l_valeurs.append(t)
           liste_valeurs=l_valeurs
        self.ajouter_valeurs(liste_valeurs)
        self.appli.affiche_infos("Liste de valeurs accept�e")

    def test_probleme(self, message, message_eficas):
        """ Cette m�thode affiche un message d'erreur si message != ''
            et retourne 0, sinon retourne 1 sans rien afficher.
        """
        if message != "":
            showinfo("Probl�me",message,parent=self.fenetre)
            self.fenetre.tkraise()
            self.appli.affiche_infos(message_eficas)
            return 0
        else:
            return 1

    def recupere_liste(self):
        """ Cette m�thode r�cup�re le texte de la zone s�lectionn�e, construit et
            retourne une liste avec les chaines qui se trouvent entre les s�parateurs.
            S'il n'y a pas de donn�es selectionn�es, elle retourne un message d'erreur
            et une liste vide.
        """
        message = ""
        try:
            selection=self.fenetre.selection_get()
        except:
            message = "Pas de donn�e s�lectionn�e"
            return message,None
        # les retours chariots doivent �tre interpr�t�s comme des s�parateurs
        selection = string.replace(selection,'\n',self.separateur)
        # on splitte la s�lection suivant le caract�re s�parateur
        liste_chaines = string.split(selection,self.separateur)
        l_chaines = []
        for chaine in liste_chaines:
            chaine = string.strip(chaine)
            if chaine != '' : l_chaines.append(chaine)
        return message,l_chaines

    def verif_liste(self, liste):
        """ Cette m�thode effectue des tests sur le nombre d'�l�ments de la liste
            et retourne 1 si la liste est correcte, sinon 0 et le message d'erreur
            correspondant.
        """
        message = ""
        # nombre d'�l�ments s�lectionn�s
        nombre_elements = len(liste)
        # nombre d'�l�ments d�ja dans la liste du panel
        nombre_in_liste = len(self.panel.Liste_valeurs.get_liste())
        multiplicite = self.item.GetMultiplicite()
        if (nombre_elements % multiplicite) != 0:
            message = "Vous devez s�lectionner "+str(multiplicite)+" * n donn�es"
            return message
        nombre_valeurs = nombre_elements / multiplicite
        cardinalite = self.item.GetMinMax()
        if nombre_valeurs < cardinalite[0]:
            message = "Vous devez s�lectionner au moins "+str(cardinalite[0])+" valeurs"
            return message
        if cardinalite[1] != "**" and nombre_valeurs > (long(cardinalite[1])-nombre_in_liste):
            message = "La liste ne peut avoir plus de "+str(cardinalite[1])+" valeurs"
            return message

        return message

    def creation_liste_valeurs(self, liste):
        """ Cette m�thode cr�e et retourne une liste de valeurs du type attendu
            par le mot-cl�. La liste de valeurs est cr��e � partir de la liste
            de chaines de caract�res transmise.
        """
        type_attendu = self.item.GetType()[0]
        if type_attendu == 'R':
            return self.convertir(liste, f_conversion= float)
        elif type_attendu == 'I':
            return self.convertir(liste, f_conversion= int)
        elif type_attendu == 'TXM':
            return self.convertir(liste)
        else:
            message = "Seuls les entiers, les r�els et les chaines de caract�res sont convertis"
            return message,None

    def convertir(self, liste, f_conversion=None):
        """ Cette m�thode essaie de convertir les �l�ments de la liste avec la
            fonction f_conversion si elle existe, et retourne la liste des
            �l�ments dans le type voulu en cas de succ�s, sinon retourne None.
        """
        liste_valeurs = []
        message = ""
        for chaine in liste:
            if f_conversion:
                try:
                    liste_valeurs.append(f_conversion(chaine))
                except:
                    message = "Impossible de convertir "+chaine+" dans le type attendu"
                    return message,None
            else:
                liste_valeurs.append(chaine)
        return message,liste_valeurs

    def verif_valeurs(self, liste_valeurs):
        """ Cette m�thode teste la validit� de tous les �l�ments de la liste,
            retourne un message vide s'ils sont valides
            ou un message non vide au premier �l�ment non valide rencontr�
        """
        message = ""
        for valeur in liste_valeurs:
            test,message = self.item.object.verif_type(valeur)
            if test == 0: return message
        return message

    def ajouter_valeurs(self, liste_valeurs):
        """ Cette m�thode ajoute les nouvelles valeurs � la liste existante."""
        liste = self.panel.Liste_valeurs.get_liste()
        liste.extend(liste_valeurs)
        self.panel.Liste_valeurs.put_liste(liste)

class FenetreDeParametre(Fenetre) :
    def __init__(self,parent,item,appli,texte):
        self.parent=parent
        self.appli=appli
        self.fenetre = Toplevel()
        #self.fenetre.configure(width = 250,height=100)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
        self.fenetre.title("Parametres")
        self.titre = "Parametres"
        self.texte = string.replace(texte,'\r\n','\n')
        fonte=fontes.standardcourier10

        # d�finition des frames
        self.frame_texte = Frame(self.fenetre)
        # d�finition de la zone texte et du scrollbar
        self.zone_texte = Text(self.frame_texte,font=fonte,width=40)
        self.zone_texte.bind("<Key-Prior>", self.page_up)
        self.zone_texte.bind("<Key-Next>", self.page_down)
        self.zone_texte.bind("<Key-Up>", self.unit_up)
        self.zone_texte.bind("<Key-Down>", self.unit_down)
        self.scroll_v = Scrollbar (self.frame_texte,command = self.zone_texte.yview)
        self.scroll_v.pack(side='right',fill ='y')
        self.zone_texte.pack(side='top',fill='both',expand=1,padx=5,pady=10)
        self.zone_texte.configure(yscrollcommand=self.scroll_v.set)
        # affichage du texte
        self.affiche_texte(self.texte)
        self.zone_texte.config(state="disabled")

        # d�finition des boutons
        self.frame_boutons = Frame(self.fenetre)
        self.label1 = Label(self.frame_boutons,text="surligner la\nligne enti�re",justify=LEFT)
        self.but_quit = Button(self.frame_boutons,text = "Fermer",command=self.quit)
        self.but_save = Button(self.frame_boutons,text = "Choisir",command = self.Choisir)
        self.but_quit.pack(side='right',padx=5, pady=5)
        self.but_save.pack(side='right',padx=5, pady=5)
        self.label1.pack(side='right',padx=5, pady=5)
        self.frame_boutons.pack(side='bottom')
        self.frame_texte.pack(side='top',expand=1,fill='both')


    def Choisir(self):
        try:
            selection=self.zone_texte.selection_get()
        except:
            showerror("Pas de donn�e s�lectionn�e",
                       "Selectionner un parametre")
        l_param = ""
        for param in selection.splitlines():
            nomparam=param[0:param.find("=")-1]
            if nomparam != '' :
                l_param=l_param+nomparam+','
        self.parent.entry.delete(0,Tkinter.END)
        self.parent.entry.insert(0,l_param[0:-1])
        self.parent.valid_valeur()
        self.quit()

    def affiche_texte(self,texte):
        """ Affiche le texte dans la fen�tre """
        if texte != "" :
            self.zone_texte.insert(END,texte)
            self.fenetre.update_idletasks()
            curline = int(self.zone_texte.index("insert").split('.')[0])
            if curline < int(self.zone_texte["height"]):
              self.zone_texte["height"]=curline
              self.efface_scroll()

class Formulaire:
    """
    Cette classe permet de cr�er une bo�te Dialog dans laquelle
    on affiche un formulaire � remplir par l'utilisateur
    """
    def __init__(self,fen_pere,obj_pere=None,titre="",texte="",items=(),mode='query',commande=None):
        self.resultat=0
        if items in ((),[]) : return
        self.items = items
        self.titre = titre
        self.texte = texte
        self.fen_pere = fen_pere
        self.obj_pere = obj_pere
        self.mode= mode
        self.command = commande
        self.display()

    def display(self):
        self.init_validateurs()
        self.init_fenetre()
        self.init_texte()
        self.init_items_formulaire()
        self.fenetre.activate(geometry='centerscreenalways')

    def init_validateurs(self):
        """
        Cr�e le dictionnaire des validateurs des objets reconnus par le formulaire
        """
        self.d_validateurs = {}
        self.d_validateurs['rep']  = self.repvalidator
        self.d_validateurs['file'] = self.filevalidator
        self.d_validateurs['cata']= self.catavalidator
        self.d_validateurs['mot']= self.motvalidator
        self.d_validateurs['mot2']= self.mot2validator
        self.d_validateurs['mot3']= self.mot3validator
        self.d_validateurs['mot4']= self.mot4validator
        
    def init_fenetre(self):
        """
        Cr�e la fen�tre Dialog
        """
        if self.mode == 'query':
            buttons=('Valider','Annuler')
            defaultbutton = 'Valider'
        elif self.mode == 'display':
            if self.command :
                buttons=(self.command[0],'OK')
                defaultbutton = 'OK'
            else:
                buttons=('OK')
                defaultbutton = 'OK'
        self.fenetre = Pmw.Dialog(self.fen_pere,
                                  buttons=buttons,
                                  defaultbutton = defaultbutton,
                                  title = self.titre,
                                  command = self.execute)
        self.fenetre.withdraw()
        
    def init_texte(self):
        """
        Cr�e le label qui affiche le texte � l'int�rieur du panneau
        """
        fonte=fontes.standard
        fr_texte = Frame(self.fenetre.interior(),height=60)
        fr_texte.pack(side='top',fill='x',expand=1)
        Label(fr_texte,text = self.texte, font=fonte).place(relx=0.5,rely=0.5,anchor='center')

    def init_items_formulaire(self):
        """
        Cr�e et affiche les items dans la bo�te de dialogue
        """
        self.radiobut = 0
        self.widgets = []
        self.item_widgets = {}
        length_maxi = 0
        for item in self.items:
            if len(item[0])>length_maxi : length_maxi = len(item[0])
        window = self.fenetre.interior()
        for item in self.items :
            if len(item) == 4 :
               label,nature,nom_var,defaut = item
               chaine="Yes" 
               chaine2="No"
            else :
               label,nature,nom_var,defaut,chaine,chaine2 = item
          
            # cr�ation de la frame
            fr_item = Frame(window,height=40,width=700)
            fr_item.pack(side='top',fill='x',expand=1)
            # cr�ation du label
            Label(fr_item,text = label).place(relx=0.05,rely=0.4)
            if nature in ('rep','file','cata','mot','mot2','mot3','mot4'):
                # cr�ation de l'entry
                e_item = Entry(fr_item) 
                e_item.place(relx=0.5,rely=0.4,relwidth=0.45)
                self.widgets.append(e_item)
                self.item_widgets[item] = e_item
                if defaut : e_item.insert(0,str(defaut))
            elif nature == 'YesNo':
                # cr�ation de la StringVar
                var = StringVar()
                setattr(self,'item_'+nom_var,var)
                var.set(defaut)
                # cr�ation du radiobouton
                rb1 = Radiobutton(fr_item,text=chaine,variable=var,value='OUI')
                rb2 = Radiobutton(fr_item,text=chaine2,variable=var,value='NON')
                rb1.place(relx=0.65,rely=0.5,anchor='center')
                rb2.place(relx=0.80,rely=0.5,anchor='center')
                self.widgets.append((rb1,rb2))
                self.item_widgets[item] = var
        # d�termination de la m�thode � appliquer sur les boutons
        if self.mode == 'query':
            function = self.active
        elif self.mode == 'display':
            function = self.inactive
        else:
            return
        # on applique la m�thode sur les boutons (activation ou d�sactivation)  
        for widget in self.widgets :
            if type(widget) == types.TupleType:
                for widg in widget :
                    apply(function,(widg,),{})
            else:
                apply(function,(widget,),{})

    def active(self,widget):
        """
        Active le widget pass� en argument
        """
        widget.configure(state='normal',bg='white')

    def inactive(self,widget):
        """
        Inactive le widget pass� en argument
        """
        if not isinstance(widget,Radiobutton) :
            widget.configure(state='disabled',bg='gray95')
        else :
            widget.configure(state='disabled')

# --------------------------------------------------------------------------------
#       Validateurs des noms de r�pertoire, de fichiers et de catalogues
# -------------------------------------------------------------------------------

    def motvalidator(self,text):
        text2="("+text+")"
        return self.motlongueurvalidator(text2,1) 

    def mot2validator(self,text):
        return self.motlongueurvalidator(text,2) 

    def mot3validator(self,text):
        return self.motlongueurvalidator(text,3) 

    def mot4validator(self,text):
        return self.motlongueurvalidator(text,4) 

    def motlongueurvalidator(self,text,longueur):
        try :
          if ((text[0] != "(") or (text[-1] != ")")) : return 0
          if len(text.split(",")) != longueur : return 0
          return 1
        except :
          return 0

    def repvalidator(self,text):
        """
        Teste si text peut faire r�f�rence � un r�pertoire ou non
        Retourne 1 si valide, 0 sinon
        """
        return os.path.isdir(text),'R�pertoire introuvable : %s' %text

    def filevalidator(self,text):
        """
        Teste si text peut faire r�f�rence � un fichier ou non
        Retourne 1 si valide, 0 sinon
        """
        return os.path.isfile(text),'Fichier introuvable : %s' %text

    def catavalidator(self,text):
        """
        Teste si  text est un chemin d'acc�s valide � un catalogue
        Retourne 1 si valide, 0 sinon
        """
        return os.path.isfile(text),"Catalogue introuvable : %s" %text

# --------------------------------------------------------------------------------
#       M�thodes callbacks des boutons et de fin
# --------------------------------------------------------------------------------
        
    def execute(self,txt):
        """
        Cette commande est activ�e � chaque clic sur un bouton.
        Redirige l'action sur la bonne m�thode en fonction du bouton activ�
        """
        if txt == 'Valider':
            self.fini()
        elif txt in ('OK','Annuler'):
            self.quit()
        elif txt == 'Modifier':
            self.resultat = apply(self.command[1],(),{})
            self.fenetre.destroy()
        else :
            self.quit()

    def fini(self):
        """
        Commande qui termine le panneau et sauvegarde les nouvelles options
        dans l'objet resultat (dictionnaire)
        """
        dico={}
        for item,widget in self.item_widgets.items():
            nom_var = item[2]
            type_var = item[1]
            valeur = widget.get()
            if self.d_validateurs.has_key(type_var):
                test = self.d_validateurs[type_var](valeur)
                if not test :
                    # une entr�e n'est pas valide --> on la met en surbrillance et on quitte la m�thode
                    # sans tuer la fen�tre bien s�r
                    widget.selection_range(0,END)
                    return
            dico[nom_var] = valeur
        self.fenetre.destroy()    
        self.resultat=dico
        
    def quit(self):
        self.fenetre.destroy()
        self.resultat=None
        
class ListeChoix :
    """ Cette classe est utilis�e pour afficher une liste de choix pass�e en param�tre
        en passant les commandes � lancer suivant diff�rents bindings """
    def __init__(self,parent,page,liste,liste_commandes=[],liste_marques =[],active ='oui',filtre='non',titre='',
                 optionReturn=None, fonte_titre=fontes.standard_gras_souligne):
        self.parent = parent
        self.page = page
        self.liste = liste
        self.dico_labels={}
        self.dico_mots={}
        self.nBlabel = 0
        self.dico_place={}
	self.dico_mots={}
        self.selection = None
        self.liste_commandes = liste_commandes
        self.liste_marques = liste_marques
        self.arg_selected=''
        self.active = active
        self.titre = titre
        self.filtre = filtre
        self.optionReturn = optionReturn
        self.fonte_titre=fonte_titre
        self.init()

    def init(self):        
        self.make_label_titre()
        self.make_entry_filtre()
        self.make_text_box()
        try:
            self.entry.component('entry').focus()
        except:
            pass

    def make_label_titre(self):
        """ Cr�e le label correspondant au titre """
        if self.titre == '' : return
        self.label = Label(self.page,
                           text = self.titre,
                           font = self.fonte_titre)
        self.label.pack(side='top',pady=2)
        
    def make_entry_filtre(self):
        """ Cr�e l'entry permettant � l'utilisateur d'entrer un filtre de s�lection dans la liste """
        if self.filtre != 'oui' : return
        self.entry = Pmw.EntryField(self.page,labelpos='w',
                                    label_text="Filtre :",
                                    command=self.entry_changed)
        self.entry.pack(side='top',pady=2)
        
    def make_text_box(self):
        """ Cr�e la fen�tre texte dans laquelle sera affich�e la liste """
        self.MCbox = Text (self.page,relief='sunken',bg='gray95',bd=2)
        self.MCscroll = Scrollbar (self.page,command = self.MCbox.yview)
        self.MCscroll.pack(side='right',fill ='y',pady=2)
        self.MCbox.pack(fill='y',expand=1,padx=2,pady=2)
        self.MCbox.configure(yscrollcommand=self.MCscroll.set)


    def affiche_liste(self):
        """ Affiche la liste dans la fen�tre"""
        liste_labels=[]
        self.MCbox.config(state=NORMAL)
        self.MCbox.delete(1.0,END)
        self.nBlabel = 0
        self.dico_place={}
        for objet in self.liste :
          if type(objet) == types.InstanceType:
              try:
                  mot = objet.nom
              except:
                  mot = str(objet)
          elif type(objet) in (types.StringType,types.IntType):
              mot = objet
          elif type(objet) == types.FloatType :
              mot = self.parent.get_valeur_texte(objet)
              if mot == "" :
                 mot = str(objet)
          elif type(objet) == types.TupleType :
              mot="("
              premier=1
              for val in objet:
                 if (not premier):
                   mot=mot+"," 
                 else:
                   premier=0
                 valtexte = self.parent.get_valeur_texte(val)
                 if valtexte != "" :
                    mot=mot+valtexte
                 else:
                    mot=mot+str(val)
              mot=mot+")"
          elif string.find(str(type(objet)),".SD.") :
              mot=objet.nom
          else :
              mot=`objet`
          label = Label(self.MCbox,
                        text = mot,
                        fg = 'black',bg = 'gray95',justify = 'left')
          self.dico_labels[mot]=label
          self.dico_place[mot]=self.nBlabel
	  self.dico_mots[label]=mot
          self.nBlabel=self.nBlabel+1
          liste_labels.append(label)
          self.MCbox.window_create(END,
                                   window=label,
                                   stretch = 1)
          self.MCbox.insert(END,'\n')
          if self.optionReturn != None :
              label.bind("<Return>",lambda e,s=self,c=self.liste_commandes[2][1],x=objet,l=label : s.chooseitemsurligne(x,l,c))
              label.bind("<KP_Enter>",lambda e,s=self,c=self.liste_commandes[2][1],x=objet,l=label : s.chooseitemsurligne(x,l,c))
          label.bind("<Key-Right>",lambda e,s=self,x=objet,l=label : s.selectNextItem(x,l))
          label.bind("<Key-Down>",lambda e, s=self,x=objet,l=label : s.selectNextItem(x,l))
          label.bind("<Key-Left>" ,lambda e,s=self,x=objet,l=label  : s.selectPrevItem(x,l))
          label.bind("<Key-Up>" ,lambda e,s=self,x=objet,l=label  : s.selectPrevItem(x,l))
          if self.active == 'oui':
              label.bind(self.liste_commandes[0][0],lambda e,s=self,c=self.liste_commandes[0][1],x=objet,l=label : s.selectitem(x,l,c))
              label.bind(self.liste_commandes[1][0],lambda e,s=self,c=self.liste_commandes[1][1],x=objet,l=label : s.deselectitem(l,x,c))
              label.bind(self.liste_commandes[2][0],lambda e,s=self,c=self.liste_commandes[2][1],x=objet,l=label : s.chooseitem(x,l,c))

        for marque in self.liste_marques:
           try:
              self.markitem(liste_labels[marque])
           except:
              pass

        self.MCbox.config(state=DISABLED)
        self.selection = None
        self.dontselect=0
        for event,callback in self.liste_commandes:
            if event == "<Enter>":
               self.selection=None,None,callback
               break

    def clear_marque(self):
        try:
          self.dico_labels[self.arg_selected].configure(bg='gray95',fg='black')
          self.arg_selected = ''
        except :
          pass

    def surligne(self,marque):
        try :
           self.highlightitem(self.dico_labels[marque])
           self.arg_selected = marque
        except:
           pass

    def chooseitemsurligne(self,mot,label,commande):
        """ Active la m�thode de choix pass�e en argument"""
        try:
           mot=self.arg_selected
           commande(mot)
        except AsException,e:
           raison=str(e)
           showerror(raison.split('\n')[0],raison)

    def chooseitem(self,mot,label,commande):
        """ Active la m�thode de choix pass�e en argument"""
        try:
           commande(mot)
        except AsException,e:
           raison=str(e)
           showerror(raison.split('\n')[0],raison)

    def afficheMot(self,mot):
        """ Pour contourner le bug sur l index 
            on commence par la methode dite normale     
            puis par la methode de contournement     
            puis rien du tout 
        """
        try:
             labelsuivant=self.dico_labels[mot]
             index = self.MCbox.index(labelsuivant)
             self.MCbox.see(index)
        except :
             posmot=self.dico_place[mot]
             totale=self.nBlabel + 0.0
             self.MCbox.yview_moveto(posmot/totale)

    def selectNextItem(self,mot,label):
        index=self.liste.index(mot)
        indexsuivant=index+1
        if indexsuivant > len(self.liste) -1:
           indexsuivant=0
        motsuivant=self.liste[indexsuivant]
        labelsuivant=self.dico_labels[motsuivant]
        self.afficheMot(motsuivant)
        self.selectthis(motsuivant,labelsuivant,self.selection[2],)
        self.dontselect=1
           
    def selectPrevItem(self,mot,label):
        index=self.liste.index(mot)
        indexprec=index-1
        motprec=self.liste[indexprec]
        labelprec=self.dico_labels[motprec]
        self.afficheMot(motprec)
        self.selectthis(motprec,labelprec,self.selection[2],)
        self.dontselect=1
        
    def selectthis(self,mot,label,commande) :
        self.clear_marque()
        if self.selection != None :
            self.deselectitem(self.selection[1],self.selection[0],self.selection[2],)
        self.highlightitem(label)
        self.selection = (mot,label,commande)
        self.arg_selected = mot
        if commande : commande(mot)

    def selectitem(self,mot,label,commande) :
        """ Met l'item s�lectionn� (repr�sent� par son label) en surbrillance
            et lance la commande associ�e au double-clic"""
        if self.dontselect:
           self.dontselect=0
           return
        self.selectthis(mot,label,commande)

    def highlightitem(self,label) :
        """ Met l'item repr�sent� par son label en surbrillance """
        label.focus_set()
        label.configure(bg='#00008b',fg='white')
        
    def markitem(self,label):
        """ Met l'item (repr�sent� par son label) en rouge """
        label.configure(bg='gray95',fg='red')
        
    def deselectitem(self,label,mot='',commande=None) :
        """ Remet l'item (repr�sent� par son label) en noir"""
        if label:label.configure(bg='gray95',fg='black')
        self.arg_selected = ''
        if commande and mot : commande(mot)

    def cherche_selected_item(self):
        try :
           index=self.MCbox.index(self.selection[1])
           lign,col=map(int,string.split(index,'.'))
        except :
	   label=self.dico_labels[self.arg_selected]
           mot=self.dico_mots[label] 
           lign=self.dico_place[mot]+1
        return lign

    def remove_selected_item(self):
        try :
           index=self.MCbox.index(self.selection[1])
           lign,col=map(int,string.split(index,'.'))
        except :
	   label=self.dico_labels[self.arg_selected]
           mot=self.dico_mots[label] 
           lign=self.dico_place[mot]+1
        del self.liste[lign-1]
        self.affiche_liste()

    def entry_changed(self,event=None):
        """ Cette m�thode est invoqu�e chaque fois que l'utilisateur modifie le contenu
        de l'entry et frappe <Return>"""
        if self.arg_selected != '' : self.deselectitem(self.dico_labels[self.arg_selected])
        filtre = self.entry.get()+"*"
        FILTRE = string.upper(filtre)
        self.dontselect=0
        for arg in self.liste :
            if fnmatch.fnmatch(arg,filtre) or fnmatch.fnmatch(arg,FILTRE) :
                label=self.dico_labels[arg]
                self.afficheMot(arg)
                self.selectitem(arg,label,self.selection[2])
                break

        #try :
          #self.dico_labels[self.arg_selected].focus_set()
        #except :
          #pass


    # PN attention � la gestion des param�tres
    # cela retourne H = 1 , et ni H, ni 1
    #            print repr(val)
    #            print val.__class__.__name__
    def get_liste(self):
        l=[]
        for val in self.liste:
#            try:
#                v = eval(val)
#                    l.append(v)
#            except:
                l.append(val)
        return l
    
    def put_liste(self,liste):
        self.liste = liste
        self.affiche_liste()

class Affichage :
  """ Cette classe permet d'afficher au lancement d'EFICAS le message
      d'attente et la barre de progression"""
  def __init__(self,master,message,barre ='oui'):
      from Tools.foztools.foztools import Slider
      fonte=fontes.standard12_gras
      self.master=master
      self.frame = Frame(self.master)
      self.frame.pack(expand=1,fill='both')
      self.mess = Label(self.frame,text=message,justify='center',
                        bd=2,relief='groove',font=fonte)
      self.mess.pack(in_ = self.frame,side='top',expand=1,fill='both')
      self.progress = Slider(self.frame,value=0,max=100,orientation='horizontal',
                             fillColor='#00008b',width=200,height=30,
                             background='white',labelColor='red')
      if barre == 'oui':
          self.progress.frame.pack(in_=self.frame,side='top')
      self.master.update()
      if barre == 'oui':
          self.progress.frame.after(1000,self.update)

  def configure(self,**options):
      if options.has_key('message'):
          self.mess.configure(text=options['message'])
      if options.has_key('barre'):
          if options['barre'] == 'oui' :
              self.progress.frame.pack(in_=self.frame,side='top')
          elif options['barre'] == 'non' :
              self.progress.frame.pack_forget()
      self.master.update_idletasks()
      
  def quit(self):
      self.frame.destroy()
      self.master.update()

  def update(self,event=None):
      """ Permet de faire avancer la barre de progression """
      try :
          bar=self.progress
          bar.value = bar.value+self.increment
          bar.update()
          self.master.after(100,self.update)
      except:
          pass

  def configure_barre(self,nb):
      """ Calcule l'incr�ment de progression de la barre en fonction
          du nombre d'op�rations � effectuer afin que le compteur
          soit � 100% � la fin des op�rations"""
      self.increment = 100./nb
      self.progress.update()

class Ask_Format_Fichier :
    """
    Cette classe permet de cr�er une fen�tre Toplevel dans laquelle
    on propose le choix du format de fichier de commandes � ouvrir
    """
    def __init__(self,appli):
        self.fenetre = Toplevel()
        self.fenetre.configure(width = 250,height=150)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
        self.fenetre.title("Choix du format du fichier de commandes")
        # d�finition des frames
        self.frame_texte = Frame(self.fenetre)
        self.frame_radioboutons = Frame(self.fenetre)
        self.frame_bouton_ok = Frame(self.fenetre)
        self.frame_texte.place(relx=0,rely=0,relwidth=1,relheight=0.3)
        self.frame_radioboutons.place(relheight=0.5,relx=0,rely=0.3,relwidth=1.)
        self.frame_bouton_ok.place(relheight=0.2,relx=0,rely=0.8,relwidth=1.)
        # d�finition de la zone texte et du scrollbar
        zone_texte = Label(self.frame_texte,text = "Format du fichier � ouvrir :")
        zone_texte.pack(side='top',fill='both',expand=1,padx=5,pady=10)
        # d�finition des radioboutons
        Radiobutton(self.frame_radioboutons,text='Format Aster (Code_Aster --> v5)',
                    variable=appli.format_fichier,value='Aster').pack(anchor='n')
        Radiobutton(self.frame_radioboutons,text='Format Python (Code_Aster v6-->)',
                    variable=appli.format_fichier,value='Python').pack(anchor='n')
        # cr�ation du bouton OK
        Button(self.frame_bouton_ok,text='OK',command=self.quit).pack(anchor='n')
        # centrage de la fen�tre
        centerwindow(self.fenetre)

    def quit(self):
        self.fenetre.destroy()

class BARRE_K2000(Toplevel):
    def __init__(self,master=None,text = ""):
        Toplevel.__init__(self,master,relief='groove')
        self.master.iconify()
        self.geometry("250x100+0+0")
        self.protocol("WM_DELETE_WINDOW",self.quit)
        # frame principale dans self (= Toplevel)
        self.frame = Frame(self)
        self.frame.place(relwidth=1,relheight=1)
        # frame contenant le texte � afficher 
        self.frame_text = Frame(self.frame)
        self.frame_text.place(relwidth=1,relheight=0.75,rely=0)
        # frame contenant le canvas de la barre
        self.frame_canv = Frame(self.frame)
        self.frame_canv.place(relwidth=1,relheight=0.25,rely=0.75)
        # canvas dans lequel sera affich�e la barre K2000
        self.canvas = Canvas(self.frame_canv)
        self.canvas.place(relx=0.5,rely=0.5,relheight=0.8,relwidth=0.8,anchor='center')
        # on affiche le texte et la barre
        self.build_text(text)
        self.build_batons()
        #self.overrideredirect(1)
        # on active la barre ...
        self.master.after(1000,self.launch)
        # on centre la fen�tre
        centerwindow(self)
        self.focus()

    def build_text(self,text):
        """
        Affichage de text dans frame_text
        """
        self.texte_var = StringVar()
        self.texte_var.set(text)
        Label(self.frame_text,textvariable=self.texte_var).place(relx=0.5,rely=0.5,anchor='center')
        
    def build_batons(self):
        """
        Construit la suite de b�tons dans le canvas
        """
        self.l_batons=[]
        self.black = -1
        self.sens = 'D'
        self.quit = 0
        for i in range(0,40):
            id = self.canvas.create_rectangle(i*5,0,(i+1)*5,20,fill='gray90',outline='')
            self.l_batons.append(id)

    def launch(self):
        """
        Active la barre K2000 en affichant les b�tons avec des couleurs en d�grad�
        """
        if self.quit == 1 :
            self.destroy()
            self.master.deiconify()
            return
        if self.sens == 'D':
            self.black = self.black+1
            l_bat = self.l_batons[0:self.black+1]
            l_bat.reverse()
        elif self.sens == 'G':
            self.black = self.black-1
            l_bat = self.l_batons[self.black:]
        i=0
        for bat in l_bat :
            num_color = 5+i*10
            if num_color < 10 : color = 'black'
            elif num_color > 90 : color = 'white'
            else: color = 'gray'+`num_color`
            self.canvas.itemconfigure(bat,fill=color)
            i=i+1
        if self.black == len(self.l_batons) :
            self.sens = 'G'
        if self.black == 0 and self.sens == 'G':self.sens = 'D'
        self.after(80,self.launch)

    def update_text(self,new_text):
        """
        Remplace le texte affich� par new_text
        """
        self.texte_var.set(new_text)
        
    def quit(self):
        self.quit = 1        

class ListeChoixParGroupes(ListeChoix) :
    """ 
        Cette classe est utilis�e pour afficher une liste de commandes class�es par
        groupes. L'utilisateur peut r�aliser des actions de selection
        qui d�clenchent des actions sp�cifi�es par les bindings contenus dans liste_commandes
        Exemple de binding:
           liste_commandes = (("<Enter>",self.selectCmd),
                              ("<Leave>",self.deselectCmd),
                              ("<Double-Button-1>",self.defCmd))
        Il s'agit d'une liste de doublets dont le premier element est un evenement et le 
        deuxieme un callback a appeler sur l'evenement en question.

    """
    def __init__(self,parent,page,liste_groupes,dict_groupes,liste_commandes=[],liste_marques =[],
                      active ='oui',filtre='non',titre='',optionReturn=None,fonte_titre=fontes.standard_gras_souligne):
        self.parent = parent
        self.page = page
        self.liste_groupes = liste_groupes
        self.dict_groupes = dict_groupes
        self.dico_labels={}
        self.selection = None
        self.liste_commandes = liste_commandes
        self.liste_marques = liste_marques
        self.arg_selected=''
        self.active = active
        self.titre = titre
        self.filtre = filtre
        self.optionReturn = optionReturn
        self.fonte_titre=fonte_titre
        self.init()

    def affiche_liste(self):
        """ Affiche la liste dans la fen�tre"""
        liste_labels=[]
        self.dico_mots={}
        self.MCbox.config(state=NORMAL)
        self.MCbox.delete(1.0,END)
        for grp in self.liste_groupes:
           # On it�re sur les groupes
           if grp == "CACHE":continue
           liste_commandes=self.dict_groupes[grp]
           text="GROUPE<<<<<<<< "+grp+" "
           text=text+">"*max(0,30-len(text))
           label = Label(self.MCbox,
                        text = text,
                        fg = 'black',bg = 'gray95',justify = 'left')
           # On stocke la relation entre le nom de la commande et le label
           self.dico_labels[grp]=label
           liste_labels.append(label)
           self.MCbox.window_create(END,
                                   window=label,
                                   stretch = 1)
           self.MCbox.insert(END,'\n')
           for cmd in liste_commandes:
              label = Label(self.MCbox,
                        text = cmd,
                        fg = 'black',bg = 'gray95',justify = 'left')
              # On stocke la relation entre le nom de la commande et le label
              self.dico_labels[cmd]=label
	      self.dico_mots[label]=cmd
              self.MCbox.window_create(END,
                                   window=label,
                                   stretch = 1)
              self.MCbox.insert(END,'\n')

              def null(*tp,**args): return

              if self.active == 'oui':
                  # Traitement par defaut des evenements
                  label.bind("<Enter>",lambda e,s=self,c=null,x=cmd,l=label: s.selectitem(x,l,c))
                  label.bind("<Leave>",lambda e,s=self,c=null,x=cmd,l=label: s.deselectitem(l,x,c))
                  label.bind("<Double-Button-1>",lambda e,s=self,c=null,x=cmd,l=label: s.chooseitem(x,l,c))
                  label.bind("<Return>",lambda e,s=self,c=null,x=cmd,l=label: s.chooseitem(x,l,c))
                  label.bind("<KP_Enter>",lambda e,s=self,c=null,x=cmd,l=label: s.chooseitem(x,l,c))
                  label.bind("<Key-Right>",lambda e,s=self,c=null,x=cmd,l=label,gr=grp: s.selectNextItem(x,l,c,gr,x))
                  label.bind("<Key-Down>",lambda e,s=self,c=null,x=cmd,l=label,gr=grp: s.selectNextItem(x,l,c,gr,x))
                  label.bind("<Key-Left>",lambda e,s=self,c=null,x=cmd,l=label,gr=grp: s.selectPrevItem(x,l,c,gr,x))
                  label.bind("<Key-Up>",lambda e,s=self,c=null,x=cmd,l=label,gr=grp: s.selectPrevItem(x,l,c,gr,x))

                  # Si des callbacks sont definis on les utilise
                  for event,callback in self.liste_commandes:
                      if event == "<Enter>":
                         label.bind("<Enter>",lambda e,s=self,c=callback,x=cmd,l=label: s.selectitem(x,l,c))
                      elif event == "<Leave>":
                         label.bind("<Leave>",lambda e,s=self,c=callback,x=cmd,l=label: s.deselectitem(l,x,c))
                      elif event == "<Double-Button-1>":
                         label.bind("<Double-Button-1>",lambda e,s=self,c=callback,x=cmd,l=label: s.chooseitem(x,l,c))
                      elif event == "<Return>":
                         label.bind("<Return>",lambda e,s=self,c=callback,x=cmd,l=label: s.chooseitem(x,l,c))
                      elif event == "<KP_Enter>":
                         label.bind("<KP_Enter>",lambda e,s=self,c=callback,x=cmd,l=label: s.chooseitem(x,l,c))
                      elif event == "<Key-Right>":
                         label.bind("<Key-Right>",lambda e,s=self,c=callback,x=cmd,l=label,gr=grp:s.selectNextItem(x,l,c,gr,x))
                      elif event == "<Key-Down>":
                         label.bind("<Key-Down>",lambda e,s=self,c=callback,x=cmd,l=label,gr=grp:s.selectNextItem(x,l,c,gr,x))
                      elif event == "<Key-Left>":
                         label.bind("<Key-Left>",lambda e,s=self,c=callback,x=cmd,l=label,gr=grp:s.selectPrevItem(x,l,c,gr,x))
                      elif event == "<Key-Up>":
                         label.bind("<Key-Up>",lambda e,s=self,c=callback,x=cmd,l=label,gr=grp:s.selectPrevItem(x,l,c,gr,x))
                      else:
                         label.bind(event,lambda e,s=self,c=callback,x=cmd,l=label: c())

        for marque in self.liste_marques:
           try:
              self.markitem(liste_labels[marque])
           except:
              pass

        self.MCbox.config(state=DISABLED)
        self.selection = None
        self.dontselect=0
        for event,callback in self.liste_commandes:
            if event == "<Enter>":
               self.selection=None,None,callback
               break

    def selectPrevItem(self,mot,label,callback,group,cmd):
        g=self.liste_groupes.index(group)
        liste_commandes=self.dict_groupes[group]
        c=liste_commandes.index(cmd)
        if c > 0:
           co=liste_commandes[c-1]
        else:
           # debut de liste. On passe au groupe precedent
           if g > 0:
              gr=self.liste_groupes[g-1]
              co=self.dict_groupes[gr][-1]
           else:
              # debut des groupes. On ne fait rien
              return
        # On a trouve l'item precedent
        labelsuivant=self.dico_labels[co]
        index = self.MCbox.index(labelsuivant)
        self.MCbox.see(index)
        self.selectthis(co,labelsuivant,self.selection[2],)
        self.dontselect=1

    def selectNextItem(self,mot,label,callback,group,cmd):
        g=self.liste_groupes.index(group)
        liste_commandes=self.dict_groupes[group]
        c=liste_commandes.index(cmd)
        try:
           co=liste_commandes[c+1]
        except:
           # fin de liste. On passe au groupe suivant
           try:
              gr=self.liste_groupes[g+1]
              co=self.dict_groupes[gr][0]
           except:
              # fin des groupes. On ne fait rien
              return
        # On a trouve l'item suivant
        labelsuivant=self.dico_labels[co]
        index = self.MCbox.index(labelsuivant)
        self.MCbox.see(index)
        self.selectthis(co,labelsuivant,self.selection[2],)
        self.dontselect=1

    def entry_changed(self,event=None):
        """ 
            Cette m�thode est invoqu�e chaque fois que l'utilisateur modifie le contenu
            de l'entry et frappe <Return>
        """
        if self.arg_selected != '' : self.deselectitem(self.dico_labels[self.arg_selected])

        filtre = self.entry.get()+"*"
        FILTRE = string.upper(filtre)
        #
        # On cherche d'abord dans les noms de groupe
        # puis dans les noms de commande groupe par groupe
        #
        for grp in self.liste_groupes:
            if fnmatch.fnmatch(grp,filtre) or fnmatch.fnmatch(grp,FILTRE) :
                cmd=self.dict_groupes[grp][0]
                label=self.dico_labels[cmd]
                index = self.MCbox.index(label)
                self.MCbox.see(index)
                self.selectitem(cmd,label,self.selection[2])
                # On a trouve un groupe on arrete la recherche
                return

        for grp in self.liste_groupes:
           for cmd in self.dict_groupes[grp] :
              if fnmatch.fnmatch(cmd,filtre) or fnmatch.fnmatch(cmd,FILTRE) :
                 label=self.dico_labels[cmd]
                 index = self.MCbox.index(label)
                 self.MCbox.see(index)
                 self.selectitem(cmd,label,self.selection[2])
                 # On a trouve une commande  on arrete la recherche
                 return

if __name__ == "__main__":
  root=Tkinter.Tk()
  f=FenetreDeParametre(root,None,None,"\n".join(["coucouxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=2"]*15))
  #f=FenetreYesNo(None,titre="Le titre",texte="\n".join(["Le textexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]*35),yes="Yes",no="No")


  root.mainloop()
