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
from PyQt4.QtGui import *

from Editeur  import import_code
from Editeur  import session
from qtEficas import Appli

def lance_eficas(code=None,fichier=None,choix="non"):
    """
        Lance l'appli EFICAS
    """
    # Analyse des arguments de la ligne de commande
    options=session.parse(sys.argv)
    code=options.code

    app = QApplication(sys.argv)
    Eficas=Appli(code=code,choix=choix)
    Eficas.show()

    res=app.exec_()
    sys.exit(res)


def lance_eficas_ssIhm(code=None,fichier=None,version='v9.5'):
    """
        Lance l'appli EFICAS pour trouver les noms des groupes
    """
    # Analyse des arguments de la ligne de commande
    options=session.parse(sys.argv)
    code=options.code

    app = QApplication(sys.argv)
    Eficas=Appli(code=code)

    from ssIhm  import QWParentSSIhm
    parent=QWParentSSIhm(code,Eficas,version)

    import readercata
    if not hasattr( readercata, 'reader' ) :
       readercata.reader = readercata.READERCATA( parent, Eficas )

    from editor import JDCEditor
    monEditeur=JDCEditor(Eficas,fichier)
    print monEditeur.cherche_Groupes()
