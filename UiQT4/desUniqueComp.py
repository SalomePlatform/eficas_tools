# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueComp.ui'
#
# Created: Wed Jul  9 10:31:14 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DUnComp(object):
    def setupUi(self, DUnComp):
        DUnComp.setObjectName("DUnComp")
        DUnComp.resize(484,529)
        DUnComp.setMinimumSize(QtCore.QSize(350,0))
        self.gridlayout = QtGui.QGridLayout(DUnComp)
        self.gridlayout.setObjectName("gridlayout")
        self.tabuniqueinto = QtGui.QTabWidget(DUnComp)
        self.tabuniqueinto.setObjectName("tabuniqueinto")
        self.Widget8 = QtGui.QWidget()
        self.Widget8.setGeometry(QtCore.QRect(0,0,462,484))
        self.Widget8.setObjectName("Widget8")
        self.gridLayout = QtGui.QGridLayout(self.Widget8)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtGui.QLabel(self.Widget8)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1,0,0,1,2)
        self.LEcomp = QtGui.QLineEdit(self.Widget8)
        self.LEcomp.setMinimumSize(QtCore.QSize(390,40))
        self.LEcomp.setObjectName("LEcomp")
        self.gridLayout.addWidget(self.LEcomp,1,0,1,2)
        self.groupBox = QtGui.QGroupBox(self.Widget8)
        self.groupBox.setObjectName("groupBox")
        self.RBRI = QtGui.QRadioButton(self.groupBox)
        self.RBRI.setGeometry(QtCore.QRect(10,30,444,23))
        self.RBRI.setObjectName("RBRI")
        self.RBMP = QtGui.QRadioButton(self.groupBox)
        self.RBMP.setGeometry(QtCore.QRect(10,50,444,23))
        self.RBMP.setObjectName("RBMP")
        self.gridLayout.addWidget(self.groupBox,2,0,1,2)
        self.LEReel = QtGui.QLineEdit(self.Widget8)
        self.LEReel.setMinimumSize(QtCore.QSize(190,40))
        self.LEReel.setObjectName("LEReel")
        self.gridLayout.addWidget(self.LEReel,3,0,1,1)
        self.LEImag = QtGui.QLineEdit(self.Widget8)
        self.LEImag.setMinimumSize(QtCore.QSize(190,40))
        self.LEImag.setObjectName("LEImag")
        self.gridLayout.addWidget(self.LEImag,3,1,1,1)
        self.Commentaire = QtGui.QLabel(self.Widget8)
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridLayout.addWidget(self.Commentaire,4,0,1,2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bSup = QtGui.QPushButton(self.Widget8)
        self.bSup.setAutoDefault(True)
        self.bSup.setObjectName("bSup")
        self.horizontalLayout.addWidget(self.bSup)
        self.bOk = QtGui.QPushButton(self.Widget8)
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.horizontalLayout.addWidget(self.bOk)
        self.bHelp = QtGui.QPushButton(self.Widget8)
        self.bHelp.setAutoDefault(True)
        self.bHelp.setObjectName("bHelp")
        self.horizontalLayout.addWidget(self.bHelp)
        self.gridLayout.addLayout(self.horizontalLayout,5,0,1,2)
        self.tabuniqueinto.addTab(self.Widget8,"")
        self.gridlayout.addWidget(self.tabuniqueinto,0,0,1,1)

        self.retranslateUi(DUnComp)
        QtCore.QMetaObject.connectSlotsByName(DUnComp)

    def retranslateUi(self, DUnComp):
        DUnComp.setWindowTitle(QtGui.QApplication.translate("DUnComp", "DUnComp", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("DUnComp", "<font size=\"+2\">Complexe de la forme : a+bj</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DUnComp", "Ou", None, QtGui.QApplication.UnicodeUTF8))
        self.RBRI.setText(QtGui.QApplication.translate("DUnComp", "RI   : Réel                                                 Imaginaire", None, QtGui.QApplication.UnicodeUTF8))
        self.RBMP.setText(QtGui.QApplication.translate("DUnComp", "MP    : Module                                             Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.Commentaire.setText(QtGui.QApplication.translate("DUnComp", "<font size=\"+2\">Un complexe est attendu</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setToolTip(QtGui.QApplication.translate("DUnComp", "suppression du mot clef", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setText(QtGui.QApplication.translate("DUnComp", "&Supprimer", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setShortcut(QtGui.QApplication.translate("DUnComp", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DUnComp", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DUnComp", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DUnComp", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setToolTip(QtGui.QApplication.translate("DUnComp", "affichage documentation aster", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setText(QtGui.QApplication.translate("DUnComp", "&Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setShortcut(QtGui.QApplication.translate("DUnComp", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.tabuniqueinto.setTabText(self.tabuniqueinto.indexOf(self.Widget8), QtGui.QApplication.translate("DUnComp", "Saisir Valeur", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DUnComp = QtGui.QWidget()
    ui = Ui_DUnComp()
    ui.setupUi(DUnComp)
    DUnComp.show()
    sys.exit(app.exec_())

