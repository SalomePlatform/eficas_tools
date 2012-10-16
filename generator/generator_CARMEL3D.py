# -*- coding: utf-8 -*-
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
"""Ce module contient le plugin generateur de fichier au format  Code_Carmel3D pour EFICAS.
"""

import traceback
import types,string,re,os

from generator_python import PythonGenerator

# dictionnaire contenant la liste des materiaux :
#     cle = nom du materiau 
#     valeur = nature du materiau ; correspond a un sous bloc du bloc MATERIALS du fichier de parametres Carmel3D
#
# les materiaux sont : 
#  - des materiaux de reference connus fournis par THEMIS,
#  - ou des materiaux generiques theoriques 
#
#
dictNatureMaterRef={"DIELECTRIC":"DIELECTRIC",
                    "CONDUCTOR":"CONDUCTOR",
                    "ZSURFACIC":"ZSURFACIC",
                    "ZINSULATOR":"ZINSULATOR",
                    "NILMAT":"NILMAT",
                    "EM_ISOTROPIC":"EMISO",
                    "EM_ANISOTROPIC":"EMANISO",
                    "ACIER_CIMBLOT":"CONDUCTOR", 
                    "ACIER_Noir":"CONDUCTOR", 
                    "ACIER_PE":"CONDUCTOR", 
                    "ALU":"CONDUCTOR", 
                    "BRONZE":"CONDUCTOR", 
                    "CUIVRE":"CONDUCTOR", 
                    "FERRITE_Mn_Zn":"CONDUCTOR", 
                    "FERRITE_Ni_Zn":"CONDUCTOR", 
                    "INCONEL600":"CONDUCTOR", 
                    "POTASSE":"CONDUCTOR",
                    "M6X2ISO1":"CONDUCTOR", 
                    "AIR":"DIELECTRIC", 
                    "FERRITEB30":"DIELECTRIC", 
                    "E24":"DIELECTRIC",
                    "FEV470":"DIELECTRIC",
                    "FEV600":"DIELECTRIC",
                    "FEV800":"DIELECTRIC",
                    "FEV1000":"DIELECTRIC",
                    "HA600":"DIELECTRIC",
                    "M600_65":"DIELECTRIC",
                    "M6X":"EMANISO",
                    "M6X_lineaire":"EMANISO",
                    "M6X_homog":"EMANISO"
                    }

# Groupes de mailles dont les types sont définis par des préfixes dans leur nom
usePrefix = False # les noms ont des préfixes (True) ou non (False)
# liste des préfixes des groupes de mailles, sans le caractère _ séparant le préfixe du reste du nom
# Ce préfixe (et caractère _) doivent être supprimés dans le fichier .phys
listePrefixesGroupeMaille = ("DIEL","NOCOND","COND","CURRENT","EPORT","HPORT","TOPO","PB_MOBILE","NILMAT",
                         "VCUT","VCUTN","EWALL","HWALL","GAMMAJ","PERIODIC","APERIODIC",
                         "HPROBE","EPROBE","BFLUX","BFLUXN","JFLUX","JFLUXN",
                         "PORT_OMEGA","POST_PHI","PB_GRID",
                         "SCUTE","SCUTN","ZS","ZJ","ZT")
# liste des préfixes des groupes de mailles, sans le séparateur, par type de bloc du fichier PHYS sous la forme d'un dictionnaire
dictPrefixesGroupeMaille = {'DIELECTRIC':('DIEL','NOCOND'), 
                                             'CONDUCTOR':('COND',), 
                                             'STRANDED_INDUCTOR':('CURRENT', ), 
                                             'EPORT':('EPORT', ), 
                                             'HPORT':('HPORT', ), 
                                             'ZSURFACIC':('ZS', ), 
                                             'ZINSULATOR':('ZJ', ), 
                                             'NILMAT':('NILMAT', )}
# séparateur entre le préfixe et le reste du nom du groupe de maille
sepNomGroupeMaille = '_'

