# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tuple2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tuple2(object):
    def setupUi(self, Tuple2):
        Tuple2.setObjectName("Tuple2")
        Tuple2.resize(482, 34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tuple2.sizePolicy().hasHeightForWidth())
        Tuple2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Tuple2)
        self.horizontalLayout.setContentsMargins(0, 1, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(Tuple2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEditVal_1 = LECustomTuple(Tuple2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVal_1.sizePolicy().hasHeightForWidth())
        self.lineEditVal_1.setSizePolicy(sizePolicy)
        self.lineEditVal_1.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEditVal_1.setMaximumSize(QtCore.QSize(805, 16777215))
        self.lineEditVal_1.setStyleSheet("background:rgb(235,235,235);\n"
"border:0px;\n"
"\n"
"")
        self.lineEditVal_1.setText("")
        self.lineEditVal_1.setReadOnly(False)
        self.lineEditVal_1.setObjectName("lineEditVal_1")
        self.horizontalLayout.addWidget(self.lineEditVal_1)
        self.label_6 = QtWidgets.QLabel(Tuple2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEditVal_2 = LECustomTuple(Tuple2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVal_2.sizePolicy().hasHeightForWidth())
        self.lineEditVal_2.setSizePolicy(sizePolicy)
        self.lineEditVal_2.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEditVal_2.setMaximumSize(QtCore.QSize(805, 16777215))
        self.lineEditVal_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEditVal_2.setStyleSheet("background:rgb(235,235,235);\n"
"border:0px;")
        self.lineEditVal_2.setObjectName("lineEditVal_2")
        self.horizontalLayout.addWidget(self.lineEditVal_2)
        self.label_7 = QtWidgets.QLabel(Tuple2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.retranslateUi(Tuple2)
        QtCore.QMetaObject.connectSlotsByName(Tuple2)

    def retranslateUi(self, Tuple2):
        _translate = QtCore.QCoreApplication.translate
        Tuple2.setWindowTitle(_translate("Tuple2", "Form"))
        self.label_5.setText(_translate("Tuple2", "<html><head/><body><p><span style=\" font-size:14pt;\">(</span></p></body></html>"))
        self.label_6.setText(_translate("Tuple2", "<html><head/><body><p><span style=\" font-size:14pt;\">,</span></p></body></html>"))
        self.label_7.setText(_translate("Tuple2", "<html><head/><body><p><span style=\" font-size:14pt;\">)</span></p></body></html>"))

from gereListe import LECustomTuple

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tuple2 = QtWidgets.QWidget()
    ui = Ui_Tuple2()
    ui.setupUi(Tuple2)
    Tuple2.show()
    sys.exit(app.exec_())

