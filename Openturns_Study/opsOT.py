# -*- coding: iso-8859-1 -*-

def INCLUDE(self,FileName,**args):
   """ 
       Fonction sd_prod pour la macro INCLUDE
   """
   if hasattr(self,'change_fichier'):
       delattr(self,'change_fichier')
       delattr(self,'fichier_ini')

   self.make_include2(fichier=FileName)

def INCLUDE_context(self,d):
   """ 
       Fonction op_init pour macro INCLUDE
   """
   for k,v in self.g_context.items():
      d[k]=v


