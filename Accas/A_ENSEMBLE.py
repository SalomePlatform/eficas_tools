from Noyau import N_REGLE
from Validation import V_ENSEMBLE
from Ihm import I_REGLE

class ENSEMBLE(I_REGLE.REGLE,V_ENSEMBLE.ENSEMBLE,N_REGLE.REGLE):
   """
       La classe utilise l'initialiseur de REGLE. Il n'est pas 
       nécessaire d'expliciter son initialiseur car 
       V_ENSEMBLE.ENSEMBLE n'en a pas 
   """
