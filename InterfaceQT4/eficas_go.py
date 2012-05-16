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

# Modules Python
import sys,os
repIni=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
ihmQTDir=os.path.join(repIni,"UiQT4")
editeurDir=os.path.join(repIni,"Editeur")
ihmDir=os.path.join(repIni,"InterfaceQT4")
if ihmDir not in sys.path : sys.path.append(ihmDir)
if ihmQTDir not in sys.path : sys.path.append(ihmQTDir)
if editeurDir not in sys.path :sys.path.append(editeurDir)

from PyQt4.QtGui import *

def lance_eficas(code=None,fichier=None,ssCode=None,multi=False):
    """
        Lance l'appli EFICAS
    """
    # Analyse des arguments de la ligne de commande
    from Editeur  import session
    options=session.parse(sys.argv)
    if options.code!= None : code=options.code
    if options.ssCode!= None : ssCode=options.ssCode

    from qtEficas import Appli
    app = QApplication(sys.argv)
    Eficas=Appli(code=code,ssCode=ssCode,multi=multi)
    Eficas.show()

    res=app.exec_()
    sys.exit(res)


def lance_eficas_ssIhm(code=None,fichier=None,ssCode=None,version=None):
    """
        Lance l'appli EFICAS pour trouver les noms des groupes
    """
    # Analyse des arguments de la ligne de commande
    options=session.parse(sys.argv)
    code=options.code

    from qtEficas import Appli
    app = QApplication(sys.argv)
    Eficas=Appli(code=code,ssCode=ssCode)

    from ssIhm  import QWParentSSIhm
    parent=QWParentSSIhm(code,Eficas,version)

    import readercata
    if not hasattr ( Eficas, 'readercata'):
           monreadercata  = readercata.READERCATA( parent, Eficas )
           Eficas.readercata=monreadercata


    from editor import JDCEditor
    monEditeur=JDCEditor(Eficas,fichier)
    print monEditeur.cherche_Groupes()

def lance_eficas_param(code='MAP',fichier='/local/noyret/Eficas_MAP/creation.comm',ssCode='Creation',version='creation'):
    """
        Lance l'appli EFICAS pour trouver les noms des groupes
    """
    # Analyse des arguments de la ligne de commande
    from Editeur  import session
    options=session.parse(sys.argv)
    if options.code!= None : code=options.code
    if options.ssCode!= None : ssCode=options.ssCode

    from qtEficas import Appli
    app = QApplication(sys.argv)
    Eficas=Appli(code=code,ssCode=ssCode)

    from ssIhm  import QWParentSSIhm
    parent=QWParentSSIhm(code,Eficas,version)

    import readercata
    if not hasattr ( Eficas, 'readercata'):
           monreadercata  = readercata.READERCATA( parent, Eficas )
           Eficas.readercata=monreadercata


    from editor import JDCEditor
    monEditeur=JDCEditor(Eficas,fichier)
    print monEditeur.cherche_Dico()

if __name__ == "__main__":
    import sys
    sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))
    lance_eficas(code=None,fichier=None,ssCode=None,multi=True)
    

