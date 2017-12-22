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
   Ce module sert a lancer EFICAS configure pour Code_Aster
"""
# Modules Python
# Modules Eficas

import sys,os
#sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))
import prefs
name='prefs_'+prefs.code
__import__(name)

#acceder scripts de Lucie
path1 = os.path.abspath(os.path.join(os.path.abspath(__file__),'TreatOutputs'))
path1 = 'C:\\Logiciels DER\\PSEN_V15\\Code\\ProcessOutputs_Eficas\TreatOutputs'
sys.path.append(path1)

print ('kjlkjlkjkl')
print ('kjlkjlkjkl')
print ('kjlkjlkjkl')
print ('kjlkjlkjkl')
print ('kjlkjlkjkl')
print ('kjlkjlkjkl')
print ('kjlkjlkjkl')

from InterfaceQT4 import eficas_go
if __name__ == '__main__': eficas_go.lanceEficas(code=prefs.code)
