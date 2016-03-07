# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetCreeParam.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_desWidgetCreeParam(object):
    def setupUi(self, desWidgetCreeParam):
        desWidgetCreeParam.setObjectName("desWidgetCreeParam")
        desWidgetCreeParam.resize(728, 530)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(desWidgetCreeParam)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(desWidgetCreeParam)
        self.scrollArea.setMinimumSize(QtCore.QSize(701, 291))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 710, 349))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LBParam = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBParam.sizePolicy().hasHeightForWidth())
        self.LBParam.setSizePolicy(sizePolicy)
        self.LBParam.setMinimumSize(QtCore.QSize(701, 291))
        self.LBParam.setStyleSheet("alternate-background-color:rgb(235,235,235); \n"
"background-color: rgb(247,247,247);\n"
"")
        self.LBParam.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBParam.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LBParam.setAlternatingRowColors(True)
        self.LBParam.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.LBParam.setObjectName("LBParam")
        self.verticalLayout.addWidget(self.LBParam)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(desWidgetCreeParam)
        self.frame.setMinimumSize(QtCore.QSize(701, 131))
        self.frame.setStyleSheet("background:rgb(247,247,247)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 531, 70))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditVal = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditVal.setMinimumSize(QtCore.QSize(231, 31))
        self.lineEditVal.setStyleSheet("background:rgb(235,235,235);\n"
"border:0px;")
        self.lineEditVal.setFrame(False)
        self.lineEditVal.setObjectName("lineEditVal")
        self.gridLayout.addWidget(self.lineEditVal, 1, 1, 1, 1)
        self.textLabel2_2 = QtWidgets.QLabel(self.layoutWidget)
        self.textLabel2_2.setWordWrap(False)
        self.textLabel2_2.setObjectName("textLabel2_2")
        self.gridLayout.addWidget(self.textLabel2_2, 0, 0, 1, 1)
        self.lineEditNom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditNom.setMinimumSize(QtCore.QSize(231, 31))
        self.lineEditNom.setStyleSheet("background:rgb(235,235,235);\n"
"border:0px;")
        self.lineEditNom.setFrame(False)
        self.lineEditNom.setObjectName("lineEditNom")
        self.gridLayout.addWidget(self.lineEditNom, 0, 1, 1, 1)
        self.textLabel2 = QtWidgets.QLabel(self.layoutWidget)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")
        self.gridLayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 10, 531, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textLabel2_2_2 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel2_2_2.sizePolicy().hasHeightForWidth())
        self.textLabel2_2_2.setSizePolicy(sizePolicy)
        self.textLabel2_2_2.setWordWrap(False)
        self.textLabel2_2_2.setObjectName("textLabel2_2_2")
        self.horizontalLayout_2.addWidget(self.textLabel2_2_2)
        spacerItem1 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(desWidgetCreeParam)
        QtCore.QMetaObject.connectSlotsByName(desWidgetCreeParam)

    def retranslateUi(self, desWidgetCreeParam):
        _translate = QtCore.QCoreApplication.translate
        desWidgetCreeParam.setWindowTitle(_translate("desWidgetCreeParam", "Gestion des Paramètres"))
        self.textLabel2_2.setText(_translate("desWidgetCreeParam", "<html><head/><body><p>Nom: </p></body></html>"))
        self.textLabel2.setText(_translate("desWidgetCreeParam", "<html><head/><body><p>Valeur: </p></body></html>"))
        self.textLabel2_2_2.setText(_translate("desWidgetCreeParam", "<html><head/><body><p><span style=\" text-decoration: underline;\">Créer un paramètre</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desWidgetCreeParam = QtWidgets.QWidget()
    ui = Ui_desWidgetCreeParam()
    ui.setupUi(desWidgetCreeParam)
    desWidgetCreeParam.show()
    sys.exit(app.exec_())

