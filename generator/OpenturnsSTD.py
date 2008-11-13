#@ AJOUT OpenturnsSolver Macro
# -*- coding: iso-8859-1 -*-
# RESPONSABLE

"""
Ce module contient le generateur Etude pour Openturns
"""

__revision__ = "V1.0"

import os



#=============================================
#  La classe de creation du fichier STD
#=============================================

class STDGenerateur :

  '''
  Generation du fichier pyhton
  '''
  def __init__ (self, DictMCVal, ListeVariables, DictLois ) :
  #---------------------------------------------------------#

    self.NomAlgo = "myAlgo"
    self.DictMCVal = DictMCVal
    self.ListeVariables = ListeVariables
    self.DictLois = DictLois

    self.ListeOrdreMCReliability = (
      "MaximumIterationsNumber",
      "MaximumAbsoluteError",
      "RelativeAbsoluteError",
      "MaximumConstraintError",
      "MaximumResidualError",
      )
    self.ListeOrdreMCDirectionalSampling = (
      "RootStrategy",
      "SamplingStrategy",
      )
    self.ListeOrdreMCParametresAlgo = (
      "BlockSize",
      "MaximumCoefficientOfVariation",
      ) 
    self.ListeOrdreImportanceSampling = (
      "ImportanceSampling_BlockSize",
      "ImportanceSampling_MaximumCoefficientOfVariation",
      "ImportanceSampling_MaximumOuterSampling",
      ) 

    # Ce dictionnaire contient la liste de tous les parametres possibles pour chaque loi
    # Les parametres qui n'apparaissent pas ne pourront pas etre substitues dans le fichier
    # produit (etude python), et donc n'apparaitront pas.
    self.listeParamLoi = {
      "Beta"            : ["Mu", "Sigma", "T", "R", "A", "B" ],
      "Exponential"     : ["Lambda", "Gamma" ],
      "Gamma"           : ["K", "Mu", "Sigma", "Lambda", "Gamma" ],
      #"Geometric"       : ["P", ],
      "Gumbel"          : ["Alpha","Beta","Mu","Sigma" ],
      #"Histogram"       : ["Sup", "Values" ],
      "LogNormal"       : ["MuLog", "SigmaLog", "Mu", "Sigma", "SigmaOverMu", "Gamma", ],
      "Logistic"        : [ "Alpha", "Beta" ],
      #"MultiNomial"     : [ "N", "Values" ],
      "Normal"          : ["Mu", "Sigma" ],
      "Poisson"         : [ "Lambda", ],
      "Student"         : [ "Mu", "Nu" ],
      "Triangular"      : [ "A", "M", "B" ],
      "TruncatedNormal" : [ "MuN", "SigmaN", "A", "B" ],
      "Uniform"         : [ "A", "B" ],
      #"UserDefined"     : [ "Values", ],
      "Weibull"         : [ "Alpha", "Beta", "Mu", "Sigma", "Gamma" ],
      }

    # Ce dictionnaire contient, pour chaque loi qui possede plusieurs parametrages possibles,
    # la correspondance entre le parametrage et son "numero" pour Open TURNS.
    self.listeParamLoiSettings = {
      "Beta"      : { "RT"         : "0", "MuSigma" : "1" }, \
      "Gamma"     : { "KLambda"    : "0", "MuSigma" : "1" }, \
      "Gumbel"    : { "AlphaBeta"  : "0", "MuSigma" : "1" }, \
      "LogNormal" : { "MuSigmaLog" : "0", "MuSigma" : "1", "MuSigmaOverMu" : "2" }, \
      "Weibull"   : { "AlphaBeta"  : "0", "MuSigma" : "1" }, \
      }

		 

  def CreeSTD (self) :
  #------------------
    '''
    Pilotage de la creation du fichier python
    '''
    self.texte  = self.CreeEntete() 
    self.texte += self.CreeRandomGenerator() 
    self.texte += self.CreeFunction() 
    self.texte += self.CreeLois()
    self.texte += self.CreeCopula() 
    self.texte += self.CreeDistribution() 
    self.texte += self.CreeRandomVector()
    self.texte += self.CreeAnalyse()
    self.texte += self.CreeResu()
    self.texte += self.CreeTexteFin()
    return self.texte

