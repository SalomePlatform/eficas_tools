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

   i=0
   for f in ("params.comm",):
      file=os.path.join(prefs.INSTALLDIR,"Tests/testelem",f)
      i=i+1
      exec """def test%s(self,file="%s"):
                  "fichier : %s"
                  self.commtest(file)
""" % (i,file,f)
   del i

   def commtest(self,file):
      """ Test de lecture/ecriture de fichier .comm"""
      #print file
      app=appli.STANDALONE(version=version)
      j=app.openJDC(file=file)
      assert j.isValid(),j.report()

      text1=app.getTextJDC(j,'python')
      f=open(file)
      text2=f.read()
      f.close()
      assert text1 == text2 , cdiff(text2,text1)

