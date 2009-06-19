# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OptionsPdf.ui'
#
# Created: Tue Jan 27 12:25:38 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_desPdf(object):
    def setupUi(self, desPdf):
        desPdf.setObjectName("desPdf")
        desPdf.resize(538, 142)
        self.textLabel1_2 = QtGui.QLabel(desPdf)
        self.textLabel1_2.setGeometry(QtCore.QRect(20, 10, 280, 20))
        self.textLabel1_2.setWordWrap(False)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.BCancel = QtGui.QPushButton(desPdf)
        self.BCancel.setGeometry(QtCore.QRect(450, 90, 70, 31))
        self.BCancel.setObjectName("BCancel")
        self.LERepPdf = QtGui.QLineEdit(desPdf)
        self.LERepPdf.setGeometry(QtCore.QRect(20, 40, 501, 31))
        self.LERepPdf.setObjectName("LERepPdf")
        self.Bok = QtGui.QPushButton(desPdf)
        self.Bok.setGeometry(QtCore.QRect(350, 90, 70, 31))
        self.Bok.setObjectName("Bok")

        self.retranslateUi(desPdf)
        desPdf.setTabOrder(self.LERepPdf, self.Bok)
        desPdf.setTabOrder(self.Bok, self.BCancel)

    def retranslateUi(self, desPdf):
        desPdf.setWindowTitle(QtGui.QApplication.translate("desPdf", "desPdf", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1_2.setText(QtGui.QApplication.translate("desPdf", "Lecteur Pdf", None, QtGui.QApplication.UnicodeUTF8))
        self.BCancel.setText(QtGui.QApplication.translate("desPdf", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.LERepPdf.setText(QtGui.QApplication.translate("desPdf", "acroread", None, QtGui.QApplication.UnicodeUTF8))
        self.Bok.setText(QtGui.QApplication.translate("desPdf", "Ok", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    desPdf = QtGui.QDialog()
    ui = Ui_desPdf()
    ui.setupUi(desPdf)
    desPdf.show()
    sys.exit(app.exec_())

