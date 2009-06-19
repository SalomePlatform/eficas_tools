# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desViewTexte.ui'
#
# Created: Tue Jan 27 12:25:39 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dView(object):
    def setupUi(self, dView):
        dView.setObjectName("dView")
        dView.resize(400, 322)
        self.gridLayout = QtGui.QGridLayout(dView)
        self.gridLayout.setObjectName("gridLayout")
        self.view = QtGui.QTextBrowser(dView)
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 0, 0, 1, 4)
        spacerItem = QtGui.QSpacerItem(209, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.bclose = QtGui.QPushButton(dView)
        self.bclose.setObjectName("bclose")
        self.gridLayout.addWidget(self.bclose, 1, 2, 1, 1)
        self.bsave = QtGui.QPushButton(dView)
        self.bsave.setObjectName("bsave")
        self.gridLayout.addWidget(self.bsave, 1, 1, 1, 1)

        self.retranslateUi(dView)
        QtCore.QMetaObject.connectSlotsByName(dView)

    def retranslateUi(self, dView):
        dView.setWindowTitle(QtGui.QApplication.translate("dView", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.bclose.setText(QtGui.QApplication.translate("dView", "Fermer", None, QtGui.QApplication.UnicodeUTF8))
        self.bsave.setText(QtGui.QApplication.translate("dView", "Sauver", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dView = QtGui.QDialog()
    ui = Ui_dView()
    ui.setupUi(dView)
    dView.show()
    sys.exit(app.exec_())

