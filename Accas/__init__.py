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
   Ce package contient les classes qui seront effectivement utilisées dans les applications. 
   C'est dans ce package que sont réalisées les combinaisons de classes de base
   avec les classes MIXIN qui implémentent les fonctionnalités qui ont été séparées
   du noyau pour des raisons de modularité afin de faciliter la maintenance et
   l'extensibilité.

   De plus toutes les classes utilisables par les applications sont remontées au
   niveau du package afin de rendre le plus indépendant possible l'utilisation des
   classes et leur implémentation.
"""
from A_JDC_CATA import JDC_CATA
from A_OPER import OPER
from A_PROC import PROC
from A_MACRO import MACRO
from A_FORM import FORM
from A_BLOC import BLOC
from A_FACT import FACT
from A_SIMP import SIMP
from A_EVAL import EVAL
from A_NUPLET import NUPL

from A_JDC import JDC
from A_ETAPE import ETAPE
from A_PROC_ETAPE import PROC_ETAPE
from A_MACRO_ETAPE import MACRO_ETAPE
from A_FORM_ETAPE import FORM_ETAPE
from A_MCFACT import MCFACT
from A_MCLIST import MCList
from A_MCBLOC import MCBLOC
from A_MCSIMP import MCSIMP

# Les règles
from A_AU_MOINS_UN import AU_MOINS_UN
from A_AU_PLUS_UN import AU_PLUS_UN
from A_UN_PARMI import UN_PARMI
from A_PRESENT_PRESENT import PRESENT_PRESENT
from A_PRESENT_ABSENT import PRESENT_ABSENT
from A_EXCLUS import EXCLUS
from A_ENSEMBLE import ENSEMBLE
from A_A_CLASSER import A_CLASSER

from A_ASSD import ASSD,assd
from A_ASSD import GEOM,geom
# Pour le moment on laisse fonction (ceinture et bretelles)
from A_ASSD import FONCTION, fonction
from A_ASSD import formule
from A_ASSD import CO

from Noyau.N__F import _F

from Noyau.N_Exception import AsException
from Noyau.N_utils import AsType

#from Noyau.N_VALIDATOR import Valid,RangeVal,OrdList,NoRepeat,LongStr,EnumVal,CardVal,TypeVal,InstanceVal,OrVal,AndVal
from A_VALIDATOR import OrdList,NoRepeat,LongStr,OrVal,AndVal
from A_VALIDATOR import RangeVal, EnumVal, TypeVal, PairVal
from A_VALIDATOR import CardVal, InstanceVal

# On remplace la factory des validateurs initialement dans Noyau par celle
# de A_VALIDATOR
import A_VALIDATOR
import Noyau.N_ENTITE
Noyau.N_ENTITE.ENTITE.factories['validator']=A_VALIDATOR.validatorFactory


from Extensions.niveau import NIVEAU
from Extensions.etape_niveau import ETAPE_NIVEAU
from Extensions.commentaire import COMMENTAIRE
from Extensions.parametre import PARAMETRE  
from Extensions.parametre_eval import PARAMETRE_EVAL
from Extensions.commande_comm import COMMANDE_COMM 
from Extensions.mcnuplet import MCNUPLET

