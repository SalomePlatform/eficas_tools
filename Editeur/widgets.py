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
#   Cette classe sert à définir les widgets utilisés par
#          EFICAS
# ----------------------------------------------------------

import Tkinter
from Tkinter import *
import Pmw
import os,sys,re,string
import types,fnmatch
from tkFileDialog import *
from tkMessageBox import showinfo,askyesno,showerror,askretrycancel

import fontes
import prefs
from utils import save_in_file
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
    """ Cette classe permet de créer une fenêtre Toplevel dans laquelle
        on peut afficher un texte et qui permet de le sauver"""
    def __init__(self,appli,titre="",texte=""):
        self.appli=appli
        self.fenetre = Toplevel()
        self.fenetre.configure(width = 800,height=500)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
        self.fenetre.title("Visualisation du "+titre)
        self.texte = string.replace(texte,'\r\n','\n')
        self.titre = titre
        fonte=fontes.standardcourier10
        # définition des frames
        self.frame_texte = Frame(self.fenetre)
        self.frame_boutons = Frame(self.fenetre)
        self.frame_texte.place(relx=0,rely=0,relwidth=1,relheight=0.9)
        self.frame_boutons.place(relheight=0.1,relx=0,rely=0.9,relwidth=1.)
        # définition de la zone texte et du scrollbar
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
        # définition des boutons
        self.but_quit = Button(self.frame_boutons,text = "Fermer",command=self.quit)
        self.but_save = Button(self.frame_boutons,text = "sauver",command = self.save)
        self.but_quit.place(relx=0.4,rely=0.5,anchor='center')
        self.but_save.place(relx=0.6,rely=0.5,anchor='center')
        # affichage du texte
        self.affiche_texte(self.texte)
        centerwindow(self.fenetre)

    def page_up(self,event):
        event.widget.yview_scroll(-1, "page")
    def page_down(self,event):
        event.widget.yview_scroll(1, "page")
    def unit_up(self,event):
        event.widget.yview_scroll(-1, "unit")
    def unit_down(self,event):
        event.widget.yview_scroll(1, "unit")

    def wait(self):
        self.fenetre.grab_set()
        self.zone_texte.focus_set()
        self.fenetre.wait_window(self.fenetre)

    def quit(self):
        self.fenetre.destroy()

    def efface_scroll(self):
        """ Efface le scroll lorsqu'il n'est pas nécessaire : ne marche pas"""
        self.scroll_v.pack_forget()
        #self.scroll_h.pack_forget()

    def affiche_texte(self,texte):
        """ Affiche le texte dans la fenêtre """
        if texte != "" :
            self.zone_texte.insert(END,texte)
            try:
                self.fenetre.update_idletasks()
                x0,y0,x1,y1 = self.zone_texte.bbox(END)
                if (y1-y0) < 300 : self.efface_scroll()
            except:
                pass

    def save(self):
        """ Permet de sauvegarder le texte dans un fichier dont on a demandé le nom
        à l'utilisateur """
        file = asksaveasfilename(defaultextension = '.comm',
                               #initialdir = self.appli.CONFIGURATION.rep_user,
                               initialdir = self.appli.CONFIGURATION.initialdir,
                               title="Sauvegarde du "+self.titre)
        if file :
            if not save_in_file(file,self.texte) :
                showerror("Sauvegarde impossible",
                       "Impossible de sauvegarder le texte dans le fichier spécifié\n"+
                          "Vérifiez les droits d'écriture")
            else:
                showinfo("Sauvegarde effectuée","Sauvegarde effectuée dans le fichier %s" %file)

