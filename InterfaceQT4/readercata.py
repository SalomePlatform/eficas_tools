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
import types

# Modules Eficas
from Noyau.N_CR import CR
from Editeur.catadesc import CatalogDescription

import analyse_catalogue
import analyse_catalogue_initial
import autre_analyse_cata
import uiinfo
from monChoixCata import MonChoixCata

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class READERCATA:

   def __init__(self,QWParent, appliEficas):
      self.QWParent=QWParent
      self.appliEficas=self.QWParent.appliEficas
      self.VERSION_EFICAS=self.appliEficas.VERSION_EFICAS
      self.code=self.QWParent.code
      self.ssCode=self.appliEficas.ssCode
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
      self.Commandes_Ordre_Catalogue=[]

      all_cata_list = []
      for catalogue in self.appliEficas.CONFIGURATION.catalogues:
          if isinstance(catalogue, CatalogDescription):
              all_cata_list.append(catalogue)
          elif isinstance(catalogue, types.TupleType):
              all_cata_list.append(CatalogDescription.create_from_tuple(catalogue))
          else:
              print "Catalog description cannot be interpreted: ", catalogue

      # This filter is only useful for codes that have subcodes (like MAP).
      # Otherwise, the "code" attribute of the catalog description can (should) be None.
      if self.ssCode is None:
          liste_cata_possibles = all_cata_list
      else:
          for catalogue in all_cata_list:
              if catalogue.code == self.code and catalogue.file_format == self.ssCode:
                  liste_cata_possibles.append(catalogue)

      if len(liste_cata_possibles)==0:          
          QMessageBox.critical(self.QWParent, "Import du catalogue",
                               u"Pas de catalogue défini pour le code %s" % self.code)
          self.appliEficas.close()
          if self.appliEficas.salome == 0 :
             sys.exit(1)
          return


      if self.version_code is not None:
          # La version a ete fixee
          for cata in liste_cata_possibles:
             if self.version_code == cata.identifier:
                self.fic_cata = cata.cata_file_path
                self.appliEficas.format_fichier = cata.file_format
                self.appliEficas.format_fichier_in = cata.file_format_in
      else:
          cata_choice_list = []
          for cata in liste_cata_possibles:
              if cata.selectable:
                  if cata.default:
                      cata_choice_list.insert(0, cata)
                  else :
                      cata_choice_list.append(cata)
          if len(cata_choice_list) == 0:
              QMessageBox.critical(self.QWParent, "Import du catalogue",
                                   QString.fromUtf8("Aucun catalogue trouvé"))
              self.appliEficas.close()
              if self.appliEficas.salome == 0 :
                 sys.exit(1)
          elif len(cata_choice_list) == 1:
              self.fic_cata = cata_choice_list[0].cata_file_path
              self.version_code = cata_choice_list[0].identifier
              self.appliEficas.format_fichier = cata_choice_list[0].file_format
              self.appliEficas.format_fichier_in = cata_choice_list[0].file_format_in
              lab=QString("Eficas ") 
              lab+=QString(self.VERSION_EFICAS) 
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
              self.ask_choix_catalogue(cata_choice_list)

      if self.fic_cata == None :
          if self.appliEficas.salome == 0 :
             print "Pas de catalogue pour code %s, version %s" %(self.code,self.version_code)
             sys.exit(1)
          else :
             self.appliEficas.close()
             return

      if self.code == "ASTER" : self.determineMater()

      # import du catalogue
      self.cata = self.import_cata(self.fic_cata)
      if not self.cata :          
          QMessageBox.critical( self.QWParent, "Import du catalogue","Impossible d'importer le catalogue %s" %self.fic_cata)
	  self.appliEficas.close()
          if self.appliEficas.salome == 0 :
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

      #
      # analyse des données liées l'IHM : UIinfo
      #
      uiinfo.traite_UIinfo(self.cata)

      #
      # traitement des clefs documentaires
      #
      if self.code == "ASTER" : self.traite_clefs_documentaires()
      self.cata=(self.cata,)

      titre=self.VERSION_EFICAS + " avec le catalogue " + os.path.basename(self.fic_cata)
      if self.appliEficas.top:
        self.appliEficas.setWindowTitle(titre)
      self.appliEficas.titre=titre
      self.QWParent.titre=titre

   def determineMater(self) :
      # Determinination du repertoire materiau
      v_codeSansPoint=self.version_code
      if v_codeSansPoint == None : return 
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
          Realise l'import du catalogue dont le chemin d'acces est donne par cata
      """
      nom_cata = os.path.splitext(os.path.basename(cata))[0]
      rep_cata = os.path.dirname(cata)
      sys.path[:0] = [rep_cata]
      self.appliEficas.listeAEnlever.append(rep_cata)

      
      if sys.modules.has_key(nom_cata):
        del sys.modules[nom_cata]
      for k in sys.modules.keys():
        if k[0:len(nom_cata)+1] == nom_cata+'.':
          del sys.modules[k]

      if self.code == "ASTER" :
         self.appliEficas.rep_scripts=os.path.join(rep_cata,nom_cata)
         sys.path[:0] = [self.appliEficas.rep_scripts]
         try :
             self.appliEficas.mesScripts=__import__('mesScripts')
         except:
             pass
         sys.path=sys.path[1:]
      else :
         try :
            self.appliEficas.mesScripts=__import__('mesScripts')
         except:
            pass

      try :
          o=__import__(nom_cata)
          return o
      except Exception,e:
          traceback.print_exc()
          return 0



   def Retrouve_Ordre_Cata_Standard_autre(self):
      """ 
          Construit une structure de données dans le catalogue qui permet
          a EFICAS de retrouver l'ordre des mots-clés dans le texte du catalogue.
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

   def ask_choix_catalogue(self, cata_choice_list):
      """
      Ouvre une fenetre de sélection du catalogue dans le cas où plusieurs
      ont été définis dans Accas/editeur.ini
      """      
      code = getattr(self.appliEficas.CONFIGURATION, "code", None)
      if code != None : 
          title="Choix d une version du code "+str(code)
      else :
          title="Choix d une version "
    
      widgetChoix = MonChoixCata(self.appliEficas, [cata.user_name for cata in cata_choice_list], title)
      ret=widgetChoix.exec_()
      
      lab=QString(self.VERSION_EFICAS)
      lab+=QString(" pour ")
      lab+=QString(self.code) 
      lab+=QString(" avec le catalogue ")
      if ret == QDialog.Accepted:
          cata = cata_choice_list[widgetChoix.CBChoixCata.currentIndex()]
          self.version_cata = cata.identifier
          self.fic_cata = cata.cata_file_path
          self.version_code = self.version_cata
          self.appliEficas.format_fichier = cata.file_format
          self.appliEficas.format_fichier_in = cata.file_format_in
          lab+=self.version_cata
          self.appliEficas.setWindowTitle(lab)
          #qApp.mainWidget().setCaption(lab)
      else:
          self.appliEficas.close()
          if self.appliEficas.salome == 0 :
             sys.exit(0)

   def traite_clefs_documentaires(self):
      try:
        fic_doc='rep_doc_'+str(self.version_code)
        self.fic_doc=getattr(self.appliEficas.CONFIGURATION,fic_doc )
        f=open(self.fic_doc)
      except:
        print "Pas de fichier associe contenant des clefs documentaires"
        return

      dict_clef_docu={}
      for l in f.readlines():
          clef=l.split(':')[0]
          deb=l.find(':')+1
          docu=l[deb:-1]
          dict_clef_docu[clef]=docu
      for oper in self.cata.JdC.commandes:
           if dict_clef_docu.has_key(oper.nom):
              oper.docu=dict_clef_docu[oper.nom]

