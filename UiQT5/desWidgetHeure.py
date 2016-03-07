# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetHeure.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetHeure(object):
    def setupUi(self, WidgetHeure):
        WidgetHeure.setObjectName("WidgetHeure")
        WidgetHeure.resize(658, 61)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetHeure.sizePolicy().hasHeightForWidth())
        WidgetHeure.setSizePolicy(sizePolicy)
        WidgetHeure.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(WidgetHeure)
        self.horizontalLayout_3.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.RBValide = MonBoutonValide(WidgetHeure)
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
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.label = MonLabelClic(WidgetHeure)
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
        self.label_2 = QtWidgets.QLabel(WidgetHeure)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.timeEdit = QtWidgets.QTimeEdit(WidgetHeure)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_2.addWidget(self.timeEdit)
        spacerItem2 = QtWidgets.QSpacerItem(454, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.RBPoubelle = QtWidgets.QToolButton(WidgetHeure)
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
        spacerItem3 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(WidgetHeure)
        QtCore.QMetaObject.connectSlotsByName(WidgetHeure)

    def retranslateUi(self, WidgetHeure):
        _translate = QtCore.QCoreApplication.translate
        WidgetHeure.setWindowTitle(_translate("WidgetHeure", "Form"))
        self.RBValide.setToolTip(_translate("WidgetHeure", "Affiche le rapport de validation du mot-clef"))
        self.RBValide.setText(_translate("WidgetHeure", "..."))
        self.label.setText(_translate("WidgetHeure", "<html><head/><body><p>aaa</p><p>dqsklmdqm</p></body></html>"))
        self.label_2.setText(_translate("WidgetHeure", "<html><head/><body><p><br/></p></body></html>"))
        self.RBPoubelle.setToolTip(_translate("WidgetHeure", "Détruit le mot-clef"))
        self.RBPoubelle.setText(_translate("WidgetHeure", "..."))

from monBoutonValide import MonBoutonValide
from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetHeure = QtWidgets.QWidget()
    ui = Ui_WidgetHeure()
    ui.setupUi(WidgetHeure)
    WidgetHeure.show()
    sys.exit(app.exec_())

