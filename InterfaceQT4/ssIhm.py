# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
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
#    permet de lancer  EFICAS en n affichant rien

class QWParentSSIhm:
   def __init__(self,code,appliEficas,version_code,ssCode=None):
        self.ihm="QT"
        self.code=code
        self.version_code=version_code
        self.ssCode=ssCode
        if ssCode != None :
           self.format_fichier= ssCode  #par defaut
           #prefsCode.NAME_SCHEME=ssCode
        else :
           self.format_fichier="python" #par defaut
        self.appliEficas=appliEficas

