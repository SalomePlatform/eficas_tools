# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
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
import string,types,os

# Modules Eficas
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr


from desUniqueBase import Ui_DUnBase
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiqueUnique
listeSuffixe= ('bmp','png','jpg' )



class DUnBase(Ui_DUnBase,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.appliEficas=parent.appliEficas
       self.RepIcon=parent.appliEficas.RepIcon
       if hasattr(parent,"leLayout"):
          parent.leLayout.removeWidget(parent.leLayout.widgetActive)
          parent.leLayout.widgetActive.close()
          parent.leLayout.addWidget(self)
          parent.leLayout.widgetActive=self
       else:
          parent.partieDroite=QWidget()
          parent.leLayout=QGridLayout(parent.partieDroite)
          parent.leLayout.addWidget(self)
          parent.addWidget(parent.partieDroite)
          parent.leLayout.widgetActive=self
       self.setupUi(self)


# Import des panels

class MonUniqueBasePanel(DUnBase,QTPanel,SaisieValeur):
  """
  Classe definissant le panel associe aux mots-cles qui demandent
  a l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discretes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        #print "MonUniqueBasePanel"
        self.editor=parent
        QTPanel.__init__(self,node,parent)
        DUnBase.__init__(self,parent,fl)
        self.politique=PolitiqueUnique(node,parent)
        self.InitLineEditVal()
        self.InitCommentaire()
        self.detruitBouton()
        self.connecterSignaux()
        self.lineEditVal.setFocus()

  def connecterSignaux(self) :
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOk2Pressed)
        self.connect(self.lineEditVal,SIGNAL("returnPressed()"),self.LEValeurPressed)
        self.connect(self.bParametres,SIGNAL("pressed()"),self.BParametresPressed)
        self.connect(self.BSalome,SIGNAL("pressed()"),self.BSalomePressed)
        self.connect(self.BView2D,SIGNAL("clicked()"),self.BView2DPressed)
        self.connect(self.BFichier,SIGNAL("clicked()"),self.BFichierPressed)
        self.connect(self.BVisuFichier,SIGNAL("clicked()"),self.BFichierVisu)
        self.connect(self.BRepertoire,SIGNAL("clicked()"),self.BRepertoirePressed)


  def detruitBouton(self):
        icon = QIcon(self.RepIcon+"/image240.png")
        self.BSalome.setIcon(icon)
        mc = self.node.item.get_definition()
        mctype = mc.type[0]
        if mctype == "Fichier" or mctype == "FichierNoAbs" or \
            (hasattr(mctype, "enable_file_selection") and mctype.enable_file_selection):
           self.bParametres.close()
           self.BRepertoire.close()
        elif mctype == "Repertoire":
           self.bParametres.close()
           self.BFichier.close()
           self.BVisuFichier.close()
        else :
           self.BVisuFichier.close()
           self.BFichier.close()
           self.BRepertoire.close()
        # TODO: Use type properties instead of hard-coded "grno" and "grma" type check
        enable_salome_selection = self.editor.salome and \
            (('grma' in repr(mctype)) or ('grno' in repr(mctype)) or
             (hasattr(mctype, "enable_salome_selection") and mctype.enable_salome_selection))
        if not enable_salome_selection:
           self.BSalome.close()
        if not(('grma' in repr(mctype)) or ('grno' in repr(mctype))) or not(self.editor.salome):
           self.BView2D.close()

  def InitLineEditVal(self):
        valeur=self.node.item.get_valeur()
        valeurTexte=self.politique.GetValeurTexte(valeur)
        if valeurTexte != None :
           from decimal import Decimal
           if isinstance(valeurTexte,Decimal):
               chaine=str(valeurTexte)
           elif repr(valeurTexte.__class__).find("PARAMETRE") > 0:
               chaine = QString(repr(valeur)) 
           else :
               try :
                   chaine=QString("").setNum(valeurTexte)
               except :
                   chaine=QString(valeurTexte)
           self.lineEditVal.setText(chaine)
           mc = self.node.item.get_definition()
           if hasattr(self,"BSelectInFile"): return
           if (( mc.type[0]=="Fichier") and (QFileInfo(chaine).suffix() in listeSuffixe )):
             self.BSelectInFile = QPushButton(self.Widget8)
             self.BSelectInFile.setMinimumSize(QSize(140,40))
             self.BSelectInFile.setObjectName("BSelectInFile")
             self.gridLayout.addWidget(self.BSelectInFile,1,1,1,1)
             self.BSelectInFile.setText(tr("Selection"))
             self.image=chaine
             self.connect(self.BSelectInFile,SIGNAL("clicked()"),self.BSelectInFilePressed)



  def InitCommentaire(self):
      mc = self.node.item.get_definition()
      d_aides = { 'TXM' : tr("Une chaine de caracteres est attendue.  "),
                  'R'   : tr("Un reel est attendu. "),
                  'I'   : tr("Un entier est attendu.  "),
                  'Matrice' : tr('Une Matrice est attendue.  '),
                  'Fichier' : tr('Un fichier est attendu.  '),
                  'FichierNoAbs' : tr('Un fichier est attendu.  '),
                  'Repertoire' : tr('Un repertoire est attendu.  ')}
      mctype = mc.type[0]

      if type(mctype) == types.ClassType:
         commentaire = getattr(mctype, 'help_message', tr("Type de base inconnu"))
      else:
         commentaire = d_aides.get(mctype, tr("Type de base inconnu"))
       
      commentaire = commentaire +  str(self.node.item.aide())
      self.Commentaire.setText(commentaire)

  def BOk2Pressed(self):
        SaisieValeur.BOk2Pressed(self)

  def BFichierVisu(self):
       fichier=self.lineEditVal.text()
       from qtCommun import ViewText
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
         self.Commentaire.setText(tr("Fichier selectionne"))
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

  def BSelectInFilePressed(self):
      from monSelectImage import MonSelectImage
      MonSelectImage(file=self.image,parent=self).show()

          
  def LEValeurPressed(self):
        SaisieValeur.LEValeurPressed(self)
        if self.node.item.parent.nom == "MODEL" : 
           if self.node.item.isvalid():
		   self.node.item.parent.change_fichier="1"
                   self.node.item.parent.build_include(None,"")

  def BParametresPressed(self):
        QTPanel.BParametresPressed(self)

  def Ajout1Valeur(self,valeur):
        SaisieValeur.LEValeurPressed(self,valeur)

  def BSalomePressed(self):
        self.Commentaire.setText(QString(""))
        genea=self.node.item.get_genealogie()
        kwType = self.node.item.get_definition().type[0]
        for e in genea:
            if "GROUP_NO" in e: kwType = "GROUP_NO"
            if "GROUP_MA" in e: kwType = "GROUP_MA"

        selection, commentaire = self.appliEficas.selectGroupFromSalome(kwType,editor=self.editor)
        if commentaire !="" :
            self.Commentaire.setText(QString(commentaire))
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

