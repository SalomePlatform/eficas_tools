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
   SEP pour EFICAS.

"""
import traceback
import types,string,re,os

from generator_python import PythonGenerator

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins

      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'SEP',
        # La factory pour creer une instance du plugin
          'factory' : SEPGenerator,
          }


class SEPGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 
      un texte au format py 

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

   def gener(self,obj,format='brut',config=None):
      self.initDico()
      # Cette instruction génère le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)
      # Cette instruction génère le contenu du fichier de paramètres python
      self.genereSEP()
      return self.text

   def getTubePy(self) :
      return self.texteTubePy

   def genereSEP(self) :
      '''
      Prépare le contenu du fichier de paramètres python. Le contenu
      peut ensuite être obtenu au moyen de la fonction getTubePy().
      '''
      #self.__genereSEP_withVariables()
      self.__genereSEP_withDico()

   def __genereSEP_withVariables(self) :
      '''
      Les paramètres sont transcrits sous forme de variables nom=valeur.
      '''
      self.texteTubePy="# Parametres generes par Eficas \n"
      for MC in self.dictMCVal.keys():
	 ligne = MC +"="+ repr(self.dictMCVal[MC])+'\n'
         self.texteTubePy=self.texteTubePy+ligne

      print self.texteTubePy

      # __GBO__: Tester self.tube pour aiguiller en fonction du cas (au besoin)
      fichier=os.path.join(os.path.dirname(__file__),"tube.py")
      f=open(fichier,'r')
      for ligne in f.readlines():
         self.texteTubePy=self.texteTubePy+ligne
      f.close

   def __genereSEP_withDico(self) :
      """
      Les paramètres sont transcrits sous la forme d'un dictionnaire nom=valeur.
      """
      from Sep import properties
      self.texteTubePy="# -*- coding: utf-8 -*-\n"
      self.texteTubePy+="# ======================================================================================\n"
      self.texteTubePy+="# FICHIER GENERE PAR EFICAS - OUTIL MÉTIER SOUS-EPAISSEUR - "
      self.texteTubePy+="VERSION "+str(properties.version)+" du "+str(properties.date)+"\n"
      self.texteTubePy+="# ======================================================================================\n"
      self.texteTubePy+="\n"
      self.texteTubePy+="# Parametres Utilisateur Eficas \n"
      self.texteTubePy+="parameters={}\n"
      
      for MC in self.dictMCVal.keys():
	 ligne = "parameters['"+MC+"']="+ repr(self.dictMCVal[MC])+'\n'
         self.texteTubePy=self.texteTubePy+ligne

      # On ajoute des paramètres de configuration pour contrôle de
      # cohérence avec la procédure outil métier
      self.texteTubePy+="# Parametres de Configuration Eficas \n"
      ligne = "parameters['OMVERSION']="+str(properties.version)+"\n"
      self.texteTubePy+=ligne

      # __GBO__: Tester self.tube pour aiguiller en fonction du cas (au besoin)
      self.texteTubePy+="\n"
      self.texteTubePy+="# Exécution de la procédure outil métier \n"
      self.texteTubePy+="import os,sys\n"
      self.texteTubePy+="sys.path.insert(0,os.environ['OM_ROOT_DIR'])\n"
      self.texteTubePy+="import om_data\n"
      self.texteTubePy+="om_data.setParameters(parameters)\n"
      self.texteTubePy+="def run():\n"
      self.texteTubePy+="    import om_smeca\n"
      self.texteTubePy+="\n"
      self.texteTubePy+='if __name__ == "__main__":\n'
      self.texteTubePy+="    run()\n"

      # For debug only
      print self.texteTubePy


   def initDico(self) :
      self.tube=0
      self.coude=0
      self.dictMCVal={}
      self.texteTubePy=""

   # __GBO__: surcharge de PythonGenerator:
   # voir example generator_cuve2dg.py (genea)
   def generMCSIMP(self,obj) :
      """
      Convertit un objet MCSIMP en texte python
      Remplit le dictionnaire des MCSIMP si nous ne sommes ni dans une loi, ni dans une variable
      """
      clef=""
      for i in obj.get_genealogie() :
         clef=clef+"__"+i
      #self.dictMCVal[obj.nom]=obj.valeur
      self.dictMCVal[clef]=obj.valeur

      s=PythonGenerator.generMCSIMP(self,obj)
      return s
  
   # __GBO__: surcharge de PythonGenerator
   def generMACRO_ETAPE(self,obj):
      print obj.nom
      if obj.nom == "S_EP_INTERNE" :
	 self.tube=1
      if obj.nom == "M_COUDE" :
	 self.coude=1
      s=PythonGenerator.generMACRO_ETAPE(self,obj)
      return s