def entryPoint():
   """
      Retourne les informations necessaires pour le chargeur de plugins
      Ces informations sont retournees dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'CARMEL3D',
        # La factory pour creer une instance du plugin
          'factory' : CARMEL3DGenerator,
          }


class CARMEL3DGenerator(PythonGenerator):
   """
      Ce generateur parcourt un objet de type JDC et produit
      un texte au format eficas et 
      un texte au format attendu par le code Code_Carmel3D (fichier '.PHYS') 

   """
   # Les extensions de fichier permis?
   extensions=('.comm',)

#----------------------------------------------------------------------------------------
   def gener(self,obj,format='brut',config=None):
       
      self.initDico()
      
      # Cette instruction genere le contenu du fichier de commandes (persistance)
      self.text=PythonGenerator.gener(self,obj,format)

      if self.debug:
         print "self.text=",self.text

      # Cette instruction genere le contenu du fichier de parametres pour le code Carmel3D
      # si le jdc est valide (sinon cela n a pas de sens)
      if obj.isvalid() : 
           # constitution du bloc VERSION du fichier PHYS (existe toujours)
           self.generBLOC_VERSION(obj)

           # constitution du bloc MATERIALS du fichier PHYS (existe toujours)
           self.generBLOC_MATERIALS()

           # constitution du bloc SOURCES du fichier PHYS (existe toujours)
           self.generBLOC_SOURCES()

#      print "texte carmel3d :\n",self.texteCarmel3D
#      print "dictMaterDielectric : ",self.dictMaterDielectric
      if self.debug:
         print "dictMaterConductor : ",self.dictMaterConductor
      
      return self.text


#----------------------------------------------------------------------------------------
# initialisations
#----------------------------------------------------------------------------------------
   
   def initDico(self) :
 
      self.texteCarmel3D=""
      self.debug = False # affichage de messages pour déboguage (.true.) ou non
      self.dicoEtapeCourant=None
      self.dicoMCFACTCourant=None
      self.dicoCourant=None
      self.dictGroupesMaillage = {'ordreMateriauxJdC':[], 'ordreSourcesJdC':[]} # association des noms de groupes de maillage avec les noms de matériaux ou de sources, en sauvegardant l'ordre du JdC en séparant les groupes associés à des matériaux de ceux associés à des sources
      self.dictMaterConductor={}
      self.dictMaterDielectric={}
      self.dictMaterZsurfacic={}
      self.dictMaterEmIso={}
      self.dictMaterEmAnIso={}
      self.dictMaterNilmat={}
      self.dictMaterZinsulator={}
      self.dictSourceStInd={}
      self.dictSourceEport={}
      self.dictSourceHport={}


#----------------------------------------------------------------------------------------
# ecriture
#----------------------------------------------------------------------------------------

   def writeDefault(self,fn) :
        """Ecrit le fichier de parametres (PHYS) pour le code Carmel3D"""
        if self.debug: print "ecriture fic phys"
        filePHYS = fn[:fn.rfind(".")] + '.phys'
        f = open( str(filePHYS), 'wb')
        f.write( self.texteCarmel3D)
        f.close()

#----------------------------------------------------------------------------------------
#  analyse de chaque noeud de l'arbre 
#----------------------------------------------------------------------------------------

   def generMCSIMP(self,obj) :
        """recuperation de l objet MCSIMP"""
        if self.debug: print "MCSIMP", obj.nom, "  ", obj.valeur
        s=PythonGenerator.generMCSIMP(self,obj)
        self.dicoCourant[obj.nom]=obj.valeurFormatee
        return s

  
#----------------------------------------------------------------------------------------
   def generMCFACT(self,obj) :
        """recuperation de l objet MCFACT"""
        dico={}
        self.dicoMCFACTCourant=dico
        self.dicoCourant=self.dicoMCFACTCourant
        s=PythonGenerator.generMCFACT(self,obj)
        self.dicoEtapeCourant[obj.nom]=self.dicoMCFACTCourant
        self.dicoMCFACTCourant=None
        self.dicoCourant=self.dicoEtapeCourant
        return s
  
#----------------------------------------------------------------------------------------
   def generPROC_ETAPE(self,obj):
        """analyse des PROC du catalogue  ( VERSION )"""
        dico={}
        self.dicoEtapeCourant=dico
        self.dicoCourant=self.dicoEtapeCourant
        s=PythonGenerator.generPROC_ETAPE(self,obj)
        obj.valeur=self.dicoEtapeCourant
        if self.debug: print "PROC_ETAPE", obj.nom, "  ", obj.valeur
        s=PythonGenerator.generPROC_ETAPE(self,obj)
        return s
  
#----------------------------------------------------------------------------------------
   def generETAPE(self,obj):
        """analyse des OPER du catalogue"""
        dico={}
        self.dicoEtapeCourant=dico
        self.dicoCourant=self.dicoEtapeCourant
        s=PythonGenerator.generETAPE(self,obj)
        obj.valeur=self.dicoEtapeCourant
        if self.debug: print "ETAPE :obj.nom =", obj.nom, " , obj.valeur= ", obj.valeur
        if obj.nom=="MESHGROUP" : self.generMESHGROUP(obj)
        if obj.nom=="MATERIAL" : self.generMATERIAL(obj)
        if obj.nom=="SOURCE" : self.generSOURCE(obj)
        s=PythonGenerator.generETAPE(self,obj)
        return s

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
   def generMESHGROUP(self,obj):
        """preparation de la ligne NAME referencant le groupe de mailles 
            associe le groupe de mailles au materiau ou a la source utilisateur
            on sauvegarde aussi les noms des groupes de maillage
        """
        try:
            if usePrefix:
                nomGroupeMaillage = self.nomReelGroupeMaillage(obj.get_sdname()) # nom du groupe de maillage, i.e. nom du concept, avec préfixes enlevés
            else:
                nomGroupeMaillage = obj.get_sdname() # nom du groupe de maillage, i.e. nom du concept
            # test: un et un seul nom de matériau ou source doit être associé à ce groupe de maillage, via les clés MATERIAL et SOURCE, respectivement.
            # test sur un seul attribut, non pertinent car il peut y en avoir plusieurs.
            #assert len(obj.valeur.keys())==1,u"Un et un seul nom de matériau ou source doit être associé à ce groupe du maillage :"+nomGroupeMaillage
            #
            # on utilise le fait que obj.valeur est un dictionnaire
            if self.debug: print "obj.valeur.keys()=", obj.valeur.keys()
            if 'MATERIAL' in obj.valeur.keys() and 'SOURCE' in obj.valeur.keys(): # test d'erreur lors de présence de matériau et source à la fois
                raise ValueError, u"ce groupe de maillage ("+nomGroupeMaillage+") est associé à au moins un matériau et au moins une source."
            # association à un matériau
            if 'MATERIAL' in obj.valeur.keys():
                self.dictGroupesMaillage[nomGroupeMaillage] = obj.valeur['MATERIAL'].nom # sauvegarde de l'association entre ce groupe de maillage et un matériau ou source, par son nom, i.e. nom du concept du matériau ou de la source
                self.dictGroupesMaillage['ordreMateriauxJdC'].append(nomGroupeMaillage) # sauvegarde du nom du groupe de maillage associé à un matériau, dans l'ordre du JdC
            # association à une source
            elif 'SOURCE' in obj.valeur.keys():
                self.dictGroupesMaillage[nomGroupeMaillage] = obj.valeur['SOURCE'].nom # sauvegarde de l'association entre ce groupe de maillage et un matériau ou source, par son nom, i.e. nom du concept du matériau ou de la source
                self.dictGroupesMaillage['ordreSourcesJdC'].append(nomGroupeMaillage) # sauvegarde du nom du groupe de maillage associé à une source, dans l'ordre du JdC
            # erreur ni matériau ni source associée
            else:
                raise ValueError, u"ce groupe de maillage ("+nomGroupeMaillage+") n'est associé à aucun matériau ou source."
            if self.debug:
                print "self.dictGroupesMaillage=",self.dictGroupesMaillage
        except:
            pass


   def generMATERIAL(self,obj):
        """préparation du bloc correspondant à un matériau du fichier PHYS"""
        texte=""
        if self.debug: print "gener material obj valeur = ", obj.valeur
        try :
            nature=dictNatureMaterRef[obj.valeur['MAT_REF']]
            if nature=="CONDUCTOR" : self.generMATERIAL_CONDUCTOR(obj)
            if nature=="DIELECTRIC" : self.generMATERIAL_DIELECTRIC(obj)
            if nature=="ZSURFACIC" : self.generMATERIAL_ZSURFACIC(obj)
            if nature=="EMISO" : self.generMATERIAL_EMISO(obj)
            if nature=="EMANISO" : self.generMATERIAL_EMANISO(obj)
            if nature=="NILMAT" : self.generMATERIAL_NILMAT(obj)
            if nature=="ZINSULATOR" : self.generMATERIAL_ZINSULATOR(obj)
        except:
            pass

   def generMATERIAL_CONDUCTOR(self,obj):
      # preparation du sous bloc CONDUCTOR
      texte=""
      # print "__________cond_________________"
      # parcours des proprietes du sous bloc CONDUCTOR
      for keyN1 in obj.valeur :
       if keyN1=='MAT_REF': continue
      #     print "keyN1=", keyN1
#      print obj.valeur[keyN1]['TYPE_LAW']
       texte+="         ["+keyN1+"\n"
      # loi lineaire reelle
       if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_REAL' :
          texte+="            LAW LINEAR\n"
          texte+="            HOMOGENEOUS "+str(obj.valeur[keyN1]["HOMOGENEOUS"])+"\n"
          texte+="            ISOTROPIC "+str(obj.valeur[keyN1]["ISOTROPIC"])+"\n"
          texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_REAL"])+" 0\n"
      # loi lineaire complexe
          if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_COMPLEX' :
   #            print "si avec linear complex"
            texte+="            LAW LINEAR\n"
            texte+="            HOMOGENEOUS "+str(obj.valeur[keyN1]["HOMOGENEOUS"])+"\n"
            texte+="            ISOTROPIC "+str(obj.valeur[keyN1]["ISOTROPIC"])+"\n"
            texte+="            VALUE "
  #               print "nbre a formater : ",obj.valeur[keyN1]["VALUE_COMPLEX"]
            chC= self.formateCOMPLEX(obj.valeur[keyN1]["VALUE_COMPLEX"])
            texte+= chC+"\n"
      # loi non lineaire de nature spline, Marrocco ou Marrocco et Saturation
      #  seuls les reels sont pris en compte
       if obj.valeur[keyN1]['TYPE_LAW']=='NONLINEAR' :
          texte+="            LAW NONLINEAR\n"
          texte+="            HOMOGENEOUS "+str(obj.valeur[keyN1]["HOMOGENEOUS"])+"\n"
          texte+="            ISOTROPIC "+str(obj.valeur[keyN1]["ISOTROPIC"])+"\n"
          texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE"])+" 0\n"
          texte+="            [NONLINEAR \n"
          texte+="                ISOTROPY TRUE\n"
          texte+="                NATURE "+str(obj.valeur[keyN1]['NATURE'])+"\n"
          for keyN2 in obj.valeur[keyN1] :
              if keyN2 != 'TYPE_LAW' and keyN2 != 'VALUE' and keyN2 != 'NATURE' :
                   texte+="                "+keyN2+" "+str(obj.valeur[keyN1][keyN2])+"\n"
          texte+="            ]"+"\n"
          texte+="         ]"+"\n"

       self.dictMaterConductor[obj.get_sdname()]=texte
     #  self.dictMaterConductor[obj.get_sdname()]=[texte,]
#       print texte
   

   def generMATERIAL_DIELECTRIC(self,obj):
      # preparation du sous bloc DIELECTRIC
       texte=""
      # print "______________nocond_____________"
      # parcours des proprietes du sous bloc DIELECTRIC
       for keyN1 in obj.valeur :
           if keyN1=='MAT_REF': continue
              # print "type loi = ", obj.valeur[keyN1]['TYPE_LAW']
          # debut du sous bloc de propriete du DIELECTRIC
           texte+="         ["+keyN1+"\n"
          # loi lineaire reelle
           if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_REAL' :
              texte+="            LAW LINEAR\n"
              texte+="            HOMOGENEOUS "+str(obj.valeur[keyN1]["HOMOGENEOUS"])+"\n"
              texte+="            ISOTROPIC "+str(obj.valeur[keyN1]["ISOTROPIC"])+"\n"
              texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_REAL"])+" 0\n"
          # loi lineaire complexe
           if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_COMPLEX' :
                 texte+="            LAW LINEAR\n"
                 texte+="            HOMOGENEOUS "+str(obj.valeur[keyN1]["HOMOGENEOUS"])+"\n"
                 texte+="            ISOTROPIC "+str(obj.valeur[keyN1]["ISOTROPIC"])+"\n"
                 texte+="            VALUE "
                 chC= self.formateCOMPLEX(obj.valeur[keyN1]["VALUE_COMPLEX"])
                 texte+= chC+"\n"
                  
          # loi non lineaire de nature spline, Marrocco ou Marrocco et Saturation
          #  seuls les reels sont pris en compte
           if obj.valeur[keyN1]['TYPE_LAW']=='NONLINEAR' :
                texte+="            LAW NONLINEAR\n"
                texte+="            HOMOGENEOUS "+str(obj.valeur[keyN1]["HOMOGENEOUS"])+"\n"
                texte+="            ISOTROPIC "+str(obj.valeur[keyN1]["ISOTROPIC"])+"\n"
                texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE"])+" 0\n"
                texte+="            [NONLINEAR \n"
                texte+="                ISOTROPY TRUE\n"
                texte+="                NATURE "+str(obj.valeur[keyN1]['NATURE'])+"\n"
                for keyN2 in obj.valeur[keyN1] :
                    if keyN2 != 'TYPE_LAW' and keyN2 != 'VALUE' and keyN2 != 'NATURE' :
                       texte+="                "+keyN2+" "+str(obj.valeur[keyN1][keyN2])+"\n"
                texte+="            ]"+"\n"
           # fin du sous bloc de propriete
           texte+="         ]"+"\n"
        #print "texte = ", texte    
       self.dictMaterDielectric[obj.get_sdname()]=texte
 
   def generMATERIAL_ZSURFACIC(self,obj):
      # preparation du sous bloc ZSURFACIC
       texte=""
       #print "______________zsurf_____________"
       for keyN1 in obj.valeur :
           if keyN1=='MAT_REF': continue
      #         print "keyN1=", keyN1
    #      print obj.valeur[keyN1]['TYPE_LAW']
           texte+="         ["+keyN1+"\n"
          # loi lineaire reelle
           if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_REAL' :
              texte+="            LAW LINEAR\n"
              texte+="            HOMOGENEOUS "+str(obj.valeur[keyN1]["HOMOGENEOUS"])+"\n"
              texte+="            ISOTROPIC "+str(obj.valeur[keyN1]["ISOTROPIC"])+"\n"
              texte+="            VALUE COMPLEX "+str(obj.valeur[keyN1]["VALUE_REAL"])+" 0\n"
          # loi lineaire complexe
           if obj.valeur[keyN1]['TYPE_LAW']=='LINEAR_COMPLEX' :
                texte+="            LAW LINEAR\n"
                texte+="            HOMOGENEOUS "+str(obj.valeur[keyN1]["HOMOGENEOUS"])+"\n"
                texte+="            ISOTROPIC "+str(obj.valeur[keyN1]["ISOTROPIC"])+"\n"
                texte+="            VALUE "
                chC= self.formateCOMPLEX(obj.valeur[keyN1]["VALUE_COMPLEX"])
                texte+= chC+"\n"             
           texte+="         ]"+"\n"
       self.dictMaterZsurfacic[obj.get_sdname()]=texte

   def generMATERIAL_EMISO(self,obj):
        """preparation du sous bloc EM_ISOTROPIC_FILES.
        Les fichiers sont indiqués par le chemin indiqué dans Eficas, i.e. le chemin absolu par défaut
        """
        texte ="        CONDUCTIVITY MED "+str(obj.valeur["CONDUCTIVITY_File"])+"\n"
        texte+="        PERMEABILITY MED "+str(obj.valeur["PERMEABILITY_File"])+"\n"
        # Possibilité de forcer le chemin relatif (nom de fichier seulement) plutôt que le chemin absolu par défaut
        #from os.path import basename
        #texte ="        CONDUCTIVITY MED "+basename(str(obj.valeur["CONDUCTIVITY_File"]))+"\n"
        #texte+="        PERMEABILITY MED "+basename(str(obj.valeur["PERMEABILITY_File"]))+"\n"
        #      print "obj get sdname= ", obj.get_sdname()
        #   if obj.get_sdname() in self.dictMaterEmIso.keys() :
        #    self.dictMaterEmIso[obj.get_sdname()].append(texte) 
        # else :
        self.dictMaterEmIso[obj.get_sdname()]=texte
  
   def generMATERIAL_EMANISO(self,obj):
        """preparation du sous bloc EM_ANISOTROPIC_FILES.
        Les fichiers sont indiqués par le chemin indiqué dans Eficas, i.e. le chemin absolu par défaut
        """
        texte ="        CONDUCTIVITY  "+str(obj.valeur["CONDUCTIVITY_File"])+"\n"
        texte+="        PERMEABILITY  "+str(obj.valeur["PERMEABILITY_File"])+"\n"
        # Possibilité de forcer le chemin relatif (nom de fichier seulement) plutôt que le chemin absolu par défaut
        #from os.path import basename
        #texte ="        CONDUCTIVITY  "+basename(str(obj.valeur["CONDUCTIVITY_File"]))+"\n"
        #texte+="        PERMEABILITY  "+basename(str(obj.valeur["PERMEABILITY_File"]))+"\n"
        #  print "obj get sdname= ", obj.get_sdname()
        #  if obj.get_sdname() in self.dictMaterEmAnIso.keys() :
        #    self.dictMaterEmAnIso[obj.get_sdname()].append(texte) 
        #  else :
        self.dictMaterEmAnIso[obj.get_sdname()]=texte
   
   def generMATERIAL_NILMAT(self,obj):
      # preparation du sous bloc NILMAT
       texte=""
       self.dictMaterNilmat[obj.get_sdname()]=texte
   
   def generMATERIAL_ZINSULATOR(self,obj):
        """"preparation du sous bloc ZINSULATOR"""
        texte=""
        self.dictMaterZinsulator[obj.get_sdname()]=texte

