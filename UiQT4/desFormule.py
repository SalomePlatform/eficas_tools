# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desFormule.ui'
#
# Created: Fri Jun 19 11:40:11 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DFormule(object):
    def setupUi(self, DFormule):
        DFormule.setObjectName("DFormule")
        DFormule.resize(529, 493)
        DFormule.setMinimumSize(QtCore.QSize(505, 0))
        self.gridLayout_3 = QtGui.QGridLayout(DFormule)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TWChoix = QtGui.QTabWidget(DFormule)
        self.TWChoix.setObjectName("TWChoix")
        self.Formule = QtGui.QWidget()
        self.Formule.setObjectName("Formule")
        self.gridlayout = QtGui.QGridLayout(self.Formule)
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1 = QtGui.QLabel(self.Formule)
        self.textLabel1.setMinimumSize(QtCore.QSize(0, 0))
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.textLabel1_3 = QtGui.QLabel(self.Formule)
        self.textLabel1_3.setWordWrap(False)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.gridlayout.addWidget(self.textLabel1_3, 6, 0, 1, 2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.LENomFormule = QtGui.QLineEdit(self.Formule)
        self.LENomFormule.setMinimumSize(QtCore.QSize(0, 40))
        self.LENomFormule.setObjectName("LENomFormule")
        self.hboxlayout.addWidget(self.LENomFormule)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.textLabel1_6 = QtGui.QLabel(self.Formule)
        self.textLabel1_6.setWordWrap(False)
        self.textLabel1_6.setObjectName("textLabel1_6")
        self.hboxlayout1.addWidget(self.textLabel1_6)
        self.LENomsArgs = QtGui.QLineEdit(self.Formule)
        self.LENomsArgs.setMinimumSize(QtCore.QSize(230, 40))
        self.LENomsArgs.setObjectName("LENomsArgs")
        self.hboxlayout1.addWidget(self.LENomsArgs)
        self.textLabel1_6_2 = QtGui.QLabel(self.Formule)
        self.textLabel1_6_2.setWordWrap(False)
        self.textLabel1_6_2.setObjectName("textLabel1_6_2")
        self.hboxlayout1.addWidget(self.textLabel1_6_2)
        self.hboxlayout.addLayout(self.hboxlayout1)
        self.gridlayout.addLayout(self.hboxlayout, 2, 0, 1, 2)
        self.textLabel2 = QtGui.QLabel(self.Formule)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2, 1, 1, 1, 1)
        self.textLabel1_3_2 = QtGui.QLabel(self.Formule)
        self.textLabel1_3_2.setWordWrap(False)
        self.textLabel1_3_2.setObjectName("textLabel1_3_2")
        self.gridlayout.addWidget(self.textLabel1_3_2, 7, 0, 1, 2)
        self.textLabel2_2 = QtGui.QLabel(self.Formule)
        self.textLabel2_2.setWordWrap(False)
        self.textLabel2_2.setObjectName("textLabel2_2")
        self.gridlayout.addWidget(self.textLabel2_2, 3, 0, 1, 2)
        self.textLabel1_5 = QtGui.QLabel(self.Formule)
        self.textLabel1_5.setMinimumSize(QtCore.QSize(0, 0))
        self.textLabel1_5.setWordWrap(False)
        self.textLabel1_5.setObjectName("textLabel1_5")
        self.gridlayout.addWidget(self.textLabel1_5, 4, 0, 1, 2)
        self.LECorpsFormule = QtGui.QLineEdit(self.Formule)
        self.LECorpsFormule.setMinimumSize(QtCore.QSize(0, 30))
        self.LECorpsFormule.setObjectName("LECorpsFormule")
        self.gridlayout.addWidget(self.LECorpsFormule, 5, 0, 1, 2)
        self.textLabel1_2 = QtGui.QLabel(self.Formule)
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.gridlayout.addWidget(self.textLabel1_2, 0, 1, 1, 1)
        self.TWChoix.addTab(self.Formule, "")
        self.Commande = QtGui.QWidget()
        self.Commande.setObjectName("Commande")
        self.gridLayout_4 = QtGui.QGridLayout(self.Commande)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textLabel1_4 = QtGui.QLabel(self.Commande)
        self.textLabel1_4.setWordWrap(False)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.gridLayout_2.addWidget(self.textLabel1_4, 0, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(self.Commande)
        self.groupBox.setMinimumSize(QtCore.QSize(171, 71))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.RBalpha = QtGui.QRadioButton(self.groupBox)
        self.RBalpha.setMinimumSize(QtCore.QSize(149, 16))
        self.RBalpha.setMaximumSize(QtCore.QSize(149, 16))
        self.RBalpha.setChecked(True)
        self.RBalpha.setObjectName("RBalpha")
        self.gridLayout.addWidget(self.RBalpha, 0, 0, 1, 1)
        self.RBGroupe = QtGui.QRadioButton(self.groupBox)
        self.RBGroupe.setObjectName("RBGroupe")
        self.gridLayout.addWidget(self.RBGroupe, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 4, 2, 1)
        self.textLabel6 = QtGui.QLabel(self.Commande)
        self.textLabel6.setMinimumSize(QtCore.QSize(91, 30))
        self.textLabel6.setWordWrap(False)
        self.textLabel6.setObjectName("textLabel6")
        self.gridLayout_2.addWidget(self.textLabel6, 1, 0, 1, 1)
        self.LEFiltre = QtGui.QLineEdit(self.Commande)
        self.LEFiltre.setMinimumSize(QtCore.QSize(231, 30))
        self.LEFiltre.setObjectName("LEFiltre")
        self.gridLayout_2.addWidget(self.LEFiltre, 1, 1, 1, 1)
        self.BNext = QtGui.QPushButton(self.Commande)
        self.BNext.setMinimumSize(QtCore.QSize(90, 30))
        self.BNext.setObjectName("BNext")
        self.gridLayout_2.addWidget(self.BNext, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.LBNouvCommande = QtGui.QListWidget(self.Commande)
        self.LBNouvCommande.setObjectName("LBNouvCommande")
        self.gridLayout_4.addWidget(self.LBNouvCommande, 1, 0, 1, 1)
        self.textLabel4 = QtGui.QLabel(self.Commande)
        self.textLabel4.setMaximumSize(QtCore.QSize(721, 20))
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName("textLabel4")
        self.gridLayout_4.addWidget(self.textLabel4, 2, 0, 1, 1)
        self.TWChoix.addTab(self.Commande, "")
        self.gridLayout_3.addWidget(self.TWChoix, 0, 0, 1, 1)
        self.Commentaire = QtGui.QLabel(DFormule)
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridLayout_3.addWidget(self.Commentaire, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(158, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bOk = QtGui.QPushButton(DFormule)
        self.bOk.setMinimumSize(QtCore.QSize(163, 30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.horizontalLayout.addWidget(self.bOk)
        spacerItem2 = QtGui.QSpacerItem(158, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(DFormule)
        self.TWChoix.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DFormule)
        DFormule.setTabOrder(self.LEFiltre, self.LENomFormule)
        DFormule.setTabOrder(self.LENomFormule, self.LENomsArgs)
        DFormule.setTabOrder(self.LENomsArgs, self.LECorpsFormule)
        DFormule.setTabOrder(self.LECorpsFormule, self.bOk)
        DFormule.setTabOrder(self.bOk, self.TWChoix)
        DFormule.setTabOrder(self.TWChoix, self.RBalpha)
        DFormule.setTabOrder(self.RBalpha, self.RBGroupe)
        DFormule.setTabOrder(self.RBGroupe, self.LBNouvCommande)

    def retranslateUi(self, DFormule):
        DFormule.setWindowTitle(QtGui.QApplication.translate("DFormule", "DMacro", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("DFormule", "<h3><p align=\"center\"><u><b>Nom de la formule</b></u></p></h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3.setText(QtGui.QApplication.translate("DFormule", "Retour-Chariot permet de vérifier que l\'expression est valide.", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_6.setText(QtGui.QApplication.translate("DFormule", "<h1><b>(</b></h1>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_6_2.setText(QtGui.QApplication.translate("DFormule", "<h1><b>)</b></h1>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("DFormule", "variables séparées par des \",\"\n"
"          par ex. : x,y,z", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3_2.setText(QtGui.QApplication.translate("DFormule", "Ce n\'est qu\'après avoir appuyé sur le bouton Valider que les nouvelles\n"
"valeurs seront effectivement prises en compte", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2_2.setText(QtGui.QApplication.translate("DFormule", "<font size=\"+4\" face=\"Helvetica\"><b>=</b></font>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_5.setText(QtGui.QApplication.translate("DFormule", "<h3><p align=\"center\"><u><b>Expression</b></u></p></h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("DFormule", "<h3><p align=\"center\"><u><b>Arguments</b></u></p></h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.Formule), QtGui.QApplication.translate("DFormule", "Définition Formule", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4.setText(QtGui.QApplication.translate("DFormule", "<b><u>Commandes :</u></b>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DFormule", "Affichage", None, QtGui.QApplication.UnicodeUTF8))
        self.RBalpha.setText(QtGui.QApplication.translate("DFormule", "alphabétique", None, QtGui.QApplication.UnicodeUTF8))
        self.RBGroupe.setText(QtGui.QApplication.translate("DFormule", "par groupe", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel6.setText(QtGui.QApplication.translate("DFormule", "Filtre", None, QtGui.QApplication.UnicodeUTF8))
        self.BNext.setText(QtGui.QApplication.translate("DFormule", "Suivant", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel4.setText(QtGui.QApplication.translate("DFormule", "La commande choisie sera ajoutée APRES la commande courante", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.Commande), QtGui.QApplication.translate("DFormule", "Nouvelle Commande", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DFormule", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DFormule", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DFormule", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DFormule = QtGui.QWidget()
    ui = Ui_DFormule()
    ui.setupUi(DFormule)
    DFormule.show()
    sys.exit(app.exec_())

