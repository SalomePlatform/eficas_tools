# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetPlusieursInto.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetPlusieursInto(object):
    def setupUi(self, WidgetPlusieursInto):
        WidgetPlusieursInto.setObjectName("WidgetPlusieursInto")
        WidgetPlusieursInto.resize(938, 236)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetPlusieursInto.sizePolicy().hasHeightForWidth())
        WidgetPlusieursInto.setSizePolicy(sizePolicy)
        WidgetPlusieursInto.setMinimumSize(QtCore.QSize(0, 60))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(WidgetPlusieursInto)
        self.horizontalLayout_2.setContentsMargins(0, 2, 2, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BFermeListe = QtWidgets.QToolButton(WidgetPlusieursInto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BFermeListe.sizePolicy().hasHeightForWidth())
        self.BFermeListe.setSizePolicy(sizePolicy)
        self.BFermeListe.setMaximumSize(QtCore.QSize(21, 25))
        self.BFermeListe.setStyleSheet("border:0px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Editeur/icons/minusnode.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BFermeListe.setIcon(icon)
        self.BFermeListe.setIconSize(QtCore.QSize(25, 25))
        self.BFermeListe.setObjectName("BFermeListe")
        self.horizontalLayout.addWidget(self.BFermeListe)
        self.RBValide = MonBoutonValide(WidgetPlusieursInto)
        self.RBValide.setMinimumSize(QtCore.QSize(21, 25))
        self.RBValide.setMaximumSize(QtCore.QSize(21, 25))
        self.RBValide.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.RBValide.setStyleSheet("border : 0px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Editeur/icons/ast-green-ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBValide.setIcon(icon1)
        self.RBValide.setIconSize(QtCore.QSize(25, 25))
        self.RBValide.setObjectName("RBValide")
        self.horizontalLayout.addWidget(self.RBValide)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = MonLabelClic(WidgetPlusieursInto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(280, 25))
        self.label.setMaximumSize(QtCore.QSize(280, 16777215))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.scrollArea_2 = QtWidgets.QScrollArea(WidgetPlusieursInto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(300, 0))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 300, 166))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.monCommentaireLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monCommentaireLabel.sizePolicy().hasHeightForWidth())
        self.monCommentaireLabel.setSizePolicy(sizePolicy)
        self.monCommentaireLabel.setMinimumSize(QtCore.QSize(78, 25))
        self.monCommentaireLabel.setMaximumSize(QtCore.QSize(278, 16777215))
        self.monCommentaireLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.monCommentaireLabel.setScaledContents(False)
        self.monCommentaireLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.monCommentaireLabel.setObjectName("monCommentaireLabel")
        self.gridLayout_2.addWidget(self.monCommentaireLabel, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(WidgetPlusieursInto)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("background : rgb(247,247,247)")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.scrollArea.setObjectName("scrollArea")
        self.verticalWidgetLE = QtWidgets.QWidget()
        self.verticalWidgetLE.setGeometry(QtCore.QRect(0, 0, 543, 232))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidgetLE.sizePolicy().hasHeightForWidth())
        self.verticalWidgetLE.setSizePolicy(sizePolicy)
        self.verticalWidgetLE.setObjectName("verticalWidgetLE")
        self.CBLayout = QtWidgets.QVBoxLayout(self.verticalWidgetLE)
        self.CBLayout.setContentsMargins(0, 0, 0, 0)
        self.CBLayout.setSpacing(0)
        self.CBLayout.setObjectName("CBLayout")
        self.scrollArea.setWidget(self.verticalWidgetLE)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        spacerItem1 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.RBPoubelle = QtWidgets.QToolButton(WidgetPlusieursInto)
        self.RBPoubelle.setMinimumSize(QtCore.QSize(21, 31))
        self.RBPoubelle.setMaximumSize(QtCore.QSize(21, 31))
        self.RBPoubelle.setStyleSheet("border : 0px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Editeur/icons/deleteRond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBPoubelle.setIcon(icon2)
        self.RBPoubelle.setIconSize(QtCore.QSize(32, 32))
        self.RBPoubelle.setObjectName("RBPoubelle")
        self.verticalLayout.addWidget(self.RBPoubelle)
        self.CBCheck = QtWidgets.QCheckBox(WidgetPlusieursInto)
        self.CBCheck.setText("")
        self.CBCheck.setChecked(True)
        self.CBCheck.setObjectName("CBCheck")
        self.verticalLayout.addWidget(self.CBCheck)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.raise_()

        self.retranslateUi(WidgetPlusieursInto)
        QtCore.QMetaObject.connectSlotsByName(WidgetPlusieursInto)

    def retranslateUi(self, WidgetPlusieursInto):
        _translate = QtCore.QCoreApplication.translate
        WidgetPlusieursInto.setWindowTitle(_translate("WidgetPlusieursInto", "Form"))
        self.BFermeListe.setToolTip(_translate("WidgetPlusieursInto", "permet de gérer la liste"))
        self.BFermeListe.setText(_translate("WidgetPlusieursInto", "..."))
        self.RBValide.setToolTip(_translate("WidgetPlusieursInto", "Affiche le rapport de validation du mot-clef"))
        self.RBValide.setText(_translate("WidgetPlusieursInto", "..."))
        self.label.setText(_translate("WidgetPlusieursInto", "<html><head/><body><p>aaa</p><p>dqsklmdqm</p></body></html>"))
        self.monCommentaireLabel.setText(_translate("WidgetPlusieursInto", "<html><head/><body><p>aaa</p><p>dqsklmdqm</p></body></html>"))
        self.RBPoubelle.setToolTip(_translate("WidgetPlusieursInto", "Détruit le mot-clef"))
        self.RBPoubelle.setText(_translate("WidgetPlusieursInto", "..."))

from monBoutonValide import MonBoutonValide
from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetPlusieursInto = QtWidgets.QWidget()
    ui = Ui_WidgetPlusieursInto()
    ui.setupUi(WidgetPlusieursInto)
    WidgetPlusieursInto.show()
    sys.exit(app.exec_())

