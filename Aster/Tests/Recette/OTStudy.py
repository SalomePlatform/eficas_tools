#! /usr/bin/env python

# Chargement du module systeme
import sys
sys.path[:0]=['']

# Chargement du module math
import math

# Chargement du module Open TURNS
from openturns import *

results = {}


from openturns.viewer import ViewImage,StopViewer,WaitForViewer
# Definit le niveau d'affichage de la log
flags = Log.NONE
flags = flags + Log.WARN
flags = flags + Log.ERROR
flags = flags - Log.WRAPPER
flags = flags + Log.INFO
flags = flags - Log.USER
flags = flags - Log.DBG
Log.Show( flags )

# Charge le modele physique
wrapper = WrapperFile( '/local/noyret/Install_Eficas/EficasV1/Recettes/OTWrapper.xml' )
wrapperdata = wrapper.getWrapperData()
# Ces lignes sont utiles pour le fonctionnement du script sous Salome
if globals().has_key('framework'):
  frameworkdata = wrapperdata.getFrameworkData()
  frameworkdata.studyid_ = framework['studyid']
  frameworkdata.studycase_ = framework['studycase']
  frameworkdata.componentname_ = framework['componentname']
  wrapperdata.setFrameworkData( frameworkdata )
  wrapper.setWrapperData( wrapperdata )
# Fin des lignes pour Salome
model = NumericalMathFunction( wrapper )
n = model.getInputDimension()

# Etude par echantillonage aleatoire
# Definit la loi jointe des variables d'entree
collection = DistributionCollection( n )
description = Description( n )

# Definit la loi marginale de la composante 0
marginal_0 = Poisson( 3 )
marginal_0.setName( 'maDistr' )
description[ 0 ] = 'maVIn1'
collection[ 0 ] = Distribution( marginal_0 )

# Definit la loi marginale de la composante 1
marginal_1 = Poisson( 3 )
marginal_1.setName( 'maDistr' )
description[ 1 ] = 'maVIn2'
collection[ 1 ] = Distribution( marginal_1 )

# Definit la copule de la loi jointe
correlation = {}
correlation['maVIn1'] = {}
correlation['maVIn1']['maVIn1'] = 1
correlation['maVIn1']['maVIn2'] = 0
correlation['maVIn2'] = {}
correlation['maVIn2']['maVIn1'] = 0
correlation['maVIn2']['maVIn2'] = 1
R = getCorrelationMatrixFromMap( wrapperdata.getVariableList(), correlation )
copula = NormalCopula( R )

# Definit la loi jointe
distribution = ComposedDistribution( collection, Copula( copula ) )
distribution.setDescription( description )

# Definit le vecteur aleatoire d'entree
inputRandomVector = RandomVector( distribution )


# Etude 'Min/Max'
# Calcul
inSize = 12
outputRandomVector = RandomVector( model, inputRandomVector )
outputSample = outputRandomVector.getNumericalSample( inSize )
# Resultats
results["minValue"] = outputSample.getMin()
print 'minValue = ', results["minValue"]

results["maxValue"] = outputSample.getMax()
print 'maxValue = ', results["maxValue"]



# Flush des messages en attente
Log.Flush()

# Terminaison du fichier
#sys.exit( 0 )
