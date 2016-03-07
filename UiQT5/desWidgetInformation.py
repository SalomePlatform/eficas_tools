# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetInformation.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetInformative(object):
    def setupUi(self, WidgetInformative):
        WidgetInformative.setObjectName("WidgetInformative")
        WidgetInformative.resize(837, 44)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetInformative.sizePolicy().hasHeightForWidth())
        WidgetInformative.setSizePolicy(sizePolicy)
        WidgetInformative.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(WidgetInformative)
        self.horizontalLayout.setContentsMargins(0, 1, 0, 1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(38, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEditVal = QtWidgets.QLineEdit(WidgetInformative)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVal.sizePolicy().hasHeightForWidth())
        self.lineEditVal.setSizePolicy(sizePolicy)
        self.lineEditVal.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEditVal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditVal.setStyleSheet("background:rgb(255,255,235);\n"
"border:0px;")
        self.lineEditVal.setObjectName("lineEditVal")
        self.horizontalLayout.addWidget(self.lineEditVal)
        spacerItem1 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(WidgetInformative)
        QtCore.QMetaObject.connectSlotsByName(WidgetInformative)

    def retranslateUi(self, WidgetInformative):
        _translate = QtCore.QCoreApplication.translate
        WidgetInformative.setWindowTitle(_translate("WidgetInformative", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetInformative = QtWidgets.QWidget()
    ui = Ui_WidgetInformative()
    ui.setupUi(WidgetInformative)
    WidgetInformative.show()
    sys.exit(app.exec_())

