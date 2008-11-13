# -*- coding: utf-8 -*-

import os, re

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
       #print "Options"
       desOptions.__init__(self,parent,modal)
       self.configuration=configuration
       self.viewMan=parent
       self.dVersion={}
       self.dRepMat={}
       self.dRepCat={}
       self.connecterSignaux()
       self.initAll()
  
   def connecterSignaux(self) :
       self.connect(self.CBVersions,SIGNAL("activated(int)"),self.VersionChoisie)
       self.connect(self.Bdefaut,SIGNAL("clicked()"),self.BdefautChecked)
       self.connect(self.LEVersionAjout,SIGNAL("returnPressed()"),self.AjoutVersion)
       self.connect(self.LERepDoc,SIGNAL("returnPressed()"),self.ChangePathDoc)
       self.connect(self.Bok,SIGNAL("clicked()"),self.BokClicked)
       self.connect(self.LEVersionSup,SIGNAL("returnPressed()"),self.SupVersion)
       self.connect(self.PBajout,SIGNAL("clicked()"),self.AjoutVersion)
       self.connect(self.PBSup,SIGNAL("clicked()"),self.SupVersion)
       self.connect(self.PBQuit,SIGNAL("clicked()"),self.close)
       self.connect(self.LERepDoc,SIGNAL("textChanged(const QString&)"),self.ChangePathDoc)


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
       self.LERepMat.setText(self.dRepMat[version])
       self.LERepCata.setText(self.dRepCat[version])
       if hasattr(self.configuration,"path_doc"):
          self.LERepDoc.setText(self.configuration.path_doc)

        
   def VersionChoisie(self):
       version=str(self.CBVersions.currentText())
       if self.dRepMat.has_key(version):
          self.LERepMat.setText(self.dRepMat[version])
       if self.dRepCat.has_key(version):
          self.LERepCata.setText(self.dRepCat[version])

   def BokClicked(self):
       version=str(self.CBVersions.currentText())
       if self.LERepCata.text() == "" :
          QMessageBox.critical( self, "Champ non rempli","Le champs Catalogue  doit etre rempli" )
          return

       self.dRepMat[version]=self.LERepMat.text()
       if str(self.dRepMat[version] != "") != "" :
          codeSansPoint=re.sub("\.","",version)
          chaine="rep_mat_"+codeSansPoint
          setattr(self.configuration,chaine,self.dRepMat[version])

       self.dRepCat[version]=str(self.LERepCata.text())
       if version in self.dVersion.keys():
          item=list(self.dVersion[version])
          item[2]=self.dRepCat[version]
          self.dVersion[version]=tuple(item)
       else :
          self.dVersion[version]=('ASTER',version,self.dRepCat[version],'python')
          
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
                 self.trUtf8("Restauration des parametres par defaut "),
                 self.trUtf8("Votre fichier editeur sera ecrase."),
                 self.trUtf8("&Ok"),
                 self.trUtf8("&Abandonner"))
       self.Bdefaut.setState(QButton.Off)
       if res == 1 : return 

       appli=self.configuration.appli
       rep_ini=self.configuration.rep_ini
       fic_ini_util=self.configuration.fic_ini_utilisateur
       old_fic_ini_util=fic_ini_util+"_old"
       commande="mv "+fic_ini_util+" "+old_fic_ini_util
       os.system(commande)
       from Editeur import configuration
       configNew=configuration.CONFIG(appli,rep_ini)
       self.configuration=configNew
       appli.CONFIGURATION=configNew
       self.configuration.save_params()
       self.dVersion={}
       self.dRepMat={}
       self.dRepCat={}
       self.initAll()

   def ChangePathDoc(self):
       self.configuration.path_doc=str(self.LERepDoc.text())
       self.configuration.save_params()

