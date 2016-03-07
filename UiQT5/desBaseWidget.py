# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desBaseWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_baseWidget(object):
    def setupUi(self, baseWidget):
        baseWidget.setObjectName("baseWidget")
        baseWidget.resize(1038, 557)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(baseWidget.sizePolicy().hasHeightForWidth())
        baseWidget.setSizePolicy(sizePolicy)
        baseWidget.setMinimumSize(QtCore.QSize(0, 0))
        baseWidget.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(baseWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(baseWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widgetTree = QtWidgets.QWidget(self.splitter)
        self.widgetTree.setStyleSheet("background:rgb(247,247,247);\n"
"\n"
"")
        self.widgetTree.setObjectName("widgetTree")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widgetTree)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgetCentrale = QtWidgets.QWidget(self.splitter)
        self.widgetCentrale.setObjectName("widgetCentrale")
        self.widgetCentraleLayout = QtWidgets.QVBoxLayout(self.widgetCentrale)
        self.widgetCentraleLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetCentraleLayout.setSpacing(6)
        self.widgetCentraleLayout.setObjectName("widgetCentraleLayout")
        self.verticalLayout.addWidget(self.splitter)
        self.labelCommentaire = QtWidgets.QLabel(baseWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCommentaire.sizePolicy().hasHeightForWidth())
        self.labelCommentaire.setSizePolicy(sizePolicy)
        self.labelCommentaire.setMinimumSize(QtCore.QSize(0, 0))
        self.labelCommentaire.setStyleSheet("")
        self.labelCommentaire.setText("")
        self.labelCommentaire.setObjectName("labelCommentaire")
        self.verticalLayout.addWidget(self.labelCommentaire)

        self.retranslateUi(baseWidget)
        QtCore.QMetaObject.connectSlotsByName(baseWidget)

    def retranslateUi(self, baseWidget):
        _translate = QtCore.QCoreApplication.translate
        baseWidget.setWindowTitle(_translate("baseWidget", "DMacro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    baseWidget = QtWidgets.QWidget()
    ui = Ui_baseWidget()
    ui.setupUi(baseWidget)
    baseWidget.show()
    sys.exit(app.exec_())

