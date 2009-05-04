# -*- coding: utf-8 -*-
import logging
import string
from parseur import FactNode
debug=0


#--------------------
class ensembleRegles:
#--------------------

   def __init__(self,liste_regles):
      self.liste=[]
      for item in liste_regles :
         args,clefRegle=item
         r=regle(clefRegle,args)
         self.liste.append(r)

   def verif(self,commande) :
       bool=1
       for regle in self.liste :
         result=regle.verif(commande)
         bool=bool*result
       return bool
         
#--------------------------------
class pasDeRegle(ensembleRegles):
#--------------------------------
   def __init__(self) :
     pass

   def verif (self,commande) :
     return 1
 

#------------
class regle :
#------------

   def __init__(self,clef_regle,args):
      self.fonction=dictionnaire_regle[clef_regle]
      self.list_args=args
      self.bool=0

   def verif(self,commande):
       f=self.fonction(self.list_args)
       return f.verif(commande)
      
#---------------------
class existeMCFParmi :
#---------------------
   def __init__(self,list_arg):
      self.listeMCF=list_arg;

   def verif(self,commande):
      bool=0
      for c in commande.childNodes :
         if c.name in self.listeMCF : 
            bool=1
            break
      return bool
      
#----------------------
class existeMCsousMCF :
#----------------------
   def __init__(self,list_arg):
      self.liste=list_arg;
      self.MCF=self.liste[0]
      self.MC=self.liste[1]

   def verif(self,commande):
      bool=0
      for mcf in commande.childNodes :
         if mcf.name != self.MCF : continue 
         l=mcf.childNodes[:]
         l.reverse()
         for ll in l:
            for mc in ll.childNodes:
               if mc.name != self.MC : continue
               bool=1
      return bool
      
#-----------------------------------------
class nexistepasMCsousMCF(existeMCsousMCF):
#-----------------------------------------
   def __init__(self,list_arg):
       existeMCsousMCF.__init__(self,list_arg)
      

   def verif(self,commande):
       bool=existeMCsousMCF.verif(self,commande)
       if bool : return 0
       return 1

#-------------
class existe :
#--------------
   def __init__(self,list_arg):
      self.genea=list_arg

   def cherche_mot(self,niveau,commande):
      if commande == None            : return 0
      if niveau   == len(self.genea) : return 1
      texte=self.genea[niveau]
      for c in commande.childNodes :
          if c.name == texte : 
             niveau = niveau+1
             return self.cherche_mot(niveau,c)
      return None

   def verif(self,commande):
      bool=self.cherche_mot(0,commande)
      if bool == None : bool = 0
      return bool

#-------------
class nexistepas :
#--------------
   def __init__(self,list_arg):
      self.genea=list_arg

   def cherche_mot(self,niveau,commande):
      if commande == None            : return 0
      if niveau   == len(self.genea) : return 1
      texte=self.genea[niveau]
      for c in commande.childNodes :
          if c.name == texte : 
             niveau = niveau+1
             return self.cherche_mot(niveau,c)
      return None

   def verif(self,commande):
      bool=self.cherche_mot(0,commande)
      if bool : return 0
      return 1

#-------------------------------
class MCsousMCFaPourValeur :
#------------------------------
   def __init__(self,list_arg):
      assert (len(list_arg)==4)
      self.genea=list_arg[0:-2]
      self.MCF=list_arg[0]
      self.MC=list_arg[1]
      self.Val=list_arg[2]
      self.Jdc=list_arg[3]

   def verif(self,commande):
      bool=0
      for mcf in commande.childNodes :
         if mcf.name != self.MCF : continue 
         l=mcf.childNodes[:]
         l.reverse()
         for ll in l:
            for mc in ll.childNodes:
               if mc.name != self.MC : continue
               TexteMC=mc.getText(self.Jdc)
               if (TexteMC.find(self.Val) < 0 ): continue
               bool=1
      return bool

#-------------------------------
class MCaPourValeur :
#------------------------------
   def __init__(self,list_arg):
      assert (len(list_arg)==3)
      self.MC=list_arg[0]
      self.Val=list_arg[1]
      self.Jdc=list_arg[2]

   def verif(self,commande):
      bool=0
      for mc in commande.childNodes :
         if mc.name != self.MC : continue 
         TexteMC=mc.getText(self.Jdc)
         if (TexteMC.find(self.Val) < 0 ): continue
         bool=1
      return bool

dictionnaire_regle={"existe":existe,"nexistepas":nexistepas,"existeMCFParmi":existeMCFParmi,"existeMCsousMCF":existeMCsousMCF,"nexistepasMCsousMCF":nexistepasMCsousMCF,"MCsousMCFaPourValeur":MCsousMCFaPourValeur,"MCaPourValeur":MCaPourValeur}
SansRegle=pasDeRegle()
