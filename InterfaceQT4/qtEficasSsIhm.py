# -*- coding: iso-8859-1 -*-
# Copyright (C) 2007-2017   EDF R&D
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

from __future__ import absolute_import
from __future__ import print_function
try :
   from builtins import str
except : pass

import os, sys
import six

from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException
from Extensions import param2
from InterfaceQT4.viewManagerSsIhm import MyTabviewSsIhm


from InterfaceQT4.getVersion import getEficasVersion

from editorSsIhm import JDCEditorSsIhm


class AppliSsIhm:
    """
    Class implementing the main user interface.
    """
    def __init__(self,code=None,salome=1,parent=None,ssCode=None,multi=False,langue='fr',ssIhm=True,versionCode=None):
        """
        Constructor
        """
        version=getEficasVersion()
        self.VERSION_EFICAS="Eficas QT5 Salome " + version
        self.version_code=versionCode

        self.salome=salome
        self.ssIhm=True
        self.code=code

        self.dict_reels={}
        self.fichierIn=None
        self.fichierOut=None

        self.recent =  []
        self.ficRecents={}
        self.mesScripts={}
        self.listeAEnlever=[]
        self.ListePathCode=['Adao','ADAO','Carmel3D','Telemac','CF','MAP','ZCracks', 'SEP','SPECA','PSEN_Eficas','PSEN_N1']
        self.listeCode=['Adao','ADAO','Carmel3D','Telemac','CF','MAP','ZCracks', 'SEP','SPECA','PSEN_Eficas','PSEN_N1']
        self.repIcon=os.path.join( os.path.dirname(os.path.abspath(__file__)),'..','Editeur','icons')

        if self.salome:
          import Accas
          try :
            import eficasSalome
            Accas.SalomeEntry = eficasSalome.SalomeEntry
          except : 
            print ('eficas hors salome')

        self.multi=multi
        self.demande=multi # specifique PSEN

        if langue=='fr': self.langue=langue
        else           : self.langue="ang"

        if self.multi == False :
             self.definitCode(code,ssCode)
             if code==None: return

        self.suiteTelemac=False
        self.viewmanager = MyTabviewSsIhm(self)


    def definitCode(self,code,ssCode) :
        self.code=code
        self.ssCode=ssCode
        if self.code == None:return # pour le cancel de la fenetre choix code

        name='prefs_'+self.code
        prefsCode=__import__(name)

        self.repIni=prefsCode.repIni
        if ssCode != None :
           self.format_fichier= ssCode  #par defaut
           prefsCode.NAME_SCHEME=ssCode
        else :
           self.format_fichier="python" #par defaut

        nameConf='configuration_'+self.code
        configuration=__import__(nameConf)
        self.CONFIGURATION = configuration.make_config(self,prefsCode.repIni)
        self.CONFIGStyle = None
        if hasattr(configuration,'make_config_style'):
           self.CONFIGStyle = configuration.make_config_style(self,prefsCode.repIni)


        
    def fileNew(self):
        self.viewmanager.newEditor()

    def fileOpen(self,fichier):
        self.viewmanager.handleOpen(fichier)

    def fileSave(self):
        return self.viewmanager.saveCurrentEditor()

    def fileSaveAs(self,fichier):
        return self.viewmanager.saveAsCurrentEditor(fichier)

    def fileClose(self):
        self.viewmanager.handleClose()

    def jdcRapport(self):
        return self.viewmanager.jdcRapport()

    def jdcText(self):
        return self.viewmanager.jdcText()

    def jdcDico(self):
        return self.viewmanager.jdcDico()

    def jdcDicoPython(self):
        return self.viewmanager.jdcDicoPython()

    def getSource(self,file):
    # appele par Editeur/session.py
    # a garder pour les poursuites
    # le format n est pas le meme que celui de la fonction jdcText
        import convert
        p=convert.plugins['python']()
        p.readfile(file)
        texte=p.convert('execnoparseur')
        return texte

if __name__=='__main__':

    # Modules Eficas
    monEficas= AppliSsIhm(code='Adao',salome=0,versionCode='V83')
