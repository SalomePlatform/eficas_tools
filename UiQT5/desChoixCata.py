# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desChoixCata.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DChoixCata(object):
    def setupUi(self, DChoixCata):
        DChoixCata.setObjectName("DChoixCata")
        DChoixCata.resize(466, 206)
        DChoixCata.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(DChoixCata)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TLNb = QtWidgets.QLabel(DChoixCata)
        self.TLNb.setMinimumSize(QtCore.QSize(0, 0))
        self.TLNb.setWordWrap(False)
        self.TLNb.setObjectName("TLNb")
        self.horizontalLayout_3.addWidget(self.TLNb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.CBChoixCata = QtWidgets.QComboBox(DChoixCata)
        self.CBChoixCata.setEnabled(True)
        self.CBChoixCata.setMinimumSize(QtCore.QSize(400, 41))
        self.CBChoixCata.setMaximumSize(QtCore.QSize(150, 16777215))
        self.CBChoixCata.setObjectName("CBChoixCata")
        self.verticalLayout.addWidget(self.CBChoixCata)
        spacerItem2 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.buttonCancel = QtWidgets.QPushButton(DChoixCata)
        self.buttonCancel.setMinimumSize(QtCore.QSize(140, 40))
        self.buttonCancel.setToolTip("")
        self.buttonCancel.setStyleSheet("background-color:rgb(104,110,149);\n"
"color :white;\n"
"border-radius : 12px\n"
"")
        self.buttonCancel.setShortcut("")
        self.buttonCancel.setAutoDefault(True)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout.addWidget(self.buttonCancel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.buttonOk = QtWidgets.QPushButton(DChoixCata)
        self.buttonOk.setMinimumSize(QtCore.QSize(140, 40))
        self.buttonOk.setStyleSheet("background-color:rgb(104,110,149);\n"
"color :white;\n"
"border-radius : 12px\n"
"\n"
"")
        self.buttonOk.setShortcut("")
        self.buttonOk.setAutoDefault(True)
        self.buttonOk.setDefault(True)
        self.buttonOk.setObjectName("buttonOk")
        self.horizontalLayout.addWidget(self.buttonOk)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DChoixCata)
        QtCore.QMetaObject.connectSlotsByName(DChoixCata)

    def retranslateUi(self, DChoixCata):
        _translate = QtCore.QCoreApplication.translate
        DChoixCata.setWindowTitle(_translate("DChoixCata", "Choix d\'une version du code Aster"))
        self.TLNb.setText(_translate("DChoixCata", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">2 versions sont disponibles</span></p></body></html>"))
        self.buttonCancel.setText(_translate("DChoixCata", "&Cancel"))
        self.buttonOk.setToolTip(_translate("DChoixCata", "Validate choice"))
        self.buttonOk.setText(_translate("DChoixCata", "&OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DChoixCata = QtWidgets.QDialog()
    ui = Ui_DChoixCata()
    ui.setupUi(DChoixCata)
    DChoixCata.show()
    sys.exit(app.exec_())

