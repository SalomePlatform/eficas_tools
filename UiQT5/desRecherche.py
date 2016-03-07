# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desRecherche.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_desRecherche(object):
    def setupUi(self, desRecherche):
        desRecherche.setObjectName("desRecherche")
        desRecherche.resize(525, 55)
        self.LERecherche = QtWidgets.QLineEdit(desRecherche)
        self.LERecherche.setGeometry(QtCore.QRect(0, 10, 411, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LERecherche.sizePolicy().hasHeightForWidth())
        self.LERecherche.setSizePolicy(sizePolicy)
        self.LERecherche.setStyleSheet("background:rgb(240,240,240)")
        self.LERecherche.setObjectName("LERecherche")
        self.PBSuivant = QtWidgets.QPushButton(desRecherche)
        self.PBSuivant.setEnabled(True)
        self.PBSuivant.setGeometry(QtCore.QRect(420, 10, 101, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBSuivant.sizePolicy().hasHeightForWidth())
        self.PBSuivant.setSizePolicy(sizePolicy)
        self.PBSuivant.setStyleSheet("background-color:rgb(104,110,149);\n"
"color :white;\n"
"border-radius : 12px\n"
"")
        self.PBSuivant.setAutoDefault(False)
        self.PBSuivant.setDefault(True)
        self.PBSuivant.setObjectName("PBSuivant")

        self.retranslateUi(desRecherche)
        QtCore.QMetaObject.connectSlotsByName(desRecherche)

    def retranslateUi(self, desRecherche):
        _translate = QtCore.QCoreApplication.translate
        desRecherche.setWindowTitle(_translate("desRecherche", "Rechercher dans le JDC"))
        desRecherche.setToolTip(_translate("desRecherche", "Next"))
        self.PBSuivant.setText(_translate("desRecherche", "Suivant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desRecherche = QtWidgets.QWidget()
    ui = Ui_desRecherche()
    ui.setupUi(desRecherche)
    desRecherche.show()
    sys.exit(app.exec_())

