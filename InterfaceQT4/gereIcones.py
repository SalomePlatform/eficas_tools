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
      cle_doc=None
      if not hasattr(self,"RBInfo"):return
      if isinstance(self,MonWidgetCommande) and self.editor.code =="MAP":
         self.cle_doc = self.chercheDocMAP()
      else :
         self.cle_doc = self.node.item.get_docu()
      if self.cle_doc == None  : self.RBInfo.close()
      else : self.connect (self.RBInfo,SIGNAL("clicked()"),self.viewDoc)


  def chercheDocMAP(self):
      try :
        clef=self.editor.CONFIGURATION.adresse+"/"
      except :
        return None
      for k in self.editor.readercata.cata[0].JdC.dict_groupes.keys():
          if self.obj.nom in self.editor.readercata.cata[0].JdC.dict_groupes[k]:
             clef+=k
             break
      clef+="/"+ self.obj.nom[0:-5].lower()+"/spec_"+self.obj.nom[0:-5].lower()+".html"

      return clef
 
  def viewDoc(self):
      try :
          cmd="xdg-open "+self.cle_doc
          os.system(cmd)
      except:
          QMessageBox.warning( self,tr( "Aide Indisponible"),tr( "l'aide n est pas installee "))


  def setIconePoubelle(self):
      if not(hasattr(self,"RBPoubelle")):return
      icon1 = QtGui.QIcon()
      repIcon=os.path.join(os.path.abspath(os.path.dirname(__file__)),'../Editeur/icons')
      if self.node.item.object.isoblig() : 
         icon1.addPixmap(QtGui.QPixmap(repIcon+"/deleteRondVide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
         self.RBPoubelle.setIcon(icon1)
         return
      icon1.addPixmap(QtGui.QPixmap(repIcon+"/deleteRond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
      self.RBPoubelle.show()
      self.connect(self.RBPoubelle,SIGNAL("clicked()"),self.aDetruire)

  def setIconesSalome(self):
       if not (hasattr(self,"RBSalome")): return
       from Accas import SalomeEntry
       mc = self.node.item.get_definition()
       mctype = mc.type[0]
       enable_salome_selection = self.editor.salome and \
         (('grma' in repr(mctype)) or ('grno' in repr(mctype)) or ('SalomeEntry' in repr(mctype)) or \
         (hasattr(mctype, "enable_salome_selection") and mctype.enable_salome_selection))
       if enable_salome_selection:
          self.connect(self.RBSalome,SIGNAL("pressed()"),self.BSalomePressed)
          if not(('grma' in repr(mctype)) or ('grno' in repr(mctype))) or not(self.editor.salome): self.BView2D.close()
          else : self.connect(self.RBSalomeVue,SIGNAL("clicked()"),self.BView2DPressed)
       else:
          self.RBSalome.close()
          self.RBSalomeVue.close()

     
  def setIconesFichier(self):
       if not ( hasattr(self,"BFichier")): return
       mc = self.node.item.get_definition()
       mctype = mc.type[0]
       if mctype == "Repertoire":
          self.BRepertoire=self.BFichier
          self.connect(self.BRepertoire,SIGNAL("clicked()"),self.BRepertoirePressed)
          self.BVisuFichier.close()
       else :
          self.connect(self.BFichier,SIGNAL("clicked()"),self.BFichierPressed)
          self.connect(self.BVisuFichier,SIGNAL("clicked()"),self.BFichierVisu)




  def setRun(self):
      if hasattr(self.editor.appliEficas, 'mesScripts'):
         if self.tree.currentItem().item.get_nom() in self.appliEficas.mesScripts.dict_commandes.keys() :
               print 'il faut programmer le self.ajoutScript()'
               print '#PNPNPNPN'
               return
      if hasattr(self,"RBRun"): self.RBRun.close()


  def aDetruire(self):
      self.node.delete()

  def setValide(self):
      #print " c est le moment de gerer le passage au suivant"
      if not(hasattr (self,'RBValide')) : return
      icon = QIcon()
      repIcon=os.path.join(os.path.abspath(os.path.dirname(__file__)),'../Editeur/icons')
      if self.node.item.object.isvalid() : 
         icon=QIcon(repIcon+"/ast-green-ball.png")
      else :
         icon=QIcon(repIcon+"/ast-red-ball.png")
      self.RBValide.setIcon(icon)

  # il faut chercher la bonne fenetre
  def rendVisible(self):
      #print "je passe par rendVisible de FacultatifOuOptionnel"
      #print self
      #print self.node.fenetre
      #print "return pour etre sure"
      return
      #PNPN
      newNode=self.node.treeParent.chercheNoeudCorrespondant(self.node.item.object)
      #print newNode
      self.editor.fenetreCentraleAffichee.scrollAreaCommandes.ensureWidgetVisible(newNode.fenetre)
      #newNode.fenetre.setFocus()


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

