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
import re, string
from Extensions.i18n import tr
from Accas.A_BLOC import BLOC
from Accas import *

                                                                                        
from convert_python import PythonParser

pattern_comment_slash   = re.compile(r"^\s*/")
pattern_eta   = re.compile(r".*&ETA.*")
pattern_fin   = re.compile(r".*&FIN.*")
pattern_blanc = re.compile(r"^ *$")
pattern_OUI   = re.compile(r"^ *OUI *")
pattern_oui   = re.compile(r"^ *oui *")
pattern_NON   = re.compile(r"^ *NON *")
pattern_non   = re.compile(r"^ *non *")
pattern_vide  = re.compile(r"^ *$")

from aideAuxConvertisseurs import DicoEficasToCas, ListeSupprimeCasToEficas
from aideAuxConvertisseurs import ListeCalculCasToEficas, DicoAvecMajuscules
from enumDicoTelemac2      import DicoEnumCasEn

from Extensions import localisation

from determine import monEnvQT5



def entryPoint():
   """
   Return a dictionary containing the description needed to load the plugin
   """
   return {
          'name' : 'TELEMAC',
          'factory' : TELEMACParser
          }

class TELEMACParser(PythonParser):
   """
   This converter works like PythonParser, except that it also initializes all
   model variables to None in order to avoid Python syntax errors when loading
   a file with a different or inexistent definition of variables.
   """

   def convert(self, outformat, appli=None):
      self.dicoInverseFrancais=appli.readercata.dicoInverseFrancais
      self.dicoAnglaisFrancais=appli.readercata.dicoAnglaisFrancais
      self.dicoFrancaisAnglais=appli.readercata.dicoFrancaisAnglais
      self.dicoMC=appli.readercata.dicoMC
      self.Ordre_Des_Commandes=appli.readercata.Ordre_Des_Commandes
   

      #print self.dicoInverseFrancais
      #text = PythonParser.convert(self, outformat, appli)
      
      text=""
      l_lignes = string.split(self.text,'\n')
      self.dictSimp={}
      for ligne in l_lignes :
          if pattern_comment_slash.match(ligne) : continue
          if pattern_eta.match(ligne) : continue
          if pattern_fin.match(ligne) : continue
          if pattern_blanc.match(ligne) : continue
          ligne=re.sub('\t',' ',ligne)
          ligne=re.sub("'",' ',ligne)
          ligne=re.sub(":",'=',ligne)
          if ligne.count('=') != 1 :
              print "pb avec la ligne " , ligne
              continue 

          motsInLigne=string.split(ligne,' ')
          listeMotsSimp=()
          simp=""
          for mot in motsInLigne:
              if mot == ""   : continue
	      if mot == "="  :
                 simp=simp[0:-1]
                 while simp[-1] == " " : simp=simp[0:-1]
                 if simp.find('-') > 0 : simp=self.redecoupeSimp(simp)
                 break

              mot=mot.replace('_','__')
              simp=simp+mot[0].upper() +mot[1:].lower()+'_'
          valeur=ligne.split('=')[1]
          self.dictSimp[simp]=valeur

      
      
      #print dictSimp
      #print self.dicoInverseFrancais

      dicoParMC={}
      #print ListeCalculCasToEficas

      if 'Titre' not in self.dictSimp.keys():
          import os
          self.dictSimp['Titre']=os.path.basename(self.filename)
      
      for simp in self.dictSimp.keys():
          if simp in ListeSupprimeCasToEficas: continue
          if simp in TELEMACParser.__dict__.keys() : apply(TELEMACParser.__dict__[simp],(self,))

      for simp in self.dictSimp.keys():
          if simp not in self.dicoInverseFrancais.keys() : 
             print "************"
             print "pb avec ", simp,'------'
             print "************"
             continue
          listeGenea=self.dicoInverseFrancais[simp]
          listeGeneaReverse=[]
          for (u,v) in listeGenea : 
              if isinstance(v,BLOC): continue
              listeGeneaReverse.append(u)
          listeGeneaReverse.reverse()
          dicoTravail=dicoParMC
          i=0
          #print (listeGeneaReverse[0:-1])
          while i < len(listeGeneaReverse[0:-1]) : 
            mot=listeGeneaReverse[i]
            i=i+1
            if mot not in dicoTravail.keys(): dicoTravail[mot]={}
            dicoTravail=dicoTravail[mot]
          dicoTravail[simp]=self.dictSimp[simp]
        
      self.textePy=""
      #print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
      #print dicoParMC
      #print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
      listeMC=self.tri(dicoParMC.keys())
      for k in listeMC :
          print "----------- traitement de " , k
          self.textePy += self.dicoFrancaisAnglais[k] + "("
          self.traiteMC(dicoParMC[k])
          self.textePy += ");\n"
          print "----------- " 
           
              
      print self.textePy
      return self.textePy 

   def traiteMC(self,dico) :
       for k in dico.keys() :
           valeur= dico[k]
           if k not in self.dicoMC.keys() : kA=self.dicoFrancaisAnglais[k] 
           else : kA=k
           obj=self.dicoMC[kA]
           if isinstance(obj,FACT):   self.generFACT(obj,kA,valeur)
           elif isinstance(obj,BLOC): self.generBLOC(obj,kA,valeur)
           elif isinstance(obj,SIMP): self.generSIMP(obj,kA,valeur)
           else : print "%%%%%%%%%%%\n", "pb generation pour", k, obj, "\n%%%%%%%%%%%"

           #print "_____________"

   def generFACT(self,obj,nom,valeur):
       if nom in TELEMACParser.__dict__.keys() : 
          apply(TELEMACParser.__dict__[nom],(self,))
          return
       self.textePy +=  nom + "=_F( "
       self.traiteMC(valeur)
       self.textePy += '),\n'


   def generBLOC(self,obj,nom,valeur):
       print "BLOC "
       print nom

   def generSIMP(self,obj,nom,valeur):
       if nom in ("Prescribed_Flowrates", "Prescribed_Velocities", "Prescribed_Elevations" ): return
       if obj.max==1 : 
          if 'TXM' in obj.type :
              valeur=str(valeur)
              while valeur[-1] == " " : valeur=valeur[0:-1]
              while valeur[0]  == " " : valeur=valeur[1:]
              valeur=valeur[0].upper()+valeur[1:].lower()
              valeur=tr(valeur)
          try    : valeur=eval(valeur,{})
          except : pass
          if nom in DicoEnumCasEn.keys(): 
             try    : valeur=DicoEnumCasEn[nom][valeur]
             except : pass
          if 'Fichier' in obj.type or 'TXM' in obj.type or 'Repertoire' in obj.type :
              valeur=str(valeur)
              while valeur[-1] == " " : valeur=valeur[0:-1]
              while valeur[0]  == " " : valeur=valeur[1:]
              self.textePy += nom + "= '" + str(valeur) +"' ,"
              return
          if bool in obj.type :
            if pattern_OUI.match(valeur) or  pattern_oui.match(valeur) : self.textePy += nom + "= True,"
            if pattern_NON.match(valeur) or  pattern_non.match(valeur) : self.textePy += nom + "= False,"
            return
          self.textePy += nom + "=" + str(valeur) +","
       else :
          if pattern_vide.match(valeur) : return
          while valeur[-1] == " " : valeur=valeur[0:-1]
          while valeur[0]  == " " : valeur=valeur[1:]

          if   ";" in valeur : valeur=valeur.split(';')
          elif "," in valeur : valeur=valeur.split(',')

          if valeur == None : return
          newVal=[]
          for v in valeur :
            try :    v==eval(v,{})
            except : pass
            if nom in DicoEnumCasEn.keys():
               try    : v=DicoEnumCasEn[nom][v]
               except : pass
            newVal.append(v)
          self.textePy += nom + "=" + str(newVal) +","
          



   def tri(self, listeIn):
      if len(listeIn) == 1 : return listeIn
      if self.Ordre_Des_Commandes == None : return listeIn
      #print self.Ordre_Des_Commandes
      listeOut=[listeIn[0],]
      for kF in listeIn[1:]:
          k=str(self.dicoFrancaisAnglais[kF])
          ordreK=self.Ordre_Des_Commandes.index(k)
          i=0
          while i < len(listeOut):
             ordreI=self.Ordre_Des_Commandes.index(self.dicoFrancaisAnglais[listeOut[i]])
             if ordreK < ordreI : break
             i=i+1
          listeOut.insert(i,kF)
      return listeOut

   def Processeurs_Paralleles(self):
      #YOANN
      if self.dictSimp["Processeurs_Paralleles"] == 0 : del  self.dictSimp["Processeurs_Paralleles"]
      else : self.dictSimp["Parallel_Computation"]="Parallel"
 
      
   def Option_De_Supg(self):
       print "ds Option_De_Supg"
       return

   def Forme_De_La_Convection(self):
       print "ds Forme_De_La_Convection"
       return

   def redecoupeSimp(self,simp): 
      # replace('-','_')  uniquement dans les identifiants
      while simp.find('-') > 0 : 
        ind=simp.find('-')
        if ind==len(simp)-1 : break
        simp=simp[0:ind]+'_'+simp[ind+1].upper()+simp[ind+2:]
      return simp



   def Liquid_Boundaries(self):
       texte_Boundaries="Liquid_Boundaries=( "
       premier=0
       if 'Prescribed_Elevations' in self.dictSimp.keys(): 
           valeurs=self.dictSimp["Prescribed_Elevations"].split(";")
       elif 'Cotes_Imposees' in self.dictSimp.keys(): 
           valeurs=self.dictSimp["Cotes_Imposees"].split(";")
       else : valeurs=()
       for e in range(len(valeurs)):
          if valeurs[e] == "" or valeurs[e] == "\n" : continue
          if eval(valeurs[e],{})==0 : continue
          if not premier : premier=1
          texte_Boundaries += "_F(Type_Condition = 'Prescribed Elevations',\n"
          texte_Boundaries += "Prescribed_Elevations = " + str(valeurs[e]) + "),\n"
               
       if 'Prescribed_Flowrates' in self.dictSimp.keys(): 
          valeurs=self.dictSimp["Prescribed_Flowrates"].split(";")
       elif 'Debits_Imposes' in self.dictSimp.keys(): 
          valeurs=self.dictSimp["Debits_Imposes"].split(";")
       else : valeurs=()
       for e in range(len(valeurs)):
          if valeurs[e] == "" or valeurs[e] == "\n" : continue
          if eval(valeurs[e],{})==0 : continue
          if not premier : premier=1
          texte_Boundaries += "_F(Type_Condition = 'Prescribed Flowrates',\n"
          texte_Boundaries += "Prescribed_Flowrates = " + str(valeurs[e]) + "),\n"
               
       if 'Prescribed_Velocity' in self.dictSimp.keys(): 
           valeurs=self.dictSimp["Prescribed_Velocity"].split(";")
       elif 'Vitesses_Imposees' in self.dictSimp.keys(): 
           valeurs=self.dictSimp["Vitesses_Imposees"].split(";")
       else : valeurs=()
       for e in range(len(valeurs)):
          if valeurs[e] == "" or valeurs[e] == "\n" : continue
          if eval(valeurs[e],{})==0 : continue
          if not premier : premier=1
          texte_Boundaries += "_F(Type_Condition = 'Prescribed Velocity',\n"
          texte_Boundaries += "Prescribed_Velocity = " + str(valeurs[e]) + "),\n"
       if premier :  texte_Boundaries +="),\n"
       else : texte_Boundaries="" ; print "pb texte_Boundaries "
       self.textePy += texte_Boundaries
      
