"""
    Ce module permet de créer, mettre à jour et détruire
    un écran Splash
"""
from Tkinter import *

from centerwindow import centerwindow
from Tools.foztools.foztools import Slider
import fontes
import images

_splash=None

def init_splash(*pos,**args):
   global _splash
   _splash=SplashScreen(*pos,**args)

def fini_splash():
   global _splash
   _splash.quit()
   _splash=None

class SplashScreen(Toplevel):
    """ 
        Provides a splash screen. Usage:
        Subclass and override 'CreateWidgets()'
        In constructor of main window/application call
        - S = SplashScreen(main=self)        (if caller is Toplevel)
        - S = SplashScreen(main=self.master) (if caller is Frame)
        - S.quit()  after you are done creating your widgets etc.
    """
    def __init__(self, master=None,**args):
        Toplevel.__init__(self, master, relief='groove',
                          borderwidth=5)
        self.main = master
        if self.main != None :
            self.main.iconify()
        self.withdraw()
        self.frame = Frame(self)
        self.frame.pack(expand=1,fill='both')
        self.init(args)
        self.geometry("300x200")
        self.resizable(0,0)
        centerwindow(self)
        self.CreateWidgets()
        self.deiconify()

    def init(self,args={}):
        self.text = StringVar()
        self.text.set('')
        self.text2 = StringVar()
        self.text2.set('')
        self.icone = 'logo_edf.gif'
        self.barre = 'non'
        if args == {} : return
        if args.has_key('text'):
            self.text.set(args['text'])
        if args.has_key('info'):
            self.text2.set(args['info'])
        if args.has_key('titre'):
            self.title(args['titre'])
        if args.has_key('code'):
            self.code = args['code']
        else:
            self.code = 'inconnu'
        if args.has_key('icone'):
            self.icone = args['icone']
        if self.code == 'ASTER' :
            self.icone = 'code_aster.gif'
        elif self.code == 'SATURNE':
            self.icone = 'code_saturne.gif'
        elif self.code == 'DESCARTES':
            self.icone = 'code_descartes.gif'

    def CreateWidgets(self):
        self.catIcon = images.get_image(self.icone)
        self.label = Label(self.frame, image=self.catIcon)
        self.label.pack(side=TOP)
        self.label = Label(self.frame, textvariable=self.text,font = fontes.standard_gras)
        self.label.pack(side=TOP,expand=1,fill='both')
        self.label2 = Label(self.frame, textvariable=self.text2,font = fontes.standard_italique)
        self.label2.pack(side=TOP,expand=1,fill='both')
        self.progress = Slider(self.frame,value=0,max=100,orientation='horizontal',
                               fillColor='#00008b',width=200,height=30,
                               background='white',labelColor='red')
        centerwindow(self)

    def update_barre(self,event=None):
        """ Permet de faire avancer la barre de progression """
        try:
            self.progress.value = self.progress.value+self.increment
            self.progress.update()
        except:
            pass

    def configure_barre(self):
        """ 
             Calcule l'incrément de progression de la barre en fonction
             du nombre d'opérations à effectuer afin que le compteur
             soit à 100% à la fin des opérations
        """
        self.increment = 100./self.ratio
        self.progress.update()

    def configure(self,**args):
        if args.has_key('text'):
            self.text.set(args['text'])
        if args.has_key('info'):
            self.text2.set(args['info'])
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
        self.destroy()
        if self.main:
           self.main.update()
           self.main.deiconify()
           centerwindow(self.main,parent='sans')

