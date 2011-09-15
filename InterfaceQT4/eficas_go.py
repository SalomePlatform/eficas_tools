#!/usr/bin/env python
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

def lance_MapToSh(code=None,fichier=None,ssCode='s_polymers_st_1_V1'):
     
    options=session.parse(sys.argv)
    code=options.code
    fichier=options.comm[0]

    from qtEficas import Appli
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

if __name__ == "__main__":
    import sys
    sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))
    lance_eficas(code=None,fichier=None,ssCode=None,multi=True)
    

