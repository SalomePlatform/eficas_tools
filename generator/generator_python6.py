# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
    Ce module contient le plugin generateur de fichier au format 
    python pour EFICAS.

"""
import traceback
import types,string,re

from Noyau import N_CR
from Noyau.N_utils import repr_float
from Accas import ETAPE,PROC_ETAPE,MACRO_ETAPE,ETAPE_NIVEAU,JDC,FORM_ETAPE
from Accas import MCSIMP,MCFACT,MCBLOC,MCList,EVAL
from Accas import GEOM,ASSD,MCNUPLET
from Accas import COMMENTAIRE,PARAMETRE, PARAMETRE_EVAL,COMMANDE_COMM
from Formatage import Formatage

import generator_python

def entryPoint():
   """
       Retourne les informations nécessaires pour le chargeur de plugins

       Ces informations sont retournées dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'python6',
        # La factory pour créer une instance du plugin
          'factory' : PythonGenerator,
          }


class PythonGenerator(generator_python.PythonGenerator):
   """
       Ce generateur parcourt un objet de type JDC et produit
       un fichier au format python6

       L'acquisition et le parcours sont réalisés par la méthode
       generator.gener(objet_jdc,format)

       L'écriture du fichier au format python6 par appel de la méthode
       generator.writefile(nom_fichier)

       Ses caractéristiques principales sont exposées dans des attributs 
       de classe :
         - extensions : qui donne une liste d'extensions de fichier préconisées

   """
   # Les extensions de fichier préconisées
   extensions=('.comm',)

   def generFORM_ETAPE(self,obj):
        """
            Méthode particulière pour les objets de type FORMULE
        """
        l=[]
        nom = obj.get_nom()
        if nom == '' : nom = 'sansnom'
        l.append(nom + ' = FORMULE(')
        for v in obj.mc_liste:
            text=self.generator(v)
    	    l.append(v.nom+'='+text)
        l.append(');')
        return l

   def gen_formule(self,obj):
      """
           Méthode particuliere aux objets de type FORMULE
      """
      try:
        if obj.sd == None:
          sdname=''
        else:
          sdname= self.generator(obj.sd)
      except:
        sdname='sansnom'
      l=[]
      label=sdname + ' = FORMULE('
      l.append(label)
      for v in obj.mc_liste:
        s=''
        s= v.nom+':'+sdname+'('+v.valeur+')'
        l.append(s)
      if len(l) == 1:
        l[0]=label+');'
      else :
        l.append(');')
      return l
