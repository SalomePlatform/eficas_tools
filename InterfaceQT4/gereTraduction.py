# Copyright (C) 2007-2021   EDF R&D
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
from __future__ import absolute_import
try :
   from builtins import str
except : pass

from PyQt5.QtWidgets import  QFileDialog, QApplication

import os
from Extensions.i18n import tr


def traduction(directPath,editor,version):
    if version == "V9V10" : 
       from Traducteur import traduitV9V10 
       suffixe="v10.comm"
    if version == "V10V11" :
       from Traducteur import traduitV10V11
       suffixe="v11.comm"
    if version == "V11V12" :
       from Traducteur import traduitV11V12
       suffixe="v12.comm"

    fn = QFileDialog.getOpenFileName( 
   			editor.appliEficas,
                        tr('Traduire Fichier'),
			directPath ,
                        tr('Fichiers JDC  (*.comm);;''Tous les Fichiers (*)'))


    fn=fn[0]
    FichieraTraduire=str(fn)
    if (FichieraTraduire == "" or FichieraTraduire == () ) : return
    i=FichieraTraduire.rfind(".")
    Feuille=FichieraTraduire[0:i]
    FichierTraduit=Feuille+suffixe

    i=Feuille.rfind("/")
    directLog=Feuille[0:i]
    log=directLog+"/convert.log"
    os.system("rm -rf "+log)
    os.system("rm -rf "+FichierTraduit)

    QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
    if version == "V9V10" : traduitV9V10.traduc(FichieraTraduire,FichierTraduit,log)
    if version == "V10V11" : traduitV10V11.traduc(FichieraTraduire,FichierTraduit,log)
    if version == "V11V12" : traduitV11V12.traduc(FichieraTraduire,FichierTraduit,log)
    QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))

    Entete=tr("Fichier Traduit : %s\n\n",str(FichierTraduit))
    if  os.stat(log)[6] != 0 :
        f=open(log)
        texte= f.read()
        f.close()
    else :
       texte = Entete  
       commande="diff "+FichieraTraduire+" "+FichierTraduit+" >/dev/null"
       try :
         if os.system(commande) == 0 :
            texte = texte + tr("Pas de difference entre le fichier origine et le fichier traduit")
       except :
         pass

    from .monVisu import DVisu
    titre = "conversion de "+ FichieraTraduire
    monVisuDialg=DVisu(parent=editor.appliEficas,fl=0)
    monVisuDialg.setWindowTitle(titre)
    monVisuDialg.TB.setText(texte)
    monVisuDialg.show()

