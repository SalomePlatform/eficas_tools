# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desListeParam.ui'
#
# Created: Tue Jan 27 12:25:36 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DLisParam(object):
    def setupUi(self, DLisParam):
        DLisParam.setObjectName("DLisParam")
        DLisParam.resize(413, 394)
        self.gridlayout = QtGui.QGridLayout(DLisParam)
        self.gridlayout.setObjectName("gridlayout")
        self.LBParam = QtGui.QListWidget(DLisParam)
        self.LBParam.setObjectName("LBParam")
        self.gridlayout.addWidget(self.LBParam, 0, 0, 1, 1)

        self.retranslateUi(DLisParam)

    def retranslateUi(self, DLisParam):
        DLisParam.setWindowTitle(QtGui.QApplication.translate("DLisParam", "Sélection de paramétres", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DLisParam = QtGui.QWidget()
    ui = Ui_DLisParam()
    ui.setupUi(DLisParam)
    DLisParam.show()
    sys.exit(app.exec_())

