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
import os, sys, string, types, re
import traceback
from PyQt4.QtGui  import *
from utils import read_file

# Modules Eficas
from Editeur import utils

class CONFIG_BASE:

  #--------------------------------------
  def __init__(self,appli,repIni,nomDir):
  #--------------------------------------

  # Classe de base permettant de lire, afficher
  # et sauvegarder les fichiers utilisateurs 
  # On a deux directories : la directory generale (Repertoire d instal + Nom du code
  #                       Par exemple : ~/Install_Eficas/EficasV1_14/Openturns_Wrapper
  # et la directorie de l utilisateur 
  #			  HOME/.Eficas_Openturns
  # Le fichier prefs.py va etre lu dans la directory generale puis surcharge eventuellement 
  # par celui de l utilisateur
  # le fichier de catalogue va etre lu dans la directory de l utilisateur s il exite
  # dans le fichier general sinon
      self.appli   = appli  
      self.code    = appli.code
      self.salome  = appli.salome
      self.repIni  = repIni
      self.REPINI  = repIni
      self.rep_user   = os.path.join(os.environ['HOME'],nomDir)
     
      if self.appli: 
         self.parent=appli.top
         self.appli.mode_nouv_commande='initial'
      else: 	     self.parent=None



  def setValeurs(self):
  #---------------------
  
      # Valeurs par defaut
      if not os.path.isdir(self.rep_user) : os.mkdir(self.rep_user)
      self.initialdir   = self.rep_user
      self.path_doc     = self.rep_user
      self.savedir      = self.rep_user
      self.exec_acrobat = self.rep_user
 
      #Lecture des fichiers utilisateurs
      self.lecture_fichier_ini_standard()
      self.lecture_fichier_ini_utilisateur()
      self.lecture_catalogues()

  #--------------------------------------
  def lecture_fichier_ini_standard(self):
  #--------------------------------------
  # Verifie l'existence du fichier "standard"
  # appelle la lecture de ce fichier
      import prefs
      name='prefs_'+prefs.code
      prefsCode=__import__(name)
      self.prefsUser=name+".py"
      for k in self.labels_eficas :
         try :
            valeur=getattr(prefsCode,k)
            setattr(self,k,valeur)
         except :
            pass
      if hasattr(self,'map_path') :
         oldPath=self.map_path
              

  #--------------------------------------
  def lecture_fichier_ini_utilisateur(self):
  #--------------------------------------
  # Surcharge les paramètres standards par les paramètres utilisateur s'ils existent
      self.fic_ini_utilisateur = os.path.join(self.rep_user,self.prefsUser)
      if not os.path.isfile(self.fic_ini_utilisateur): return

      txt = utils.read_file(self.fic_ini_utilisateur)
      from styles import style
      d=locals()
      try:
         exec txt in d
      except :
         l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
         QMessageBox.critical( None, "Import du fichier de Configuration", 
			"Erreur à la lecture du fichier de configuration " + self.fic_ini_utilisateur )
         sys.exit(0)
      for k in self.labels_user :
         try :
            setattr(self,k,d[k])
         except :
            pass


  #--------------------------------------
  def lecture_catalogues(self):
  #--------------------------------------
      rep_mat=" " # Compatibilite Aster
      if hasattr(self,"catalogues") : return
 
      fic_ini = os.path.join(self.repIni,self.cataFile)
      if not os.path.isfile(fic_ini) :
         QMessageBox.critical( None, "Erreur a l'import du fichier des Catalogues", 
	            "Le fichier de configuration des catalogues "+fic_ini+" n a pas été trouvé" )
         sys.exit(0)

      txt = utils.read_file(fic_ini)
      d=locals()
      try:
         exec txt in d
         self.catalogues=d["catalogues"]
      except :
         l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
         QMessageBox.critical( None, "Import du fichier de Configuration", 
			"Erreur à la lecture du fichier de configuration " + fic_ini )
         sys.exit(0)



  #--------------------------------------
  def save_params(self):
  #--------------------------------------
  # sauvegarde
  # les nouveaux paramètres dans le fichier de configuration utilisateur
  #
      texte=""
      for clef in self.labels_user :
          if hasattr(self,clef):
             valeur=getattr(self,clef)
             texte= texte + clef+"	= " + repr(valeur) +"\n"
      f=open(self.fic_ini_utilisateur,'w+')
      print self.fic_ini_utilisateur
      f.write(texte) 
      f.close()
#

