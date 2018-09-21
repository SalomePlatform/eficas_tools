# -*- coding: utf-8 -*-
# Copyright (C) 2007-2017   EDF R&D
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
from __future__ import absolute_import
from __future__ import print_function
try :
   from builtins import str
   from builtins import object
except : pass

import time
import os,sys,py_compile
import traceback
import six.moves.cPickle
import re
import types

# Modules Eficas
from Noyau.N_CR import CR
from Editeur.catadesc import CatalogDescription

import analyse_catalogue
import analyse_catalogue_initial
import autre_analyse_cata
import uiinfo
from InterfaceQT4.monChoixCata import MonChoixCata
from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException

from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog

#-------------------------------
class ReaderCataCommun(object):
#-------------------------------

   def askChoixCatalogue(self, cata_choice_list):
   # ____________________________________________
      """
      Ouvre une fenetre de selection du catalogue dans le cas où plusieurs
      ont ete definis dans Accas/editeur.ini
      """
      code = getattr(self.appliEficas.maConfiguration, "code", None)
      if code != None :
          title=tr("Choix d une version du code ")+str(code)
      else :
          title=tr("Choix d une version ")

      widgetChoix = MonChoixCata(self.appliEficas, [cata.user_name for cata in cata_choice_list], title)
      ret=widgetChoix.exec_()


      lab=str(self.VERSION_EFICAS)+" "
      lab+=tr(" pour ")
      lab+=str(self.code)
      lab+=tr(" avec le catalogue ")
      if ret == QDialog.Accepted:
          cata = cata_choice_list[widgetChoix.CBChoixCata.currentIndex()]
          self.fic_cata = cata.cata_file_path
          self.versionCode = cata.identifier
          self.appliEficas.format_fichier = cata.file_format
          self.appliEficas.format_fichier_in = cata.file_format_in
          lab+=self.versionCode
          self.appliEficas.setWindowTitle(lab)
          #qApp.mainWidget().setCaption(lab)
          widgetChoix.close()
      else:
          widgetChoix.close()
          raise EficasException()

   def choisitCata(self):
   # ____________________

      liste_cata_possibles=[]
      self.Commandes_Ordre_Catalogue=[]

      all_cata_list = []
      for catalogue in self.appliEficas.maConfiguration.catalogues:
          if isinstance(catalogue, CatalogDescription): all_cata_list.append(catalogue)
          elif isinstance(catalogue, tuple)           : all_cata_list.append(CatalogDescription.create_from_tuple(catalogue))
          else: print(("Catalog description cannot be interpreted: ", catalogue))

      # This filter is only useful for codes that have subcodes (like MAP).
      # Otherwise, the "code" attribute of the catalog description can (should) be None.
      if self.ssCode is None: liste_cata_possibles = all_cata_list
      else:
          for catalogue in all_cata_list:
              if catalogue.code == self.code and catalogue.file_format == self.ssCode: liste_cata_possibles.append(catalogue)

      if len(liste_cata_possibles)==0:
          QMessageBox.critical(self.QWParent, tr("Import du catalogue"),
                               tr("Pas de catalogue defini pour le code ") + self.code)
          self.appliEficas.close()
          if self.appliEficas.salome == 0 : sys.exit(1)
          return


      if self.versionCode is not None:
          # La version a ete fixee
          for cata in liste_cata_possibles:
             if self.versionCode == cata.identifier:
                self.fic_cata = cata.cata_file_path
                self.appliEficas.format_fichier = cata.file_format
                self.appliEficas.format_fichier_in = cata.file_format_in
      else:
          cata_choice_list = []
          for cata in liste_cata_possibles:
              if cata.selectable:
                  if cata.default : cata_choice_list.insert(0, cata)
                  else            : cata_choice_list.append(cata)

          if len(cata_choice_list) == 0:
              QMessageBox.critical(self.QWParent, tr("Import du catalogue"),
                                   tr("Aucun catalogue trouve"))
              self.appliEficas.close()
              if self.appliEficas.salome == 0 : sys.exit(1)

          elif len(cata_choice_list) == 1:
              self.fic_cata = cata_choice_list[0].cata_file_path
              self.versionCode = cata_choice_list[0].identifier
              self.appliEficas.format_fichier = cata_choice_list[0].file_format
              self.appliEficas.format_fichier_in = cata_choice_list[0].file_format_in

          else:
              # plusieurs catalogues sont disponibles : il faut demander a l'utilisateur
              # lequel il veut utiliser ...
              self.askChoixCatalogue(cata_choice_list)
              self.demandeCatalogue=True

      if self.fic_cata == None :
          if self.appliEficas.salome == 0 :
             print(("Pas de catalogue pour code %s, version %s" %(self.code,self.versionCode)))
             sys.exit(1)
          else :
             self.appliEficas.close()
             return


