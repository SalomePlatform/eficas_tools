# -*- coding: utf-8 -*-
SUCCES,ECHEC = 1,0
OUI,NON = 1,0

## constantes pour les tests de versions 

python_min = 20
tcl_min = 83
tk_min  = 83
pmw_min = 85
test = 0

try:
    import sys,string,re,types,traceback
    import os,commands
except Exception,e:
    print "Mauvaise installation de Python"
    print str(e)

REPERTOIRE = os.path.abspath(os.curdir)

def strip_points(chaine):
    """
    Enlève les caractères autres que les chiffres des chaînes
    """
    x=""
    for i in range(len(chaine)):
        try:
            dummy = float(chaine[i])
            x=x+chaine[i]
        except:
            pass
    return x

class Test_Environnement :
    def __init__(self):
        self.l_errors = []

    def test_plate_forme(self):
        """
        Teste que la plate-forme est bien supportée
        """
        if os.name not in ('nt','posix'):
            self.l_errors.append("La plate-forme %s n'est pas supportée" %os.name)
            
    def test_version_python(self):
        """
        Test de la version de python
        """
        version = sys.version
        n = string.index(version,"(") - 1
        vpyt = strip_points(version[0:n])[0:2]     ## recupere les 2 premiers caracteres
        if int(vpyt)<python_min :
            self.l_errors.append("La version %s de python n'est plus supportée" %version[0:n])

    def test_tcl_tk(self):
        """
        Test des versions de tcl et tk
        """
        try:
            import Tkinter
            vtcl = Tkinter.tkinter.TCL_VERSION
            vtk  = Tkinter.tkinter.TK_VERSION
            # version tcl
            x = strip_points(vtcl)
            if int(x)<tcl_min :
                self.l_errors.append("La version %s de tcl n'est plus supportée" %vtcl)
            # version tk
            x = strip_points(vtk)
            if int(x)<tk_min :
                self.l_errors.append("La version %s de tk n'est plus supportée" %vtk)
        except Exception,e:
            self.l_errors.append("Tkinter n'est pas installé")
            print str(e)

    def test_Pmw(self):
        """
        Test de la version de Pmw
        """
        try:
            import Pmw
            vpmw = Pmw._version
            x = strip_points(vpmw)
            if int(x)<pmw_min :
                self.l_errors.append("La version %s de Pmw n'est plus supportée" %vpmw)
        except:
            self.l_errors.append("Pmw n'est pas installé")

    def test(self):
        """
        Active les tests de version Python, versions Tcl/Tk et Pmw
        """
        self.test_plate_forme()
        self.test_version_python()
        self.test_tcl_tk()
        self.test_Pmw()
        if not len(self.l_errors):
            print "Environnement Ok"
            return 1
        else :
            print "Il manque des prérequis"
            print "EFICAS ne peut pas être installé"
            print "Erreurs : ",string.join(self.l_errors)
            return 0

class Slider:
    def __init__(self, master=None, orientation="horizontal", min=0, max=100,
                 width=100, height=25, autoLabel="true", appearance="sunken",
                 fillColor="blue", background="black", labelColor="yellow",
                 labelText="", labelFormat="%d%%", value=50, bd=2):
        # preserve various values
        self.master=master
        self.orientation=orientation
        self.min=min
        self.max=max
        self.width=width
        self.height=height
        self.autoLabel=autoLabel
        self.fillColor=fillColor
        self.labelColor=labelColor
        self.background=background
        self.labelText=labelText
        self.labelFormat=labelFormat
        self.value=value
        self.frame=Tkinter.Frame(master, relief=appearance, bd=bd)
        self.canvas=Tkinter.Canvas(self.frame, height=height, width=width, bd=0,
                                   highlightthickness=0, background=background)
        self.scale=self.canvas.create_rectangle(0, 0, width, height,
                                                fill=fillColor)
        self.label=self.canvas.create_text(self.canvas.winfo_reqwidth() / 2,
                                           height / 2, text=labelText,
                                           anchor="c", fill=labelColor)
        self.update()
        self.canvas.pack(side='top', fill='x', expand='no')

    def update(self):
        # Trim the values to be between min and max
        value=self.value
        if value > self.max:
            value = self.max
        if value < self.min:
            value = self.min
        # Preserve the new value
        c=self.canvas
        # Adjust the rectangle
        if self.orientation == "horizontal":
            c.coords(self.scale,0, 0,float(value) / self.max * self.width, self.height)
        else:
            c.coords(self.scale,0, self.height - (float(value) / self.max*self.height),self.width, self.height)
        # Now update the colors
        c.itemconfig(self.scale, fill=self.fillColor)
        c.itemconfig(self.label, fill=self.labelColor)
        # And update the label
        if self.autoLabel=="true":
            c.itemconfig(self.label, text=self.labelFormat % value)
        else:
            c.itemconfig(self.label, text=self.labelFormat % self.labelText)
        c.update_idletasks()
