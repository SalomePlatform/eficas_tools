# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desInclude.ui'
#
# Created: ven mai 16 13:30:38 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DInc1(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DInc1")

        self.setMinimumSize(QSize(505,0))

        DInc1Layout = QGridLayout(self,1,1,11,6,"DInc1Layout")

        self.bOk = QPushButton(self,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        DInc1Layout.addWidget(self.bOk,2,1)

        self.bHelp = QPushButton(self,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)

        DInc1Layout.addWidget(self.bHelp,2,2)

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)

        DInc1Layout.addWidget(self.bSup,2,0)

        self.Commentaire = QLabel(self,"Commentaire")

        DInc1Layout.addMultiCellWidget(self.Commentaire,1,1,0,2)

        self.TWChoix = QTabWidget(self,"TWChoix")

        self.MotClef = QWidget(self.TWChoix,"MotClef")
        MotClefLayout = QGridLayout(self.MotClef,1,1,11,6,"MotClefLayout")

        self.LBMCPermis = QListBox(self.MotClef,"LBMCPermis")
        self.LBMCPermis.setMinimumSize(QSize(0,0))

        MotClefLayout.addWidget(self.LBMCPermis,1,0)

        self.textLabel1 = QLabel(self.MotClef,"textLabel1")
        self.textLabel1.setMinimumSize(QSize(0,0))

        MotClefLayout.addWidget(self.textLabel1,0,0)

        self.LBRegles = QListBox(self.MotClef,"LBRegles")

        MotClefLayout.addWidget(self.LBRegles,1,1)

        self.textLabel1_2 = QLabel(self.MotClef,"textLabel1_2")

        MotClefLayout.addWidget(self.textLabel1_2,0,1)
        self.TWChoix.insertTab(self.MotClef,QString(""))

        self.Commande = QWidget(self.TWChoix,"Commande")
        CommandeLayout = QGridLayout(self.Commande,1,1,11,6,"CommandeLayout")

        self.LBNouvCommande = QListBox(self.Commande,"LBNouvCommande")

        CommandeLayout.addMultiCellWidget(self.LBNouvCommande,2,2,0,3)

        self.buttonGroup1 = QButtonGroup(self.Commande,"buttonGroup1")

        self.RBGroupe = QRadioButton(self.buttonGroup1,"RBGroupe")
        self.RBGroupe.setGeometry(QRect(20,40,101,20))

        self.RBalpha = QRadioButton(self.buttonGroup1,"RBalpha")
        self.RBalpha.setGeometry(QRect(20,20,120,20))
        self.RBalpha.setChecked(1)

        CommandeLayout.addMultiCellWidget(self.buttonGroup1,0,1,3,3)

        self.textLabel4 = QLabel(self.Commande,"textLabel4")

        CommandeLayout.addMultiCellWidget(self.textLabel4,3,3,0,3)

        self.textLabel1_4 = QLabel(self.Commande,"textLabel1_4")

        CommandeLayout.addMultiCellWidget(self.textLabel1_4,0,0,0,2)

        self.textLabel6 = QLabel(self.Commande,"textLabel6")
        self.textLabel6.setMinimumSize(QSize(40,0))

        CommandeLayout.addWidget(self.textLabel6,1,0)

        self.LEFiltre = QLineEdit(self.Commande,"LEFiltre")
        self.LEFiltre.setMinimumSize(QSize(160,40))

        CommandeLayout.addWidget(self.LEFiltre,1,1)

        self.BNext = QToolButton(self.Commande,"BNext")
        self.BNext.setMinimumSize(QSize(60,0))
        self.BNext.setIconSet(QIconSet())

        CommandeLayout.addWidget(self.BNext,1,2)
        self.TWChoix.insertTab(self.Commande,QString(""))

        self.TabPage = QWidget(self.TWChoix,"TabPage")

        self.textLabel1_3 = QLabel(self.TabPage,"textLabel1_3")
        self.textLabel1_3.setGeometry(QRect(30,40,440,41))

        self.LENomFichier = QLineEdit(self.TabPage,"LENomFichier")
        self.LENomFichier.setGeometry(QRect(18,117,450,40))
        self.LENomFichier.setSizePolicy(QSizePolicy(0,0,0,0,self.LENomFichier.sizePolicy().hasHeightForWidth()))
        self.LENomFichier.setMinimumSize(QSize(450,40))

        self.BBrowse = QPushButton(self.TabPage,"BBrowse")
        self.BBrowse.setGeometry(QRect(288,306,161,41))
        self.BBrowse.setSizePolicy(QSizePolicy(0,0,0,0,self.BBrowse.sizePolicy().hasHeightForWidth()))

        self.BChangeFile = QPushButton(self.TabPage,"BChangeFile")
        self.BChangeFile.setGeometry(QRect(290,350,161,41))
        self.BChangeFile.setSizePolicy(QSizePolicy(0,0,0,0,self.BChangeFile.sizePolicy().hasHeightForWidth()))
        self.TWChoix.insertTab(self.TabPage,QString(""))

        self.TabPage_2 = QWidget(self.TWChoix,"TabPage_2")
        TabPageLayout = QGridLayout(self.TabPage_2,1,1,11,6,"TabPageLayout")

        self.textLabel1_5 = QLabel(self.TabPage_2,"textLabel1_5")

        TabPageLayout.addWidget(self.textLabel1_5,0,0)
        self.TWChoix.insertTab(self.TabPage_2,QString(""))

        DInc1Layout.addMultiCellWidget(self.TWChoix,0,0,0,2)

        self.languageChange()

        self.resize(QSize(521,511).expandedTo(self.minimumSizeHint()))
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
        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)

        self.setTabOrder(self.LEFiltre,self.LENomFichier)
        self.setTabOrder(self.LENomFichier,self.bHelp)
        self.setTabOrder(self.bHelp,self.bSup)
        self.setTabOrder(self.bSup,self.bOk)
        self.setTabOrder(self.bOk,self.TWChoix)
        self.setTabOrder(self.TWChoix,self.LBMCPermis)
        self.setTabOrder(self.LBMCPermis,self.LBRegles)
        self.setTabOrder(self.LBRegles,self.LBNouvCommande)
        self.setTabOrder(self.LBNouvCommande,self.RBalpha)
        self.setTabOrder(self.RBalpha,self.BBrowse)
        self.setTabOrder(self.BBrowse,self.BChangeFile)


    def languageChange(self):
        self.setCaption(self.__tr("DMacro"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A"))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(self.__tr("Alt+D"))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.Commentaire.setText(QString.null)
        self.textLabel1.setText(self.__tr("<h3><p align=\"center\"><u><b>Mots Clefs Permis</b></u></p></h3>"))
        self.textLabel1_2.setText(self.__trUtf8("\x3c\x68\x33\x3e\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x63\x65\x6e\x74\x65\x72\x22\x3e\x3c\x75\x3e\x3c\x62\x3e\x52\xc3\xa9\x67\x6c\x65\x73\x3c\x2f\x62\x3e\x3c\x2f\x75\x3e\x3c\x2f\x70\x3e\x3c\x2f\x68\x33\x3e"))
        self.TWChoix.changeTab(self.MotClef,self.__tr("Ajouter Mot-Clef"))
        self.buttonGroup1.setTitle(self.__tr("Affichage"))
        self.RBGroupe.setText(self.__tr("par groupe"))
        self.RBalpha.setText(self.__trUtf8("\x61\x6c\x70\x68\x61\x62\xc3\xa9\x74\x69\x71\x75\x65"))
        self.textLabel4.setText(self.__trUtf8("\x4c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x68\x6f\x69\x73\x69\x65\x20\x73\x65\x72\x61\x20\x61\x6a\x6f\x75\x74\xc3\xa9\x65\x20\x41\x50\x52\x45\x53\x20\x6c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x6f\x75\x72\x61\x6e\x74\x65"))
        self.textLabel1_4.setText(self.__tr("<b><u>Commandes :</u></b>"))
        self.textLabel6.setText(self.__tr("Filtre"))
        self.BNext.setText(self.__tr("Suivant"))
        QToolTip.add(self.BNext,self.__tr("affiche la prochaine occurence"))
        self.TWChoix.changeTab(self.Commande,self.__tr("Nouvelle Commande"))
        self.textLabel1_3.setText(self.__tr("<font size=\"+1\">La commande INCLUDE requiert un nom de Fichier :</font>"))
        self.BBrowse.setText(self.__tr("Edit"))
        self.BChangeFile.setText(self.__tr("Autre Fichier"))
        self.TWChoix.changeTab(self.TabPage,self.__tr("Fichier Include"))
        self.textLabel1_5.setText(self.__trUtf8("\x3c\x66\x6f\x6e\x74\x20\x73\x69\x7a\x65\x3d\x22\x2b\x31\x22\x3e\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x63\x65\x6e\x74\x65\x72\x22\x3e\x4c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x49\x4e\x43\x4c\x55\x44\x45\x20\x6e\x27\x61\x20\x70\x61\x73\x20\x64\x65\x20\x66\x69\x63\x68\x69\x65\x72\x20\x61\x73\x73\x6f\x63\x69\xc3\xa9\x2e\x0a\x49\x6c\x20\x66\x61\x75\x74\x20\x64\x27\x61\x62\x6f\x72\x64\x20\x63\x68\x6f\x69\x73\x69\x72\x20\x75\x6e\x20\x6e\x75\x6d\xc3\xa9\x72\x6f\x20\x64\x27\x75\x6e\x69\x74\xc3\xa9\x3c\x2f\x70\x3e\x3c\x2f\x66\x6f\x6e\x74\x3e"))
        self.TWChoix.changeTab(self.TabPage_2,self.__tr("Fichier Inc"))


    def LBNouvCommandeClicked(self):
        print "DInc1.LBNouvCommandeClicked(): Not implemented yet"

    def LEFiltreTextChanged(self):
        print "DInc1.LEFiltreTextChanged(): Not implemented yet"

    def LEfiltreReturnPressed(self):
        print "DInc1.LEfiltreReturnPressed(): Not implemented yet"

    def BSupPressed(self):
        print "DInc1.BSupPressed(): Not implemented yet"

    def BOkPressed(self):
        print "DInc1.BOkPressed(): Not implemented yet"

    def BuildTabCommand(self):
        print "DInc1.BuildTabCommand(): Not implemented yet"

    def BNextPressed(self):
        print "DInc1.BNextPressed(): Not implemented yet"

    def BBrowsePressed(self):
        print "DInc1.BBrowsePressed(): Not implemented yet"

    def LENomFichReturnPressed(self):
        print "DInc1.LENomFichReturnPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DInc1.ViewDoc(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DInc1",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DInc1",s,c,QApplication.UnicodeUTF8)
