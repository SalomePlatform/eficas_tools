#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Ce module sert à lancer EFICAS configuré pour Code_Mini
"""
# Modules Python

# Modules Eficas
import prefs
#import Misc.Trace
from InterfaceTK import eficas_go

def main():
   #Misc.Trace.begin_trace()
   eficas_go.lance_eficas(code=prefs.code)
   #Misc.Trace.end_trace()

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