class FenetreYesNo(Fenetre):
    def __init__(self,appli,titre="",texte="",yes="Yes",no="No"):
        self.appli=appli
        self.fenetre = Toplevel()
        self.fenetre.configure(width = 800,height=500)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
        self.fenetre.title(titre)
        self.texte = string.replace(texte,'\r\n','\n')
        self.titre = titre
        fonte=fontes.standardcourier10
        # définition des frames
        self.frame_texte = Frame(self.fenetre)
        self.frame_boutons = Frame(self.fenetre)
        self.frame_boutons.place(relx=0,rely=0,    relwidth=1.,relheight=0.1)
        self.frame_texte.place(  relx=0,rely=0.1,  relwidth=1, relheight=0.9)
        # définition de la zone texte et du scrollbar
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
        # définition des boutons
        self.but_yes = Button(self.frame_boutons,text = yes,command=self.yes)
        self.but_no = Button(self.frame_boutons,text = no,command = self.no)
        self.but_yes.place(relx=0.4,rely=0.5,anchor='center')
        self.but_no.place(relx=0.6,rely=0.5,anchor='center')
        # affichage du texte
        self.affiche_texte(self.texte)
        centerwindow(self.fenetre)

    def yes(self):
        self.result=1
        self.quit()

    def no(self):
        self.result=0
        self.quit()

