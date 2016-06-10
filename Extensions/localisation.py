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
Creates and loads two ``QTranslator`` objects, one for pure Qt, one for Eficas,
and installs them to a ``QApplication``.

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
    localise(QApplication) -> None

    Loads and installs to a ``QApplication`` two ``QTranslator``
    objects, one for pure Qt for translating the strings 
    available in Qt, and one or Eficas, for translating 
    the strings specified precisely for Eficas.
    If the Qt base translator cannot be loaded with the locale
    specified by the user, one attempts to load Qt base 
    translator with the system locale.
    If no locale is specified by the user, the system locale
    is used instead, for both Qt base and Eficas translators.
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

    if locale is None:
        #locale = sys_locale
        locale="fr"

    #global qt_translator
    #if qt_translator.load("qt_" + locale,
    #                      QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
    #    application.installTranslator(qt_translator)
    #elif qt_translator.load("qt_" + sys_locale,
    #                        QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
    #    print "Qt base translator with default locale loaded!"
    #    application.installTranslator(qt_translator)
        # Try to load Qt base translator according to system locale.
    #else:
    #    print "Unable to load Qt base translator!"
    
    global eficas_translator
    print locale
    if locale=="ang" : locale="en"
    #print "eficas_" + locale, monPath
    if file != None :
       print 'chagrement de ', file,monPath
       print eficas_translator.load(file,monPath)
       print QApplication.installTranslator(eficas_translator)
       return
     

    if eficas_translator.load("eficas_" + locale, monPath):
        QApplication.installTranslator(eficas_translator)
        print "chargement eficas_", locale, monPath
    else:
        print "Unable to load Eficas translator!"

    

if __name__ == "__main__":
    import sys
    localise(sys.argv[1])
