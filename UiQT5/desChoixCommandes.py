# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desChoixCommandes.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChoixCommandes(object):
    def setupUi(self, ChoixCommandes):
        ChoixCommandes.setObjectName("ChoixCommandes")
        ChoixCommandes.resize(1244, 652)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChoixCommandes.sizePolicy().hasHeightForWidth())
        ChoixCommandes.setSizePolicy(sizePolicy)
        ChoixCommandes.setMinimumSize(QtCore.QSize(505, 0))
        ChoixCommandes.setStyleSheet("background-color : rgb(248,247,246)")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(ChoixCommandes)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frameAffichage = QtWidgets.QFrame(ChoixCommandes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameAffichage.sizePolicy().hasHeightForWidth())
        self.frameAffichage.setSizePolicy(sizePolicy)
        self.frameAffichage.setMinimumSize(QtCore.QSize(0, 130))
        self.frameAffichage.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frameAffichage.setStyleSheet("background-color:rgb(224,223,222)")
        self.frameAffichage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameAffichage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAffichage.setObjectName("frameAffichage")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameAffichage)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frameAffichage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.RBalpha = QtWidgets.QRadioButton(self.frameAffichage)
        self.RBalpha.setObjectName("RBalpha")
        self.verticalLayout_2.addWidget(self.RBalpha)
        self.RBOrdre = QtWidgets.QRadioButton(self.frameAffichage)
        self.RBOrdre.setObjectName("RBOrdre")
        self.verticalLayout_2.addWidget(self.RBOrdre)
        self.RBGroupe = QtWidgets.QRadioButton(self.frameAffichage)
        self.RBGroupe.setObjectName("RBGroupe")
        self.verticalLayout_2.addWidget(self.RBGroupe)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(109, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textLabel6 = QtWidgets.QLabel(self.frameAffichage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel6.sizePolicy().hasHeightForWidth())
        self.textLabel6.setSizePolicy(sizePolicy)
        self.textLabel6.setMinimumSize(QtCore.QSize(141, 35))
        self.textLabel6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textLabel6.setFrameShape(QtWidgets.QFrame.Box)
        self.textLabel6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textLabel6.setLineWidth(1)
        self.textLabel6.setWordWrap(False)
        self.textLabel6.setObjectName("textLabel6")
        self.verticalLayout_3.addWidget(self.textLabel6)
        self.LEFiltre = QtWidgets.QLineEdit(self.frameAffichage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEFiltre.sizePolicy().hasHeightForWidth())
        self.LEFiltre.setSizePolicy(sizePolicy)
        self.LEFiltre.setMinimumSize(QtCore.QSize(195, 30))
        self.LEFiltre.setStyleSheet("background-color : rgb(248,247,246)")
        self.LEFiltre.setFrame(False)
        self.LEFiltre.setObjectName("LEFiltre")
        self.verticalLayout_3.addWidget(self.LEFiltre)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RBCasse = QtWidgets.QRadioButton(self.frameAffichage)
        self.RBCasse.setAutoExclusive(False)
        self.RBCasse.setObjectName("RBCasse")
        self.horizontalLayout_2.addWidget(self.RBCasse)
        self.RBClear = QtWidgets.QPushButton(self.frameAffichage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RBClear.sizePolicy().hasHeightForWidth())
        self.RBClear.setSizePolicy(sizePolicy)
        self.RBClear.setMinimumSize(QtCore.QSize(200, 40))
        self.RBClear.setMaximumSize(QtCore.QSize(200, 40))
        self.RBClear.setStyleSheet("background-color:rgb(104,110,149);\n"
"color :white;\n"
"border-radius : 12px\n"
"")
        self.RBClear.setObjectName("RBClear")
        self.horizontalLayout_2.addWidget(self.RBClear)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.RBRegle = QtWidgets.QToolButton(self.frameAffichage)
        self.RBRegle.setMinimumSize(QtCore.QSize(21, 31))
        self.RBRegle.setMaximumSize(QtCore.QSize(21, 31))
        self.RBRegle.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.RBRegle.setStyleSheet("border : 0px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Editeur/icons/lettreRblanc30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBRegle.setIcon(icon)
        self.RBRegle.setIconSize(QtCore.QSize(21, 31))
        self.RBRegle.setObjectName("RBRegle")
        self.horizontalLayout.addWidget(self.RBRegle)
        self.labelRegle = QtWidgets.QLabel(self.frameAffichage)
        self.labelRegle.setObjectName("labelRegle")
        self.horizontalLayout.addWidget(self.labelRegle)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addWidget(self.frameAffichage)
        self.scrollAreaCommandes = QtWidgets.QScrollArea(ChoixCommandes)
        self.scrollAreaCommandes.setStyleSheet("")
        self.scrollAreaCommandes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaCommandes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollAreaCommandes.setWidgetResizable(True)
        self.scrollAreaCommandes.setObjectName("scrollAreaCommandes")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1226, 498))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.commandesLayout = QtWidgets.QVBoxLayout()
        self.commandesLayout.setContentsMargins(11, 11, 11, 11)
        self.commandesLayout.setSpacing(0)
        self.commandesLayout.setObjectName("commandesLayout")
        self.verticalLayout.addLayout(self.commandesLayout)
        self.scrollAreaCommandes.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollAreaCommandes)

        self.retranslateUi(ChoixCommandes)
        QtCore.QMetaObject.connectSlotsByName(ChoixCommandes)

    def retranslateUi(self, ChoixCommandes):
        _translate = QtCore.QCoreApplication.translate
        ChoixCommandes.setWindowTitle(_translate("ChoixCommandes", "DMacro"))
        self.label.setText(_translate("ChoixCommandes", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Affichage</span></p></body></html>"))
        self.RBalpha.setToolTip(_translate("ChoixCommandes", "affiche les commandes par ordre alphabetique"))
        self.RBalpha.setText(_translate("ChoixCommandes", "Alphabetique"))
        self.RBOrdre.setToolTip(_translate("ChoixCommandes", "affiche les commandes selon les thèmes"))
        self.RBOrdre.setText(_translate("ChoixCommandes", "Ordre de la modélisation"))
        self.RBGroupe.setToolTip(_translate("ChoixCommandes", "affiche les commandes selon les thèmes"))
        self.RBGroupe.setText(_translate("ChoixCommandes", "Par Groupe"))
        self.textLabel6.setToolTip(_translate("ChoixCommandes", "selectionne les mots qui CONTIENNENT l expression"))
        self.textLabel6.setText(_translate("ChoixCommandes", "<html><head/><body><p align=\"center\">Filtre Commande</p></body></html>"))
        self.LEFiltre.setToolTip(_translate("ChoixCommandes", "filter commands"))
        self.RBCasse.setText(_translate("ChoixCommandes", "Sensible à la casse"))
        self.RBClear.setToolTip(_translate("ChoixCommandes", "ré-affiche toutes les commandes"))
        self.RBClear.setText(_translate("ChoixCommandes", "Effacer "))
        self.RBRegle.setToolTip(_translate("ChoixCommandes", "affiche les régles de validité"))
        self.RBRegle.setText(_translate("ChoixCommandes", "..."))
        self.labelRegle.setText(_translate("ChoixCommandes", "Règles de construction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChoixCommandes = QtWidgets.QWidget()
    ui = Ui_ChoixCommandes()
    ui.setupUi(ChoixCommandes)
    ChoixCommandes.show()
    sys.exit(app.exec_())

