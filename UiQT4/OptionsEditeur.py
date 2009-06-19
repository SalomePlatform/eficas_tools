# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OptionsEditeur.ui'
#
# Created: Fri Apr 24 13:21:13 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_desOptions(object):
    def setupUi(self, desOptions):
        desOptions.setObjectName("desOptions")
        desOptions.resize(570, 474)
        self.gridLayout = QtGui.QGridLayout(desOptions)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox1 = QtGui.QGroupBox(desOptions)
        self.groupBox1.setMinimumSize(QtCore.QSize(548, 191))
        self.groupBox1.setObjectName("groupBox1")
        self.textLabel1_3 = QtGui.QLabel(self.groupBox1)
        self.textLabel1_3.setGeometry(QtCore.QRect(30, 60, 280, 20))
        self.textLabel1_3.setWordWrap(False)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.textLabel1_2_2 = QtGui.QLabel(self.groupBox1)
        self.textLabel1_2_2.setGeometry(QtCore.QRect(30, 120, 280, 20))
        self.textLabel1_2_2.setWordWrap(False)
        self.textLabel1_2_2.setObjectName("textLabel1_2_2")
        self.CBVersions = QtGui.QComboBox(self.groupBox1)
        self.CBVersions.setGeometry(QtCore.QRect(30, 20, 90, 30))
        self.CBVersions.setObjectName("CBVersions")
        self.LERepMat = QtGui.QLineEdit(self.groupBox1)
        self.LERepMat.setGeometry(QtCore.QRect(30, 140, 501, 31))
        self.LERepMat.setMinimumSize(QtCore.QSize(501, 31))
        self.LERepMat.setObjectName("LERepMat")
        self.LERepCata = QtGui.QLineEdit(self.groupBox1)
        self.LERepCata.setGeometry(QtCore.QRect(30, 80, 501, 31))
        self.LERepCata.setMinimumSize(QtCore.QSize(501, 31))
        self.LERepCata.setObjectName("LERepCata")
        self.Bok = QtGui.QPushButton(self.groupBox1)
        self.Bok.setGeometry(QtCore.QRect(440, 20, 90, 31))
        self.Bok.setMinimumSize(QtCore.QSize(90, 31))
        self.Bok.setAutoDefault(False)
        self.Bok.setObjectName("Bok")
        self.gridLayout.addWidget(self.groupBox1, 0, 0, 1, 2)
        self.groupBox2 = QtGui.QGroupBox(desOptions)
        self.groupBox2.setMinimumSize(QtCore.QSize(548, 90))
        self.groupBox2.setObjectName("groupBox2")
        self.LEVersionAjout = QtGui.QLineEdit(self.groupBox2)
        self.LEVersionAjout.setGeometry(QtCore.QRect(120, 31, 101, 30))
        self.LEVersionAjout.setMinimumSize(QtCore.QSize(101, 30))
        self.LEVersionAjout.setObjectName("LEVersionAjout")
        self.LEVersionSup = QtGui.QLineEdit(self.groupBox2)
        self.LEVersionSup.setGeometry(QtCore.QRect(410, 30, 101, 30))
        self.LEVersionSup.setObjectName("LEVersionSup")
        self.PBSup = QtGui.QPushButton(self.groupBox2)
        self.PBSup.setGeometry(QtCore.QRect(300, 20, 101, 41))
        self.PBSup.setMinimumSize(QtCore.QSize(101, 41))
        self.PBSup.setObjectName("PBSup")
        self.PBajout = QtGui.QPushButton(self.groupBox2)
        self.PBajout.setGeometry(QtCore.QRect(10, 20, 101, 41))
        self.PBajout.setMinimumSize(QtCore.QSize(101, 41))
        self.PBajout.setObjectName("PBajout")
        self.gridLayout.addWidget(self.groupBox2, 1, 0, 1, 2)
        self.groupBox3 = QtGui.QGroupBox(desOptions)
        self.groupBox3.setMinimumSize(QtCore.QSize(548, 90))
        self.groupBox3.setObjectName("groupBox3")
        self.LERepDoc = QtGui.QLineEdit(self.groupBox3)
        self.LERepDoc.setGeometry(QtCore.QRect(20, 50, 520, 31))
        self.LERepDoc.setMinimumSize(QtCore.QSize(520, 31))
        self.LERepDoc.setObjectName("LERepDoc")
        self.textLabel1 = QtGui.QLabel(self.groupBox3)
        self.textLabel1.setGeometry(QtCore.QRect(20, 20, 280, 30))
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.groupBox3, 2, 0, 1, 2)
        self.Bdefaut = QtGui.QCheckBox(desOptions)
        self.Bdefaut.setMinimumSize(QtCore.QSize(340, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Bdefaut.setFont(font)
        self.Bdefaut.setObjectName("Bdefaut")
        self.gridLayout.addWidget(self.Bdefaut, 3, 0, 1, 1)
        self.PBQuit = QtGui.QPushButton(desOptions)
        self.PBQuit.setMinimumSize(QtCore.QSize(151, 31))
        self.PBQuit.setObjectName("PBQuit")
        self.gridLayout.addWidget(self.PBQuit, 3, 1, 1, 1)

        self.retranslateUi(desOptions)
        QtCore.QMetaObject.connectSlotsByName(desOptions)

    def retranslateUi(self, desOptions):
        desOptions.setWindowTitle(QtGui.QApplication.translate("desOptions", "Options Aster", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox1.setTitle(QtGui.QApplication.translate("desOptions", "Configurer une Version", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3.setText(QtGui.QApplication.translate("desOptions", "Répertoire d\'accès au catalogue :", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2_2.setText(QtGui.QApplication.translate("desOptions", "Répertoire d\'accès aux matériaux :", None, QtGui.QApplication.UnicodeUTF8))
        self.Bok.setText(QtGui.QApplication.translate("desOptions", "Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox2.setTitle(QtGui.QApplication.translate("desOptions", "Gérer les versions", None, QtGui.QApplication.UnicodeUTF8))
        self.PBSup.setText(QtGui.QApplication.translate("desOptions", "Supprimer\n"
"Version :", None, QtGui.QApplication.UnicodeUTF8))
        self.PBajout.setText(QtGui.QApplication.translate("desOptions", "Ajouter\n"
"Version :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox3.setTitle(QtGui.QApplication.translate("desOptions", "Doc", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("desOptions", "Repertoire d\'acces à la documentation :", None, QtGui.QApplication.UnicodeUTF8))
        self.Bdefaut.setText(QtGui.QApplication.translate("desOptions", "Reinitialiser avec les valeurs par defaut", None, QtGui.QApplication.UnicodeUTF8))
        self.PBQuit.setText(QtGui.QApplication.translate("desOptions", "Quitter", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    desOptions = QtGui.QDialog()
    ui = Ui_desOptions()
    ui.setupUi(desOptions)
    desOptions.show()
    sys.exit(app.exec_())

