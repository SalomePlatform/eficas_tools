# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueSDCO.ui'
#
# Created: ven avr 4 11:27:09 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DUnSDCO(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DUnSDCO")

        self.setMinimumSize(QSize(350,0))

        DUnSDCOLayout = QGridLayout(self,1,1,11,6,"DUnSDCOLayout")

        self.tabuniqueinto = QTabWidget(self,"tabuniqueinto")

        self.Widget8 = QWidget(self.tabuniqueinto,"Widget8")
        Widget8Layout = QGridLayout(self.Widget8,1,1,11,6,"Widget8Layout")

        self.bSup = QPushButton(self.Widget8,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)

        Widget8Layout.addWidget(self.bSup,4,0)

        self.bOk = QPushButton(self.Widget8,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        Widget8Layout.addWidget(self.bOk,4,1)

        self.bHelp = QPushButton(self.Widget8,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)

        Widget8Layout.addWidget(self.bHelp,4,2)

        self.Commentaire = QLabel(self.Widget8,"Commentaire")
        self.Commentaire.setMinimumSize(QSize(311,30))

        Widget8Layout.addMultiCellWidget(self.Commentaire,3,3,0,2)

        self.textLabel2_2 = QLabel(self.Widget8,"textLabel2_2")

        Widget8Layout.addMultiCellWidget(self.textLabel2_2,0,0,0,2)

        self.LESDCO = QLineEdit(self.Widget8,"LESDCO")
        self.LESDCO.setMinimumSize(QSize(300,40))

        Widget8Layout.addMultiCellWidget(self.LESDCO,1,1,0,2)

        self.textLabel2 = QLabel(self.Widget8,"textLabel2")

        Widget8Layout.addMultiCellWidget(self.textLabel2,2,2,0,2)
        self.tabuniqueinto.insertTab(self.Widget8,QString(""))

        DUnSDCOLayout.addWidget(self.tabuniqueinto,0,0)

        self.languageChange()

        self.resize(QSize(461,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)
        self.connect(self.LESDCO,SIGNAL("returnPressed()"),self.LESDCOReturnPressed)

        self.setTabOrder(self.LESDCO,self.tabuniqueinto)
        self.setTabOrder(self.tabuniqueinto,self.bSup)
        self.setTabOrder(self.bSup,self.bOk)
        self.setTabOrder(self.bOk,self.bHelp)


    def languageChange(self):
        self.setCaption(self.__tr("DUnIn"))
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
        self.textLabel2_2.setText(self.__tr("<h1><font size=\"+2\">Nom du nouveau concept : </font></h1>"))
        self.textLabel2.setText(self.__tr("<font size=\"+1\">Un objet de type CO est attendu</font>"))
        self.tabuniqueinto.changeTab(self.Widget8,self.__tr("Saisir Valeur"))


    def BSupPressed(self):
        print "DUnSDCO.BSupPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DUnSDCO.ViewDoc(): Not implemented yet"

    def BOkPressed(self):
        print "DUnSDCO.BOkPressed(): Not implemented yet"

    def LESDCOReturnPressed(self):
        print "DUnSDCO.LESDCOReturnPressed(): Not implemented yet"

    def BOuiPressed(self):
        print "DUnSDCO.BOuiPressed(): Not implemented yet"

    def BNonPressed(self):
        print "DUnSDCO.BNonPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DUnSDCO",s,c)
