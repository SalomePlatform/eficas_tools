# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desCommande.ui'
#
# Created: ven mai 16 13:30:38 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DComm(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DComm")

        self.setMinimumSize(QSize(505,0))

        DCommLayout = QGridLayout(self,1,1,11,6,"DCommLayout")

        self.Commentaire = QLabel(self,"Commentaire")
        self.Commentaire.setFrameShape(QLabel.NoFrame)
        self.Commentaire.setFrameShadow(QLabel.Plain)

        DCommLayout.addMultiCellWidget(self.Commentaire,1,1,0,2)

        self.bOk = QPushButton(self,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        DCommLayout.addWidget(self.bOk,2,1)

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)

        DCommLayout.addWidget(self.bSup,2,0)

        self.bHelp = QPushButton(self,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)

        DCommLayout.addWidget(self.bHelp,2,2)

        self.TWChoix = QTabWidget(self,"TWChoix")

        self.MotClef = QWidget(self.TWChoix,"MotClef")

        self.textLabel1 = QLabel(self.MotClef,"textLabel1")
        self.textLabel1.setGeometry(QRect(11,11,226,18))
        self.textLabel1.setMinimumSize(QSize(0,0))

        self.LBMCPermis = QListBox(self.MotClef,"LBMCPermis")
        self.LBMCPermis.setGeometry(QRect(11,35,226,342))
        self.LBMCPermis.setMinimumSize(QSize(0,0))

        self.textLabel1_2 = QLabel(self.MotClef,"textLabel1_2")
        self.textLabel1_2.setGeometry(QRect(243,11,225,18))

        self.LBRegles = QListBox(self.MotClef,"LBRegles")
        self.LBRegles.setGeometry(QRect(243,35,225,342))
        self.TWChoix.insertTab(self.MotClef,QString(""))

        self.Concept = QWidget(self.TWChoix,"Concept")
        ConceptLayout = QGridLayout(self.Concept,1,1,11,6,"ConceptLayout")

        self.groupBox1 = QGroupBox(self.Concept,"groupBox1")

        self.textLabel1_3 = QLabel(self.groupBox1,"textLabel1_3")
        self.textLabel1_3.setGeometry(QRect(80,50,130,31))

        self.textLabel1_3_2 = QLabel(self.groupBox1,"textLabel1_3_2")
        self.textLabel1_3_2.setGeometry(QRect(80,170,150,31))

        self.LENomConcept = QLineEdit(self.groupBox1,"LENomConcept")
        self.LENomConcept.setGeometry(QRect(80,110,310,30))

        self.textLabel3 = QLabel(self.groupBox1,"textLabel3")
        self.textLabel3.setGeometry(QRect(10,200,290,31))

        self.typeConcept = QLabel(self.groupBox1,"typeConcept")
        self.typeConcept.setGeometry(QRect(310,200,130,31))

        ConceptLayout.addWidget(self.groupBox1,0,0)
        self.TWChoix.insertTab(self.Concept,QString(""))

        self.Commande = QWidget(self.TWChoix,"Commande")
        CommandeLayout = QGridLayout(self.Commande,1,1,11,6,"CommandeLayout")

        self.buttonGroup1 = QButtonGroup(self.Commande,"buttonGroup1")

        self.RBalpha = QRadioButton(self.buttonGroup1,"RBalpha")
        self.RBalpha.setGeometry(QRect(20,20,120,20))
        self.RBalpha.setChecked(1)

        self.RBGroupe = QRadioButton(self.buttonGroup1,"RBGroupe")
        self.RBGroupe.setGeometry(QRect(20,40,110,20))

        CommandeLayout.addMultiCellWidget(self.buttonGroup1,0,1,3,3)

        self.LBNouvCommande = QListBox(self.Commande,"LBNouvCommande")

        CommandeLayout.addMultiCellWidget(self.LBNouvCommande,2,2,0,3)

        self.textLabel1_4 = QLabel(self.Commande,"textLabel1_4")
        self.textLabel1_4.setMaximumSize(QSize(32767,20))

        CommandeLayout.addMultiCellWidget(self.textLabel1_4,0,0,0,2)

        self.textLabel4 = QLabel(self.Commande,"textLabel4")

        CommandeLayout.addMultiCellWidget(self.textLabel4,3,3,0,3)

        self.textLabel6 = QLabel(self.Commande,"textLabel6")
        self.textLabel6.setMinimumSize(QSize(40,40))

        CommandeLayout.addWidget(self.textLabel6,1,0)

        self.LEFiltre = QLineEdit(self.Commande,"LEFiltre")
        self.LEFiltre.setMinimumSize(QSize(0,40))

        CommandeLayout.addWidget(self.LEFiltre,1,1)

        self.BNext = QToolButton(self.Commande,"BNext")
        self.BNext.setMinimumSize(QSize(70,40))
        self.BNext.setIconSet(QIconSet())

        CommandeLayout.addWidget(self.BNext,1,2)
        self.TWChoix.insertTab(self.Commande,QString(""))

        DCommLayout.addMultiCellWidget(self.TWChoix,0,0,0,2)

        self.languageChange()

        self.resize(QSize(505,483).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListBoxItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bSup,SIGNAL("pressed()"),self.BSupPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.LENomConcept,SIGNAL("returnPressed()"),self.LENomConceptReturnPressed)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)
        self.connect(self.BNext,SIGNAL("pressed()"),self.BNextPressed)

        self.setTabOrder(self.LEFiltre,self.LBRegles)
        self.setTabOrder(self.LBRegles,self.LENomConcept)
        self.setTabOrder(self.LENomConcept,self.TWChoix)
        self.setTabOrder(self.TWChoix,self.LBMCPermis)
        self.setTabOrder(self.LBMCPermis,self.RBalpha)
        self.setTabOrder(self.RBalpha,self.LBNouvCommande)
        self.setTabOrder(self.LBNouvCommande,self.bOk)
        self.setTabOrder(self.bOk,self.bSup)
        self.setTabOrder(self.bSup,self.bHelp)


    def languageChange(self):
        self.setCaption(self.__tr("DComm"))
        self.Commentaire.setText(QString.null)
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A"))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(self.__tr("Alt+D"))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))
        self.textLabel1.setText(self.__tr("<h3><p align=\"center\"><u><b>Mots Clefs Permis</b></u></p></h3>"))
        self.textLabel1_2.setText(self.__trUtf8("\x3c\x68\x33\x3e\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x63\x65\x6e\x74\x65\x72\x22\x3e\x3c\x75\x3e\x3c\x62\x3e\x52\xc3\xa8\x67\x6c\x65\x73\x3c\x2f\x62\x3e\x3c\x2f\x75\x3e\x3c\x2f\x70\x3e\x3c\x2f\x68\x33\x3e"))
        self.TWChoix.changeTab(self.MotClef,self.__tr("Ajouter Mot-Clef"))
        self.groupBox1.setTitle(self.__tr("Concept"))
        self.textLabel1_3.setText(self.__tr("<u>Nom du concept :</u>"))
        self.textLabel1_3_2.setText(self.__tr("<u>Type du concept :</u>"))
        self.textLabel3.setText(self.__trUtf8("\x4c\x27\x6f\x70\xc3\xa9\x72\x61\x74\x65\x75\x72\x20\x72\x65\x74\x6f\x75\x72\x6e\x65\x20\x75\x6e\x20\x63\x6f\x6e\x63\x65\x70\x74\x20\x64\x65\x20\x74\x79\x70\x65\x20\x3a"))
        self.typeConcept.setText(self.__tr("TypeDuConcept"))
        self.TWChoix.changeTab(self.Concept,self.__tr("Nommer Concept"))
        self.buttonGroup1.setTitle(self.__tr("Affichage"))
        self.RBalpha.setText(self.__trUtf8("\x61\x6c\x70\x68\x61\x62\xc3\xa9\x74\x69\x71\x75\x65"))
        self.RBGroupe.setText(self.__tr("par groupe"))
        self.textLabel1_4.setText(self.__tr("<b><u>Commandes :</u></b>"))
        self.textLabel4.setText(self.__trUtf8("\x4c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x68\x6f\x69\x73\x69\x65\x20\x73\x65\x72\x61\x20\x61\x6a\x6f\x75\x74\xc3\xa9\x65\x20\x41\x50\x52\x45\x53\x20\x6c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x6f\x75\x72\x61\x6e\x74\x65"))
        self.textLabel6.setText(self.__tr("Filtre"))
        self.BNext.setText(self.__tr("Suivant"))
        QToolTip.add(self.BNext,self.__tr("affiche la prochaine occurence"))
        self.TWChoix.changeTab(self.Commande,self.__tr("Nouvelle Commande"))


    def LBNouvCommandeClicked(self):
        print "DComm.LBNouvCommandeClicked(): Not implemented yet"

    def LEFiltreTextChanged(self):
        print "DComm.LEFiltreTextChanged(): Not implemented yet"

    def LEfiltreReturnPressed(self):
        print "DComm.LEfiltreReturnPressed(): Not implemented yet"

    def BSupPressed(self):
        print "DComm.BSupPressed(): Not implemented yet"

    def LENomConceptReturnPressed(self):
        print "DComm.LENomConceptReturnPressed(): Not implemented yet"

    def BOkPressed(self):
        print "DComm.BOkPressed(): Not implemented yet"

    def BuildTabCommand(self):
        print "DComm.BuildTabCommand(): Not implemented yet"

    def ViewDoc(self):
        print "DComm.ViewDoc(): Not implemented yet"

    def BNextPressed(self):
        print "DComm.BNextPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DComm",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DComm",s,c,QApplication.UnicodeUTF8)
