import os
import re
import Tkinter


from Editeur import listePatrons

class listePatronsTK(listePatrons.listePatrons) :

    def __init__(self,appli):
       self.appli=appli
       listePatrons.listePatrons.__init__(self)
       self.ajout_menu()

    def ajout_menu(self):
        menuFichier=self.appli.menubar.menubar
        menu_cascade=Tkinter.Menu(menuFichier,tearoff=0)
        menuFichier.add_cascade(label="Patrons",menu=menu_cascade)
        for ss_menu in self.liste.keys():
           ssmenu=Tkinter.Menu(menu_cascade,tearoff=0)
           menu_cascade.add_cascade(label=ss_menu,menu=ssmenu)
           for fichier in self.liste[ss_menu]:
               ssmenu.add_command(label=fichier,command= lambda self=self, l=fichier:self.ouvre(l));

    def ouvre(self,label):
        fichier=self.rep_patrons+"/"+label
        self.appli.bureau.openJDC(file=fichier,enregistre="non") 
