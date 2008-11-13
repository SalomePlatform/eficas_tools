# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desError.ui'
#
# Created: mar mar 25 10:05:08 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class DError(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("DError")

        self.setMinimumSize(QSize(350,0))

        DErrorLayout = QGridLayout(self,1,1,11,6,"DErrorLayout")

        self.textLabel1_3 = QLabel(self,"textLabel1_3")

        DErrorLayout.addWidget(self.textLabel1_3,0,0)

        layout1 = QHBoxLayout(None,0,6,"layout1")
        spacer1_2 = QSpacerItem(171,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout1.addItem(spacer1_2)

        self.bSup = QPushButton(self,"bSup")
        self.bSup.setAutoDefault(1)
        layout1.addWidget(self.bSup)
        spacer1 = QSpacerItem(171,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout1.addItem(spacer1)

        DErrorLayout.addLayout(layout1,1,0)

        self.languageChange()

        self.resize(QSize(482,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.bSup,SIGNAL("clicked()"),self.BSupPressed)


    def languageChange(self):
        self.setCaption(self.__tr("DInactif"))
        self.textLabel1_3.setText(self.__trUtf8("\x3c\x66\x6f\x6e\x74\x20\x73\x69\x7a\x65\x3d\x22\x2b\x34\x22\x3e\x3c\x70\x20\x61\x6c\x69\x67\x6e\x3d\x22\x63\x65\x6e\x74\x65\x72\x22\x3e\x4c\x65\x20\x6e\x6f\x65\x75\x64\x20\x73\xc3\xa9\x6c\x65\x63\x74\x69\x6f\x6e\x6e\xc3\xa9\x20\x6e\x65\x20\x63\x6f\x72\x72\x65\x73\x70\x6f\x6e\x64\x20\x70\x61\x73\x20\xc3\xa0\x20\x75\x6e\x20\x6f\x62\x6a\x65\x74\x20\x61\x63\x74\x69\x66\x2e\x3c\x2f\x70\x3e\x3c\x2f\x66\x6f\x6e\x74\x3e"))
        self.bSup.setText(self.__tr("&Supprimer"))
        self.bSup.setAccel(self.__tr("Alt+S"))
        QToolTip.add(self.bSup,self.__tr("suppression du mot clef"))


    def BSupPressed(self):
        print "DError.BSupPressed(): Not implemented yet"

    def ViewDoc(self):
        print "DError.ViewDoc(): Not implemented yet"

    def BOkPressed(self):
        print "DError.BOkPressed(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("DError",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("DError",s,c,QApplication.UnicodeUTF8)