class FenetreDeSelection(Fenetre):
    """ Classe dérivée de Fenêtre permettant la récupération d'une zone de texte sélectionnée.
        Cette classe est utilisée pour affecter une liste de valeurs à un mot-clé.
    """
    def __init__(self,panel,item,appli,titre="",texte=""):
        Fenetre.__init__(self,appli,titre=titre,texte=texte)
        self.fenetre.configure(width = 320,height=400)
        centerwindow(self.fenetre)
        self.panel = panel
        self.item = item
        self.fenetre.title(titre)
        self.but_save.configure(text="Ajouter",command=self.traite_selection)
        # séparateur par défaut
        self.separateur = ";"
        # création de la zone de saisie du séparateur
        l_separateurs_autorises = self.get_separateurs_autorises()
        self.choix_sep = Pmw.ComboBox(self.frame_boutons,
                                      label_text = "Séparateur :",
                                      labelpos = 'w',
                                      listheight = 100,
                                      selectioncommand = self.choose_separateur,
                                      scrolledlist_items = l_separateurs_autorises)
        self.choix_sep.component('entry').configure(width=6)
        self.choix_sep.place(relx=0.01,rely=0.5,anchor='w')
        self.choix_sep.selectitem(self.separateur)
        # Replacement
        self.but_quit.place_forget()
        self.but_save.place_forget()
        self.but_save.place(relx=0.6,rely=0.5,anchor='center')
        self.but_quit.place(relx=0.8,rely=0.5,anchor='center')

    def get_separateurs_autorises(self):
        """
        Retourne la liste des séparateurs autorisés
        """
        return ['espace',';',',']

    def choose_separateur(self,nom_sep):
        """
        Affecte à self.separateur le caractère séparateur correspondant à nom_sep
        """
        if nom_sep == 'espace' :
            self.separateur = ' '
        else:
            self.separateur = nom_sep
        
    def traite_selection(self):
        """ Cette méthode effectue tous les traitements nécessaires pour vérifier
            et affecter la liste de valeurs à l'objet réprésenté par self.item
        """
        # Récupère la liste des chaines de caractères de la zone sélectionnée
        message,liste = self.recupere_liste()
        if self.test_probleme(message,"Sélectionnez des données") == 0:
            return
        # Vérifie que le nombre de données est dans les limites attendues
        message = self.verif_liste(liste)
        if self.test_probleme(message,"Vérifiez le nombre de données") == 0:
            return
        # Crée une liste de valeurs du type attendu
        message,liste_valeurs = self.creation_liste_valeurs(liste)
        if self.test_probleme(message,"Vérifiez le type des données") == 0:
            return
        # Vérifie que chaque valeur est dans le domaine exigé
        message = self.verif_valeurs(liste_valeurs)
        if self.test_probleme(message,"Vérifiez le domaine des valeurs") == 0:
            return
        # Ajoute les valeurs dans la liste de valeurs du mot-clé
        self.ajouter_valeurs(liste_valeurs)
        self.appli.affiche_infos("Liste de valeurs acceptée")

    def test_probleme(self, message, message_eficas):
        """ Cette méthode affiche un message d'erreur si message != ''
            et retourne 0, sinon retourne 1 sans rien afficher.
        """
        if message != "":
            showinfo("Problème",message)
            self.fenetre.tkraise()
            self.appli.affiche_infos(message_eficas)
            return 0
        else:
            return 1

    def recupere_liste(self):
        """ Cette méthode récupère le texte de la zone sélectionnée, construit et
            retourne une liste avec les chaines qui se trouvent entre les séparateurs.
            S'il n'y a pas de données selectionnées, elle retourne un message d'erreur
            et une liste vide.
        """
        message = ""
        try:
            selection=self.fenetre.selection_get()
        except:
            message = "Pas de donnée sélectionnée"
            return message,None
        # les retours chariots doivent être interprétés comme des séparateurs
        selection = string.replace(selection,'\n',self.separateur)
        # on splitte la sélection suivant le caractère séparateur
        liste_chaines = string.split(selection,self.separateur)
        l_chaines = []
        for chaine in liste_chaines:
            chaine = string.strip(chaine)
            if chaine != '' : l_chaines.append(chaine)
        return message,l_chaines

    def verif_liste(self, liste):
        """ Cette méthode effectue des tests sur le nombre d'éléments de la liste
            et retourne 1 si la liste est correcte, sinon 0 et le message d'erreur
            correspondant.
        """
        message = ""
        # nombre d'éléments sélectionnés
        nombre_elements = len(liste)
        # nombre d'éléments déja dans la liste du panel
        nombre_in_liste = len(self.panel.Liste_valeurs.get_liste())
        multiplicite = self.item.GetMultiplicite()
        if (nombre_elements % multiplicite) != 0:
            message = "Vous devez sélectionner "+str(multiplicite)+" * n données"
            return message
        nombre_valeurs = nombre_elements / multiplicite
        cardinalite = self.item.GetMinMax()
        if nombre_valeurs < cardinalite[0]:
            message = "Vous devez sélectionner au moins "+str(cardinalite[0])+" valeurs"
            return message
        if cardinalite[1] != "**" and nombre_valeurs > (long(cardinalite[1])-nombre_in_liste):
            message = "La liste ne peut avoir plus de "+str(cardinalite[1])+" valeurs"
            return message

        return message

    def creation_liste_valeurs(self, liste):
        """ Cette méthode crée et retourne une liste de valeurs du type attendu
            par le mot-clé. La liste de valeurs est créée à partir de la liste
            de chaines de caractères transmise.
        """
        type_attendu = self.item.GetType()[0]
        if type_attendu == 'R':
            return self.convertir(liste, f_conversion= float)
        elif type_attendu == 'I':
            return self.convertir(liste, f_conversion= int)
        elif type_attendu == 'TXM':
            return self.convertir(liste)
        else:
            message = "Seuls les entiers, les réels et les chaines de caractères sont convertis"
            return message,None

    def convertir(self, liste, f_conversion=None):
        """ Cette méthode essaie de convertir les éléments de la liste avec la
            fonction f_conversion si elle existe, et retourne la liste des
            éléments dans le type voulu en cas de succès, sinon retourne None.
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
        """ Cette méthode teste tous les éléments de la liste, et retourne 1 si chaque
            élément est dans le domaine voulu.
        """
        message = ""
        for valeur in liste_valeurs:
            test = self.item.IsInIntervalle(valeur)
            if test == 0:
                intervalle = str(self.item.GetIntervalle()[0])+","+str(self.item.GetIntervalle()[1])
                message = "La valeur "+str(valeur)+" n'est pas dans l'intervalle ["+intervalle+"]"
                return message
        return message

    def ajouter_valeurs(self, liste_valeurs):
        """ Cette méthode ajoute les nouvelles valeurs à la liste existante."""
        liste = self.panel.Liste_valeurs.get_liste()
        liste.extend(liste_valeurs)
        self.panel.Liste_valeurs.put_liste(liste)

class Formulaire:
    """
    Cette classe permet de créer une boîte Dialog dans laquelle
    on affiche un formulaire à remplir par l'utilisateur
    """
    def __init__(self,fen_pere,obj_pere=None,titre="",texte="",items=(),mode='query',commande=None):
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
        Crée le dictionnaire des validateurs des objets reconnus par le formulaire
        """
        self.d_validateurs = {}
        self.d_validateurs['rep']  = self.repvalidator
        self.d_validateurs['file'] = self.filevalidator
        self.d_validateurs['cata']= self.catavalidator
        
    def init_fenetre(self):
        """
        Crée la fenêtre Dialog
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
        Crée le label qui affiche le texte à l'intérieur du panneau
        """
        fonte=fontes.standard
        fr_texte = Frame(self.fenetre.interior(),height=60)
        fr_texte.pack(side='top',fill='x',expand=1)
        Label(fr_texte,text = self.texte, font=fonte).place(relx=0.5,rely=0.5,anchor='center')

    def init_items_formulaire(self):
        """
        Crée et affiche les items dans la boîte de dialogue
        """
        self.radiobut = 0
        self.widgets = []
        self.item_widgets = {}
        length_maxi = 0
        for item in self.items:
            if len(item[0])>length_maxi : length_maxi = len(item[0])
        window = self.fenetre.interior()
        for item in self.items :
            label,nature,nom_var,defaut = item
            # création de la frame
            fr_item = Frame(window,height=40,width=700)
            fr_item.pack(side='top',fill='x',expand=1)
            # création du label
            Label(fr_item,text = label).place(relx=0.05,rely=0.4)
            if nature in ('rep','file','cata'):
                # création de l'entry
                e_item = Entry(fr_item) 
                e_item.place(relx=0.5,rely=0.4,relwidth=0.45)
                self.widgets.append(e_item)
                self.item_widgets[item] = e_item
                if defaut : e_item.insert(0,str(defaut))
            elif nature == 'YesNo':
                # création de la StringVar
                var = StringVar()
                setattr(self,'item_'+nom_var,var)
                var.set(defaut)
                # création du radiobouton
                rb1 = Radiobutton(fr_item,text='OUI',variable=var,value='OUI')
                rb2 = Radiobutton(fr_item,text='NON',variable=var,value='NON')
                rb1.place(relx=0.65,rely=0.5,anchor='center')
                rb2.place(relx=0.80,rely=0.5,anchor='center')
                self.widgets.append((rb1,rb2))
                self.item_widgets[item] = var
        # détermination de la méthode à appliquer sur les boutons
        if self.mode == 'query':
            function = self.active
        elif self.mode == 'display':
            function = self.inactive
        else:
            return
        # on applique la méthode sur les boutons (activation ou désactivation)  
        for widget in self.widgets :
            if type(widget) == types.TupleType:
                for widg in widget :
                    apply(function,(widg,),{})
            else:
                apply(function,(widget,),{})

    def active(self,widget):
        """
        Active le widget passé en argument
        """
        widget.configure(state='normal',bg='white')

    def inactive(self,widget):
        """
        Inactive le widget passé en argument
        """
        if not isinstance(widget,Radiobutton) :
            widget.configure(state='disabled',bg='gray95')
        else :
            widget.configure(state='disabled')

