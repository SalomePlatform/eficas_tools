# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myMain.ui'
#
# Created: Tue Nov 18 17:37:26 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Eficas(object):
    def setupUi(self, Eficas):
        Eficas.setObjectName("Eficas")
        Eficas.resize(1406,600)
        self.centralwidget = QtGui.QWidget(Eficas)
        self.centralwidget.setGeometry(QtCore.QRect(0,68,1406,510))
        self.centralwidget.setObjectName("centralwidget")
        Eficas.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Eficas)
        self.menubar.setGeometry(QtCore.QRect(0,0,1406,29))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuEdition = QtGui.QMenu(self.menubar)
        self.menuEdition.setObjectName("menuEdition")
        self.menuJdC = QtGui.QMenu(self.menubar)
        self.menuJdC.setObjectName("menuJdC")
        self.menu_Aide = QtGui.QMenu(self.menubar)
        self.menu_Aide.setObjectName("menu_Aide")
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuTraduction = QtGui.QMenu(self.menubar)
        self.menuTraduction.setObjectName("menuTraduction")
        self.menuPatrons = QtGui.QMenu(self.menubar)
        self.menuPatrons.setObjectName("menuPatrons")
        Eficas.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Eficas)
        self.statusbar.setGeometry(QtCore.QRect(0,578,1406,22))
        self.statusbar.setObjectName("statusbar")
        Eficas.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Eficas)
        self.toolBar.setGeometry(QtCore.QRect(0,29,1406,39))
        self.toolBar.setObjectName("toolBar")
        Eficas.addToolBar(QtCore.Qt.TopToolBarArea,self.toolBar)
        self.action_Nouveau = QtGui.QAction(Eficas)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/New24.gif"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.action_Nouveau.setIcon(icon)
        self.action_Nouveau.setObjectName("action_Nouveau")
        self.actionNouvel_Include = QtGui.QAction(Eficas)
        self.actionNouvel_Include.setObjectName("actionNouvel_Include")
        self.action_Ouvrir = QtGui.QAction(Eficas)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Open24.gif"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.action_Ouvrir.setIcon(icon)
        self.action_Ouvrir.setObjectName("action_Ouvrir")
        self.actionEnregistrer = QtGui.QAction(Eficas)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Save24.gif"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionEnregistrer.setIcon(icon)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionEnregistrer_sous = QtGui.QAction(Eficas)
        self.actionEnregistrer_sous.setObjectName("actionEnregistrer_sous")
        self.actionFermer = QtGui.QAction(Eficas)
        self.actionFermer.setObjectName("actionFermer")
        self.actionFermer_tout = QtGui.QAction(Eficas)
        self.actionFermer_tout.setObjectName("actionFermer_tout")
        self.actionCouper = QtGui.QAction(Eficas)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Cut24.gif"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionCouper.setIcon(icon)
        self.actionCouper.setObjectName("actionCouper")
        self.actionCopier = QtGui.QAction(Eficas)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Copy24.gif"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionCopier.setIcon(icon)
        self.actionCopier.setObjectName("actionCopier")
        self.actionColler = QtGui.QAction(Eficas)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Paste24.gif"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.actionColler.setIcon(icon)
        self.actionColler.setObjectName("actionColler")
        self.actionQuitter = QtGui.QAction(Eficas)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionRapport_de_Validation = QtGui.QAction(Eficas)
        self.actionRapport_de_Validation.setObjectName("actionRapport_de_Validation")
        self.actionFichier_Source = QtGui.QAction(Eficas)
        self.actionFichier_Source.setObjectName("actionFichier_Source")
        self.actionFichier_Resultat = QtGui.QAction(Eficas)
        self.actionFichier_Resultat.setObjectName("actionFichier_Resultat")
        self.actionParametres_Eficas = QtGui.QAction(Eficas)
        self.actionParametres_Eficas.setObjectName("actionParametres_Eficas")
        self.actionLecteur_Pdf = QtGui.QAction(Eficas)
        self.actionLecteur_Pdf.setObjectName("actionLecteur_Pdf")
        self.actionTraduitV7V8 = QtGui.QAction(Eficas)
        self.actionTraduitV7V8.setObjectName("actionTraduitV7V8")
        self.actionTraduitV8V9 = QtGui.QAction(Eficas)
        self.actionTraduitV8V9.setObjectName("actionTraduitV8V9")
        self.menuFichier.addAction(self.action_Nouveau)
        self.menuFichier.addAction(self.actionNouvel_Include)
        self.menuFichier.addAction(self.action_Ouvrir)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addAction(self.actionEnregistrer_sous)
        self.menuFichier.addAction(self.actionFermer)
        self.menuFichier.addAction(self.actionFermer_tout)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuEdition.addAction(self.actionCouper)
        self.menuEdition.addAction(self.actionCopier)
        self.menuEdition.addAction(self.actionColler)
        self.menuJdC.addAction(self.actionRapport_de_Validation)
        self.menuJdC.addAction(self.actionFichier_Source)
        self.menuJdC.addAction(self.actionFichier_Resultat)
        self.menuOptions.addAction(self.actionParametres_Eficas)
        self.menuOptions.addAction(self.actionLecteur_Pdf)
        self.menuTraduction.addAction(self.actionTraduitV7V8)
        self.menuTraduction.addAction(self.actionTraduitV8V9)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuEdition.menuAction())
        self.menubar.addAction(self.menuJdC.menuAction())
        self.menubar.addAction(self.menu_Aide.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuTraduction.menuAction())
        self.menubar.addAction(self.menuPatrons.menuAction())
        self.toolBar.addAction(self.action_Nouveau)
        self.toolBar.addAction(self.action_Ouvrir)
        self.toolBar.addAction(self.actionEnregistrer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCouper)
        self.toolBar.addAction(self.actionCopier)
        self.toolBar.addAction(self.actionColler)

        self.retranslateUi(Eficas)
        QtCore.QMetaObject.connectSlotsByName(Eficas)

    def retranslateUi(self, Eficas):
        Eficas.setWindowTitle(QtGui.QApplication.translate("Eficas", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFichier.setTitle(QtGui.QApplication.translate("Eficas", "&Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdition.setTitle(QtGui.QApplication.translate("Eficas", "Edition", None, QtGui.QApplication.UnicodeUTF8))
        self.menuJdC.setTitle(QtGui.QApplication.translate("Eficas", "JdC", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Aide.setTitle(QtGui.QApplication.translate("Eficas", "&Aide", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("Eficas", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTraduction.setTitle(QtGui.QApplication.translate("Eficas", "Traduction", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPatrons.setTitle(QtGui.QApplication.translate("Eficas", "Patrons", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Eficas", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Nouveau.setText(QtGui.QApplication.translate("Eficas", "&Nouveau", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Nouveau.setShortcut(QtGui.QApplication.translate("Eficas", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNouvel_Include.setText(QtGui.QApplication.translate("Eficas", "Nouvel Include", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Ouvrir.setText(QtGui.QApplication.translate("Eficas", "&Ouvrir", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Ouvrir.setShortcut(QtGui.QApplication.translate("Eficas", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnregistrer.setText(QtGui.QApplication.translate("Eficas", "Enregistrer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnregistrer.setShortcut(QtGui.QApplication.translate("Eficas", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnregistrer_sous.setText(QtGui.QApplication.translate("Eficas", "Enregistrer sous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnregistrer_sous.setShortcut(QtGui.QApplication.translate("Eficas", "Ctrl+Shift+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFermer.setText(QtGui.QApplication.translate("Eficas", "Fermer ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFermer.setShortcut(QtGui.QApplication.translate("Eficas", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFermer_tout.setText(QtGui.QApplication.translate("Eficas", "Fermer tout", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCouper.setText(QtGui.QApplication.translate("Eficas", "Couper", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCouper.setShortcut(QtGui.QApplication.translate("Eficas", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopier.setText(QtGui.QApplication.translate("Eficas", "Copier", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopier.setShortcut(QtGui.QApplication.translate("Eficas", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColler.setText(QtGui.QApplication.translate("Eficas", "Coller", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColler.setShortcut(QtGui.QApplication.translate("Eficas", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setText(QtGui.QApplication.translate("Eficas", "Quitter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setShortcut(QtGui.QApplication.translate("Eficas", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRapport_de_Validation.setText(QtGui.QApplication.translate("Eficas", "Rapport de Validation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFichier_Source.setText(QtGui.QApplication.translate("Eficas", "Fichier Source", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFichier_Resultat.setText(QtGui.QApplication.translate("Eficas", "Fichier Résultat", None, QtGui.QApplication.UnicodeUTF8))
        self.actionParametres_Eficas.setText(QtGui.QApplication.translate("Eficas", "Parametres Eficas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLecteur_Pdf.setText(QtGui.QApplication.translate("Eficas", "Lecteur Pdf", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTraduitV7V8.setText(QtGui.QApplication.translate("Eficas", "TraduitV7V8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTraduitV8V9.setText(QtGui.QApplication.translate("Eficas", "TraduitV8V9", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Eficas = QtGui.QMainWindow()
    ui = Ui_Eficas()
    ui.setupUi(Eficas)
    Eficas.show()
    sys.exit(app.exec_())

