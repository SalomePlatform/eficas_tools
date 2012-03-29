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
    Ce module sert pour charger les parametres de configuration d'EFICAS
"""
# Modules Python
import os, sys, string, types, re
import traceback
from PyQt4.QtGui import QMessageBox
from  Editeur.utils import read_file

class CONFIG_BASE:

  #--------------------------------------
  def __init__(self,appli,repIni,nomDir):
  #--------------------------------------

  # Classe de base permettant de lire, afficher
  # et sauvegarder les fichiers utilisateurs 
  # On a deux directories : la directory generale (Repertoire d install + Nom du code
  #                       Par exemple : ~/Install_Eficas/EficasV1_14/Openturns_Wrapper
  # et la directorie de l utilisateur 
  #			  HOME/.Eficas_Openturns
  # Le fichier prefs.py va etre lu dans la directory generale 
  #         puis surcharge eventuellement par celui contenu dans ${PREFS_CATA_$CODE} 
  #         par celui de l utilisateur
  # le fichier de catalogue va etre lu dans la directory de l utilisateur s il exite
  # dans le fichier general sinon
      self.appli   = appli  
      self.code    = appli.code
      self.salome  = appli.salome
      if self.salome : self.name="editeur_salome.ini"
      else           : self.name="editeur.ini"
      self.rep_mat = None
      self.repIni  = repIni
      self.rep_user   = os.path.join(os.environ['HOME'],nomDir)
      self.mode_nouv_commande='initial'
     

      self.setValeursParDefaut()
      
      self.lecture_fichier_ini_standard()
      self.lecture_fichier_ini_integrateur()
      self.lecture_fichier_ini_utilisateur()

      #Particularite des schemas MAP
      if hasattr(self,'make_ssCode'): self.make_ssCode(self.ssCode)

      if self.appli: 
         self.parent=appli.top
         self.appli.mode_nouv_commande= self.mode_nouv_commande
      else: 	     self.parent=None
      


  def setValeursParDefaut(self):
  #-----------------------------
  
      # Valeurs par defaut
      if not os.path.isdir(self.rep_user) : os.mkdir(self.rep_user)
      self.path_doc     = os.path.abspath(os.path.join(self.repIni,'..','Doc'))
      self.exec_acrobat = 'acroread'
      nomDir="Eficas_"+self.code
      self.savedir   = os.path.abspath(os.path.join(os.environ['HOME'],nomDir))
      if not os.path.isdir(self.savedir) : os.mkdir(self.savedir)
 
  #--------------------------------------
  def lecture_fichier_ini_standard(self):
  #--------------------------------------

      name='prefs_'+self.appli.code
      prefsCode=__import__(name)
      for k in dir(prefsCode):
          if (k[0:1] != "__" and k[-1:-2] !='__'):
             valeur=getattr(prefsCode,k)
             setattr(self,k,valeur)


  #--------------------------------------
  def lecture_fichier_ini_integrateur(self):
  #--------------------------------------
  # Verifie l'existence du fichier "standard"
  # appelle la lecture de ce fichier
      clef="PREFS_CATA_"+self.code
      try :
        repIntegrateur=os.path.abspath(os.environ[clef])
      except :
        return
      
      fic_ini_integrateur=os.path.join(repIntegrateur,self.name)
      if not os.path.isfile(fic_ini_integrateur): return
      txt = read_file(fic_ini_integrateur)
      d=locals()
      try:
         exec txt in d
      except :
         QMessageBox.critical( None, "Import du fichier de Configuration", 
			"Erreur a la lecture du fichier de configuration " + fic_ini_integrateur)
         return
      for k in self.labels_eficas :
         try :
            setattr(self,k,d[k])
         except :
            pass
      #Glut pour les repertoires materiaux
      #et pour la doc
      for k in d.keys() :
          if (k[0:8]=="rep_mat_") or (k[0:8]=="fic_doc_"):
             setattr(self,k,d[k])


  #--------------------------------------
  def lecture_fichier_ini_utilisateur(self):
  #--------------------------------------
  # Surcharge les parametres standards par les parametres utilisateur s'ils existent
      self.fic_ini_utilisateur = os.path.join(self.rep_user,self.name)
      if not os.path.isfile(self.fic_ini_utilisateur): return

      txt = read_file(self.fic_ini_utilisateur)
      d=locals()
      try:
         exec txt in d
      except :
         l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
         QMessageBox.critical( None, "Import du fichier de Configuration", 
			"Erreur a la lecture du fichier de configuration " + fic_ini_utilisateur )
      for k in self.labels_user :
         try :
            setattr(self,k,d[k])
         except :
            pass

  #--------------------------------------
  def save_params(self):
  #--------------------------------------
  # sauvegarde
  # les nouveaux parametres dans le fichier de configuration utilisateur
  #
      texte=""
      for clef in self.labels_user :
          if hasattr(self,clef):
             valeur=getattr(self,clef)
             texte= texte + clef+"	= " + repr(valeur) +"\n"
      f=open(self.fic_ini_utilisateur,'w+')
      f.write(texte) 
      f.close()
#

