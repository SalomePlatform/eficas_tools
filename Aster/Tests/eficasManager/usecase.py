#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# This illustrates how to run Eficas dynamically with a user defined catalog
# (gboulant - 23/03/2011)

import eficasManager

def UC_run_with_my_catalog():
    eficasManager.addCatalog(catalogName="demo", catalogPath="catalog.py")
    eficasManager.start("demo")

def UC_getJdcParameters_fromFile():
    # After having used the calaog.py to enter data, and save to a
    # file named data.comm, you could run the following instruction to
    # get the data frm the data comm file.
    jdc = eficasManager.loadJdc('data.comm')
    parameters=eficasManager.getJdcParameters(jdc,"EPREUVE_ENCEINTE")
    print parameters

if __name__ == "__main__":
    #UC_run_with_my_catalog()
    UC_getJdcParameters_fromFile()
