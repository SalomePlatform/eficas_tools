"""
   Construction d'un item JDC
"""

import prefs

import sys
sys.path[:0]=['../..','../../Editeur','../../Aster' ]

from Cata import cata_STA6
cata=cata_STA6

from analyse_catalogue import analyse_catalogue

from Appli import Appli
import jdcdisplay

f=open('ahlv100a.comm','r')
text=f.read()
f.close()

fic_cata="../../Aster/Cata/cata_STA6.py"
cata_ordonne = analyse_catalogue(None,fic_cata)

j=cata.JdC(procedure=text,cata=cata,nom="ahlv100a",
            cata_ord_dico=cata_ordonne.entites)

j.compile()
if not j.cr.estvide():
   print j.cr
   sys.exit()

j.exec_compile()
if not j.cr.estvide():
   print j.cr
   sys.exit()

a=Appli()

d=jdcdisplay.JDCDISPLAY(j,"ahlv100a",appli=a,parent=a.root)

a.root.mainloop()




