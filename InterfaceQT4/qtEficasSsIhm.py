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

from Extensions.eficas_exception import EficasException
from Extensions import param2

from InterfaceQT4.getVersion import getEficasVersion
from InterfaceQT4.viewManagerSsIhm import MyViewManagerSsIhm
#from editorSsIhm import JDCEditorSsIhm


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
        self.versionCode=versionCode

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
        if self.multi : 
              print ('pas de multi sans ihm')


        if langue=='fr': self.langue=langue
        else           : self.langue="ang"

        if self.multi == False :
             self.definitCode(code,ssCode)
             if code==None: return

        self.suiteTelemac=False
        self.viewmanager=MyViewManagerSsIhm(self)


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
        self.maConfiguration = configuration.make_config(self,prefsCode.repIni)

        if hasattr (self,'maConfiguration') and self.maConfiguration.translatorFichier :
           from Extensions import localisation
           localisation.localise(None,self.langue,translatorFichier=self.maConfiguration.translatorFichier)


    def getSource(self,file):
    # appele par Editeur/session.py
        import convert
        p=convert.plugins['python']()
        p.readfile(file)
        texte=p.convert('execnoparseur')
        return texte


    def initEditor(self,fichier = None,jdc = None, units = None,include=0):
        if self.editor != None : 
           print ('un seul editeur par appli')
           sys.Exit()
        self.editor = JDCEditorSsIhm(self,fichier, jdc, self.myQtab,units=units,include=include)
        

    def fileNew(self):
        self.editor=initEditor(self)

    def getEditor(self):
        return self.editor

    def fileOpen(self,fichier):
        fichierIn = os.path.abspath(six.text_type(fichier))
        try:
            monEditor=self.viewmanager.handleOpen(fichierIn)
        except EficasException as exc:
            print ('poum')
            monEditor=None
        return monEditor

    def fileSave(self):
        if self.editor == None : return False
        ok, newName = editor.saveFileAs()
        print ('ok, newName ',ok, newName)

    def fileSaveAs(self,fileName):
        if self.editor == None : return False
        ok = editor.saveFileAs()
        print ('ok ',ok)

    def dumpXsd(self):
        current_cata    = CONTEXT.getCurrentCata()
        current_cata.dumpXsd()
        if self.maConfiguration.afficheIhm==False : exit()

#,self.fileSaveAs
#,self.fileClose
#,self.fileExit
#,self.jdcRapport
#,self.jdcRegles
#,self.jdcFichierSource
#,self.visuJdcPy
       


if __name__=='__main__':

    # Modules Eficas
    monEficas= AppliSsIhm(code='Adao',salome=0,versionCode='V83')
