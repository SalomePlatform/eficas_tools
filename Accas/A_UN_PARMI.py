from Noyau import N_REGLE
from Validation import V_UN_PARMI
from Ihm import I_UN_PARMI

class UN_PARMI(I_UN_PARMI.UN_PARMI,V_UN_PARMI.UN_PARMI,N_REGLE.REGLE):
   """
       La classe utilise l'initialiseur de REGLE. Il n'est pas 
       nécessaire d'expliciter son initialiseur car 
       V_UN_PARMI.UN_PARMI n'en a pas 
   """
