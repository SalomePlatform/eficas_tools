# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetSimpComplexe.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetSimpComplexe(object):
    def setupUi(self, WidgetSimpComplexe):
        WidgetSimpComplexe.setObjectName("WidgetSimpComplexe")
        WidgetSimpComplexe.resize(1242, 87)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetSimpComplexe.sizePolicy().hasHeightForWidth())
        WidgetSimpComplexe.setSizePolicy(sizePolicy)
        WidgetSimpComplexe.setMinimumSize(QtCore.QSize(940, 0))
        WidgetSimpComplexe.setMaximumSize(QtCore.QSize(1493, 1400))
        WidgetSimpComplexe.setStyleSheet("QLineEdit {\n"
"background:rgb(235,235,235);\n"
"border:0px;\n"
"}")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(WidgetSimpComplexe)
        self.horizontalLayout_5.setContentsMargins(0, 1, 0, 1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.RBValide = MonBoutonValide(WidgetSimpComplexe)
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
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.label = MonLabelClic(WidgetSimpComplexe)
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
        self.horizontalLayout_5.addWidget(self.label)
        self.frame = QtWidgets.QFrame(WidgetSimpComplexe)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 29))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 29))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(19, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.LEComp = QtWidgets.QLineEdit(self.frame)
        self.LEComp.setFrame(False)
        self.LEComp.setObjectName("LEComp")
        self.gridLayout.addWidget(self.LEComp, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(50, 24))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(4, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RBRI = QtWidgets.QRadioButton(self.frame)
        self.RBRI.setObjectName("RBRI")
        self.horizontalLayout_2.addWidget(self.RBRI)
        self.RBMP = QtWidgets.QRadioButton(self.frame)
        self.RBMP.setObjectName("RBMP")
        self.horizontalLayout_2.addWidget(self.RBMP)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LEReel = QtWidgets.QLineEdit(self.frame)
        self.LEReel.setFrame(False)
        self.LEReel.setObjectName("LEReel")
        self.horizontalLayout_3.addWidget(self.LEReel)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.LEImag = QtWidgets.QLineEdit(self.frame)
        self.LEImag.setFrame(False)
        self.LEImag.setObjectName("LEImag")
        self.horizontalLayout_3.addWidget(self.LEImag)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.RBPoubelle = QtWidgets.QToolButton(WidgetSimpComplexe)
        self.RBPoubelle.setMinimumSize(QtCore.QSize(21, 31))
        self.RBPoubelle.setMaximumSize(QtCore.QSize(21, 31))
        self.RBPoubelle.setStyleSheet("border : 0px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Editeur/icons/deleteRond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBPoubelle.setIcon(icon1)
        self.RBPoubelle.setIconSize(QtCore.QSize(32, 32))
        self.RBPoubelle.setObjectName("RBPoubelle")
        self.verticalLayout_3.addWidget(self.RBPoubelle)
        spacerItem5 = QtWidgets.QSpacerItem(18, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.retranslateUi(WidgetSimpComplexe)
        QtCore.QMetaObject.connectSlotsByName(WidgetSimpComplexe)
        WidgetSimpComplexe.setTabOrder(self.LEComp, self.RBRI)
        WidgetSimpComplexe.setTabOrder(self.RBRI, self.RBMP)
        WidgetSimpComplexe.setTabOrder(self.RBMP, self.RBPoubelle)

    def retranslateUi(self, WidgetSimpComplexe):
        _translate = QtCore.QCoreApplication.translate
        WidgetSimpComplexe.setWindowTitle(_translate("WidgetSimpComplexe", "Form"))
        self.RBValide.setToolTip(_translate("WidgetSimpComplexe", "Affiche le rapport de validation du mot-clef"))
        self.RBValide.setText(_translate("WidgetSimpComplexe", "..."))
        self.label.setText(_translate("WidgetSimpComplexe", "<html><head/><body><p>aaa</p><p>dqsklmdqm</p></body></html>"))
        self.label_2.setText(_translate("WidgetSimpComplexe", "Complexe : a+bj"))
        self.label_3.setText(_translate("WidgetSimpComplexe", "<html><head/><body><p align=\"center\">OU </p></body></html>"))
        self.RBRI.setText(_translate("WidgetSimpComplexe", "Réel/Imaginaire"))
        self.RBMP.setText(_translate("WidgetSimpComplexe", "Module/Phase"))
        self.RBPoubelle.setText(_translate("WidgetSimpComplexe", "..."))

from monBoutonValide import MonBoutonValide
from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetSimpComplexe = QtWidgets.QWidget()
    ui = Ui_WidgetSimpComplexe()
    ui.setupUi(WidgetSimpComplexe)
    WidgetSimpComplexe.show()
    sys.exit(app.exec_())

