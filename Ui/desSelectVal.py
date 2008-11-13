# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desSelectVal.ui'
#
# Created: mar mar 25 10:05:09 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DSelVal(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DSelVal")


        DSelValLayout = QGridLayout(self,1,1,11,6,"DSelValLayout")

        self.TBtext = QTextBrowser(self,"TBtext")

        DSelValLayout.addMultiCellWidget(self.TBtext,0,0,0,1)

        self.BGSeparateur = QButtonGroup(self,"BGSeparateur")
        self.BGSeparateur.setMinimumSize(QSize(180,100))

        LayoutWidget = QWidget(self.BGSeparateur,"layout1")
        LayoutWidget.setGeometry(QRect(17,20,150,74))
        layout1 = QGridLayout(LayoutWidget,1,1,11,6,"layout1")

        self.BpointVirgule = QRadioButton(LayoutWidget,"BpointVirgule")

        layout1.addWidget(self.BpointVirgule,2,0)

        self.Bespace = QRadioButton(LayoutWidget,"Bespace")
        self.Bespace.setChecked(1)

        layout1.addWidget(self.Bespace,0,0)

        self.Bvirgule = QRadioButton(LayoutWidget,"Bvirgule")

        layout1.addWidget(self.Bvirgule,1,0)

        DSelValLayout.addMultiCellWidget(self.BGSeparateur,1,2,0,0)

        self.BImportTout = QPushButton(self,"BImportTout")

        DSelValLayout.addWidget(self.BImportTout,2,1)

        self.BImportSel = QPushButton(self,"BImportSel")

        DSelValLayout.addWidget(self.BImportSel,1,1)

        self.languageChange()

        self.resize(QSize(413,497).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.BGSeparateur,SIGNAL("clicked(int)"),self.SeparateurSelect)
        self.connect(self.BImportSel,SIGNAL("clicked()"),self.BImportSelPressed)
        self.connect(self.BImportTout,SIGNAL("clicked()"),self.BImportToutPressed)


    def languageChange(self):
        self.setCaption(self.__trUtf8("\x53\xc3\xa9\x6c\x65\x63\x74\x69\x6f\x6e\x20\x64\x65\x20\x76\x61\x6c\x65\x75\x72\x73"))
        self.BGSeparateur.setTitle(self.__trUtf8("\x53\xc3\xa9\x70\x61\x72\x61\x74\x65\x75\x72"))
        self.BpointVirgule.setText(self.__tr("point-virgule"))
        self.Bespace.setText(self.__tr("espace"))
        self.Bvirgule.setText(self.__tr("virgule"))
        self.BImportTout.setText(self.__tr("Importer Tout"))
        self.BImportSel.setText(self.__tr("Ajouter Selection"))


    def SeparateurSelect(self):
        print "DSelVal.SeparateurSelect(): Not implemented yet"

    def BImportSelPressed(self):
        print "DSelVal.BImportSelPressed(): Not implemented yet"

    def BImportToutPressed(self):
        print "DSelVal.BImportToutPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DSelVal",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DSelVal",s,c,QApplication.UnicodeUTF8)
