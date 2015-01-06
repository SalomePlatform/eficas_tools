# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desDoc.ui'
#
# Created: Tue Nov 19 18:52:47 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_desGraphique(object):
    def setupUi(self, desGraphique):
        desGraphique.setObjectName(_fromUtf8("desGraphique"))
        desGraphique.resize(566, 575)
        self.label = QtGui.QLabel(desGraphique)
        self.label.setGeometry(QtCore.QRect(0, 0, 571, 571))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../monCode/docMonCode2.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.PB_layer_2_height = QtGui.QPushButton(desGraphique)
        self.PB_layer_2_height.setGeometry(QtCore.QRect(370, 80, 201, 32))
        self.PB_layer_2_height.setObjectName(_fromUtf8("PB_layer_2_height"))
        self.PB_layer_1_height = QtGui.QRadioButton(desGraphique)
        self.PB_layer_1_height.setGeometry(QtCore.QRect(200, 70, 21, 29))
        self.PB_layer_1_height.setText(_fromUtf8(""))
        self.PB_layer_1_height.setObjectName(_fromUtf8("PB_layer_1_height"))

        self.retranslateUi(desGraphique)
        QtCore.QMetaObject.connectSlotsByName(desGraphique)

    def retranslateUi(self, desGraphique):
        desGraphique.setWindowTitle(_translate("desGraphique", "Form", None))
        self.PB_layer_2_height.setText(_translate("desGraphique", "layer_2_height", None))
        self.PB_layer_1_height.setToolTip(_translate("desGraphique", "layer_1_height", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    desGraphique = QtGui.QWidget()
    ui = Ui_desGraphique()
    ui.setupUi(desGraphique)
    desGraphique.show()
    sys.exit(app.exec_())

