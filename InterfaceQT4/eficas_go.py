#!/usr/bin/env python
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
from __future__ import absolute_import
from __future__ import print_function
try :
   from builtins import str
except : pass

from PyQt5.QtWidgets import QApplication

import sys,os
repIni=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),".."))
ihmQTDir=os.path.join(repIni,"UiQT5")
editeurDir=os.path.join(repIni,"Editeur")
ihmDir=os.path.join(repIni,"InterfaceQT4")

if ihmDir not in sys.path : sys.path.append(ihmDir)
if ihmQTDir not in sys.path : sys.path.append(ihmQTDir)
if editeurDir not in sys.path :sys.path.append(editeurDir)


def lance_eficas(code=None,fichier=None,ssCode=None,multi=False,langue='en'):
    """
        Lance l'appli EFICAS
    """
    # Analyse des arguments de la ligne de commande
    from Editeur  import session
    options=session.parse(sys.argv)
    if options.code!= None : code=options.code
    if options.ssCode!= None : ssCode=options.ssCode

    from InterfaceQT4.qtEficas import Appli
    app = QApplication(sys.argv)
    Eficas=Appli(code=code,salome=0,ssCode=ssCode,multi=multi,langue=langue)
    Eficas.show()

    res=app.exec_()
    sys.exit(res)


def lance_eficas_ssIhm(code=None,fichier=None,ssCode=None,version=None,debug=False,langue='en'):
    """
        Lance l'appli EFICAS pour trouver les noms des groupes
    """
    # Analyse des arguments de la ligne de commande
    from Editeur  import session
    options=session.parse(sys.argv)
    if version!=None and options.cata==None : options.cata=version
    if fichier==None : fichier=options.comm[0]
    if code == None : code=options.code

    from .qtEficas import Appli
    Eficas=Appli(code=code,salome=0,ssCode=ssCode,ssIhm=True,langue=langue)

    from .ssIhm  import QWParentSSIhm
    parent=QWParentSSIhm(code,Eficas,version)

    from . import readercata
    if not hasattr ( Eficas, 'readercata'):
           monreadercata  = readercata.READERCATA( parent, Eficas )
           Eficas.readercata=monreadercata

    from .editor import JDCEditor
    monEditeur=JDCEditor(Eficas,fichier)
    return monEditeur

def lance_eficas_ssIhm_cherche_Groupes(code=None,fichier=None,ssCode=None,version=None):
    monEditeur=lance_eficas_ssIhm(code,fichier,ssCode,version)
    print((monEditeur.cherche_Groupes()))

def lance_eficas_ssIhm_cherche_cr(code=None,fichier=None,ssCode=None,version=None):
    monEditeur=lance_eficas_ssIhm(code,fichier,ssCode,version)
    print((monEditeur.jdc.cr))

def lance_eficas_ssIhm_reecrit(code=None,fichier=None,ssCode=None,version=None,ou=None,cr=False,debug=False,leger=False,langue='ang'):
    #print 'lance_eficas_ssIhm_reecrit', fichier
    monEditeur=lance_eficas_ssIhm(code,fichier,ssCode,version,langue=langue)
    if ou == None : 
       fileName=fichier.split(".")[0]+"_reecrit.comm"
       fn=fichier.split(".")[0]+"_cr.txt"
    else :
       f=fichier.split(".")[0]+"_reecrit.comm"
       f1=os.path.basename(f)
       fn=fichier.split(".")[0]+"_cr.txt"
       f2=os.path.basename(fn)
       fileName=os.path.join(ou,f1)
       fileCr=os.path.join(ou,f2)
    debut=False
    if debug :
         import cProfile, pstats, StringIO
         pr = cProfile.Profile()
         pr.enable()
         monEditeur.saveFileAs(fileName=fileName)
         pr.disable()
         s = StringIO.StringIO()
         sortby = 'cumulative'
         ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
         ps.print_stats()
         print (s.getvalue())

    elif not leger : monEditeur.saveFileAs(fileName=fileName)
    else : monEditeur.saveFileLegerAs(fileName=fileName)
    if cr:
       f = open(fileCr, 'w')
       f.write(str(monEditeur.jdc.report()))
       f.close()

def lance_eficas_param(code='Adao',fichier=None,version='V0',macro='ASSIMILATION_STUDY'):
    """
        Lance l'appli EFICAS pour trouver les noms des groupes
    """
    # Analyse des arguments de la ligne de commande
    from Editeur  import session
    options=session.parse(sys.argv)

    from .qtEficas import Appli
    app = QApplication(sys.argv)
    Eficas=Appli(code=code,ssCode=None)

    from .ssIhm  import QWParentSSIhm
    parent=QWParentSSIhm(code,Eficas,version)

    from . import readercata
    if not hasattr ( Eficas, 'readercata'):
           monreadercata  = readercata.READERCATA( parent, Eficas )
           Eficas.readercata=monreadercata

    from .editor import JDCEditor
    monEditeur=JDCEditor(Eficas,fichier)
    texte=loadJDC(fichier)
    parameters=getJdcParameters(texte,macro)
    return parameters

def getJdcParameters(jdc,macro):
    """
    This function converts the data from the specified macro of the
    specified jdc text to a python dictionnary whose keys are the
    names of the data of the macro.
    """
    context = {}
    source = "def args_to_dict(**kwargs): return kwargs \n"
    source+= "%s = _F = args_to_dict          \n"%macro
    source+= "parameters="+jdc+"                        \n"
    source+= "context['parameters'] = parameters         \n"
    code = compile(source, 'file.py', 'exec')
    eval(code)
    parameters = context['parameters']
    return parameters

def loadJDC(filename):
    """
    This function loads the text from the specified JdC file. A JdC
    file is the persistence file of Eficas (*.comm).
    """
    fcomm=open(filename,'r')
    jdc = ""
    for line in fcomm.readlines():
        if not (line[0]=='#'):
           jdc+="%s"%line

    # Warning, we have to make sure that the jdc comes as a simple
    # string without any extra spaces/newlines
    return jdc.strip()

if __name__ == "__main__":
    import sys
    sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))
    lance_eficas(code=None,fichier=None,ssCode=None,multi=True)
    

