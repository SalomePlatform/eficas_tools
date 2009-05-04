# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueASSD.ui'
#
# Created: Tue Nov 18 17:37:25 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DUnASSD(object):
    def setupUi(self, DUnASSD):
        DUnASSD.setObjectName("DUnASSD")
        DUnASSD.resize(482,480)
        DUnASSD.setMinimumSize(QtCore.QSize(350,0))
        self.gridlayout = QtGui.QGridLayout(DUnASSD)
        self.gridlayout.setObjectName("gridlayout")
        self.tabuniqueinto = QtGui.QTabWidget(DUnASSD)
        self.tabuniqueinto.setObjectName("tabuniqueinto")
        self.Widget8 = QtGui.QWidget()
        self.Widget8.setObjectName("Widget8")
        self.gridlayout1 = QtGui.QGridLayout(self.Widget8)
        self.gridlayout1.setObjectName("gridlayout1")
        self.textLabel2 = QtGui.QLabel(self.Widget8)
        self.textLabel2.setMinimumSize(QtCore.QSize(436,50))
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout1.addWidget(self.textLabel2,0,0,1,1)
        self.listBoxASSD = QtGui.QListWidget(self.Widget8)
        self.listBoxASSD.setObjectName("listBoxASSD")
        self.gridlayout1.addWidget(self.listBoxASSD,1,0,1,1)
        self.Commentaire = QtGui.QLabel(self.Widget8)
        self.Commentaire.setMinimumSize(QtCore.QSize(380,30))
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridlayout1.addWidget(self.Commentaire,2,0,1,1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.bSup = QtGui.QPushButton(self.Widget8)
        self.bSup.setMinimumSize(QtCore.QSize(0,30))
        self.bSup.setAutoDefault(True)
        self.bSup.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DUnASSD", "suppression du mot clef", None, QtGui.QApplication.UnicodeUTF8)))
        self.bSup.setObjectName("bSup")
        self.hboxlayout.addWidget(self.bSup)
        self.bOk = QtGui.QPushButton(self.Widget8)
        self.bOk.setMinimumSize(QtCore.QSize(0,30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DUnASSD", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8)))
        self.bOk.setObjectName("bOk")
        self.hboxlayout.addWidget(self.bOk)
        self.bHelp = QtGui.QPushButton(self.Widget8)
        self.bHelp.setMinimumSize(QtCore.QSize(0,30))
        self.bHelp.setAutoDefault(True)
        self.bHelp.setProperty("toolTip",QtCore.QVariant(QtGui.QApplication.translate("DUnASSD", "affichage documentation aster", None, QtGui.QApplication.UnicodeUTF8)))
        self.bHelp.setObjectName("bHelp")
        self.hboxlayout.addWidget(self.bHelp)
        self.gridlayout1.addLayout(self.hboxlayout,3,0,1,1)
        self.tabuniqueinto.addTab(self.Widget8,"")
        self.gridlayout.addWidget(self.tabuniqueinto,0,0,1,1)

        self.retranslateUi(DUnASSD)

    def retranslateUi(self, DUnASSD):
        DUnASSD.setWindowTitle(QtGui.QApplication.translate("DUnASSD", "DUnIn", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("DUnASSD", "<font size=\"+1\"><p align=\"center\">Structures de données du type\n"
"requis par l\'objet courant :</p></font>", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setText(QtGui.QApplication.translate("DUnASSD", "&Supprimer", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setShortcut(QtGui.QApplication.translate("DUnASSD", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DUnASSD", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DUnASSD", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setText(QtGui.QApplication.translate("DUnASSD", "&Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setShortcut(QtGui.QApplication.translate("DUnASSD", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.tabuniqueinto.setTabText(self.tabuniqueinto.indexOf(self.Widget8), QtGui.QApplication.translate("DUnASSD", "Saisir Valeur", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DUnASSD = QtGui.QWidget()
    ui = Ui_DUnASSD()
    ui.setupUi(DUnASSD)
    DUnASSD.show()
    sys.exit(app.exec_())

