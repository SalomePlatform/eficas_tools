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

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'../InterfaceQT4'))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'../UiQT4'))
from Extensions.i18n import tr
from string import split,strip,lowercase,uppercase
import re,string

import xml.etree.ElementTree as ET
from xml.dom import minidom

from PyQt4.QtGui import *

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'iso-8859-1')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

                
class CatalogueXML:
        def __init__(self,cata,cataName):
                self.fichier="/tmp/XML/"+cataName+".xml"
                self.cata=cata
                self.first=ET.Element('cata')
                comment=ET.Comment("catalogue "+str(cataName))
                self.first.append(comment)
                self.reglesUtilisees=[]
                self.validatorsUtilises=[]
                self.constr_list_txt_cmd()
                self.ecrire_fichier()


        def ecrire_fichier(self):
                try :
                   import codecs
		   f = codecs.open(self.fichier, "w", "ISO-8859-1")
                   f.write(prettify(self.first))
                   f.close()
                except :
                   print ("Impossible d'ecrire le fichier : "+ str(self.fichier))

        def constr_list_txt_cmd(self):
                mesCommandes=self.cata.JdC.commandes
                self.commandes=ET.SubElement(self.first,'commandes')
                for maCommande in mesCommandes:
                    maCommande.enregistreXML(self.commandes,self)


if __name__ == "__main__" :
	#monCata="/local/noyret/Install_Eficas/MAP/mapcata.py"
        code="SPECA"
        version=None

        from Editeur  import session
        options=session.parse(sys.argv)
        if options.code!= None :    code=options.code
        if options.cata!= None : monCata=options.cata
        if options.ssCode!= None :  ssCode=options.ssCode

        sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..',code))

        from InterfaceQT4.ssIhm  import QWParentSSIhm, appliEficasSSIhm
        Eficas=appliEficasSSIhm(code=code)
        parent=QWParentSSIhm(code,Eficas,version)

        import readercata
        monreadercata  = readercata.READERCATA( parent, parent )
        Eficas.readercata=monreadercata
        monCata=monreadercata.cata[0]

        monCataXML=CatalogueXML(monCata,code)



