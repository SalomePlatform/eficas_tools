# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desSelectVal.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DSelVal(object):
    def setupUi(self, DSelVal):
        DSelVal.setObjectName("DSelVal")
        DSelVal.resize(633, 705)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DSelVal.sizePolicy().hasHeightForWidth())
        DSelVal.setSizePolicy(sizePolicy)
        DSelVal.setStyleSheet("background:rgb(235,235,235)")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DSelVal)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.TBtext = QtWidgets.QTextEdit(DSelVal)
        self.TBtext.setMinimumSize(QtCore.QSize(0, 400))
        self.TBtext.setStyleSheet("background:rgb(250,250,250)")
        self.TBtext.setObjectName("TBtext")
        self.verticalLayout_3.addWidget(self.TBtext)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BGSeparateur = QtWidgets.QGroupBox(DSelVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BGSeparateur.sizePolicy().hasHeightForWidth())
        self.BGSeparateur.setSizePolicy(sizePolicy)
        self.BGSeparateur.setMinimumSize(QtCore.QSize(280, 150))
        self.BGSeparateur.setObjectName("BGSeparateur")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.BGSeparateur)
        self.verticalLayout_4.setContentsMargins(11, 15, 11, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Bespace = QtWidgets.QRadioButton(self.BGSeparateur)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Bespace.sizePolicy().hasHeightForWidth())
        self.Bespace.setSizePolicy(sizePolicy)
        self.Bespace.setChecked(True)
        self.Bespace.setObjectName("Bespace")
        self.verticalLayout.addWidget(self.Bespace)
        self.Bvirgule = QtWidgets.QRadioButton(self.BGSeparateur)
        self.Bvirgule.setObjectName("Bvirgule")
        self.verticalLayout.addWidget(self.Bvirgule)
        self.BpointVirgule = QtWidgets.QRadioButton(self.BGSeparateur)
        self.BpointVirgule.setObjectName("BpointVirgule")
        self.verticalLayout.addWidget(self.BpointVirgule)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.BGSeparateur)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(23, 43, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.BImportTout = QtWidgets.QPushButton(DSelVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BImportTout.sizePolicy().hasHeightForWidth())
        self.BImportTout.setSizePolicy(sizePolicy)
        self.BImportTout.setMinimumSize(QtCore.QSize(200, 40))
        self.BImportTout.setMaximumSize(QtCore.QSize(200, 40))
        self.BImportTout.setStyleSheet("background-color:rgb(104,110,149);\n"
"color :white;\n"
"border-radius : 12px\n"
"")
        self.BImportTout.setObjectName("BImportTout")
        self.verticalLayout_2.addWidget(self.BImportTout)
        self.BImportSel = QtWidgets.QPushButton(DSelVal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BImportSel.sizePolicy().hasHeightForWidth())
        self.BImportSel.setSizePolicy(sizePolicy)
        self.BImportSel.setMinimumSize(QtCore.QSize(200, 40))
        self.BImportSel.setMaximumSize(QtCore.QSize(200, 40))
        self.BImportSel.setStyleSheet("background-color:rgb(104,110,149);\n"
"color :white;\n"
"border-radius : 12px\n"
"")
        self.BImportSel.setObjectName("BImportSel")
        self.verticalLayout_2.addWidget(self.BImportSel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(DSelVal)
        QtCore.QMetaObject.connectSlotsByName(DSelVal)

    def retranslateUi(self, DSelVal):
        _translate = QtCore.QCoreApplication.translate
        DSelVal.setWindowTitle(_translate("DSelVal", "Sélection de valeurs"))
        self.BGSeparateur.setTitle(_translate("DSelVal", "Separateur"))
        self.Bespace.setText(_translate("DSelVal", "espace"))
        self.Bvirgule.setText(_translate("DSelVal", "virgule"))
        self.BpointVirgule.setText(_translate("DSelVal", "point-virgule"))
        self.BImportTout.setText(_translate("DSelVal", "Importer Tout"))
        self.BImportSel.setText(_translate("DSelVal", "Ajouter Selection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DSelVal = QtWidgets.QWidget()
    ui = Ui_DSelVal()
    ui.setupUi(DSelVal)
    DSelVal.show()
    sys.exit(app.exec_())

