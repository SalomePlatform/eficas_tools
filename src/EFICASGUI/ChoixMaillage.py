# Form implementation generated from reading ui file 'ChoixMaillage.ui'
#
# Created: Tue Jan 25 11:28:46 2005
#      by: The PyQt User Interface Compiler (pyuic)
#
# WARNING! All changes made in this file will be lost!


from qt import *
Extracting Python code from ChoixMaillage.ui.h


class ChoixMaillage(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if name == None:
            self.setName("ChoixMaillage")

        self.resize(526,252)
        self.setCaption(self.trUtf8("Choix du Maillage sur lequel s appliquent les condtions aux limites"))


        self.TextLabel1 = QLabel(self,"TextLabel1")
        self.TextLabel1.setGeometry(QRect(10,190,191,40))
        self.TextLabel1.setText(self.trUtf8("Nom du nouveau maillage"))

        self.TextLabel2 = QLabel(self,"TextLabel2")
        self.TextLabel2.setGeometry(QRect(20,70,181,31))
        self.TextLabel2.setText(self.trUtf8("Maillage sélectionné"))

        self.Maillage = QListBox(self,"Maillage")
        self.Maillage.setGeometry(QRect(210,70,281,90))

        self.TextLabel1_2 = QLabel(self,"TextLabel1_2")
        self.TextLabel1_2.setGeometry(QRect(20,10,120,20))
        self.TextLabel1_2.setText(self.trUtf8("Géométrie traitée :"))

        self.NomShape = QLabel(self,"NomShape")
        self.NomShape.setGeometry(QRect(140,10,191,21))
        self.NomShape.setText(self.trUtf8("TextLabel2"))

        self.NouveauMesh = QLineEdit(self,"NouveauMesh")
        self.NouveauMesh.setGeometry(QRect(210,200,280,24))

        self.connect(self.Maillage,SIGNAL("clicked(QListBoxItem*)"),self.Maillage_clicked)
        self.connect(self.NouveauMesh,SIGNAL("returnPressed()"),self.NouveauMesh_returnPressed)

    def Maillage_clicked(self,a0):
        print "ChoixMaillage.Maillage_clicked(QListBoxItem*): Not implemented yet"

    def NouveauMesh_returnPressed(self):
        print "ChoixMaillage.NouveauMesh_returnPressed(): Not implemented yet"
