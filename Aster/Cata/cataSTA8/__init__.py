import os,sys
import prefs
import sys
rep_macro = os.path.join(prefs.REPINI,'Cata/cataSTA8')
sys.path.insert(0,rep_macro)
from cata import *
from math import ceil
from Extensions import param2
pi=param2.Variable('pi',pi)
