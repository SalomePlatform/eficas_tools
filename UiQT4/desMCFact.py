# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desMCFact.ui'
#
# Created: Thu Mar 12 10:42:30 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DMCFact(object):
    def setupUi(self, DMCFact):
        DMCFact.setObjectName("DMCFact")
        DMCFact.resize(511, 499)
        DMCFact.setMinimumSize(QtCore.QSize(505, 0))
        self.gridlayout = QtGui.QGridLayout(DMCFact)
        self.gridlayout.setObjectName("gridlayout")
        self.TWChoix = QtGui.QTabWidget(DMCFact)
        self.TWChoix.setObjectName("TWChoix")
        self.MotClef = QtGui.QWidget()
        self.MotClef.setObjectName("MotClef")
        self.gridlayout1 = QtGui.QGridLayout(self.MotClef)
        self.gridlayout1.setObjectName("gridlayout1")
        self.textLabel1 = QtGui.QLabel(self.MotClef)
        self.textLabel1.setMinimumSize(QtCore.QSize(0, 0))
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout1.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.LBMCPermis = QtGui.QListWidget(self.MotClef)
        self.LBMCPermis.setMinimumSize(QtCore.QSize(0, 0))
        self.LBMCPermis.setObjectName("LBMCPermis")
        self.gridlayout1.addWidget(self.LBMCPermis, 1, 0, 1, 1)
        self.LBRegles = QtGui.QListWidget(self.MotClef)
        self.LBRegles.setObjectName("LBRegles")
        self.gridlayout1.addWidget(self.LBRegles, 1, 1, 1, 1)
        self.textLabel1_2 = QtGui.QLabel(self.MotClef)
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.gridlayout1.addWidget(self.textLabel1_2, 0, 1, 1, 1)
        self.TWChoix.addTab(self.MotClef, "")
        self.gridlayout.addWidget(self.TWChoix, 0, 0, 1, 3)
        self.Commentaire = QtGui.QLabel(DMCFact)
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridlayout.addWidget(self.Commentaire, 1, 0, 1, 3)
        self.bOk = QtGui.QPushButton(DMCFact)
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.gridlayout.addWidget(self.bOk, 2, 1, 1, 1)

        self.retranslateUi(DMCFact)
        QtCore.QMetaObject.connectSlotsByName(DMCFact)

    def retranslateUi(self, DMCFact):
        DMCFact.setWindowTitle(QtGui.QApplication.translate("DMCFact", "DMacro", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("DMCFact", "<h3><p align=\"center\"><u><b>Mots Clefs Permis</b></u></p></h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("DMCFact", "<h3><p align=\"center\"><u><b>Régles</b></u></p></h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.MotClef), QtGui.QApplication.translate("DMCFact", "Ajouter Mot-Clef", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DMCFact", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DMCFact", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DMCFact", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DMCFact = QtGui.QWidget()
    ui = Ui_DMCFact()
    ui.setupUi(DMCFact)
    DMCFact.show()
    sys.exit(app.exec_())

