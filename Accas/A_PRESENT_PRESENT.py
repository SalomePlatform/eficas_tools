from Noyau import N_REGLE
from Validation import V_PRESENT_PRESENT
from Ihm import I_PRESENT_PRESENT

class PRESENT_PRESENT(I_PRESENT_PRESENT.PRESENT_PRESENT,
                      V_PRESENT_PRESENT.PRESENT_PRESENT,
                      N_REGLE.REGLE):
   """
       La classe utilise l'initialiseur de REGLE. Il n'est pas 
       nécessaire d'expliciter son initialiseur car 
       V_PRESENT_PRESENT.PRESENT_PRESENT n'en a pas 
   """
