# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
    Ce module sert pour charger les paramètres de configuration d'EFICAS
"""
# Modules Python
print "dans Aster"
import os, sys, string, types, re
import traceback


# Modules Eficas
from Editeur import utils

class CONFIGbase:

  #-----------------------------------
  def __init__(self,appli):
  #-----------------------------------

  # Classe de base permettant de lire, afficher
  # et sauvegarder les fichiers utilisateurs editeur.ini
  # et style.py
  # Classe Mere de : class CONFIG(CONFIGbase)
  #                  class CONFIGStyle(CONFIGbase):
      self.appli = appli  
      self.salome = appli.salome
      self.dRepMat={}
      if self.appli:
         self.parent=appli.top
      else:
         self.parent=None
      self.rep_user = utils.get_rep_user()
      if not os.path.isdir(self.rep_user) : os.mkdir(self.rep_user)
      self.lecture_fichier_ini_standard()
      self.lecture_catalogues_standard()
      self.lecture_fichier_ini_utilisateur()
      self.init_liste_param()
      

  #--------------------------------------
  def lecture_fichier_ini_standard(self):
  #--------------------------------------
  # Verifie l'existence du fichier "standard"
  # appelle la lecture de ce fichier
      if not os.path.isfile(self.fic_ini):
          if self.appli.ihm=="TK" :
              from widgets import showerror
              showerror("Erreur","Pas de fichier de configuration" + self.fic_ini+"\n")
          print "Erreur à la lecture du fichier de configuration : %s" % self.fic_ini
          sys.exit(0)
      self.lecture_fichier(self.fic_ini)

  #-----------------------------
  def lecture_fichier(self,fic):
  #------------------------------
  # lit les paramètres du fichier eficas.ini ou style.py
  # les transforme en attribut de l 'objet  
  # utilisation du dictionnaire local pour récuperer style
      txt = utils.read_file(fic)
      from styles import style
      d=locals()
      try:
         exec txt in d
      except:
         l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
         if self.appli.ihm=="TK" :
              from widgets import showerror
              showerror("Erreur","Une erreur s'est produite lors de la lecture du fichier : " + fic + "\n")
         print ("Erreur","Une erreur s'est produite lors de la lecture du fichier : " + fic + "\n")
         sys.exit()

      for k in d.keys() :
          if  k in self.labels.keys()  :
             setattr(self,k,d[k])
    # Glut horrible pour les repertoires materiau...
          elif k[0:9]=="rep_mat_v" :
             setattr(self,k,d[k])
      
      for k in d['style'].__dict__.keys() :
          setattr(self,k,d['style'].__dict__[k])

      if hasattr(self,"catalogues") :
         for ligne in self.catalogues :
            version=ligne[1]
            codeSansPoint=re.sub("\.","",version)
            chaine="rep_mat_"+codeSansPoint
            if hasattr(self,chaine):
               rep_mat=getattr(self,chaine)
               self.dRepMat[version]=str(rep_mat)


  #--------------------------------------
  def lecture_fichier_ini_utilisateur(self):
  #--------------------------------------
  # Surcharge les paramètres standards par les paramètres utilisateur s'ils existent
      self.fic_ini_utilisateur = os.path.join(self.rep_user,self.fichier)
      if not os.path.isfile(self.fic_ini_utilisateur):
          return
      self.lecture_fichier(self.fic_ini_utilisateur)

  #--------------------------------------
  def lecture_catalogues_standard(self):
  #--------------------------------------
      # repertoires Materiau
      if hasattr(self,"catalogues") :
         for ligne in self.catalogues :
            version=ligne[1]
            cata=ligne[2]
            self.dRepMat[version]=os.path.join(cata,'materiau')

  #--------------------------------------
  def affichage_fichier_ini(self):
  #--------------------------------------
      """
      Affichage des valeurs des paramètres relus par Eficas
      """
      import widgets
      result = widgets.Formulaire(self.parent,
                                  obj_pere = self,
                                  titre = self.titre,
                                  texte = self.texte_ini,
                                  items = self.l_param,
                                  mode='display',
                                  commande=('Modifier',self.commande))
      if result.resultat :
          #print 'on sauvegarde les nouveaux paramètres :',result.resultat
          self.save_param_ini(result.resultat)

  #--------------------------------------
  def save_param_ini(self,dico):
  #--------------------------------------
  # sauvegarde
  # les nouveaux paramètres dans le fichier de configuration utilisateur
  #
      f=open(self.fic_ini_utilisateur,'w+')
      for k,v in dico.items():
         if self.types[k] in ('mot2','mot3','mot4'): 
            v1=v[1:-1]
            val=v1.split(",")
            p = "(" 
            listeval=""
            for valeur in val:
              listeval = listeval+ p + str(valeur) 
              p=" , "
            listeval = listeval + ")"
            f.write(str(self.pref)+str(k) + '=' + str(listeval) + '\n') 
         elif k == 'catalogues' :
            f.write(k + '\t=\t' + str(v) + '\n')
         else:
            f.write(str(self.pref)+str(k) + '\t=\t"' + str(v) + '"\n')
      f.close()
      self.lecture_fichier_ini_utilisateur()

  #-------------------------------------------
  def creation_fichier_ini_si_possible(self):
  #-------------------------------------------
      return self.creation_fichier_ini(mode='ignorer_annuler')

  #--------------------------------------------------------
  def creation_fichier_ini(self,mode='considerer_annuler'):
  #---------------------------------------------------------
  # Récupération des valeurs des paramétres requis pour la création du fichier
  # eficas.ini
  #
      import widgets
      items = self.l_param
      result = widgets.Formulaire(self.parent,
                                  obj_pere = self,
                                  titre = "Saisie des donnees indispensables a la configuration d'EFICAS",
                                  texte = self.texte,
                                  items = items,
                                  mode='query')
      if not result.resultat :
          if mode == 'considerer_annuler':
             test=0
             if self.appli.ihm=="TK" :
                from widgets import showerror,askretrycancel
                test = askretrycancel("Erreur","Données incorrectes !")
             if not test:
                 # XXX On sort d'EFICAS, je suppose
                 self.appli.exitEFICAS()
             else:
                 self.creation_fichier_ini()
          else:
              return None
      else :
          self.save_param_ini(result.resultat)
          return result.resultat

  #--------------------------
  def init_liste_param (self):
  #--------------------------
  # construit self.l_param 
  # a partir de self.labels et des attributs 
  # de l objet (mis a jour lors de la lecture du fichier)
  # l_param est une liste de tuples où chaque tuple est de la forme :
  #           (label,nature,nom_var,defaut)

      self.l_param=[]
      for k in self.labels.keys()  :
          if hasattr(self,k) :
             if k in self.YesNo.keys():
                self.l_param.append((self.labels[k],self.types[k],k,self.__dict__[k],
                                     self.YesNo[k][0],self.YesNo[k][1]))
             else :
                self.l_param.append((self.labels[k],self.types[k],k,self.__dict__[k]))
      self.l_param = tuple(self.l_param)


class CONFIG(CONFIGbase):
  def __init__(self,appli,repIni):

      self.dFichierEditeur={"ASTER"                    : "editeur.ini", 
			    "ASTER_SALOME"             : "editeur_salome.ini"}
      self.texte = "EFICAS a besoin de certains renseignements pour se configurer\n"+\
              "Veuillez remplir TOUS les champs ci-dessous et appuyer sur 'Valider'\n"+\
              "Si vous annulez, EFICAS ne se lancera pas !!"

      self.salome=appli.salome
      self.code=appli.code
      clef=self.code
      if self.salome != 0 :
	  clef = clef + "_SALOME"
      self.fichier=self.dFichierEditeur[clef]
      self.repIni = repIni
      self.rep_ini = repIni
      self.fic_ini = os.path.join(self.repIni,self.fichier)
      self.titre = 'Parametres necessaires a la configuration d\'EFICAS'
      self.texte_ini = "Voici les parametres que requiert Eficas"
      self.commande = self.creation_fichier_ini_si_possible
      self.labels={"savedir"       : "Repertoire initial pour Open/Save des fichiers",
                   "rep_travail"   : "Repertoire de travail",
                   "rep_mat"       : "Repertoire materiaux",
                   "path_doc"      : "Chemin d'acces a la doc Aster",
                   "exec_acrobat"  : "Ligne de commande Acrobat Reader",
                   "catalogues"    : "Versions du code ",
                   "isdeveloppeur" : "Niveau de message ",
                   "path_cata_dev" : "Chemin d'acces aux catalogues developpeurs"}

                   
      self.types ={"savedir":"rep", "rep_travail":"rep","rep_mat":"rep",
                   "path_doc": "rep","exec_acrobat":"file","exec_acrobat":"file",
                   "catalogues" :"cata","isdeveloppeur":"YesNo","path_cata_dev":"rep",
		   "DTDDirectory":"rep"}

      self.YesNo={}
      self.YesNo['isdeveloppeur']=('Deboggage','Utilisation')

      # Valeurs par defaut
      self.rep_user = utils.get_rep_user()
      self.initialdir=self.rep_user
      self.savedir = os.environ['HOME']
      self.rep_travail=os.path.join(self.rep_user,'uaster','tmp_eficas')
      self.rep_mat=""
      self.path_doc=self.rep_user
      self.exec_acrobat=self.rep_user
      self.isdeveloppeur='NON'
      self.path_cata_dev=os.path.join(self.rep_user,'cata')
      CONFIGbase.__init__ (self,appli)
      self.pref=""

  #--------------------------------------
  def save_params(self):
  #--------------------------------------
  # sauvegarde
  # les nouveaux parametres dans le fichier de configuration utilisateur
  #
      l_param=('exec_acrobat', 'repIni','catalogues','rep_travail','rep_mat','path_doc','savedir')
      texte=""
      for clef in l_param :
          if hasattr(self,clef):
             valeur=getattr(self,clef)
             texte= texte + clef+"	= " + repr(valeur) +"\n"


      # recuperation des repertoires materiaux
      try :
          for item in self.catalogues :
              try :
                  (code,version,cata,format,defaut)=item
              except :
                  (code,version,cata,format)=item
              codeSansPoint=re.sub("\.","",version)
              chaine="rep_mat_"+codeSansPoint
              if hasattr(self,chaine):
                 valeur=getattr(self,chaine)
                 texte= texte + chaine+"	= '" + str(valeur) +"'\n"
      except :
             pass

      f=open(self.fic_ini_utilisateur,'w+')
      f.write(texte) 
      f.close()


class CONFIGStyle(CONFIGbase):
  def __init__(self,appli,repIni):
      self.salome=appli.salome
      self.texte = "Pour prendre en compte les modifications \n"+\
                   "     RELANCER EFICAS"
      self.fichier="style.py"
      self.repIni = repIni
      self.rep_ini = repIni
      self.fic_ini = os.path.join(self.repIni,self.fichier)
      self.titre = "Parametres d affichage"
      self.texte_ini = "Voici les parametres configurables :  "
      self.commande = self.creation_fichier_ini_si_possible
      self.labels={"background":"couleur du fonds", 
                   "foreground":"couleur de la police standard" ,
                   "standard":" police et taille standard",
                   "standard_italique":"police utilisee pour l'arbre ",
                   "standard_gras_souligne":"police utilisee pour le gras souligne",
                   "canvas_italique":"police italique",
                   "standard_gras":"gras",
                  }
      self.types ={"background":"mot", 
                   "foreground":"mot" ,
                   "standard":"mot2",
                   "standard_italique":"mot3",
                   "standard_gras":"mot3",
                   "standard_gras_souligne":"mot4",
                   "canvas":"mot2",
                   "canvas_italique":"mot3",
                   "canvas_gras":"mot3",
                   "canvas_gras_italique":"mot4",
                   "standard12":"mot2",
                   "standard12_gras":"mot3",
                   "standard12_gras_italique":"mot4",
                   "statusfont":"mot2",
                   "standardcourier10":"mot2"}
      self.YesNo={}
      self.l_param=[]
      CONFIGbase.__init__ (self,appli)
      self.pref="style."

  def affichage_style_ini(self):
      self.affichage_fichier_ini()

def make_config(appli,rep):
    return CONFIG(appli,rep)

def make_config_style(appli,rep):
    return CONFIGStyle(appli,rep)


