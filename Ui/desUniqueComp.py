# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueComp.ui'
#
# Created: ven avr 4 11:27:09 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DUnComp(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DUnComp")

        self.setMinimumSize(QSize(350,0))

        DUnCompLayout = QGridLayout(self,1,1,11,6,"DUnCompLayout")

        self.tabuniqueinto = QTabWidget(self,"tabuniqueinto")

        self.Widget8 = QWidget(self.tabuniqueinto,"Widget8")
        Widget8Layout = QGridLayout(self.Widget8,1,1,11,6,"Widget8Layout")

        layout3 = QVBoxLayout(None,0,6,"layout3")

        self.textLabel1 = QLabel(self.Widget8,"textLabel1")
        layout3.addWidget(self.textLabel1)

        self.LEcomp = QLineEdit(self.Widget8,"LEcomp")
        self.LEcomp.setMinimumSize(QSize(390,40))
        layout3.addWidget(self.LEcomp)

        Widget8Layout.addMultiCellLayout(layout3,0,0,0,1)

        self.Commentaire = QLabel(self.Widget8,"Commentaire")

        Widget8Layout.addMultiCellWidget(self.Commentaire,5,5,0,1)

        self.LEReel = QLineEdit(self.Widget8,"LEReel")
        self.LEReel.setMinimumSize(QSize(190,40))

        Widget8Layout.addWidget(self.LEReel,3,0)

        self.LEImag = QLineEdit(self.Widget8,"LEImag")
        self.LEImag.setMinimumSize(QSize(190,40))

        Widget8Layout.addWidget(self.LEImag,3,1)

        self.buttonGroup1 = QButtonGroup(self.Widget8,"buttonGroup1")

        self.RBRI = QRadioButton(self.buttonGroup1,"RBRI")
        self.RBRI.setGeometry(QRect(20,40,335,20))

        self.RBMP = QRadioButton(self.buttonGroup1,"RBMP")
        self.RBMP.setGeometry(QRect(20,20,335,20))

        Widget8Layout.addMultiCellWidget(self.buttonGroup1,2,2,0,1)
        spacer3 = QSpacerItem(20,41,QSizePolicy.Minimum,QSizePolicy.Expanding)
        Widget8Layout.addItem(spacer3,1,0)
        spacer4 = QSpacerItem(20,41,QSizePolicy.Minimum,QSizePolicy.Expanding)
        Widget8Layout.addItem(spacer4,4,0)

        layout2 = QHBoxLayout(None,0,6,"layout2")

        self.bSup = QPushButton(self.Widget8,"bSup")
        self.bSup.setAutoDefault(1)
        layout2.addWidget(self.bSup)

        self.bOk = QPushButton(self.Widget8,"bOk")
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)
        layout2.addWidget(self.bOk)

        self.bHelp = QPushButton(self.Widget8,"bHelp")
        self.bHelp.setAutoDefault(1)
        layout2.addWidget(self.bHelp)

        Widget8Layout.addMultiCellLayout(layout2,6,6,0,1)
        self.tabuniqueinto.insertTab(self.Widget8,QString(""))

        DUnCompLayout.addWidget(self.tabuniqueinto,0,0)

        self.languageChange()

        self.resize(QSize(484,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)
        self.connect(self.LEImag,SIGNAL("returnPressed()"),self.LEImagRPressed)
        self.connect(self.LEReel,SIGNAL("returnPressed()"),self.LEReelRPressed)
        self.connect(self.LEcomp,SIGNAL("returnPressed()"),self.LEcompRPressed)

        self.setTabOrder(self.LEcomp,self.LEReel)
        self.setTabOrder(self.LEReel,self.LEImag)
        self.setTabOrder(self.LEImag,self.tabuniqueinto)
        self.setTabOrder(self.tabuniqueinto,self.RBRI)
        self.setTabOrder(self.RBRI,self.RBMP)
        self.setTabOrder(self.RBMP,self.bSup)
        self.setTabOrder(self.bSup,self.bOk)
        self.setTabOrder(self.bOk,self.bHelp)


    def languageChange(self):
        self.setCaption(self.__tr("DUnComp"))
        self.textLabel1.setText(self.__tr("<font size=\"+2\">Complexe de la forme : a+bj</font>"))
        self.Commentaire.setText(self.__tr("<font size=\"+2\">Un complexe est attendu</font>"))
        self.buttonGroup1.setTitle(self.__tr("OU"))
        self.RBRI.setText(self.__trUtf8("\x52\x49\x20\x20\x20\x3a\x20\x52\xc3\xa9\x65\x6c\x09\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x49\x6d\x61\x67\x69\x6e\x61\x69\x72\x65"))
        self.RBMP.setText(self.__tr("MP	: Module	                                         Phase"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A"))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(self.__tr("Alt+D"))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))
        self.tabuniqueinto.changeTab(self.Widget8,self.__tr("Saisir Valeur"))


    def BSupPressed(self):
        print "DUnComp.BSupPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DUnComp.ViewDoc(): Not implemented yet"

    def BOkPressed(self):
        print "DUnComp.BOkPressed(): Not implemented yet"

    def LEImagRPressed(self):
        print "DUnComp.LEImagRPressed(): Not implemented yet"

    def LEReelRPressed(self):
        print "DUnComp.LEReelRPressed(): Not implemented yet"

    def LEcompRPressed(self):
        print "DUnComp.LEcompRPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DUnComp",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DUnComp",s,c,QApplication.UnicodeUTF8)