#-------------------------------------------------------------------

   def generSOURCE(self,obj):
        """preparation du bloc correspondant à une source du fichier PHYS"""
        if self.debug: print "gener source obj valeur = ", obj.valeur
        texte=""
        try :
            typesource=obj.valeur['TYPE_SOURCE']
            if typesource=="STRANDED_INDUCTOR" : self.generSOURCE_STRANDED_INDUCTOR(obj)
            if typesource=="HPORT" : self.generSOURCE_HPORT(obj)
            if typesource=="EPORT" : self.generSOURCE_EPORT(obj)
        except:
            pass

   def generSOURCE_STRANDED_INDUCTOR(self,obj):
        """preparation du sous bloc STRANDED_INDUCTOR"""
        texte=""
        try :
            texte+="        NTURNS "+ str(obj.valeur['NTURNS']) + "\n"
            texte+="        CURJ " + self.formateCOMPLEX(obj.valeur['CURJ']) + "\n"
            self.dictSourceStInd[obj.get_sdname()]=texte
            if self.debug: print texte
        except:
            pass

   def generSOURCE_HPORT(self,obj):
        """preparation du sous bloc HPORT"""
        texte=""
        try :
            texte+="        TYPE "+ str(obj.valeur['TYPE']) + "\n"
            texte+="        AMP " + self.formateCOMPLEX(obj.valeur['AMP']) + "\n"
            self.dictSourceHport[obj.get_sdname()]=texte
            if self.debug: print texte
        except:
            pass

   def generSOURCE_EPORT(self,obj):
        """preparation du sous bloc EPORT"""
        texte=""
        try :
            texte+="        TYPE "+ str(obj.valeur['TYPE']) + "\n"
            texte+="        AMP " + self.formateCOMPLEX(obj.valeur['AMP']) + "\n"
            self.dictSourceEport[obj.get_sdname()]=texte
            if self.debug: print texte
        except:
            pass

