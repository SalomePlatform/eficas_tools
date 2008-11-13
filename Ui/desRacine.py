# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desRacine.ui'
#
# Created: Mon Jun 2 16:02:17 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.16
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DRac(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DRac")

        self.setMinimumSize(QSize(505,0))

        DRacLayout = QGridLayout(self,1,1,11,6,"DRacLayout")

        self.textLabel1_4 = QLabel(self,"textLabel1_4")
        self.textLabel1_4.setMinimumSize(QSize(291,21))

        DRacLayout.addMultiCellWidget(self.textLabel1_4,0,0,0,1)

        self.textLabel1_4_2 = QLabel(self,"textLabel1_4_2")

        DRacLayout.addMultiCellWidget(self.textLabel1_4_2,0,1,2,3)

        self.buttonGroup1 = QButtonGroup(self,"buttonGroup1")
        self.buttonGroup1.setMinimumSize(QSize(0,60))

        self.RBGroupe = QRadioButton(self.buttonGroup1,"RBGroupe")
        self.RBGroupe.setGeometry(QRect(10,20,90,20))

        self.RBalpha = QRadioButton(self.buttonGroup1,"RBalpha")
        self.RBalpha.setGeometry(QRect(110,20,120,20))
        self.RBalpha.setChecked(1)

        DRacLayout.addMultiCellWidget(self.buttonGroup1,1,1,0,1)

        self.bHelp = QPushButton(self,"bHelp")
        self.bHelp.setMinimumSize(QSize(160,30))
        self.bHelp.setAutoDefault(1)

        DRacLayout.addWidget(self.bHelp,3,3)

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setMinimumSize(QSize(160,30))
        self.bSup.setAutoDefault(1)

        DRacLayout.addWidget(self.bSup,3,0)

        self.bOk = QPushButton(self,"bOk")
        self.bOk.setMinimumSize(QSize(160,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        DRacLayout.addMultiCellWidget(self.bOk,3,3,1,2)

        layout2 = QGridLayout(None,1,1,0,6,"layout2")

        self.BNext = QToolButton(self,"BNext")
        self.BNext.setMinimumSize(QSize(60,30))
        self.BNext.setIconSet(QIconSet())

        layout2.addWidget(self.BNext,0,2)

        self.LEFiltre = QLineEdit(self,"LEFiltre")
        self.LEFiltre.setMinimumSize(QSize(0,30))

        layout2.addWidget(self.LEFiltre,0,1)

        self.LBRegles = QListBox(self,"LBRegles")
        self.LBRegles.setMinimumSize(QSize(240,350))

        layout2.addMultiCellWidget(self.LBRegles,0,1,3,3)

        self.textLabel6 = QLabel(self,"textLabel6")
        self.textLabel6.setMinimumSize(QSize(40,0))

        layout2.addWidget(self.textLabel6,0,0)

        self.LBNouvCommande = QListBox(self,"LBNouvCommande")

        layout2.addMultiCellWidget(self.LBNouvCommande,1,1,0,2)

        DRacLayout.addMultiCellLayout(layout2,2,2,0,3)

        self.languageChange()

        self.resize(QSize(509,513).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.LBNouvCommande,SIGNAL("doubleClicked(QListBoxItem*)"),self.LBNouvCommandeClicked)
        self.connect(self.LEFiltre,SIGNAL("textChanged(const QString&)"),self.LEFiltreTextChanged)
        self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.LEfiltreReturnPressed)
        self.connect(self.bSup,SIGNAL("pressed()"),self.BSupPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.RBalpha,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.RBGroupe,SIGNAL("clicked()"),self.BuildTabCommand)
        self.connect(self.BNext,SIGNAL("clicked()"),self.BNextPressed)
        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)

        self.setTabOrder(self.LEFiltre,self.LBNouvCommande)
        self.setTabOrder(self.LBNouvCommande,self.RBalpha)
        self.setTabOrder(self.RBalpha,self.bSup)
        self.setTabOrder(self.bSup,self.bOk)
        self.setTabOrder(self.bOk,self.bHelp)
        self.setTabOrder(self.bHelp,self.LBRegles)


    def languageChange(self):
        self.setCaption(self.__tr("DMacro"))
        self.textLabel1_4.setText(self.__tr("<b><u>Commandes :</u></b>"))
        self.textLabel1_4_2.setText(self.__trUtf8("\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x63\x65\x6e\x74\x65\x72\x22\x3e\x3c\x62\x3e\x3c\x75\x3e\x52\xc3\xa9\x67\x6c\x65\x73\x20\x3a\x3c\x2f\x75\x3e\x3c\x2f\x62\x3e\x3c\x2f\x70\x3e"))
        self.buttonGroup1.setTitle(self.__tr("Affichage"))
        self.RBGroupe.setText(self.__tr("par groupe"))
        self.RBalpha.setText(self.__trUtf8("\x61\x6c\x70\x68\x61\x62\xc3\xa9\x74\x69\x71\x75\x65"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(QKeySequence(self.__tr("Alt+D")))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(QKeySequence(self.__tr("Alt+S")))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(QKeySequence(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A")))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.BNext.setText(self.__tr("Suivant"))
        QToolTip.add(self.BNext,self.__tr("affiche la prochaine occurence"))
        self.textLabel6.setText(self.__tr("Filtre"))


    def LBNouvCommandeClicked(self):
        print "DRac.LBNouvCommandeClicked(): Not implemented yet"

    def LEFiltreTextChanged(self):
        print "DRac.LEFiltreTextChanged(): Not implemented yet"

    def LEfiltreReturnPressed(self):
        print "DRac.LEfiltreReturnPressed(): Not implemented yet"

    def BSupPressed(self):
        print "DRac.BSupPressed(): Not implemented yet"

    def BOkPressed(self):
        print "DRac.BOkPressed(): Not implemented yet"

    def BuildTabCommand(self):
        print "DRac.BuildTabCommand(): Not implemented yet"

    def BNextPressed(self):
        print "DRac.BNextPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DRac.ViewDoc(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DRac",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DRac",s,c,QApplication.UnicodeUTF8)
