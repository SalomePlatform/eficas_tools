# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desVisu.ui'
#
# Created: Tue Nov 18 17:37:26 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DVisu(object):
    def setupUi(self, DVisu):
        DVisu.setObjectName("DVisu")
        DVisu.resize(501,394)
        self.gridlayout = QtGui.QGridLayout(DVisu)
        self.gridlayout.setObjectName("gridlayout")
        self.TB = QtGui.QTextBrowser(DVisu)
        self.TB.setObjectName("TB")
        self.gridlayout.addWidget(self.TB,0,0,1,1)

        self.retranslateUi(DVisu)

    def retranslateUi(self, DVisu):
        DVisu.setWindowTitle(QtGui.QApplication.translate("DVisu", "Visualisation Include Materiau", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DVisu = QtGui.QWidget()
    ui = Ui_DVisu()
    ui.setupUi(DVisu)
    DVisu.show()
    sys.exit(app.exec_())