#------------------------------------
class ReaderCata (ReaderCataCommun):
#------------------------------------

   def __init__(self,QWParent, appliEficas):
   # ______________________________________

      self.QWParent=QWParent
      self.appliEficas=self.QWParent.appliEficas
      self.VERSION_EFICAS=self.appliEficas.VERSION_EFICAS
      self.demandeCatalogue=False
      self.code=self.appliEficas.code
      self.ssCode=self.appliEficas.ssCode
      self.appliEficas.format_fichier='python'
      self.versionCode=self.appliEficas.versionCode
      self.fic_cata=None
      self.openCata()
      self.traiteIcones()
      self.cataitem=None
      self.creeDicoInverse()
      if self.code=="TELEMAC": self.creeDicoCasToCata()



   def openCata(self):
      """
          Ouvre le catalogue standard du code courant, cad le catalogue present
          dans le repertoire Cata
      """
      # import du catalogue
      self.choisitCata()

      if self.appliEficas.maConfiguration.withXSD :
         try :
           #import raw.Telemac2d as modeleMetier
           #import raw.cata_genere_fact as modeleMetier
           import raw.cata_map_genere as modeleMetier
           #import raw.cata_bloc as modeleMetier
           print ('import Test ad modeleMetier')
         except :
           modeleMetier = None
      else :
           modeleMetier = None

      self.cata = self.importCata(self.fic_cata)
      self.cata.modeleMetier = modeleMetier
      if not self.cata :
          QMessageBox.critical( self.QWParent, tr("Import du catalogue"),tr("Impossible d'importer le catalogue ")+ self.fic_cata)
          self.appliEficas.close()
          if self.appliEficas.salome == 0 :
             sys.exit(1)
      #
      # analyse du catalogue (ordre des mots-cles)
      #
      # retrouveOrdreCataStandard fait une analyse textuelle du catalogue
      # remplace par retrouveOrdreCataStandardAutre qui utilise une numerotation
      # des mots cles a la creation
      #print (self.cata)
      #print (dir(self.cata))
      self.retrouveOrdreCataStandardAutre()
      if self.appliEficas.maConfiguration.modeNouvCommande == "initial" : self.retrouveOrdreCataStandard()
      if hasattr(self.cata, 'Ordre_Des_Commandes') : self.Ordre_Des_Commandes=self.cata.Ordre_Des_Commandes
      else : self.Ordre_Des_Commandes=None

      if hasattr(self.cata, 'Classement_Commandes_Ds_Arbre') :
             self.Classement_Commandes_Ds_Arbre=self.cata.Classement_Commandes_Ds_Arbre
      else : self.Classement_Commandes_Ds_Arbre=()
      if hasattr(self.cata,'enum'):
         try :
           _temp= __import__(self.cata.enum,globals(), locals(), ['DicoEnumCasFrToEnumCasEn', 'TelemacdicoEn'], 0)
           self.DicoEnumCasFrToEnumCasEn = _temp.DicoEnumCasFrToEnumCasEn
           self.TelemacdicoEn = _temp.TelemacdicoEn
         except : pass

      #print self.cata.Ordre_Des_Commandes

      #
      # analyse des donnees liees l'IHM : UIinfo
      #
      uiinfo.traite_UIinfo(self.cata)

      #
      # traitement des clefs documentaires
      #

      self.titre=self.VERSION_EFICAS+" "+tr( " avec le catalogue ") + os.path.basename(self.fic_cata)
      if self.appliEficas.ssIhm == False : self.appliEficas.setWindowTitle(self.titre)
      self.appliEficas.titre=self.titre
      self.QWParent.titre=self.titre


   def importCata(self,cata):
      """
          Realise l'import du catalogue dont le chemin d'acces est donne par cata
      """
      nom_cata = os.path.splitext(os.path.basename(cata))[0]
      rep_cata = os.path.dirname(cata)
      sys.path[:0] = [rep_cata]
      self.appliEficas.listeAEnlever.append(rep_cata)


      if nom_cata in list(sys.modules.keys()) :
        del sys.modules[nom_cata]
      for k in sys.modules:
        if k[0:len(nom_cata)+1] == nom_cata+'.':
          del sys.modules[k]

      mesScriptsNomFichier='mesScripts_'+self.code.upper()
      try :
          self.appliEficas.mesScripts[self.code]=__import__(mesScriptsNomFichier)
      except:
          pass

      #if 1 :
      try :
          o=__import__(nom_cata)
          return o
      except Exception as e:
          traceback.print_exc()
          return 0



   def retrouveOrdreCataStandardAutre(self):
      """
          Construit une structure de donnees dans le catalogue qui permet
          a EFICAS de retrouver l'ordre des mots-cles dans le texte du catalogue.
          Pour chaque entite du catlogue on cree une liste de nom ordre_mc qui
          contient le nom des mots cles dans le bon ordre
      """
      self.cata_ordonne_dico, self.appliEficas.liste_simp_reel=autre_analyse_cata.analyseCatalogue(self.cata)
      #self.appliEficas.liste_simp_reel = ()
      #self.cata_ordonne_dico = {}

   def retrouveOrdreCataStandard(self):
      """
          Retrouve l'ordre des mots-cles dans le catalogue, cad :
          Attention s appuie sur les commentaires
      """
      nom_cata = os.path.splitext(os.path.basename(self.fic_cata))[0]
      rep_cata = os.path.dirname(self.fic_cata)
      self.Commandes_Ordre_Catalogue = analyse_catalogue_initial.analyseCatalogue(self.fic_cata)
      #print self.Commandes_Ordre_Catalogue

   def traiteIcones(self):
      if self.appliEficas.maConfiguration.ficIcones==None : return
      try:
        ficIcones=self.appliEficas.maConfiguration.ficIcones
        fichierIcones = __import__(ficIcones, globals(), locals(), [], -1)
        self.appliEficas.maConfiguration.dicoIcones=fichierIcones.dicoDesIcones.dicoIcones
        self.appliEficas.maConfiguration.dicoImages=fichierIcones.dicoDesIcones.dicoImages
      except:
        print ("Pas de fichier associe contenant des liens sur les icones ")
        self.appliEficas.maConfiguration.dicoIcones={}



   def creeDicoInverse(self):
        self.dicoInverse={}
        self.dicoMC={}
        listeEtapes=self.cata.JdC.commandes
        for e in self.cata.JdC.commandes:
            self.traiteEntite(e)


   def creeDicoCasToCata(self):
      if hasattr(self.cata,'dicoCasEn'):
        _temp= __import__(self.cata.dicoCasEn,globals(), locals(), ['DicoCasEnToCata'], 0)
        if self.appliEficas.langue=="ang" :
           self.dicoCasToCata=_temp.dicoCasEnToCata
        else :
           self.dicoCasToCata=_temp.dicoCasFrToCata



   def traiteEntite(self,e):
       boolIn=0
       for (nomFils, fils) in list(e.entites.items()) :
          self.dicoMC[nomFils]=fils
          self.traiteEntite(fils)
          boolIn=1
       if boolIn==0 :
          liste=[]
          moi=e
          while hasattr(moi,'pere') :
                liste.append((moi.nom,moi))
                moi=moi.pere
          liste.append((moi.nom,moi))
          self.dicoInverse[e.nom]=liste
          self.dicoInverse[tr(e.nom)]=liste

   def creeRubrique(self,e,dico, niveau):
       from Accas import A_BLOC
       decale=niveau*"   "
       #if niveau != 0 :
       #    if isinstance(e,A_BLOC.BLOC): print decale, e.condition
       #    else :                           print decale, e. nom
       for (nom, fils) in list(e.entites.items()) :
           if  list(fils.entites.items()) != [] : self.creeRubrique(fils,dico,niveau+1)
           #else : print (niveau+1)*"   ", nom


   def dumpToXsdEficas(self):
       # Pas sur qu on ait jamais besoin de cela
       pass
       #from Efi2Xsd import readerEfficas
       #newSchema=   xml = open('Cata_MED_FAM.xml').read()
       #SchemaMed = efficas.CreateFromDocument(xml)
       #SchemaMed.alimenteCata(self.cata)

