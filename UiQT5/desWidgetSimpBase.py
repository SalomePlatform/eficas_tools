# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetSimpBase.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetSimpBase(object):
    def setupUi(self, WidgetSimpBase):
        WidgetSimpBase.setObjectName("WidgetSimpBase")
        WidgetSimpBase.resize(743, 60)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetSimpBase.sizePolicy().hasHeightForWidth())
        WidgetSimpBase.setSizePolicy(sizePolicy)
        WidgetSimpBase.setMinimumSize(QtCore.QSize(0, 0))
        WidgetSimpBase.setMaximumSize(QtCore.QSize(1677721, 60))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(WidgetSimpBase)
        self.horizontalLayout_3.setContentsMargins(0, 1, 0, 1)
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
        self.RBValide = MonBoutonValide(WidgetSimpBase)
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
        self.label = MonLabelClic(WidgetSimpBase)
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
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditVal = QtWidgets.QLineEdit(WidgetSimpBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVal.sizePolicy().hasHeightForWidth())
        self.lineEditVal.setSizePolicy(sizePolicy)
        self.lineEditVal.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEditVal.setMaximumSize(QtCore.QSize(805, 16777215))
        self.lineEditVal.setStyleSheet("background:rgb(235,235,235);\n"
"border:0px;")
        self.lineEditVal.setObjectName("lineEditVal")
        self.horizontalLayout_2.addWidget(self.lineEditVal)
        spacerItem2 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.RBPoubelle = QtWidgets.QToolButton(WidgetSimpBase)
        self.RBPoubelle.setMinimumSize(QtCore.QSize(21, 25))
        self.RBPoubelle.setMaximumSize(QtCore.QSize(21, 25))
        self.RBPoubelle.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.RBPoubelle.setStyleSheet("border : 0px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Editeur/icons/deleteRond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBPoubelle.setIcon(icon1)
        self.RBPoubelle.setIconSize(QtCore.QSize(25, 25))
        self.RBPoubelle.setObjectName("RBPoubelle")
        self.horizontalLayout_2.addWidget(self.RBPoubelle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(WidgetSimpBase)
        QtCore.QMetaObject.connectSlotsByName(WidgetSimpBase)

    def retranslateUi(self, WidgetSimpBase):
        _translate = QtCore.QCoreApplication.translate
        WidgetSimpBase.setWindowTitle(_translate("WidgetSimpBase", "Form"))
        self.RBValide.setToolTip(_translate("WidgetSimpBase", "Affiche le rapport de validation du mot-clef"))
        self.RBValide.setText(_translate("WidgetSimpBase", "..."))
        self.label.setText(_translate("WidgetSimpBase", "<html><head/><body><p>aaa</p><p>dqsklmdqm</p></body></html>"))
        self.RBPoubelle.setToolTip(_translate("WidgetSimpBase", "Détruit le mot-clef"))
        self.RBPoubelle.setText(_translate("WidgetSimpBase", "..."))

from monBoutonValide import MonBoutonValide
from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetSimpBase = QtWidgets.QWidget()
    ui = Ui_WidgetSimpBase()
    ui.setupUi(WidgetSimpBase)
    WidgetSimpBase.show()
    sys.exit(app.exec_())