#			______________________________________
#
#  Methodes liees a la creation de la partie Analayse
#  Si le mot clef Analyse existe la methode portant le meme nom va etre appele
#  Exple : si self.DictMCVal["Analysis"]=="Reliability" on appelle la methode Reliability(self)
#
  def CreeAnalyse (self) :
  #----------------------
  # Appelee  par CreeSTD
    texte=""
    if self.DictMCVal.has_key("Analysis"):
       texte += apply( STDGenerateur.__dict__[self.DictMCVal["Analysis"]], (self,) )
    return texte

  def  Reliability (self) :
  #------------------------
  # Appelee eventuellement par CreeAnalyse
    texte  = self.CreeEvent()
    texte += "\n# La methode\n\n"
    if not self.DictMCVal.has_key("Method"):
       print 'Attention Mot Clef "Method" non renseigne'
       return texte

    texte += "   myMethod = "+ self.DictMCVal["Method"] + "()\n"
    texte += "   myMethod.setSpecificParameters( " + self.DictMCVal["Method"] + "SpecificParameters() )\n"

    for MC in self.ListeOrdreMCReliability :
      if self.DictMCVal.has_key(MC) and self.DictMCVal[MC] != None :
          texte += "   myMethod.set"+ MC +"( " + str(self.DictMCVal[MC]) + " )\n\n "

    texte  += "\n# L'algorithme\n\n"
    if not self.DictMCVal.has_key("Algorithm"):
       print 'Attention Mot Clef "Algorithm" non renseigne'
       return texte
    texte += "   " + self.NomAlgo + " = " + str (self.DictMCVal["Algorithm"]) 
    texte += "( NearestPointAlgorithm(myMethod), myEvent, myPhysicalStartingPoint )\n"
    texte += "   " + self.NomAlgo + ".run()\n "
   
    if self.DictMCVal.has_key("ImportanceSampling") and self.DictMCVal["ImportanceSampling"]=="yes" :
       texte += self.ImportanceSampling() 
    return texte

  def  Simulation (self) :
  #------------------------
  # Appelee eventuellement par CreeAnalyse
    texte  = self.CreeEvent()
    texte += "\n# L'algorithme\n\n"
    if not self.DictMCVal.has_key("Algorithm"):
       print 'Attention Mot Clef "Algorithm" non renseigne'
       return texte
    texte += "   " + self.NomAlgo + " = " + str (self.DictMCVal["Algorithm"]) 
    texte += "( myEvent )\n"
    if self.DictMCVal["Algorithm"] == "DirectionalSampling" : 
       texte += self.DirectionalSampling()
    texte += self.ParametresAlgo()
    texte += "   " + self.NomAlgo + ".run() "
    return texte


  def DirectionalSampling (self) :
  #-------------------------------
  # Appelee eventuellement par Simulation
    texte = ""
    for MC in self.ListeOrdreMCDirectionalSampling :
       if self.DictMCVal.has_key(MC) and self.DictMCVal[MC] != None :
          texte += apply(STDGenerateur.__dict__[self.DictMCVal[MC]], (self,))
    return texte

  def RootStrategy(self):
  #----------------------
  # Appelee eventuellement par DirectionalSampling
    texte = "   myRoot = " + self.DictMCVal["RootStrategy"] + "()\n"
    if self.DictMCVal.has_key("Solver") and (self.DictMCVal["Solver"] != None) :
       texte += "   mySolver = " + self.DictMCVal["Solver"] + "() \n"
       texte += "   myRoot.setSolver( Solver( mySolver ) ) \n"
    texte += "   " + self.NomAlgo + ".setRootStrategy( RootStrategy( myRoot )) \n"
    return texte

  def SamplingStrategy(self):
  #--------------------------
  # Appelee eventuellement par DirectionalSampling
    texte += "   mySampling = " + self.DictMCVal["SamplingStrategy"] + "()\n"
    texte += "   mySampling.setSamplingStrategy( SamplingStrategy( mySampling ) )\n"
    return texte


  def QuadraticCumul (self) :
  #--------------------------
  # Appelee eventuellement par CreeAnalyse
    texte  = "\n# Cumul quadratique\n\n"
    texte += "   myQuadraticCumul  = QuadraticCumul( myRandomVector_out)\n\n"
    texte += "   firstOrderMean    = myQuadraticCumul.getMeanFirstOrder()\n"
    texte += "   secondOrderMean   = myQuadraticCumul.getMeanSecondOrder()\n"
    texte += "   covariance        = myQuadraticCumul.getCovariance()\n"
    texte += "   importanceFactors = myQuadraticCumul.getImportanceFactors()\n"
    return texte

  def CreeEvent (self) :
  #------------------
  # Appelee eventuellement par Simulation et Reliability
    texte  = "\n# L'evenement\n\n"
    if not self.DictMCVal.has_key("Threshold") or not self.DictMCVal.has_key("ComparisonOperator"):
       print 'Attention Mot Clef "Threshold" ou "ComparisonOperator"  non renseigne'
       return texte
    texte += "   seuil = " +str (self.DictMCVal["Threshold"]) + "\n"
    texte += "   myEvent = Event(myRandomVector_out," 
    texte += "ComparisonOperator(" + str (self.DictMCVal["ComparisonOperator"]) + "()), seuil) \n"
    return texte

  def ParametresAlgo( self ):
  #---------------------------
  # Appelee par Simulation

    texte += "   nbMaxOutSampling = "

    if self.DictMCVal["MaximumOuterSamplingType"] == "UserDefined" :
       texte += str(self.DictMCVal["MaximumOuterSampling"])

    elif self.DictMCVal["MaximumOuterSamplingType"] == "Wilks" :
       texte += "Wilks.ComputeSampleSize( " + str(self.DictMCVal["Wilks_Alpha"]) + ", " \
                 + str(self.DictMCVal["Wilks_Beta"]) + ", " + str(self.DictMCVal["Wilks_I"]) + " )"
       texte += '\n   print "MaximumOuterSampling = ", nbMaxOutSampling, "\n" \n'

    texte += "   " + NomAlgo + ".setMaximumOuterSampling(nbMaxOutSampling)"
    for MC in self.ListeOrdreMCParametresAlgo :
        if self.DictMCVal.has_key(MC) and self.DictMCVal[MC] != None :
           texte += "   myMethod.set"+ MC +"(" + str(self.DictMCVal[MC]) + ")\n\n "

