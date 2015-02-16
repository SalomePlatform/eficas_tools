# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
# Modules Python
import string,types,os
import traceback

from Extensions.i18n import tr
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from desViewTexte import Ui_dView

# ------------------------------- #
class ViewText(Ui_dView,QDialog):
# ------------------------------- #
    """
    Classe permettant la visualisation de texte
    """
    def __init__(self,parent,editor=None,entete=None,texte=None,largeur=600,hauteur=600):
        QDialog.__init__(self,parent)
        self.editor=editor
        self.setupUi(self)

        self.resize( QSize(largeur,hauteur).expandedTo(self.minimumSizeHint()) )
        self.connect( self.bclose,SIGNAL("clicked()"), self, SLOT("close()") )
        self.connect( self.bsave,SIGNAL("clicked()"), self.saveFile )
        if entete != None : self.setWindowTitle (entete)
        if entete != None : self.setText (texte)

        
    def setText(self, txt ):    
        self.view.setText(txt)
        
    def saveFile(self):
        #recuperation du nom du fichier
        if self.editor != None :
           dir=self.editor.appliEficas.CONFIGURATION.savedir
        else:
           dir='/tmp'
        fn = QFileDialog.getSaveFileName(None,
                tr("Sauvegarder le fichier"),
                dir)
        if fn.isNull() : return
        ulfile = os.path.abspath(unicode(fn))
        if self.editor != None :
           self.editor.appliEficas.CONFIGURATION.savedir=os.path.split(ulfile)[0]
        try:
           f = open(fn, 'wb')
           f.write(str(self.view.toPlainText()))
           f.close()
           return 1
        except IOError, why:
           QMessageBox.critical(self, tr("Sauvegarder le fichier"),
                tr("Le fichier <b>%(v_1)s</b> n'a pu etre sauvegarde. <br>Raison : %(v_2)s", {'v_1': unicode(fn), 'v_2': unicode(why)}))
           return

