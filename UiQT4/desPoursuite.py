# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desPoursuite.ui'
#
# Created: Thu Mar 12 10:42:31 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DPour(object):
    def setupUi(self, DPour):
        DPour.setObjectName("DPour")
        DPour.resize(521, 544)
        DPour.setMinimumSize(QtCore.QSize(505, 0))
        self.gridlayout = QtGui.QGridLayout(DPour)
        self.gridlayout.setObjectName("gridlayout")
        self.TWChoix = QtGui.QTabWidget(DPour)
        self.TWChoix.setObjectName("TWChoix")
        self.MotClef = QtGui.QWidget()
        self.MotClef.setObjectName("MotClef")
        self.gridLayout_4 = QtGui.QGridLayout(self.MotClef)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textLabel1 = QtGui.QLabel(self.MotClef)
        self.textLabel1.setMinimumSize(QtCore.QSize(0, 0))
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout_4.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.textLabel1_2 = QtGui.QLabel(self.MotClef)
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.gridLayout_4.addWidget(self.textLabel1_2, 0, 1, 1, 1)
        self.LBMCPermis = QtGui.QListWidget(self.MotClef)
        self.LBMCPermis.setMinimumSize(QtCore.QSize(0, 0))
        self.LBMCPermis.setObjectName("LBMCPermis")
        self.gridLayout_4.addWidget(self.LBMCPermis, 1, 0, 1, 1)
        self.LBRegles = QtGui.QListWidget(self.MotClef)
        self.LBRegles.setObjectName("LBRegles")
        self.gridLayout_4.addWidget(self.LBRegles, 1, 1, 1, 1)
        self.TWChoix.addTab(self.MotClef, "")
        self.Commande = QtGui.QWidget()
        self.Commande.setObjectName("Commande")
        self.gridLayout_3 = QtGui.QGridLayout(self.Commande)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textLabel1_4 = QtGui.QLabel(self.Commande)
        self.textLabel1_4.setWordWrap(False)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.gridLayout_3.addWidget(self.textLabel1_4, 0, 0, 1, 3)
        self.groupBox = QtGui.QGroupBox(self.Commande)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.RBalpha = QtGui.QRadioButton(self.groupBox)
        self.RBalpha.setChecked(True)
        self.RBalpha.setObjectName("RBalpha")
        self.gridLayout.addWidget(self.RBalpha, 0, 0, 1, 1)
        self.RBGroupe = QtGui.QRadioButton(self.groupBox)
        self.RBGroupe.setObjectName("RBGroupe")
        self.gridLayout.addWidget(self.RBGroupe, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 3, 2, 1)
        self.textLabel6 = QtGui.QLabel(self.Commande)
        self.textLabel6.setMinimumSize(QtCore.QSize(50, 30))
        self.textLabel6.setWordWrap(False)
        self.textLabel6.setObjectName("textLabel6")
        self.gridLayout_3.addWidget(self.textLabel6, 1, 0, 1, 1)
        self.LEFiltre = QtGui.QLineEdit(self.Commande)
        self.LEFiltre.setMinimumSize(QtCore.QSize(160, 30))
        self.LEFiltre.setObjectName("LEFiltre")
        self.gridLayout_3.addWidget(self.LEFiltre, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.Commande)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 1, 2, 1, 1)
        self.LBNouvCommande = QtGui.QListWidget(self.Commande)
        self.LBNouvCommande.setObjectName("LBNouvCommande")
        self.gridLayout_3.addWidget(self.LBNouvCommande, 2, 0, 1, 4)
        self.textLabel4 = QtGui.QLabel(self.Commande)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName("textLabel4")
        self.gridLayout_3.addWidget(self.textLabel4, 3, 0, 1, 4)
        self.TWChoix.addTab(self.Commande, "")
        self.TabPage = QtGui.QWidget()
        self.TabPage.setObjectName("TabPage")
        self.textLabel1_3 = QtGui.QLabel(self.TabPage)
        self.textLabel1_3.setGeometry(QtCore.QRect(9, 9, 481, 19))
        self.textLabel1_3.setWordWrap(False)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.LENomFichier = QtGui.QLineEdit(self.TabPage)
        self.LENomFichier.setGeometry(QtCore.QRect(9, 33, 481, 40))
        self.LENomFichier.setMinimumSize(QtCore.QSize(470, 40))
        self.LENomFichier.setObjectName("LENomFichier")
        self.BFichier = QtGui.QPushButton(self.TabPage)
        self.BFichier.setGeometry(QtCore.QRect(330, 170, 140, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BFichier.sizePolicy().hasHeightForWidth())
        self.BFichier.setSizePolicy(sizePolicy)
        self.BFichier.setMinimumSize(QtCore.QSize(140, 50))
        self.BFichier.setObjectName("BFichier")
        self.BBrowse = QtGui.QPushButton(self.TabPage)
        self.BBrowse.setGeometry(QtCore.QRect(330, 110, 140, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BBrowse.sizePolicy().hasHeightForWidth())
        self.BBrowse.setSizePolicy(sizePolicy)
        self.BBrowse.setMinimumSize(QtCore.QSize(140, 50))
        self.BBrowse.setObjectName("BBrowse")
        self.TWChoix.addTab(self.TabPage, "")
        self.gridlayout.addWidget(self.TWChoix, 0, 0, 1, 3)
        self.bOk = QtGui.QPushButton(DPour)
        self.bOk.setMinimumSize(QtCore.QSize(0, 30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.gridlayout.addWidget(self.bOk, 2, 1, 1, 1)
        self.Commentaire = QtGui.QLabel(DPour)
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridlayout.addWidget(self.Commentaire, 1, 0, 1, 3)

        self.retranslateUi(DPour)
        self.TWChoix.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(DPour)
        DPour.setTabOrder(self.LEFiltre, self.LENomFichier)
        DPour.setTabOrder(self.LENomFichier, self.TWChoix)
        DPour.setTabOrder(self.TWChoix, self.LBMCPermis)
        DPour.setTabOrder(self.LBMCPermis, self.LBRegles)
        DPour.setTabOrder(self.LBRegles, self.LBNouvCommande)
        DPour.setTabOrder(self.LBNouvCommande, self.RBalpha)
        DPour.setTabOrder(self.RBalpha, self.bOk)

    def retranslateUi(self, DPour):
        DPour.setWindowTitle(QtGui.QApplication.translate("DPour", "DMacro", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("DPour", "<h3><p align=\"center\"><u><b>Mots Clefs Permis</b></u></p></h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("DPour", "<h3><p align=\"center\"><u><b>Régles</b></u></p></h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.MotClef), QtGui.QApplication.translate("DPour", "Ajouter Mot-Clef", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4.setText(QtGui.QApplication.translate("DPour", "<b><u>Commandes :</u></b>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DPour", "Affichage", None, QtGui.QApplication.UnicodeUTF8))
        self.RBalpha.setText(QtGui.QApplication.translate("DPour", "alphabétique", None, QtGui.QApplication.UnicodeUTF8))
        self.RBGroupe.setText(QtGui.QApplication.translate("DPour", "par groupe", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel6.setText(QtGui.QApplication.translate("DPour", "Filtre", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("DPour", "Suivant", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel4.setText(QtGui.QApplication.translate("DPour", "La commande choisie sera ajoutée APRES la commande courante", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.Commande), QtGui.QApplication.translate("DPour", "Nouvelle Commande", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3.setText(QtGui.QApplication.translate("DPour", "<font size=\"+1\">La commande POURSUITE requiert un nom de Fichier :</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.BFichier.setText(QtGui.QApplication.translate("DPour", "Autre Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.BBrowse.setText(QtGui.QApplication.translate("DPour", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.TabPage), QtGui.QApplication.translate("DPour", "Fichier Poursuite", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DPour", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DPour", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DPour", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DPour = QtGui.QWidget()
    ui = Ui_DPour()
    ui.setupUi(DPour)
    DPour.show()
    sys.exit(app.exec_())

