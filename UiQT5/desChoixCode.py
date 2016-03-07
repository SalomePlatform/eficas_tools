# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desChoixCode.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChoixCode(object):
    def setupUi(self, ChoixCode):
        ChoixCode.setObjectName("ChoixCode")
        ChoixCode.resize(555, 332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChoixCode.sizePolicy().hasHeightForWidth())
        ChoixCode.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChoixCode)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_choix = QtWidgets.QLabel(ChoixCode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_choix.sizePolicy().hasHeightForWidth())
        self.label_choix.setSizePolicy(sizePolicy)
        self.label_choix.setMinimumSize(QtCore.QSize(0, 30))
        self.label_choix.setObjectName("label_choix")
        self.verticalLayout.addWidget(self.label_choix)
        self.groupBox = QtWidgets.QGroupBox(ChoixCode)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pB_cancel = QtWidgets.QPushButton(ChoixCode)
        self.pB_cancel.setMinimumSize(QtCore.QSize(140, 40))
        self.pB_cancel.setToolTip("")
        self.pB_cancel.setStyleSheet("background-color:rgb(104,110,149);\n"
"color :white;\n"
"border-radius : 12px\n"
"")
        self.pB_cancel.setShortcut("")
        self.pB_cancel.setAutoDefault(True)
        self.pB_cancel.setObjectName("pB_cancel")
        self.horizontalLayout.addWidget(self.pB_cancel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pB_OK = QtWidgets.QPushButton(ChoixCode)
        self.pB_OK.setMinimumSize(QtCore.QSize(140, 40))
        self.pB_OK.setStyleSheet("background-color:rgb(104,110,149);\n"
"color :white;\n"
"border-radius : 12px\n"
"\n"
"")
        self.pB_OK.setShortcut("")
        self.pB_OK.setAutoDefault(True)
        self.pB_OK.setDefault(True)
        self.pB_OK.setObjectName("pB_OK")
        self.horizontalLayout.addWidget(self.pB_OK)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ChoixCode)
        QtCore.QMetaObject.connectSlotsByName(ChoixCode)

    def retranslateUi(self, ChoixCode):
        _translate = QtCore.QCoreApplication.translate
        ChoixCode.setWindowTitle(_translate("ChoixCode", "Choix du code"))
        self.label_choix.setText(_translate("ChoixCode", "Veuillez choisir un code :"))
        self.pB_cancel.setText(_translate("ChoixCode", "&Cancel"))
        self.pB_OK.setToolTip(_translate("ChoixCode", "Validate choice"))
        self.pB_OK.setText(_translate("ChoixCode", "&OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChoixCode = QtWidgets.QWidget()
    ui = Ui_ChoixCode()
    ui.setupUi(ChoixCode)
    ChoixCode.show()
    sys.exit(app.exec_())

