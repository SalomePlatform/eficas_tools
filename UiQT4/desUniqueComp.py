# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueComp.ui'
#
# Created: Fri Apr 24 16:01:08 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DUnComp(object):
    def setupUi(self, DUnComp):
        DUnComp.setObjectName("DUnComp")
        DUnComp.resize(484, 529)
        DUnComp.setMinimumSize(QtCore.QSize(350, 0))
        self.gridlayout = QtGui.QGridLayout(DUnComp)
        self.gridlayout.setObjectName("gridlayout")
        self.tabuniqueinto = QtGui.QTabWidget(DUnComp)
        self.tabuniqueinto.setObjectName("tabuniqueinto")
        self.Widget8 = QtGui.QWidget()
        self.Widget8.setObjectName("Widget8")
        self.gridLayout_2 = QtGui.QGridLayout(self.Widget8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textLabel1 = QtGui.QLabel(self.Widget8)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.verticalLayout_2.addWidget(self.textLabel1)
        self.LEcomp = QtGui.QLineEdit(self.Widget8)
        self.LEcomp.setMinimumSize(QtCore.QSize(390, 40))
        self.LEcomp.setObjectName("LEcomp")
        self.verticalLayout_2.addWidget(self.LEcomp)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.groupBox = QtGui.QGroupBox(self.Widget8)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.RBRI = QtGui.QRadioButton(self.groupBox)
        self.RBRI.setObjectName("RBRI")
        self.gridLayout.addWidget(self.RBRI, 0, 0, 1, 1)
        self.RBMP = QtGui.QRadioButton(self.groupBox)
        self.RBMP.setObjectName("RBMP")
        self.gridLayout.addWidget(self.RBMP, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LEReel = QtGui.QLineEdit(self.Widget8)
        self.LEReel.setMinimumSize(QtCore.QSize(190, 40))
        self.LEReel.setObjectName("LEReel")
        self.horizontalLayout_2.addWidget(self.LEReel)
        self.LEImag = QtGui.QLineEdit(self.Widget8)
        self.LEImag.setMinimumSize(QtCore.QSize(190, 40))
        self.LEImag.setObjectName("LEImag")
        self.horizontalLayout_2.addWidget(self.LEImag)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Commentaire = QtGui.QLabel(self.Widget8)
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.verticalLayout.addWidget(self.Commentaire)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bOk = QtGui.QPushButton(self.Widget8)
        self.bOk.setMinimumSize(QtCore.QSize(160, 30))
        self.bOk.setMaximumSize(QtCore.QSize(160, 30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.horizontalLayout.addWidget(self.bOk)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.tabuniqueinto.addTab(self.Widget8, "")
        self.gridlayout.addWidget(self.tabuniqueinto, 0, 0, 1, 1)

        self.retranslateUi(DUnComp)
        QtCore.QMetaObject.connectSlotsByName(DUnComp)

    def retranslateUi(self, DUnComp):
        DUnComp.setWindowTitle(QtGui.QApplication.translate("DUnComp", "DUnComp", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("DUnComp", "<font size=\"+2\">Complexe de la forme : a+bj</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DUnComp", "Ou", None, QtGui.QApplication.UnicodeUTF8))
        self.RBRI.setText(QtGui.QApplication.translate("DUnComp", "RI   : Réel                                                 Imaginaire", None, QtGui.QApplication.UnicodeUTF8))
        self.RBMP.setText(QtGui.QApplication.translate("DUnComp", "MP    : Module                                             Phase", None, QtGui.QApplication.UnicodeUTF8))
        self.Commentaire.setText(QtGui.QApplication.translate("DUnComp", "<font size=\"+2\">Un complexe est attendu</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DUnComp", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DUnComp", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DUnComp", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.tabuniqueinto.setTabText(self.tabuniqueinto.indexOf(self.Widget8), QtGui.QApplication.translate("DUnComp", "Saisir Valeur", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DUnComp = QtGui.QWidget()
    ui = Ui_DUnComp()
    ui.setupUi(DUnComp)
    DUnComp.show()
    sys.exit(app.exec_())

