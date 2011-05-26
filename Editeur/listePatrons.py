import os
import re

sous_menus={
	    "OPENTURNS_STUDY" : {0:{"Anne":"Std.comm"}},
            "OPENTURNS_WRAPPER" : {0:{"Anne":"wrapper_exemple.comm"}},
           }

class listePatrons :

    def __init__(self,code = "ASTER"):
       repIni=os.path.dirname(os.path.abspath(__file__))
       self.rep_patrons=repIni+"/Patrons/"+code
       self.sous_menu={}
       if code in sous_menus.keys()  :
          self.sous_menu=sous_menus[code]
       self.code=code
       self.liste={}
       self.traite_liste()

    def traite_liste(self):
        if not (self.code in sous_menus.keys()) : return
        if not (os.path.exists(self.rep_patrons)) : return
        for file in os.listdir(self.rep_patrons):
            for i in range(len(self.sous_menu)):
                clef=self.sous_menu[i].keys()[0]
                chaine=self.sous_menu[i][clef]
                if re.search(chaine,file) :
                   if clef in self.liste.keys():
                      self.liste[clef].append(file)
                   else :
                      self.liste[clef]=[file]
                   break
