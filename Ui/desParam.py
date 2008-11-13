# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desParam.ui'
#
# Created: ven mai 16 13:30:38 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DParam(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DParam")

        self.setMinimumSize(QSize(505,0))

        DParamLayout = QGridLayout(self,1,1,11,6,"DParamLayout")

        self.Commentaire = QLabel(self,"Commentaire")
        self.Commentaire.setFrameShape(QLabel.NoFrame)
        self.Commentaire.setFrameShadow(QLabel.Plain)

        DParamLayout.addMultiCellWidget(self.Commentaire,1,1,0,2)

        self.TWChoix = QTabWidget(self,"TWChoix")

        self.Valeur_Parametre = QWidget(self.TWChoix,"Valeur_Parametre")

        self.textLabel2_2_2 = QLabel(self.Valeur_Parametre,"textLabel2_2_2")
        self.textLabel2_2_2.setGeometry(QRect(80,11,231,89))

        self.Commentaire_2 = QLabel(self.Valeur_Parametre,"Commentaire_2")
        self.Commentaire_2.setGeometry(QRect(11,275,459,89))

        self.lineEditNom = QLineEdit(self.Valeur_Parametre,"lineEditNom")
        self.lineEditNom.setGeometry(QRect(80,106,231,31))
        self.lineEditNom.setMinimumSize(QSize(231,31))

        self.textLabel2_2 = QLabel(self.Valeur_Parametre,"textLabel2_2")
        self.textLabel2_2.setGeometry(QRect(11,106,63,31))

        self.textLabel2 = QLabel(self.Valeur_Parametre,"textLabel2")
        self.textLabel2.setGeometry(QRect(11,143,63,31))

        self.Commentaire2 = QLabel(self.Valeur_Parametre,"Commentaire2")
        self.Commentaire2.setGeometry(QRect(11,180,459,89))

        self.lineEditVal = QLineEdit(self.Valeur_Parametre,"lineEditVal")
        self.lineEditVal.setGeometry(QRect(80,143,231,31))
        self.lineEditVal.setMinimumSize(QSize(231,31))
        self.TWChoix.insertTab(self.Valeur_Parametre,QString(""))

        self.Commande = QWidget(self.TWChoix,"Commande")
        CommandeLayout = QGridLayout(self.Commande,1,1,11,6,"CommandeLayout")

        self.textLabel6 = QLabel(self.Commande,"textLabel6")
        self.textLabel6.setMinimumSize(QSize(40,0))

        CommandeLayout.addWidget(self.textLabel6,1,0)

        self.LBNouvCommande = QListBox(self.Commande,"LBNouvCommande")

        CommandeLayout.addMultiCellWidget(self.LBNouvCommande,2,2,0,3)

        self.buttonGroup1 = QButtonGroup(self.Commande,"buttonGroup1")

        self.RBGroupe = QRadioButton(self.buttonGroup1,"RBGroupe")
        self.RBGroupe.setGeometry(QRect(20,40,101,20))

        self.RBalpha = QRadioButton(self.buttonGroup1,"RBalpha")
        self.RBalpha.setGeometry(QRect(20,20,120,20))
        self.RBalpha.setChecked(1)

        CommandeLayout.addMultiCellWidget(self.buttonGroup1,0,1,3,3)

        self.textLabel1_4 = QLabel(self.Commande,"textLabel1_4")

        CommandeLayout.addMultiCellWidget(self.textLabel1_4,0,0,0,1)

        self.textLabel4 = QLabel(self.Commande,"textLabel4")

        CommandeLayout.addMultiCellWidget(self.textLabel4,3,3,0,3)

        self.BNext = QToolButton(self.Commande,"BNext")
        self.BNext.setMinimumSize(QSize(60,0))
        self.BNext.setIconSet(QIconSet())

        CommandeLayout.addWidget(self.BNext,1,2)

        self.LEFiltre = QLineEdit(self.Commande,"LEFiltre")
        self.LEFiltre.setMinimumSize(QSize(160,30))

        CommandeLayout.addWidget(self.LEFiltre,1,1)
        self.TWChoix.insertTab(self.Commande,QString(""))

        DParamLayout.addMultiCellWidget(self.TWChoix,0,0,0,2)

        self.bOk = QPushButton(self,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        DParamLayout.addWidget(self.bOk,2,1)

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)

        DParamLayout.addWidget(self.bSup,2,0)

        self.bHelp = QPushButton(self,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)

        DParamLayout.addWidget(self.bHelp,2,2)

        self.languageChange()

        self.resize(QSize(505,483).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListBoxItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bSup,SIGNAL("pressed()"),self.BSupPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)
        self.connect(self.BNext,SIGNAL("pressed()"),self.BNextPressed)
        self.connect(self.lineEditVal,SIGNAL("returnPressed()"),self.BOkPressed)

        self.setTabOrder(self.LEFiltre,self.TWChoix)
        self.setTabOrder(self.TWChoix,self.lineEditNom)
        self.setTabOrder(self.lineEditNom,self.lineEditVal)
        self.setTabOrder(self.lineEditVal,self.LBNouvCommande)
        self.setTabOrder(self.LBNouvCommande,self.RBalpha)
        self.setTabOrder(self.RBalpha,self.bOk)
        self.setTabOrder(self.bOk,self.bSup)
        self.setTabOrder(self.bSup,self.bHelp)


    def languageChange(self):
        self.setCaption(self.__tr("DComm"))
        self.Commentaire.setText(QString.null)
        self.textLabel2_2_2.setText(self.__tr("<u><b><p align=\"center\">Parametre</p></b></u>"))
        self.Commentaire_2.setText(QString.null)
        self.textLabel2_2.setText(self.__tr("<b> Nom: </b>"))
        self.textLabel2.setText(self.__tr("<b> Valeur: </b>"))
        self.Commentaire2.setText(self.__trUtf8("\x52\x65\x74\x6f\x75\x72\x20\x43\x68\x61\x72\x69\x6f\x74\x20\x64\x61\x6e\x73\x20\x75\x6e\x65\x20\x73\x6f\x6e\x65\x20\x64\x65\x20\x73\x61\x69\x73\x69\x65\x20\x70\x65\x72\x6d\x65\x74\x20\x64\x65\x20\x76\xc3\xa9\x72\x69\x66\x69\x65\x72\x20\x6c\x61\x20\x0a\x76\x61\x6c\x69\x64\x69\x74\xc3\xa9\x20\x64\x65\x20\x6c\x61\x20\x76\x61\x6c\x65\x75\x72\x20\x73\x61\x69\x73\x69\x65\x2e\x0a\x0a\x4c\x65\x73\x20\x6e\x6f\x75\x76\x65\x6c\x6c\x65\x73\x20\x76\x61\x6c\x65\x75\x72\x73\x20\x6e\x65\x20\x73\x65\x72\x6f\x6e\x74\x20\x70\x72\x69\x73\x65\x73\x20\x20\x65\x6e\x20\x63\x6f\x6d\x70\x74\x65\x20\x71\x75\x27\x61\x70\x72\xc3\xa8\x73\x20\x61\x76\x6f\x69\x72\x20\x0a\x61\x70\x70\x75\x79\xc3\xa9\x20\x73\x75\x72\x20\x20\x6c\x65\x20\x62\x6f\x75\x74\x6f\x6e\x20\x56\x61\x6c\x69\x64\x65\x72\x2e"))
        self.TWChoix.changeTab(self.Valeur_Parametre,self.__tr("Valeur Parametre"))
        self.textLabel6.setText(self.__tr("Filtre"))
        self.buttonGroup1.setTitle(self.__tr("Affichage"))
        self.RBGroupe.setText(self.__tr("par groupe"))
        self.RBalpha.setText(self.__trUtf8("\x61\x6c\x70\x68\x61\x62\xc3\xa9\x74\x69\x71\x75\x65"))
        self.textLabel1_4.setText(self.__tr("<b><u>Commandes :</u></b>"))
        self.textLabel4.setText(self.__trUtf8("\x4c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x68\x6f\x69\x73\x69\x65\x20\x73\x65\x72\x61\x20\x61\x6a\x6f\x75\x74\xc3\xa9\x65\x20\x41\x50\x52\x45\x53\x20\x6c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x6f\x75\x72\x61\x6e\x74\x65"))
        self.BNext.setText(self.__tr("Suivant"))
        QToolTip.add(self.BNext,self.__tr("affiche la prochaine occurence"))
        self.TWChoix.changeTab(self.Commande,self.__tr("Nouvelle Commande"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A"))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(self.__tr("Alt+D"))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))


    def LBNouvCommandeClicked(self):
        print "DParam.LBNouvCommandeClicked(): Not implemented yet"

    def LEFiltreTextChanged(self):
        print "DParam.LEFiltreTextChanged(): Not implemented yet"

    def LEfiltreReturnPressed(self):
        print "DParam.LEfiltreReturnPressed(): Not implemented yet"

    def BSupPressed(self):
        print "DParam.BSupPressed(): Not implemented yet"

    def LENomConceptReturnPressed(self):
        print "DParam.LENomConceptReturnPressed(): Not implemented yet"

    def BOkPressed(self):
        print "DParam.BOkPressed(): Not implemented yet"

    def BuildTabCommand(self):
        print "DParam.BuildTabCommand(): Not implemented yet"

    def ViewDoc(self):
        print "DParam.ViewDoc(): Not implemented yet"

    def BNextPressed(self):
        print "DParam.BNextPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DParam",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DParam",s,c,QApplication.UnicodeUTF8)
