# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueASSD.ui'
#
# Created: mar mar 25 10:05:09 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DUnASSD(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DUnASSD")

        self.setMinimumSize(QSize(350,0))

        DUnASSDLayout = QGridLayout(self,1,1,11,6,"DUnASSDLayout")

        self.tabuniqueinto = QTabWidget(self,"tabuniqueinto")

        self.Widget8 = QWidget(self.tabuniqueinto,"Widget8")
        Widget8Layout = QGridLayout(self.Widget8,1,1,11,6,"Widget8Layout")

        self.textLabel2 = QLabel(self.Widget8,"textLabel2")
        self.textLabel2.setMinimumSize(QSize(436,50))

        Widget8Layout.addWidget(self.textLabel2,0,0)

        self.listBoxASSD = QListBox(self.Widget8,"listBoxASSD")

        Widget8Layout.addWidget(self.listBoxASSD,1,0)

        self.Commentaire = QLabel(self.Widget8,"Commentaire")
        self.Commentaire.setMinimumSize(QSize(380,30))

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
        self.tabuniqueinto.insertTab(self.Widget8,QString(""))

        DUnASSDLayout.addWidget(self.tabuniqueinto,0,0)

        self.languageChange()

        self.resize(QSize(482,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)


    def languageChange(self):
        self.setCaption(self.__tr("DUnIn"))
        self.textLabel2.setText(self.__trUtf8("\x3c\x66\x6f\x6e\x74\x20\x73\x69\x7a\x65\x3d\x22\x2b\x31\x22\x3e\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x63\x65\x6e\x74\x65\x72\x22\x3e\x53\x74\x72\x75\x63\x74\x75\x72\x65\x73\x20\x64\x65\x20\x64\x6f\x6e\x6e\xc3\xa9\x65\x73\x20\x64\x75\x20\x74\x79\x70\x65\x0a\x72\x65\x71\x75\x69\x73\x20\x70\x61\x72\x20\x6c\x27\x6f\x62\x6a\x65\x74\x20\x63\x6f\x75\x72\x61\x6e\x74\x20\x3a\x3c\x2f\x70\x3e\x3c\x2f\x66\x6f\x6e\x74\x3e"))
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
        self.tabuniqueinto.changeTab(self.Widget8,self.__tr("Saisir Valeur"))


    def BSupPressed(self):
        print "DUnASSD.BSupPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DUnASSD.ViewDoc(): Not implemented yet"

    def BOkPressed(self):
        print "DUnASSD.BOkPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DUnASSD",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DUnASSD",s,c,QApplication.UnicodeUTF8)
