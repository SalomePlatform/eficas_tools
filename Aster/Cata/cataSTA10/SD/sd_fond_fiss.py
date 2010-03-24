#@ MODIF sd_fond_fiss SD  DATE 08/01/2008   AUTEUR MACOCCO K.MACOCCO 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2007  EDF R&D                  WWW.CODE-ASTER.ORG
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
# ======================================================================

from SD import *

class sd_fond_fiss(AsBase):
    nomj = SDNom(fin=8)
    LEVREINF___MAIL = Facultatif(AsVK8(SDNom(nomj='.LEVREINF  .MAIL'), ))
    NORMALE = Facultatif(AsVR(lonmax=3, ))
    FOND_______TYPE = AsVK8(SDNom(nomj='.FOND      .TYPE'), lonmax=1, )
    FOND_______NOEU = AsVK8(SDNom(nomj='.FOND      .NOEU'), )
    FONDSUP____NOEU = Facultatif(AsVK8(SDNom(nomj='.FOND_SUP  .NOEU'), ))
    FONDINF____NOEU = Facultatif(AsVK8(SDNom(nomj='.FOND_INF  .NOEU'), ))
    DTAN_EXTREMITE = Facultatif(AsVR(lonmax=3, ))
    INFNORM____NOEU = Facultatif(AsVK8(SDNom(nomj='.INFNORM   .NOEU'), ))
    DTAN_ORIGINE = Facultatif(AsVR(lonmax=3, ))
    SUPNORM____NOEU = Facultatif(AsVK8(SDNom(nomj='.SUPNORM   .NOEU'), ))
    LEVRESUP___MAIL = Facultatif(AsVK8(SDNom(nomj='.LEVRESUP  .MAIL'), ))

