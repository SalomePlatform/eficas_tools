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

                                                                                        
from convert_python import PythonParser

pattern_comment_slash   = re.compile(r"^\s*/")
pattern_eta   = re.compile(r".*&ETA.*")
pattern_fin   = re.compile(r".*&FIN.*")
pattern_oui   = re.compile(r"^\s*(oui|OUI|YES|yes|TRUE|VRAI)\s*$")
pattern_non   = re.compile(r"^\s*(non|NON|NO|no|FALSE|FAUX)\s*$")
pattern_blanc = re.compile(r"^\s*$")
pattern_listeVide = re.compile(r"^\s*'\s*'\s*$")
pattern_commence_par_quote=re.compile(r'^\s*[\'"].*')
pattern_finit_par_virgule_ou_affect=re.compile(r'^.*(,|;|=|:)\s*$')

pattern_ligne=re.compile(r'^\s*(?P<ident>[^=:]*)\s*[:=]\s*(?P<reste>.*)$')

pattern_variables=re.compile (r"^\s*(?P<ident>VARIABLES FOR GRAPHIC PRINTOUTS|VARIABLES POUR LES SORTIES GRAPHIQUES)\s*[:=]\s*(?P<valeur>[A-Za-z]+(\d*|\*)(,[A-Za-z]+(\d*|\*))*)\s*(?P<reste>.*)$")

# Attention aux listes de flottants
pattern_liste=re.compile(r'^\s*(?P<valeur>[+-.\w]+(\s*;\s*[+-.\w]+)+)\s*(?P<reste>.*)$')
pattern_liste_texte=re.compile(r"^\s*(?P<valeur>('.*(';\s*))+('.*'\s*)?)(?P<reste>.*)$")
pattern_flottant=re.compile(r'^\s*(?P<valeur>[+-]?((\d+(\.\d*)?)|(\.\d+))([dDeE][+-]?\d+)?)\s*(?P<reste>.*)$')
pattern_texteQuote  = re.compile (r"^\s*(?P<valeur>'[^']+(''[^']+)*')\s*(?P<reste>.*)$")
pattern_texteSimple = re.compile (r"(?P<valeur>(^|\s)\s*[\w\.-]+)\s*(?P<reste>.*)$")
pattern_texteVide   = re.compile (r"^\s*(?P<valeur>'')\s*(?P<reste>.*)$")

pattern_ContientDouble=re.compile (r"^.*''.*$")

# le pattern texte reconnait 
#nom1 nom 2 : ou = chaine entre ' 
# avec eventuellement  des quotes au milieu par exemple
# TITRE = 'TELEMAC 2D : GOUTTE D''EAU DANS UN BASSIN$'
# m.group("texte") va rendre 'TELEMAC 2D : GOUTTE D''EAU DANS UN BASSIN$' 


#Si le code n est pas Telemac
try :
#if 1 :
   from aideAuxConvertisseurs import ListeSupprimeCasToEficas
   from enumDicoTelemac       import TelemacdicoEn
except :
   pass

from Extensions import localisation

from determine import monEnvQT5



def entryPoint():
   """
   Return a dictionary containing the description needed to load the plugin
   """
   return {
          'name' : 'TELEMAC3',
          'factory' : TELEMACParser
          }

