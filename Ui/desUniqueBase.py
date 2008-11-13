# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueBase.ui'
#
# Created: ven avr 4 11:27:09 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x14\x00\x00\x00\x14" \
    "\x08\x06\x00\x00\x00\x8d\x89\x1d\x0d\x00\x00\x00" \
    "\x8d\x49\x44\x41\x54\x38\x8d\xb5\xd3\xdb\x0d\x80" \
    "\x20\x0c\x05\xd0\x5b\xe3\x3a\x8e\xe2\x4c\x86\x99" \
    "\x18\x85\x81\xea\x87\xc6\xc4\xd2\x56\x28\xd8\x84" \
    "\x0f\x5e\x27\x17\x50\x02\x63\x6a\x2d\x73\xb9\x1f" \
    "\xc0\xb5\x69\x15\x39\x17\xc3\xa0\x7e\xf0\xae\x9c" \
    "\xca\xab\xbf\x1f\x5b\xb5\xa6\xed\xc8\x0c\x02\x83" \
    "\x34\x20\x06\x02\x00\x81\x65\xc2\x38\x28\x30\x2f" \
    "\xa9\x77\xdd\x36\xc6\xa0\x67\xa7\x78\x14\x3f\xa1" \
    "\x85\xf9\x5b\xe6\x61\x76\xc2\x20\xa6\x83\x03\x58" \
    "\x0d\x0e\x62\x7a\xc2\x01\xcc\x04\xa3\xd8\x55\x2c" \
    "\x1a\xc0\x39\x95\xab\x27\xe7\x5a\x9a\x3e\x18\x47" \
    "\xdd\xef\x30\x72\xec\xef\x5f\xaf\xb3\x4e\xcb\x01" \
    "\x65\xf7\x82\x6b\x45\x7b\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"

class DUnBase(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        if not name:
            self.setName("DUnBase")

        self.setMinimumSize(QSize(350,0))

        DUnBaseLayout = QGridLayout(self,1,1,11,6,"DUnBaseLayout")

        self.tabuniqueinto = QTabWidget(self,"tabuniqueinto")

        self.Widget8 = QWidget(self.tabuniqueinto,"Widget8")
        Widget8Layout = QGridLayout(self.Widget8,1,1,11,6,"Widget8Layout")

        layout2 = QHBoxLayout(None,0,6,"layout2")

        self.textLabel2 = QLabel(self.Widget8,"textLabel2")
        layout2.addWidget(self.textLabel2)

        self.lineEditVal = QLineEdit(self.Widget8,"lineEditVal")
        self.lineEditVal.setMinimumSize(QSize(290,50))
        layout2.addWidget(self.lineEditVal)

        Widget8Layout.addMultiCellLayout(layout2,1,1,0,2)
        spacer1 = QSpacerItem(288,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        Widget8Layout.addMultiCell(spacer1,0,0,0,1)

        self.bParametres = QPushButton(self.Widget8,"bParametres")
        self.bParametres.setSizePolicy(QSizePolicy(0,0,0,0,self.bParametres.sizePolicy().hasHeightForWidth()))
        self.bParametres.setMinimumSize(QSize(140,30))

        Widget8Layout.addWidget(self.bParametres,0,2)

        self.bSup = QPushButton(self.Widget8,"bSup")
        self.bSup.setMinimumSize(QSize(0,30))
        self.bSup.setAutoDefault(1)

        Widget8Layout.addWidget(self.bSup,5,0)

        self.bOk = QPushButton(self.Widget8,"bOk")
        self.bOk.setMinimumSize(QSize(0,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        Widget8Layout.addWidget(self.bOk,5,1)

        self.bHelp = QPushButton(self.Widget8,"bHelp")
        self.bHelp.setMinimumSize(QSize(0,30))
        self.bHelp.setAutoDefault(1)

        Widget8Layout.addWidget(self.bHelp,5,2)
        spacer4 = QSpacerItem(41,112,QSizePolicy.Minimum,QSizePolicy.Expanding)
        Widget8Layout.addItem(spacer4,2,1)
        spacer3 = QSpacerItem(21,112,QSizePolicy.Minimum,QSizePolicy.Expanding)
        Widget8Layout.addItem(spacer3,4,1)

        self.Commentaire = QLabel(self.Widget8,"Commentaire")
        self.Commentaire.setMinimumSize(QSize(430,40))

        Widget8Layout.addMultiCellWidget(self.Commentaire,3,3,0,2)

        self.BView2D = QPushButton(self.Widget8,"BView2D")
        self.BView2D.setMinimumSize(QSize(110,40))

        Widget8Layout.addWidget(self.BView2D,2,2)

        self.BSalome = QPushButton(self.Widget8,"BSalome")
        self.BSalome.setMinimumSize(QSize(50,40))
        self.BSalome.setIconSet(QIconSet(self.image0))

        Widget8Layout.addWidget(self.BSalome,2,0)
        self.tabuniqueinto.insertTab(self.Widget8,QString(""))

        DUnBaseLayout.addWidget(self.tabuniqueinto,0,0)

        self.languageChange()

        self.resize(QSize(482,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOk2Pressed)
        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)
        self.connect(self.lineEditVal,SIGNAL("returnPressed()"),self.LEValeurPressed)
        self.connect(self.bParametres,SIGNAL("pressed()"),self.BParametresPressed)
        self.connect(self.BSalome,SIGNAL("pressed()"),self.BSalomePressed)
        self.connect(self.BView2D,SIGNAL("clicked()"),self.BView2DPressed)

        self.setTabOrder(self.lineEditVal,self.tabuniqueinto)
        self.setTabOrder(self.tabuniqueinto,self.bParametres)
        self.setTabOrder(self.bParametres,self.bSup)
        self.setTabOrder(self.bSup,self.bOk)
        self.setTabOrder(self.bOk,self.bHelp)
        self.setTabOrder(self.bHelp,self.BView2D)
        self.setTabOrder(self.BView2D,self.BSalome)


    def languageChange(self):
        self.setCaption(self.__tr("DUnIn"))
        self.textLabel2.setText(self.__tr("<b><u><p align=\"center\">Valeur: </p></u></b>"))
        self.bParametres.setText(self.__tr("Parametres"))
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
        self.BView2D.setText(self.__tr("Visualiser"))
        self.BSalome.setText(QString.null)
        self.tabuniqueinto.changeTab(self.Widget8,self.__tr("Saisir Valeur"))


    def BSupPressed(self):
        print "DUnBase.BSupPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DUnBase.ViewDoc(): Not implemented yet"

    def BOk2Pressed(self):
        print "DUnBase.BOk2Pressed(): Not implemented yet"

    def BParametresPressed(self):
        print "DUnBase.BParametresPressed(): Not implemented yet"

    def LEValeurPressed(self):
        print "DUnBase.LEValeurPressed(): Not implemented yet"

    def BSalomePressed(self):
        print "DUnBase.BSalomePressed(): Not implemented yet"

    def BView2DPressed(self):
        print "DUnBase.BView2DPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DUnBase",s,c)
