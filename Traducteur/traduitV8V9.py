#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
usage="""usage: %prog [options]
Typical use is:
  python traduitV7V8.py --infile=xxxx --outfile=yyyy
"""

import log
import optparse

from load   import getJDC
from mocles import parseKeywords
from removemocle  import *
from renamemocle  import *
from renamemocle  import *
from inseremocle  import *
from changeValeur import *
from movemocle    import *
from dictErreurs  import GenereErreurPourCommande

import calcG


atraiter=( "DEFI_MAILLAGE",)

def traduc(infile,outfile,flog=None):

    hdlr=log.initialise(flog)
    jdc=getJDC(infile,atraiter)
    root=jdc.root

    #Parse les mocles des commandes
    parseKeywords(root)
    
    ####################### traitement erreurs ########################
    #GenereErreurPourCommande(jdc,("POST_RCCM","DIST_LIGN_3D","IMPR_OAR","COMB_CHAM_NO","COMB_CHAM_ELEM"))
    GenereErreurPourCommande(jdc,())

    ####################### traitement CALC_META     #######################
    renameMotCleInFact(jdc,"DEFI_MAILLAGE","DEFI_SUPER_MAILLE","MACR_ELEM_STAT","MACR_ELEM")

    #########################################################################


    f=open(outfile,'w')
    f.write(jdc.getSource())
    f.close()

    log.ferme(hdlr)

def main():
    parser = optparse.OptionParser(usage=usage)

    parser.add_option('-i','--infile', dest="infile", default='toto.comm',
        help="Le fichier à traduire")
    parser.add_option('-o','--outfile', dest="outfile", default='tutu.comm',
        help="Le fichier traduit")

    options, args = parser.parse_args()
    traduc(options.infile,options.outfile)

if __name__ == '__main__':
    main()

