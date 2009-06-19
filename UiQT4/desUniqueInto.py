# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueInto.ui'
#
# Created: Fri Apr 24 14:21:54 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DUnIn(object):
    def setupUi(self, DUnIn):
        DUnIn.setObjectName("DUnIn")
        DUnIn.resize(482, 480)
        DUnIn.setMinimumSize(QtCore.QSize(350, 0))
        self.gridLayout_2 = QtGui.QGridLayout(DUnIn)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabuniqueinto = QtGui.QTabWidget(DUnIn)
        self.tabuniqueinto.setObjectName("tabuniqueinto")
        self.Widget8 = QtGui.QWidget()
        self.Widget8.setObjectName("Widget8")
        self.gridLayout = QtGui.QGridLayout(self.Widget8)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel2 = QtGui.QLabel(self.Widget8)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")
        self.gridLayout.addWidget(self.textLabel2, 0, 0, 1, 1)
        self.listBoxVal = QtGui.QListWidget(self.Widget8)
        self.listBoxVal.setObjectName("listBoxVal")
        self.gridLayout.addWidget(self.listBoxVal, 1, 0, 1, 1)
        self.Commentaire = QtGui.QLabel(self.Widget8)
        self.Commentaire.setMinimumSize(QtCore.QSize(420, 30))
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridLayout.addWidget(self.Commentaire, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bOk = QtGui.QPushButton(self.Widget8)
        self.bOk.setMinimumSize(QtCore.QSize(160, 30))
        self.bOk.setMaximumSize(QtCore.QSize(160, 30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.horizontalLayout.addWidget(self.bOk)
        spacerItem1 = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.tabuniqueinto.addTab(self.Widget8, "")
        self.gridLayout_2.addWidget(self.tabuniqueinto, 0, 0, 1, 1)

        self.retranslateUi(DUnIn)
        QtCore.QMetaObject.connectSlotsByName(DUnIn)

    def retranslateUi(self, DUnIn):
        DUnIn.setWindowTitle(QtGui.QApplication.translate("DUnIn", "DUnIn", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("DUnIn", "<b><u><p align=\"center\">Valeurs possibles</p></u></b>", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DUnIn", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DUnIn", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DUnIn", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.tabuniqueinto.setTabText(self.tabuniqueinto.indexOf(self.Widget8), QtGui.QApplication.translate("DUnIn", "Saisir Valeur", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DUnIn = QtGui.QWidget()
    ui = Ui_DUnIn()
    ui.setupUi(DUnIn)
    DUnIn.show()
    sys.exit(app.exec_())

