# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desPlusieursInto.ui'
#
# Created: ven avr 4 11:27:09 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x21\x00\x00\x00\x0e" \
    "\x08\x06\x00\x00\x00\xa1\x1e\x75\x8c\x00\x00\x00" \
    "\xcf\x49\x44\x41\x54\x38\x8d\xd5\x94\xdb\x0e\xc3" \
    "\x20\x0c\x43\xed\xfd\xf8\xd8\x97\xbb\x0f\x34\x5b" \
    "\x48\x08\x45\xd5\x1e\xb6\x48\x88\xf4\x12\xe7\x60" \
    "\x01\xc0\x0f\x04\x6f\xd6\xe9\x9b\xba\x77\x20\x04" \
    "\x80\x92\x4a\x10\x32\xc9\x2e\xfb\xd8\xc7\xd5\xca" \
    "\xbc\xc0\x25\x40\x00\x99\xe9\x57\x84\x95\x68\xfe" \
    "\x7f\x06\xc0\xde\xd1\xde\xb3\x2b\x4a\x1e\xc4\xea" \
    "\x82\x4b\x9e\x74\x09\x71\x65\xbd\x01\xf8\x55\x27" \
    "\xf7\x8a\x72\x01\xe0\xa3\x12\x9f\x34\x5a\x01\x7c" \
    "\x54\x3b\xaf\xdc\x98\x3d\x0f\x71\x09\xd1\x5a\x33" \
    "\x1b\x47\x1f\x47\x07\x2c\x17\x49\x4a\x82\x33\x8f" \
    "\x61\x78\x20\x3a\x88\x17\xe6\x73\x06\xb1\xf0\x8b" \
    "\x07\xba\x03\xe6\x02\xc9\xb8\x31\x07\x7e\x37\xe0" \
    "\x20\x9e\x67\xe3\x38\x67\x10\x97\x7b\x17\xde\x80" \
    "\xc1\x85\xad\x38\x69\x5a\x51\xd5\x22\xc8\x2c\xe7" \
    "\x79\x12\xe2\xfe\xd8\xbe\x83\x76\x20\x92\xf5\x2b" \
    "\x18\x20\xdd\x11\xbb\x10\xe5\x65\xb5\x3a\x5a\x3b" \
    "\xba\xff\x13\x07\x13\xd6\x6f\xa6\x98\x18\x57\x06" \
    "\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"
image1_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x21\x00\x00\x00\x0e" \
    "\x08\x06\x00\x00\x00\xa1\x1e\x75\x8c\x00\x00\x00" \
    "\xc7\x49\x44\x41\x54\x38\x8d\xcd\x94\x59\x0e\xc3" \
    "\x20\x0c\x44\x71\xd5\x7b\xc7\x3d\xf9\xf4\x07\xd3" \
    "\x31\xb1\x59\xa2\x28\xaa\x25\x44\x48\xbc\x3c\xc6" \
    "\x81\x52\xfe\xc0\xe4\x42\x0c\xee\xce\xb9\x12\xe0" \
    "\x8a\x02\x39\x83\x88\x48\xf5\xdf\x02\xc9\x9c\x11" \
    "\xf8\x60\x04\x30\x01\x19\x05\x4a\xe8\x68\xc5\x6a" \
    "\xc2\x06\xc0\x6b\x4b\x10\x91\x11\xc8\x02\x87\x4f" \
    "\x3a\x52\xa5\x87\x75\x71\x23\x89\x7e\x40\x39\xc4" \
    "\x6b\x50\xd8\x86\x5b\x07\xf5\x40\x0a\x45\x00\x53" \
    "\x33\x08\x93\xcf\x86\x74\xa3\x00\x28\xd4\x92\xde" \
    "\xef\x04\x62\x6b\x55\x9d\xfe\x48\xac\x84\x2b\x1a" \
    "\x6d\xaa\xe6\x85\x01\x55\x03\x3b\x99\xc5\x00\x9f" \
    "\x70\xce\xda\x11\x1a\xab\x41\x3b\x6f\x6a\x70\xd1" \
    "\x18\xe0\x08\xe6\xfd\x8b\xc5\x1d\x5d\x00\xa0\xf6" \
    "\x14\x55\x6d\x1f\xf9\xb9\xbe\x49\x52\xaa\xbc\x37" \
    "\x21\xf8\xf8\xb6\xf6\x24\xc5\x57\xef\x89\x47\xaf" \
    "\xed\xf4\x8c\x5e\x60\xb8\xdf\xbe\xb8\x1d\x6d\xab" \
    "\x9a\xff\x99\x27\x00\x00\x00\x00\x49\x45\x4e\x44" \
    "\xae\x42\x60\x82"

