# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desInclude.ui'
#
# Created: Fri Sep 17 16:46:35 2010
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DInc1(object):
    def setupUi(self, DInc1):
        DInc1.setObjectName("DInc1")
        DInc1.resize(521,511)
        DInc1.setMinimumSize(QtCore.QSize(505,0))
        self.gridlayout = QtGui.QGridLayout(DInc1)
        self.gridlayout.setObjectName("gridlayout")
        self.bOk = QtGui.QPushButton(DInc1)
        self.bOk.setMinimumSize(QtCore.QSize(0,30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.gridlayout.addWidget(self.bOk,2,1,1,1)
        self.Commentaire = QtGui.QLabel(DInc1)
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridlayout.addWidget(self.Commentaire,1,0,1,3)
        self.TWChoix = QtGui.QTabWidget(DInc1)
        self.TWChoix.setObjectName("TWChoix")
        self.MotClef = QtGui.QWidget()
        self.MotClef.setObjectName("MotClef")
        self.gridlayout1 = QtGui.QGridLayout(self.MotClef)
        self.gridlayout1.setObjectName("gridlayout1")
        self.LBMCPermis = QtGui.QListWidget(self.MotClef)
        self.LBMCPermis.setMinimumSize(QtCore.QSize(0,0))
        self.LBMCPermis.setObjectName("LBMCPermis")
        self.gridlayout1.addWidget(self.LBMCPermis,1,0,1,1)
        self.textLabel1 = QtGui.QLabel(self.MotClef)
        self.textLabel1.setMinimumSize(QtCore.QSize(0,0))
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout1.addWidget(self.textLabel1,0,0,1,1)
        self.LBRegles = QtGui.QListWidget(self.MotClef)
        self.LBRegles.setObjectName("LBRegles")
        self.gridlayout1.addWidget(self.LBRegles,1,1,1,1)
        self.textLabel1_2 = QtGui.QLabel(self.MotClef)
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.gridlayout1.addWidget(self.textLabel1_2,0,1,1,1)
        self.TWChoix.addTab(self.MotClef,"")
        self.Commande = QtGui.QWidget()
        self.Commande.setObjectName("Commande")
        self.gridLayout_2 = QtGui.QGridLayout(self.Commande)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textLabel1_4 = QtGui.QLabel(self.Commande)
        self.textLabel1_4.setWordWrap(False)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.gridLayout_2.addWidget(self.textLabel1_4,0,0,1,3)
        self.groupBox = QtGui.QGroupBox(self.Commande)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.RBalpha = QtGui.QRadioButton(self.groupBox)
        self.RBalpha.setChecked(True)
        self.RBalpha.setObjectName("RBalpha")
        self.gridLayout.addWidget(self.RBalpha,0,0,1,1)
        self.RBGroupe = QtGui.QRadioButton(self.groupBox)
        self.RBGroupe.setObjectName("RBGroupe")
        self.gridLayout.addWidget(self.RBGroupe,1,0,1,1)
        self.gridLayout_2.addWidget(self.groupBox,0,3,2,1)
        self.textLabel6 = QtGui.QLabel(self.Commande)
        self.textLabel6.setMinimumSize(QtCore.QSize(50,30))
        self.textLabel6.setWordWrap(False)
        self.textLabel6.setObjectName("textLabel6")
        self.gridLayout_2.addWidget(self.textLabel6,1,0,1,1)
        self.LEFiltre = QtGui.QLineEdit(self.Commande)
        self.LEFiltre.setMinimumSize(QtCore.QSize(160,30))
        self.LEFiltre.setObjectName("LEFiltre")
        self.gridLayout_2.addWidget(self.LEFiltre,1,1,1,1)
        self.BNext = QtGui.QPushButton(self.Commande)
        self.BNext.setObjectName("BNext")
        self.gridLayout_2.addWidget(self.BNext,1,2,1,1)
        self.LBNouvCommande = QtGui.QListWidget(self.Commande)
        self.LBNouvCommande.setObjectName("LBNouvCommande")
        self.gridLayout_2.addWidget(self.LBNouvCommande,2,0,1,4)
        self.textLabel4 = QtGui.QLabel(self.Commande)
        self.textLabel4.setWordWrap(False)
        self.textLabel4.setObjectName("textLabel4")
        self.gridLayout_2.addWidget(self.textLabel4,3,0,1,4)
        self.TWChoix.addTab(self.Commande,"")
        self.maPageOk = QtGui.QWidget()
        self.maPageOk.setObjectName("maPageOk")
        self.textLabel1_3 = QtGui.QLabel(self.maPageOk)
        self.textLabel1_3.setGeometry(QtCore.QRect(30,10,440,41))
        self.textLabel1_3.setWordWrap(False)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.LENomFichier = QtGui.QLineEdit(self.maPageOk)
        self.LENomFichier.setGeometry(QtCore.QRect(20,50,450,40))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LENomFichier.sizePolicy().hasHeightForWidth())
        self.LENomFichier.setSizePolicy(sizePolicy)
        self.LENomFichier.setMinimumSize(QtCore.QSize(450,40))
        self.LENomFichier.setObjectName("LENomFichier")
        self.BBrowse = QtGui.QPushButton(self.maPageOk)
        self.BBrowse.setGeometry(QtCore.QRect(20,110,161,41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BBrowse.sizePolicy().hasHeightForWidth())
        self.BBrowse.setSizePolicy(sizePolicy)
        self.BBrowse.setObjectName("BBrowse")
        self.BChangeFile = QtGui.QPushButton(self.maPageOk)
        self.BChangeFile.setGeometry(QtCore.QRect(20,160,161,41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BChangeFile.sizePolicy().hasHeightForWidth())
        self.BChangeFile.setSizePolicy(sizePolicy)
        self.BChangeFile.setObjectName("BChangeFile")
        self.TWChoix.addTab(self.maPageOk,"")
        self.maPageBad = QtGui.QWidget()
        self.maPageBad.setObjectName("maPageBad")
        self.gridlayout2 = QtGui.QGridLayout(self.maPageBad)
        self.gridlayout2.setObjectName("gridlayout2")
        self.textLabel1_5 = QtGui.QLabel(self.maPageBad)
        self.textLabel1_5.setWordWrap(False)
        self.textLabel1_5.setObjectName("textLabel1_5")
        self.gridlayout2.addWidget(self.textLabel1_5,0,0,1,1)
        self.TWChoix.addTab(self.maPageBad,"")
        self.gridlayout.addWidget(self.TWChoix,0,0,1,3)

        self.retranslateUi(DInc1)
        self.TWChoix.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(DInc1)
        DInc1.setTabOrder(self.LEFiltre,self.LENomFichier)
        DInc1.setTabOrder(self.LENomFichier,self.bOk)
        DInc1.setTabOrder(self.bOk,self.TWChoix)
        DInc1.setTabOrder(self.TWChoix,self.LBMCPermis)
        DInc1.setTabOrder(self.LBMCPermis,self.LBRegles)
        DInc1.setTabOrder(self.LBRegles,self.LBNouvCommande)
        DInc1.setTabOrder(self.LBNouvCommande,self.RBalpha)
        DInc1.setTabOrder(self.RBalpha,self.BBrowse)
        DInc1.setTabOrder(self.BBrowse,self.BChangeFile)

    def retranslateUi(self, DInc1):
        DInc1.setWindowTitle(QtGui.QApplication.translate("DInc1", "DMacro", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DInc1", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DInc1", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DInc1", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("DInc1", "<h3><p align=\"center\"><u><b>Mots Clefs Permis</b></u></p></h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("DInc1", "<h3><p align=\"center\"><u><b>Régles</b></u></p></h3>", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.MotClef), QtGui.QApplication.translate("DInc1", "Ajouter Mot-Clef", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_4.setText(QtGui.QApplication.translate("DInc1", "<b><u>Commandes :</u></b>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DInc1", "Affichage", None, QtGui.QApplication.UnicodeUTF8))
        self.RBalpha.setText(QtGui.QApplication.translate("DInc1", "alphabétique", None, QtGui.QApplication.UnicodeUTF8))
        self.RBGroupe.setText(QtGui.QApplication.translate("DInc1", "par groupe", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel6.setText(QtGui.QApplication.translate("DInc1", "Filtre", None, QtGui.QApplication.UnicodeUTF8))
        self.BNext.setText(QtGui.QApplication.translate("DInc1", "Suivant", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel4.setText(QtGui.QApplication.translate("DInc1", "La commande choisie sera ajoutée APRES la commande courante", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.Commande), QtGui.QApplication.translate("DInc1", "Nouvelle Commande", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_3.setText(QtGui.QApplication.translate("DInc1", "<font size=\"+1\">La commande INCLUDE requiert un nom de Fichier :</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.BBrowse.setText(QtGui.QApplication.translate("DInc1", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.BChangeFile.setText(QtGui.QApplication.translate("DInc1", "Autre Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.maPageOk), QtGui.QApplication.translate("DInc1", "Fichier Include", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_5.setText(QtGui.QApplication.translate("DInc1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:large;\"><span style=\" font-size:11pt; font-weight:600;\">La commande INCLUDE n\'a pas de fichier associé. </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><span style=\" font-size:large;\">Il faut d\'abord choisir un numéro d\'unité</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.TWChoix.setTabText(self.TWChoix.indexOf(self.maPageBad), QtGui.QApplication.translate("DInc1", "Fichier Inc", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DInc1 = QtGui.QWidget()
    ui = Ui_DInc1()
    ui.setupUi(DInc1)
    DInc1.show()
    sys.exit(app.exec_())

