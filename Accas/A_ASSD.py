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

from Ihm import I_ASSD
from Ihm import I_FONCTION
from Noyau import N_ASSD 
from Noyau import N_GEOM 
from Noyau import N_FONCTION 
from Noyau import N_CO 

# On ajoute la classe ASSD dans l'héritage multiple pour recréer 
# une hiérarchie d'héritage identique à celle de Noyau
# pour faire en sorte que isinstance(o,ASSD) marche encore après 
# dérivation

class ASSD(N_ASSD.ASSD,I_ASSD.ASSD):pass

class assd(N_ASSD.assd,I_ASSD.ASSD,ASSD):pass

class FONCTION(N_FONCTION.FONCTION,I_FONCTION.FONCTION,ASSD):
   def __init__(self,etape=None,sd=None,reg='oui'):
      N_FONCTION.FONCTION.__init__(self,etape=etape,sd=sd,reg=reg)
      I_FONCTION.FONCTION.__init__(self,etape=etape,sd=sd,reg=reg)

class fonction(N_FONCTION.fonction,I_FONCTION.fonction,ASSD):
   def __init__(self,etape=None,sd=None,reg='oui'):
      N_FONCTION.fonction.__init__(self,etape=etape,sd=sd,reg=reg)
      I_FONCTION.fonction.__init__(self,etape=etape,sd=sd,reg=reg)

class GEOM(N_GEOM.GEOM,I_ASSD.ASSD,ASSD):pass
class geom(N_GEOM.geom,I_ASSD.ASSD,ASSD):pass
class CO(N_CO.CO,I_ASSD.ASSD,ASSD):pass
