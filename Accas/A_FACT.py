from Noyau import N_FACT
from Ihm import I_ENTITE
import A_MCFACT
import A_MCLIST

class FACT(N_FACT.FACT,I_ENTITE.ENTITE):
   class_instance=A_MCFACT.MCFACT
   list_instance=A_MCLIST.MCList
