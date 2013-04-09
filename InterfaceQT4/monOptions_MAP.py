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

import os, re, sys

from PyQt4.QtGui  import *
from PyQt4.QtCore import *

from OptionsMAP import Ui_desOptions


class desOptions(Ui_desOptions,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.setupUi(self)
       self.setModal(modal)

class Options(desOptions):
   def __init__(self,parent = None,modal = 0,configuration=None):
       desOptions.__init__(self,parent,modal)
       self.configuration=configuration
       self.viewMan=parent
       self.dVersion={}
       self.dRepCat={}
       self.connecterSignaux()
       self.code='MAP'
       self.initAll()
  
   def connecterSignaux(self) :
       self.connect(self.CBVersions,SIGNAL("activated(int)"),self.VersionChoisie)
       self.connect(self.Bdefaut,SIGNAL("clicked()"),self.BdefautChecked)
       self.connect(self.LEVersionAjout,SIGNAL("returnPressed()"),self.AjoutVersion)
       self.connect(self.PBajout,SIGNAL("clicked()"),self.AjoutVersion)
       self.connect(self.LEVersionSup,SIGNAL("returnPressed()"),self.SupVersion)
       self.connect(self.PBSup,SIGNAL("clicked()"),self.SupVersion)
       self.connect(self.LERepDoc,SIGNAL("returnPressed()"),self.ChangePathDoc)
       self.connect(self.LERepOT,SIGNAL("returnPressed()"),self.ChangePathOT)
       self.connect(self.LERepMAP,SIGNAL("returnPressed()"),self.ChangePathMAP)
       self.connect(self.LERepAster,SIGNAL("returnPressed()"),self.ChangePathAster)
       self.connect(self.LERepCata,SIGNAL("returnPressed()"),self.BokClicked)
       self.connect(self.LESaveDir,SIGNAL("returnPressed()"),self.ChangeSaveDir)
       self.connect(self.Bok,SIGNAL("clicked()"),self.BokClicked)
       self.connect(self.PBQuit,SIGNAL("clicked()"),self.close)


   def initAll(self):
       self.CBVersions.clear()
       for item in self.configuration.catalogues :
           (code,ssCode,cata,formatOut,formatIn)=item
           self.dVersion[ssCode]=(item)
           self.dRepCat[ssCode]=str(cata)
           self.CBVersions.addItem(QString(ssCode))
       self.LERepCata.setText(self.dRepCat[str(self.CBVersions.currentText())])

       if hasattr(self.configuration,"path_doc"):
          self.LERepDoc.setText(self.configuration.path_doc)
       if hasattr(self.configuration,"OpenTURNS_path"):
          self.LERepOT.setText(self.configuration.OpenTURNS_path)
       if hasattr(self.configuration,"savedir"):
          self.LESaveDir.setText(self.configuration.savedir)
       if hasattr(self.configuration,"PATH_MAP"):
          self.LERepMAP.setText(self.configuration.PATH_MAP)
       if hasattr(self.configuration,"PATH_ASTER"):
          self.LERepAster.setText(self.configuration.PATH_ASTER)

   def ChangePathMAP(self):
       if self.LERepMAP.text()=="" : return
       if not os.path.isdir(self.LERepMAP.text()) :
          res = QMessageBox.warning( None,
                 self.trUtf8("Repertoire MAP "),
                 self.trUtf8("Le Repertoire n existe pas."),
                 self.trUtf8("&Ok"),
                 self.trUtf8("&Abandonner"))
          if res == 1 :
             if hasattr(self.configuration,"PATH_MAP"):
                self.LERepAster.setText(self.configuration.PATH_MAP)
             return
       self.configuration.PATH_MAP=str(self.LERepMAP.text())
       self.configuration.PATH_PYGMEE=self.configuration.PATH_MAP+"/components/pygmee_v2"
       self.configuration.PATH_BENHUR=self.configuration.PATH_MAP+"/components/benhur"
       self.configuration.PATH_FDVGRID=self.configuration.PATH_MAP+"components/fdvgrid/ther2d/bin"
       self.configuration.PATH_MODULE=self.configuration.PATH_MODULE+"components/fdvgrid/ther2d/bin"
       self.configuration.save_params()

   def VersionChoisie(self):
       version=str(self.CBVersions.currentText())
       pass

   def ChangePathAster(self):
       if self.LERepAster.text()=="" : return
       if not os.path.isdir(self.LERepAster.text()) :
          res = QMessageBox.warning( None,
                 self.trUtf8("Repertoire Aster "),
                 self.trUtf8("Le Repertoire n existe pas."),
                 self.trUtf8("&Ok"),
                 self.trUtf8("&Abandonner"))
          if res == 1 :
             if hasattr(self.configuration,"PATH_ASTER"):
                self.LERepAster.setText(self.configuration.PATH_ASTER)
             return
       self.configuration.PATH_ASTER=str(self.LERepAster.text())
       self.configuration.save_params()

   def VersionChoisie(self):
       version=str(self.CBVersions.currentText())
       if self.dRepCat.has_key(version):
          self.LERepCata.setText(self.dRepCat[version])

   def BokClicked(self):
       version=str(self.CBVersions.currentText())
       if self.LERepCata.text() == "" :
          QMessageBox.critical( self, "Champ non rempli","Le champ Catalogue  doit etre rempli" )
          return
       if not os.path.isfile(self.LERepCata.text()) :
          res = QMessageBox.warning( None,
                 self.trUtf8("Fichier Catalogue "),
                 self.trUtf8("Le Fichier n existe pas. Voulez-vous supprimer cette version ?"),
                 self.trUtf8("&Oui"),
                 self.trUtf8("&Non"))
          if res == 0 :
             self.LEVersionSup.setText(version)
             self.SupVersion()
             return

       self.dRepCat[version]=str(self.LERepCata.text())
       if version in self.dVersion.keys():
          item=list(self.dVersion[version])
          item[2]=self.dRepCat[version]
          self.dVersion[version]=tuple(item)
       else :
          self.dVersion[version]=(self.code,version,self.dRepCat[version],self.code.lower())
          
       lItem=[]
       for version in self.dVersion.keys() :
          lItem.append(self.dVersion[version])
       self.configuration.catalogues=lItem
       self.configuration.save_params()

   def AjoutVersion(self):
       version=self.LEVersionAjout.text()
       if str(version) == "" : return
       self.CBVersions.addItem(version)
       self.LERepCata.setText("")
       self.LEVersionAjout.setText("")
       self.CBVersions.setCurrentIndex(self.CBVersions.count()-1)

   def SupVersion(self):
       version=str(self.LEVersionSup.text())
       if version == "" : return
       i =0
       while i < self.CBVersions.count() :
           if  self.CBVersions.itemText(i) == version :
               self.CBVersions.removeItem(i)
               break
           i=i+1
       try :
          del self.dVersion[version]
          del self.dRepCat[version]
       except :
          self.LEVersionSup.setText("")
          try :
             self.CBVersions.setCurrentIndex(self.CBVersions.count()-1)
             self.VersionChoisie()
          except :
             pass
          return
       codeSansPoint=re.sub("\.","",version)
       chaine="rep_mat_"+codeSansPoint
       if hasattr(self.configuration,chaine):
          delattr(self.configuration,chaine)
       self.LEVersionSup.setText("")

       lItem=[]
       for version in self.dVersion.keys() :
           lItem.append(self.dVersion[version])
       self.LERepCata.setText("")
       self.configuration.catalogues=lItem
       self.configuration.save_params()
       self.CBVersions.setCurrentIndex(0)
       self.VersionChoisie()


   def BdefautChecked(self):
       res = QMessageBox.warning( None,
                 self.trUtf8("Restauration des parametres par defaut "),
                 self.trUtf8("Votre fichier editeur sera ecrase."),
                 self.trUtf8("&Ok"),
                 self.trUtf8("&Abandonner"))
       self.Bdefaut.setCheckState(Qt.Unchecked)
       if res == 1 : return 

       appli=self.configuration.appli
       fic_ini_util=self.configuration.fic_ini_utilisateur
       old_fic_ini_util=fic_ini_util+"_old"
       commande="mv "+fic_ini_util+" "+old_fic_ini_util
       os.system(commande)
       name='prefs_'+self.code
       prefsCode=__import__(name)
       nameConf='configuration_'+prefs.code
       configuration=__import__(nameConf)

       configNew=configuration.CONFIG(appli,prefsCode.repIni)
       self.configuration=configNew
       appli.CONFIGURATION=configNew
       self.configuration.save_params()
       self.dVersion={}
       self.dRepCat={}
       self.initAll()

   def ChangePathDoc(self):
       if self.LERepDoc.text()=="" : return
       if not os.path.isdir(self.LERepDoc.text()) :
          res = QMessageBox.warning( None,
                 self.trUtf8("Repertoire de Documentation "),
                 self.trUtf8("Le Repertoire  n existe pas."),
                 self.trUtf8("&Ok"),
                 self.trUtf8("&Abandonner"))
          if res == 1 :
             if hasattr(self.configuration,"path_doc"):
                self.LERepDoc.setText(self.configuration.path_doc)
             return

       self.configuration.path_doc=str(self.LERepDoc.text())
       self.configuration.save_params()

   def ChangePathOT(self):
       if not os.path.isdir(self.LERepOT.text()) :
          res = QMessageBox.warning( None,
                 self.trUtf8("Repertoire Open TURNS "),
                 self.trUtf8("Le Repertoire  n existe pas."),
                 self.trUtf8("&Ok"),
                 self.trUtf8("&Abandonner"))
          if res == 1 :
             if hasattr(self.configuration,"OpenTURNS_path"):
                self.LERepOT.setText(self.configuration.OpenTURNS_path)
             return

       if hasattr(self.configuration,"OpenTURNS_path"):
          sys.path.remove(self.configuration.OpenTURNS_path)
       self.configuration.OpenTURNS_path=str(self.LERepOT.text())
       self.configuration.save_params()
       if self.configuration.OpenTURNS_path == "" : return
       sys.path[:0]=[self.configuration.OpenTURNS_path]

   def ChangeSaveDir(self):
       if not os.path.isdir(self.LESaveDir.text()) :
          res = QMessageBox.warning( None,
                 self.trUtf8("Repertoire Open TURNS "),
                 self.trUtf8("Le Repertoire  n existe pas."),
                 self.trUtf8("&Ok"),
                 self.trUtf8("&Abandonner"))
          if res == 1 :
             if hasattr(self.configuration,"savedir"):
                self.LESaveDir.setText(self.configuration.savedir)
       self.configuration.savedir=str(self.LESaveDir.text())
       self.configuration.save_params()

