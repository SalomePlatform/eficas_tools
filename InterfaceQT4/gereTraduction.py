# Copyright (C) 2007-2012   EDF R&D
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
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os


def traduction(directPath,editor,version):
    if version == "V7V8" : 
       from Traducteur import traduitV7V8 
       suffixe="v8.comm"
    if version == "V8V9" : 
       from Traducteur import traduitV8V9 
       suffixe="v9.comm"
    if version == "V9V10" : 
       from Traducteur import traduitV9V10 
       suffixe="v10.comm"
    fn = QFileDialog.getOpenFileName( 
   			editor.appliEficas,
                        editor.appliEficas.trUtf8('Traduire Fichier'),
			QString(directPath) ,
                        editor.appliEficas.trUtf8('JDC Files (*.comm);;''All Files (*)'))

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

    qApp.setOverrideCursor(QCursor(Qt.WaitCursor))
    if version == "V7V8" : traduitV7V8.traduc(FichieraTraduire,FichierTraduit,log)
    if version == "V8V9" : traduitV8V9.traduc(FichieraTraduire,FichierTraduit,log)
    if version == "V9V10" : traduitV9V10.traduc(FichieraTraduire,FichierTraduit,log)
    qApp.setOverrideCursor(QCursor(Qt.ArrowCursor))

    Entete="Fichier Traduit : "+FichierTraduit +"\n\n"
    if  os.stat(log)[6] != 0L :
        f=open(log)
        texte= f.read()
        f.close()
    else :
       texte = Entete  
       commande="diff "+FichieraTraduire+" "+FichierTraduit+" >/dev/null"
       try :
         if os.system(commande) == 0 :
            texte = texte + "Pas de difference entre le fichier origine et le fichier traduit"
       except :
         pass

    from monVisu import DVisu
    titre = "conversion de "+ FichieraTraduire
    monVisuDialg=DVisu(parent=editor.appliEficas,fl=0)
    monVisuDialg.setWindowTitle(titre)
    monVisuDialg.TB.setText(texte)
    monVisuDialg.show()