#			_____________________________________

  def CreeRandomGenerator (self) :
  #-------------------------------
  # Appelee par CreeSTD
    texte = ""
    if self.DictMCVal.has_key("RandomGeneratorSeed") :
      texte += "# We set the RandomGenerator seed in order to replay the study\n"
      texte += "   RandomGenerator().SetSeed(%d)\n" % self.DictMCVal["RandomGeneratorSeed"]
    return texte

  def CreeFunction (self) :
  #-------------------------
  # Appelee par CreeSTD
    '''
    La fonction :
    Remarque : le nom 'solver' est en dur ici. Il doit imperativement correspondre
                 au nom du fichier xml : 'solver.xml'
    '''
    texte  = "\n# La fonction\n\n"
    texte += '   myFunction = NumericalMathFunction(\"XXXXXX\")\n'
    texte += '   dim = myFunction.getInputNumericalPointDimension()\n'
    return texte


  def CreeCopula (self) :
  #------------------
  # Appelee par CreeSTD
    texte  = "\n# La copule\n\n"
    texte += "   myCopula = IndependentCopula(dim)\n"
    return texte


  def CreeDistribution (self) :
  #----------------------------
  # Appelee par CreeSTD
    texte  = "\n# La distribution\n\n"
    texte +=  "   myDistribution = ComposedDistribution(myCollection, Copula(myCopula))\n"
    return texte


  def CreeRandomVector (self) :
  #----------------------------
  # Appelee par CreeSTD
    texte  = "\n# Le Random Vector\n\n"
    texte += "   myRandomVector_in  = RandomVector(Distribution(myDistribution))\n"
    texte += "   myRandomVector_out = RandomVector(myFunction, myRandomVector_in)\n"
    return texte