# --------------------------------------------------------------------------------
#       Validateurs des noms de répertoire, de fichiers et de catalogues
# -------------------------------------------------------------------------------

    def repvalidator(self,text):
        """
        Teste si text peut faire référence à un répertoire ou non
        Retourne 1 si valide, 0 sinon
        """
        return os.path.isdir(text),'Répertoire introuvable : %s' %text

    def filevalidator(self,text):
        """
        Teste si text peut faire référence à un fichier ou non
        Retourne 1 si valide, 0 sinon
        """
        return os.path.isfile(text),'Fichier introuvable : %s' %text

    def catavalidator(self,text):
        """
        Teste si  text est un chemin d'accès valide à un catalogue
        Retourne 1 si valide, 0 sinon
        """
        return os.path.isfile(text),"Catalogue introuvable : %s" %text

# --------------------------------------------------------------------------------
#       Méthodes callbacks des boutons et de fin
# --------------------------------------------------------------------------------
        
    def execute(self,txt):
        """
        Cette commande est activée à chaque clic sur un bouton.
        Redirige l'action sur la bonne méthode en fonction du bouton activé
        """
        if txt == 'Valider':
            self.fini()
        elif txt in ('OK','Annuler'):
            self.quit()
        elif txt == 'Modifier':
            self.resultat = apply(self.command[1],(),{})
            self.fenetre.destroy()
        else :
            print "Nom de bouton inconnu"
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
                    # une entrée n'est pas valide --> on la met en surbrillance et on quitte la méthode
                    # sans tuer la fenêtre bien sûr
                    widget.selection_range(0,END)
                    return
            dico[nom_var] = valeur
        self.fenetre.destroy()    
        self.resultat=dico
        
    def quit(self):
        self.fenetre.destroy()
        self.resultat=None
        
