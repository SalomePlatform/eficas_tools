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

``PyQt4`` is currently supported.
"""

from PyQt4.QtCore import QTranslator

qt_translator = QTranslator()
eficas_translator = QTranslator()

def localise(application, locale=None):
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
    from PyQt4.QtCore import QLibraryInfo, QTextCodec
    
    QTextCodec.setCodecForTr(QTextCodec.codecForName("utf-8"))
    
    from PyQt4.QtCore import QLocale
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
    if eficas_translator.load("eficas_" + locale, "../UiQT4"):
        print "Eficas translator loaded!"
        application.installTranslator(eficas_translator)
    else:
        print "Unable to load Eficas translator!"

    

if __name__ == "__main__":
    import sys
    localise(sys.argv[1])
