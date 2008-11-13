# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desMCListAjout.ui'
#
# Created: mar mar 25 10:05:08 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DMCListAjout(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DMCListAjout")

        self.setMinimumSize(QSize(350,0))

        DMCListAjoutLayout = QGridLayout(self,1,1,11,6,"DMCListAjoutLayout")

        self.textLabel1 = QLabel(self,"textLabel1")

        DMCListAjoutLayout.addMultiCellWidget(self.textLabel1,1,1,0,2)

        self.textLabel1_2 = QLabel(self,"textLabel1_2")

        DMCListAjoutLayout.addMultiCellWidget(self.textLabel1_2,2,2,0,2)

        layout9 = QHBoxLayout(None,0,6,"layout9")
        spacer4 = QSpacerItem(60,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9.addItem(spacer4)

        self.bAjout = QPushButton(self,"bAjout")
        self.bAjout.setAutoDefault(1)
        self.bAjout.setDefault(1)
        layout9.addWidget(self.bAjout)
        spacer2 = QSpacerItem(80,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9.addItem(spacer2)

        DMCListAjoutLayout.addMultiCellLayout(layout9,8,8,0,2)
        spacer1 = QSpacerItem(21,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
        DMCListAjoutLayout.addItem(spacer1,9,1)

        self.textLabel1_2_2 = QLabel(self,"textLabel1_2_2")

        DMCListAjoutLayout.addMultiCellWidget(self.textLabel1_2_2,6,6,0,2)
        spacer5 = QSpacerItem(20,20,QSizePolicy.Minimum,QSizePolicy.Expanding)
        DMCListAjoutLayout.addItem(spacer5,7,1)

        self.MCFacteur = QLabel(self,"MCFacteur")

        DMCListAjoutLayout.addMultiCellWidget(self.MCFacteur,4,4,0,2)
        spacer6 = QSpacerItem(21,31,QSizePolicy.Minimum,QSizePolicy.Expanding)
        DMCListAjoutLayout.addItem(spacer6,5,1)
        spacer7 = QSpacerItem(21,51,QSizePolicy.Minimum,QSizePolicy.Expanding)
        DMCListAjoutLayout.addItem(spacer7,3,1)
        spacer8 = QSpacerItem(41,51,QSizePolicy.Minimum,QSizePolicy.Expanding)
        DMCListAjoutLayout.addItem(spacer8,0,1)

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setAutoDefault(1)

        DMCListAjoutLayout.addWidget(self.bSup,10,0)

        self.bOk = QPushButton(self,"bOk")
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        DMCListAjoutLayout.addWidget(self.bOk,10,1)

        self.bHelp = QPushButton(self,"bHelp")
        self.bHelp.setAutoDefault(1)

        DMCListAjoutLayout.addWidget(self.bHelp,10,2)

        self.languageChange()

        self.resize(QSize(459,472).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bOk,SIGNAL("clicked()"),self.BAjoutClicked)
        self.connect(self.bAjout,SIGNAL("clicked()"),self.BAjoutClicked)
        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)
        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)


    def languageChange(self):
        self.setCaption(self.__tr("Form1"))
        self.textLabel1.setText(self.__tr("<p align=\"center\"><font size=\"+1\">Pour ajouter une autre occurrence</font></p>"))
        self.textLabel1_2.setText(self.__tr("<p align=\"center\"><font size=\"+1\">du mot clef-facteur</font> </p>"))
        self.bAjout.setText(self.__tr("&Ajouter"))
        self.bAjout.setAccel(self.__tr("Alt+A"))
        QToolTip.add(self.bAjout,self.__tr("validation de la saisie"))
        self.textLabel1_2_2.setText(self.__tr("<p align=\"center\"><font size=\"+1\">cliquez ci-dessous</font> </p>"))
        self.MCFacteur.setText(self.__tr("<p align=\"center\">AFFE</p>"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A"))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(self.__tr("Alt+D"))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))


    def BAjoutClicked(self):
        print "DMCListAjout.BAjoutClicked(): Not implemented yet"

    def BSupPressed(self):
        print "DMCListAjout.BSupPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DMCListAjout.ViewDoc(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DMCListAjout",s,c)
