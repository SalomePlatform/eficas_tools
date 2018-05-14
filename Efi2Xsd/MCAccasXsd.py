#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
#import raw.efficas as efficas
import types

sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))



class X_MCSIMP:
# -------------
      
   def buildObjPyxb(self) :
      if not self.cata.modeleMetier : return
      #print ('X_MCSIMP buildObjPyxb', self.nom, self)
      self.monNomDeClasseModeleMetier='T_'+self.nom
      self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomDeClasseModeleMetier)
      if self.val != None : self.objPyxb=self.maClasseModeleMetier(self.val)
      else                : self.objPyxb=self.maClasseModeleMetier()
      #print ('fin X_MCSIMP', self.objPyxb, self.nom,self)


   def setValeurObjPyxb(self,newVal):
       if not self.cata.modeleMetier : return
       print ('setValeurObjPyxb')
       if newVal != None : nvlObj=self.maClasseModeleMetier(newVal)
       else              : nvlObj=self.maClasseModeleMetier()
       self.val=newVal
       self.objPyxb=nvlObj
       setattr(self.parent.objPyxb, self.nom, nvlObj)
      

class X_MCCOMPO:
# --------------
# 
   def buildObjPyxb(self,mc_list) :
      if not self.cata.modeleMetier : return
      print ('X_MCCOMPO buildObjPyxb', self.nom, self)
      self.monNomDeClasseModeleMetier='T_'+self.nom
      self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomDeClasseModeleMetier)
      listArg=[]
      for objAccas in mc_list :
         from Accas.A_MCLIST import MCList
         if isinstance(objAccas,MCList) :
            for mcfact in objAccas : listArg.append(mcfact.objPyxb)
         else : listArg.append(objAccas.objPyxb)
      print (listArg)
      self.objPyxb=self.maClasseModeleMetier(*listArg)

class X_MCFACT :
# --------------
#   Pour un MCFACT : 
#   le buildObjPyxb  sera  pris en charge par X_MCLIST 
#   on ne fait rien
 
   def buildObjPyxb(self,mc_list):
      #print ('X_MCFACT buildObjPyxb debut et fin', self.nom, self)
      pass

class X_MCLIST:
# --------------
 
  
   def buildObjPyxb(self,factList):
      if not self.cata.modeleMetier : return
      #print ('X_MCLIST buildObjPyxb', self.nom, self)

      self.monNomDeClasseModeleMetier='T_'+self.nom
      self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomDeClasseModeleMetier)
      for objAccas in factList :
          listArg=[]
          for objAccasFils in objAccas.mc_liste :
              listArg.append(objAccasFils.objPyxb)
          objAccas.objPyxb=self.maClasseModeleMetier(*listArg)
          #print (objAccas , 'ds MCLIST a pour obj pyxb', objAccas.objPyxb)

class X_JDC:
# ----------
 
   def  __init__(self):
      #print ('X_JDC buildObjPyxb',  self)
      if not self.cata.modeleMetier : return
      self.monNomDeClasseModeleMetier=self.code
      self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomDeClasseModeleMetier)
      self.objPyxb=self.maClasseModeleMetier()
      #print ('fin X_JDC buildObjPyxb', self.objPyxb, self)

   def enregistreEtapePyxb(self,etape):
     # OK seulement si sequence (choice ? ...)
      print ('ds enregistreEtapePyxb', etape.nom)
      if not self.cata.modeleMetier : return
      self.objPyxb.append(etape.objPyxb)
      #self.toXml()

   def toXml(self):
      if not self.cata.modeleMetier : return
      print(self.objPyxb.toDOM().toprettyxml())
      print(self.objPyxb.toxml())
        
   

if __name__ == "__main__":
   print ('a faire')
