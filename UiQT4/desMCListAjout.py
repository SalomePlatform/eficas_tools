# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desMCListAjout.ui'
#
# Created: Tue Nov 18 17:37:24 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DMCListAjout(object):
    def setupUi(self, DMCListAjout):
        DMCListAjout.setObjectName("DMCListAjout")
        DMCListAjout.resize(459,472)
        DMCListAjout.setMinimumSize(QtCore.QSize(350,0))
        self.gridlayout = QtGui.QGridLayout(DMCListAjout)
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1 = QtGui.QLabel(DMCListAjout)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1,1,0,1,3)
        self.textLabel1_2 = QtGui.QLabel(DMCListAjout)
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.gridlayout.addWidget(self.textLabel1_2,2,0,1,3)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtGui.QSpacerItem(60,21,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.bAjout = QtGui.QPushButton(DMCListAjout)
        self.bAjout.setAutoDefault(True)
        self.bAjout.setDefault(True)
        self.bAjout.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DMCListAjout", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8)))
        self.bAjout.setObjectName("bAjout")
        self.hboxlayout.addWidget(self.bAjout)
        spacerItem1 = QtGui.QSpacerItem(80,21,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.gridlayout.addLayout(self.hboxlayout,8,0,1,3)
        spacerItem2 = QtGui.QSpacerItem(21,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem2,9,1,1,1)
        self.textLabel1_2_2 = QtGui.QLabel(DMCListAjout)
        self.textLabel1_2_2.setWordWrap(False)
        self.textLabel1_2_2.setObjectName("textLabel1_2_2")
        self.gridlayout.addWidget(self.textLabel1_2_2,6,0,1,3)
        spacerItem3 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem3,7,1,1,1)
        self.MCFacteur = QtGui.QLabel(DMCListAjout)
        self.MCFacteur.setWordWrap(False)
        self.MCFacteur.setObjectName("MCFacteur")
        self.gridlayout.addWidget(self.MCFacteur,4,0,1,3)
        spacerItem4 = QtGui.QSpacerItem(21,31,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem4,5,1,1,1)
        spacerItem5 = QtGui.QSpacerItem(21,51,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem5,3,1,1,1)
        spacerItem6 = QtGui.QSpacerItem(41,51,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem6,0,1,1,1)
        self.bSup = QtGui.QPushButton(DMCListAjout)
        self.bSup.setAutoDefault(True)
        self.bSup.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DMCListAjout", "suppression du mot clef", None, QtGui.QApplication.UnicodeUTF8)))
        self.bSup.setObjectName("bSup")
        self.gridlayout.addWidget(self.bSup,10,0,1,1)
        self.bOk = QtGui.QPushButton(DMCListAjout)
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DMCListAjout", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8)))
        self.bOk.setObjectName("bOk")
        self.gridlayout.addWidget(self.bOk,10,1,1,1)
        self.bHelp = QtGui.QPushButton(DMCListAjout)
        self.bHelp.setAutoDefault(True)
        self.bHelp.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DMCListAjout", "affichage documentation aster", None, QtGui.QApplication.UnicodeUTF8)))
        self.bHelp.setObjectName("bHelp")
        self.gridlayout.addWidget(self.bHelp,10,2,1,1)

        self.retranslateUi(DMCListAjout)

    def retranslateUi(self, DMCListAjout):
        DMCListAjout.setWindowTitle(QtGui.QApplication.translate("DMCListAjout", "Form1", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("DMCListAjout", "<p align=\"center\"><font size=\"+1\">Pour ajouter une autre occurrence</font></p>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("DMCListAjout", "<p align=\"center\"><font size=\"+1\">du mot clef-facteur</font> </p>", None, QtGui.QApplication.UnicodeUTF8))
        self.bAjout.setText(QtGui.QApplication.translate("DMCListAjout", "&Ajouter", None, QtGui.QApplication.UnicodeUTF8))
        self.bAjout.setShortcut(QtGui.QApplication.translate("DMCListAjout", "Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2_2.setText(QtGui.QApplication.translate("DMCListAjout", "<p align=\"center\"><font size=\"+1\">cliquez ci-dessous</font> </p>", None, QtGui.QApplication.UnicodeUTF8))
        self.MCFacteur.setText(QtGui.QApplication.translate("DMCListAjout", "<p align=\"center\">AFFE</p>", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setText(QtGui.QApplication.translate("DMCListAjout", "&Supprimer", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setShortcut(QtGui.QApplication.translate("DMCListAjout", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DMCListAjout", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DMCListAjout", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setText(QtGui.QApplication.translate("DMCListAjout", "&Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setShortcut(QtGui.QApplication.translate("DMCListAjout", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DMCListAjout = QtGui.QWidget()
    ui = Ui_DMCListAjout()
    ui.setupUi(DMCListAjout)
    DMCListAjout.show()
    sys.exit(app.exec_())

