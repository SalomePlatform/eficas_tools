#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
# Modules Python
# Modules Eficas

from desChoixMap import Ui_ChoixMap
from PyQt4  import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *


labels = {
"s_scc_st_1"    : "Analyse morphologique et mecanique d'une couche d'oxydes",
"s_scc_st_2"    : "Analyse statistique de donnees locales et experimentales \nou numeriques",
"s_scc_st_3"    : "taux de couverture des joints de grains par des precipites",
"s_scc_3d"      : "Analyse 3D",
"maquettemap"   : "Analyse 3D",
"s_oxides_st_1" : "Determination de l'allure de l'interface d'un oxyde donne pour un niveau a determiner d'irradiation" ,
"s_oxides_st_2" : "Estimation du champ mecanique dans une couche de zircone" ,
"s_oxides_mt_1" : "Estimation du champ mecanique dans une couche de zircone presentant des defauts et de l'energie elastique relaxee",
"s_polymers_st_1"   : "Estimation numerique 3D de la diffusion effective des gaz dans les polymeres charges",
"s_Perfect"     : "Essai Perfect",
"Creation"    : "Essai PN",
"s_DIC"   : "Essai Felix",
"maquettemap" : "Essai",
         }

dico={"scc" : {"analyse morphologique" : "s_scc_st_1",
               "analyse statistique"   : "s_scc_st_2",
               "taux de couverture"    : "s_scc_st_3",
               "analyse 3d"            : "s_scc_3d",
               "maquette"              : "maquettemap"},
      "Creation de catalogue" : {"Essai pour Perfect":"s_Perfect",
                                 "Essai pour composant":"Creation"},
      "image" : {"" : "c_image_2d_align",
                 "" : "c_image_2d_", }
# cli20i2.der.edf.fr/MAP/milestone/2012.1
}
    
# Import des panels

class MonRadioBouton(QRadioButton) :

  def setModule(self,module,fenetreMere):
      self.module=module
      self.fenetreMere=fenetreMere

  def enterEvent(self,e):
      schema=str(self.text())
      nomCata=dico[self.module][schema]
      self.fenetreMere.labelScheme.setText(labels[nomCata])

class MonChoixMap(Ui_ChoixMap,QtGui.QDialog):
  """
  """
  def __init__(self, parentAppli):
      QtGui.QDialog.__init__(self)
      self.setMinimumSize(50, 50);
      self.setModal(True)
      self.setupUi(self)
      self.parentAppli=parentAppli
      self.ajouteCeQuilFaut()
 

  def ajouteCeQuilFaut(self) :
        self.groupModules=QButtonGroup(self.groupBoxModule)
        self.vLayoutScheme=QVBoxLayout(self.groupBoxScheme)
        self.groupModules.addButton(self.RBM1)
        self.groupModules.addButton(self.RBM2)
        self.groupModules.addButton(self.RBM3)
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
      dicoModules=dico[self.module]
      for bouton in self.groupScheme.buttons():
          self.groupScheme.removeButton(bouton)
          bouton.close()
      for label in dicoModules.keys():
          bouton=MonRadioBouton(QString(label),self.groupBoxScheme)
          bouton.setModule(self.module,self)
          self.vLayoutScheme.addWidget(bouton)
          self.groupScheme.addButton(bouton)

      
  def choisitSchema(self):
      schema=str(self.groupScheme.checkedButton().text())
      nomCata= dico[self.module][schema]
      self.parentAppli.ssCode=nomCata
      self.close();

