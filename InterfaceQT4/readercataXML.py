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
    Ce module sert a lire un catalogue et a construire
    un objet CataItem pour Eficas.
    Il s'appuie sur la classe READERCATA
"""
# Modules Python
import sys, os
import autre_analyse_cata


# Modules Eficas

from monChoixCata import MonChoixCata
from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException
import uiinfo
from Efi2Xsd import readerEfiXsd
# ATtention pas teste depuis le chgt de nom

from readercata import ReaderCataCommun

class ReaderCata (ReaderCataCommun):

   def __init__(self,QWParent, appliEficas):
      self.QWParent=QWParent
      self.appliEficas=appliEficas
      self.VERSION_EFICAS=self.appliEficas.VERSION_EFICAS
      self.code=self.appliEficas.code
      self.ssCode=self.appliEficas.ssCode
      self.appliEficas.format_fichier='python'
      self.appliEficas.format_fichier_in ='xml'
      self.modeNouvCommande=self.appliEficas.maConfiguration.modeNouvCommande
      self.versionCode=self.appliEficas.versionCode
      self.version_cata=None
      self.fic_cata=None
      self.OpenCata()
      self.cataitem=None
      self.titre='Eficas XML'
      self.Ordre_Des_Commandes=None
      self.Classement_Commandes_Ds_Arbre=()
      self.demandeCatalogue=False

      #self.traiteIcones()
      #self.creeDicoInverse()


   def OpenCata(self):

      #self.fic_cata = 'Cata_MED_FAM.xml'
      #xml = open('/home/A96028/QT5GitEficasTravail/eficas/Med/Cata_MED_FAM.xml').read()
      #xml = open('/home/A96028/QT5GitEficasTravail/eficas/CataTestXSD/cata_test1.xml').read()
      self.choisitCata()
      xml=open(self.fic_cata).read()
      SchemaMed = readerEfiXsd.efficas.CreateFromDocument(xml)
      SchemaMed.exploreCata() 
      self.cata=SchemaMed
      uiinfo.traite_UIinfo(self.cata)
      self.Commandes_Ordre_Catalogue=[]
      self.cata_ordonne_dico,self.appliEficas.liste_simp_reel=autre_analyse_cata.analyseCatalogue(self.cata)
      self.liste_groupes=None

   def dumpToXml(self):
      # pour compatibilite
       pass
