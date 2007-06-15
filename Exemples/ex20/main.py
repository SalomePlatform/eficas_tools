# -*- coding: utf-8 -*-
"""
   Construction d'un item JDC
"""

import sys
sys.path[:0]=['../..','../../Aster/Cata','../../Aster']

from cataSTA8 import cata
from Editeur.autre_analyse_cata import analyse_catalogue

f=open('ahlv100a.comm','r')
text=f.read()
f.close()

cata_ordonne,list_simp_reel = analyse_catalogue(cata)
j=cata.JdC(procedure=text,cata=cata,nom="ahlv100a",
            cata_ord_dico=cata_ordonne)
j.compile()
if not j.cr.estvide():
   print j.cr
   sys.exit()

j.exec_compile()
if not j.cr.estvide():
   print j.cr
   sys.exit()

from Editeur.treeitemincanvas import TREEITEMINCANVAS
from Editeur import comploader
comploader.charger_composants()
t=TREEITEMINCANVAS(j,"ahlv100a")
t.mainloop()




