# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OptionsEditeur.ui'
#
# Created: Tue Jun 10 18:23:53 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.16
#
# WARNING! All changes made in this file will be lost!


from qt import *


class desOptions(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("desOptions")



        self.groupBox1 = QGroupBox(self,"groupBox1")
        self.groupBox1.setGeometry(QRect(11,11,548,191))

        self.textLabel1_3 = QLabel(self.groupBox1,"textLabel1_3")
        self.textLabel1_3.setGeometry(QRect(30,60,280,20))

        self.textLabel1_2_2 = QLabel(self.groupBox1,"textLabel1_2_2")
        self.textLabel1_2_2.setGeometry(QRect(30,120,280,20))

        self.CBVersions = QComboBox(0,self.groupBox1,"CBVersions")
        self.CBVersions.setGeometry(QRect(30,20,90,30))

        self.LERepMat = QLineEdit(self.groupBox1,"LERepMat")
        self.LERepMat.setGeometry(QRect(30,140,501,31))

        self.LERepCata = QLineEdit(self.groupBox1,"LERepCata")
        self.LERepCata.setGeometry(QRect(30,80,501,31))

        self.Bok = QPushButton(self.groupBox1,"Bok")
        self.Bok.setGeometry(QRect(440,20,90,31))
        self.Bok.setAutoDefault(0)

        self.groupBox2 = QGroupBox(self,"groupBox2")
        self.groupBox2.setGeometry(QRect(11,208,548,90))

        self.LEVersionAjout = QLineEdit(self.groupBox2,"LEVersionAjout")
        self.LEVersionAjout.setGeometry(QRect(120,31,101,30))

        self.LEVersionSup = QLineEdit(self.groupBox2,"LEVersionSup")
        self.LEVersionSup.setGeometry(QRect(410,30,101,30))

        self.PBSup = QPushButton(self.groupBox2,"PBSup")
        self.PBSup.setGeometry(QRect(300,20,101,41))

        self.PBajout = QPushButton(self.groupBox2,"PBajout")
        self.PBajout.setGeometry(QRect(10,20,101,41))

        self.PBQuit = QPushButton(self,"PBQuit")
        self.PBQuit.setGeometry(QRect(400,420,151,31))
        self.PBQuit.setMinimumSize(QSize(0,30))

        self.groupBox3 = QGroupBox(self,"groupBox3")
        self.groupBox3.setGeometry(QRect(10,310,548,90))

        self.LERepDoc = QLineEdit(self.groupBox3,"LERepDoc")
        self.LERepDoc.setGeometry(QRect(20,50,520,31))

        self.textLabel1 = QLabel(self.groupBox3,"textLabel1")
        self.textLabel1.setGeometry(QRect(20,20,280,30))

        self.Bdefaut = QCheckBox(self,"Bdefaut")
        self.Bdefaut.setGeometry(QRect(10,430,340,20))
        Bdefaut_font = QFont(self.Bdefaut.font())
        Bdefaut_font.setPointSize(12)
        self.Bdefaut.setFont(Bdefaut_font)

        self.languageChange()

        self.resize(QSize(570,474).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.CBVersions,SIGNAL("activated(int)"),self.VersionChoisie)
        self.connect(self.Bdefaut,SIGNAL("clicked()"),self.BdefautChecked)
        self.connect(self.LEVersionAjout,SIGNAL("returnPressed()"),self.AjoutVersion)
        self.connect(self.LERepDoc,SIGNAL("returnPressed()"),self.ChangePathDoc)
        self.connect(self.Bok,SIGNAL("clicked()"),self.BokClicked)
        self.connect(self.LEVersionSup,SIGNAL("returnPressed()"),self.SupVersion)
        self.connect(self.PBajout,SIGNAL("clicked()"),self.AjoutVersion)
        self.connect(self.PBSup,SIGNAL("clicked()"),self.SupVersion)
        self.connect(self.PBQuit,SIGNAL("clicked()"),self.close)
        self.connect(self.LERepDoc,SIGNAL("textChanged(const QString&)"),self.ChangePathDoc)


    def languageChange(self):
        self.setCaption(self.__tr("Options Aster"))
        self.groupBox1.setTitle(self.__tr("Configurer une Version"))
        self.textLabel1_3.setText(self.__trUtf8("\x52\xc3\xa9\x70\x65\x72\x74\x6f\x69\x72\x65\x20\x64\x27\x61\x63\x63\xc3\xa8\x73\x20\x61\x75\x20\x63\x61\x74\x61\x6c\x6f\x67\x75\x65\x20\x3a"))
        self.textLabel1_2_2.setText(self.__trUtf8("\x52\xc3\xa9\x70\x65\x72\x74\x6f\x69\x72\x65\x20\x64\x27\x61\x63\x63\xc3\xa8\x73\x20\x61\x75\x78\x20\x6d\x61\x74\xc3\xa9\x72\x69\x61\x75\x78\x20\x3a"))
        self.LERepMat.setText(QString.null)
        self.LERepCata.setText(QString.null)
        self.Bok.setText(self.__tr("Valider"))
        self.groupBox2.setTitle(self.__trUtf8("\x47\xc3\xa9\x72\x65\x72\x20\x6c\x65\x73\x20\x76\x65\x72\x73\x69\x6f\x6e\x73"))
        self.PBSup.setText(self.__tr("Supprimer\n"
"Version :"))
        self.PBajout.setText(self.__tr("Ajouter\n"
"Version :"))
        self.PBQuit.setText(self.__tr("Quitter"))
        self.groupBox3.setTitle(self.__tr("Doc"))
        self.LERepDoc.setText(QString.null)
        self.textLabel1.setText(self.__trUtf8("\x52\x65\x70\x65\x72\x74\x6f\x69\x72\x65\x20\x64\x27\x61\x63\x63\x65\x73\x20\xc3\xa0\x20\x6c\x61\x20\x64\x6f\x63\x75\x6d\x65\x6e\x74\x61\x74\x69\x6f\x6e\x20\x3a"))
        self.Bdefaut.setText(self.__tr("Reinitialiser avec les valeurs par defaut"))


    def VersionChoisie(self):
        print "desOptions.VersionChoisie(): Not implemented yet"

    def BdefautChecked(self):
        print "desOptions.BdefautChecked(): Not implemented yet"

    def AjoutVersion(self):
        print "desOptions.AjoutVersion(): Not implemented yet"

    def SupVersion(self):
        print "desOptions.SupVersion(): Not implemented yet"

    def ChangePathDoc(self):
        print "desOptions.ChangePathDoc(): Not implemented yet"

    def BokClicked(self):
        print "desOptions.BokClicked(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("desOptions",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("desOptions",s,c,QApplication.UnicodeUTF8)
