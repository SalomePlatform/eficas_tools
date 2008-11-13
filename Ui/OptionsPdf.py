# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OptionsPdf.ui'
#
# Created: lun avr 7 09:36:07 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class desPdf(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("desPdf")



        self.textLabel1_2 = QLabel(self,"textLabel1_2")
        self.textLabel1_2.setGeometry(QRect(20,10,280,20))

        self.BCancel = QPushButton(self,"BCancel")
        self.BCancel.setGeometry(QRect(450,90,70,31))

        self.LERepPdf = QLineEdit(self,"LERepPdf")
        self.LERepPdf.setGeometry(QRect(20,40,501,31))

        self.Bok = QPushButton(self,"Bok")
        self.Bok.setGeometry(QRect(350,90,70,31))

        self.languageChange()

        self.resize(QSize(538,142).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.BCancel,SIGNAL("clicked()"),self.reject)
        self.connect(self.LERepPdf,SIGNAL("returnPressed()"),self.LeRepPdfPressed)
        self.connect(self.Bok,SIGNAL("clicked()"),self.BokClicked)

        self.setTabOrder(self.LERepPdf,self.Bok)
        self.setTabOrder(self.Bok,self.BCancel)


    def languageChange(self):
        self.setCaption(self.__tr("desPdf"))
        self.textLabel1_2.setText(self.__tr("Lecteur Pdf"))
        self.BCancel.setText(self.__tr("Cancel"))
        self.LERepPdf.setText(self.__tr("acroread"))
        self.Bok.setText(self.__tr("Ok"))


    def LeRepPdfPressed(self):
        print "desPdf.LeRepPdfPressed(): Not implemented yet"

    def BokClicked(self):
        print "desPdf.BokClicked(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("desPdf",s,c)
