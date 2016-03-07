# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetCB.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetCB(object):
    def setupUi(self, WidgetCB):
        WidgetCB.setObjectName("WidgetCB")
        WidgetCB.resize(739, 63)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetCB.sizePolicy().hasHeightForWidth())
        WidgetCB.setSizePolicy(sizePolicy)
        WidgetCB.setMinimumSize(QtCore.QSize(0, 0))
        WidgetCB.setMaximumSize(QtCore.QSize(1493, 85))
        WidgetCB.setStyleSheet("QComboBox{combobox-popup:0;};")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(WidgetCB)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.RBValide = MonBoutonValide(WidgetCB)
        self.RBValide.setMinimumSize(QtCore.QSize(21, 25))
        self.RBValide.setMaximumSize(QtCore.QSize(21, 25))
        self.RBValide.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.RBValide.setStyleSheet("border : 0px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Editeur/icons/ast-green-ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBValide.setIcon(icon)
        self.RBValide.setIconSize(QtCore.QSize(25, 25))
        self.RBValide.setObjectName("RBValide")
        self.horizontalLayout.addWidget(self.RBValide)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.label = MonLabelClic(WidgetCB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(300, 25))
        self.label.setMaximumSize(QtCore.QSize(178, 16777215))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CBChoix = QtWidgets.QComboBox(WidgetCB)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CBChoix.sizePolicy().hasHeightForWidth())
        self.CBChoix.setSizePolicy(sizePolicy)
        self.CBChoix.setMinimumSize(QtCore.QSize(361, 25))
        self.CBChoix.setAccessibleName("")
        self.CBChoix.setAccessibleDescription("")
        self.CBChoix.setStyleSheet("QComboBox {\n"
" background:rgb(235,235,235);\n"
" }\n"
"/*QComboBox: on {\n"
"  font : italic\n"
" }\n"
"background:rgb(235,235,235);\n"
"border:0px;\n"
"\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"background: black;\n"
"    font : italic 14px\n"
" }\n"
"QComboBox:on { \n"
"  font : italic 20px;\n"
"  background: red ;\n"
"}/*\n"
"")
        self.CBChoix.setMaxVisibleItems(100)
        self.CBChoix.setFrame(False)
        self.CBChoix.setObjectName("CBChoix")
        self.horizontalLayout_2.addWidget(self.CBChoix)
        spacerItem2 = QtWidgets.QSpacerItem(301, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.RBPoubelle = QtWidgets.QToolButton(WidgetCB)
        self.RBPoubelle.setMinimumSize(QtCore.QSize(21, 25))
        self.RBPoubelle.setMaximumSize(QtCore.QSize(21, 25))
        self.RBPoubelle.setStyleSheet("border : 0px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Editeur/icons/deleteRond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBPoubelle.setIcon(icon1)
        self.RBPoubelle.setIconSize(QtCore.QSize(25, 25))
        self.RBPoubelle.setObjectName("RBPoubelle")
        self.horizontalLayout_2.addWidget(self.RBPoubelle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(WidgetCB)
        QtCore.QMetaObject.connectSlotsByName(WidgetCB)

    def retranslateUi(self, WidgetCB):
        _translate = QtCore.QCoreApplication.translate
        WidgetCB.setWindowTitle(_translate("WidgetCB", "Form"))
        self.RBValide.setToolTip(_translate("WidgetCB", "Affiche le rapport de validation du mot-clef"))
        self.RBValide.setText(_translate("WidgetCB", "..."))
        self.label.setText(_translate("WidgetCB", "<html><head/><body><p>aaa</p><p>dqsklmdqm</p></body></html>"))
        self.RBPoubelle.setToolTip(_translate("WidgetCB", "Détruit le mot-clef"))
        self.RBPoubelle.setText(_translate("WidgetCB", "..."))

from monBoutonValide import MonBoutonValide
from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetCB = QtWidgets.QWidget()
    ui = Ui_WidgetCB()
    ui.setupUi(WidgetCB)
    WidgetCB.show()
    sys.exit(app.exec_())

