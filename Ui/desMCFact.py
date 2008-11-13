# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desMCFact.ui'
#
# Created: mar mar 25 10:05:08 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DMCFact(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DMCFact")

        self.setMinimumSize(QSize(505,0))

        DMCFactLayout = QGridLayout(self,1,1,11,6,"DMCFactLayout")

        self.TWChoix = QTabWidget(self,"TWChoix")

        self.MotClef = QWidget(self.TWChoix,"MotClef")
        MotClefLayout = QGridLayout(self.MotClef,1,1,11,6,"MotClefLayout")

        self.textLabel1 = QLabel(self.MotClef,"textLabel1")
        self.textLabel1.setMinimumSize(QSize(0,0))

        MotClefLayout.addWidget(self.textLabel1,0,0)

        self.LBMCPermis = QListBox(self.MotClef,"LBMCPermis")
        self.LBMCPermis.setMinimumSize(QSize(0,0))

        MotClefLayout.addWidget(self.LBMCPermis,1,0)

        self.LBRegles = QListBox(self.MotClef,"LBRegles")

        MotClefLayout.addWidget(self.LBRegles,1,1)

        self.textLabel1_2 = QLabel(self.MotClef,"textLabel1_2")

        MotClefLayout.addWidget(self.textLabel1_2,0,1)
        self.TWChoix.insertTab(self.MotClef,QString(""))

        DMCFactLayout.addMultiCellWidget(self.TWChoix,0,0,0,2)

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setAutoDefault(1)

        DMCFactLayout.addWidget(self.bSup,2,0)

        self.Commentaire = QLabel(self,"Commentaire")

        DMCFactLayout.addMultiCellWidget(self.Commentaire,1,1,0,2)

        self.bHelp = QPushButton(self,"bHelp")
        self.bHelp.setAutoDefault(1)

        DMCFactLayout.addWidget(self.bHelp,2,2)

        self.bOk = QPushButton(self,"bOk")
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        DMCFactLayout.addWidget(self.bOk,2,1)

        self.languageChange()

        self.resize(QSize(511,499).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bSup,SIGNAL("pressed()"),self.BSupPressed)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)


    def languageChange(self):
        self.setCaption(self.__tr("DMacro"))
        self.textLabel1.setText(self.__tr("<h3><p align=\"center\"><u><b>Mots Clefs Permis</b></u></p></h3>"))
        self.textLabel1_2.setText(self.__trUtf8("\x3c\x68\x33\x3e\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x63\x65\x6e\x74\x65\x72\x22\x3e\x3c\x75\x3e\x3c\x62\x3e\x52\xc3\xa9\x67\x6c\x65\x73\x3c\x2f\x62\x3e\x3c\x2f\x75\x3e\x3c\x2f\x70\x3e\x3c\x2f\x68\x33\x3e"))
        self.TWChoix.changeTab(self.MotClef,self.__tr("Ajouter Mot-Clef"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.Commentaire.setText(QString.null)
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(self.__tr("Alt+D"))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A"))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))


    def ViewDoc(self):
        print "DMCFact.ViewDoc(): Not implemented yet"

    def BSupPressed(self):
        print "DMCFact.BSupPressed(): Not implemented yet"

    def BOkPressed(self):
        print "DMCFact.BOkPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DMCFact",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DMCFact",s,c,QApplication.UnicodeUTF8)
