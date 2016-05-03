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
pattern_non   = re.compile(r"^\s*(non|NON|NO|no|FALSE|FAUX)\*s$")
pattern_blanc = re.compile(r"^\s*$")
pattern_listeVide = re.compile(r"^\s*'\s*'\s*$")

pattern_ligne=re.compile(r'^\s*(?P<ident>[^=:]*)\s*[:=]\s*(?P<reste>.*)$')

pattern_variables=re.compile (r"^\s*(?P<ident>VARIABLES POUR LES SORTIES GRAPHIQUES)\s*[:=]\s*(?P<valeur>\w(,\w)*)\s*(?P<reste>.*)$")

# Attention aux listes de flottants
pattern_liste=re.compile(r'^\s*(?P<valeur>[+-.\w]+(\s*;\s*[+-.\w]+)+)\s*(?P<reste>.*)$')
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
   from aideAuxConvertisseurs import DicoEficasToCas, ListeSupprimeCasToEficas
   from aideAuxConvertisseurs import ListeCalculCasToEficas, DicoAvecMajuscules
   from enumDicoTelemac       import DicoEnumCasEn
except :
   pass

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
      from Accas import A_BLOC, A_FACT, A_SIMP
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
 

          finLigne=ligne
          while finLigne != "" :
              #print finLigne
              if pattern_comment_slash.match(finLigne) : finLigne=""; continue
              valeur=""
              if pattern_variables.match(finLigne) :
                 m=pattern_variables.match(finLigne)
                 valeur=m.group('valeur')
                 simp=self.traiteIdent(m.group('ident'))
                 finLigne=m.group('reste')
                 self.dictSimp[simp]=valeur
                 continue

              m=pattern_ligne.match(finLigne)
              if m == None : 
                 #print "________________________________________________"
                 print 'pb avec ****', finLigne , '**** dans ', ligne
                 #print "________________________________________________"
                 break
      
              simp=self.traiteIdent(m.group('ident'))
              finLigne=m.group('reste')

              # attention, l ordre des if est important
              if pattern_liste.match(finLigne) :
                 m=pattern_liste.match(finLigne)
              elif pattern_texteQuote.match(finLigne) :
                 m=pattern_texteQuote.match(finLigne)
              elif pattern_flottant.match(finLigne) : 
                 m=pattern_flottant.match(finLigne)
              elif pattern_texteVide.match(finLigne):
                 m=pattern_texteVide.match(finLigne)
              elif pattern_texteSimple.match(finLigne):
                 m=pattern_texteSimple.match(finLigne)
              else :
                 #print "________________________________________________"
                 print 'pb avec ****', finLigne , '**** dans ', ligne
                 print "non match"
                 #print "________________________________________________"
                 break
              
              valeur=m.group('valeur')
              if pattern_blanc.match(valeur) : valeur=None

              if pattern_flottant.match(finLigne) : 
                 valeur=re.sub("d","e",valeur)
                 valeur=re.sub("D","E",valeur)

              if pattern_liste.match(finLigne):
                 valeur=valeur.split(";")

              finLigne=m.group('reste')
              #print simp 
              #print valeur
              #print finLigne
              self.dictSimp[simp]=valeur
      
      if 'Title' not in self.dictSimp.keys() and 'Titre' not in self.dictSimp.keys():
          import os
          self.dictSimp['Titre']=os.path.basename(self.filename)
      
      dicoParMC={}
      for simp in self.dictSimp.keys():
          #print simp, " : ", self.dictSimp[simp]
           
          if simp in TELEMACParser.__dict__.keys() : apply(TELEMACParser.__dict__[simp],(self,))

      for simp in self.dictSimp.keys():
          if simp in ListeSupprimeCasToEficas: continue
          if simp not in self.dicoInverseFrancais.keys() : 
             print "************"
             print "pb avec dans dicoInverseFrancais", simp,'------'
             print "************"
             #print poum
             continue
          listeGenea=self.dicoInverseFrancais[simp]
          listeGeneaReverse=[]
          for (u,v) in listeGenea : 
              if isinstance(v,A_BLOC.BLOC): continue
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
          #print "----------- traitement de " , k
          self.textePy += self.dicoFrancaisAnglais[k] + "("
          self.traiteMC(dicoParMC[k])
          self.textePy += ");\n"
          #print "----------- " 
           
              
      #print self.textePy
      return self.textePy 

   #----------------------------------------
   def redecoupeSimp(self,simp): 
   # traite les - dans les identifants python
   # les remplace par des _
   #----------------------------------------
      # replace('-','_')  uniquement dans les identifiants
      while simp.find('-') > 0 : 
        ind=simp.find('-')
        if ind==len(simp)-1 : break
        simp=simp[0:ind]+'_'+simp[ind+1].upper()+simp[ind+2:]
      return simp

   #----------------------------------------
   def traiteIdent(self,listeIdent):
   # Recree l identifiant Python
   #----------------------------------------
          while listeIdent[-1] == " " or listeIdent[-1] == '\t' : listeIdent=listeIdent[0:-1]
          while listeIdent[0]  == " " or listeIdent[0]  == '\t' : listeIdent=listeIdent[1:]
          
          listeIdent=re.sub("'"," ",listeIdent)
          motsInIdent=string.split(listeIdent,' ')
          simp=""
          for mot in motsInIdent:
              if re.compile(r"^\s*$").match(mot) : continue
              mot=mot.replace('_','__')
              simp=simp+mot[0].upper() +mot[1:].lower()+'_'

          simp=simp[0:-1]
          while simp[-1] == " " : simp=simp[0:-1]
          if simp.find('-') > 0 : simp=self.redecoupeSimp(simp)

          return simp


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
           else : print "%%%%%%%%%%%\n", "pb conversion type pour", k, obj, "\n%%%%%%%%%%%"

           #print "_____________"

   def convertFACT(self,obj,nom,valeur):
       if nom in TELEMACParser.__dict__.keys() : 
          apply(TELEMACParser.__dict__[nom],(self,))
          return
       self.textePy +=  nom + "=_F( "
       self.traiteMC(valeur)
       self.textePy += '),\n'


   def convertBLOC(self,obj,nom,valeur):
       print "BLOC "
       print nom

   def convertSIMP(self,obj,nom,valeur):
       if nom in ("Prescribed_Flowrates", "Prescribed_Velocities", "Prescribed_Elevations" ): return
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
          if nom in DicoEnumCasEn.keys(): 
             #print "est dans le dico des enum, valeur simple"
             try    : 
               valeur=DicoEnumCasEn[nom][valeur]
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
                   print "pb avec le type de ", obj.nom, obj.type, 'et la valeur ', valeur

          if 'Fichier' in obj.type or 'TXM' in obj.type or 'Repertoire' in obj.type :
              valeur=str(valeur)
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
          if pattern_listeVide.match(valeur) :
             self.textePy += nom + "= None,"
             return
          while valeur[-1] == " " or  valeur[-1]=="'" : valeur=valeur[0:-1]
          while valeur[0]  == " " or  valeur[-0]=="'" : valeur=valeur[1:]

          if   ";" in valeur : valeur=valeur.split(';')
          elif "," in valeur : valeur=valeur.split(',')

          if valeur == None : return
          newVal=[]
          for v in valeur :
            try :    v=eval(v,{})
            except : pass
            if nom in DicoEnumCasEn.keys():
               #print "est dans le dico des enum, valeurs multiples"
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
 
   def decoupeListe(self,valeurs,label):
      #print "decoupeListe"
      #print valeurs
      i=0
      for prefixe in ('_U_And_V','_H'):
          labelComplet=label+prefixe
          valeur=valeurs[i]
          try    : valeur=eval(valeur,{})
          except : pass
          if tr(label) in DicoEnumCasEn.keys(): 
             try    : valeur=DicoEnumCasEn[tr(label)][valeur]
             except : pass
          self.dictSimp[labelComplet]=valeur
          i=i+1
      if len(valeurs)==2 : return
      for prefixe in ('_K_And_Epsilon','_Tracers'):
          labelComplet=label+prefixe
          valeur=valeurs[i]
          try    : valeur=eval(valeur,{})
          except : pass
          if tr(label) in DicoEnumCasEn.keys(): 
             try    : valeur=DicoEnumCasEn[tr(label)][valeur]
             except : pass
          self.dictSimp[labelComplet]=valeur
          i=i+1
      
   def Option_De_Supg(self):
       #print "ds Option_De_Supg"
       self.decoupeListe( self.dictSimp["Option_De_Supg"],"Option_De_Supg")
       del self.dictSimp["Option_De_Supg"]

   def Forme_De_La_Convection(self):
       self.decoupeListe( self.dictSimp["Forme_De_La_Convection"],"Forme_De_La_Convection")
       valeurs=self.dictSimp["Forme_De_La_Convection"]
       del self.dictSimp["Forme_De_La_Convection"]
       self.dictSimp['Convection_De_U_Et_V']=True
       self.dictSimp['Convection_De_H']=True
       if len(valeurs)==2 : return
       self.dictSimp['Convection_De_K_Et_Epsilon']=True
       self.dictSimp['Convection_Des_Traceurs']=True

   def Discretisations_En_Espace(self):
       self.decoupeListe( self.dictSimp["Discretisations_En_Espace"],"Discretisations_En_Espace")
       del self.dictSimp["Discretisations_En_Espace"]
       
   def Date_De_L_Origine_Des_Temps (self):
       valeurs=self.dictSimp["Date_De_L_Origine_Des_Temps"]
       self.dictSimp['Annee']=valeurs[0]
       self.dictSimp['Mois']=valeurs[1]
       self.dictSimp['Jour']=valeurs[2]
       del  self.dictSimp["Date_De_L_Origine_Des_Temps"]
       
   
   def Heure_De_L_Origine_Des_Temps (self):
       valeurs=self.dictSimp["Heure_De_L_Origine_Des_Temps"]
       self.dictSimp['Heure']=valeurs[0]
       self.dictSimp['Minute']=valeurs[1]
       self.dictSimp['Seconde']=valeurs[2]
       del  self.dictSimp["Heure_De_L_Origine_Des_Temps"]

   def Liquid_Boundaries(self):
       #print 'Liquid Boundaries'
       texte_Boundaries="Liquid_Boundaries=( "
       premier=0
       if 'Prescribed_Elevations' in self.dictSimp.keys(): 
           valeurs=self.dictSimp["Prescribed_Elevations"]
       elif 'Cotes_Imposees' in self.dictSimp.keys(): 
           valeurs=self.dictSimp["Cotes_Imposees"]
       else : valeurs=()
       #print valeurs
       for e in range(len(valeurs)):
          if valeurs[e] == "" or valeurs[e] == "\n" : continue
          if eval(valeurs[e],{})==0 : continue
          if not premier : premier=1
          texte_Boundaries += "_F(Type_Condition = 'Prescribed Elevations',\n"
          texte_Boundaries += "Prescribed_Elevations = " + str(valeurs[e]) + "),\n"
               
       if 'Prescribed_Flowrates' in self.dictSimp.keys(): 
          valeurs=self.dictSimp["Prescribed_Flowrates"]
       elif 'Debits_Imposes' in self.dictSimp.keys(): 
          valeurs=self.dictSimp["Debits_Imposes"]
       else : valeurs=()
       #print valeurs
       for e in range(len(valeurs)):
          if valeurs[e] == "" or valeurs[e] == "\n" : continue
          if eval(valeurs[e],{})==0 : continue
          if not premier : premier=1
          texte_Boundaries += "_F(Type_Condition = 'Prescribed Flowrates',\n"
          texte_Boundaries += "Prescribed_Flowrates = " + str(valeurs[e]) + "),\n"
               
       if 'Prescribed_Velocity' in self.dictSimp.keys(): 
           valeurs=self.dictSimp["Prescribed_Velocity"]
       elif 'Vitesses_Imposees' in self.dictSimp.keys(): 
           valeurs=self.dictSimp["Vitesses_Imposees"]
       else : valeurs=()
       #print valeurs
       for e in range(len(valeurs)):
          if valeurs[e] == "" or valeurs[e] == "\n" : continue
          if eval(valeurs[e],{})==0 : continue
          if not premier : premier=1
          texte_Boundaries += "_F(Type_Condition = 'Prescribed Velocity',\n"
          texte_Boundaries += "Prescribed_Velocity = " + str(valeurs[e]) + "),\n"
       if premier :  texte_Boundaries +="),\n"
       else : texte_Boundaries="" ; print "pb texte_Boundaries "
       self.textePy += texte_Boundaries
      
