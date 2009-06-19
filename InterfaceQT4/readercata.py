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
    Ce module sert a lire un catalogue et a construire
    un objet CataItem pour Eficas.
    Il s'appuie sur la classe READERCATA
"""
# Modules Python
import time
import os,sys,py_compile
import traceback
import cPickle
import re

# Modules Eficas
from Noyau.N_CR import CR
from Editeur.utils  import init_rep_cata_dev

import analyse_catalogue
import analyse_catalogue_initial
import autre_analyse_cata
import uiinfo
from monChoixCata import MonChoixCata

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *

VERSION_EFICAS="Eficas V1.16"

class READERCATA:

   def __init__(self,QWParent, appliEficas):
      self.QWParent=QWParent
      self.appliEficas=self.QWParent.appliEficas
      self.code=self.QWParent.code
      self.appliEficas.format_fichier='python'
      if hasattr(self.appliEficas,'mode_nouv_commande'):
	 self.mode_nouv_commande=self.appliEficas.mode_nouv_commande
      else :
         self.mode_nouv_commande='alpha'
      self.version_code=self.QWParent.version_code
      self.version_cata=None
      self.fic_cata=None
      self.OpenCata()
      self.cataitem=None

   def OpenCata(self):
      """ 
          Ouvre le catalogue standard du code courant, cad le catalogue présent
          dans le répertoire Cata 
      """

      liste_cata_possibles=[]
      for catalogue in self.appliEficas.CONFIGURATION.catalogues:
          if catalogue[0] == self.code :
             liste_cata_possibles.append(catalogue)

      if len(liste_cata_possibles)==0:          
          QMessageBox.critical( self.QWParent, "Import du catalogue","Pas de catalogue defini pour le code %s" % self.code)
          self.appliEficas.close()
          sys.exit(1)

      if self.version_code is not None:
          # La version a ete fixee
          for cata in liste_cata_possibles:
             if self.version_code == cata[1]:
                self.fic_cata = cata[2]
                self.appliEficas.format_fichier=cata[3]
      elif len(liste_cata_possibles)==1:
          self.fic_cata = liste_cata_possibles[0][2]
          self.version_code = liste_cata_possibles[0][1]
          self.appliEficas.format_fichier=liste_cata_possibles[0][3] 
          lab=QString("Eficas V1.") 
          lab+=QString(VERSION_EFICAS) 
          lab+=QString(" pour ")
          lab+=QString(self.code) 
          lab+=QString(" avec le catalogue ")
          lab+=self.version_code
          try :
          # souci pour les includes et sans Ihm
              self.appliEficas.setWindowTitle(lab)
          except :
              pass
      else:
          # plusieurs catalogues sont disponibles : il faut demander a l'utilisateur
          # lequel il veut utiliser ...
          self.ask_choix_catalogue()

      if self.fic_cata == None :
          print "Pas de catalogue pour code %s, version %s" %(self.code,self.version_code)
          sys.exit(0)

      self.determineMater()


      # détermination de fic_cata_c et fic_cata_p
      self.fic_cata_c = self.fic_cata + 'c'
      self.fic_cata_p = os.path.splitext(self.fic_cata)[0]+'_pickled.py'

      # import du catalogue
      self.cata = self.import_cata(self.fic_cata)
      if not self.cata :          
          QMessageBox.critical( self.QWParent, "Import du catalogue","Impossible d'importer le catalogue %s" %self.fic_cata)
	  self.appliEficas.close()
          sys.exit(1)
      #
      # analyse du catalogue (ordre des mots-clés)
      #
      # Retrouve_Ordre_Cata_Standard fait une analyse textuelle du catalogue
      # remplacé par Retrouve_Ordre_Cata_Standard_autre qui utilise une numerotation
      # des mots clés a la création
      self.Retrouve_Ordre_Cata_Standard_autre()
      if self.mode_nouv_commande== "initial" :
         self.Retrouve_Ordre_Cata_Standard()
      else:
         self.Commandes_Ordre_Catalogue=[]

      #
      # analyse des données liées a  l'IHM : UIinfo
      #
      uiinfo.traite_UIinfo(self.cata)

      #
      # traitement des clefs documentaires
      #
      self.traite_clefs_documentaires()
      self.cata=(self.cata,)
      titre=VERSION_EFICAS + " avec le catalogue " + os.path.basename(self.fic_cata)
      if self.appliEficas.top:
        self.appliEficas.setWindowTitle(titre)
      self.appliEficas.titre=titre

   def determineMater(self) :
      # Determinination du repertoire materiau
      v_codeSansPoint=self.version_code
      v_codeSansPoint=re.sub("\.","",v_codeSansPoint)
      chaine="rep_mat_"+v_codeSansPoint
      if hasattr(self.appliEficas.CONFIGURATION,chaine):
          a=getattr(self.appliEficas.CONFIGURATION,chaine)
      else :
          try :
             a=self.appliEficas.CONFIGURATION.dRepMat[self.version_code]
          except :
             if self.code == "ASTER" :
                print "Probleme avec le repertoire materiau"
             a='.'
      self.appliEficas.CONFIGURATION.rep_mat=a

   def import_cata(self,cata):
      """ 
          Réalise l'import du catalogue dont le chemin d'acces est donné par cata
      """
      nom_cata = os.path.splitext(os.path.basename(cata))[0]
      rep_cata = os.path.dirname(cata)
      sys.path[:0] = [rep_cata]
      try :
          o=__import__(nom_cata)
          return o
      except Exception,e:
          traceback.print_exc()
          return 0

   def Retrouve_Ordre_Cata_Standard_autre(self):
      """ 
          Construit une structure de données dans le catalogue qui permet
          a  EFICAS de retrouver l'ordre des mots-clés dans le texte du catalogue.
          Pour chaque entité du catlogue on crée une liste de nom ordre_mc qui
          contient le nom des mots clés dans le bon ordre
      """ 
      self.cata_ordonne_dico,self.appliEficas.liste_simp_reel=autre_analyse_cata.analyse_catalogue(self.cata)

   def Retrouve_Ordre_Cata_Standard(self):
      """ 
          Retrouve l'ordre des mots-clés dans le catalogue, cad :
          Attention s appuie sur les commentaires
      """
      nom_cata = os.path.splitext(os.path.basename(self.fic_cata))[0]
      rep_cata = os.path.dirname(self.fic_cata)
      self.Commandes_Ordre_Catalogue = analyse_catalogue_initial.analyse_catalogue(self.fic_cata)

   def ask_choix_catalogue(self):
      """
      Ouvre une fenetre de sélection du catalogue dans le cas oa¹ plusieurs
      ont été définis dans Accas/editeur.ini
      """      
      # construction du dictionnaire et de la liste des catalogues
      self.dico_catalogues = {}
      defaut = None
      for catalogue in self.appliEficas.CONFIGURATION.catalogues:
          if catalogue[0] == self.code :
              self.dico_catalogues[catalogue[1]] = catalogue
              if len(catalogue) == 5 :
                  if catalogue[4]=='defaut' : defaut = catalogue[1]
      liste_choix = self.dico_catalogues.keys()
      liste_choix.sort()

      lab=QString(VERSION_EFICAS)
      lab+=QString(" pour ")
      lab+=QString(self.code) 
      lab+=QString(" avec le catalogue ")

      # teste si plusieurs catalogues ou non
      if len(liste_choix) == 0:          
          QMessageBox.critical( self.QWParent, "", "Aucun catalogue déclaré pour %s" %self.code)
	  self.appliEficas.close()
          sys.exit(1)
          
      # création d'une boite de dialogue modale
      widgetChoix=MonChoixCata(liste_choix,self, self.appliEficas, "", True )
      ret=widgetChoix.exec_()
      
      lab=QString(VERSION_EFICAS)
      lab+=QString(" pour ")
      lab+=QString(self.code) 
      lab+=QString(" avec le catalogue ")
      if ret == QDialog.Accepted:
          self.version_cata=str(self.version_cata)
          self.fic_cata = self.dico_catalogues[self.version_cata][2]
          self.version_code = self.version_cata
          self.appliEficas.format_fichier = self.dico_catalogues[self.version_cata][3]
          lab+=self.version_cata
          self.appliEficas.setWindowTitle(lab)
          #qApp.mainWidget().setCaption(lab)
      else :
          sys.exit(0)



   def traite_clefs_documentaires(self):
      try:
        self.fic_cata_clef=os.path.splitext(self.fic_cata_c)[0]+'_clefs_docu'
        f=open(self.fic_cata_clef)
      except:
        #print "Pas de fichier associé contenant des clefs documentaires"
        return

      dict_clef_docu={}
      for l in f.readlines():
          clef=l.split(':')[0]
          docu=l.split(':')[1]
          docu=docu[0:-1]
          dict_clef_docu[clef]=docu
      for oper in self.cata.JdC.commandes:
           if dict_clef_docu.has_key(oper.nom):
              oper.docu=dict_clef_docu[oper.nom]