try :
    import Tkinter
    import Pmw
    from tkMessageBox import showinfo,askyesno,showerror,askretrycancel
except:
    pass

class SplashScreen(Tkinter.Toplevel):
    """ Provides a splash screen. Usage:
        Subclass and override 'CreateWidgets()'
        In constructor of main window/application call
        - S = SplashScreen(main=self)        (if caller is Toplevel)
        - S = SplashScreen(main=self.master) (if caller is Frame)
        - S.quit()  after you are done creating your widgets etc.
    """
    def __init__(self, master,**args):
        Tkinter.Toplevel.__init__(self, master, relief='groove',borderwidth=5)
        self.protocol("WM_DELETE_WINDOW",lambda x=0: x+x  )       # pour ne pas détruire la fenêtre en pleine copie de fichiers
        self.main = master
        if self.main != None :
            self.main.withdraw()
        self.frame = Tkinter.Frame(self)
        self.frame.pack(expand=1,fill='both')
        self.init(args)
        self.geometry("300x200")
        self.resizable(0,0)
        self.CreateWidgets()

    def init(self,args={}):
        self.text = Tkinter.StringVar()
        self.text.set('')
        self.icone = 'Editeur/icons/logo_edf.gif'
        self.barre = 'non'
        if args == {} : return
        if args.has_key('text'):
            self.text.set(args['text'])
        if args.has_key('titre'):
            self.title(args['titre'])
        if args.has_key('code'):
            self.code = args['code']
        else:
            self.code = 'inconnu'
        if self.code == 'ASTER' :
            self.icone = 'Editeur/icons/code_aster.gif'
        
    def CreateWidgets(self):
        fic_image = os.path.join("./", self.icone)
        if os.path.exists(fic_image):
            self.catIcon = Tkinter.PhotoImage(file=os.path.join("./", self.icone))
            Tkinter.Label(self.frame, image=self.catIcon).pack(side=Tkinter.TOP)
        else:
            Tkinter.Label(self.frame, text = "EFICAS pour Code_Aster").pack(side=Tkinter.TOP)
        self.label = Tkinter.Label(self.frame, textvariable=self.text)
        self.label.pack(side=Tkinter.TOP,expand=1,fill='both')
        self.progress = Slider(self.frame,value=0,max=100,orientation='horizontal',
                               fillColor='blue',width=200,height=30,
                               background='white',labelColor='red')

    def update_barre(self,event=None):
        """ Permet de faire avancer la barre de progression """
        try:
            self.progress.value = self.progress.value+self.increment
            self.progress.update()
            #self.after(100,self.update_barre)
        except:
            pass

    def configure_barre(self):
        """ Calcule l'incrément de progression de la barre en fonction
        du nombre d'opérations à effectuer afin que le compteur
        soit à 100% à la fin des opérations"""
        self.increment = 100./self.ratio
        self.progress.update()

    def configure(self,**args):
        if args.has_key('text'):
            self.text.set(args['text'])
        if args.has_key('titre'):
            self.title(args['titre'])
        if args.has_key('barre'):
            old = self.barre
            self.barre = args['barre']
            if self.barre == 'oui' and old == 'non':
                self.progress.frame.pack(in_=self.frame,side='top')
            elif self.barre == 'non' and old == 'oui':
                self.progress.frame.pack_forget()
        if args.has_key('ratio'):
            self.ratio = args['ratio']
            self.configure_barre()
        self.update()
        
    def quit(self):
        self.progress = None
        self.withdraw()
        self.main.update()
        self.main.deiconify()

