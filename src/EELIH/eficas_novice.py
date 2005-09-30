# -*- coding: iso-8859-1 -*-

# modules de base
import sys
# modules PyQt
from qt import *
# modules IHM
from mainwindow import *
from appli import *

if __name__ == '__main__':
   a = QApplication(sys.argv)
   appli = Appli()
   a.connect(a, SIGNAL('lastWindowClosed()'), a, SLOT('quit()'))
   a.exec_loop()
