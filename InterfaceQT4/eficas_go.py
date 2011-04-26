# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
    Ce module permet de lancer l'application EFICAS en affichant
    un ecran Splash pour faire patienter l'utilisateur
"""
# Modules Python
import sys

# Test PyQt version
min_version_number_str = "4.4.2"
min_version_number = 0x040402
version_number_str = "0"
version_number = 0
try:
    from PyQt4 import pyqtconfig
    conf = pyqtconfig.Configuration()
    version_number_str = conf.pyqt_version_str
    version_number = conf.pyqt_version
except:
    sys.stderr.write("Error: PyQt4 not found (Eficas needs PyQt4 version %s or greater to run).\n" %
                     min_version_number_str)
    sys.exit(1)
if version_number < min_version_number:
    sys.stderr.write("Error: Eficas needs PyQt4 version %s or greater to run "
                     "(installed version is %s).\n" %
                     (min_version_number_str, version_number_str))
    sys.exit(1)

from PyQt4.QtGui import *

from Editeur  import import_code
from Editeur  import session
from qtEficas import Appli

def lance_eficas(code=None,fichier=None,ssCode=None):
    """
        Lance l'appli EFICAS
    """
    # Analyse des arguments de la ligne de commande
    options=session.parse(sys.argv)
    code=options.code

    app = QApplication(sys.argv)
    Eficas=Appli(code=code,ssCode=ssCode)
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

def lance_MapToSh(code=None,fichier=None,ssCode='s_polymers_st_1_V1'):
    """
        Lance l'appli EFICAS pour trouver les noms des groupes
    """
    # Analyse des arguments de la ligne de commande
     
    options=session.parse(sys.argv)
    code=options.code
    fichier=options.comm[0]

    app = QApplication(sys.argv)
    Eficas=Appli(code=code,ssCode=ssCode)

    from ssIhm  import QWParentSSIhm
    parent=QWParentSSIhm(code,Eficas,None,ssCode)

    import readercata
    if not hasattr ( Eficas, 'readercata'):
           monreadercata  = readercata.READERCATA( parent, Eficas )
           Eficas.readercata=monreadercata

    from editor import JDCEditor
    monEditeur=JDCEditor(Eficas,fichier)
    texte=monEditeur.run("non")
    print texte