class ListeChoix :
    """ Cette classe est utilisée pour afficher une liste de choix passée en paramètre
        en passant les commandes à lancer suivant différents bindings """
    def __init__(self,parent,page,liste,liste_commandes=[],liste_marques =[],active ='oui',filtre='non',titre=''):
        self.parent = parent
        self.page = page
        self.liste = liste
        self.dico_labels={}
        self.selection = None
        self.liste_commandes = liste_commandes
        self.liste_marques = liste_marques
        self.arg_selected=''
        self.active = active
        self.titre = titre
        self.filtre = filtre
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
        """ Crée le label correspondant au titre """
        if self.titre == '' : return
        fonte_titre = fontes.standard_gras_souligne
        self.label = Label(self.page,
                           text = self.titre,
                           font = fonte_titre)
        self.label.pack(side='top',pady=2)
        
    def make_entry_filtre(self):
        """ Crée l'entry permettant à l'utilisateur d'entrer un filtre de sélection dans la liste """
        if self.filtre != 'oui' : return
        self.entry = Pmw.EntryField(self.page,labelpos='w',
                                    label_text="Filtre :",
                                    command=self.entry_changed)
        self.entry.pack(side='top',pady=2)
        
    def make_text_box(self):
        """ Crée la fenêtre texte dans laquelle sera affichée la liste """
        self.MCbox = Text (self.page,relief='sunken',bg='gray95',bd=2)
        self.MCscroll = Scrollbar (self.page,command = self.MCbox.yview)
        self.MCscroll.pack(side='right',fill ='y',pady=2)
        self.MCbox.pack(fill='y',expand=1,padx=2,pady=2)
        self.MCbox.configure(yscrollcommand=self.MCscroll.set)

    def affiche_liste(self):
        """ Affiche la liste dans la fenêtre"""
        liste_labels=[]
        self.MCbox.config(state=NORMAL)
        self.MCbox.delete(1.0,END)
        for objet in self.liste :
          if type(objet) == types.InstanceType:
              try:
                  mot = objet.nom
              except:
                  mot = str(objet)
          elif type(objet) in (types.StringType,types.IntType):
              mot = objet
          elif type(objet) == types.FloatType :
              #mot = repr_float(objet)
              mot = str(objet)
          elif type(objet) == types.TupleType :
              mot="("
              premier=1
              for val in objet:
	          if (not premier):
		     mot=mot+"," 
                  else:
                     premier=0
                  mot=mot+str(val)
              mot=mot+")"
          else:
              mot=`objet`
          label = Label(self.MCbox,
                        text = mot,
                        fg = 'black',bg = 'gray95',justify = 'left')
          self.dico_labels[mot]=label
          liste_labels.append(label)
          self.MCbox.window_create(END,
                                   window=label,
                                   stretch = 1)
          self.MCbox.insert(END,'\n')
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

    def chooseitem(self,mot,label,commande):
        """ Active la méthode de choix passée en argument"""
        try:
           commande(mot)
        except AsException,e:
           raison=str(e)
           showerror(raison.split('\n')[0],raison)
        
    def selectitem(self,mot,label,commande) :
        """ Met l'item sélectionné (représenté par son label) en surbrillance
            et lance la commande associée au double-clic"""
        if self.selection != None :
            self.deselectitem(self.selection[1],self.selection[0],self.selection[2],)
        self.highlightitem(label)
        self.selection = (mot,label,commande)
        self.arg_selected = mot
        commande(mot)

    def highlightitem(self,label) :
        """ Met l'item représenté par son label en surbrillance """
        label.configure(bg='#00008b',fg='white')
        
    def markitem(self,label):
        """ Met l'item (représenté par son label) en rouge """
        label.configure(bg='gray95',fg='red')
        
    def deselectitem(self,label,mot='',commande=None) :
        """ Remet l'item (représenté par son label) en noir"""
        label.configure(bg='gray95',fg='black')
        self.arg_selected = ''
        if commande != None : commande(mot)

    def cherche_selected_item(self):
        index=self.MCbox.index(self.selection[1])
        lign,col=map(int,string.split(index,'.'))
        return lign

    def remove_selected_item(self):
        index=self.MCbox.index(self.selection[1])
        lign,col=map(int,string.split(index,'.'))
        del self.liste[lign-1]
        self.affiche_liste()

    def entry_changed(self,event=None):
        """ Cette méthode est invoquée chaque fois que l'utilisateur modifie le contenu
        de l'entry et frappe <Return>"""
        if self.arg_selected != '' : self.deselectitem(self.dico_labels[self.arg_selected])
        filtre = self.entry.get()+"*"
        FILTRE = string.upper(filtre)
        for arg in self.liste :
            if fnmatch.fnmatch(arg,filtre) or fnmatch.fnmatch(arg,FILTRE) :
                self.highlightitem(self.dico_labels[arg])
                index = self.MCbox.index(self.dico_labels[arg])
                self.MCbox.see(index)
                self.arg_selected = arg
                break

    def get_liste_old(self):
        return self.liste

    # PN attention à la gestion des paramétres
    # cela retourne H = 1 , et ni H, ni 1
    #            print repr(val)
    #            print val.__class__.__name__
    def get_liste(self):
        l=[]
        for val in self.liste:
