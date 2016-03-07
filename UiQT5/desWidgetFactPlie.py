# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetFactPlie.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetFactPlie(object):
    def setupUi(self, WidgetFactPlie):
        WidgetFactPlie.setObjectName("WidgetFactPlie")
        WidgetFactPlie.resize(727, 27)
        WidgetFactPlie.setStyleSheet(" QGroupBox {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 1ex; /* leave space at the top for the title */\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     padding: 0 3px;\n"
" }")
        self.horizontalLayout = QtWidgets.QHBoxLayout(WidgetFactPlie)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RBDeplie = QtWidgets.QToolButton(WidgetFactPlie)
        self.RBDeplie.setMinimumSize(QtCore.QSize(21, 15))
        self.RBDeplie.setMaximumSize(QtCore.QSize(21, 21))
        self.RBDeplie.setStyleSheet("border : 0px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Editeur/icons/plusnode.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBDeplie.setIcon(icon)
        self.RBDeplie.setIconSize(QtCore.QSize(25, 25))
        self.RBDeplie.setObjectName("RBDeplie")
        self.horizontalLayout.addWidget(self.RBDeplie)
        self.widget_5 = QtWidgets.QWidget(WidgetFactPlie)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.RBValide = MonBoutonValide(self.widget_5)
        self.RBValide.setMinimumSize(QtCore.QSize(17, 25))
        self.RBValide.setMaximumSize(QtCore.QSize(21, 25))
        self.RBValide.setStyleSheet("border : 0px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Editeur/icons/ast-green-ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBValide.setIcon(icon1)
        self.RBValide.setIconSize(QtCore.QSize(25, 25))
        self.RBValide.setObjectName("RBValide")
        self.horizontalLayout_5.addWidget(self.RBValide)
        self.horizontalLayout.addWidget(self.widget_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(22)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = MonLabelClic(WidgetFactPlie)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 25))
        self.groupBox.setMaximumSize(QtCore.QSize(12121213, 25))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.line_5 = QtWidgets.QFrame(WidgetFactPlie)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setMinimumSize(QtCore.QSize(500, 0))
        self.line_5.setMaximumSize(QtCore.QSize(1500, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.RBPoubelle = QtWidgets.QToolButton(WidgetFactPlie)
        self.RBPoubelle.setMinimumSize(QtCore.QSize(21, 25))
        self.RBPoubelle.setMaximumSize(QtCore.QSize(21, 25))
        self.RBPoubelle.setStyleSheet("border : 0px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Editeur/icons/deleteRond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBPoubelle.setIcon(icon2)
        self.RBPoubelle.setIconSize(QtCore.QSize(25, 25))
        self.RBPoubelle.setObjectName("RBPoubelle")
        self.horizontalLayout_2.addWidget(self.RBPoubelle)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(WidgetFactPlie)
        QtCore.QMetaObject.connectSlotsByName(WidgetFactPlie)

    def retranslateUi(self, WidgetFactPlie):
        _translate = QtCore.QCoreApplication.translate
        WidgetFactPlie.setWindowTitle(_translate("WidgetFactPlie", "Form"))
        self.RBDeplie.setText(_translate("WidgetFactPlie", "..."))
        self.RBValide.setText(_translate("WidgetFactPlie", "..."))
        self.groupBox.setText(_translate("WidgetFactPlie", "TextLabel"))
        self.RBPoubelle.setText(_translate("WidgetFactPlie", "..."))

from monBoutonValide import MonBoutonValide
from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetFactPlie = QtWidgets.QWidget()
    ui = Ui_WidgetFactPlie()
    ui.setupUi(WidgetFactPlie)
    WidgetFactPlie.show()
    sys.exit(app.exec_())

