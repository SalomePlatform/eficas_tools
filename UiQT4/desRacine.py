# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desRacine.ui'
#
# Created: Fri Jun 19 11:40:13 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DRac(object):
    def setupUi(self, DRac):
        DRac.setObjectName("DRac")
        DRac.resize(582, 540)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DRac.sizePolicy().hasHeightForWidth())
        DRac.setSizePolicy(sizePolicy)
        DRac.setMinimumSize(QtCore.QSize(505, 0))
        self.gridLayout_2 = QtGui.QGridLayout(DRac)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textLabel1_4 = QtGui.QLabel(DRac)
        self.textLabel1_4.setMinimumSize(QtCore.QSize(0, 20))
        self.textLabel1_4.setWordWrap(False)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.horizontalLayout.addWidget(self.textLabel1_4)
        self.textLabel1_4_2 = QtGui.QLabel(DRac)
        self.textLabel1_4_2.setWordWrap(False)
        self.textLabel1_4_2.setObjectName("textLabel1_4_2")
        self.horizontalLayout.addWidget(self.textLabel1_4_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RBalpha = QtGui.QRadioButton(DRac)
        self.RBalpha.setChecked(True)
        self.RBalpha.setObjectName("RBalpha")
        self.horizontalLayout_2.addWidget(self.RBalpha)
        self.RBGroupe = QtGui.QRadioButton(DRac)
        self.RBGroupe.setObjectName("RBGroupe")
        self.horizontalLayout_2.addWidget(self.RBGroupe)
        spacerItem = QtGui.QSpacerItem(228, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textLabel6 = QtGui.QLabel(DRac)
        self.textLabel6.setMinimumSize(QtCore.QSize(40, 0))
        self.textLabel6.setWordWrap(False)
        self.textLabel6.setObjectName("textLabel6")
        self.horizontalLayout_3.addWidget(self.textLabel6)
        self.LEFiltre = QtGui.QLineEdit(DRac)
        self.LEFiltre.setMinimumSize(QtCore.QSize(0, 30))
        self.LEFiltre.setObjectName("LEFiltre")
        self.horizontalLayout_3.addWidget(self.LEFiltre)
        self.BNext = QtGui.QPushButton(DRac)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BNext.sizePolicy().hasHeightForWidth())
        self.BNext.setSizePolicy(sizePolicy)
        self.BNext.setObjectName("BNext")
        self.horizontalLayout_3.addWidget(self.BNext)
        spacerItem1 = QtGui.QSpacerItem(268, 27, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LBNouvCommande = QtGui.QListWidget(DRac)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBNouvCommande.sizePolicy().hasHeightForWidth())
        self.LBNouvCommande.setSizePolicy(sizePolicy)
        self.LBNouvCommande.setObjectName("LBNouvCommande")
        self.gridLayout.addWidget(self.LBNouvCommande, 0, 0, 1, 1)
        self.LBRegles = QtGui.QListWidget(DRac)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBRegles.sizePolicy().hasHeightForWidth())
        self.LBRegles.setSizePolicy(sizePolicy)
        self.LBRegles.setMinimumSize(QtCore.QSize(0, 0))
        self.LBRegles.setObjectName("LBRegles")
        self.gridLayout.addWidget(self.LBRegles, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.bOk = QtGui.QPushButton(DRac)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bOk.sizePolicy().hasHeightForWidth())
        self.bOk.setSizePolicy(sizePolicy)
        self.bOk.setMinimumSize(QtCore.QSize(160, 30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.horizontalLayout_4.addWidget(self.bOk)
        spacerItem3 = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.retranslateUi(DRac)
        QtCore.QMetaObject.connectSlotsByName(DRac)
        DRac.setTabOrder(self.LEFiltre, self.LBNouvCommande)
        DRac.setTabOrder(self.LBNouvCommande, self.bOk)
        DRac.setTabOrder(self.bOk, self.LBRegles)

    def retranslateUi(self, DRac):
        DRac.setWindowTitle(QtGui.QApplication.translate("DRac", "DMacro", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4.setText(QtGui.QApplication.translate("DRac", "<b><u>Commandes :</u></b>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4_2.setText(QtGui.QApplication.translate("DRac", "<p align=\"center\"><b><u>Régles :</u></b></p>", None, QtGui.QApplication.UnicodeUTF8))
        self.RBalpha.setText(QtGui.QApplication.translate("DRac", "alphabétique", None, QtGui.QApplication.UnicodeUTF8))
        self.RBGroupe.setText(QtGui.QApplication.translate("DRac", "par groupe", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel6.setText(QtGui.QApplication.translate("DRac", "Filtre", None, QtGui.QApplication.UnicodeUTF8))
        self.BNext.setText(QtGui.QApplication.translate("DRac", "Suivant", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DRac", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DRac", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DRac", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DRac = QtGui.QWidget()
    ui = Ui_DRac()
    ui.setupUi(DRac)
    DRac.show()
    sys.exit(app.exec_())

