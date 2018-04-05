#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
#import raw.efficas as efficas
import types

sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))


import  Atmo.raw.atmo_test1 as modeleMetier 

class X_MCSIMP:
# -------------
      
   def buildObjPyxb(self) :
      #print ('X_MCSIMP buildObjPyxb', self.nom, self)
      self.monNomDeClasseModeleMetier='T_'+self.nom
      self.maClasseModeleMetier=getattr(modeleMetier,self.monNomDeClasseModeleMetier)
      if self.val != None : self.objPyxb=self.maClasseModeleMetier(self.val)
      else                 : self.objPyxb=self.maClasseModeleMetier()
      #print ('fin X_MCSIMP', self.objPyxb, self.nom,self)


   def setValeur(self,val):
       print  ('a faire PNPNPNPN')
      

class X_MCCOMPO:
# --------------
# 
   def buildObjPyxb(self,mc_list) :
      print ('X_MCCOMPO buildObjPyxb', self.nom, self)
      self.monNomDeClasseModeleMetier='T_'+self.nom
      self.maClasseModeleMetier=getattr(modeleMetier,self.monNomDeClasseModeleMetier)
      listArg=[]
      for objAccas in mc_list :
         listArg.append(objAccas.objPyxb)
      self.objPyxb=self.maClasseModeleMetier(*listArg)
      print ('fin MCCOMPO', self.objPyxb, self.nom,self,self.objPyxb.content())

class X_MCFACT:
# --------------
#   Pour un MCFACT : 
#   le buildObjPyxb  sera  pris en charge par X_MCLIST 
#   on ne fait rien
 
   def buildObjPyxb(self,mc_list):
      pass

class X_MCLIST:
# --------------
 
   def buildObjPyxb(self,factList):
      #print ('X_MCLIST buildObjPyxb', self.nom, self)
      self.monNomDeClasseModeleMetier='T_'+self.nom
      self.maClasseModeleMetier=getattr(modeleMetier,self.monNomDeClasseModeleMetier)
      listArg=[]
      for objAccas in factList :
          #print objAccas.nom
          for objAccasFils in objAccas.mc_liste :
              #print (objAccasFils)
              #print (objAccasFils.nom)
              #print (objAccasFils.objPyxb)
              listArg.append(objAccasFils.objPyxb)
      #         print (objAccasFils.objPyxb)
      self.objPyxb=self.maClasseModeleMetier(*listArg)
      #print (self.objPyxb.content())
      #print ('fin MCLIST', self.objPyxb, self.nom,self)

class X_JDC:
# ----------
 
   def  __init__(self):
      print ('--------- init du X_JDC')
      self.monNomDeClasseModeleMetier=self.code
      self.maClasseModeleMetier=getattr(modeleMetier,self.monNomDeClasseModeleMetier)
      self.objPyxb=self.maClasseModeleMetier()

   def ajoutEtapeAPyxb(self,etape):
     # OK seulement si sequence (choice ? ...)
       print ('----------------------------------------------------------------------------------------------je suis la')
       self.objPyxb.append(etape.objPyxb)
       self.toxml()

   def toxml(self):
       print(self.objPyxb.toDOM().toprettyxml())
       print(self.objPyxb.toxml())
        
   

if __name__ == "__main__":
   print ('a faire')
