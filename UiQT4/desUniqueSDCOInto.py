# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desUniqueSDCOInto.ui'
#
# Created: Fri Jun 19 11:40:13 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DUnSDCOInto(object):
    def setupUi(self, DUnSDCOInto):
        DUnSDCOInto.setObjectName("DUnSDCOInto")
        DUnSDCOInto.resize(482, 480)
        DUnSDCOInto.setMinimumSize(QtCore.QSize(350, 0))
        self.gridlayout = QtGui.QGridLayout(DUnSDCOInto)
        self.gridlayout.setObjectName("gridlayout")
        self.tabuniqueinto = QtGui.QTabWidget(DUnSDCOInto)
        self.tabuniqueinto.setObjectName("tabuniqueinto")
        self.Widget8 = QtGui.QWidget()
        self.Widget8.setObjectName("Widget8")
        self.gridlayout1 = QtGui.QGridLayout(self.Widget8)
        self.gridlayout1.setObjectName("gridlayout1")
        self.textLabel2 = QtGui.QLabel(self.Widget8)
        self.textLabel2.setWordWrap(False)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout1.addWidget(self.textLabel2, 0, 0, 1, 3)
        self.LBSDCO = QtGui.QListWidget(self.Widget8)
        self.LBSDCO.setObjectName("LBSDCO")
        self.gridlayout1.addWidget(self.LBSDCO, 1, 0, 1, 3)
        self.textLabel2_3 = QtGui.QLabel(self.Widget8)
        self.textLabel2_3.setWordWrap(False)
        self.textLabel2_3.setObjectName("textLabel2_3")
        self.gridlayout1.addWidget(self.textLabel2_3, 5, 0, 1, 3)
        self.Commentaire = QtGui.QLabel(self.Widget8)
        self.Commentaire.setMinimumSize(QtCore.QSize(420, 30))
        self.Commentaire.setWordWrap(False)
        self.Commentaire.setObjectName("Commentaire")
        self.gridlayout1.addWidget(self.Commentaire, 4, 0, 1, 3)
        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setObjectName("gridlayout2")
        self.gridlayout1.addLayout(self.gridlayout2, 2, 0, 1, 3)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.frame3 = QtGui.QFrame(self.Widget8)
        self.frame3.setMinimumSize(QtCore.QSize(190, 50))
        self.frame3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.textLabel2_2 = QtGui.QLabel(self.frame3)
        self.textLabel2_2.setGeometry(QtCore.QRect(20, 10, 150, 30))
        self.textLabel2_2.setWordWrap(False)
        self.textLabel2_2.setObjectName("textLabel2_2")
        self.hboxlayout.addWidget(self.frame3)
        self.LESDCO = QtGui.QLineEdit(self.Widget8)
        self.LESDCO.setMinimumSize(QtCore.QSize(220, 40))
        self.LESDCO.setObjectName("LESDCO")
        self.hboxlayout.addWidget(self.LESDCO)
        self.gridlayout1.addLayout(self.hboxlayout, 3, 0, 1, 3)
        self.bOk = QtGui.QPushButton(self.Widget8)
        self.bOk.setMinimumSize(QtCore.QSize(0, 30))
        self.bOk.setAutoDefault(True)
        self.bOk.setDefault(True)
        self.bOk.setObjectName("bOk")
        self.gridlayout1.addWidget(self.bOk, 6, 1, 1, 1)
        self.tabuniqueinto.addTab(self.Widget8, "")
        self.gridlayout.addWidget(self.tabuniqueinto, 0, 0, 1, 1)

        self.retranslateUi(DUnSDCOInto)
        QtCore.QMetaObject.connectSlotsByName(DUnSDCOInto)
        DUnSDCOInto.setTabOrder(self.LESDCO, self.LBSDCO)
        DUnSDCOInto.setTabOrder(self.LBSDCO, self.tabuniqueinto)
        DUnSDCOInto.setTabOrder(self.tabuniqueinto, self.bOk)

    def retranslateUi(self, DUnSDCOInto):
        DUnSDCOInto.setWindowTitle(QtGui.QApplication.translate("DUnSDCOInto", "DUnIn", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("DUnSDCOInto", "<font size=\"+1\"><u>Structures de données du type requis par l\'objet courant </u></font>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2_3.setText(QtGui.QApplication.translate("DUnSDCOInto", "<font size=\"+1\">Un objet de type CO est attendu</font>", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2_2.setText(QtGui.QApplication.translate("DUnSDCOInto", "<font size=\"+1\"> Nom concept : </font>", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setToolTip(QtGui.QApplication.translate("DUnSDCOInto", "validation de la saisie", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("DUnSDCOInto", "&Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setShortcut(QtGui.QApplication.translate("DUnSDCOInto", "Shift+A, Alt+A, Alt+A, Alt+A", None, QtGui.QApplication.UnicodeUTF8))
        self.tabuniqueinto.setTabText(self.tabuniqueinto.indexOf(self.Widget8), QtGui.QApplication.translate("DUnSDCOInto", "Saisir Valeur", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DUnSDCOInto = QtGui.QWidget()
    ui = Ui_DUnSDCOInto()
    ui.setupUi(DUnSDCOInto)
    DUnSDCOInto.show()
    sys.exit(app.exec_())

