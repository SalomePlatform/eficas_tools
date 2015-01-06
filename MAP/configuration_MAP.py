# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
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
      configuration.CONFIG_BASE.__init__(self,appli,repIni)
  
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