class DPlusInto(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        self.image1 = QPixmap()
        self.image1.loadFromData(image1_data,"PNG")
        if not name:
            self.setName("DPlusInto")

        self.setMinimumSize(QSize(350,0))

        DPlusIntoLayout = QGridLayout(self,1,1,11,6,"DPlusIntoLayout")

        self.tabuniqueinto = QTabWidget(self,"tabuniqueinto")

        self.Widget8 = QWidget(self.tabuniqueinto,"Widget8")
        Widget8Layout = QGridLayout(self.Widget8,1,1,11,6,"Widget8Layout")

        self.textLabel1 = QLabel(self.Widget8,"textLabel1")

        Widget8Layout.addMultiCellWidget(self.textLabel1,0,0,0,1)

        self.bSup = QPushButton(self.Widget8,"bSup")
        self.bSup.setMinimumSize(QSize(130,30))
        self.bSup.setAutoDefault(1)

        Widget8Layout.addWidget(self.bSup,3,0)

        self.bOk = QPushButton(self.Widget8,"bOk")
        self.bOk.setMinimumSize(QSize(130,30))
        self.bOk.setAutoDefault(1)
        self.bOk.setDefault(1)

        Widget8Layout.addMultiCellWidget(self.bOk,3,3,1,2)

        self.bHelp = QPushButton(self.Widget8,"bHelp")
        self.bHelp.setSizePolicy(QSizePolicy(1,0,150,0,self.bHelp.sizePolicy().hasHeightForWidth()))
        self.bHelp.setMinimumSize(QSize(130,30))
        self.bHelp.setAutoDefault(1)

        Widget8Layout.addWidget(self.bHelp,3,3)

        self.Commentaire = QLabel(self.Widget8,"Commentaire")
        self.Commentaire.setMinimumSize(QSize(0,40))

        Widget8Layout.addMultiCellWidget(self.Commentaire,2,2,0,3)

        layout8 = QHBoxLayout(None,0,6,"layout8")

        self.LBValeurs = QListBox(self.Widget8,"LBValeurs")
        layout8.addWidget(self.LBValeurs)

        layout5 = QVBoxLayout(None,0,6,"layout5")
        spacer2 = QSpacerItem(21,44,QSizePolicy.Minimum,QSizePolicy.Expanding)
        layout5.addItem(spacer2)

        layout2 = QVBoxLayout(None,0,6,"layout2")

        self.BSup1Val = QToolButton(self.Widget8,"BSup1Val")
        self.BSup1Val.setMinimumSize(QSize(40,31))
        self.BSup1Val.setMaximumSize(QSize(40,31))
        self.BSup1Val.setIconSet(QIconSet(self.image0))
        layout2.addWidget(self.BSup1Val)

        self.BAjout1Val = QToolButton(self.Widget8,"BAjout1Val")
        self.BAjout1Val.setMinimumSize(QSize(40,31))
        self.BAjout1Val.setMaximumSize(QSize(40,31))
        self.BAjout1Val.setIconSet(QIconSet(self.image1))
        layout2.addWidget(self.BAjout1Val)
        spacer3 = QSpacerItem(21,176,QSizePolicy.Minimum,QSizePolicy.Expanding)
        layout2.addItem(spacer3)
        layout5.addLayout(layout2)
        layout8.addLayout(layout5)

        self.listBoxVal = QListBox(self.Widget8,"listBoxVal")
        layout8.addWidget(self.listBoxVal)

        Widget8Layout.addMultiCellLayout(layout8,1,1,0,3)

        self.textLabel1_2 = QLabel(self.Widget8,"textLabel1_2")

        Widget8Layout.addMultiCellWidget(self.textLabel1_2,0,0,2,3)
        self.tabuniqueinto.insertTab(self.Widget8,QString(""))

        DPlusIntoLayout.addWidget(self.tabuniqueinto,0,0)

        self.languageChange()

        self.resize(QSize(482,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bHelp,SIGNAL("clicked()"),self.ViewDoc)
        self.connect(self.bOk,SIGNAL("clicked()"),self.BOkPourListePressed)
        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)
        self.connect(self.LBValeurs,SIGNAL("doubleClicked(QListBoxItem*)"),self.Sup1Valeur)
        self.connect(self.BAjout1Val,SIGNAL("clicked()"),self.Ajout1Valeur)
        self.connect(self.BSup1Val,SIGNAL("clicked()"),self.Sup1Valeur)

        self.setTabOrder(self.listBoxVal,self.tabuniqueinto)
        self.setTabOrder(self.tabuniqueinto,self.bSup)
        self.setTabOrder(self.bSup,self.bOk)
        self.setTabOrder(self.bOk,self.bHelp)
        self.setTabOrder(self.bHelp,self.LBValeurs)


    def languageChange(self):
        self.setCaption(self.__tr("DUnIn"))
        self.textLabel1.setText(self.__tr("<u><font size=\"+1\">Valeur(s) actuelle(s)</font></u>"))
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
        self.BSup1Val.setText(QString.null)
        QToolTip.add(self.BSup1Val,self.__tr("enleve l occurence selectionnee"))
        self.BAjout1Val.setText(QString.null)
        QToolTip.add(self.BAjout1Val,self.__trUtf8("\x61\x6a\x6f\x75\x74\x65\x20\x6c\x61\x20\x76\x61\x6c\x65\x75\x72\x20\x73\x61\x69\x73\x69\x65\x20\x73\x6f\x75\x73\x20\x6c\x20\x6f\x63\x63\x75\x72\x65\x6e\x63\x65\x20\x73\x65\x6c\x65\x63\x74\x69\x6f\x6e\x6e\xc3\xa9\x65\x20\x28\x65\x6e\x20\x66\x69\x6e\x20\x64\x65\x20\x6c\x69\x73\x74\x65\x20\x73\x69\x20\x69\x6c\x20\x6e\x20\x79\x20\x61\x20\x70\x61\x73\x20\x64\x65\x20\x73\x65\x6c\x65\x63\x74\x69\x6f\x6e\x29"))
        self.textLabel1_2.setText(self.__tr("<u><font size=\"+1\">Valeur(s) possibles(s)</font></u>"))
        self.tabuniqueinto.changeTab(self.Widget8,self.__tr("Saisir Valeur"))


    def BSupPressed(self):
        print "DPlusInto.BSupPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DPlusInto.ViewDoc(): Not implemented yet"

    def BOkPourListePressed(self):
        print "DPlusInto.BOkPourListePressed(): Not implemented yet"

    def Ajout1Valeur(self):
        print "DPlusInto.Ajout1Valeur(): Not implemented yet"

    def Sup1Valeur(self):
        print "DPlusInto.Sup1Valeur(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DPlusInto",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DPlusInto",s,c,QApplication.UnicodeUTF8)
