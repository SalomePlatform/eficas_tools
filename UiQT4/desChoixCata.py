# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desChoixCata.ui'
#
# Created: Fri Jun 19 11:40:11 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DChoixCata(object):
    def setupUi(self, DChoixCata):
        DChoixCata.setObjectName("DChoixCata")
        DChoixCata.resize(547, 215)
        DChoixCata.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(DChoixCata)
        self.gridLayout.setObjectName("gridLayout")
        self.TLNb = QtGui.QLabel(DChoixCata)
        self.TLNb.setMinimumSize(QtCore.QSize(30, 0))
        self.TLNb.setWordWrap(False)
        self.TLNb.setObjectName("TLNb")
        self.gridLayout.addWidget(self.TLNb, 0, 0, 1, 1)
        self.CBChoixCata = QtGui.QComboBox(DChoixCata)
        self.CBChoixCata.setEnabled(True)
        self.CBChoixCata.setMinimumSize(QtCore.QSize(125, 41))
        self.CBChoixCata.setMaximumSize(QtCore.QSize(150, 16777215))
        self.CBChoixCata.setObjectName("CBChoixCata")
        self.gridLayout.addWidget(self.CBChoixCata, 0, 1, 2, 1)
        self.textLabel1_2 = QtGui.QLabel(DChoixCata)
        self.textLabel1_2.setMinimumSize(QtCore.QSize(60, 60))
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.gridLayout.addWidget(self.textLabel1_2, 1, 0, 1, 1)
        self.frame3 = QtGui.QFrame(DChoixCata)
        self.frame3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.buttonOk = QtGui.QPushButton(self.frame3)
        self.buttonOk.setGeometry(QtCore.QRect(11, 13, 91, 41))
        self.buttonOk.setAutoDefault(True)
        self.buttonOk.setDefault(True)
        self.buttonOk.setObjectName("buttonOk")
        self.buttonCancel = QtGui.QPushButton(self.frame3)
        self.buttonCancel.setGeometry(QtCore.QRect(437, 13, 81, 41))
        self.buttonCancel.setMinimumSize(QtCore.QSize(81, 41))
        self.buttonCancel.setAutoDefault(True)
        self.buttonCancel.setObjectName("buttonCancel")
        self.gridLayout.addWidget(self.frame3, 2, 0, 1, 2)

        self.retranslateUi(DChoixCata)
        QtCore.QMetaObject.connectSlotsByName(DChoixCata)

    def retranslateUi(self, DChoixCata):
        DChoixCata.setWindowTitle(QtGui.QApplication.translate("DChoixCata", "Choix d\'une version du code Aster", None, QtGui.QApplication.UnicodeUTF8))
        self.TLNb.setText(QtGui.QApplication.translate("DChoixCata", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">2 versions sont disponibles</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("DChoixCata", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large;\">Veuillez choisir celle avec laquelle</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:large;\"><span style=\" font-size:large;\"> vous souhaitez travailler</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOk.setText(QtGui.QApplication.translate("DChoixCata", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("DChoixCata", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DChoixCata = QtGui.QDialog()
    ui = Ui_DChoixCata()
    ui.setupUi(DChoixCata)
    DChoixCata.show()
    sys.exit(app.exec_())

