# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueSDCOInto.ui'
#
# Created: ven avr 4 11:27:09 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DUnSDCOInto(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DUnSDCOInto")

        self.setMinimumSize(QSize(350,0))

        DUnSDCOIntoLayout = QGridLayout(self,1,1,11,6,"DUnSDCOIntoLayout")

        self.tabuniqueinto = QTabWidget(self,"tabuniqueinto")

        self.Widget8 = QWidget(self.tabuniqueinto,"Widget8")
        Widget8Layout = QGridLayout(self.Widget8,1,1,11,6,"Widget8Layout")

        self.textLabel2 = QLabel(self.Widget8,"textLabel2")

        Widget8Layout.addMultiCellWidget(self.textLabel2,0,0,0,2)

        self.LBSDCO = QListBox(self.Widget8,"LBSDCO")

        Widget8Layout.addMultiCellWidget(self.LBSDCO,1,1,0,2)

        self.textLabel2_3 = QLabel(self.Widget8,"textLabel2_3")

        Widget8Layout.addMultiCellWidget(self.textLabel2_3,5,5,0,2)

        self.Commentaire = QLabel(self.Widget8,"Commentaire")
        self.Commentaire.setMinimumSize(QSize(420,30))

        Widget8Layout.addMultiCellWidget(self.Commentaire,4,4,0,2)

        layout3 = QGridLayout(None,1,1,0,6,"layout3")

        Widget8Layout.addMultiCellLayout(layout3,2,2,0,2)

        layout6 = QHBoxLayout(None,0,6,"layout6")

        self.frame3 = QFrame(self.Widget8,"frame3")
        self.frame3.setMinimumSize(QSize(190,50))
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Raised)

        self.textLabel2_2 = QLabel(self.frame3,"textLabel2_2")
        self.textLabel2_2.setGeometry(QRect(20,10,150,30))
        layout6.addWidget(self.frame3)

        self.LESDCO = QLineEdit(self.Widget8,"LESDCO")
        self.LESDCO.setMinimumSize(QSize(220,40))
        layout6.addWidget(self.LESDCO)

        Widget8Layout.addMultiCellLayout(layout6,3,3,0,2)

        self.bSup = QPushButton(self.Widget8,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)

        Widget8Layout.addWidget(self.bSup,6,0)

        self.bOk = QPushButton(self.Widget8,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        Widget8Layout.addWidget(self.bOk,6,1)

        self.bHelp = QPushButton(self.Widget8,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)

        Widget8Layout.addWidget(self.bHelp,6,2)
        self.tabuniqueinto.insertTab(self.Widget8,QString(""))

        DUnSDCOIntoLayout.addWidget(self.tabuniqueinto,0,0)

        self.languageChange()

        self.resize(QSize(482,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)
        self.connect(self.LBSDCO,SIGNAL("clicked(QListBoxItem*)"),self.LBSDCOReturnPressed)
        self.connect(self.LESDCO,SIGNAL("returnPressed()"),self.LESDCOReturnPressed)

        self.setTabOrder(self.LESDCO,self.LBSDCO)
        self.setTabOrder(self.LBSDCO,self.tabuniqueinto)
        self.setTabOrder(self.tabuniqueinto,self.bSup)
        self.setTabOrder(self.bSup,self.bOk)
        self.setTabOrder(self.bOk,self.bHelp)


    def languageChange(self):
        self.setCaption(self.__tr("DUnIn"))
        self.textLabel2.setText(self.__trUtf8("\x3c\x66\x6f\x6e\x74\x20\x73\x69\x7a\x65\x3d\x22\x2b\x31\x22\x3e\x3c\x75\x3e\x53\x74\x72\x75\x63\x74\x75\x72\x65\x73\x20\x64\x65\x20\x64\x6f\x6e\x6e\xc3\xa9\x65\x73\x20\x64\x75\x20\x74\x79\x70\x65\x20\x72\x65\x71\x75\x69\x73\x20\x70\x61\x72\x20\x6c\x27\x6f\x62\x6a\x65\x74\x20\x63\x6f\x75\x72\x61\x6e\x74\x20\x3c\x2f\x75\x3e\x3c\x2f\x66\x6f\x6e\x74\x3e"))
        self.textLabel2_3.setText(self.__tr("<font size=\"+1\">Un objet de type CO est attendu</font>"))
        self.Commentaire.setText(QString.null)
        self.textLabel2_2.setText(self.__tr("<font size=\"+1\"> Nom concept : </font>"))
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
        print "DUnSDCOInto.BSupPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DUnSDCOInto.ViewDoc(): Not implemented yet"

    def BOkPressed(self):
        print "DUnSDCOInto.BOkPressed(): Not implemented yet"

    def LESDCOReturnPressed(self):
        print "DUnSDCOInto.LESDCOReturnPressed(): Not implemented yet"

    def BOuiPressed(self):
        print "DUnSDCOInto.BOuiPressed(): Not implemented yet"

    def BNonPressed(self):
        print "DUnSDCOInto.BNonPressed(): Not implemented yet"

    def LBSDCOReturnPressed(self):
        print "DUnSDCOInto.LBSDCOReturnPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DUnSDCOInto",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DUnSDCOInto",s,c,QApplication.UnicodeUTF8)
