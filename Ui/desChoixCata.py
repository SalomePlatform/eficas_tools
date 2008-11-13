# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desChoixCata.ui'
#
# Created: mar mar 25 10:05:07 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DChoixCata(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("DChoixCata")

        self.setSizeGripEnabled(1)

        DChoixCataLayout = QGridLayout(self,1,1,11,6,"DChoixCataLayout")

        self.frame3 = QFrame(self,"frame3")
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Raised)

        self.buttonCancel = QPushButton(self.frame3,"buttonCancel")
        self.buttonCancel.setGeometry(QRect(380,6,90,30))
        self.buttonCancel.setAutoDefault(1)

        self.buttonOk = QPushButton(self.frame3,"buttonOk")
        self.buttonOk.setGeometry(QRect(40,6,90,30))
        self.buttonOk.setAutoDefault(1)
        self.buttonOk.setDefault(1)

        DChoixCataLayout.addMultiCellWidget(self.frame3,2,2,0,1)

        self.TLNb = QLabel(self,"TLNb")
        self.TLNb.setMinimumSize(QSize(30,0))

        DChoixCataLayout.addWidget(self.TLNb,0,0)

        self.CBChoixCata = QComboBox(0,self,"CBChoixCata")
        self.CBChoixCata.setEnabled(1)

        DChoixCataLayout.addWidget(self.CBChoixCata,1,1)

        self.textLabel1_2 = QLabel(self,"textLabel1_2")
        self.textLabel1_2.setMinimumSize(QSize(380,60))

        DChoixCataLayout.addWidget(self.textLabel1_2,1,0)

        self.languageChange()

        self.resize(QSize(547,172).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.buttonOk,SIGNAL("clicked()"),self.BOkPressed)
        self.connect(self.buttonCancel,SIGNAL("clicked()"),self.BCancelPressed)
        self.connect(self.CBChoixCata,SIGNAL("activated(const QString&)"),self.CataChoisi)


    def languageChange(self):
        self.setCaption(self.__tr("Choix d'une version du code Aster"))
        self.buttonCancel.setText(self.__tr("&Cancel"))
        self.buttonCancel.setAccel(QString.null)
        self.buttonOk.setText(self.__tr("&OK"))
        self.buttonOk.setAccel(QString.null)
        self.TLNb.setText(self.__tr("2"))
        self.textLabel1_2.setText(self.__tr("<font size=\"+1\">Veuillez choisir celle avec laquelle vous souhaitez travailler</font>"))


    def CataChoisi(self):
        print "DChoixCata.CataChoisi(): Not implemented yet"

    def BOkPressed(self):
        print "DChoixCata.BOkPressed(): Not implemented yet"

    def BCancelPressed(self):
        print "DChoixCata.BCancelPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DChoixCata",s,c)
