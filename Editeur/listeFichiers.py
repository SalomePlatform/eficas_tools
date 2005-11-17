import string

class listeFichiers :

    def __init__(self,appli):
       self.appli=appli
       self.premiere=1
       self.nbfich=0
       self.rep=self.appli.CONFIGURATION.rep_user
       self.menuFichier=self.appli.menubar.menudict['Fichier']
       self.monFichier=self.rep+"/listefichiers"
       self.liste_Fichiers=[] 
       self.init_Fichier()
       self.traite_liste()

    def init_Fichier(self):
	index=0
        try :
	    f=open(self.monFichier)
	    while ( index < 5) :
	      ligne=f.readline()
	      if ligne != "" :
	         l=(ligne.split("\n"))[0]
	         self.liste_Fichiers.append(l)
	      index=index+1
	except :
	     pass
	try :
	    f.close()
	except :
	     pass

    def sauve_Fichier(self):
        try :
	    if len(self.liste_Fichiers) == 0 :
	      return
	    f=open(self.monFichier,'w')
	    index=0
	    while ( index <  len(self.liste_Fichiers)):
	      ligne=self.liste_Fichiers[index]+"\n"
	      f.write(ligne)
	      index=index+1
	except :
	     pass
	try :
	    f.close()
	except :
	     pass

    def traite_liste(self):
        index=0
	for  index in range(self.nbfich):
           self.menuFichier.delete(9)
	self.nbfich = 0
	index = 0
	while( index < len(self.liste_Fichiers)) :
	    self.ajout_item(index)
	    index=index+1
	   
    def ajout_item(self,index):
        if self.premiere and (len(self.liste_Fichiers)!=0):
	   self.premiere=0
	   self.menuFichier.add_separator()
	label=self.liste_Fichiers[index]
        self.menuFichier.insert_command(8,label=label,command= lambda self=self, l=label:self.coucou (l));
	self.nbfich=self.nbfich+1

    def coucou(self,label):
        self.appli.bureau.openJDC(file=label) 

    def aOuvert(self,file):
         if file not in self.liste_Fichiers :
	    if (len(self.liste_Fichiers) > 4) :
	       f=self.liste_Fichiers[0]
	       self.liste_Fichiers.remove(f)
	    self.liste_Fichiers.insert(len(self.liste_Fichiers),file)
	 else:
	    self.liste_Fichiers.remove(file)
	    self.liste_Fichiers.insert(len(self.liste_Fichiers),file)
	 self.traite_liste()
	 self.sauve_Fichier()
