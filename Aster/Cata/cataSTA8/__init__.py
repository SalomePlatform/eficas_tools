import os,sys
sys.modules["Cata"]=sys.modules[__name__]
rep_macro = os.path.dirname(__file__)
sys.path.insert(0,rep_macro)
rep_macro=os.path.join(rep_macro,'Macro')
sys.path.insert(0,rep_macro)


#compatibilite avec V9
import Noyau
import Accas
class ASSD(Accas.ASSD,Noyau.AsBase):pass
class GEOM(Accas.GEOM,ASSD):pass
class formule(Accas.formule,ASSD):pass
Accas.ASSD=ASSD
Accas.GEOM=GEOM
Accas.formule=formule
#fin compatibilite

from cata import *
from math import ceil
from Extensions import param2
pi=param2.Variable('pi',pi)
