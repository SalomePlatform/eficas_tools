from Noyau import N_REGLE
from Validation import V_A_CLASSER
from Ihm import I_A_CLASSER

class A_CLASSER(V_A_CLASSER.A_CLASSER,N_REGLE.REGLE,I_A_CLASSER.A_CLASSER):
   """
       La classe utilise l'initialiseur  du module V_. 
       Il faut absolument que V_A_CLASSER soit en premier dans l'héritage
   """
