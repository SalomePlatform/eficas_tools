# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desVisu.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DVisu(object):
    def setupUi(self, DVisu):
        DVisu.setObjectName("DVisu")
        DVisu.resize(501, 61)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DVisu)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TB = QtWidgets.QTextBrowser(DVisu)
        self.TB.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TB.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TB.setObjectName("TB")
        self.horizontalLayout.addWidget(self.TB)

        self.retranslateUi(DVisu)
        QtCore.QMetaObject.connectSlotsByName(DVisu)

    def retranslateUi(self, DVisu):
        _translate = QtCore.QCoreApplication.translate
        DVisu.setWindowTitle(_translate("DVisu", "Visualisation Include Materiau"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DVisu = QtWidgets.QWidget()
    ui = Ui_DVisu()
    ui.setupUi(DVisu)
    DVisu.show()
    sys.exit(app.exec_())

