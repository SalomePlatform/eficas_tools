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
"""
lancement EFICAS  ss Ihm
"""
from __future__ import absolute_import
from __future__ import print_function

# On ajoute le path jusqu a eficas et celui ou on trouve le prefs_Code
import os, sys
sys.path.insert(0,'/home/A96028/QT5GitEficasTravail/eficas')
sys.path.insert(0,'/home/A96028/QT5GitEficasTravail/eficas/Adao')

debug = True

if __name__ == '__main__': 
   from InterfaceQT4.eficas_go import getEficasSsIhm
   code='Adao'
   versionCode="V83"
   monEficasSsIhm = getEficasSsIhm(code=code,versionCode=versionCode)

   monFichier       = '/tmp/monFichierExistant.com'
   monHandler       = monEficasSsIhm.fileOpen(monFichier)
   if not monHandler : print (' souci!'); exit()

   #if debug : print ('monHandler  : ' , monHandler )
   #monHandlerDuplique   = monEficasSsIhm.fileOpen('/tmp/monFichierExistant.comm')
   #if debug : print ('monHandlerDuplique  : ' , monHandlerDuplique )
   #if monHandlerDuplique != monHandler : print ('Pb a l ouverture des fichiers')
   #monHandlerNew    = monEficasSsIhm.fileOpen('/tmp/monFichierVide.comm')
   #if debug : print ('monHandlerNew  : ' , monHandlerNew )


   # Attention il faut que le fichier existe -> arret du code sinon
   try    : monHandler.viewJdcSource()
   except : print ('impossible de visualiser le fichier ' , monHandler.getFileName())

   if debug :
      print ('______________________________________________________________')
      print (' Visualisation du Fichier en entree')
      print (monHandler.jdcRapport())
      print ('______________________________________________________________')
   if debug :
      print ('______________________________________________________________')
      print (' Visualisation du jdcText /tmp/monFichierExistant.comm')
      print (monHandler.viewJdcPy())
      print ('______________________________________________________________')
   debug=True
   if debug :
      print ('______________________________________________________________')
      print (' Visualisation du jdcDicoPython /tmp/monFichierExistant.comm')
      print (monHandler.getDicoPython())
      print ('______________________________________________________________')

   #monEficasSsIhm.fileClose()
   #monEficasSsIhm.fileNew()
   #monEficasSsIhm.fileSaveAs('/tmp/titi.comm')

   




