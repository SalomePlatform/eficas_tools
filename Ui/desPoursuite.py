# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desPoursuite.ui'
#
# Created: ven mai 16 13:30:38 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DPour(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DPour")

        self.setMinimumSize(QSize(505,0))

        DPourLayout = QGridLayout(self,1,1,11,6,"DPourLayout")

        self.Commentaire = QLabel(self,"Commentaire")

        DPourLayout.addMultiCellWidget(self.Commentaire,1,1,0,2)

        self.TWChoix = QTabWidget(self,"TWChoix")

        self.MotClef = QWidget(self.TWChoix,"MotClef")
        MotClefLayout = QGridLayout(self.MotClef,1,1,11,6,"MotClefLayout")

        self.textLabel1_2 = QLabel(self.MotClef,"textLabel1_2")

        MotClefLayout.addWidget(self.textLabel1_2,0,1)

        self.LBMCPermis = QListBox(self.MotClef,"LBMCPermis")
        self.LBMCPermis.setMinimumSize(QSize(0,0))

        MotClefLayout.addWidget(self.LBMCPermis,1,0)

        self.LBRegles = QListBox(self.MotClef,"LBRegles")

        MotClefLayout.addWidget(self.LBRegles,1,1)

        self.textLabel1 = QLabel(self.MotClef,"textLabel1")
        self.textLabel1.setMinimumSize(QSize(0,0))

        MotClefLayout.addWidget(self.textLabel1,0,0)
        self.TWChoix.insertTab(self.MotClef,QString(""))

        self.Commande = QWidget(self.TWChoix,"Commande")
        CommandeLayout = QGridLayout(self.Commande,1,1,11,6,"CommandeLayout")

        self.LBNouvCommande = QListBox(self.Commande,"LBNouvCommande")

        CommandeLayout.addMultiCellWidget(self.LBNouvCommande,2,2,0,3)

        self.textLabel1_4 = QLabel(self.Commande,"textLabel1_4")

        CommandeLayout.addMultiCellWidget(self.textLabel1_4,0,0,0,1)

        self.buttonGroup1 = QButtonGroup(self.Commande,"buttonGroup1")

        self.RBGroupe = QRadioButton(self.buttonGroup1,"RBGroupe")
        self.RBGroupe.setGeometry(QRect(20,40,101,20))

        self.RBalpha = QRadioButton(self.buttonGroup1,"RBalpha")
        self.RBalpha.setGeometry(QRect(20,20,120,20))
        self.RBalpha.setChecked(1)

        CommandeLayout.addMultiCellWidget(self.buttonGroup1,0,1,3,3)

        self.textLabel4 = QLabel(self.Commande,"textLabel4")

        CommandeLayout.addMultiCellWidget(self.textLabel4,3,3,0,3)

        self.BNext = QToolButton(self.Commande,"BNext")
        self.BNext.setMinimumSize(QSize(60,0))
        self.BNext.setIconSet(QIconSet())

        CommandeLayout.addWidget(self.BNext,1,2)

        self.textLabel6 = QLabel(self.Commande,"textLabel6")
        self.textLabel6.setMinimumSize(QSize(40,0))

        CommandeLayout.addWidget(self.textLabel6,1,0)

        self.LEFiltre = QLineEdit(self.Commande,"LEFiltre")
        self.LEFiltre.setMinimumSize(QSize(160,30))

        CommandeLayout.addWidget(self.LEFiltre,1,1)
        self.TWChoix.insertTab(self.Commande,QString(""))

        self.TabPage = QWidget(self.TWChoix,"TabPage")

        LayoutWidget = QWidget(self.TabPage,"layout4")
        LayoutWidget.setGeometry(QRect(10,31,472,90))
        layout4 = QVBoxLayout(LayoutWidget,11,6,"layout4")

        self.textLabel1_3 = QLabel(LayoutWidget,"textLabel1_3")
        layout4.addWidget(self.textLabel1_3)

        self.LENomFichier = QLineEdit(LayoutWidget,"LENomFichier")
        self.LENomFichier.setMinimumSize(QSize(470,40))
        layout4.addWidget(self.LENomFichier)

        LayoutWidget_2 = QWidget(self.TabPage,"layout5")
        LayoutWidget_2.setGeometry(QRect(8,131,481,250))
        layout5 = QGridLayout(LayoutWidget_2,1,1,11,6,"layout5")

        layout3 = QHBoxLayout(None,0,6,"layout3")
        spacer3 = QSpacerItem(331,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout3.addItem(spacer3)

        self.BBrowse = QPushButton(LayoutWidget_2,"BBrowse")
        self.BBrowse.setSizePolicy(QSizePolicy(0,0,0,0,self.BBrowse.sizePolicy().hasHeightForWidth()))
        self.BBrowse.setMinimumSize(QSize(140,50))
        layout3.addWidget(self.BBrowse)

        layout5.addLayout(layout3,1,0)
        spacer1 = QSpacerItem(21,190,QSizePolicy.Minimum,QSizePolicy.Expanding)
        layout5.addItem(spacer1,0,0)
        self.TWChoix.insertTab(self.TabPage,QString(""))

        DPourLayout.addMultiCellWidget(self.TWChoix,0,0,0,2)

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)

        DPourLayout.addWidget(self.bSup,2,0)

        self.bOk = QPushButton(self,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        DPourLayout.addWidget(self.bOk,2,1)

        self.bHelp = QPushButton(self,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)

        DPourLayout.addWidget(self.bHelp,2,2)

        self.languageChange()

        self.resize(QSize(521,499).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListBoxItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bSup,SIGNAL("pressed()"),self.BSupPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.BNext,SIGNAL("clicked()"),self.BNextPressed)
        self.connect(self.BBrowse,SIGNAL("clicked()"),self.BBrowsePressed)
        self.connect(self.LENomFichier,SIGNAL("returnPressed()"),self.LENomFichReturnPressed)

        self.setTabOrder(self.LEFiltre,self.LENomFichier)
        self.setTabOrder(self.LENomFichier,self.TWChoix)
        self.setTabOrder(self.TWChoix,self.LBMCPermis)
        self.setTabOrder(self.LBMCPermis,self.LBRegles)
        self.setTabOrder(self.LBRegles,self.LBNouvCommande)
        self.setTabOrder(self.LBNouvCommande,self.RBalpha)
        self.setTabOrder(self.RBalpha,self.BBrowse)
        self.setTabOrder(self.BBrowse,self.bSup)
        self.setTabOrder(self.bSup,self.bOk)
        self.setTabOrder(self.bOk,self.bHelp)


    def languageChange(self):
        self.setCaption(self.__tr("DMacro"))
        self.Commentaire.setText(QString.null)
        self.textLabel1_2.setText(self.__trUtf8("\x3c\x68\x33\x3e\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x63\x65\x6e\x74\x65\x72\x22\x3e\x3c\x75\x3e\x3c\x62\x3e\x52\xc3\xa9\x67\x6c\x65\x73\x3c\x2f\x62\x3e\x3c\x2f\x75\x3e\x3c\x2f\x70\x3e\x3c\x2f\x68\x33\x3e"))
        self.textLabel1.setText(self.__tr("<h3><p align=\"center\"><u><b>Mots Clefs Permis</b></u></p></h3>"))
        self.TWChoix.changeTab(self.MotClef,self.__tr("Ajouter Mot-Clef"))
        self.textLabel1_4.setText(self.__tr("<b><u>Commandes :</u></b>"))
        self.buttonGroup1.setTitle(self.__tr("Affichage"))
        self.RBGroupe.setText(self.__tr("par groupe"))
        self.RBalpha.setText(self.__trUtf8("\x61\x6c\x70\x68\x61\x62\xc3\xa9\x74\x69\x71\x75\x65"))
        self.textLabel4.setText(self.__trUtf8("\x4c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x68\x6f\x69\x73\x69\x65\x20\x73\x65\x72\x61\x20\x61\x6a\x6f\x75\x74\xc3\xa9\x65\x20\x41\x50\x52\x45\x53\x20\x6c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x6f\x75\x72\x61\x6e\x74\x65"))
        self.BNext.setText(self.__tr("Suivant"))
        QToolTip.add(self.BNext,self.__tr("affiche la prochaine occurence"))
        self.textLabel6.setText(self.__tr("Filtre"))
        self.TWChoix.changeTab(self.Commande,self.__tr("Nouvelle Commande"))
        self.textLabel1_3.setText(self.__tr("<font size=\"+1\">La commande POURSUITE requiert un nom de Fichier :</font>"))
        self.BBrowse.setText(self.__tr("Edit"))
        self.TWChoix.changeTab(self.TabPage,self.__tr("Fichier Poursuite"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A"))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(self.__tr("Alt+D"))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))


    def LBNouvCommandeClicked(self):
        print "DPour.LBNouvCommandeClicked(): Not implemented yet"

    def LEFiltreTextChanged(self):
        print "DPour.LEFiltreTextChanged(): Not implemented yet"

    def LEfiltreReturnPressed(self):
        print "DPour.LEfiltreReturnPressed(): Not implemented yet"

    def BSupPressed(self):
        print "DPour.BSupPressed(): Not implemented yet"

    def BOkPressed(self):
        print "DPour.BOkPressed(): Not implemented yet"

    def BuildTabCommand(self):
        print "DPour.BuildTabCommand(): Not implemented yet"

    def BNextPressed(self):
        print "DPour.BNextPressed(): Not implemented yet"

    def BBrowsePressed(self):
        print "DPour.BBrowsePressed(): Not implemented yet"

    def LENomFichReturnPressed(self):
        print "DPour.LENomFichReturnPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DPour",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DPour",s,c,QApplication.UnicodeUTF8)
