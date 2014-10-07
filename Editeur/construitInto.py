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
listeCode=( "Aster" , "Adao" , "Carmel3D" , "CarmelCND" , "Openturns_Wrapper" , "Openturns_Study" , "MAP" , "MT" , "SPECA")

import sys,os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'../InterfaceQT4'))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)),'../UiQT4'))
from Extensions.i18n import tr
from string import split,strip,lowercase,uppercase
import re,string


class ChercheInto:
        def __init__(self,cata,cataName):
                self.cata=cata
                self.dictInto={}
                mesCommandes=self.cata.JdC.commandes
                for maCommande in mesCommandes:
                    self.construitListeInto(maCommande)
                #print self.dictInto


        def construitListeInto(self,e):
            if hasattr(e,'into') and e.into!=None:
               if len(e.into) in self.dictInto.keys():
                 self.dictInto[len(e.into)]+=1
               else :
                 self.dictInto[len(e.into)]=1
            for nomFils, fils in e.entites.items():
                self.construitListeInto(fils)

        def getDico(self):
            return self.dictInto

class CompteInto:
      def __init__ (self) :
        self.monDico={}
        self.monDico[2]=0
        self.monDico[10]=0
        self.monDico[30]=0
        self.monDico[60]=0
        self.monDico[61]=0
        self.tout=0.0

      def ajoutDico(self,dico) :
          for k in dico.keys():
              if k < 3 : self.monDico[2]+=dico[k]
              elif k < 11 : self.monDico[10]+=dico[k]
              elif k < 31 : self.monDico[30]+=dico[k]
              elif k < 61 : self.monDico[60]+=dico[k]
              else : self.monDico[61]+=dico[k]
              self.tout+=dico[k]

      def imprime(self):
          for l in 2,10,30,60,61:
              print l
              print self.monDico[l]
              print self.monDico[l]/self.tout 
              print "_______________________"
              

        
if __name__ == "__main__" :
	#monCata="/local/noyret/Install_Eficas/MAP/mapcata.py"
	#monCata="/local/noyret/Install_Eficas/Aster/Cata/cataSTA11/cata.py"
	#monCata="/local/noyret/Install_Eficas/MAP/mapcata.py"
	#monCata="/local/noyret/Install_Eficas/MAP/mapcata.py"



   cmpte=CompteInto()
   for code in listeCode:

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

        monConstruitInto=ChercheInto(monCata,code)
        dic=monConstruitInto.getDico()
        cmpte.ajoutDico(dic)

   cmpte.imprime()




