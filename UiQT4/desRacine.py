# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desRacine.ui'
#
# Created: Tue Sep 23 10:19:58 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DRac(object):
    def setupUi(self, DRac):
        DRac.setObjectName("DRac")
        DRac.resize(554,540)
        DRac.setMinimumSize(QtCore.QSize(505,0))
        self.gridLayout = QtGui.QGridLayout(DRac)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1_4 = QtGui.QLabel(DRac)
        self.textLabel1_4.setMinimumSize(QtCore.QSize(291,21))
        self.textLabel1_4.setWordWrap(False)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.gridLayout.addWidget(self.textLabel1_4,0,0,2,5)
        self.textLabel1_4_2 = QtGui.QLabel(DRac)
        self.textLabel1_4_2.setWordWrap(False)
        self.textLabel1_4_2.setObjectName("textLabel1_4_2")
        self.gridLayout.addWidget(self.textLabel1_4_2,1,4,1,2)
        self.RBalpha = QtGui.QRadioButton(DRac)
        self.RBalpha.setChecked(True)
        self.RBalpha.setObjectName("RBalpha")
        self.gridLayout.addWidget(self.RBalpha,2,0,1,2)
        self.RBGroupe = QtGui.QRadioButton(DRac)
        self.RBGroupe.setObjectName("RBGroupe")
        self.gridLayout.addWidget(self.RBGroupe,2,2,1,3)
        self.textLabel6 = QtGui.QLabel(DRac)
        self.textLabel6.setMinimumSize(QtCore.QSize(40,0))
        self.textLabel6.setWordWrap(False)
        self.textLabel6.setObjectName("textLabel6")
        self.gridLayout.addWidget(self.textLabel6,3,0,1,1)
        self.LEFiltre = QtGui.QLineEdit(DRac)
        self.LEFiltre.setMinimumSize(QtCore.QSize(0,30))
        self.LEFiltre.setObjectName("LEFiltre")
        self.gridLayout.addWidget(self.LEFiltre,3,1,1,1)
        self.BNext = QtGui.QPushButton(DRac)
        self.BNext.setObjectName("BNext")
        self.gridLayout.addWidget(self.BNext,3,2,1,1)
        self.LBRegles = QtGui.QListWidget(DRac)
        self.LBRegles.setMinimumSize(QtCore.QSize(0,0))
        self.LBRegles.setObjectName("LBRegles")
        self.gridLayout.addWidget(self.LBRegles,3,3,2,3)
        self.LBNouvCommande = QtGui.QListWidget(DRac)
        self.LBNouvCommande.setObjectName("LBNouvCommande")
        self.gridLayout.addWidget(self.LBNouvCommande,4,0,1,3)
        self.bSup = QtGui.QPushButton(DRac)
        self.bSup.setMinimumSize(QtCore.QSize(160,30))
        self.bSup.setAutoDefault(True)
        self.bSup.setObjectName("bSup")
        self.gridLayout.addWidget(self.bSup,5,0,1,2)
        self.bOk = QtGui.QPushButton(DRac)
        self.bOk.setMinimumSize(QtCore.QSize(160,30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.gridLayout.addWidget(self.bOk,5,2,1,3)
        self.bHelp = QtGui.QPushButton(DRac)
        self.bHelp.setMinimumSize(QtCore.QSize(160,30))
        self.bHelp.setAutoDefault(True)
        self.bHelp.setObjectName("bHelp")
        self.gridLayout.addWidget(self.bHelp,5,5,1,1)

        self.retranslateUi(DRac)
        QtCore.QMetaObject.connectSlotsByName(DRac)
        DRac.setTabOrder(self.LEFiltre,self.LBNouvCommande)
        DRac.setTabOrder(self.LBNouvCommande,self.bSup)
        DRac.setTabOrder(self.bSup,self.bOk)
        DRac.setTabOrder(self.bOk,self.bHelp)
        DRac.setTabOrder(self.bHelp,self.LBRegles)

    def retranslateUi(self, DRac):
        DRac.setWindowTitle(QtGui.QApplication.translate("DRac", "DMacro", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4.setText(QtGui.QApplication.translate("DRac", "<b><u>Commandes :</u></b>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4_2.setText(QtGui.QApplication.translate("DRac", "<p align=\"center\"><b><u>Régles :</u></b></p>", None, QtGui.QApplication.UnicodeUTF8))
        self.RBalpha.setText(QtGui.QApplication.translate("DRac", "alphabétique", None, QtGui.QApplication.UnicodeUTF8))
        self.RBGroupe.setText(QtGui.QApplication.translate("DRac", "par groupe", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel6.setText(QtGui.QApplication.translate("DRac", "Filtre", None, QtGui.QApplication.UnicodeUTF8))
        self.BNext.setText(QtGui.QApplication.translate("DRac", "Suivant", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setToolTip(QtGui.QApplication.translate("DRac", "suppression du mot clef", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setText(QtGui.QApplication.translate("DRac", "&Supprimer", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setShortcut(QtGui.QApplication.translate("DRac", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DRac", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DRac", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DRac", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setToolTip(QtGui.QApplication.translate("DRac", "affichage documentation aster", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setText(QtGui.QApplication.translate("DRac", "&Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setShortcut(QtGui.QApplication.translate("DRac", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DRac = QtGui.QWidget()
    ui = Ui_DRac()
    ui.setupUi(DRac)
    DRac.show()
    sys.exit(app.exec_())

