# -*- coding: utf-8 -*-
import os
import prefs
import basestyle
from basestyle import STYLE,style

inistylefile=os.path.join(prefs.REPINI,"style.py")
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


