#@ AJOUT OpenturnsSolver Macro
# -*- coding: iso-8859-1 -*-
# RESPONSABLE

"""
Ce module contient la partie commune 
aux generateurs XML et Etude d Openturns
"""

__revision__ = "V1.0"

import os
import sys

path=os.getcwd()
pathDef=path+"DefautOpenturns"

sys.path.append(pathDef)


#=============================================
# La classe generale
#=============================================

class Generateur :

  '''
  Classe generale du generateur
  DictMCVal : dictionnaire des mots-cles
  ListeVariables : chaque variable est decrite par un dictionnaire ; cette liste les regroupe
  DictLois : dictionnaires des lois
  '''
  def __init__ (self, DictMCVal, ListeVariables, DictLois ) :
  #---------------------------------------------------------#
    self.ListeVariables = ListeVariables
    self.ListeVariablesIn = []
    self.DictLois = DictLois
    self.DictMCVal = DictMCVal
    self.DictTypeVar = {}
    self.nbVarIn = 0
    self.creeInfoVar()
    #
    # On charge eventuellement le Solver par defaut
    # et les valeurs par defaut du Solver (dans l init)
    #
    try :
    #if 1 :
        Solver = self.DictMCVal["PhysicalSolver"]
        import_name = "Defaut"+Solver
	self.module = __import__( import_name, globals(), locals() )
	monDefaut = self.module.Defaut( self )
    #else :
    except:
        self.module = None


  def getSTDGenerateur(self) :
  #--------------------------#
    try :
	gener = self.module.__dict__["MonSTDGenerateur"]
	monSTDGenerateur=gener( self.DictMCVal, self.ListeVariablesIn, self.DictLois )
    except :
        from OpenturnsSTD import STDGenerateur
        monSTDGenerateur = STDGenerateur( self.DictMCVal, self.ListeVariablesIn, self.DictLois )
    return monSTDGenerateur
      
  def getXMLGenerateur(self) :
  #--------------------------#
    try :
	gener = self.module.__dict__["MonXMLGenerateur"]
	monXMLGenerateur=gener( self.DictMCVal, self.ListeVariables, self.DictLois )
    except :
        from OpenturnsXML import XMLGenerateur
        monXMLGenerateur = XMLGenerateur( self.DictMCVal, self.ListeVariables, self.DictLois )
    return monXMLGenerateur
      
  def creeInfoVar (self) :
  #----------------------#
    """
    On repere les variables in/out et on les numerote.
    """
    num = 0
    liste = []
    for DictVariable in self.ListeVariables :
      if not DictVariable.has_key("Type") : DictVariable["Type"] = "in"
      self.DictTypeVar[num] = DictVariable["Type"]
      if DictVariable["Type"] == "in" : 
         self.nbVarIn = self.nbVarIn + 1
         self.ListeVariablesIn.append( DictVariable )
      liste.append( DictVariable )
      num = num + 1
    self.ListeVariables = liste


  def ajouteDictMCVal(self, dicoPlus) :
  #-----------------------------------#
  # Appele par le classe Defaut du python specifique au code (exple DefautASTER.py)
  # enrichit self.DictMCVal avec les valeurs donnees dans dicoPlus
  # si elles ne sont pas deja dans le dictionnaire

    for clef in dicoPlus.keys():
        if not self.DictMCVal.has_key(clef) :
	   self.DictMCVal[clef] = dicoPlus[clef]

  def ajouteInfoVariables (self, dicoVariablesIn, dicoVariablesOut) :
  #-----------------------------------------------------------------#
  # Appele par le classe Defaut du python specifique au code (exple DefautASTER.py)
  # met a jour les dictionnaires qui decrivent les variables (regexp par exemple)
    liste=[]
    num = 0
    for dictVariable in self.ListeVariables:
         if self.DictTypeVar[num] == "in" :
	    dico = dicoVariablesIn
	 else :
	    dico = dicoVariablesOut
	 for nouvelleVariable in dico.keys() :
	    if not dictVariable.has_key(nouvelleVariable):
	       dictVariable[nouvelleVariable] = dico[nouvelleVariable]
	 liste.append( dictVariable )
	 num = num + 1
