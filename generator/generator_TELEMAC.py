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

from __future__ import absolute_import
from __future__ import print_function
try :
   from builtins import str
except : pass

import traceback
import types,re,os
from Extensions.i18n import tr
from .generator_python import PythonGenerator

extensions=('.comm',)
#if 1:
try :
   from enumDicoTelemac       import TelemacdicoEn
   DicoEnumCasEnInverse={}
   for motClef in TelemacdicoEn:
     d={}
     for valTelemac in TelemacdicoEn[motClef]:
        valEficas= TelemacdicoEn[motClef][valTelemac]
        d[valEficas]=valTelemac
     DicoEnumCasEnInverse[motClef]=d

except :
   pass




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
   def gener(self,obj,format='brut',config=None,appli=None,statut="Entier"):
       
      self.statut=statut
      self.langue=appli.langue
      self.initDico()
      # Pour Simplifier les verifs d ecriture
      if hasattr(appli,'listeTelemac') : self.listeTelemac=appli.listeTelemac
      else : self.listeTelemac = ()

      self.dicoCataToCas={}
      self.dicoCasToCata=appli.readercata.dicoCasToCata
      for motClef in self.dicoCasToCata:
           self.dicoCataToCas[self.dicoCasToCata[motClef]]=motClef



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
      self.commentaireAvant = False
      self.texteCom=''
      if self.langue == "fr" :
        self.textPE = 'COTES IMPOSEES :'
        self.textFE = 'DEBITS IMPOSES :'
        self.textVE = 'VITESSES IMPOSEES :'
      else :
        self.textPE = 'PRESCRIBED ELEVATIONS :'
        self.textFE = 'PRESCRIBED FLOWRATES :'
        self.textVE = 'PRESCRIBED VELOCITIES :'
      self.nbTracers = 0
      self.texteDico = ""
 



#----------------------------------------------------------------------------------------
# ecriture de tout
#----------------------------------------------------------------------------------------

   def writeDefault(self,fn) :
       self.texteDico+='\n&ETA\n&FIN\n'
       if self.statut == 'Leger' : extension = ".Lcas"
       else                      : extension = ".cas"
       fileDico = fn[:fn.rfind(".")] + extension 
       f = open( str(fileDico), 'w')
       f.write( self.texteDico )
       f.close()

#----------------------------------------------------------------------------------------
# ecriture de Leger
#----------------------------------------------------------------------------------------

   def writeLeger(self,fn,jdc,config,appli) :
       jdc_formate=self.gener(jdc,config=config,appli=appli,statut="Leger")
       self.writeDefault(fn) 


