# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidget4a6RadioButton.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget4a6RadioButton(object):
    def setupUi(self, Widget4a6RadioButton):
        Widget4a6RadioButton.setObjectName("Widget4a6RadioButton")
        Widget4a6RadioButton.resize(949, 73)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget4a6RadioButton.sizePolicy().hasHeightForWidth())
        Widget4a6RadioButton.setSizePolicy(sizePolicy)
        Widget4a6RadioButton.setMinimumSize(QtCore.QSize(0, 0))
        Widget4a6RadioButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Widget4a6RadioButton)
        self.horizontalLayout_2.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.RBValide = MonBoutonValide(Widget4a6RadioButton)
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
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.label = MonLabelClic(Widget4a6RadioButton)
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
        self.horizontalLayout_2.addWidget(self.label)
        self.frame = QtWidgets.QFrame(Widget4a6RadioButton)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(1, 0, 1, 0)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_1 = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_1.sizePolicy().hasHeightForWidth())
        self.radioButton_1.setSizePolicy(sizePolicy)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout.addWidget(self.radioButton_1, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 2, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.radioButton_4, 1, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_5.sizePolicy().hasHeightForWidth())
        self.radioButton_5.setSizePolicy(sizePolicy)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout.addWidget(self.radioButton_5, 1, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_6.sizePolicy().hasHeightForWidth())
        self.radioButton_6.setSizePolicy(sizePolicy)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout.addWidget(self.radioButton_6, 1, 2, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(17, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.RBPoubelle = QtWidgets.QToolButton(Widget4a6RadioButton)
        self.RBPoubelle.setMinimumSize(QtCore.QSize(25, 25))
        self.RBPoubelle.setMaximumSize(QtCore.QSize(25, 25))
        self.RBPoubelle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.RBPoubelle.setStyleSheet("border : 0px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Editeur/icons/deleteRond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBPoubelle.setIcon(icon1)
        self.RBPoubelle.setIconSize(QtCore.QSize(25, 25))
        self.RBPoubelle.setObjectName("RBPoubelle")
        self.verticalLayout_4.addWidget(self.RBPoubelle)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.retranslateUi(Widget4a6RadioButton)
        QtCore.QMetaObject.connectSlotsByName(Widget4a6RadioButton)
        Widget4a6RadioButton.setTabOrder(self.radioButton_1, self.radioButton_4)
        Widget4a6RadioButton.setTabOrder(self.radioButton_4, self.RBPoubelle)

    def retranslateUi(self, Widget4a6RadioButton):
        _translate = QtCore.QCoreApplication.translate
        Widget4a6RadioButton.setWindowTitle(_translate("Widget4a6RadioButton", "Form"))
        self.RBValide.setToolTip(_translate("Widget4a6RadioButton", "Affiche le rapport de validation du mot-clef"))
        self.RBValide.setText(_translate("Widget4a6RadioButton", "..."))
        self.label.setText(_translate("Widget4a6RadioButton", "<html><head/><body><p>aaa</p><p>dqsklmdqm</p></body></html>"))
        self.radioButton_1.setText(_translate("Widget4a6RadioButton", "RadioButton"))
        self.radioButton_2.setText(_translate("Widget4a6RadioButton", "RadioButton"))
        self.radioButton_3.setText(_translate("Widget4a6RadioButton", "RadioButton"))
        self.radioButton_4.setText(_translate("Widget4a6RadioButton", "RadioButton"))
        self.radioButton_5.setText(_translate("Widget4a6RadioButton", "RadioButton"))
        self.radioButton_6.setText(_translate("Widget4a6RadioButton", "RadioButton"))
        self.RBPoubelle.setToolTip(_translate("Widget4a6RadioButton", "Détruit le mot-clef"))
        self.RBPoubelle.setText(_translate("Widget4a6RadioButton", "..."))

from monBoutonValide import MonBoutonValide
from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget4a6RadioButton = QtWidgets.QWidget()
    ui = Ui_Widget4a6RadioButton()
    ui.setupUi(Widget4a6RadioButton)
    Widget4a6RadioButton.show()
    sys.exit(app.exec_())

