# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
"""
    Ce module contient le plugin generateur de fichier au format 
    python pour EFICAS.
    PN

"""
import traceback
import types,string,re
import math

from Noyau import N_CR
from Noyau.N_utils import repr_float
import Accas
import Extensions
from Extensions.parametre import ITEM_PARAMETRE
from Formatage import Formatage
from generator_python import PythonGenerator
#from Editeur.widgets import showerror

def entryPoint():
   """
       Retourne les informations nécessaires pour le chargeur de plugins

       Ces informations sont retournées dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'vers3DSalome',
        # La factory pour créer une instance du plugin
          'factory' : vers3DSalomeGenerator,
          }


class vers3DSalomeGenerator(PythonGenerator):
   """
       Ce generateur parcourt un objet AFFE-CARA_ELEM
       et produit un fichier au format texte contenant
       les instructions idl pour PAL 
   """

   def __init__(self,cr=None):
      self.list_commandes=[];
      self.jdc=None
      self.node=None
      self.clefs=None
      self.liste_motetat = ("AFFE_CARA_ELEM", "ORIG_AXE", "AXE" , 
                            "BARRE", "CABLE", "CARA", "COQUE", "EPAIS", 
                            "EXCENTREMENT", "GROUP_MA", "ORIENTATION", 
                            "POUTRE", "SECTION", "VALE", "VARI_SECT",
                            "GRILLE", "ANGL_REP", "VECTEUR",
                             "b_constant", "b_homothetique", 
                            "b_rectangle", "b_affine", "b_cercle", "b_generale" )
      self.dict_deb_com={"POUTRE":"VisuPoutre", "CABLE" : "VisuCable",
                         "COQUE" : "VisuCoque", "GRILLE" : "VisuGrille",
                         "ORIENTATION" : "Orientation", "BARRE" : "VisuBarre"}

      self.dict_suite_com={"RECTANGLE":"Rectangle","GENERALE":"Generale",
                           "CERCLE":"Cercle"}

      self.dict_traduit={"VARI_SECT":"extrusion","EXCENTREMENT":"Excentre","EPAIS":"Epais","VECTEUR":"Vecteur"}

      self.init_ligne() 

   def init_jdc(self,jdc) :
      self.jdc=jdc

   def init_ligne (self) :
      self.boolGpMa = 0
      self.commande = ""
      self.dict_attributs = {} 

   def gener(self,node,config=None):
      """
      """
      self.node=node
      self.list_commandes=[];
      self.generator(self.node.object)
      #print self.list_commandes
      return self.list_commandes

   def generator(self,obj):
      if (obj.nom in self.liste_motetat) and (self.calcule_ouinon(obj)):
         PythonGenerator.generator(self,obj)
      """
        f1=PythonGenerator.generator(self,obj)
      else :
        return ""
      """

   def calcule_ouinon(self,obj):
      ouinon=1
      for l in obj.get_genealogie() :
          if not l in self.liste_motetat :
             ouinon=0
             break
      return ouinon

       
   def generETAPE(self,obj):
      """
      """
      if obj.isvalid() == 0 :
         #showerror("Element non valide","Salome ne sait pas traiter les elements non valides")
         return
      for v in obj.mc_liste:
         liste=self.generator(v)

   def generMACRO_ETAPE(self,obj):
      """
      """
      if obj.isvalid() == 0 :
         #showerror("Element non valide","Salome ne sait pas traiter les elements non valides")
         return
      for v in obj.mc_liste:
         liste=self.generator(v)


   def generMCSIMP(self,obj) :
      """
      """
      if obj.nom in dir(self) :
         suite = self.__class__.__dict__[obj.nom](self,obj)
      else :
         clef=self.dict_traduit[obj.nom]
         # Traitement des parametres
         try :
             self.dict_attributs[clef]=obj.val.eval()
         except :
             self.dict_attributs[clef]=obj.val


   def generMCFACT(self,obj):
      """
          Convertit un objet MCFACT en une liste de chaines de caractères à la
          syntaxe python
      """
      self.init_ligne()
      self.commande=self.dict_deb_com[obj.nom]
      for v in obj.mc_liste:
         self.generator(v)
      if self.boolGpMa == 1:
         self.list_commandes.append((self.commande,self.dict_attributs)) 
      else :
         #showerror("Elements ne portant pas sur un Groupe de Maille","Salome ne sait pas montrer ce type d' element")
         print ("Elements ne portant pas sur un Groupe de Maille","Salome ne sait pas montrer ce type d' element")
         pass

   def generMCList(self,obj):
      """
      """
      for mcfact in obj.data:
          self.generator(mcfact)

   def generMCBLOC(self,obj):
      """
      """
      for v in obj.mc_liste:
         self.generator(v)

   def GROUP_MA(self,obj):
      self.boolGpMa = 1
      self.dict_attributs["Group_Maille"]=obj.val

   def SECTION(self,obj):
      assert (self.commande != "" )
      if self.commande == "VisuCable" :
         self.dict_attributs["R"]= math.sqrt(obj.val/math.pi).eval()
      elif (self.commande !="VisuGrille")  :
         self.commande=self.commande+self.dict_suite_com[obj.valeur]

   def CARA(self,obj) :
       self.clefs=obj.val
       if type(self.clefs) == types.StringType :
          self.clefs=(obj.val,)

   def VALE(self,obj) :
       atraiter=obj.val
       if len(self.clefs) > 1 :
           assert (len(atraiter) == len(self.clefs))
       else :
           atraiter=(atraiter,)
       for k in range(len(atraiter)) :
           clef=self.clefs[k]
           val =atraiter[k] 
           if isinstance(val, (types.TupleType, types.ListType)) and len(val) == 1:
               val = val[0]
           if isinstance (val, Extensions.parametre.PARAMETRE):
              val=val.valeur
              print val.__class__
              context={}
              if type(val) == type("aaa") :
                 for p in self.jdc.params:
                     context[p.nom]=eval(p.val,self.jdc.const_context, context)
                     print context[p.nom]
                 res=eval(val,self.jdc.const_context, context)
                 val=res
           self.dict_attributs[clef]=val

   def ANGL_REP(self,obj) :
      assert (len(obj.val) == 2)
      alpha,beta=obj.val
      self.dict_attributs["angleAlpha"]=alpha
      self.dict_attributs["angleBeta"]=beta

   def ORIG_AXE(self,obj) :
      assert (len(obj.val) == 3)
      alpha,beta,gamma=obj.val
      self.dict_attributs["origAxeX"]=alpha
      self.dict_attributs["origAxeY"]=beta
      self.dict_attributs["origAxeZ"]=gamma

   def AXE(self,obj) :
      assert (len(obj.val) == 3)
      alpha,beta,gamma=obj.val
      self.dict_attributs["axeX"]=alpha
      self.dict_attributs["axeY"]=beta
      self.dict_attributs["axeZ"]=gamma
