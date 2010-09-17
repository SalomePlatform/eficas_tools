#!/usr/bin/env python
# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================

"""
   Ce module sert à lancer EFICAS configuré pour Perfect
"""
# Modules Python

# Modules Eficas
import prefs
name='prefs_'+prefs.code
__import__(name)

import sys
from PyQt4.QtGui import *

from Editeur  import import_code
from Editeur  import session
from qtEficas import Appli

from InterfaceQT4 import eficas_go
from InterfaceQT4 import monChoixMap

class ChoixCata:
 def __init__(self):
   self.schema=""
   self.module=""
   self.nom=""
  
options=session.parse(sys.argv)
cata=options.cata
MonChoixCata=ChoixCata()
if cata == None :
   app = QApplication(sys.argv)
   ChoixMap = monChoixMap.MonChoixMap(MonChoixCata) 
   ChoixMap.show()
   res=app.exec_()
else :
   import re
   p=re.compile('_V\d+')
   if p.search(cata) == None :
      print "Ce Catalogue ne convient pas"
      exit(1)
   MonChoixCata.nom=cata[0: p.search(cata).start()]
   #MonChoixCata.nom=cata

#permet de choisir le module
eficas_go.lance_eficas(code=prefs.code,ssCode=MonChoixCata.nom)
#eficas_go.lance_eficas(code=prefs.code,choix="non")
