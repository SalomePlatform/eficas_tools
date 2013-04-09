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

import os, re
from Extensions.i18n import tr

from PyQt4.QtGui  import *
from PyQt4.QtCore import *

from OptionsEditeur import Ui_desOptions


class desOptions(Ui_desOptions,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.setupUi(self)
       self.setModal(modal)

class Options(desOptions):
   def __init__(self,parent = None,modal = 0,configuration=None):
       self.code='ASTER'
       desOptions.__init__(self,parent,modal)
       self.configuration=configuration
       self.dVersion={}
       self.dRepMat={}
       self.dRepCat={}
       self.dRepDoc={}
       self.connecterSignaux()
       self.initAll()
  
   def connecterSignaux(self) :
       self.connect(self.CBVersions,SIGNAL("activated(int)"),self.VersionChoisie)
       self.connect(self.Bdefaut,SIGNAL("clicked()"),self.BdefautChecked)
       self.connect(self.LEVersionAjout,SIGNAL("returnPressed()"),self.AjoutVersion)
       self.connect(self.LERepSaveDir,SIGNAL("returnPressed()"),self.ChangeSaveDir)
       self.connect(self.Bok,SIGNAL("clicked()"),self.BokClicked)
       self.connect(self.LEVersionSup,SIGNAL("returnPressed()"),self.SupVersion)
       self.connect(self.PBajout,SIGNAL("clicked()"),self.AjoutVersion)
       self.connect(self.PBSup,SIGNAL("clicked()"),self.SupVersion)
       self.connect(self.PBQuit,SIGNAL("clicked()"),self.close)


   def initAll(self):
       self.CBVersions.clear()
       for item in self.configuration.catalogues :
           try :
              (code,version,cata,format,defaut)=item
           except :
              (code,version,cata,format)=item
           self.dVersion[version]=(item)
           self.dRepCat[version]=str(cata)
           self.CBVersions.addItem(QString(version))

           codeSansPoint=re.sub("\.","",version)
           chaine="rep_mat_"+codeSansPoint
           if hasattr(self.configuration,chaine):
              rep_mat=getattr(self.configuration,chaine)
              self.dRepMat[version]=str(rep_mat)
           else :
              self.dRepMat[version]=""
           chaine="rep_doc_"+codeSansPoint
           if hasattr(self.configuration,chaine):
              rep_doc=getattr(self.configuration,chaine)
              self.dRepDoc[version]=str(rep_doc)
           else :
              self.dRepDoc[version]=""
       version=str(self.CBVersions.itemText(0))
       
       self.LERepMat.setText(self.dRepMat[version])
       self.LERepCata.setText(self.dRepCat[version])
       self.LERepDoc.setText(self.dRepDoc[version])
       if hasattr(self.configuration,"savedir"):
          self.LERepSaveDir.setText(self.configuration.savedir)

        
   def VersionChoisie(self):
       version=str(self.CBVersions.currentText())
       if self.dRepMat.has_key(version):
          self.LERepMat.setText(self.dRepMat[version])
       if self.dRepCat.has_key(version):
          self.LERepCata.setText(self.dRepCat[version])
       if self.dRepDoc.has_key(version):
          self.LERepDoc.setText(self.dRepDoc[version])

   def BokClicked(self):
       version=str(self.CBVersions.currentText())
       if self.LERepCata.text() == "" :
          QMessageBox.critical( self, tr("Champ non rempli"),tr("Le champ Catalogue  doit etre rempli" ))
          return

       self.dRepMat[version]=str(self.LERepMat.text())
       if str(self.dRepMat[version] != "") != "" :
          codeSansPoint=re.sub("\.","",version)
          chaine="rep_mat_"+codeSansPoint
          try :
             ancienneValeur=getattr(self.configuration,chaine)
          except :
             ancienneValeur=''
          if ancienneValeur != self.dRepMat[version]:
             setattr(self.configuration,chaine,self.dRepMat[version])

       self.dRepCat[version]=str(self.LERepCata.text())
       if version in self.dVersion.keys():
          item=list(self.dVersion[version])
          item[2]=self.dRepCat[version]
          self.dVersion[version]=tuple(item)
       else :
          self.dVersion[version]=('ASTER',version,self.dRepCat[version],'python')
          
       self.dRepDoc[version]=str(self.LERepDoc.text())
       if str(self.dRepDoc[version] != "") != "" :
          codeSansPoint=re.sub("\.","",version)
          chaine="rep_doc_"+codeSansPoint
          try :
             ancienneValeur=getattr(self.configuration,chaine)
          except :
             ancienneValeur=''
          if ancienneValeur != self.dRepDoc[version]:
             setattr(self.configuration,chaine,self.dRepDoc[version])

       lItem=[]
       for version in self.dVersion.keys() :
          lItem.append(self.dVersion[version])
       self.configuration.catalogues=lItem
       self.configuration.save_params()

   def AjoutVersion(self):
       version=self.LEVersionAjout.text()
       if str(version) == "" : return
       self.CBVersions.addItem(version)
       self.LERepMat.setText("")
       self.LERepCata.setText("")
       self.LERepCata.setText("")
       self.dRepDoc[version]=""
       self.LERepDoc.setText("")
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
          del self.dRepMat[version]
          del self.dRepCat[version]
       except :
          self.LEVersionSup.setText("")
          return
       codeSansPoint=re.sub("\.","",version)
       chaine="rep_mat_"+codeSansPoint
       if hasattr(self.configuration,chaine):
          delattr(self.configuration,chaine)
       self.LEVersionSup.setText("")

       lItem=[]
       for version in self.dVersion.keys() :
           lItem.append(self.dVersion[version])
       self.LERepMat.setText("")
       self.LERepCata.setText("")
       self.configuration.catalogues=lItem
       self.configuration.save_params()
       self.CBVersions.setCurrentIndex(0)
       self.VersionChoisie()


   def BdefautChecked(self):
       res = QMessageBox.warning(
                 None,
                 tr("Restauration des parametres par defaut "),
                 tr("Votre fichier editeur sera ecrase."),
                 tr("&Ok"),
                 tr("&Abandonner"))
       self.Bdefaut.setCheckState(Qt.Unchecked)
       if res == 1 : return 

       fic_ini_util=self.configuration.fic_ini_utilisateur
       old_fic_ini_util=fic_ini_util+"_old"
       commande="mv "+fic_ini_util+" "+old_fic_ini_util
       try:
         os.system(commande)
       except:
         pass
       self.configuration.setValeursParDefaut()
       self.configuration.lecture_fichier_ini_standard()
       self.configuration.lecture_fichier_ini_integrateur()
       self.configuration.save_params()
       self.dVersion={}
       self.dRepMat={}
       self.dRepCat={}
       self.initAll()


   def ChangeSaveDir(self):
       self.configuration.savedir=str(self.LERepSaveDir.text())
       self.configuration.save_params()
