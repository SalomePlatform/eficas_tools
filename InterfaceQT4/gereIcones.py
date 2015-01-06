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
# Modules Python
import string,types,os,re
import traceback

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
listeSuffixe=('bmp','png','jpg' ,'txt','med')


class FacultatifOuOptionnel:

  def setReglesEtAide(self):
      from monWidgetCommande import MonWidgetCommande
      listeRegles=()
      try :
         listeRegles     = self.node.item.get_regles()
      except :
         pass
      if listeRegles==() and hasattr(self,"RBRegle"): self.RBRegle.close() 
      if isinstance(self,MonWidgetCommande):return
      cle_doc = self.node.item.get_docu()
      if cle_doc == None and hasattr(self,"RBInfo") : self.RBInfo.close()


 
  def setPoubelle(self):
      if not(hasattr(self,"RBPoubelle")):return
      if self.node.item.object.isoblig() : 
         icon1 = QtGui.QIcon()
         icon1.addPixmap(QtGui.QPixmap("/home/A96028/Install_EficasV1/KarineEficas/Editeur/icons/deleteRondVide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
         self.RBPoubelle.setIcon(icon1)
         return
      self.RBPoubelle.show()
      self.connect(self.RBPoubelle,SIGNAL("clicked()"),self.aDetruire)

  def aDetruire(self):
      self.node.delete()
      # Cas du mono-commande
      if self.parentQt == None : self.afficheCatalogue()
      else : self.parentQt.reaffiche()

  def setValide(self):
      if not(hasattr (self,'RBValide')) : return
      icon = QIcon()
      if self.node.item.object.isvalid() : 
         icon=QIcon(self.repIcon+"/ast-green-ball.png")
      else :
         icon=QIcon(self.repIcon+"/ast-red-ball.png")
      self.RBValide.setIcon(icon)



class ContientIcones:

  def BFichierVisu(self):
       fichier=self.lineEditVal.text()
       if fichier == None or str(fichier)=="" : return
       from qtCommun import ViewText
       try :
         cmd="xdg-open "+str(fichier)
         os.system(cmd)
       except:
         try :
            fp=open(fichier)
            txt=fp.read()
            nomFichier=QFileInfo(fichier).baseName()
            maVue=ViewText(self,entete=nomFichier)
            maVue.setText(txt)
            maVue.show()
            fp.close()
         except:
            QMessageBox.warning( None,
                       tr("Visualisation Fichier "),
                       tr("Impossibilite d'afficher le Fichier"),)

  def BFichierPressed(self):
      mctype = self.node.item.get_definition().type
      if len(mctype) > 1:
          filters = mctype[1]
      elif hasattr(mctype[0], "filters"):
          filters = mctype[0].filters
      else:
          filters = QString()
      if len(mctype) > 2 and mctype[2] == "Sauvegarde":
          fichier = QFileDialog.getSaveFileName(self.appliEficas,
                              tr('Sauvegarder Fichier'),
                              self.appliEficas.CONFIGURATION.savedir,
                              filters)
      else:
          fichier = QFileDialog.getOpenFileName(self.appliEficas,
                              tr('Ouvrir Fichier'),
                              self.appliEficas.CONFIGURATION.savedir,
                              filters)

      if not(fichier.isNull()):
         ulfile = os.path.abspath(unicode(fichier))
         self.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
         self.lineEditVal.setText(fichier)
         self.editor.affiche_infos(tr("Fichier selectionne"))
         self.LEValeurPressed()
         if (QFileInfo(fichier).suffix() in listeSuffixe ):
             self.image=fichier
             if (not hasattr(self,"BSelectInFile")):
               self.BSelectInFile = QPushButton(self.Widget8)
               self.BSelectInFile.setMinimumSize(QSize(140,40))
               self.BSelectInFile.setObjectName("BSelectInFile")
               self.gridLayout.addWidget(self.BSelectInFile,1,1,1,1)
               self.BSelectInFile.setText(tr("Selection"))
               self.connect(self.BSelectInFile,SIGNAL("clicked()"),self.BSelectInFilePressed)
             else :
               self.BSelectInFile.setVisible(1)
         elif hasattr(self, "BSelectInFile"):
             self.BSelectInFile.setVisible(0)

  def BRepertoirePressed(self):
      directory = QFileDialog.getExistingDirectory(self.appliEficas,
            directory = self.appliEficas.CONFIGURATION.savedir,
            options = QFileDialog.ShowDirsOnly)

      if not directory.isNull():
         absdir = os.path.abspath(unicode(directory))
         self.appliEficas.CONFIGURATION.savedir = os.path.dirname(absdir)
         self.lineEditVal.setText(directory)
         self.LEValeurPressed()

  def BSelectInFilePressed(self):
      from monSelectImage import MonSelectImage
      MonSelectImage(file=self.image,parent=self).show()

          

  def BSalomePressed(self):
        self.editor.affiche_infos(QString(""))
        selection=[]
        commentaire=""
        genea=self.node.item.get_genealogie()
        kwType = self.node.item.get_definition().type[0]
        for e in genea:
            if "GROUP_NO" in e: kwType = "GROUP_NO"
            if "GROUP_MA" in e: kwType = "GROUP_MA"

        if 'grno' in repr(kwType): kwType = "GROUP_NO"
        if 'grma' in repr(kwType): kwType = "GROUP_NO"

        if kwType in ("GROUP_NO","GROUP_MA"):
           selection, commentaire = self.appliEficas.selectGroupFromSalome(kwType,editor=self.editor)

        mc = self.node.item.get_definition()

        if  (isinstance(mc.type,types.TupleType) and len(mc.type) > 1 and "(*.med)" in mc.type[1] ):
           selection, commentaire = self.appliEficas.selectMeshFile(editor=self.editor)
           print selection, commentaire
           if commentaire != "" : 
                  QMessageBox.warning( None,
                  tr("Export Med vers Fichier "),
                  tr("Impossibilite d exporter le Fichier"),)
                  return
           else :
                  self.lineEditVal.setText(QString(selection))
                  return

        from Accas import SalomeEntry
        if isinstance(kwType, types.ClassType) and issubclass(kwType, SalomeEntry):
           selection, commentaire = self.appliEficas.selectEntryFromSalome(kwType,editor=self.editor)

        if commentaire !="" :
            self.editor.affiche_infos(tr(QString(commentaire)))
        monTexte=""
        if selection == [] : return
        for geomElt in selection:
            monTexte=geomElt+","
        monTexte= monTexte[0:-1]
        self.lineEditVal.setText(QString(monTexte))

  def BView2DPressed(self):
        valeur=self.lineEditVal.text()
        if valeur == QString("") : return
        valeur = str(valeur)
        if valeur :
           ok, msgError = self.appliEficas.displayShape(valeur)
           if not ok:
              self.appliEficas.affiche_infos(msgError,Qt.red)

  def BParametresPressed(self):
        liste=self.node.item.get_liste_param_possible()
        from monListeParamPanel import MonListeParamPanel
        MonListeParamPanel(liste=liste,parent=self).show()

