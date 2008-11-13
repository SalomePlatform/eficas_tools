# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desCommentaire.ui'
#
# Created: Thu Jun 19 16:49:50 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.16
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DComment(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DComment")

        self.setMinimumSize(QSize(505,0))

        DCommentLayout = QGridLayout(self,1,1,11,6,"DCommentLayout")

        self.TWChoix = QTabWidget(self,"TWChoix")

        self.Valeur_Parametre = QWidget(self.TWChoix,"Valeur_Parametre")

        self.textCommentaire = QTextEdit(self.Valeur_Parametre,"textCommentaire")
        self.textCommentaire.setGeometry(QRect(0,0,480,390))
        self.TWChoix.insertTab(self.Valeur_Parametre,QString.fromLatin1(""))

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

        self.textLabel1_4 = QLabel(self.Commande,"textLabel1_4")

        CommandeLayout.addMultiCellWidget(self.textLabel1_4,0,0,0,2)

        self.textLabel4 = QLabel(self.Commande,"textLabel4")

        CommandeLayout.addMultiCellWidget(self.textLabel4,3,3,0,3)

        self.LEFiltre = QLineEdit(self.Commande,"LEFiltre")
        self.LEFiltre.setMinimumSize(QSize(160,30))

        CommandeLayout.addWidget(self.LEFiltre,1,1)

        self.BNext = QToolButton(self.Commande,"BNext")
        self.BNext.setMinimumSize(QSize(60,30))
        self.BNext.setIconSet(QIconSet())

        CommandeLayout.addWidget(self.BNext,1,2)

        self.textLabel6 = QLabel(self.Commande,"textLabel6")
        self.textLabel6.setMinimumSize(QSize(50,30))

        CommandeLayout.addWidget(self.textLabel6,1,0)
        self.TWChoix.insertTab(self.Commande,QString.fromLatin1(""))

        DCommentLayout.addMultiCellWidget(self.TWChoix,0,0,0,2)

        self.bOk = QPushButton(self,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        DCommentLayout.addWidget(self.bOk,2,1)

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)

        DCommentLayout.addWidget(self.bSup,2,0)

        self.bHelp = QPushButton(self,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)

        DCommentLayout.addWidget(self.bHelp,2,2)

        self.Commentaire = QLabel(self,"Commentaire")
        self.Commentaire.setFrameShape(QLabel.NoFrame)
        self.Commentaire.setFrameShadow(QLabel.Plain)

        DCommentLayout.addMultiCellWidget(self.Commentaire,1,1,0,2)

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
        self.connect(self.textCommentaire,SIGNAL("textChanged()"),self.TexteCommentaireEntre)

        self.setTabOrder(self.LEFiltre,self.TWChoix)
        self.setTabOrder(self.TWChoix,self.textCommentaire)
        self.setTabOrder(self.textCommentaire,self.LBNouvCommande)
        self.setTabOrder(self.LBNouvCommande,self.RBalpha)
        self.setTabOrder(self.RBalpha,self.bOk)
        self.setTabOrder(self.bOk,self.bSup)
        self.setTabOrder(self.bSup,self.bHelp)


    def languageChange(self):
        self.setCaption(self.__tr("DComm"))
        self.TWChoix.changeTab(self.Valeur_Parametre,self.__tr("Commentaire"))
        self.buttonGroup1.setTitle(self.__tr("Affichage"))
        self.RBGroupe.setText(self.__tr("par groupe"))
        self.RBalpha.setText(self.__trUtf8("\x61\x6c\x70\x68\x61\x62\xc3\xa9\x74\x69\x71\x75\x65"))
        self.textLabel1_4.setText(self.__tr("<b><u>Commandes :</u></b>"))
        self.textLabel4.setText(self.__trUtf8("\x4c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x68\x6f\x69\x73\x69\x65\x20\x73\x65\x72\x61\x20\x61\x6a\x6f\x75\x74\xc3\xa9\x65\x20\x41\x50\x52\x45\x53\x20\x6c\x61\x20\x63\x6f\x6d\x6d\x61\x6e\x64\x65\x20\x63\x6f\x75\x72\x61\x6e\x74\x65"))
        self.BNext.setText(self.__tr("Suivant"))
        QToolTip.add(self.BNext,self.__tr("affiche la prochaine occurence"))
        self.textLabel6.setText(self.__tr("Filtre"))
        self.TWChoix.changeTab(self.Commande,self.__tr("Nouvelle Commande"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(QKeySequence(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A")))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(QKeySequence(self.__tr("Alt+S")))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(QKeySequence(self.__tr("Alt+D")))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))
        self.Commentaire.setText(QString.null)


    def LBNouvCommandeClicked(self):
        print "DComment.LBNouvCommandeClicked(): Not implemented yet"

    def LEFiltreTextChanged(self):
        print "DComment.LEFiltreTextChanged(): Not implemented yet"

    def LEfiltreReturnPressed(self):
        print "DComment.LEfiltreReturnPressed(): Not implemented yet"

    def BSupPressed(self):
        print "DComment.BSupPressed(): Not implemented yet"

    def LENomConceptReturnPressed(self):
        print "DComment.LENomConceptReturnPressed(): Not implemented yet"

    def BOkPressed(self):
        print "DComment.BOkPressed(): Not implemented yet"

    def BuildTabCommand(self):
        print "DComment.BuildTabCommand(): Not implemented yet"

    def ViewDoc(self):
        print "DComment.ViewDoc(): Not implemented yet"

    def BNextPressed(self):
        print "DComment.BNextPressed(): Not implemented yet"

    def textCommentaireChanged(self):
        print "DComment.textCommentaireChanged(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DComment",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DComment",s,c,QApplication.UnicodeUTF8)
