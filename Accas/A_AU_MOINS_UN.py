from Noyau import N_REGLE
from Validation import V_AU_MOINS_UN
from Ihm import I_REGLE

class AU_MOINS_UN(V_AU_MOINS_UN.AU_MOINS_UN,I_REGLE.REGLE,N_REGLE.REGLE):
   """
       La classe utilise l'initialiseur de REGLE. Il n'est pas 
       nécessaire d'expliciter son initialiseur car 
       V_AU_MOINS_UN.AU_MOINS_UN n'en a pas 
   """
