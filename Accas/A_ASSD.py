
from Ihm import I_ASSD
from Ihm import I_FONCTION
from Noyau import N_ASSD 
from Noyau import N_GEOM 
from Noyau import N_FONCTION 
from Noyau import N_CO 

# On ajoute la classe ASSD dans l'héritage multiple pour recréer 
# une hiérarchie d'héritage identique à celle de Noyau
# pour faire en sorte que isinstance(o,ASSD) marche encore après 
# dérivation

class ASSD(N_ASSD.ASSD,I_ASSD.ASSD):pass

class assd(N_ASSD.assd,I_ASSD.ASSD,ASSD):pass

class FONCTION(N_FONCTION.FONCTION,I_FONCTION.FONCTION,ASSD):
   def __init__(self,etape=None,sd=None,reg='oui'):
      N_FONCTION.FONCTION.__init__(self,etape=etape,sd=sd,reg=reg)
      I_FONCTION.FONCTION.__init__(self,etape=etape,sd=sd,reg=reg)

class fonction(N_FONCTION.fonction,I_FONCTION.fonction,ASSD):
   def __init__(self,etape=None,sd=None,reg='oui'):
      N_FONCTION.fonction.__init__(self,etape=etape,sd=sd,reg=reg)
      I_FONCTION.fonction.__init__(self,etape=etape,sd=sd,reg=reg)

class GEOM(N_GEOM.GEOM,I_ASSD.ASSD,ASSD):pass
class geom(N_GEOM.geom,I_ASSD.ASSD,ASSD):pass
class CO(N_CO.CO,I_ASSD.ASSD,ASSD):pass
