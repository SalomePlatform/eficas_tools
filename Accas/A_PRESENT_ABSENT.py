from Noyau import N_REGLE
from Validation import V_PRESENT_ABSENT
from Ihm import I_PRESENT_ABSENT

class PRESENT_ABSENT(I_PRESENT_ABSENT.PRESENT_ABSENT,V_PRESENT_ABSENT.PRESENT_ABSENT,
                     N_REGLE.REGLE):
   """
       La classe utilise l'initialiseur de REGLE. Il n'est pas 
       nécessaire d'expliciter son initialiseur car 
       V_PRESENT_ABSENT.PRESENT_ABSENT n'en a pas 
   """