#---------------------------------------------------------------------------------------
# traitement fichier PHYS
#---------------------------------------------------------------------------------------

   def generBLOC_VERSION(self,obj) :
      # constitution du bloc VERSION du fichier PHYS
      # creation d une entite  VERSION ; elle sera du type PROC car decrit ainsi
      # dans le du catalogue
      version=obj.addentite('VERSION',pos=None)
      self.generPROC_ETAPE(obj.etapes[0])
      self.texteCarmel3D+="["+obj.etapes[0].nom+"\n"
      for cle in obj.etapes[0].valeur :
          self.texteCarmel3D+="   "+cle+" "+str(obj.etapes[0].valeur[cle])+"\n"
      self.texteCarmel3D+="]\n"
      # destruction de l entite creee 
      obj.suppentite(version)

#----------------------------------------------------------------------------------------
   def generBLOC_MATERIALS(self) :
        """Prepare une partie du contenu du fichier de parametres (PHYS) pour le code Carmel3D (bloc MATERIALS).
        Le bloc MATERIALS existe toujours ! 
        """
        if self.debug:
            print "cle dico materconductor : " , self.dictMaterConductor.keys()
            print "cle dico materdielectric : " , self.dictMaterDielectric.keys()
        # constitution du bloc MATERIALS du fichier PHYS
        self.texteCarmel3D+="[MATERIALS\n"
        # tri alphabétique de tous les groupes de maillage associés à des sources (plus nécessaire Code_Carmel3D V_2_3_1 et +, mais avant oui)
        nomsGroupesMaillage = self.dictGroupesMaillage['ordreMateriauxJdC'][:] # copie de l'original, qui est une liste
        nomsGroupesMaillage.sort() # tri alphabétique, avec les préfixes éventuels
        if self.debug:
            print u"noms groupes de mailles associés à des matériaux (ordre JdC puis tri)=", self.dictGroupesMaillage['ordreMateriauxJdC'], nomsGroupesMaillage
        # constitution du bloc CONDUCTOR du fichier PHYS si existe
        if self.dictMaterConductor != {} : self.creaBLOC_CONDUCTOR(nomsGroupesMaillage)
        # constitution du bloc DIELECTRIC du fichier PHYS si exixte
        if self.dictMaterDielectric != {} : self.creaBLOC_DIELECTRIC(nomsGroupesMaillage)
        # constitution du bloc ZSURFACIC du fichier PHYS si exixte
        if self.dictMaterZsurfacic != {} : self.creaBLOC_ZSURFACIC(nomsGroupesMaillage)
        # constitution du bloc NILMAT du fichier PHYS si exixte
        if self.dictMaterNilmat != {} : self.creaBLOC_NILMAT(nomsGroupesMaillage)
        # constitution du bloc ZINSULATOR du fichier PHYS si exixte
        if self.dictMaterZinsulator != {} : self.creaBLOC_ZINSULATOR(nomsGroupesMaillage)
        # Les blocs EM_ISOTROPIC_FILES et EM_ANISOTROPIC_FILES sont placés en dernier dans le fichier PHYS
        # constitution du bloc EM_ISOTROPIC_FILES du fichier PHYS si exixte
        if self.dictMaterEmIso != {} : self.creaBLOC_EMISO()
        # constitution du bloc EM_ANISOTROPIC_FILES du fichier PHYS si exixte
        if self.dictMaterEmAnIso != {} : self.creaBLOC_EMANISO()
        # fin du bloc MATERIALS du fichier PHYS
        self.texteCarmel3D+="]\n"  
    
   def creaBLOC_CONDUCTOR(self, nomsGroupesMaillage) :
        """Constitution du bloc CONDUCTOR du fichier PHYS"""
        typeBloc = 'CONDUCTOR' # initialisation du type de bloc
        dictProprietes = self.dictMaterConductor # initialisation du dictionnaire des propriétés du bloc
        if self.debug: print u'clés matériaux de type '+typeBloc+'=', dictProprietes.keys()
        for nom in nomsGroupesMaillage: # parcours des noms des groupes de maillage
            if self.dictGroupesMaillage[nom] in dictProprietes.keys(): # test si le nom du matériau associé est du bon type
                # ecriture du bloc complet
                self.texteCarmel3D+="     ["+typeBloc+"\n" # début de bloc
                if usePrefix:
                    nomReel = self.nomReelGroupeMaillage(nom, typeBloc)
                else:
                    nomReel = nom
                self.texteCarmel3D+="        NAME "+nomReel+"\n" # ecriture du nom (réel) du groupe du maillage
                self.texteCarmel3D+=  dictProprietes[self.dictGroupesMaillage[nom]] # ecriture des propriétés du type associé
                self.texteCarmel3D+="     ]\n" # fin de bloc

   def creaBLOC_DIELECTRIC(self, nomsGroupesMaillage) :
        """Constitution du bloc DIELECTRIC du fichier PHYS"""
        typeBloc = 'DIELECTRIC' # initialisation du type de bloc
        dictProprietes = self.dictMaterDielectric # initialisation du dictionnaire des propriétés du bloc
        if self.debug: print u'clés matériaux de type '+typeBloc+'=', dictProprietes.keys()
        for nom in nomsGroupesMaillage: # parcours des noms des groupes de maillage
            if self.dictGroupesMaillage[nom] in dictProprietes.keys(): # test si le nom du matériau associé est du bon type
                # ecriture du bloc complet
                self.texteCarmel3D+="     ["+typeBloc+"\n" # début de bloc
                self.texteCarmel3D+="        NAME "+nom+"\n" # ecriture du nom (réel) du groupe du maillage
                self.texteCarmel3D+=  dictProprietes[self.dictGroupesMaillage[nom]] # ecriture des propriétés du type associé
                self.texteCarmel3D+="     ]\n" # fin de bloc

   def creaBLOC_ZSURFACIC(self, nomsGroupesMaillage) :
        """Constitution du bloc ZSURFACIC du fichier PHYS"""
        typeBloc = 'ZSURFACIC' # initialisation du type de bloc
        dictProprietes = self.dictMaterZsurfacic # initialisation du dictionnaire des propriétés du bloc
        if self.debug: print u'clés matériaux de type '+typeBloc+'=', dictProprietes.keys()
        for nom in nomsGroupesMaillage: # parcours des noms des groupes de maillage
            if self.dictGroupesMaillage[nom] in dictProprietes.keys(): # test si le nom du matériau associé est du bon type
                # ecriture du bloc complet
                self.texteCarmel3D+="     ["+typeBloc+"\n" # début de bloc
                if usePrefix:
                    nomReel = self.nomReelGroupeMaillage(nom, typeBloc)
                else:
                    nomReel = nom
                self.texteCarmel3D+="        NAME "+nomReel+"\n" # ecriture du nom (réel) du groupe du maillage
                self.texteCarmel3D+=  dictProprietes[self.dictGroupesMaillage[nom]] # ecriture des propriétés du type associé
                self.texteCarmel3D+="     ]\n" # fin de bloc

   def creaBLOC_EMISO(self) :
        """constitution du bloc EM_ISOTROPIC_FILES du fichier PHYS"""
        for cle in self.dictMaterEmIso.keys():
            self.texteCarmel3D+="     [EM_ISOTROPIC_FILES\n"
            self.texteCarmel3D+= self.dictMaterEmIso[cle] 
            self.texteCarmel3D+="     ]\n"

   def creaBLOC_EMANISO(self) :
        """constitution du bloc EM_ANISOTROPIC_FILES du fichier PHYS"""
        for cle in self.dictMaterEmAnIso.keys():
            self.texteCarmel3D+="     [EM_ANISOTROPIC_FILES\n"
            self.texteCarmel3D+=  self.dictMaterEmAnIso[cle] 
            self.texteCarmel3D+="     ]\n"

   def creaBLOC_ZINSULATOR(self, nomsGroupesMaillage) :
        """Constitution du bloc ZINSULATOR du fichier PHYS"""
        typeBloc = 'ZINSULATOR' # initialisation du type de bloc
        dictProprietes = self.dictMaterZinsulator # initialisation du dictionnaire des propriétés du bloc
        if self.debug: print u'clés matériaux de type '+typeBloc+'=', dictProprietes.keys()
        for nom in nomsGroupesMaillage: # parcours des noms des groupes de maillage
            if self.dictGroupesMaillage[nom] in dictProprietes.keys(): # test si le nom du matériau associé est du bon type
                # ecriture du bloc complet
                self.texteCarmel3D+="     ["+typeBloc+"\n" # début de bloc
                if usePrefix:
                    nomReel = self.nomReelGroupeMaillage(nom, typeBloc)
                else:
                    nomReel = nom
                self.texteCarmel3D+="        NAME "+nomReel+"\n" # ecriture du nom (réel) du groupe du maillage
                self.texteCarmel3D+=  dictProprietes[self.dictGroupesMaillage[nom]] # ecriture des propriétés du type associé
                self.texteCarmel3D+="     ]\n" # fin de bloc

   def creaBLOC_NILMAT(self, nomsGroupesMaillage) :
        """Constitution du bloc NILMAT du fichier PHYS"""
        typeBloc = 'NILMAT' # initialisation du type de bloc
        dictProprietes = self.dictMaterNilmat # initialisation du dictionnaire des propriétés du bloc
        if self.debug: print u'clés matériaux de type '+typeBloc+'=', dictProprietes.keys()
        for nom in nomsGroupesMaillage: # parcours des noms des groupes de maillage
            if self.dictGroupesMaillage[nom] in dictProprietes.keys(): # test si le nom du matériau associé est du bon type
                # ecriture du bloc complet
                self.texteCarmel3D+="     ["+typeBloc+"\n" # début de bloc
                if usePrefix:
                    nomReel = self.nomReelGroupeMaillage(nom, typeBloc)
                else:
                    nomReel = nom
                self.texteCarmel3D+="        NAME "+nomReel+"\n" # ecriture du nom (réel) du groupe du maillage
                self.texteCarmel3D+=  dictProprietes[self.dictGroupesMaillage[nom]] # ecriture des propriétés du type associé
                self.texteCarmel3D+="     ]\n" # fin de bloc