def centerwindow(window,parent = 'avec'):
    if parent =='avec':
        parent = window.winfo_parent()
        if type(parent) == types.StringType:
            try:
                parent = window._nametowidget(parent)
            except:
                parent = window
    # Find size of window.
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    if width == 1 and height == 1:
        # If the window has not yet been displayed, its size is
        # reported as 1x1, so use requested size.
        width = window.winfo_reqwidth()
        height = window.winfo_reqheight()
    # Place in centre of screen:
    if parent =='avec' :
        x = (window.winfo_screenwidth() - width) / 2 - parent.winfo_vrootx()
        y = (window.winfo_screenheight() - height) / 3 - parent.winfo_vrooty()
    else:
        x = (window.winfo_screenwidth() - width) / 2 
        y = (window.winfo_screenheight() - height) / 3
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    window.geometry('+%d+%d' % (x, y))
    
class config_item:
    """
    Classe utilisée pour représenter chaque option de configuration
    """
    def __init__(self, pere, nom):
        self.nom = nom
        self.pere = pere
        self.entree_value = None
        self.default = None
        self.test = None
        self.pere.register_item(self)

    def get_valeur(self):
        return os.path.abspath(self.entree.get())
    
    def set_entree(self,entree):
        self.entree = entree
        self.pere.register_entree(entree)

