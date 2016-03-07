# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetOptionnel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetOptionnel(object):
    def setupUi(self, WidgetOptionnel):
        WidgetOptionnel.setObjectName("WidgetOptionnel")
        WidgetOptionnel.resize(297, 199)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetOptionnel.sizePolicy().hasHeightForWidth())
        WidgetOptionnel.setSizePolicy(sizePolicy)
        WidgetOptionnel.setMinimumSize(QtCore.QSize(0, 0))
        WidgetOptionnel.setStyleSheet("background-color : rgb(224,223,222);\n"
"font : \'times\' 9px")
        self.verticalLayout = QtWidgets.QVBoxLayout(WidgetOptionnel)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(WidgetOptionnel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.GeneaLabel = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GeneaLabel.sizePolicy().hasHeightForWidth())
        self.GeneaLabel.setSizePolicy(sizePolicy)
        self.GeneaLabel.setMinimumSize(QtCore.QSize(0, 31))
        self.GeneaLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.GeneaLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GeneaLabel.setObjectName("GeneaLabel")
        self.horizontalLayout.addWidget(self.GeneaLabel)
        spacerItem = QtWidgets.QSpacerItem(1037, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_2)
        self.widget_2 = QtWidgets.QWidget(WidgetOptionnel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollAreaCommandesOptionnelles = QtWidgets.QScrollArea(self.widget_2)
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
        self.commandesOptionnellesWidget.setGeometry(QtCore.QRect(0, 0, 279, 124))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandesOptionnellesWidget.sizePolicy().hasHeightForWidth())
        self.commandesOptionnellesWidget.setSizePolicy(sizePolicy)
        self.commandesOptionnellesWidget.setObjectName("commandesOptionnellesWidget")
        self.commandesOptionnellesLayout = QtWidgets.QVBoxLayout(self.commandesOptionnellesWidget)
        self.commandesOptionnellesLayout.setContentsMargins(11, 11, 11, 11)
        self.commandesOptionnellesLayout.setSpacing(6)
        self.commandesOptionnellesLayout.setObjectName("commandesOptionnellesLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.commandesOptionnellesLayout.addItem(spacerItem1)
        self.scrollAreaCommandesOptionnelles.setWidget(self.commandesOptionnellesWidget)
        self.verticalLayout_3.addWidget(self.scrollAreaCommandesOptionnelles)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(WidgetOptionnel)
        QtCore.QMetaObject.connectSlotsByName(WidgetOptionnel)

    def retranslateUi(self, WidgetOptionnel):
        _translate = QtCore.QCoreApplication.translate
        WidgetOptionnel.setWindowTitle(_translate("WidgetOptionnel", "WidgetOptionnel"))
        self.GeneaLabel.setText(_translate("WidgetOptionnel", "<html><head/><body><p><span style=\" color:#0000ff;\">commande </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetOptionnel = QtWidgets.QWidget()
    ui = Ui_WidgetOptionnel()
    ui.setupUi(WidgetOptionnel)
    WidgetOptionnel.show()
    sys.exit(app.exec_())

