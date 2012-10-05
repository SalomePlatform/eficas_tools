#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
"""
"""

import optparse
import log

from load   import getJDCFromTexte
from mocles import parseKeywords
from removemocle  import *
from renamemocle  import *
from renamemocle  import *
from inseremocle  import *
from changeValeur import *
from movemocle    import *
from dictErreurs  import GenereErreurPourCommande,GenereErreurMotCleInFact


atraiter=()

dict_erreurs={}

sys.dict_erreurs=dict_erreurs

atraiter=( "MACR_ADAP_MAIL",)

class MonTraducteur:
 
    def __init__(self,texte) :
       self.jdc=getJDCFromTexte(texte,atraiter)
       self.root=self.jdc.root

    def traduit(self):
       parseKeywords(self.root)
       renameMotCleInFact(self.jdc,"CALC_META","ETAT_INIT","META_INIT","META_INIT_ELNO")
       return self.jdc.getSource()

