# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desPlusieursBase.ui'
#
# Created: Tue Nov 18 17:37:25 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DPlusBase(object):
    def setupUi(self, DPlusBase):
        DPlusBase.setObjectName("DPlusBase")
        DPlusBase.resize(552,480)
        DPlusBase.setMinimumSize(QtCore.QSize(350,0))
        self.gridlayout = QtGui.QGridLayout(DPlusBase)
        self.gridlayout.setObjectName("gridlayout")
        self.tabuniqueinto = QtGui.QTabWidget(DPlusBase)
        self.tabuniqueinto.setObjectName("tabuniqueinto")
        self.Widget8 = QtGui.QWidget()
        self.Widget8.setGeometry(QtCore.QRect(0,0,530,435))
        self.Widget8.setObjectName("Widget8")
        self.gridlayout1 = QtGui.QGridLayout(self.Widget8)
        self.gridlayout1.setObjectName("gridlayout1")
        self.textLabel1 = QtGui.QLabel(self.Widget8)
        self.textLabel1.setWordWrap(False)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout1.addWidget(self.textLabel1,0,0,1,1)
        self.LBValeurs = QtGui.QListWidget(self.Widget8)
        self.LBValeurs.setMinimumSize(QtCore.QSize(200,0))
        self.LBValeurs.setObjectName("LBValeurs")
        self.gridlayout1.addWidget(self.LBValeurs,1,0,9,1)
        spacerItem = QtGui.QSpacerItem(21,231,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem,5,1,5,2)
        spacerItem1 = QtGui.QSpacerItem(31,30,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem1,0,1,1,2)
        self.BAjout1Val = QtGui.QToolButton(self.Widget8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BAjout1Val.sizePolicy().hasHeightForWidth())
        self.BAjout1Val.setSizePolicy(sizePolicy)
        self.BAjout1Val.setMinimumSize(QtCore.QSize(40,30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../EficasV1/Editeur/icons/arrow_left.gif"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.BAjout1Val.setIcon(icon)
        self.BAjout1Val.setObjectName("BAjout1Val")
        self.gridlayout1.addWidget(self.BAjout1Val,2,1,1,2)
        spacerItem2 = QtGui.QSpacerItem(150,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem2,8,2,1,3)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.bParam = QtGui.QPushButton(self.Widget8)
        self.bParam.setMinimumSize(QtCore.QSize(0,30))
        self.bParam.setAutoDefault(True)
        self.bParam.setObjectName("bParam")
        self.vboxlayout.addWidget(self.bParam)
        self.bImport = QtGui.QPushButton(self.Widget8)
        self.bImport.setMinimumSize(QtCore.QSize(0,30))
        self.bImport.setAutoDefault(True)
        self.bImport.setObjectName("bImport")
        self.vboxlayout.addWidget(self.bImport)
        self.gridlayout1.addLayout(self.vboxlayout,7,5,2,1)
        spacerItem3 = QtGui.QSpacerItem(31,50,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem3,6,5,1,1)
        spacerItem4 = QtGui.QSpacerItem(31,50,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem4,9,5,1,1)
        self.BSalome = QtGui.QToolButton(self.Widget8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BSalome.sizePolicy().hasHeightForWidth())
        self.BSalome.setSizePolicy(sizePolicy)
        self.BSalome.setMinimumSize(QtCore.QSize(40,30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image240.gif"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.BSalome.setIcon(icon)
        self.BSalome.setObjectName("BSalome")
        self.gridlayout1.addWidget(self.BSalome,4,3,1,1)
        self.BView2D = QtGui.QPushButton(self.Widget8)
        self.BView2D.setMinimumSize(QtCore.QSize(120,30))
        self.BView2D.setObjectName("BView2D")
        self.gridlayout1.addWidget(self.BView2D,4,4,1,2)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.textLabel1_2 = QtGui.QLabel(self.Widget8)
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.hboxlayout.addWidget(self.textLabel1_2)
        spacerItem5 = QtGui.QSpacerItem(111,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem5)
        self.gridlayout1.addLayout(self.hboxlayout,0,3,2,3)
        self.LEValeur = QtGui.QLineEdit(self.Widget8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEValeur.sizePolicy().hasHeightForWidth())
        self.LEValeur.setSizePolicy(sizePolicy)
        self.LEValeur.setMinimumSize(QtCore.QSize(220,30))
        self.LEValeur.setObjectName("LEValeur")
        self.gridlayout1.addWidget(self.LEValeur,2,3,2,3)
        self.BSup1Val = QtGui.QToolButton(self.Widget8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BSup1Val.sizePolicy().hasHeightForWidth())
        self.BSup1Val.setSizePolicy(sizePolicy)
        self.BSup1Val.setMinimumSize(QtCore.QSize(40,30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../EficasV1/Editeur/icons/arrow_right.gif"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
        self.BSup1Val.setIcon(icon)
        self.BSup1Val.setObjectName("BSup1Val")
        self.gridlayout1.addWidget(self.BSup1Val,3,1,2,2)
        self.Commentaire = QtGui.QLabel(self.Widget8)
        self.Commentaire.setMinimumSize(QtCore.QSize(0,60))
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridlayout1.addWidget(self.Commentaire,5,3,1,3)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.bSup = QtGui.QPushButton(self.Widget8)
        self.bSup.setMinimumSize(QtCore.QSize(0,30))
        self.bSup.setAutoDefault(True)
        self.bSup.setObjectName("bSup")
        self.hboxlayout1.addWidget(self.bSup)
        self.bOk = QtGui.QPushButton(self.Widget8)
        self.bOk.setMinimumSize(QtCore.QSize(0,30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.hboxlayout1.addWidget(self.bOk)
        self.bHelp = QtGui.QPushButton(self.Widget8)
        self.bHelp.setMinimumSize(QtCore.QSize(0,30))
        self.bHelp.setAutoDefault(True)
        self.bHelp.setObjectName("bHelp")
        self.hboxlayout1.addWidget(self.bHelp)
        self.gridlayout1.addLayout(self.hboxlayout1,10,0,1,6)
        self.tabuniqueinto.addTab(self.Widget8,"")
        self.gridlayout.addWidget(self.tabuniqueinto,0,0,1,1)

        self.retranslateUi(DPlusBase)
        QtCore.QMetaObject.connectSlotsByName(DPlusBase)
        DPlusBase.setTabOrder(self.LEValeur,self.tabuniqueinto)
        DPlusBase.setTabOrder(self.tabuniqueinto,self.bSup)
        DPlusBase.setTabOrder(self.bSup,self.bOk)
        DPlusBase.setTabOrder(self.bOk,self.bHelp)
        DPlusBase.setTabOrder(self.bHelp,self.bParam)
        DPlusBase.setTabOrder(self.bParam,self.bImport)
        DPlusBase.setTabOrder(self.bImport,self.LBValeurs)
        DPlusBase.setTabOrder(self.LBValeurs,self.BView2D)

    def retranslateUi(self, DPlusBase):
        DPlusBase.setWindowTitle(QtGui.QApplication.translate("DPlusBase", "DUnIn", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("DPlusBase", "<u><font size=\"+1\">Valeur(s) actuelle(s)</font></u>", None, QtGui.QApplication.UnicodeUTF8))
        self.BAjout1Val.setToolTip(QtGui.QApplication.translate("DPlusBase", "ajoute la valeur saisie sous l occurence selectionnée (en fin de liste si il n y a pas de selection)", None, QtGui.QApplication.UnicodeUTF8))
        self.bParam.setToolTip(QtGui.QApplication.translate("DPlusBase", "suppression du mot clef", None, QtGui.QApplication.UnicodeUTF8))
        self.bParam.setText(QtGui.QApplication.translate("DPlusBase", "&Parametres", None, QtGui.QApplication.UnicodeUTF8))
        self.bParam.setShortcut(QtGui.QApplication.translate("DPlusBase", "Alt+P", None, QtGui.QApplication.UnicodeUTF8))
        self.bImport.setToolTip(QtGui.QApplication.translate("DPlusBase", "suppression du mot clef", None, QtGui.QApplication.UnicodeUTF8))
        self.bImport.setText(QtGui.QApplication.translate("DPlusBase", "&Importer", None, QtGui.QApplication.UnicodeUTF8))
        self.bImport.setShortcut(QtGui.QApplication.translate("DPlusBase", "Alt+I", None, QtGui.QApplication.UnicodeUTF8))
        self.BSalome.setToolTip(QtGui.QApplication.translate("DPlusBase", "ajoute la valeur saisie sous l occurence selectionnée (en fin de liste si il n y a pas de selection)", None, QtGui.QApplication.UnicodeUTF8))
        self.BView2D.setText(QtGui.QApplication.translate("DPlusBase", "Visualiser", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("DPlusBase", "<font size=\"+1\">Valeur</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.BSup1Val.setToolTip(QtGui.QApplication.translate("DPlusBase", "enleve l occurence selectionnee", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setToolTip(QtGui.QApplication.translate("DPlusBase", "suppression du mot clef", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setText(QtGui.QApplication.translate("DPlusBase", "&Supprimer", None, QtGui.QApplication.UnicodeUTF8))
        self.bSup.setShortcut(QtGui.QApplication.translate("DPlusBase", "Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DPlusBase", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DPlusBase", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DPlusBase", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setToolTip(QtGui.QApplication.translate("DPlusBase", "affichage documentation aster", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setText(QtGui.QApplication.translate("DPlusBase", "&Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.bHelp.setShortcut(QtGui.QApplication.translate("DPlusBase", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.tabuniqueinto.setTabText(self.tabuniqueinto.indexOf(self.Widget8), QtGui.QApplication.translate("DPlusBase", "Saisir Valeur", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DPlusBase = QtGui.QWidget()
    ui = Ui_DPlusBase()
    ui.setupUi(DPlusBase)
    DPlusBase.show()
    sys.exit(app.exec_())

