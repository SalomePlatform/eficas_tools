# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desInactif.ui'
#
# Created: Fri Jun 19 11:40:12 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DInactif(object):
    def setupUi(self, DInactif):
        DInactif.setObjectName("DInactif")
        DInactif.resize(452, 480)
        DInactif.setMinimumSize(QtCore.QSize(350, 0))
        self.gridLayout = QtGui.QGridLayout(DInactif)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1_3 = QtGui.QLabel(DInactif)
        self.textLabel1_3.setMinimumSize(QtCore.QSize(0, 0))
        self.textLabel1_3.setWordWrap(False)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.gridLayout.addWidget(self.textLabel1_3, 0, 0, 1, 3)
        self.textLabel1 = QtGui.QLabel(DInactif)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 1, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(167, 146, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.bSup = QtGui.QPushButton(DInactif)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bSup.sizePolicy().hasHeightForWidth())
        self.bSup.setSizePolicy(sizePolicy)
        self.bSup.setMinimumSize(QtCore.QSize(170, 40))
        self.bSup.setAutoDefault(True)
        self.bSup.setObjectName("bSup")
        self.gridLayout.addWidget(self.bSup, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(166, 146, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)

        self.retranslateUi(DInactif)
        QtCore.QMetaObject.connectSlotsByName(DInactif)

    def retranslateUi(self, DInactif):
        DInactif.setWindowTitle(QtGui.QApplication.translate("DInactif", "DInactif", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3.setText(QtGui.QApplication.translate("DInactif", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:x-large;\"><span style=\" font-size:x-large;\">Le noeud sélectionné ne correspond</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:x-large;\"><span style=\" font-size:x-large;\"> pas à un objet actif.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("DInactif", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:x-large;\"><span style=\" font-size:x-large;\">Seules les commandes placées</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:x-large;\"><span style=\" font-size:x-large;\"> entre : DEBUT / FIN sont actives </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setToolTip(QtGui.QApplication.translate("DInactif", "suppression du mot clef", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setText(QtGui.QApplication.translate("DInactif", "&Supprimer", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setShortcut(QtGui.QApplication.translate("DInactif", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DInactif = QtGui.QWidget()
    ui = Ui_DInactif()
    ui.setupUi(DInactif)
    DInactif.show()
    sys.exit(app.exec_())

