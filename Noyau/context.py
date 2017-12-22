# coding=utf-8
# ======================================================================
# COPYRIGHT (C) 1991 - 2017  EDF R&D                  WWW.CODE-ASTER.ORG
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

from __future__ import absolute_import
_root = None
_cata = None
debug = 0

# Le "current step" est l'etape courante.
# Une macro se declare etape courante dans sa methode Build avant de construire
# ses etapes filles ou dans BuildExec avant de les executer.
# Les etapes simples le font aussi : dans Execute et BuildExec.
# (Build ne fait rien pour une etape)


def setCurrentStep(step):
    """
       Fonction qui permet de changer la valeur de l'etape courante
    """
    global _root
    if _root:
        raise Exception("Impossible d'affecter _root. Il devrait valoir None")
    _root = step


def getCurrentStep():
    """
       Fonction qui permet d'obtenir la valeur de l'etape courante
    """
    return _root


def unsetCurrentStep():
    """
       Fonction qui permet de remettre a None l'etape courante
    """
    global _root
    _root = None


def setCurrentCata(cata):
    """
       Fonction qui permet de changer l'objet catalogue courant
    """
    global _cata
    if _cata:
        raise Exception("Impossible d'affecter _cata. Il devrait valoir None")
    _cata = cata


def getCurrentCata():
    """
       Fonction qui retourne l'objet catalogue courant
    """
    return _cata


def unsetCurrentCata():
    """
       Fonction qui permet de remettre a None le catalogue courant
    """
    global _cata
    _cata = None
