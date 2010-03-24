#@ MODIF co_mater SD  DATE 30/06/2009   AUTEUR COURTOIS M.COURTOIS 
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

import Accas
from SD import *
from sd_mater import sd_mater

# -----------------------------------------------------------------------------
class mater_sdaster(ASSD, sd_mater):
   def RCVALE(self, phenomene, nompar=(), valpar=(), nomres=(), stop='F'):
      """Appel � la routine fortran RCVALE pour r�cup�rer les valeurs des
      propri�t�s du mat�riau.
      """
      if not self.accessible():
         raise Accas.AsException("Erreur dans mater.RCVALE en PAR_LOT='OUI'")
      from Utilitai.Utmess import UTMESS
      # v�rification des arguments
      if not type(nompar) in (list, tuple):
         nompar = [nompar,]
      if not type(valpar) in (list, tuple):
         valpar = [valpar,]
      if not type(nomres) in (list, tuple):
         nomres = [nomres,]
      nompar = tuple(nompar)
      valpar = tuple(valpar)
      nomres = tuple(nomres)
      if len(nompar) != len(valpar):
         vk1=', '.join(nompar)
         vk2=', '.join([repr(v) for v in valpar])
         UTMESS('F','SDVERI_4',valk=[vk1,vk2])
      if len(nomres) < 1:
         UTMESS('F', 'SDVERI_5')
      # appel � l'interface Python/C
      return aster.rcvale(self.nom, phenomene, nompar, valpar, nomres, stop)

