# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetUniqueSDCO.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetUniqueSDCO(object):
    def setupUi(self, WidgetUniqueSDCO):
        WidgetUniqueSDCO.setObjectName("WidgetUniqueSDCO")
        WidgetUniqueSDCO.resize(1069, 56)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetUniqueSDCO.sizePolicy().hasHeightForWidth())
        WidgetUniqueSDCO.setSizePolicy(sizePolicy)
        WidgetUniqueSDCO.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(WidgetUniqueSDCO)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.RBValide = MonBoutonValide(WidgetUniqueSDCO)
        self.RBValide.setMinimumSize(QtCore.QSize(21, 25))
        self.RBValide.setMaximumSize(QtCore.QSize(21, 25))
        self.RBValide.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.RBValide.setStyleSheet("border : 0px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Editeur/icons/ast-green-ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBValide.setIcon(icon)
        self.RBValide.setIconSize(QtCore.QSize(25, 25))
        self.RBValide.setObjectName("RBValide")
        self.horizontalLayout_3.addWidget(self.RBValide)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label = MonLabelClic(WidgetUniqueSDCO)
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
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LESDCO = QtWidgets.QLineEdit(WidgetUniqueSDCO)
        self.LESDCO.setMinimumSize(QtCore.QSize(0, 25))
        self.LESDCO.setMaximumSize(QtCore.QSize(805, 16777215))
        self.LESDCO.setStyleSheet("background:rgb(235,235,235);\n"
"border:0px;")
        self.LESDCO.setObjectName("LESDCO")
        self.verticalLayout.addWidget(self.LESDCO)
        self.label_2 = QtWidgets.QLabel(WidgetUniqueSDCO)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(79, 17, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.RBPoubelle = QtWidgets.QToolButton(WidgetUniqueSDCO)
        self.RBPoubelle.setMinimumSize(QtCore.QSize(21, 25))
        self.RBPoubelle.setMaximumSize(QtCore.QSize(21, 25))
        self.RBPoubelle.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.RBPoubelle.setStyleSheet("border : 0px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Editeur/icons/deleteRond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBPoubelle.setIcon(icon1)
        self.RBPoubelle.setIconSize(QtCore.QSize(25, 25))
        self.RBPoubelle.setObjectName("RBPoubelle")
        self.verticalLayout_3.addWidget(self.RBPoubelle)
        spacerItem3 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(WidgetUniqueSDCO)
        QtCore.QMetaObject.connectSlotsByName(WidgetUniqueSDCO)

    def retranslateUi(self, WidgetUniqueSDCO):
        _translate = QtCore.QCoreApplication.translate
        WidgetUniqueSDCO.setWindowTitle(_translate("WidgetUniqueSDCO", "Form"))
        self.RBValide.setToolTip(_translate("WidgetUniqueSDCO", "Affiche le rapport de validation du mot-clef"))
        self.RBValide.setText(_translate("WidgetUniqueSDCO", "..."))
        self.label.setText(_translate("WidgetUniqueSDCO", "<html><head/><body><p>aaa</p><p>dqsklmdqm</p></body></html>"))
        self.label_2.setText(_translate("WidgetUniqueSDCO", "Attend un objet de type CO "))
        self.RBPoubelle.setToolTip(_translate("WidgetUniqueSDCO", "Détruit le mot-clef"))
        self.RBPoubelle.setText(_translate("WidgetUniqueSDCO", "..."))

from monBoutonValide import MonBoutonValide
from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetUniqueSDCO = QtWidgets.QWidget()
    ui = Ui_WidgetUniqueSDCO()
    ui.setupUi(WidgetUniqueSDCO)
    WidgetUniqueSDCO.show()
    sys.exit(app.exec_())

