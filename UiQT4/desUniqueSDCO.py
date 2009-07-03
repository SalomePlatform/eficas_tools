# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueSDCO.ui'
#
# Created: Fri Jun 19 11:40:13 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DUnSDCO(object):
    def setupUi(self, DUnSDCO):
        DUnSDCO.setObjectName("DUnSDCO")
        DUnSDCO.resize(461, 480)
        DUnSDCO.setMinimumSize(QtCore.QSize(350, 0))
        self.gridlayout = QtGui.QGridLayout(DUnSDCO)
        self.gridlayout.setObjectName("gridlayout")
        self.tabuniqueinto = QtGui.QTabWidget(DUnSDCO)
        self.tabuniqueinto.setObjectName("tabuniqueinto")
        self.Widget8 = QtGui.QWidget()
        self.Widget8.setObjectName("Widget8")
        self.gridlayout1 = QtGui.QGridLayout(self.Widget8)
        self.gridlayout1.setObjectName("gridlayout1")
        self.bOk = QtGui.QPushButton(self.Widget8)
        self.bOk.setMinimumSize(QtCore.QSize(0, 30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.gridlayout1.addWidget(self.bOk, 4, 1, 1, 1)
        self.Commentaire = QtGui.QLabel(self.Widget8)
        self.Commentaire.setMinimumSize(QtCore.QSize(311, 30))
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridlayout1.addWidget(self.Commentaire, 3, 0, 1, 3)
        self.textLabel2_2 = QtGui.QLabel(self.Widget8)
        self.textLabel2_2.setWordWrap(False)
        self.textLabel2_2.setObjectName("textLabel2_2")
        self.gridlayout1.addWidget(self.textLabel2_2, 0, 0, 1, 3)
        self.LESDCO = QtGui.QLineEdit(self.Widget8)
        self.LESDCO.setMinimumSize(QtCore.QSize(300, 40))
        self.LESDCO.setObjectName("LESDCO")
        self.gridlayout1.addWidget(self.LESDCO, 1, 0, 1, 3)
        self.textLabel2 = QtGui.QLabel(self.Widget8)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout1.addWidget(self.textLabel2, 2, 0, 1, 3)
        self.tabuniqueinto.addTab(self.Widget8, "")
        self.gridlayout.addWidget(self.tabuniqueinto, 0, 0, 1, 1)

        self.retranslateUi(DUnSDCO)
        QtCore.QMetaObject.connectSlotsByName(DUnSDCO)
        DUnSDCO.setTabOrder(self.LESDCO, self.tabuniqueinto)
        DUnSDCO.setTabOrder(self.tabuniqueinto, self.bOk)

    def retranslateUi(self, DUnSDCO):
        DUnSDCO.setWindowTitle(QtGui.QApplication.translate("DUnSDCO", "DUnIn", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DUnSDCO", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DUnSDCO", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DUnSDCO", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2_2.setText(QtGui.QApplication.translate("DUnSDCO", "<h1><font size=\"+2\">Nom du nouveau concept : </font></h1>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("DUnSDCO", "<font size=\"+1\">Un objet de type CO est attendu</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabuniqueinto.setTabText(self.tabuniqueinto.indexOf(self.Widget8), QtGui.QApplication.translate("DUnSDCO", "Saisir Valeur", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DUnSDCO = QtGui.QWidget()
    ui = Ui_DUnSDCO()
    ui.setupUi(DUnSDCO)
    DUnSDCO.show()
    sys.exit(app.exec_())