class Config(Tkinter.Toplevel):
    """
    Classe principale : une instance de Config est utilisée pour
    créer l'interface. Toutes les actions (création de répertoire, copie
    de fichiers ...) sont réalisées par des méthodes de Config ou de ses
    composants
    """
    pat_rep = re.compile(r'^(rep_)([\w_]*)')             # expression réguliere pour reconnaitre les
                                                         # les options qui désignent des répertoires
    def __init__(self, parent):
        self.master = parent
        Tkinter.Toplevel.__init__(self,None)
        parent.withdraw()
        self.title("Installation d'EFICAS")
        self.geometry("500x320+0+0")
        centerwindow(self)
        self.install_running = 0
        #évite que la fenêtre puisse être détruite en pleine copie de fichiers
        self.protocol("WM_DELETE_WINDOW",self.exit  )
        # création des frames
        self.frame_gen = Tkinter.Frame(self,bd=1,relief='groove')
        self.frame_gen.place(relx=0,rely=0,relwidth=1,relheight=0.9 )
        self.frame_but = Tkinter.Frame(self,bd=1,relief='groove')
        self.frame_but.place(relx=0,rely=0.9 ,relheight=0.1 ,relwidth=1)
        # création des items de configuration
        self.make_items_config()
        # remplissage de la frame générale
        self.make_frame_gen()
        # remplissage de la frame boutons
        self.make_frame_but()
        # création boîtes de dialogue
        self.init_complementaire()
        # init système
        self.init_systeme()
        
    def make_items_config(self):
        """
        Création des objets Config_item
        """
        self.items = []
        self.items_a_creer = []
        self.liste_rep_crees = []
        self.entrees = []
        # designation, texte d'invite , option par defaut(unix), option par defaut(windows), flag obligatoire/facultatif
        self.l_tx_items = (('rep_install'   ,
                            "Répertoire d'installation :",
                            '',
                            '',
                            'o'),
                           ('rep_travail'   ,
                            'Répertoire de travail :',
                            'tmp',
                            'tmp',
                            'f'),
                           ('rep_mat'       ,
                            'Répertoire matériaux :',
                            None,
                            None,
                            'f'),
                           ('rep_docaster'  ,
                            "Chemin d'accès à la doc Aster :" ,
                            None,
                            None,
                            'f'
                            ),
                           ('acrobat'       ,
                            'Exécutable Acrobat Reader :',
                            '/usr/bin/acroread',
                            'acrobat.exe',
                            'o')
                           )

        for item in self.l_tx_items:
            nom_item = item[0]
            setattr(self,nom_item,config_item(self,nom_item))

    def make_frame_gen(self):
        """
        Création des zones de saisie des paramètres généraux
        """
        # Création du label titre de la frame
        self.information = Tkinter.Label(self.frame_gen,text="CONFIGURATION D'EFICAS")
        self.information.pack(side="top",pady=10)
        # création des widgets de saisie des items
        for txt in self.l_tx_items:
            nom_item = txt[0]
            txt_item = txt[1]
            if os.name == 'nt':
                default_value = txt[3]
            else:
                default_value = txt[2]
            item = getattr(self,nom_item)
            wdg_item = Pmw.EntryField(self.frame_gen,
                                      labelpos = 'w',
                                      label_text = txt_item,
                                      command = lambda s=self,i=item : s.select_next_entry(i.entree))
            item.default_value = default_value
            item.statut = txt[4]
            item.set_entree(wdg_item)
        # on affiche les entrées
        for entree in self.entrees:
            entree.pack(fill='x', expand=1, padx=10, pady=5)
        Pmw.alignlabels(self.entrees)
        self.entrees[0].focus_set()
        #self.rep_cata_dev.entree.configure(entry_state = 'disabled')
        self.display_defaults()
        
    def make_frame_but(self):
        """
        Création des boutons de commande Installer et Annuler
        """
        self.validButton    = Tkinter.Button(self.frame_but, text = 'Installer', command = self.run_install)
        self.exitButton     = Tkinter.Button(self.frame_but,
                                             text = 'Annuler',
                                             command = lambda s=self : s.exit(annule='oui'))
        self.exitButton.place(relx=0.35,rely=0.5,anchor='center')
        self.validButton.place(relx=0.65,rely=0.5,anchor='center')

    def init_complementaire(self):
        """
        Création de widgets complémentaires (boîtes de dialogue ...)
        """
        self.erreur_dialog = Pmw.Dialog(self,
                                        buttons = ('Modifier', 'Annuler'),
                                        defaultbutton = 'Modifier',
                                        title = 'Erreur',
                                        command = self.erreur_exec)
        self.erreur_dialog.withdraw()
        self.fatale_dialog = Pmw.Dialog(self,
                                        buttons = ('Annuler',),
                                        title = 'Fatal',
                                        command = self.fatale_exec)
        self.fatale_dialog.withdraw()
        self.info_dialog = Pmw.Dialog(self,
                                        buttons = ('Ok',),
                                        title = 'Attention')
        self.info_dialog.configure(command=self.info_dialog.withdraw())
        self.info_dialog.withdraw()
        self.attente = SplashScreen(None,code="ASTER")
        self.attente.withdraw()

    def init_systeme(self):
        """
        Détermine les commandes à exécuter en fonction de l'OS
        """
        self.d_commandes = {}
        if os.name == 'nt':
            self.d_commandes['decompress'] = "unzip.exe "
            self.d_commandes['copy'] = "copy "
            self.d_commandes['delete'] = "del "
        elif os.name == 'posix':
            self.d_commandes['decompress'] = "gunzip "
            self.d_commandes['copy'] = "cp "
            self.d_commandes['delete'] = "rm "

    def run_install(self):
        """
        Lance l'installation proprement dite d'EFICAS
        """
        self.install_running = 1
        self.afficher_splash()
        self.deactivate_entries()           #  Les entrees et les boutons sont desactivees
        self.deactivate_buttons()           #  pendant les operations d'installation
        #self.decompress_archive()
        #if not os.path.exists(os.path.join(REPERTOIRE,'Eficas')):
        #    self.afficher_fatale("Il manque des fichiers d'EFICAS")
        #    self.install_running = 0
        #    return
        self.nb_fichiers = self.compte_fichiers(REPERTOIRE)
        if self.nb_fichiers == 0:
            self.afficher_fatale("Il manque des fichiers d'EFICAS")
            self.install_running = 0
            return
        # essaie de creer les repertoires.
        try:
            if self.make_dirs() == ECHEC :                             
                self.activate_entries()                               
                self.activate_buttons()                               
                self.install_running = 0
                return
        except:
            self.install_running = 0
            self.afficher_fatale("Impossible de créer certains répertoires")
            
        # affiche la fenêtre avec la barre de progression
        self.afficher_copie_fichiers()          
        # essaie de copier les fichiers d'EFICAS
        try:
            if  self.move_files() == ECHEC:                           
                self.afficher_echec("Impossible de copier les fichiers d'EFICAS")
                self.activate_buttons()
                self.install_running = 0
                return
        except :
	    traceback.print_exc()
            self.install_running = 0
            self.afficher_fatale("Impossible de copier certains fichiers")

        #self.rm_temp_dirs()                     # efface les répertoires temporaires
        try:
            self.creer_fic_conf()                   # crée le fichier eficas.conf
        except:
            afficher_info("Impossible de créer le fichier de configuration\n Il est possible de le faire a la main")
