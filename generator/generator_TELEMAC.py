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
"""Ce module contient le plugin generateur de fichier au format  Code_Carmel3D pour EFICAS.
"""

import traceback
import types,string,re,os
from Extensions.i18n import tr
from generator_python import PythonGenerator

extensions=('.comm',)
from aideAuxConvertisseurs import listeSupprime, DicoAglomere, DicoEficasToCas
from enumDicoTelemac       import DicoEnumCasEnInverse


def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins
      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'TELEMAC',
        # La factory pour creer une instance du plugin
          'factory' : TELEMACGenerator,
          }


class TELEMACGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 
      un texte au format dictionnaire

   """

#----------------------------------------------------------------------------------------
   def gener(self,obj,format='brut',config=None):
       
      self.initDico()
      #print self.texteDico
      
      # Cette instruction genere le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)
      return self.text


#----------------------------------------------------------------------------------------
# initialisations
#----------------------------------------------------------------------------------------
   
   def initDico(self) :
 
      self.PE=False
      self.FE=False
      self.VE=False
      self.textPE = 'PRESCRIBED ELEVATIONS :'
      self.textFE = 'PRESCRIBED FLOWRATES :'
      self.textVE = 'PRESCRIBED VELOCITY :'
      self.texteDico = ""
 



#----------------------------------------------------------------------------------------
# ecriture
#----------------------------------------------------------------------------------------

   def writeDefault(self,fn) :
       fileDico = fn[:fn.rfind(".")] + '.py'
       f = open( str(fileDico), 'wb')
       f.write( self.texteDico )
       f.close()

#----------------------------------------------------------------------------------------
#  analyse de chaque noeud de l'arbre 
#----------------------------------------------------------------------------------------

   def generPROC_ETAPE(self,obj):
        self.texteDico += '/------------------------------------------------------/\n'
        self.texteDico += '/\t\t\t'+obj.nom +'\n'
        self.texteDico += '/------------------------------------------------------/\n'
        s=PythonGenerator.generPROC_ETAPE(self,obj)
        #print obj
        #print obj.nom
        if obj.nom in TELEMACGenerator.__dict__.keys() : apply(TELEMACGenerator.__dict__[obj.nom],(self,obj))
        
        return s

   def generMCSIMP(self,obj) :
        """recuperation de l objet MCSIMP"""
        s=PythonGenerator.generMCSIMP(self,obj)
        if obj.nom == "Title" :
            print s
            print str(obj.valeur)
            print repr(obj.valeur)

       
        # Attention pas sur --> ds certains cas non traite par MCFACT ?
        # a reflechir avec Yoann 
        if hasattr(obj.definition,'defaut') :
           if obj.definition.defaut == obj.valeur : return s

        nomMajuscule=obj.nom.upper()
        nom=nomMajuscule.replace('_',' ') 
        if nom in listeSupprime or s == "" : return s

        sTelemac=s[0:-1]
        if not( type(obj.valeur) in (types.TupleType,types.ListType) ):
           if obj.nom in DicoEnumCasEnInverse.keys():  
             try : sTelemac=DicoEnumCasEnInverse[obj.nom][obj.valeur]
             except : print "generMCSIMP Pb avec ", obj.nom, obj.valeur
        if type(obj.valeur) in (types.TupleType,types.ListType) :
           if obj.nom in DicoEnumCasEnInverse.keys():  
             sT = "'"
             for v in obj.valeur:
               try : sT +=DicoEnumCasEnInverse[obj.nom][v] +";"
               except : print "generMCSIMP Pb avec ", obj.nom, v
             sTelemac=sT[0:-1]+"'"

        if nom in DicoEficasToCas.keys() : nom=DicoEficasToCas[nom]
        self.texteDico+=nom+ ":" + str(sTelemac) + "\n"
        return s

   def generMCFACT(self,obj):
      """
      """
      s=PythonGenerator.generMCFACT(self,obj)
      if obj.nom in TELEMACGenerator.__dict__.keys() : apply(TELEMACGenerator.__dict__[obj.nom],(self,obj))
 
      return s

  
   def Liquid_Boundaries(self,obj):
      #print obj.nom , dir(obj)
      if 'Type_Condition' in  obj.liste_mc_presents() :
          objForme=obj.get_child('Type_Condition')
          valForme=objForme.valeur
          if valForme == None : return

          nomBloc='b_'+valForme.split(" ")[1] 
          if nomBloc in  obj.liste_mc_presents() :
             objBloc=obj.get_child(nomBloc)
             objValeur=objBloc.get_child(objBloc.liste_mc_presents()[0])
             valeur=objValeur.valeur
             if valeur== None : valeur="0."
          if valForme == 'Prescribed Elevations' :
              self.PE=True
              self.textPE += str(valeur) +"; "
          else : self.textPE += "0.; "
          if valForme == 'Prescribed Flowrates' :
              self.FE=True
              self.textFE += str(valeur) +"; "
          else : self.textFE += "0.; "
          if valForme == 'Prescribed Velocity'  :
              self.VE=True
              self.textVE += str(valeur) +"; "
          else : self.textVE += "0.; "
      #print self.textPE, self.textFE,self.textVE

   def BOUNDARY_CONDITIONS(self,obj):
       if self.FE :  self.texteDico += self.textFE[0:-1]+'\n' 
       if self.VE :  self.texteDico += self.textVE[0:-1]+'\n' 
       if self.PE :  self.texteDico += self.textPE[0:-1]+'\n' 

   def Validation(self,obj):
       self.texteDico += "VALIDATION : True \n"
 
   def Date_De_L_Origine_Des_Temps (self,obj):
       an=obj.get_child('Year').valeur
       mois=obj.get_child('Month').valeur
       jour=obj.get_child('Day').valeur
       #print an, mois, jour
       self.texteDico += "ORIGINAL DATE OF TIME  :"+ str(an)+ " ,"+str(mois)+ "," +str(jour)+ "\n"

   def Original_Hour_Of_Time (self,obj):
       hh=obj.get_child('Hour').valeur
       mm=obj.get_child('Minute').valeur
       ss=obj.get_child('Second').valeur
       #print hh, mm, ss
       self.texteDico += "ORIGINAL HOUR OF TIME :"+str(hh)+" ,"+str(mm)+ ","+str(ss)+"\n"

   def Type_Of_Advection(self,obj):
       listeAdvection=[1,5,1,1]
       listeSupg=[2,2,2,2]
       listeUpwind=[1.,1.,1.,1.]
       self.listeMCAdvection=[]
       self.chercheChildren(obj)
       dicoSuf={ 'U_And_V' : 0, 'H' : 1, 'K_And_Epsilon' : 2, 'Tracers' : 3}
       for c in  self.listeMCAdvection:
           #print c.nom
           if c.nom[0:18] == 'Type_Of_Advection_' and c.valeur!=None:
              suf=c.nom[18:]
              index=dicoSuf[suf]
              #print c.valeur
              #print DicoEnumCasEnInverse['Type_Of_Advection']
              listeAdvection[index]=DicoEnumCasEnInverse['Type_Of_Advection'][c.valeur]
           if c.nom[0:13] == 'Supg_Option_' and c.valeur!=None:
              suf=c.nom[13:]
              index=dicoSuf[suf]
              listeAdvection[index]=DicoEnumCasEnInverse['Supg_Option'][c.valeur]
           if c.nom[0:23] == 'Upwind_Coefficients_Of_' and c.valeur!=None:
              suf=c.nom[23:]
              index=dicoSuf[suf]
              listeUpwind[index]=c.valeur
       self.texteDico += "TYPE OF ADVECTION = "+ str(listeAdvection) + "\n"
       self.texteDico += "SUPG OPTION = "+ str(listeSupg) + "\n"
       self.texteDico += "UPWIND COEFFICIENTS = "+ str(listeUpwind) + "\n"
       
   def chercheChildren(self,obj):
       for c in obj.liste_mc_presents():
           objc=obj.get_child(c)
           if hasattr(objc,'liste_mc_presents') and objc.liste_mc_presents() != [] : self.chercheChildren(objc)
           else : self.listeMCAdvection.append(objc)

      
 
