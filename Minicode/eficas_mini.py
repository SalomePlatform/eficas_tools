#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Ce module sert � lancer EFICAS configur� pour Code_Mini
"""
# Modules Python
import sys,os

# Modules Eficas
import prefs
sys.path[:0]=[prefs.INSTALLDIR]

args=sys.argv[1:]
for a in args:
   if a == "-display":
      os.environ['DISPLAY']=args[args.index("-display")+1]

import Misc.Trace
import Editeur
from Editeur import eficas_go

def main():
   #Misc.Trace.begin_trace()
   if len(sys.argv) > 1 :
       # on veut ouvrir un fichier directement au lancement d'Eficas
       eficas_go.lance_eficas(code='MINICODE',fichier = sys.argv[1])
   else:
       # on veut ouvrir Eficas 'vide'
       eficas_go.lance_eficas(code='MINICODE')
   Misc.Trace.end_trace()

def hidez():
   from Misc import Cyclops
   z = Cyclops.CycleFinder()
   z.run(main)
   z.find_cycles()
   z.show_stats()
   z.show_cycles()
   # z.show_cycleobjs()
   # z.show_sccs()
   z.show_arcs()

withCyclops=0

if withCyclops:
   hidez()
else:
   main()

