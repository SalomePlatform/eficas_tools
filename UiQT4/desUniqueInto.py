# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueInto.ui'
#
# Created: Fri Jul 18 16:24:35 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DUnIn(object):
    def setupUi(self, DUnIn):
        DUnIn.setObjectName("DUnIn")
        DUnIn.resize(482,480)
        DUnIn.setMinimumSize(QtCore.QSize(350,0))
        self.gridlayout = QtGui.QGridLayout(DUnIn)
        self.gridlayout.setObjectName("gridlayout")
        self.tabuniqueinto = QtGui.QTabWidget(DUnIn)
        self.tabuniqueinto.setObjectName("tabuniqueinto")
        self.Widget8 = QtGui.QWidget()
        self.Widget8.setObjectName("Widget8")
        self.gridlayout1 = QtGui.QGridLayout(self.Widget8)
        self.gridlayout1.setObjectName("gridlayout1")
        self.Commentaire = QtGui.QLabel(self.Widget8)
        self.Commentaire.setMinimumSize(QtCore.QSize(420,30))
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridlayout1.addWidget(self.Commentaire,2,0,1,1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.bSup = QtGui.QPushButton(self.Widget8)
        self.bSup.setMinimumSize(QtCore.QSize(0,30))
        self.bSup.setAutoDefault(True)
        self.bSup.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DUnIn", "suppression du mot clef", None, QtGui.QApplication.UnicodeUTF8)))
        self.bSup.setObjectName("bSup")
        self.hboxlayout.addWidget(self.bSup)
        self.bOk = QtGui.QPushButton(self.Widget8)
        self.bOk.setMinimumSize(QtCore.QSize(0,30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DUnIn", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8)))
        self.bOk.setObjectName("bOk")
        self.hboxlayout.addWidget(self.bOk)
        self.bHelp = QtGui.QPushButton(self.Widget8)
        self.bHelp.setMinimumSize(QtCore.QSize(0,30))
        self.bHelp.setAutoDefault(True)
        self.bHelp.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DUnIn", "affichage documentation aster", None, QtGui.QApplication.UnicodeUTF8)))
        self.bHelp.setObjectName("bHelp")
        self.hboxlayout.addWidget(self.bHelp)
        self.gridlayout1.addLayout(self.hboxlayout,3,0,1,1)
        self.listBoxVal = QtGui.QListWidget(self.Widget8)
        self.listBoxVal.setObjectName("listBoxVal")
        self.gridlayout1.addWidget(self.listBoxVal,1,0,1,1)
        self.textLabel2 = QtGui.QLabel(self.Widget8)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout1.addWidget(self.textLabel2,0,0,1,1)
        self.tabuniqueinto.addTab(self.Widget8,"")
        self.gridlayout.addWidget(self.tabuniqueinto,0,0,1,1)

        self.retranslateUi(DUnIn)

    def retranslateUi(self, DUnIn):
        DUnIn.setWindowTitle(QtGui.QApplication.translate("DUnIn", "DUnIn", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setText(QtGui.QApplication.translate("DUnIn", "&Supprimer", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setShortcut(QtGui.QApplication.translate("DUnIn", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DUnIn", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DUnIn", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setText(QtGui.QApplication.translate("DUnIn", "&Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setShortcut(QtGui.QApplication.translate("DUnIn", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("DUnIn", "<b><u><p align=\"center\">Valeurs possibles</p></u></b>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabuniqueinto.setTabText(self.tabuniqueinto.indexOf(self.Widget8), QtGui.QApplication.translate("DUnIn", "Saisir Valeur", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DUnIn = QtGui.QWidget()
    ui = Ui_DUnIn()
    ui.setupUi(DUnIn)
    DUnIn.show()
    sys.exit(app.exec_())

