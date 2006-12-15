import os,sys
sys.modules["Cata"]=sys.modules[__name__]
rep_macro = os.path.dirname(__file__)
sys.path.insert(0,rep_macro)

from cata import *
from math import ceil
from Extensions import param2
pi=param2.Variable('pi',pi)