#----------------------------------------------------------------------------------------
   def generBLOC_SOURCES(self):
        """constitution du bloc SOURCES du fichier PHYS"""
        self.texteCarmel3D+="[SOURCES\n"
        # tri alphabétique de tous les groupes de maillage associés à des sources
        nomsGroupesMaillage = self.dictGroupesMaillage['ordreSourcesJdC'][:] # copie de l'original, qui est une liste
        nomsGroupesMaillage.sort() # tri alphabétique, avec les préfixes éventuels
        if self.debug:
            print u'noms groupes de mailles associés à des sources (ordre JdC puis tri)=', self.dictGroupesMaillage['ordreSourcesJdC'], nomsGroupesMaillage
        if self.dictSourceStInd != {}: self.creaBLOC_STRANDED_INDUCTOR(nomsGroupesMaillage)
        if self.dictSourceEport != {}: self.creaBLOC_EPORT(nomsGroupesMaillage)
        if self.dictSourceHport != {}: self.creaBLOC_HPORT(nomsGroupesMaillage)
        # fin du bloc SOURCES du fichier PHYS
        self.texteCarmel3D+="]\n"


   def creaBLOC_STRANDED_INDUCTOR(self, nomsGroupesMaillage) :
        """constitution du bloc STRANDED_INDUCTOR du fichier PHYS"""
        if self.debug: print u'clés sources STRANDED_INDUCTOR=', self.dictSourceStInd.keys()
        typeBloc = 'STRANDED_INDUCTOR'
        for nom in nomsGroupesMaillage: # parcours des noms des groupes de maillage
            if self.dictGroupesMaillage[nom] in self.dictSourceStInd.keys(): # test si le nom de la source associée est un inducteur bobiné
                # ecriture du bloc de l'inducteur bobiné
                self.texteCarmel3D+="     [STRANDED_INDUCTOR\n" # début de bloc
                self.texteCarmel3D+="        NAME "+nom+"\n" # ecriture du nom (réel) du groupe du maillage
                self.texteCarmel3D+=  self.dictSourceStInd[self.dictGroupesMaillage[nom]] # ecriture des propriétés de l'inducteur bobiné
                self.texteCarmel3D+="     ]\n" # fin de bloc
                
   def creaBLOC_EPORT(self, nomsGroupesMaillage) :
        """constitution du bloc EPORT du fichier PHYS"""
        if self.debug: print u'clés sources EPORT=', self.dictSourceEport.keys()
        typeBloc = 'EPORT'
        for nom in nomsGroupesMaillage: # parcours des noms des groupes de maillage
            if self.dictGroupesMaillage[nom] in self.dictSourceEport.keys(): # test si le nom de la source associée est un port électrique
                # ecriture du bloc du port électrique
                self.texteCarmel3D+="     [EPORT\n" # début de bloc
                if usePrefix:
                    nomReel = self.nomReelGroupeMaillage(nom, typeBloc)
                else:
                    nomReel = nom
                self.texteCarmel3D+="        NAME "+nomReel+"\n" # ecriture du nom (réel) du groupe du maillage
                self.texteCarmel3D+=  self.dictSourceEport[self.dictGroupesMaillage[nom]] # ecriture des propriétés du port électrique
                self.texteCarmel3D+="     ]\n" # fin de bloc

   def creaBLOC_HPORT(self, nomsGroupesMaillage) :
        """constitution du bloc HPORT du fichier PHYS"""
        if self.debug: print u'clés sources HPORT=', self.dictSourceHport.keys()
        typeBloc = 'HPORT'
        for nom in nomsGroupesMaillage: # parcours des noms des groupes de maillage
            if self.dictGroupesMaillage[nom] in self.dictSourceHport.keys(): # test si le nom de la source associée est un port magnétique
                # ecriture du bloc du port magnétique
                self.texteCarmel3D+="     [HPORT\n" # début de bloc
                if usePrefix:
                    nomReel = self.nomReelGroupeMaillage(nom, typeBloc)
                else:
                    nomReel = nom
                self.texteCarmel3D+="        NAME "+nomReel+"\n" # ecriture du nom (réel) du groupe du maillage
                self.texteCarmel3D+=  self.dictSourceHport[self.dictGroupesMaillage[nom]] # ecriture des propriétés du port magnétique
                self.texteCarmel3D+="     ]\n" # fin de bloc

