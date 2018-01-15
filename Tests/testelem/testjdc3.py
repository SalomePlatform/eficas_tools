# coding=utf-8
import os
import unittest
import difflib
import compare

import prefs
from InterfaceTK import appli
#from Editeur import appli
from Accas import AsException

def add_param(j,pos,nom,valeur):
    co=j.addEntite("PARAMETRE",pos)
    co.setNom(nom)
    co.set_valeur(valeur)
    return co

def add_mcsimp(obj,nom,valeur):
    mcs=obj.getChild(nom,restreint='oui')
    if mcs is None:
       pos=obj.getIndexChild(nom)
       mcs=obj.addEntite(nom,pos)
    mcs.set_valeur(mcs.evalVal(valeur))
    return mcs

def cdiff(text1,text2):
    return " ".join(difflib.context_diff(text1.splitlines(1),text2.splitlines(1)))

version='v9'

class TestCase(unittest.TestCase):
   def setUp(self):
      pass

   def tearDown(self):
      CONTEXT.unsetCurrentStep()

   def test001(self):
      """ Test de commentarisation/decommentarisation de commandes dans fichier az.comm"""
      app=appli.STANDALONE(version=version)
      file=os.path.join(prefs.INSTALLDIR,"Tests/testelem/az.comm")
      j=app.openJDC(file=file)
      assert j.isValid(),j.report()
      # on commente la commande LIRE_MAILLAGE
      for co in j.etapes:
        if co.nom == "LIRE_MAILLAGE" and co.sd.nom == "MAIL":break
      cco=co.getObjetCommentarise(format=app.format_fichier.get())
      # on decommente la commande LIRE_MAILLAGE
      commande,nom = cco.unComment()
      # on reaffecte l'objet MAIL
      for co in j.etapes:
        if co.nom in ("AFFE_MODELE","AFFE_MATERIAU") :
           add_mcsimp(co,"MAILLAGE",'MAIL')

      text1=app.getTextJDC(j,'python')
      f=open(file)
      text2=f.read()
      f.close()
      assert text1 == text2 , cdiff(text1,text2)

   def test002(self):
      """ Test de commentarisation/decommentarisation de macro commande dans fichier az.comm"""
      app=appli.STANDALONE(version=version)
      file=os.path.join(prefs.INSTALLDIR,"Tests/testelem/az.comm")
      j=app.openJDC(file=file)
      assert j.isValid(),j.report()
      # on commente la commande MACRO_MATR_ASSE
      for co in j.etapes:
        if co.nom == "MACRO_MATR_ASSE" :break
      cco=co.getObjetCommentarise(format=app.format_fichier.get())
      # on decommente la commande MACRO_MATR_ASSE
      commande,nom = cco.unComment()
      assert j.isValid(),j.report()

   def test003(self):
      """ Test de commentarisation/decommentarisation de commandes dans fichier az.comm"""
      app=appli.STANDALONE(version=version)
      text="""
DEBUT()
MA=LIRE_MAILLAGE()
FIN()
"""
      j=app.openTXT(text)
      assert j.isValid(),j.report()
      # on commente la commande LIRE_MAILLAGE
      co=j.etapes[1]
      cco=co.getObjetCommentarise(format=app.format_fichier.get())
      co=j.addEntite("LIRE_MAILLAGE",2)
      test,mess=co.nommeSd("MA")
      # on decommente la commande LIRE_MAILLAGE
      commande,nom = cco.unComment()
      expected="""DEBUT CR validation : TEXT
   Etape : LIRE_MAILLAGE    ligne : ...
      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      ! Concept retourné non défini !
      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   Fin Etape : LIRE_MAILLAGE
FIN CR validation :TEXT
"""
      msg=str( j.report())
      assert compare.check(expected,msg),cdiff(expected,msg)

   def test004(self):
      """ Test de commentarisation/decommentarisation de commandes dans fichier az.comm"""
      app=appli.STANDALONE(version=version)
      text="""
DEBUT()
MA=LIRE_MAILLAGE()
AFFE_MODELE(MAILLAGE=MA)
FIN()
"""
      j=app.openTXT(text)
      # on commente la commande LIRE_MAILLAGE
      co=j.etapes[1]
      cco=co.getObjetCommentarise(format=app.format_fichier.get())
      # on commente la commande AFFE_MODELE
      co=j.etapes[2]
      cco2=co.getObjetCommentarise(format=app.format_fichier.get())
      # on decommente la commande AFFE_MODELE
      commande,nom = cco2.unComment()
      assert commande["MAILLAGE"] == None

   def test005(self):
      """ Test de commentarisation/decommentarisation de commandes dans fichier az.comm"""
      app=appli.STANDALONE(version=version)
      text="""
DEBUT()
MA=LIRE_MAILLAGE()
AFFE_MODELE(MAILLAGE=MA)
FIN()
"""
      j=app.openTXT(text)
      # on commente la commande AFFE_MODELE
      co=j.etapes[2]
      cco2=co.getObjetCommentarise(format=app.format_fichier.get())
      # on commente la commande LIRE_MAILLAGE
      co=j.etapes[1]
      cco=co.getObjetCommentarise(format=app.format_fichier.get())
      # on decommente la commande AFFE_MODELE
      self.assertRaises(AsException, cco2.unComment, )

