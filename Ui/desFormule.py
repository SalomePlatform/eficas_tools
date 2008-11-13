# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desFormule.ui'
#
# Created: ven mai 16 13:30:38 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DFormule(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DFormule")

        self.setMinimumSize(QSize(505,0))

        DFormuleLayout = QGridLayout(self,1,1,11,6,"DFormuleLayout")

        layout4 = QHBoxLayout(None,0,6,"layout4")

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)
        layout4.addWidget(self.bSup)

        self.bOk = QPushButton(self,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)
        layout4.addWidget(self.bOk)

        self.bHelp = QPushButton(self,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)
        layout4.addWidget(self.bHelp)

        DFormuleLayout.addLayout(layout4,2,0)

        self.Commentaire = QLabel(self,"Commentaire")

        DFormuleLayout.addWidget(self.Commentaire,1,0)

        self.TWChoix = QTabWidget(self,"TWChoix")

        self.Formule = QWidget(self.TWChoix,"Formule")
        FormuleLayout = QGridLayout(self.Formule,1,1,11,6,"FormuleLayout")

        self.textLabel1 = QLabel(self.Formule,"textLabel1")
        self.textLabel1.setMinimumSize(QSize(0,0))

        FormuleLayout.addWidget(self.textLabel1,0,0)

        self.textLabel1_3 = QLabel(self.Formule,"textLabel1_3")

        FormuleLayout.addMultiCellWidget(self.textLabel1_3,6,6,0,1)

        layout6 = QHBoxLayout(None,0,6,"layout6")

        self.LENomFormule = QLineEdit(self.Formule,"LENomFormule")
        self.LENomFormule.setMinimumSize(QSize(0,40))
        layout6.addWidget(self.LENomFormule)

        layout4_2 = QHBoxLayout(None,0,6,"layout4_2")

        self.textLabel1_6 = QLabel(self.Formule,"textLabel1_6")
        layout4_2.addWidget(self.textLabel1_6)

        self.LENomsArgs = QLineEdit(self.Formule,"LENomsArgs")
        self.LENomsArgs.setMinimumSize(QSize(230,40))
        layout4_2.addWidget(self.LENomsArgs)

        self.textLabel1_6_2 = QLabel(self.Formule,"textLabel1_6_2")
        layout4_2.addWidget(self.textLabel1_6_2)
        layout6.addLayout(layout4_2)

        FormuleLayout.addMultiCellLayout(layout6,2,2,0,1)

        self.textLabel2 = QLabel(self.Formule,"textLabel2")

        FormuleLayout.addWidget(self.textLabel2,1,1)

        self.textLabel1_3_2 = QLabel(self.Formule,"textLabel1_3_2")

        FormuleLayout.addMultiCellWidget(self.textLabel1_3_2,7,7,0,1)

        self.textLabel2_2 = QLabel(self.Formule,"textLabel2_2")

        FormuleLayout.addMultiCellWidget(self.textLabel2_2,3,3,0,1)

        self.textLabel1_5 = QLabel(self.Formule,"textLabel1_5")
        self.textLabel1_5.setMinimumSize(QSize(0,0))

        FormuleLayout.addMultiCellWidget(self.textLabel1_5,4,4,0,1)

        self.LECorpsFormule = QLineEdit(self.Formule,"LECorpsFormule")
        self.LECorpsFormule.setMinimumSize(QSize(0,30))

        FormuleLayout.addMultiCellWidget(self.LECorpsFormule,5,5,0,1)

        self.textLabel1_2 = QLabel(self.Formule,"textLabel1_2")

        FormuleLayout.addWidget(self.textLabel1_2,0,1)
        self.TWChoix.insertTab(self.Formule,QString(""))

        self.Commande = QWidget(self.TWChoix,"Commande")
        CommandeLayout = QGridLayout(self.Commande,1,1,11,6,"CommandeLayout")

        self.textLabel4 = QLabel(self.Commande,"textLabel4")

        CommandeLayout.addMultiCellWidget(self.textLabel4,3,3,0,3)

        self.buttonGroup1 = QButtonGroup(self.Commande,"buttonGroup1")

        LayoutWidget = QWidget(self.buttonGroup1,"layout1")
        LayoutWidget.setGeometry(QRect(20,20,113,48))
        layout1 = QVBoxLayout(LayoutWidget,11,6,"layout1")

        self.RBalpha = QRadioButton(LayoutWidget,"RBalpha")
        self.RBalpha.setChecked(1)
        layout1.addWidget(self.RBalpha)

        self.RBGroupe = QRadioButton(LayoutWidget,"RBGroupe")
        layout1.addWidget(self.RBGroupe)

        CommandeLayout.addMultiCellWidget(self.buttonGroup1,0,1,3,3)

        self.LBNouvCommande = QListBox(self.Commande,"LBNouvCommande")

        CommandeLayout.addMultiCellWidget(self.LBNouvCommande,2,2,0,3)

        self.textLabel1_4 = QLabel(self.Commande,"textLabel1_4")

        CommandeLayout.addMultiCellWidget(self.textLabel1_4,0,0,0,2)

        self.textLabel6 = QLabel(self.Commande,"textLabel6")
        self.textLabel6.setMinimumSize(QSize(40,0))

        CommandeLayout.addWidget(self.textLabel6,1,0)

        self.LEFiltre = QLineEdit(self.Commande,"LEFiltre")
        self.LEFiltre.setMinimumSize(QSize(160,40))

        CommandeLayout.addWidget(self.LEFiltre,1,1)

        self.BNext = QToolButton(self.Commande,"BNext")
        self.BNext.setMinimumSize(QSize(60,40))
        self.BNext.setIconSet(QIconSet())

        CommandeLayout.addWidget(self.BNext,1,2)
        self.TWChoix.insertTab(self.Commande,QString(""))

        DFormuleLayout.addWidget(self.TWChoix,0,0)

        self.languageChange()

        self.resize(QSize(529,493).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListBoxItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bSup,SIGNAL("pressed()"),self.BSupPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.BNext,SIGNAL("clicked()"),self.BNextPressed)
        self.connect(self.LENomFormule,SIGNAL("returnPressed()"),self.NomFormuleSaisi)
        self.connect(self.LENomsArgs,SIGNAL("returnPressed()"),self.argsSaisis)
        self.connect(self.LECorpsFormule,SIGNAL("returnPressed()"),self.FormuleSaisie)
        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)

        self.setTabOrder(self.LEFiltre,self.LENomFormule)
        self.setTabOrder(self.LENomFormule,self.LENomsArgs)
        self.setTabOrder(self.LENomsArgs,self.LECorpsFormule)
        self.setTabOrder(self.LECorpsFormule,self.bSup)
        self.setTabOrder(self.bSup,self.bOk)
        self.setTabOrder(self.bOk,self.bHelp)
        self.setTabOrder(self.bHelp,self.TWChoix)
        self.setTabOrder(self.TWChoix,self.RBalpha)
        self.setTabOrder(self.RBalpha,self.RBGroupe)
        self.setTabOrder(self.RBGroupe,self.LBNouvCommande)


    def languageChange(self):
        self.setCaption(self.__tr("DMacro"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A"))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(self.__tr("Alt+D"))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))
        self.Commentaire.setText(QString.null)
        self.textLabel1.setText(self.__tr("<h3><p align=\"center\"><u><b>Nom de la formule</b></u></p></h3>"))
        self.textLabel1_3.setText(self.__trUtf8("\x52\x65\x74\x6f\x75\x72\x2d\x43\x68\x61\x72\x69\x6f\x74\x20\x70\x65\x72\x6d\x65\x74\x20\x64\x65\x20\x76\xc3\xa9\x72\x69\x66\x69\x65\x72\x20\x71\x75\x65\x20\x6c\x27\x65\x78\x70\x72\x65\x73\x73\x69\x6f\x6e\x20\x65\x73\x74\x20\x76\x61\x6c\x69\x64\x65\x2e"))
        self.textLabel1_6.setText(self.__tr("<h1><b>(</b></h1>"))
        self.textLabel1_6_2.setText(self.__tr("<h1><b>)</b></h1>"))
        self.textLabel2.setText(self.__trUtf8("\x76\x61\x72\x69\x61\x62\x6c\x65\x73\x20\x73\xc3\xa9\x70\x61\x72\xc3\xa9\x65\x73\x20\x70\x61\x72\x20\x64\x65\x73\x20\x22\x2c\x22\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x70\x61\x72\x20\x65\x78\x2e\x20\x3a\x20\x78\x2c\x79\x2c\x7a"))
        self.textLabel1_3_2.setText(self.__trUtf8("\x43\x65\x20\x6e\x27\x65\x73\x74\x20\x71\x75\x27\x61\x70\x72\xc3\xa8\x73\x20\x61\x76\x6f\x69\x72\x20\x61\x70\x70\x75\x79\xc3\xa9\x20\x73\x75\x72\x20\x6c\x65\x20\x62\x6f\x75\x74\x6f\x6e\x20\x56\x61\x6c\x69\x64\x65\x72\x20\x71\x75\x65\x20\x6c\x65\x73\x20\x6e\x6f\x75\x76\x65\x6c\x6c\x65\x73\x0a\x76\x61\x6c\x65\x75\x72\x73\x20\x73\x65\x72\x6f\x6e\x74\x20\x65\x66\x66\x65\x63\x74\x69\x76\x65\x6d\x65\x6e\x74\x20\x70\x72\x69\x73\x65\x73\x20\x65\x6e\x20\x63\x6f\x6d\x70\x74\x65"))
        self.textLabel2_2.setText(self.__tr("<font size=\"+4\" face=\"Helvetica\"><b>=</b></font>"))
        self.textLabel1_5.setText(self.__tr("<h3><p align=\"center\"><u><b>Expression</b></u></p></h3>"))
        self.textLabel1_2.setText(self.__tr("<h3><p align=\"center\"><u><b>Arguments</b></u></p></h3>"))
        self.TWChoix.changeTab(self.Formule,self.__trUtf8("\x44\xc3\xa9\x66\x69\x6e\x69\x74\x69\x6f\x6e\x20\x46\x6f\x72\x6d\x75\x6c\x65"))
        self.textLabel4.setText(self.__trUtf8("\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x6c\x65\x66\x74\x22\x3e\x4c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x68\x6f\x69\x73\x69\x65\x20\x73\x65\x72\x61\x20\x61\x6a\x6f\x75\x74\xc3\xa9\x65\x20\x41\x50\x52\x45\x53\x20\x6c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x6f\x75\x72\x61\x6e\x74\x65\x3c\x2f\x70\x3e"))
        self.buttonGroup1.setTitle(self.__tr("Affichage"))
        self.RBalpha.setText(self.__trUtf8("\x61\x6c\x70\x68\x61\x62\xc3\xa9\x74\x69\x71\x75\x65"))
        self.RBGroupe.setText(self.__tr("par groupe"))
        self.textLabel1_4.setText(self.__tr("<b><u>Commandes :</u></b>"))
        self.textLabel6.setText(self.__tr("Filtre"))
        self.BNext.setText(self.__tr("Suivant"))
        QToolTip.add(self.BNext,self.__tr("affiche la prochaine occurence"))
        self.TWChoix.changeTab(self.Commande,self.__tr("Nouvelle Commande"))


    def LBNouvCommandeClicked(self):
        print "DFormule.LBNouvCommandeClicked(): Not implemented yet"

    def LEFiltreTextChanged(self):
        print "DFormule.LEFiltreTextChanged(): Not implemented yet"

    def LEfiltreReturnPressed(self):
        print "DFormule.LEfiltreReturnPressed(): Not implemented yet"

    def BSupPressed(self):
        print "DFormule.BSupPressed(): Not implemented yet"

    def BOkPressed(self):
        print "DFormule.BOkPressed(): Not implemented yet"

    def BuildTabCommand(self):
        print "DFormule.BuildTabCommand(): Not implemented yet"

    def BNextPressed(self):
        print "DFormule.BNextPressed(): Not implemented yet"

    def NomFormuleSaisi(self):
        print "DFormule.NomFormuleSaisi(): Not implemented yet"

    def argsSaisis(self):
        print "DFormule.argsSaisis(): Not implemented yet"

    def FormuleSaisie(self):
        print "DFormule.FormuleSaisie(): Not implemented yet"

    def ViewDoc(self):
        print "DFormule.ViewDoc(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DFormule",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DFormule",s,c,QApplication.UnicodeUTF8)
