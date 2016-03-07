# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desViewTexte.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dView(object):
    def setupUi(self, dView):
        dView.setObjectName("dView")
        dView.resize(400, 322)
        self.gridLayout = QtWidgets.QGridLayout(dView)
        self.gridLayout.setObjectName("gridLayout")
        self.view = QtWidgets.QTextBrowser(dView)
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 0, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.bclose = QtWidgets.QPushButton(dView)
        self.bclose.setObjectName("bclose")
        self.gridLayout.addWidget(self.bclose, 1, 2, 1, 1)
        self.bsave = QtWidgets.QPushButton(dView)
        self.bsave.setObjectName("bsave")
        self.gridLayout.addWidget(self.bsave, 1, 1, 1, 1)
        self.view.raise_()
        self.bclose.raise_()
        self.bsave.raise_()

        self.retranslateUi(dView)
        QtCore.QMetaObject.connectSlotsByName(dView)

    def retranslateUi(self, dView):
        _translate = QtCore.QCoreApplication.translate
        dView.setWindowTitle(_translate("dView", "Dialog"))
        self.bclose.setText(_translate("dView", "Fermer"))
        self.bsave.setText(_translate("dView", "Sauver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dView = QtWidgets.QDialog()
    ui = Ui_dView()
    ui.setupUi(dView)
    dView.show()
    sys.exit(app.exec_())

