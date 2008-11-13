# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueInto.ui'
#
# Created: mar mar 25 10:05:09 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DUnIn(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DUnIn")

        self.setMinimumSize(QSize(350,0))

        DUnInLayout = QGridLayout(self,1,1,11,6,"DUnInLayout")

        self.tabuniqueinto = QTabWidget(self,"tabuniqueinto")

        self.Widget8 = QWidget(self.tabuniqueinto,"Widget8")
        Widget8Layout = QGridLayout(self.Widget8,1,1,11,6,"Widget8Layout")

        self.Commentaire = QLabel(self.Widget8,"Commentaire")
        self.Commentaire.setMinimumSize(QSize(420,30))

        Widget8Layout.addWidget(self.Commentaire,2,0)

        layout2 = QHBoxLayout(None,0,6,"layout2")

        self.bSup = QPushButton(self.Widget8,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)
        layout2.addWidget(self.bSup)

        self.bOk = QPushButton(self.Widget8,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)
        layout2.addWidget(self.bOk)

        self.bHelp = QPushButton(self.Widget8,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)
        layout2.addWidget(self.bHelp)

        Widget8Layout.addLayout(layout2,3,0)

        self.listBoxVal = QListBox(self.Widget8,"listBoxVal")

        Widget8Layout.addWidget(self.listBoxVal,1,0)

        self.textLabel2 = QLabel(self.Widget8,"textLabel2")

        Widget8Layout.addWidget(self.textLabel2,0,0)
        self.tabuniqueinto.insertTab(self.Widget8,QString(""))

        DUnInLayout.addWidget(self.tabuniqueinto,0,0)

        self.languageChange()

        self.resize(QSize(482,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)


    def languageChange(self):
        self.setCaption(self.__tr("DUnIn"))
        self.Commentaire.setText(QString.null)
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))
        self.bOk.setText(self.__tr("&Valider"))
        self.bOk.setAccel(self.__tr("Shift+A, Alt+A, Alt+A, Alt+A"))
        QToolTip.add(self.bOk,self.__tr("validation de la saisie"))
        self.bHelp.setText(self.__tr("&Documentation"))
        self.bHelp.setAccel(self.__tr("Alt+D"))
        QToolTip.add(self.bHelp,self.__tr("affichage documentation aster"))
        self.textLabel2.setText(self.__tr("<b><u><p align=\"center\">Valeurs possibles</p></u></b>"))
        self.tabuniqueinto.changeTab(self.Widget8,self.__tr("Saisir Valeur"))


    def BSupPressed(self):
        print "DUnIn.BSupPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DUnIn.ViewDoc(): Not implemented yet"

    def BOkPressed(self):
        print "DUnIn.BOkPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DUnIn",s,c)
