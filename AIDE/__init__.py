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
import os
import aide_objets
import aide_gui
import viewer

def go(fichier=None,master=None):
    if not fichier :
       fichier=os.path.join(os.path.dirname(__file__),"../Aide/fichiers_ASTER","index.html")
       print fichier
    o=viewer.HTMLViewer(master)
    o.display(fichier)
    return o

def go2(fichier=None,master=None):
    if not fichier :
       fichier=os.path.join(os.path.dirname(__file__),"index_aide.py")
    index = aide_objets.INDEX(fichier)
    index.build()
    o = aide_gui.AIDE_GUI(index,master=master)
    o.build()
    return o

def go3(fichier=None,parent=None):
    if not fichier :
       pathDoc=os.path.join(os.path.dirname(__file__),"fichiers")
    viewer.HTMLQTViewer(parent,pathDoc)