#----------------------------------------------------------------------------------------
#  analyse de chaque noeud de l'arbre 
#----------------------------------------------------------------------------------------

   def generPROC_ETAPE(self,obj):
        if  not self.commentaireAvant or self.texteCom.find(obj.nom) < 0: 
            self.texteDico += '/------------------------------------------------------------------/\n'
            self.texteDico += '/\t\t\t'+obj.nom +'\n'
            self.texteDico += '/------------------------------------------------------------------/\n'
        self.commentaireAvant = False
        self.texteCom=''
        s=PythonGenerator.generPROC_ETAPE(self,obj)
        if obj.nom in TELEMACGenerator.__dict__ : TELEMACGenerator.__dict__[obj.nom](*(self,obj))
        
        return s

   def generMCSIMP(self,obj) :
        """recuperation de l objet MCSIMP"""
        s=PythonGenerator.generMCSIMP(self,obj)

       
        # Attention pas sur --> ds certains cas non traite par MCFACT ?
        # a reflechir avec Yoann 
        # ajouter le statut ?
        if self.statut == 'Leger' :
          if hasattr(obj.definition,'defaut') and (obj.definition.defaut == obj.valeur) and (obj.nom not in self.listeTelemac) : return s
          if hasattr(obj.definition,'defaut') and obj.definition.defaut != None and (type(obj.valeur) == tuple or type(obj.valeur) == list) and (tuple(obj.definition.defaut) == tuple(obj.valeur)) and (obj.nom not in self.listeTelemac) : return s
 

        #nomMajuscule=obj.nom.upper()
        #nom=nomMajuscule.replace('_',' ') 
        #if nom in listeSupprime or s == "" : return s
        if s == "" : return s

      

        sTelemac=s[0:-1]
        if not( type(obj.valeur) in (tuple,list) ):
           if obj.nom in DicoEnumCasEnInverse:  
             try : sTelemac=str(DicoEnumCasEnInverse[obj.nom][obj.valeur])
             except : 
               if obj.valeur==None :  sTelemac=obj.valeur
               else : print(("generMCSIMP Pb valeur avec ", obj.nom, obj.valeur))
        if type(obj.valeur) in (tuple,list) :
           if obj.nom in DicoEnumCasEnInverse:  
             #sT = "'"
             sT=''
             for v in obj.valeur:
               try : sT +=str(DicoEnumCasEnInverse[obj.nom][v]) +";"
               except : 
                 if obj.definition.intoSug != [] : sT +=str(v) + ";"
                 else : print(("generMCSIMP Pb Tuple avec ", obj.nom, v, obj.valeur))
             #sTelemac=sT[0:-1]+"'"
             sTelemac=sT[0:-1]
           else  :
             sTelemac=sTelemac[0:-1]
             if sTelemac.find("'") > 0 :
                sTelemac= sTelemac.replace (',',';\n	') 
                # on enleve le dernier  ';'
                index=(sTelemac.rfind(";"))
                sTelemac=sTelemac[:index]+' '+sTelemac[index+1:]


        if self.langue=='fr' :
           s1=str(sTelemac).replace('True','OUI')
           s2=s1.replace('False','NON')
        else :
           s1=str(sTelemac).replace('True','YES')
           s2=s1.replace('False','NO')
        s3=s2.replace(',',';')
        if s3 != "" and s3[0]=='(' : 
          try : s3=s3[1:-1] # cas de liste vide
          except : s3 = ' '
        
       
        # LIQUID_BOUNDARIES
        if obj.nom in ('PRESCRIBED_FLOWRATES','PRESCRIBED_VELOCITIES','PRESCRIBED_ELEVATIONS') :
           return s

        if obj.nom not in self.dicoCataToCas :
           if obj.nom == 'Consigne' : return ""
           return s

        nom=self.dicoCataToCas[obj.nom]
        if nom in ["VARIABLES FOR GRAPHIC PRINTOUTS", "VARIABLES POUR LES SORTIES GRAPHIQUES", "VARIABLES TO BE PRINTED","VARIABLES A IMPRIMER"] :
              if s3 != 'None' :
                s3=s3.replace(';',',')
                s3="'"+ s3 +"'"
        if s3 == "" or s3 == " " : s3 = "None"
        ligne=nom+ " : " + s3 + "\n"
        if len(ligne) > 72 : ligne=self.redecoupeLigne(nom,s3) 
        self.texteDico+=ligne

   def generMCFACT(self,obj):
      """
      """
      s=PythonGenerator.generMCFACT(self,obj)
      if obj.nom in TELEMACGenerator.__dict__ : TELEMACGenerator.__dict__[obj.nom],(self,obj)
 
      return s

  
   def LIQUID_BOUNDARIES(self,obj):
      if 'BOUNDARY_TYPE' in  obj.liste_mc_presents() :
          objForme=obj.get_child('BOUNDARY_TYPE')
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

   def BOUNDARY_CONDITIONS(self,obj):
       # sans '; '
       if self.FE :  self.texteDico += self.textFE[0:-2]+'\n' 
       if self.PE :  self.texteDico += self.textPE[0:-2]+'\n' 
       if self.VE :  self.texteDico += self.textVE[0:-2]+'\n' 

   def TRACERS(self,obj):
       if self.nbTracers != 0 :  self.texteDico += 'NUMBER_OF_TRACERS : '+str(self.nbTracers) + '\n'
 

   def NAME_OF_TRACER(self,obj):
       print((dir(obj) ))
       print((obj.get_genealogie_precise()))

   def Validation(self,obj):
       self.texteDico += "VALIDATION : True \n"
 
   def Date_De_L_Origine_Des_Temps (self,obj):
       an=obj.get_child('Year').valeur
       mois=obj.get_child('Month').valeur
       jour=obj.get_child('Day').valeur
       self.texteDico += "ORIGINAL DATE OF TIME  :"+ str(an)+ " ,"+str(mois)+ "," +str(jour)+ "\n"

   def Original_Hour_Of_Time (self,obj):
       hh=obj.get_child('Hour').valeur
       mm=obj.get_child('Minute').valeur
       ss=obj.get_child('Second').valeur
       self.texteDico += "ORIGINAL HOUR OF TIME :"+str(hh)+" ,"+str(mm)+ ","+str(ss)+"\n"

   def Type_Of_Advection(self,obj):
       listeAdvection=[1,5,1,1]
       listeSupg=[2,2,2,2]
       listeUpwind=[1.,1.,1.,1.]
       self.listeMCAdvection=[]
       self.chercheChildren(obj)
       dicoSuf={ 'U_And_V' : 0, 'H' : 1, 'K_And_Epsilon' : 2, 'Tracers' : 3}
       for c in  self.listeMCAdvection:
           if c.nom[0:18] == 'Type_Of_Advection_' and c.valeur!=None:
              suf=c.nom[18:]
              index=dicoSuf[suf]
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

      
 
   def redecoupeLigne(self,nom,valeur) :
       text=nom+ " : \n"
       valeur=valeur
       if valeur.find("'") > -1:
          lval=valeur.split(";")
          for v in lval : text+='   '+v+';'
          text=text[0:-1]+'\n'
       else :
         lval=valeur.split(";")
         ligne="   "
         for v in lval :
           if len(ligne) < 70 : ligne += str(v)+'; '
           else :
              text+= ligne+"\n"
              ligne="   "+str(v)+'; '
         text+= ligne[0:-2]+'\n'
       return text

   def generCOMMENTAIRE(self,obj):
       sans_saut = re.sub("\n$","",obj.valeur)
       l_lignes = sans_saut.split('\n')
       txt='/'+66*'-'+'/'+'\n'
       i=1
       for ligne in l_lignes:
         self.texteCom+=ligne+'\n'
         txt = txt + '/'+ligne+'\n'
       txt= txt + '/'+66*'-'+'/'+'\n'
       self.texteDico += txt
       self.commentaireAvant= True
       return PythonGenerator.generCOMMENTAIRE(self,obj)