#        self.install_running = 0
        self.afficher_install_terminee()        # A ce stade tout est fait et il ne reste plus qu'à attendre
                                                # un clic de souris pour sortir

    def display_defaults(self):
        """
        Affiche les valeurs par défaut dans les zones de saisie
        """
        # racine indique la racine de l'arborescence
        if os.name == 'nt':
            racine = 'C:\\'
        else:
            racine = os.environ['HOME']
        # remplit les zones de saisie avec les options par défaut
        for item in self.items:
            if item.default_value == None : continue
            item.default_value = os.path.join(racine,item.default_value)
            item.entree.insert(0,item.default_value)

    def register_item(self,item):
        """
        Enregistre l'item dans la liste des items et éventuellement
        dans la liste des items à créer (répertoires)
        """
        self.items.append(item)
        if self.pat_rep.match(item.nom) :
            self.items_a_creer.append(item)

    def register_entree(self,entree):
        """
        Enregistre la zone de saisie dans la liste des zones
        """
        self.entrees.append(entree)

    def select_next_entry(self,entree):
        """
        Place le focus dans l'entry suivant celle passée en argument
        """
        index = self.entrees.index(entree)+1
        if index != len(self.entrees):
            self.entrees[index].component('entry').focus()

    def activate_entries(self):
        """
        Active les entrées. Les zones de saisie deviennent éditables.
        """
        for item in self.entrees:
            item.configure(entry_state='normal')

    def deactivate_entries(self):
        """
        Désactive les entrées. Les zones ne sont plus éditables.
        """
        for item in self.entrees:                                #  Les entrees sont desactivees
            item.configure(entry_state='disabled')               #  pendant les operations d'installation

    def activate_buttons(self):
        """
        active les boutons valider et annuler
        """
        self.validButton.configure(state = 'normal')
        self.exitButton.configure(state = 'normal')

    def deactivate_buttons(self):
        """
        désactive des boutons valider de annuler
        """
        self.validButton.configure(state = 'disabled')
        self.exitButton.configure(state = 'disabled')

    def erreur_exec(self, result):
        """
        Callback exécuté lorsque l'utilisateur clique sur un des boutons
        Modifier/Annuler de la fenêtre de dialogue qui lui présente les erreurs
        """
        self.erreur_dialog.deactivate(result)
        self.removedir()
        if result == 'Annuler':
            self.install_running = 0
            self.exit(annule='non')

    def fatale_exec(self, result):
        """
        Callback exécuté lorsque l'utilisateur clique sur le bouton
        Quitter de la fenêtre de dialogue qui lui présente les erreurs fatales
        Seule solution : sortir de l'installation
        """
        self.fatale_dialog.deactivate(result)
        self.install_running = 0
        self.exit(annule='oui')
        
    def test_confirmation(self,flag,nom):
        """
        Callback activé par le clic sur bouton fenêtre demandant confirmation
        avant création répertoire facultatif
        """
        if flag == 'NON':
            self.confirmation.destroy()
            self.TEST_confirmation_avant_creation = NON
            return 
        else :
            self.confirmation.destroy()
            self.TEST_confirmation_avant_creation = OUI            
            
    def afficher_fatale(self, message):
        """
        Affiche les erreurs fatales
        """
        self.attente.withdraw()
        w = Tkinter.Label(self.fatale_dialog.interior(),text = message, pady = 5)
        w.pack(expand = 1, fill = 'both', padx = 4, pady = 4)
        self.fatale_dialog.configure(deactivatecommand = w.destroy)
        self.fatale_dialog.activate()

    def afficher_echec(self, message):
        """
        Affiche un message d'erreur
        Par construction, dès que l'on passe par cette méthode, on sort de l'installation
        en passant le flag install_running à 0
        """
        self.attente.withdraw()
        w = Tkinter.Label(self.erreur_dialog.interior(),text = message, pady = 5)
        w.pack(expand = 1, fill = 'both', padx = 4, pady = 4)
        self.erreur_dialog.configure(deactivatecommand = w.destroy)
        self.erreur_dialog.activate()

    def confirmation_avant_creation(self,repertoire):
        """
        Affiche une boite de dialogue pour confirmer la création
        d'un répertoire facultatif.
        """
        self.attente.withdraw()
        self.confirmation = Pmw.Dialog(self,
                                       buttons = ('OUI', 'NON'),
                                       defaultbutton = 'OUI',
                                       title = "Répertoire inexistant",
                                       command = lambda f,s=self,r=repertoire : s.test_confirmation(f,r))
        self.confirmation.withdraw()
        Tkinter.Label(self.confirmation.interior(),
                      text="Le répertoire %s n'existe pas \n Voulez-vous le créer ?" %repertoire).pack(side='top')
        self.confirmation.activate(geometry='centerscreenalways')
        return self.TEST_confirmation_avant_creation
  
    def afficher_splash(self):
        """
        Afficher la boite de message 
        """
        self.attente.deiconify()
        self.attente.tkraise()
        centerwindow(self.attente)
        self.attente.configure(titre="Installation d'EFICAS",
                               text="Vérification intégrité sources Eficas",
                               barre="non")
        
    def afficher_info(self,message):
        """
        Afficher une boite de warning
        """
        w = Tkinter.Label(self.info_dialog.interior(),text = message, pady = 5)
        w.pack(expand = 1, fill = 'both', padx = 4, pady = 4)
        self.info_dialog.configure(deactivatecommand = w.destroy)
        self.info_dialog.activate()
        
    def afficher_copie_fichiers(self):
        """
        Afficher la boite de message avec la barre de progression
        """
        self.attente.deiconify()
        self.attente.tkraise()
        self.attente.configure(titre="Installation d'EFICAS",
                               text="copie des fichiers",
                               barre="oui")
        self.attente.ratio = self.nb_fichiers
        self.attente.configure_barre()

    def afficher_install_terminee(self):
        """
        Afficher le message Installation terminée
        """
        self.withdraw()
        self.attente.configure(titre="Installation d'EFICAS",
                               text="Installation terminée",
                               barre="non")
        self.exitButton.place_forget()
        self.validButton.place_forget()
        self.validButton = Tkinter.Button(self.attente.frame,
                                          text = 'Quitter',
                                          command = self.exit)
        self.validButton.pack(side='top',pady=5)
        self.install_running = 0

    def decompress_archive(self) :
        """
        Décompresse l'archive d'EFICAS dans un répertoire temporaire (.)
        """
        print "decompress_archive"
        #try:
        commande = os.path.join(REPERTOIRE,self.d_commandes['decompress'])
        fichier = os.path.join(REPERTOIRE,"eficas.zip")
        print 'commande =',commande
        print 'fichier =',fichier
        os.execv(commande,("eficas.zip",))
        #except:
        #    self.affiche_echec("Erreur dans la décompression")

    def normaliser_chemin(self, nom):
        """
        Retourne le chemin d'accès complet à nom
        """
        return os.path.abspath(os.path.expanduser(nom))

    def discriminer_noms(self):
        """
        Emet un message d'alerte si des zones de saisie ne sont pas remplies
        ou si des noms de répertoires à créer sont identiques.
        """
        liste_noms = []
        for item in self.items_a_creer:
            nom = item.entree.get()
            if nom == self.rep_install.entree.get():        # il faut ajouter 'Eficas' au chemin du repertoire
                nom = os.path.join(nom,"Eficas")            # d'installation
            liste_noms.append(nom)

        test = SUCCES
        for item in self.items_a_creer:
            nom = item.entree.get()
            if len(nom) == 0 :
                test = ECHEC
                message = "attention : certains répertoires n'ont pas de nom"
                self.afficher_echec(message)
            item.entree.component('entry').focus()
            break

        if test == ECHEC :
            return test

        for item in self.items_a_creer:
            nom = item.entree.get()
            if liste_noms.count(nom) >1 :
                test = ECHEC
                message = "attention : certains répertoires ont le même nom"
                self.afficher_echec(message)
            item.entree.component('entry').focus()
            break

        return test

    def compte_fichiers(self,path):
        """
        Dénombre les fichiers présents dans le répertoire Eficas (et ses sous-répertoires)
        """
        nb = 0
        l_fic = os.listdir(path)
        l_rep = []
        for fic in l_fic :
            if os.path.isdir(os.path.join(path,fic)):
                l_rep.append(fic)
            else:
                nb = nb+1
        for rep in l_rep :
            nb = nb + self.compte_fichiers(os.path.join(path,rep))
        return nb

    def creer_fic_conf(self):
        """
        Crée le fichier editeur.ini a partir des données saisies
        par l'administrateur.
        """
        fichier_conf = os.path.join(self.normaliser_chemin(self.rep_install.get_valeur()),"Eficas/Aster/editeur.ini")
        f = open(fichier_conf,'w')
        f.write("path_doc        =    "+'"'+self.normaliser_chemin(self.rep_docaster.get_valeur())+'"\n')
        f.write("exec_acrobat    =    "+'"'+self.normaliser_chemin(self.acrobat.get_valeur())+'"\n')
        f.write('isdeveloppeur   =    "NON"\n')
        f.write("rep_travail     =    "+'"'+self.normaliser_chemin(self.rep_travail.get_valeur())+'"\n')
        f.write("rep_cata        =    "+'"'+os.path.join(self.normaliser_chemin(self.rep_install.get_valeur()),"Eficas/Aster/Cata/")+'"\n') # attention au dernier slash
        f.write("rep_mat         =    "+'"'+self.normaliser_chemin(self.rep_mat.get_valeur())+'"\n')
        cata = """catalogues = (('ASTER','v6',rep_cata + 'cata_STA6.py','python','defaut'),)\n"""
        f.write(cata)
        f.close()
	

    def move_files(self):
        """
        Déplace les fichiers Eficas du répertoire temporaire vers
        leur répertoire de destination
        """
        # création du répertoire Eficas
        rep_eficas = os.path.join(self.rep_install.get_valeur(),'Eficas')
        self.copy_rep(REPERTOIRE,rep_eficas)

    def copy_rep(self,rep_dep,rep_arr):
        """
        Copie le répertoire path_dep et ses sous-répertoires dans path_arr
        """
        l_fichiers = os.listdir(rep_dep)
        if not os.path.exists(rep_arr) :
            # création du répertoire d'arrivée quand il n'existe pas 
            self.mkdirs(rep_arr)
        for fic in l_fichiers :
            nom_complet_dep = os.path.join(rep_dep,fic)
            nom_complet_arr = os.path.join(rep_arr,fic)
            if os.path.isfile(nom_complet_dep):
                commande_copie = self.d_commandes['copy']+nom_complet_dep+' '+nom_complet_arr
                commande_delete= self.d_commandes['delete']+nom_complet_dep
                try:
                    os.system(commande_copie)
                    #os.system(commande_delete)
                    self.attente.update_barre()
                except Exception,e:
                    pass
            elif os.path.isdir(nom_complet_dep):
                self.copy_rep(nom_complet_dep,nom_complet_arr)

    def rm_temp_dirs(self):
        """
        Détruit le répertoire temporaire de l'archive d'Eficas
        """
        rep_arch = os.path.join(REPERTOIRE,'Eficas')
        self.rm_r(rep_arch)

    def make_dirs(self):
        """
        Crée les répertoires d'accueil des fichiers d'EFICAS
        """
        # création des répertoires dont l'utilisateur a donné le nom
        if self.discriminer_noms() == ECHEC:
            return ECHEC
        for item in self.items_a_creer:
            if not item.entree.get():
                continue
            nom = item.get_valeur()
            if nom == self.normaliser_chemin(self.rep_install.entree.get()):        # il faut ajouter 'Eficas' au chemin du repertoire
                nom = os.path.join(nom,"Eficas")            # d'installation
            item.test = self.essai_creer(nom,item.statut)
            if item.test == ECHEC :
                item.entree.component('entry').focus()
                return ECHEC
        return SUCCES

    def essai_creer(self, nom, statut):
        """
        Essaie de créer le répertoire nom s'il n'existe pas déjà.
        Si statut == 'f' et si le fichier n'existe pas, demande
        confirmation avant création
        """
        repertoire = self.normaliser_chemin(nom)                # repertoire = chemin absolu de nom
        if os.path.exists(repertoire):
            if statut == 'o' :
                self.afficher_echec("Un fichier ou répertoire de nom "+ repertoire+ " existe déjà !\n"+
                                "L'installation ne peut continuer")
                return ECHEC
            else:
                return SUCCES

        if statut == 'f' :
            # on demande confirmation de création à l'utilisateur
            test = self.confirmation_avant_creation(repertoire)
            if test == NON:
                return SUCCES

        try:
            test = self.mkdirs(repertoire)
            return SUCCES
        except Exception,e:
            message = "La création de "+repertoire+" a échoué :\n %s \n Vérifiez vos droits d'écriture"  %str(e)  # message d'erreur
            self.afficher_echec(message)
            return ECHEC

    def mkdirs(self,rep):
        """
        Création récursive des répertoires d'installation.
        Les noms des répertoires crées sont stockés dans
        une liste dont se sert la méthode removedir pour
        restaurer l'environnement initial en cas d'annulation.
        """
        if rep==os.path.dirname(rep):
            return SUCCES

        if os.path.exists(os.path.dirname(rep)):
            os.mkdir(rep)
            self.liste_rep_crees.append(rep)
            return SUCCES
        else:
            test = self.mkdirs(os.path.dirname(rep))
            if test == SUCCES:
                os.mkdir(rep)
                self.liste_rep_crees.append(rep)
                return SUCCES
            else:
                return ECHEC

    def rm_r(self,path):
        """
        Detruit récursivement path
        """
        if not os.path.exists(path):
            return
        try:
            if len(os.listdir(path))!=0:
                for entree in os.listdir(path):
                    entree = os.path.join(path,entree)
                    self.rm_r(entree)
            os.rmdir(path)
        except Exception,e:
            self.afficher_info("Impossible de détruire le répertoire : "+path+"\n"+"\n"+str(e)+"\n L'installation continue néanmoins")

    def removedir(self):
        """
        Destruction des répertoires déja crées (en cas d'annulation)
        """
        for rep in self.liste_rep_crees:
            self.rm_r(rep)
        self.liste_rep_crees = []

    def exit(self,annule='non'):
        """
        Tente de sortir de l'application.
        Echoue si installation en cours
        """
        if self.install_running :
            # l'installation est en cours --> on interdit la sortie
            self.afficher_info("Impossible de quitter tant que l'installation est en cours\n Veuillez patienter")
        else:
            if annule == 'oui' : self.removedir()
            self.master.quit()

if __name__ == '__main__':
    test = Test_Environnement().test()
    if not test :
        # environnement incomplet --> on sort de la procédure d'installation
        sys.exit()
    else:
        import Tkinter
        import Pmw
        root = Tkinter.Tk()
        Pmw.initialise(root)
        try:
            principal = Config(root)
            root.mainloop()
        except Exception,e:
            print "Erreur non prévue rencontrée : ",str(e)
            print "Veuillez prévenir la maintenance"
            sys.exit()
