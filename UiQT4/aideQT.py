# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aideQT.ui'
#
# Created: Fri Jun 19 11:40:14 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Aide(object):
    def setupUi(self, Aide):
        Aide.setObjectName("Aide")
        Aide.resize(602, 480)
        self.gridLayout = QtGui.QGridLayout(Aide)
        self.gridLayout.setObjectName("gridLayout")
        self.TB1 = QtGui.QTextBrowser(Aide)
        self.TB1.setObjectName("TB1")
        self.gridLayout.addWidget(self.TB1, 0, 0, 1, 4)
        self.PBIndex = QtGui.QPushButton(Aide)
        self.PBIndex.setMinimumSize(QtCore.QSize(0, 30))
        self.PBIndex.setObjectName("PBIndex")
        self.gridLayout.addWidget(self.PBIndex, 1, 0, 1, 1)
        self.PBBack = QtGui.QPushButton(Aide)
        self.PBBack.setEnabled(True)
        self.PBBack.setMinimumSize(QtCore.QSize(0, 30))
        self.PBBack.setObjectName("PBBack")
        self.gridLayout.addWidget(self.PBBack, 1, 1, 1, 1)
        self.PBForward = QtGui.QPushButton(Aide)
        self.PBForward.setEnabled(True)
        self.PBForward.setMinimumSize(QtCore.QSize(0, 30))
        self.PBForward.setObjectName("PBForward")
        self.gridLayout.addWidget(self.PBForward, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(311, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)

        self.retranslateUi(Aide)
        QtCore.QMetaObject.connectSlotsByName(Aide)

    def retranslateUi(self, Aide):
        Aide.setWindowTitle(QtGui.QApplication.translate("Aide", "Aide", None, QtGui.QApplication.UnicodeUTF8))
        self.PBIndex.setText(QtGui.QApplication.translate("Aide", "Index", None, QtGui.QApplication.UnicodeUTF8))
        self.PBBack.setText(QtGui.QApplication.translate("Aide", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.PBForward.setText(QtGui.QApplication.translate("Aide", "Forward", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Aide = QtGui.QWidget()
    ui = Ui_Aide()
    ui.setupUi(Aide)
    Aide.show()
    sys.exit(app.exec_())

