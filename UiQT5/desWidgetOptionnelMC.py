# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetOptionnelMC.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_desWidgetOptionnel(object):
    def setupUi(self, desWidgetOptionnel):
        desWidgetOptionnel.setObjectName("desWidgetOptionnel")
        desWidgetOptionnel.resize(384, 218)
        self.verticalLayout = QtWidgets.QVBoxLayout(desWidgetOptionnel)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line = QtWidgets.QFrame(desWidgetOptionnel)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.nomMC = MonLabelClic(desWidgetOptionnel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nomMC.sizePolicy().hasHeightForWidth())
        self.nomMC.setSizePolicy(sizePolicy)
        self.nomMC.setMinimumSize(QtCore.QSize(0, 25))
        self.nomMC.setMaximumSize(QtCore.QSize(12121213, 25))
        self.nomMC.setObjectName("nomMC")
        self.horizontalLayout.addWidget(self.nomMC)
        self.line_2 = QtWidgets.QFrame(desWidgetOptionnel)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollAreaCommandesOptionnelles = QtWidgets.QScrollArea(desWidgetOptionnel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaCommandesOptionnelles.sizePolicy().hasHeightForWidth())
        self.scrollAreaCommandesOptionnelles.setSizePolicy(sizePolicy)
        self.scrollAreaCommandesOptionnelles.setStyleSheet("background : rgb(247,247,247)")
        self.scrollAreaCommandesOptionnelles.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaCommandesOptionnelles.setLineWidth(0)
        self.scrollAreaCommandesOptionnelles.setWidgetResizable(True)
        self.scrollAreaCommandesOptionnelles.setObjectName("scrollAreaCommandesOptionnelles")
        self.commandesOptionnellesWidget = QtWidgets.QWidget()
        self.commandesOptionnellesWidget.setGeometry(QtCore.QRect(0, 0, 384, 185))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandesOptionnellesWidget.sizePolicy().hasHeightForWidth())
        self.commandesOptionnellesWidget.setSizePolicy(sizePolicy)
        self.commandesOptionnellesWidget.setObjectName("commandesOptionnellesWidget")
        self.commandesOptionnellesLayout = QtWidgets.QVBoxLayout(self.commandesOptionnellesWidget)
        self.commandesOptionnellesLayout.setObjectName("commandesOptionnellesLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.commandesOptionnellesLayout.addItem(spacerItem)
        self.scrollAreaCommandesOptionnelles.setWidget(self.commandesOptionnellesWidget)
        self.verticalLayout.addWidget(self.scrollAreaCommandesOptionnelles)

        self.retranslateUi(desWidgetOptionnel)
        QtCore.QMetaObject.connectSlotsByName(desWidgetOptionnel)

    def retranslateUi(self, desWidgetOptionnel):
        _translate = QtCore.QCoreApplication.translate
        desWidgetOptionnel.setWindowTitle(_translate("desWidgetOptionnel", "Form"))
        self.nomMC.setText(_translate("desWidgetOptionnel", "TextLabel"))

from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desWidgetOptionnel = QtWidgets.QWidget()
    ui = Ui_desWidgetOptionnel()
    ui.setupUi(desWidgetOptionnel)
    desWidgetOptionnel.show()
    sys.exit(app.exec_())

