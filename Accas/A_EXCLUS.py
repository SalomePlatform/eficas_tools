from Noyau import N_REGLE
from Validation import V_EXCLUS
from Ihm import I_EXCLUS

class EXCLUS(I_EXCLUS.EXCLUS,V_EXCLUS.EXCLUS,N_REGLE.REGLE):
   """
       La classe utilise l'initialiseur de REGLE. Il n'est pas 
       nécessaire d'expliciter son initialiseur car 
       V_EXCLUS.EXCLUS n'en a pas 
   """
