# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desVisu.ui'
#
# Created: mar mar 25 10:05:09 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DVisu(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DVisu")


        DVisuLayout = QGridLayout(self,1,1,11,6,"DVisuLayout")

        self.TB = QTextBrowser(self,"TB")

        DVisuLayout.addWidget(self.TB,0,0)

        self.languageChange()

        self.resize(QSize(501,394).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Visualisation Include Materiau"))


    def __tr(self,s,c = None):
        return qApp.translate("DVisu",s,c)
