# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desListeParam.ui'
#
# Created: Tue Nov  2 16:22:59 2010
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DLisParam(object):
    def setupUi(self, DLisParam):
        DLisParam.setObjectName("DLisParam")
        DLisParam.resize(420,425)
        self.gridLayout = QtGui.QGridLayout(DLisParam)
        self.gridLayout.setObjectName("gridLayout")
        self.LBParam = QtGui.QListWidget(DLisParam)
        self.LBParam.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.LBParam.setObjectName("LBParam")
        self.gridLayout.addWidget(self.LBParam,0,0,1,1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(128,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.BOk = QtGui.QPushButton(DLisParam)
        self.BOk.setObjectName("BOk")
        self.horizontalLayout.addWidget(self.BOk)
        spacerItem1 = QtGui.QSpacerItem(168,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout,1,0,1,1)

        self.retranslateUi(DLisParam)
        QtCore.QMetaObject.connectSlotsByName(DLisParam)

    def retranslateUi(self, DLisParam):
        DLisParam.setWindowTitle(QtGui.QApplication.translate("DLisParam", "Sélection de paramétres", None, QtGui.QApplication.UnicodeUTF8))
        self.BOk.setText(QtGui.QApplication.translate("DLisParam", "Valider", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DLisParam = QtGui.QWidget()
    ui = Ui_DLisParam()
    ui.setupUi(DLisParam)
    DLisParam.show()
    sys.exit(app.exec_())

