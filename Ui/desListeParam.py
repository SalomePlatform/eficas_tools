# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desListeParam.ui'
#
# Created: mar mar 25 10:05:08 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DLisParam(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DLisParam")


        DLisParamLayout = QGridLayout(self,1,1,11,6,"DLisParamLayout")

        self.LBParam = QListBox(self,"LBParam")

        DLisParamLayout.addWidget(self.LBParam,0,0)

        self.languageChange()

        self.resize(QSize(413,394).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.LBParam,SIGNAL("clicked(QListBoxItem*)"),self.LBParamItemPressed)


    def languageChange(self):
        self.setCaption(self.__trUtf8("\x53\xc3\xa9\x6c\x65\x63\x74\x69\x6f\x6e\x20\x64\x65\x20\x70\x61\x72\x61\x6d\xc3\xa9\x74\x72\x65\x73"))


    def LBParamItemPressed(self):
        print "DLisParam.LBParamItemPressed(): Not implemented yet"

    def __trUtf8(self,s,c = None):
        return qApp.translate("DLisParam",s,c,QApplication.UnicodeUTF8)
