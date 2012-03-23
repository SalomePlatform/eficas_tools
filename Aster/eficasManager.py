#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
# This module helps you to dynamically add a catalog in the list of
# Aster catalogs and then start Eficas with this catalog
#
# WARN: this requires that <EFICAS_ROOT> and <EFICAS_ROOT>/Aster are
# both in the PYTHONPATH
#
# (gboulant - 23/03/2012)

import prefs_ASTER
def addCatalog(catalogName, catalogPath):
    """
    Function to add a catalog caraterized by a name (for the -c option
    of the command line) and a path (the location of the python module
    that corresponds to the catalog).
    """
    prefs_ASTER.addCatalog(catalogName, catalogPath)

import sys
import prefs
from InterfaceQT4 import eficas_go
def start(catalogName=None):
    """
    This simply start Eficas as usual, and passing the catalog name as
    an argument if not already present on the command line.
    """
    if catalogName is not None and not "-c" in sys.argv:
        # The catalogName can be consider as the -c option
        sys.argv.append("-c")
        sys.argv.append(catalogName)
    eficas_go.lance_eficas(code=prefs.code)

#
# ===========================================================
# Unit tests
# ===========================================================
#
def TEST_start():
    addCatalog(catalogName="demo", catalogPath="mycata.py")
    #start()
    start("demo")

if __name__ == "__main__":
    TEST_start()