# _______________________________



  def ImportanceSampling (self) :
  #-----------------------------
  # Appele eventuellement par Reliability

    texte  = "    temporaryResult = " + self.NomAlgo + ".getResult()\n\n"
    texte += "   mean  = temporaryResult.getPhysicalSpaceDesignPoint()\n"
    texte += "   sigma = NumericalPoint( mean.getDimension(), 1.0 )\n"
    texte += "   R     = CorrelationMatrix( mean.getDimension() )\n"
    texte += "   myImportance = Normal( mean, sigma, R )\n\n\n"

    texte += "   importanceSamplingAlgo = ImportanceSampling( myEvent, Distribution( myImportance ) )\n\n"

    for MC in self.ListeOrdreImportanceSampling :
        if self.DictMCVal.has_key("MC") :
           debut="   importanceSamplingAlgo.set"+MC.split("_")[-1]
           texte += debut + "( " + str(self.DictMCVal[MC]) + " )\n"

    texte += "\n   importanceSamplingAlgo.run()\n\n"
    self.NomAlgo = "importanceSamplingAlgo"
    return texte


  def CreeResu (self) :
  #------------------
    '''
    '''
    texte  = "\n# Le resultat\n\n"
    texte += " myResu  = " + self.NomAlgo +  ".getResult() \n"
    texte += " probability = myResu.getEventProbability()"

    return texte



  def CreeLois (self) :
  #------------------
    '''
    '''
    code_erreur = 0
    texte  = "\n# Les lois\n\n"
    if self.DictMCVal.has_key("Analysis") and self.DictMCVal["Analysis"] == "Reliability" :
      texte  += "   myPhysicalStartingPoint = NumericalPoint(dim, 0.0)\n"
    texte += "   myCollection = DistributionCollection(dim)\n\n"

    numVar = 0
    for DictVariable in self.ListeVariables :

       boolLoiDef = True
       if DictVariable.has_key("MarginalDistribution") and DictVariable.has_key("Name"):
          ConceptLoi = DictVariable["MarginalDistribution"]
          NomLoi = DictVariable["Name"]+"_Dist"
       else :
          boolLoiDef = False
       
       if boolLoiDef and self.DictLois.has_key(ConceptLoi):
          loi = self.DictLois[ConceptLoi]
       else :
          boolLoiDef = False
      
       if boolLoiDef and loi.has_key("Kind") :
          TypeLoi = loi["Kind"]
       else :
          boolLoiDef = False

       if not boolLoiDef or TypeLoi not in self.listeParamLoi.keys() : 
          texte += " Loi " + TypeLoi +" non programmee \n"
	  numVar += 1
	  continue

       ListeParametres = []
       TexteParametres = ""
       for Param in self.listeParamLoi[TypeLoi]:
          if loi.has_key(Param) :
             texte += "   " + NomLoi + "_" + Param + " = " + str(loi[Param]) + "\n" 
	     ListeParametres.append(NomLoi + "_" + Param) 
	     TexteParametres += NomLoi + "_" + Param + ","

       texte += "   " + NomLoi + " = " + TypeLoi + "( " 

       if loi.has_key("Settings" ) and self.listeParamLoiSettings.has_key(TypeLoi) \
       and self.listeParamLoiSettings[TypeLoi].has_key(loi["Settings"]):
          NumParam = self.listeParamLoiSettings[TypeLoi][loi["Settings"]]
          texte += TexteParametres + NumParam +" )\n"
       else :
          texte += TexteParametres[:-1] + " )\n"

       texte += "   " + NomLoi + '.setName( "'+DictVariable["Name"] +'" )\n'
       texte += "   myCollection["+str(numVar)+"] = Distribution( "+NomLoi+" )\n"

       if self.DictMCVal["Analysis"] == "Reliability" :
          texte += "   myPhysicalStartingPoint["+str(numVar)+"] = "
          if DictVariable.has_key("PhysicalStartingPoint") :
             texte += str(DictVariable["PhysicalStartingPoint"]) +"\n\n"
          else :
             texte += NomLoi+".computeQuantile( 0.5 )[0]\n\n"

       numVar += 1
    return texte


#			_____________________________________________________

  def CreeEntete (self) :
  #------------------
    '''
    Entete :
    '''

    texte  = "#!/usr/bin/env python\n"
    texte += "# -*- coding: iso-8859-1 -*-\n"
    texte += "import sys\n"
    texte += "import os\n"
    if self.DictLois.has_key("dir_openturns_python") :
      texte += "sys.path.append(\"" + self.DictLois["dir_openturns_python"] + "\")\n"
    if self.DictLois.has_key("DTDDirectory") :
      texte += "os.environ[\"OPENTURNS_WRAPPER_PATH\"] = \".:" + self.DictLois["DTDDirectory"] + "\"\n"
    texte += "from openturns import *\n"
    texte += "error_message = None\n"
    texte += "try : \n"
    return texte

  def CreeTexteFin(self) :
  #------------------------------------
    texte ='\n\nexcept : \n'
    texte += '   error_message = sys.exc_type\n'
    texte += '   if error_message is not None :\n'
    texte += '      texte  = "================================================= \\n"\n'
    texte += '      texte += "     Message d\'erreur : \" + str(error_message)  + "\\n"\n'
    texte += '      texte += "=================================================\\n"\n'
    texte += '      print texte"\n'
    texte += "sys.exit(error_message)\n"
    return texte
  