#-------------------------------------
# Méthodes utilitaires
# ------------------------------------
   def formateCOMPLEX(self,nbC):
        """prise en compte des differentes formes de description d un nombre complexe
        3 formats possibles : 2 listes (anciennement tuples?)  et 1 nombre complexe
        """
        if self.debug:
            print "formatage "
            print "type : ", type(nbC), "pour ", nbC
        nbformate =""
        if isinstance(nbC,(tuple,list)):
            if nbC[0] == "'RI'" :
                nbformate = "COMPLEX " + str(nbC[1])+" "+str(nbC[2])            
            if nbC[0] == "'MP'" :
                nbformate = "POLAR " + str(nbC[1])+" "+str(nbC[2])            
        else:
            nbformate = "COMPLEX " + str(nbC.real)+" "+str(nbC.imag)
        if self.debug: print "nbformate : ", nbformate
        return nbformate
   
   def nomReelGroupeMaillage(self, nom, typeBloc=None):
        """Calcule et retourne le nom réel du groupe de maillage donné en entrée,
        en tenant compte de l'utilisation de préfixes ou pas, et cela pour le type
        de bloc du fichier PHYS spécifié.
        Cette routine vérifie aussi, en cas d'utilisation de préfixes, si le préfixe est en adéquation avec le type du bloc.
        """
        from string import join
        if self.debug: print "nom groupe original : "+nom+" avec usePrefix="+str(usePrefix)+" devient... "
        nomReel= None # nom affiché dans le fichier PHYS, sans préfixe a priori
        if usePrefix:
            # suppression du préfixe si présent
            partiesNom = nom.split(sepNomGroupeMaille) # séparation du nom du groupe en parties
            # les tests suivants ne génèrent une erreur que si le préfixe est obligatoire
            if len(partiesNom) < 2: # test d'erreur, pas de séparateur donc nom incorrect, i.e. sans préfixe c'est sûr
                print u"ERREUR! ce groupe de maille ("+nom+") n'a pas de préfixe indiquant le type de matériau ou de source associée"
            elif partiesNom[0] not in listePrefixesGroupeMaille: # préfixe non défini
                print u"ERREUR! ce groupe de maille ("+nom+") n'a pas de préfixe valable"
            else:   
                # vérification de l'adéquation du préfixe avec le type de bloc demandé, si fourni    
                if typeBloc is not None:
                    if typeBloc not in dictPrefixesGroupeMaille: # test validité de typeBloc, devant être une clé du dictionnaire
                        print u"ERREUR! ce type de bloc ("+str(typeBloc)+") n'est pas valable"
                    elif partiesNom[0] not in dictPrefixesGroupeMaille[typeBloc]: # pas de préfixe correct pour ce type de bloc
                        print u"ERREUR! ce groupe de maille ("+nom+") n'a pas le préfixe correct pour être associé à un type "+str(typeBloc)
                    else: # c'est bon
                        nomReel = join(partiesNom[1:], sepNomGroupeMaille) # reconstruction du nom du groupe sans préfixe complet
                        if self.debug: print u"ce groupe de maille ("+nom+") a un préfixe qui est supprimé automatiquement pour devenir : "+nomReel
                else: # c'est bon
                    nomReel = join(partiesNom[1:], sepNomGroupeMaille) # reconstruction du nom du groupe sans préfixe complet
                    if self.debug: print u"ce groupe de maille ("+nom+") a un préfixe qui est supprimé automatiquement pour devenir : "+nomReel
        if self.debug: print "... "+nomReel
        return nomReel
