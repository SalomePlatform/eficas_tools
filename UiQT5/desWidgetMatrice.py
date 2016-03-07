# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desWidgetMatrice.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_desWidgetMatrice(object):
    def setupUi(self, desWidgetMatrice):
        desWidgetMatrice.setObjectName("desWidgetMatrice")
        desWidgetMatrice.resize(802, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(desWidgetMatrice)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.RBValide = MonBoutonValide(desWidgetMatrice)
        self.RBValide.setMinimumSize(QtCore.QSize(21, 25))
        self.RBValide.setMaximumSize(QtCore.QSize(21, 25))
        self.RBValide.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.RBValide.setStyleSheet("border : 0px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../home/A96028/GitEficasTravail/eficas/Editeur/icons/ast-green-ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RBValide.setIcon(icon)
        self.RBValide.setIconSize(QtCore.QSize(25, 25))
        self.RBValide.setObjectName("RBValide")
        self.horizontalLayout_2.addWidget(self.RBValide)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.PBrefresh = QtWidgets.QPushButton(desWidgetMatrice)
        self.PBrefresh.setText("")
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.PBrefresh.setIcon(icon)
        self.PBrefresh.setObjectName("PBrefresh")
        self.verticalLayout_2.addWidget(self.PBrefresh)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label = MonLabelClic(desWidgetMatrice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(300, 25))
        self.label.setMaximumSize(QtCore.QSize(178, 16777215))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.TBMatrice = QtWidgets.QTableWidget(desWidgetMatrice)
        self.TBMatrice.setObjectName("TBMatrice")
        self.TBMatrice.setColumnCount(0)
        self.TBMatrice.setRowCount(0)
        self.horizontalLayout.addWidget(self.TBMatrice)

        self.retranslateUi(desWidgetMatrice)
        QtCore.QMetaObject.connectSlotsByName(desWidgetMatrice)

    def retranslateUi(self, desWidgetMatrice):
        _translate = QtCore.QCoreApplication.translate
        desWidgetMatrice.setWindowTitle(_translate("desWidgetMatrice", "Dialog"))
        self.RBValide.setToolTip(_translate("desWidgetMatrice", "Affiche le rapport de validation du mot-clef"))
        self.RBValide.setText(_translate("desWidgetMatrice", "..."))
        self.PBrefresh.setToolTip(_translate("desWidgetMatrice", "<html><head/><body><p>Met à jour l\'en-tête</p></body></html>"))
        self.label.setText(_translate("desWidgetMatrice", "<html><head/><body><p>aaa</p><p>dqsklmdqm</p></body></html>"))

from monBoutonValide import MonBoutonValide
from monLabelClic import MonLabelClic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desWidgetMatrice = QtWidgets.QDialog()
    ui = Ui_desWidgetMatrice()
    ui.setupUi(desWidgetMatrice)
    desWidgetMatrice.show()
    sys.exit(app.exec_())

