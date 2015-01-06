#!/usr/bin/env python
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

import re
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

class MonBoutonValide(QToolButton) :

     def __init__(self,parent):
        QToolButton.__init__(self,parent)
        while( not(hasattr(parent,'node'))): 
          parent= parent.parent()
        self.parent=parent

     def mouseDoubleClickEvent(self, event):
        print "dans mouseDoubleClickEvent"
        strRapport=unicode(self.parent.node.item.object.report())
        self.parent.editor._viewText(strRapport, "JDC_RAPPORT")

     def mousePressEvent(self, event):
       print "dans mousePressEvent"
       if self.parent.node.item.object.isvalid() :
          myToolTip=QString(tr("objet valide"))
          QToolTip.showText(event.globalPos(),myToolTip )
       else :
          texte=unicode(self.parent.node.item.object.report())
          deb=1
          for l in texte.split('\n')[2:-2]:
              if re.match('^[\t !]*$',l) : continue
              if re.match('^ *Fin Mot-cl',l) : continue
              if re.match('^ *D?but Mot-cl',l) : continue
              if re.match('^ *Mot-cl',l) : continue
              l=l.replace('!','')
              if deb :
                 deb=0
                 t=l
              else :
                 t=t+'\n'+l
          myToolTip=QString(t)
       QToolTip.showText(event.globalPos(),myToolTip )


