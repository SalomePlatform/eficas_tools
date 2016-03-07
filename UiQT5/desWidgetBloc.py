# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetBloc.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetBloc(object):
    def setupUi(self, WidgetBloc):
        WidgetBloc.setObjectName("WidgetBloc")
        WidgetBloc.resize(1033, 25)
        WidgetBloc.setStyleSheet(" QGroupBox {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 1ex; /* leave space at the top for the title */\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     padding: 0 3px;\n"
" }")
        self.verticalLayout = QtWidgets.QVBoxLayout(WidgetBloc)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.commandesLayout = QtWidgets.QVBoxLayout()
        self.commandesLayout.setContentsMargins(-1, 5, -1, -1)
        self.commandesLayout.setSpacing(0)
        self.commandesLayout.setObjectName("commandesLayout")
        self.verticalLayout.addLayout(self.commandesLayout)

        self.retranslateUi(WidgetBloc)
        QtCore.QMetaObject.connectSlotsByName(WidgetBloc)

    def retranslateUi(self, WidgetBloc):
        _translate = QtCore.QCoreApplication.translate
        WidgetBloc.setWindowTitle(_translate("WidgetBloc", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetBloc = QtWidgets.QWidget()
    ui = Ui_WidgetBloc()
    ui.setupUi(WidgetBloc)
    WidgetBloc.show()
    sys.exit(app.exec_())

