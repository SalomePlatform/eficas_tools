#!/usr/bin/env python
# -*- coding: utf-8 -*-
import types
class CataMAP:

   def __init__(self,dict1,dict2):
      self.cata=""
      self.texte=self.readfile("cataDebut.py")
      self.dictParam=dict1
      self.dictData=dict2
      self.traiteDico(self.dictParam)


   def readfile(self,fn):
      try:
         texte=open(fn).read()
      except:
         print "Impossible ouvrir fichier %s" % filename
         return texte


   def traiteDico(self,dict):
       for clef in dict.keys() :
           d=dict[clef]
           texteSIMP="=SIMP(typ=%s,statut=%s)\n,"%d
           texteSIMp=clef+texteSIMP
           print texteSIMP

   def execute(self):
      contexte = globals()
      try :
          exec self.texte in contexte
      except  :
          import traceback
          traceback.print_exc()


if __name__ == "__main__" :
     dicoParam={"p1":{"typ":"TXM","statut":"o"}}
     dicoVal={"val1":{"typ":"R","statut":"o"}}
     monCata=CataMAP(dicoParam,dicoVal)
     print monCata.texte
