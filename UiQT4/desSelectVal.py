# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desSelectVal.ui'
#
# Created: Tue Jan 27 12:25:37 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DSelVal(object):
    def setupUi(self, DSelVal):
        DSelVal.setObjectName("DSelVal")
        DSelVal.resize(469, 624)
        self.TBtext = QtGui.QTextEdit(DSelVal)
        self.TBtext.setGeometry(QtCore.QRect(9, 9, 451, 476))
        self.TBtext.setObjectName("TBtext")
        self.BImportSel = QtGui.QPushButton(DSelVal)
        self.BImportSel.setGeometry(QtCore.QRect(220, 520, 208, 27))
        self.BImportSel.setObjectName("BImportSel")
        self.BImportTout = QtGui.QPushButton(DSelVal)
        self.BImportTout.setGeometry(QtCore.QRect(220, 560, 208, 27))
        self.BImportTout.setObjectName("BImportTout")
        self.BGSeparateur = QtGui.QGroupBox(DSelVal)
        self.BGSeparateur.setGeometry(QtCore.QRect(20, 500, 188, 103))
        self.BGSeparateur.setObjectName("BGSeparateur")
        self.Bespace = QtGui.QRadioButton(self.BGSeparateur)
        self.Bespace.setGeometry(QtCore.QRect(20, 20, 148, 23))
        self.Bespace.setChecked(True)
        self.Bespace.setObjectName("Bespace")
        self.Bvirgule = QtGui.QRadioButton(self.BGSeparateur)
        self.Bvirgule.setGeometry(QtCore.QRect(20, 40, 148, 23))
        self.Bvirgule.setObjectName("Bvirgule")
        self.BpointVirgule = QtGui.QRadioButton(self.BGSeparateur)
        self.BpointVirgule.setGeometry(QtCore.QRect(20, 60, 148, 23))
        self.BpointVirgule.setObjectName("BpointVirgule")

        self.retranslateUi(DSelVal)
        QtCore.QMetaObject.connectSlotsByName(DSelVal)

    def retranslateUi(self, DSelVal):
        DSelVal.setWindowTitle(QtGui.QApplication.translate("DSelVal", "Sélection de valeurs", None, QtGui.QApplication.UnicodeUTF8))
        self.BImportSel.setText(QtGui.QApplication.translate("DSelVal", "Ajouter Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.BImportTout.setText(QtGui.QApplication.translate("DSelVal", "Importer Tout", None, QtGui.QApplication.UnicodeUTF8))
        self.BGSeparateur.setTitle(QtGui.QApplication.translate("DSelVal", "Separateur", None, QtGui.QApplication.UnicodeUTF8))
        self.Bespace.setText(QtGui.QApplication.translate("DSelVal", "espace", None, QtGui.QApplication.UnicodeUTF8))
        self.Bvirgule.setText(QtGui.QApplication.translate("DSelVal", "virgule", None, QtGui.QApplication.UnicodeUTF8))
        self.BpointVirgule.setText(QtGui.QApplication.translate("DSelVal", "point-virgule", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DSelVal = QtGui.QWidget()
    ui = Ui_DSelVal()
    ui.setupUi(DSelVal)
    DSelVal.show()
    sys.exit(app.exec_())

