# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desViewRegles.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_viewRegles(object):
    def setupUi(self, viewRegles):
        viewRegles.setObjectName("viewRegles")
        viewRegles.resize(411, 322)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(viewRegles)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(viewRegles)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 393, 304))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LBRegles = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.LBRegles.setObjectName("LBRegles")
        self.verticalLayout.addWidget(self.LBRegles)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(viewRegles)
        QtCore.QMetaObject.connectSlotsByName(viewRegles)

    def retranslateUi(self, viewRegles):
        _translate = QtCore.QCoreApplication.translate
        viewRegles.setWindowTitle(_translate("viewRegles", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewRegles = QtWidgets.QDialog()
    ui = Ui_viewRegles()
    ui.setupUi(viewRegles)
    viewRegles.show()
    sys.exit(app.exec_())

