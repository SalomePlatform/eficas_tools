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
    Ce module sert pour charger les parametres de configuration d'EFICAS
"""
# Modules Python
import os
import sys
import configuration

# Modules Eficas
from Editeur import utils

class CONFIG(configuration.CONFIG_BASE):

  #-----------------------------------
  def __init__(self,appli,repIni):
  #-----------------------------------
      self.ssCode=appli.ssCode
      self.INSTALLDIR =os.path.dirname(__file__)

      self.labels_user=['exec_acrobat','savedir','path_doc']
      self.labels_eficas=['exec_acrobat','savedir','path_doc','catalogues']

      #self.cataFile="catalogues_MAP.ini"
      configuration.CONFIG_BASE.__init__(self,appli,repIni,'.Eficas_MAP')
  
  def make_ssCode(self,ssCode):
      if ssCode == None : return
      try :
        name='prefs_'+ssCode
        prefs_ssCode=__import__(name)
        prefs_ssCode.ajout(self)
      except :
       pass
       

def make_config(appli,rep):
    return CONFIG(appli,rep)



