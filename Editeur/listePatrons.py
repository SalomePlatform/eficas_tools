import os
import re
import Tkinter

# le dictionnaire sous menu est indexe parceque l'ordre des
# recherches est important

sous_menu={0:{"3D":"3D.comm"},1:{"poutre":"pou.comm"},2:{"salome":"salome.comm"},3:{"divers":"comm"}}

class listePatrons :

    def __init__(self,appli):
       self.appli=appli
       rep_ini=self.appli.CONFIGURATION.rep_ini
       if self.appli.code != "ASTER" :
          return
       self.rep_patrons=rep_ini+"/../Editeur/Patrons"
       self.liste={}
       self.traite_liste()
       self.ajout_menu()


    def traite_liste(self):
        for file in os.listdir(self.rep_patrons):
	    for i in range(len(sous_menu)):
	        clef=sous_menu[i].keys()[0]
		chaine=sous_menu[i][clef]
	        if re.search(chaine,file) :
		   if clef in self.liste.keys():
		      self.liste[clef].append(file)
		   else :
		      self.liste[clef]=[file]
		   break

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
