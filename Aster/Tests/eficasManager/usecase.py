#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# This illustrates how to run Eficas dynamically with a user defined catalog
# (gboulant - 23/03/2011)

import eficasManager
eficasManager.addCatalog(catalogName="demo", catalogPath="mycata.py")
eficasManager.start("demo")
