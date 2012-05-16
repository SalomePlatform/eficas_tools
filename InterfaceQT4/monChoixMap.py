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
# Modules Eficas

from desChoixMap import Ui_ChoixMap
from PyQt4  import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

    
# Import des panels

class MonChoixMap(Ui_ChoixMap,QtGui.QDialog):
  """
  """
  def __init__(self, parentAppli):
      QtGui.QDialog.__init__(self)
      self.setMinimumSize(50, 50);
      self.setModal(True)
      self.setupUi(self)
      self.parentAppli=parentAppli
      self.code='MAP'
      self.ChercheCatalogues()
      self.ajouteCeQuilFaut()
 

  def ajouteCeQuilFaut(self) :
        self.groupModules=QButtonGroup(self.groupBoxModule)
        self.groupModules.addButton(self.RBM1)
        self.groupModules.addButton(self.RBM2)
        self.groupModules.addButton(self.RBM4)
        self.groupModules.addButton(self.RBM5)
        self.groupModules.addButton(self.RBM6)
        self.groupModules.addButton(self.RBM7)
        self.groupModules.addButton(self.RBM8)
        self.groupScheme=QButtonGroup(self.groupBoxScheme)
        self.connect(self.groupModules,SIGNAL("buttonClicked (QAbstractButton*)"),self.modifieModule)
        self.connect(self.groupScheme,SIGNAL("buttonClicked (QAbstractButton*)"),self.choisitSchema)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Editeur/icons/map.ppm"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.PBIconeMap.setIcon(icon)

      
  def modifieModule(self):
      self.module=str(self.groupModules.checkedButton().text())
      self.dicoScheme={}
      for bouton in self.groupScheme.buttons():
          self.groupScheme.removeButton(bouton)
          bouton.close()
      for cata in self.catalogues :
          if len(cata)== 4 : code,label,fichierCata,tagCata=cata
          if len(cata)== 5 : code,label,fichierCata,tagCata,defaut=cata
          if self.module not in tagCata : continue
          bouton=QtGui.QRadioButton(self)
          self.groupScheme.addButton(bouton)
          bouton.setText(label)
          self.verticalLayout_2.addWidget(bouton)
          bouton.show()
          self.dicoScheme[label]=tagCata

  def choisitSchema(self):
      label=str(self.groupScheme.checkedButton().text())
      nomSscode=self.dicoScheme[label]
      self.parentAppli.ssCode=nomSscode
      self.close();

  def ChercheCatalogues(self):
      name='prefs_'+self.code
      prefsCode=__import__(name)
      nameConf='configuration_'+self.code
      configuration=__import__(nameConf)
      self.ssCode=None
      self.salome=self.parentAppli.salome
      self.top = self    #(pour CONFIGURATION)
      self.mode_nouv_commande='initial'
      self.CONFIGURATION = configuration.make_config(self,prefsCode.repIni)
      self.catalogues=self.CONFIGURATION.catalogues

