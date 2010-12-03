# -*- coding: utf-8 -*-
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
"s_oxides_st_1" : "Determination de l'allure de l'interface d'un oxyde donn� \npour un niveau a determiner d'irradiation" ,
"s_oxides_st_2" : "Estimation du champ mecanique dans une couche de zircone" ,
"s_oxides_mt_1" : "Estimation du champ mecanique dans une couche de zircone \npr�sentant des d�fauts et de l'�nergie �lastique relax�e",
"s_scc_st_1"    : "Analyse morphologique et m�canique d'une couche d'oxydes",
"s_scc_st_2"    : "Analyse statistique de donn�es locales et exp�rimentales \nou num�riques",
"s_scc_st_3"     : "taux de couverture des joints de grains par des pr�cipit�s",
"s_polymers_st_1"   : "Estimation num�rique 3D de la diffusion effective des gaz dans les polym�res charg�s",

         }

dico={"oxides" : {"irradiation"            : "s_oxides_st_1",
                   "mecanique"             : "s_oxides_st_2",
                   "mecanique avec defaut" : "s_oxides_mt_1"},
      "scc" : {"analyse morphologique" : "s_scc_st_1",
               "analyse statistique"   : "s_scc_st_2",
               "taux de couverture"    : "s_scc_st_3"},
      "concrete" : {},
      "polycristals" : {},
      "polymers" : {"numerique 3D" : "s_polymers_st_1"},
      "micro" : {},
      "seal" : {},
      "mox" : {},
      "nano" : {},
      "insulator" : {}}
    
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
  Classe d�finissant le panel associ� aux mots-cl�s qui demandent
  � l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discr�tes
  """
  def __init__(self, choixCata,parentQT=None,parentAppli=None):
      QtGui.QDialog.__init__(self,parentQT)
      self.setMinimumSize(50, 50);
      self.setModal(True)
      self.setupUi(self)
      self.ajouteCeQuilFaut()
      self.choixCata=choixCata
      self.parentAppli=parentAppli
 

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
        self.groupModules.addButton(self.RBM9)
        self.groupModules.addButton(self.RBM10)
        self.groupScheme=QButtonGroup(self.groupBoxScheme)
        self.connect(self.groupModules,SIGNAL("buttonClicked (QAbstractButton*)"),self.modifieModule)
        self.connect(self.groupScheme,SIGNAL("buttonClicked (QAbstractButton*)"),self.choisitSchema)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Editeur/icons/map.ppm"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.PBIconeMap.setIcon(icon)

      
  def modifieModule(self):
      self.module=str(self.groupModules.checkedButton().text())
      dicoModules=dico[self.module]
      self.choixCata.module=self.module
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
      self.choixCata.schema=schema
      nomCata= dico[self.module][schema]
      if self.parentAppli==None :
         self.choixCata.nom=nomCata
      else :
         self.parentAppli.ssCode=nomCata
      self.close();

