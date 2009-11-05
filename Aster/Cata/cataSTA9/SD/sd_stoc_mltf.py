#@ MODIF sd_stoc_mltf SD  DATE 13/02/2007   AUTEUR PELLET J.PELLET 
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

class sd_stoc_mltf(AsBase):
    nomj = SDNom(fin=19)
    ADNT = AsVI()
    ADPI = AsVI()
    ADRE = AsVI()
    ANCI = AsVI()
    DECA = AsVI()
    DESC = AsVI(lonmax=5,)
    FILS = AsVI()
    FRER = AsVI()
    GLOB = AsVI()
    LFRN = AsVI()
    LGBL = AsVI()
    LGSN = AsVI()
    LOCL = AsVI()
    NBAS = AsVI()
    NBLI = AsVI()
    NCBL = AsVI()
    NOUV = AsVI()
    RENU = AsVK8(lonmax=1,)
    SEQU = AsVI()
    SUPN = AsVI()