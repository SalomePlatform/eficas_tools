# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aideQT.ui'
#
# Created: mar mar 25 10:05:07 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class Aide(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("Aide")


        AideLayout = QGridLayout(self,1,1,11,6,"AideLayout")

        layout2 = QHBoxLayout(None,0,6,"layout2")

        self.PBIndex = QPushButton(self,"PBIndex")
        self.PBIndex.setMinimumSize(QSize(0,30))
        layout2.addWidget(self.PBIndex)

        self.PBBack = QPushButton(self,"PBBack")
        self.PBBack.setEnabled(1)
        self.PBBack.setMinimumSize(QSize(0,30))
        layout2.addWidget(self.PBBack)

        self.PBForward = QPushButton(self,"PBForward")
        self.PBForward.setEnabled(1)
        self.PBForward.setMinimumSize(QSize(0,30))
        layout2.addWidget(self.PBForward)

        AideLayout.addLayout(layout2,1,0)

        self.TB1 = QTextBrowser(self,"TB1")

        AideLayout.addMultiCellWidget(self.TB1,0,0,0,1)
        spacer1 = QSpacerItem(311,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        AideLayout.addItem(spacer1,1,1)

        self.languageChange()

        self.resize(QSize(602,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.PBBack,SIGNAL("clicked()"),self.TB1.backward)
        self.connect(self.PBForward,SIGNAL("clicked()"),self.TB1.forward)
        self.connect(self.PBIndex,SIGNAL("clicked()"),self.TB1.home)


    def languageChange(self):
        self.setCaption(self.__tr("Aide"))
        self.PBIndex.setText(self.__tr("Index"))
        self.PBBack.setText(self.__tr("Back"))
        self.PBForward.setText(self.__tr("Forward"))


    def PBIndexPushed(self):
        print "Aide.PBIndexPushed(): Not implemented yet"

    def PBBackPushed(self):
        print "Aide.PBBackPushed(): Not implemented yet"

    def PBForwardPushed(self):
        print "Aide.PBForwardPushed(): Not implemented yet"

    def SlotSourceChanged(self):
        print "Aide.SlotSourceChanged(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("Aide",s,c)