#            try:
#                v = eval(val)
#    		l.append(v)
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
      """ Calcule l'incrément de progression de la barre en fonction
          du nombre d'opérations à effectuer afin que le compteur
          soit à 100% à la fin des opérations"""
      self.increment = 100./nb
      self.progress.update()

class Ask_Format_Fichier :
    """
    Cette classe permet de créer une fenêtre Toplevel dans laquelle
    on propose le choix du format de fichier de commandes à ouvrir
    """
    def __init__(self,appli):
        self.fenetre = Toplevel()
        self.fenetre.configure(width = 250,height=150)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
        self.fenetre.title("Choix du format du fichier de commandes")
        # définition des frames
        self.frame_texte = Frame(self.fenetre)
        self.frame_radioboutons = Frame(self.fenetre)
        self.frame_bouton_ok = Frame(self.fenetre)
        self.frame_texte.place(relx=0,rely=0,relwidth=1,relheight=0.3)
        self.frame_radioboutons.place(relheight=0.5,relx=0,rely=0.3,relwidth=1.)
        self.frame_bouton_ok.place(relheight=0.2,relx=0,rely=0.8,relwidth=1.)
        # définition de la zone texte et du scrollbar
        zone_texte = Label(self.frame_texte,text = "Format du fichier à ouvrir :")
        zone_texte.pack(side='top',fill='both',expand=1,padx=5,pady=10)
        # définition des radioboutons
        Radiobutton(self.frame_radioboutons,text='Format Aster (Code_Aster --> v5)',
                    variable=appli.format_fichier,value='Aster').pack(anchor='n')
        Radiobutton(self.frame_radioboutons,text='Format Python (Code_Aster v6-->)',
                    variable=appli.format_fichier,value='Python').pack(anchor='n')
        # création du bouton OK
        Button(self.frame_bouton_ok,text='OK',command=self.quit).pack(anchor='n')
        # centrage de la fenêtre
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
        # frame contenant le texte à afficher 
        self.frame_text = Frame(self.frame)
        self.frame_text.place(relwidth=1,relheight=0.75,rely=0)
        # frame contenant le canvas de la barre
        self.frame_canv = Frame(self.frame)
        self.frame_canv.place(relwidth=1,relheight=0.25,rely=0.75)
        # canvas dans lequel sera affichée la barre K2000
        self.canvas = Canvas(self.frame_canv)
        self.canvas.place(relx=0.5,rely=0.5,relheight=0.8,relwidth=0.8,anchor='center')
        # on affiche le texte et la barre
        self.build_text(text)
        self.build_batons()
        #self.overrideredirect(1)
        # on active la barre ...
        self.master.after(1000,self.launch)
        # on centre la fenêtre
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
        Construit la suite de bâtons dans le canvas
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
        Active la barre K2000 en affichant les bâtons avec des couleurs en dégradé
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
        Remplace le texte affiché par new_text
        """
        self.texte_var.set(new_text)
        
    def quit(self):
        self.quit = 1        

class ListeChoixParGroupes(ListeChoix) :
    """ 
        Cette classe est utilisée pour afficher une liste de commandes classées par
        groupes. L'utilisateur peut réaliser des actions de selection
        qui déclenchent des actions spécifiées par les bindings contenus dans liste_commandes
    """
    def __init__(self,parent,page,liste_groupes,dict_groupes,liste_commandes=[],liste_marques =[],
                      active ='oui',filtre='non',titre=''):
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
        self.init()

    def affiche_liste(self):
        """ Affiche la liste dans la fenêtre"""
        liste_labels=[]
        self.MCbox.config(state=NORMAL)
        self.MCbox.delete(1.0,END)
        for grp in self.liste_groupes:
           # On itère sur les groupes
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
              self.MCbox.window_create(END,
                                   window=label,
                                   stretch = 1)
              self.MCbox.insert(END,'\n')
              if self.active == 'oui':
                  label.bind(self.liste_commandes[0][0],
                         lambda e,s=self,c=self.liste_commandes[0][1],x=cmd,l=label : s.selectitem(x,l,c))
                  label.bind(self.liste_commandes[1][0],
                         lambda e,s=self,c=self.liste_commandes[1][1],x=cmd,l=label : s.deselectitem(l,x,c))
                  label.bind(self.liste_commandes[2][0],
                         lambda e,s=self,c=self.liste_commandes[2][1],x=cmd,l=label : s.chooseitem(x,l,c))

        for marque in self.liste_marques:
           try:
              self.markitem(liste_labels[marque])
           except:
              pass

        self.MCbox.config(state=DISABLED)
        self.selection = None

    def entry_changed(self,event=None):
        """ 
            Cette méthode est invoquée chaque fois que l'utilisateur modifie le contenu
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
                index = self.MCbox.index(self.dico_labels[grp])
                self.MCbox.see(index)
                # On ne selectionne pas le groupe
                #self.arg_selected = grp
                # On a trouve un groupe on arrete la recherche
                return

        for grp in self.liste_groupes:
           for cmd in self.dict_groupes[grp] :
              if fnmatch.fnmatch(cmd,filtre) or fnmatch.fnmatch(cmd,FILTRE) :
                 self.highlightitem(self.dico_labels[cmd])
                 index = self.MCbox.index(self.dico_labels[cmd])
                 self.MCbox.see(index)
                 self.arg_selected = cmd
                 # On a trouve une commande  on arrete la recherche
                 return

