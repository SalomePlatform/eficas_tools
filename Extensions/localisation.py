# -*- coding: utf-8 -*-
# copyright 2012 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
"""

"""

import os
from determine import monEnvQT5
if monEnvQT5 :
   from PyQt5.QtCore import QTranslator
else :
   from PyQt4.QtCore import QTranslator

qt_translator = QTranslator()
eficas_translator = QTranslator()

def localise(application, locale=None,file=None ):
    """
    """
    if monEnvQT5 :
       from PyQt5.QtCore import QLibraryInfo
       from PyQt5.QtCore import QLocale
       from PyQt5.QtWidgets import QApplication
       monPath=os.path.join(os.path.dirname(__file__),'..','UiQT5')
    else :
       from PyQt4.QtCore import QLibraryInfo
       from PyQt4.QtCore import QLocale
       from PyQt4.QtGui import QApplication
       monPath=os.path.join(os.path.dirname(__file__),'..','UiQT4')

    sys_locale = QLocale.system().name()

    if locale is None: locale="fr"
    
    global eficas_translator
    if locale=="ang" : locale="en"

    if file != None :
       print ('chargement de ', file,monPath)
       print (eficas_translator.load(file,monPath))
       print (QApplication.installTranslator(eficas_translator))
       return
     
    if eficas_translator.load("eficas_" + locale, monPath):
        QApplication.installTranslator(eficas_translator)
    else:
        print ("Unable to load Eficas translator!")
       

if __name__ == "__main__":
    import sys
    localise(sys.argv[1])
