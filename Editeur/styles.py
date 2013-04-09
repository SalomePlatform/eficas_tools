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
import os
import prefs
name='prefs_'+prefs.code
prefsCode=__import__(name)
import basestyle
from basestyle import STYLE,style

inistylefile=os.path.join(prefsCode.repIni,"style.py")
if os.path.isfile(inistylefile):
   execfile(inistylefile)

userstylefile=os.path.expanduser("~/Eficas_install/style.py")
if os.path.isfile(userstylefile):
   execfile(userstylefile)

import fontes
for attr in dir(style):
   if attr[0]=='_':continue
   if not hasattr(fontes,attr):continue
   setattr(fontes,attr,getattr(style,attr))