class TELEMACParser(PythonParser):
   """
   This converter works like PythonParser, except that it also initializes all
   model variables to None in order to avoid Python syntax errors when loading
   a file with a different or inexistent definition of variables.
   """

   def convert(self, outformat, appli=None):
 

      from Accas import A_BLOC, A_FACT, A_SIMP
      self.dicoCasToCata=appli.readercata.dicoCasToCata
      self.dicoInverse=appli.readercata.dicoInverse
      self.dicoMC=appli.readercata.dicoMC
      self.Ordre_Des_Commandes=appli.readercata.Ordre_Des_Commandes

      if appli.langue=='fr' :
          from enumDicoTelemac       import DicoEnumCasFrToEnumCasEn
          for k in DicoEnumCasFrToEnumCasEn.keys() :
              TelemacdicoEn[k]=DicoEnumCasFrToEnumCasEn[k]

      text=""
      self.dictSimp={}

      l_lignes_texte_all = string.split(self.text,'\n')
      l_lignes_texte = []
      for l  in l_lignes_texte_all :
        if not(pattern_comment_slash.match(l)): l_lignes_texte.append(l)

      l_lignes=[]
      i=0
      while (i < len(l_lignes_texte)) :
          ligne=l_lignes_texte[i]
          i=i+1
          if not(pattern_finit_par_virgule_ou_affect.match(ligne)):
             l_lignes.append(ligne)
             continue
          nouvelle_ligne=ligne
          while (i < len(l_lignes_texte)):
             ligne_traitee=l_lignes_texte[i]
             i=i+1
             nouvelle_ligne += ligne_traitee
             if not(pattern_finit_par_virgule_ou_affect.match(ligne_traitee)):
                l_lignes.append(nouvelle_ligne)
                break
  

      for ligne in l_lignes :
          if pattern_comment_slash.match(ligne) : continue
          if pattern_eta.match(ligne) : continue
          if pattern_fin.match(ligne) : continue
          if pattern_blanc.match(ligne) : continue
 

          finLigne=ligne
          while finLigne != "" :
              if pattern_comment_slash.match(finLigne) : finLigne=""; continue
              valeur=""
              if pattern_variables.match(finLigne) :
                 m=pattern_variables.match(finLigne)
                 simpCas=self.traiteIdent(m.group('ident'))
                 valeur=m.group('valeur')
                 finLigne=m.group('reste')
                 self.dictSimp[simpCas]=valeur
                 continue

              
              m=pattern_ligne.match(finLigne)
              if m == None : 
                 #print( "________________________________________________")
                 print ('pb avec ****', finLigne , '**** dans ', ligne)
                 #print( "________________________________________________")
                 break
      
              simpCas=self.traiteIdent(m.group('ident'))
              if not simpCas : 
                 finLigne=m.group('reste')
                 continue

              finLigne=m.group('reste')
              # attention, l ordre des if est important
              if pattern_liste.match(finLigne) :
                 m=pattern_liste.match(finLigne)
              elif pattern_liste_texte.match(finLigne) :
                 m=pattern_liste_texte.match(finLigne)
              elif pattern_texteQuote.match(finLigne) :
                 m=pattern_texteQuote.match(finLigne)
              elif pattern_flottant.match(finLigne) : 
                 m=pattern_flottant.match(finLigne)
              elif pattern_texteVide.match(finLigne):
                 m=pattern_texteVide.match(finLigne)
              elif pattern_texteSimple.match(finLigne):
                 m=pattern_texteSimple.match(finLigne)
              else :
                 #print ("________________________________________________")
                 print ('pb avec ****', finLigne , '**** dans ', ligne)
                 print ("non match")
                 #print ("________________________________________________")
                 break
              

              valeur=m.group('valeur')
              if pattern_blanc.match(valeur) : valeur=None

              if pattern_flottant.match(finLigne) : 
                 valeur=re.sub("d","e",valeur)
                 valeur=re.sub("D","E",valeur)

              if pattern_liste.match(finLigne) or pattern_liste_texte.match(finLigne):
                 valeur=valeur.split(";")


              finLigne=m.group('reste')
              self.dictSimp[simpCas]=valeur
      
      if 'TITLE' not in self.dictSimp.keys() :
          import os
          #self.dictSimp['TITLE']=os.path.basename(self.filename)
      
      dicoParMC={}
      for simp in self.dictSimp.keys():
          if simp in TELEMACParser.__dict__.keys() : apply(TELEMACParser.__dict__[simp],(self,))

      for simp in self.dictSimp.keys():
          if simp in ListeSupprimeCasToEficas: continue
          if simp not in self.dicoInverse.keys() : 
             #print ( "************")
             print  ("pb avec dans dicoInverse", simp,'------')
             #print  ("************")
             continue
          listeGenea=self.dicoInverse[simp]
          listeGeneaReverse=[]
          for (u,v) in listeGenea : 
              if isinstance(v,A_BLOC.BLOC): continue
              listeGeneaReverse.append(u)
          listeGeneaReverse.reverse()
          dicoTravail=dicoParMC
          i=0
          while i < len(listeGeneaReverse[0:-1]) : 
            mot=listeGeneaReverse[i]
            i=i+1
            if mot not in dicoTravail.keys(): dicoTravail[mot]={}
            dicoTravail=dicoTravail[mot]
          dicoTravail[simp]=self.dictSimp[simp]
        
      self.textePy=""
      listeMC=self.tri(dicoParMC.keys())
      for k in listeMC :
          self.textePy += str(k )+ "("
          self.traiteMC(dicoParMC[k])
          self.textePy += ");\n"
           
              
      appli.listeTelemac=self.dictSimp.keys()  
      return self.textePy


   #----------------------------------------
   def traiteIdent(self,ident):
   # enleve les espaces de part et autre
   # traduit du langage Telemac vers le langage Catalogue
   #----------------------------------------
          while ident[-1] == " " or ident[-1] == '\t' : ident=ident[0:-1]
          while ident[0]  == " " or ident[0]  == '\t' : ident=ident[1:]
          try : identCata=self.dicoCasToCata[ident]
          except :  
            print ( "---> ", "pb mot clef  pour", ident)
            identCata=None
          return identCata


   def traiteMC(self,dico) :
       from Accas import A_BLOC, A_FACT, A_SIMP
       for k in dico.keys() :
           valeur= dico[k]
           if k not in self.dicoMC.keys() : kA=self.dicoFrancaisAnglais[k] 
           else : kA=k
           obj=self.dicoMC[kA]
           if isinstance(obj,A_FACT.FACT):   self.convertFACT(obj,kA,valeur)
           elif isinstance(obj,A_BLOC.BLOC): self.convertBLOC(obj,kA,valeur)
           elif isinstance(obj,A_SIMP.SIMP): self.convertSIMP(obj,kA,valeur)
           else : print ("%%%%%%%%%%%\n", "pb conversion type pour", k, obj, "\n%%%%%%%%%%%")


   def convertFACT(self,obj,nom,valeur):
       if nom in TELEMACParser.__dict__.keys() : 
          apply(TELEMACParser.__dict__[nom],(self,))
          return
       self.textePy +=  nom + "=_F( "
       self.traiteMC(valeur)
       self.textePy += '),\n'


   def convertBLOC(self,obj,nom,valeur):
       print ("ANOMALIE _________ BLOC ")
       print (nom)

   def convertSIMP(self,obj,nom,valeur):
       #print 'in convertSIMP', nom,valeur
       if nom in ("PRESCRIBED_FLOWRATES", "PRESCRIBED_VELOCITIES", "PRESCRIBED_ELEVATIONS" ): return
       if obj.max==1 : 
          if hasattr(obj.type[0],'ntuple') : 
             lval=[]
             for v in valeur : 
               try :    v=eval(v,{})
               except : pass
               lval.append(v)
             self.textePy += nom + "=" + str(lval) +","
             return
          if 'TXM' in obj.type :

              if pattern_ContientDouble.match(str(valeur)):
                 valeur=re.sub("''","\'\'",str(valeur))
                 self.textePy += nom + "=" + str(valeur) +","
                 return
              valeur=str(valeur)

              # ceinture et bretelle si les re sont correctes -)
              while valeur[-1] == " " or valeur[-1] == '\t' : valeur=valeur[0:-1]
              while valeur[0]  == " " or valeur[0]  == '\t' : valeur=valeur[1:]



          # Pour les enum
          try    : valeur=eval(valeur,{})
          except : pass

          if nom in TelemacdicoEn.keys(): 
             try    : 
               valeur=TelemacdicoEn[nom][valeur]
               self.textePy += nom + "= '" + str(valeur) +"',"
               return
             except : pass


          if obj.into != [] and obj.into != None and not('R' in obj.type) and not('I' in obj.type):
             for possible in obj.into :
                try :
                  if possible.upper() == valeur.upper():
                     valeur=possible
                     break
                  v=valeur[0].upper()+valeur[1:].lower()
                  v2=tr(v)
                  if possible.upper() == v2.upper():
                     valeur=possible
                     break
                except:
                   if valeur != None :
                      print ("pb avec le type de ", obj.nom, obj.type, 'et la valeur ', valeur)

          if 'Fichier' in obj.type or 'TXM' in obj.type or 'Repertoire' in obj.type :
              valeur=str(valeur)
              if valeur == "" or valeur == " " : 
                 self.textePy += nom + "= '" + str(valeur) +"' ,"
                 return
              while valeur[-1] == " " : valeur=valeur[0:-1]
              while valeur[0]  == " " : valeur=valeur[1:]
              self.textePy += nom + "= '" + str(valeur) +"' ,"
              return

          if bool in obj.type :
            if   valeur == True  :  self.textePy += nom + "= True,"
            elif valeur == False :  self.textePy += nom + "= False,"
            elif pattern_oui.match(valeur) : self.textePy += nom + "= True,"
            elif pattern_non.match(valeur) : self.textePy += nom + "= False,"
            else :  self.textePy += nom + "= None,"
            return
          self.textePy += nom + "=" + str(valeur) +","

       else :
          if valeur == () or valeur ==[] or pattern_listeVide.match(str(valeur)) :
             self.textePy += nom + "= None,"
             return

          # les 4 lignes suivantes sont probablement inutiles
          while valeur[-1] == " " or  valeur[-1]=="'" : valeur=valeur[0:-1]
          while valeur[0]  == " " or  valeur[-0]=="'" : valeur=valeur[1:]
          oldValeur=valeur
          if isinstance(valeur, basestring) :
             if   ";" in valeur : valeur=valeur.split(';')
             else  : valeur=valeur.split(',')

          if len(valeur)< 2 and pattern_flottant.match(oldValeur):
          # Attention : on attend une liste mais on a une seule valeur!
             try :    oldValeur=eval(oldValeur,{})
             except : pass
             if nom in TelemacdicoEn.keys() :  
                v=TelemacdicoEn[nom][oldValeur]
                self.textePy += nom + "= ('" + str(v) +"',),"
             else :  
                self.textePy += nom + "= (" + str(oldValeur) +",),"
             return
           
 
          if valeur == None : return
          newVal=[]
          for v in valeur :
            try :    v=eval(v,{})
            except : pass
            if nom in TelemacdicoEn.keys():
               try    : v=TelemacdicoEn[nom][v]
               except : pass
            newVal.append(v)
          self.textePy += nom + "=" + str(newVal) +","
          


   def tri(self, listeIn):
      if len(listeIn) == 1 : return listeIn
      if self.Ordre_Des_Commandes == None : return listeIn
      listeOut=[listeIn[0],]
      for k in listeIn[1:]:
          #k=str(self.dicoFrancaisAnglais[kF])
          ordreK=self.Ordre_Des_Commandes.index(k)
          i=0
          while i < len(listeOut):
             #ordreI=self.Ordre_Des_Commandes.index(self.dicoFrancaisAnglais[listeOut[i]])
             ordreI=self.Ordre_Des_Commandes.index(listeOut[i])
             if ordreK < ordreI : break
             i=i+1
          #listeOut.insert(i,kF)
          listeOut.insert(i,k)
      return listeOut

   def LIQUID_BOUNDARIES(self):
       texte_Boundaries="LIQUID_BOUNDARIES=( "
       if 'PRESCRIBED_ELEVATIONS' in self.dictSimp.keys(): 
              valeursPE=self.dictSimp["PRESCRIBED_ELEVATIONS"]
              if not type(valeursPE)==list : valeursPE = (valeursPE,)
              longueur=len(self.dictSimp["PRESCRIBED_ELEVATIONS"])
       else : valeursPE=None
       if 'PRESCRIBED_FLOWRATES' in self.dictSimp.keys(): 
              valeursPF=self.dictSimp["PRESCRIBED_FLOWRATES"]
              if not type(valeursPF)==list : valeursPF = (valeursPF,)
              longueur=len(self.dictSimp["PRESCRIBED_FLOWRATES"])
       else : valeursPF=None
       if 'PRESCRIBED_VELOCITIES' in self.dictSimp.keys(): 
              valeursPV=self.dictSimp["PRESCRIBED_VELOCITIES"]
              if not type(valeursPV)==list : valeursPV = (valeursPV,)
              longueur=len(self.dictSimp["PRESCRIBED_VELOCITIES"])
       else : valeursPV=None

       if valeursPE == None and valeursPF == None and valeursPV == None :
             texte_Boundaries +="),\n"
             return

       if valeursPE == None or valeursPF == None or valeursPV == None :
          listNulle=[]
          for i in range(longueur) : listNulle.append('0') 


       if valeursPE == None : valeursPE = listNulle
       if valeursPF == None : valeursPF = listNulle
       if valeursPV == None : valeursPV = listNulle
      

       for e in range(len(valeursPE)):
          if valeursPE[e] != "" or valeursPE[e] != "\n" :
            if eval(valeursPE[e],{}) != 0 : 
               texte_Boundaries += "_F(BOUNDARY_TYPE = 'Prescribed Elevations',\n"
               texte_Boundaries += "PRESCRIBED_ELEVATIONS = " + str(valeursPE[e]) + "),\n"
               continue

          if valeursPF[e] != "" or valeursPF[e] != "\n" :
            if eval(valeursPF[e],{}) != 0 : 
               texte_Boundaries += "_F(BOUNDARY_TYPE = 'Prescribed Flowrates',\n"
               texte_Boundaries += "PRESCRIBED_FLOWRATES = " + str(valeursPF[e]) + "),\n"
               continue
               
          if valeursPV[e] != "" or valeursPV[e] != "\n" :
             if eval(valeursPV[e],{})!=0 : 
                texte_Boundaries += "_F( BOUNDARY_TYPE= 'Prescribed Velocity',\n"
                texte_Boundaries += "PRESCRIBED_VELOCITIES = " + str(valeursPV[e]) + "),\n"
                continue
          print ("pb texte_Boundaries avec la valeur numero ", e)

       texte_Boundaries +="),\n"
       self.textePy += texte_Boundaries
      
