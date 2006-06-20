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
    Ce module sert pour charger les param�tres de configuration d'EFICAS
"""
# Modules Python
import os,sys,string,types
import traceback

# Modules Eficas
from widgets import showinfo,showerror,askretrycancel
import utils

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
      if self.appli:
         self.parent=appli.top
      else:
         self.parent=None
      self.rep_user = utils.get_rep_user()
      self.lecture_fichier_ini_standard()
      self.lecture_fichier_ini_utilisateur()
      self.init_liste_param()
  
 
  #--------------------------------------
  def lecture_fichier_ini_standard(self):
  #--------------------------------------
  # Verifie l'existence du fichier "standard"
  # appelle la lecture de ce fichier
      if not os.path.isfile(self.fic_ini):
          print self.fic_ini
          showerror("Erreur","Pas de fichier de configuration" + self.fic_ini+"\n")
          print "Erreur � la lecture du fichier de configuration : %s" % self.fic_ini
          sys.exit(0)
      self.lecture_fichier(self.fic_ini)

  #-----------------------------
  def lecture_fichier(self,fic):
  #------------------------------
  # lit les param�tres du fichier eficas.ini ou style.py
  # les transforme en attribut de l 'objet  
  # utilisation du dictionnaire local pour r�cuperer style
      txt = utils.read_file(fic)
      from styles import style
      d=locals()
      try:
         exec txt in d
      except:
         l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
         showerror("Erreur","Une erreur s'est produite lors de la lecture du fichier : " + fic + "\n")
         print "Erreur � la lecture du fichier de configuration : %s" % fic
         sys.exit()

      for k in d.keys() :
          if  k in self.labels.keys()  :
             setattr(self,k,d[k])
      
      for k in d['style'].__dict__.keys() :
          setattr(self,k,d['style'].__dict__[k])
   
  #--------------------------------------
  def lecture_fichier_ini_utilisateur(self):
  #--------------------------------------
  # Surcharge les param�tres standards par les param�tres utilisateur s'ils existent
      self.fic_ini_utilisateur = os.path.join(self.rep_user,self.fichier)
      if not os.path.isfile(self.fic_ini_utilisateur):
          return
      self.lecture_fichier(self.fic_ini_utilisateur)


  #--------------------------------------
  def affichage_fichier_ini(self):
  #--------------------------------------
      """
      Affichage des valeurs des param�tres relus par Eficas
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
          #print 'on sauvegarde les nouveaux param�tres :',result.resultat
          self.save_param_ini(result.resultat)

  #--------------------------------------
  def save_param_ini(self,dico):
  #--------------------------------------
  # sauvegarde
  # les nouveaux param�tres dans le fichier de configuration utilisateur
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
  # R�cup�ration des valeurs des param�tres requis pour la cr�ation du fichier
  # eficas.ini
  #
      import widgets
      items = self.l_param
      result = widgets.Formulaire(self.parent,
                                  obj_pere = self,
                                  titre = "Saisie des donn�es indispensables � la configuration d'EFICAS",
                                  texte = self.texte,
                                  items = items,
                                  mode='query')
      if not result.resultat :
          if mode == 'considerer_annuler':
             test = askretrycancel("Erreur","Donn�es incorrectes !")
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
  # l_param est une liste de tuples o� chaque tuple est de la forme :
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
  def __init__(self,appli,rep_ini):
      self.texte = "EFICAS a besoin de certains renseignements pour se configurer\n"+\
              "Veuillez remplir TOUS les champs ci-dessous et appuyer sur 'Valider'\n"+\
              "Si vous annulez, EFICAS ne se lancera pas !!"
      self.fichier="editeur.ini"
      self.rep_ini = rep_ini
      self.fic_ini = os.path.join(self.rep_ini,self.fichier)
      self.titre = "Param�tres n�cessaires � la configuration d'EFICAS"
      self.texte_ini = "Voici les param�tres que requiert Eficas"
      self.commande = self.creation_fichier_ini_si_possible
      self.pref=""
      self.labels={"initialdir"    : "R�pertoire initial pour Open/Save des fichiers",
                   "rep_travail"   : "R�pertoire de travail",
                   "rep_mat"       : "R�pertoire materiaux",
                   "path_doc"      : "Chemin d'acc�s � la doc Aster",
                   "exec_acrobat"  : "Ligne de commande Acrobat Reader",
                   "catalogues"    : "Versions du code ",
                   "isdeveloppeur" : "Niveau de message ",
                   "path_cata_dev" : "Chemin d'acc�s aux catalogues d�veloppeurs"}
                   
      self.types ={"initialdir":"rep", "rep_travail":"rep","rep_mat":"rep",
                   "path_doc": "rep","exec_acrobat":"file","exec_acrobat":"file",
                   "catalogues" :"cata","isdeveloppeur":"YesNo","path_cata_dev":"rep"}

      self.YesNo={}
      self.YesNo['isdeveloppeur']=('Deboggage','Utilisation')

      # Valeurs par defaut
      self.rep_user = utils.get_rep_user()
      self.initialdir=self.rep_user
      self.rep_travail=os.path.join(self.rep_user,'uaster','tmp_eficas')
      self.rep_mat='/aster/v7/materiau'
      self.path_doc=self.rep_user
      self.exec_acrobat=self.rep_user
      self.catalogues= os.path.join(self.rep_ini,'..','Cata/cata.py')
      self.isdeveloppeur='NON'
      self.path_cata_dev=os.path.join(self.rep_user,'cata')

      CONFIGbase.__init__ (self,appli)


class CONFIGStyle(CONFIGbase):
  def __init__(self,appli,rep_ini):
      self.texte = "Pour prendre en compte les modifications \n"+\
                   "     RELANCER EFICAS"
      self.fichier="style.py"
      self.rep_ini = rep_ini
      self.fic_ini = os.path.join(self.rep_ini,self.fichier)
      self.titre = "Param�tres d affichage"
      self.texte_ini = "Voici les param�tres configurables :  "
      self.commande = self.creation_fichier_ini_si_possible
      self.pref="style."
      self.labels={"background":"couleur du fonds", 
                   "foreground":"couleur de la police standard" ,
                   "standard":" police et taille standard",
                   "standard_italique":"police utilis�e pour l'arbre ",
                   "standard_gras_souligne":"police utilis�e pour le gras soulign�",
                   "canvas_italique":"police italique",
                   "standard_gras":"gras",
                   #"canvas":"police",
                   #"canvas_gras":"police gras",
                   #"canvas_gras_italique":"police gras italique",
                   #"standard12":"police 12",
                   #"standard12_gras":"police 12 gras",
                   #"standard12_gras_italique":"police 12 gras italique",
                   #"standardcourier10":"courrier "
                   "statusfont":"police utilis�e dans la status Bar",
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

  def affichage_style_ini(self):
      self.affichage_fichier_ini()

def make_config(appli,rep):
    return CONFIG(appli,rep)

def make_config_style(appli,rep):
    return CONFIGStyle(appli,rep)


