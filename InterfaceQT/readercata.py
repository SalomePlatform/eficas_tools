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
import prefs
from Noyau.N_CR import CR
from Editeur.utils  import init_rep_cata_dev

from Editeur    import analyse_catalogue
from Editeur    import autre_analyse_cata
from Editeur    import uiinfo
from monChoixCata import MonChoixCata

from qt import *

version="14"

class READERCATA:

   def __init__(self,appli,parent):
      self.appli=appli      
      self.parent=parent
      self.code=self.appli.code
      self.appli.format_fichier='python'
      self.version_code=self.appli.version_code
      self.version_cata=None
      self.fic_cata=None
      self.OpenCata()
      self.cataitem=None

   def OpenCata(self):
      """ 
          Ouvre le catalogue standard du code courant, cad le catalogue présent
          dans le répertoire Cata 
      """
      message1 = "Compilation des fichiers Eficas \n\n Veuillez patienter ..."
      self.configure_barre(4)

      liste_cata_possibles=[]
      for catalogue in self.appli.CONFIGURATION.catalogues:
          if catalogue[0] == self.code :
             liste_cata_possibles.append(catalogue)

      if len(liste_cata_possibles)==0:          
          QMessageBox.critical( self.parent, "Import du catalogue","Pas de catalogue defini pour le code %s" % self.code)
          self.appli.parent.ui.close()
          sys.exit(1)

      if self.version_code is not None:
          # La version a ete fixee
          for cata in liste_cata_possibles:
             if self.version_code == cata[1]:
                self.fic_cata = cata[2]
                self.appli.format_fichier=cata[3]
      elif len(liste_cata_possibles)==1:
          self.fic_cata = liste_cata_possibles[0][2]
          self.version_code = liste_cata_possibles[0][1]
          self.appli.format_fichier=liste_cata_possibles[0][3] 
          lab=QString("Eficas V1.") 
          lab+=QString(version) 
          lab+=QString(" pour ")
          lab+=QString(self.code) 
          lab+=QString(" avec le catalogue ")
          lab+=self.version_code
          try :
          # souci pour les includes
              self.appli.parent.ui.setCaption(lab)
          except :
              pass
          #qApp.mainWidget().setCaption(lab)
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
      self.update_barre()
      if not self.cata :          
          QMessageBox.critical( self.parent, "Import du catalogue","Impossible d'importer le catalogue %s" %self.fic_cata)
	  self.appli.parent.ui.close()
          sys.exit(1)
      #
      # analyse du catalogue (ordre des mots-clés)
      #
      # Retrouve_Ordre_Cata_Standard fait une analyse textuelle du catalogue
      # remplacé par Retrouve_Ordre_Cata_Standard_autre qui utilise une numerotation
      # des mots clés a la création
      self.Retrouve_Ordre_Cata_Standard_autre()
      self.update_barre()

      #
      # analyse des données liées a  l'IHM : UIinfo
      #
      uiinfo.traite_UIinfo(self.cata)
      self.update_barre()

      #
      # traitement des clefs documentaires
      #
      self.traite_clefs_documentaires()

      # chargement et analyse des catalogues développeur (le cas échéant)
      #
      if self.appli.CONFIGURATION.isdeveloppeur == 'OUI' :
          init_rep_cata_dev(self.fic_cata,self.appli.CONFIGURATION.path_cata_dev)
          fic_cata_dev = os.path.join(self.appli.CONFIGURATION.path_cata_dev,'cata_developpeur.py')
          if os.path.isfile(fic_cata_dev):
              # il y a bien un catalogue développeur : il faut récupérer le module_object associé ...
              test = self.compile_cata(fic_cata_dev,fic_cata_dev+'c')
              if not test :
                  showinfo("Compilation catalogue développeur",
                           "Erreur dans la compilation du catalogue développeur")
                  self.cata = (self.cata,)
              else:
                  self.cata_dev =self.import_cata(fic_cata_dev)
                  #self.Retrouve_Ordre_Cata_Developpeur()
                  self.Retrouve_Ordre_Cata_Developpeur_autre()
                  self.cata = (self.cata,self.cata_dev)
          else:
              self.cata = (self.cata,)
      else:
          self.cata = (self.cata,)
      titreSuite=" avec le catalogue " + os.path.basename(self.fic_cata)
      titre=self.appli.titre+titreSuite
      if self.appli.top:
        self.appli.top.title(titre)
      self.appli.titre=titre

   def determineMater(self) :
      # Determinination du repertoire materiau
      v_codeSansPoint=self.version_code
      v_codeSansPoint=re.sub("\.","",v_codeSansPoint)
      chaine="rep_mat_"+v_codeSansPoint
      if hasattr(self.appli.CONFIGURATION,chaine):
          a=getattr(self.appli.CONFIGURATION,chaine)
      else :
          try :
             a=self.appli.CONFIGURATION.dRepMat[self.version_code]
          except :
             if self.code == "ASTER" :
                print "Probleme avec le repertoire materiau"
             a='.'
      self.appli.CONFIGURATION.rep_mat=a

   def import_cata(self,cata):
      """ 
          Réalise l'import du catalogue dont le chemin d'acca¨s est donné par cata
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
      self.cata_ordonne_dico,self.appli.liste_simp_reel=autre_analyse_cata.analyse_catalogue(self.cata)

   def Retrouve_Ordre_Cata_Standard(self):
      """ 
          Retrouve l'ordre des mots-clés dans le catalogue, cad :
           - si ce dernier a été modifié, relance l'analyse du catalogue pour déterminer
               l'ordre des mots-clés dans le catalogue
           - s'il n'a pas été modifié, relie le fichier pickle 
      """
      time1 = os.path.getmtime(self.fic_cata)
      try :
          time2 = os.path.getmtime(self.fic_cata_p)
      except:
          time2 = 0
      if time2 > time1 :
          # l'objet catalogue n'a pas été modifié depuis le dernier "pickle"
          self.Get_Ordre_Cata()
      else :
          # le catalogue a été modifié depuis le dernier "pickle" :
          # il faut retrouver l'ordre du catalogue et refaire pickle
          self.Get_Ordre_Cata(mode='cata')
      self.appli.affiche_infos("Catalogue standard chargé")

   def Retrouve_Ordre_Cata_Developpeur(self):
      """ 
          Retrouve l'ordre des mots-clés dans le catalogue, cad :
          - si ce dernier a été modifié, relance l'analyse du catalogue pour déterminer
            l'ordre des mots-clés dans le catalogue
          - s'il n'a pas été modifié, relie le fichier pickle 
      """
      if self.code != 'ASTER' : return
      fic_cata = os.path.join(self.appli.CONFIGURATION.path_cata_dev,'cata_developpeur.py')
      message="Chargement catalogue développeur présent dans :\n %s..." % self.appli.CONFIGURATION.path_cata_dev
      cata_dev_ordonne = analyse_cata.analyse_catalogue(self,self.fic_cata)
      self.cata_dev_ordonne_cr = cata_dev_ordonne.cr
      cata_dev_ordonne_dico = cata_dev_ordonne.entites
      self.cata_ordonne_dico.update(cata_dev_ordonne_dico)
      self.appli.affiche_infos(" catalogue(s) développeur(s) chargé(s)" )

   def Retrouve_Ordre_Cata_Developpeur_autre(self):
      """
          Retrouve l'ordre des mots-clés dans le catalogue, cad :
          - si ce dernier a été modifié, relance l'analyse du catalogue pour déterminer
            l'ordre des mots-clés dans le catalogue
          - s'il n'a pas été modifié, relie le fichier pickle
      """
      if self.code != 'ASTER' : return
      message="Chargement catalogue développeur présent dans :\n %s..." % self.appli.CONFIGURATION.path_cata_dev
      cata_dev_ordonne_dico,self.appli.liste_simp_reel=autre_analyse_cata.analyse_catalogue(self.cata)
      self.cata_ordonne_dico.update(cata_dev_ordonne_dico)
      self.appli.affiche_infos(" catalogue(s) développeur(s) chargé(s)" )

   def Get_Ordre_Cata(self,mode='pickle'):
      """ 
          Retrouve l'ordre du catalogue :
            - mode='pickle ': tente de relire le fichier pickle et sinon lance l'analyse du catalogue
            - mode='cata'   : force l'analyse du catalogue directement sans relire le pickle
      """
      if mode == 'pickle' :
          try:
              f = open(self.fic_cata_p)
              u = cPickle.Unpickler(f)
              self.cata_ordonne_dico = u.load()
              f.close()
          except :
              # on peut ne pas arriver a  relire le fichier pickle s'il a été altéré
              # ou (le plus probable) s'il a été créé sous un autre OS
              self.Get_Ordre_Cata(mode='cata')
      elif mode == 'cata':
          cata_ordonne = analyse_catalogue.analyse_catalogue(self,self.fic_cata)
          self.cata_ordonne_cr = cata_ordonne.cr
          self.cata_ordonne_dico = cata_ordonne.entites
          f = open(self.fic_cata_p,'w+')
          p = cPickle.Pickler(f)
          p.dump(self.cata_ordonne_dico)
          f.close()
      else :
          raise Exception("Appel a  un mode inconnu de Get_Ordre_Cata : %s" % mode)
          return

   def ask_choix_catalogue(self):
      """
      Ouvre une fenetre de sélection du catalogue dans le cas oa¹ plusieurs
      ont été définis dans Accas/editeur.ini
      """      
      # construction du dictionnaire et de la liste des catalogues
      self.dico_catalogues = {}
      defaut = None
      for catalogue in self.appli.CONFIGURATION.catalogues:
          if catalogue[0] == self.code :
              self.dico_catalogues[catalogue[1]] = catalogue
              if len(catalogue) == 5 :
                  if catalogue[4]=='defaut' : defaut = catalogue[1]
      liste_choix = self.dico_catalogues.keys()
      liste_choix.sort()

      lab=QString("Eficas V1.") 
      lab+=QString(version) 
      lab+=QString(" pour ")
      lab+=QString(self.code) 
      lab+=QString(" avec le catalogue ")

      # teste si plusieurs catalogues ou non
      if len(liste_choix) == 0:          
          QMessageBox.critical( self.parent, "", "Aucun catalogue déclaré pour %s" %self.code)
	  self.appli.parent.ui.close()
          sys.exit(1)
          
      # création d'une boite de dialogue modale
      widgetChoix=MonChoixCata(liste_choix,self, self.parent, "", True )
      ret=widgetChoix.exec_loop()
      
      lab=QString("Eficas V1.") 
      lab+=QString(version) 
      lab+=QString(" pour ")
      lab+=QString(self.code) 
      lab+=QString(" avec le catalogue ")
      if ret == QDialog.Accepted:
          self.version_cata=str(self.version_cata)
          self.fic_cata = self.dico_catalogues[self.version_cata][2]
          self.version_code = self.version_cata
          self.appli.format_fichier = self.dico_catalogues[self.version_cata][3]
          lab+=self.version_cata
          self.appli.parent.ui.setCaption(lab)
          #qApp.mainWidget().setCaption(lab)
      else :
          sys.exit(0)


   def compile_cata(self,cata,catac):
      """ 
           Teste si le catalogue a bien besoin d'etre recompilé et si oui, le compile et
           affiche un message dans le splash . Retourne 1 si la compilation s'est bien déroulée,
           0 sinon.
      """
      time1 = os.path.getmtime(cata)
      try:
          time2 = os.path.getmtime(catac)
      except:
          time2 = 0
      if time1 > time2:
          try:
              # le catalogue doit etre recompilé avant d'etre importé
              if self.appli.test == 0 :
                 splash._splash.configure(text="Compilation du catalogue\nCela peut prendre plusieurs secondes ...")
              py_compile.compile(cata)
          except:
              return 0
      return 1


#--------------------------------------------------------------------------------
# Méthodes concernant la barre de progression lors de l'analyse du catalogue
#--------------------------------------------------------------------------------

   def configure_barre(self,nbcommandes):
      """ Configure la barre de progression en lui passant comme parama¨tre le
          nombre de commandes du catalogue qui lui sert a  déterminer la longueur de son incrément """
      try:
          if self.appli.test == 0 :
             splash._splash.configure(barre='oui',ratio = nbcommandes)
      except:
          pass

   def update_barre(self):
      """ Update la position de la barre de progression : la fait progresser de son incrément """
      try:
          if self.appli.test == 0 :
             splash._splash.update_barre()
      except:
          pass

   def visuCRCATA(self):
      """
      Méthode permettant l'affichage du rapport de validation
      """
      cr = CR( debut = "Début rapport de validation du catalogue",
               fin = "Fin rapport de validation du catalogue")
      titre="rapport de validation du catalogue"
      if hasattr(self,'cata_ordonne_cr') :
          cr.add(self.cata_ordonne_cr)
      if hasattr(self,'cata_dev_ordonne_cr') :
          cr.add(self.cata_dev_ordonne_cr)
      for cata in self.cata:
          if hasattr(cata,'JdC'):
              cr.add(cata.JdC.report())
      texte_cr = str(cr)
      self.visu_texte_cr = Fenetre(self.appli,titre=titre,texte=texte_cr)


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
