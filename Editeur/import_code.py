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
    Ce module réalise toutes les mises à jour du chemin pour 
    les imports de modules Python
"""
import sys
import os

import prefs
name='prefs_'+prefs.code
prefs_Code=__import__(name)
INSTALLDIR=prefs_Code.INSTALLDIR

# Ce chemin permet d'importer les modules Noyau et Validation
# représentant le code utilisé (si fourni)
# Ensuite on utilise les packages de l'intallation
if hasattr(prefs_Code,'CODE_PATH'):
   if prefs_Code.CODE_PATH:
      sys.path[:0]=[prefs_Code.CODE_PATH]
      import Noyau,Validation
      del sys.path[0]
sys.path[:0]=[prefs_Code.INSTALLDIR]

import Accas
