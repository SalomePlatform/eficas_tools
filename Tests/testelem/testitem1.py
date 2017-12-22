import os
import unittest
import difflib

import prefs
from InterfaceTK import appli
#from Editeur import appli
from Editeur import comploader
from Editeur import Objecttreeitem


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

version= 'v9'

class TestCase(unittest.TestCase):
   """ Tests sur des items """
   def setUp(self):
      pass

   def tearDown(self):
      CONTEXT.unsetCurrentStep()

   def test001(self):
      """Test comploader"""
      composants=comploader.chargerComposants()
      itemtype=comploader.gettreeitem({'a':1})
      assert itemtype is Objecttreeitem.ObjectTreeItem

   def test002(self):
      """ Test de commentarisation/decommentarisation a partir d'un item jdc """
      app=appli.STANDALONE(version=version)
      file=os.path.join(prefs.INSTALLDIR,"Tests/testelem/az.comm")
      j=app.openJDC(file=file)
      item=app.create_item(j)
      assert item.isValid(),item.report()
      # on commente la commande LIRE_MAILLAGE
      commands=item.getSubList()
      for it in commands:
        if it.nom == "LIRE_MAILLAGE" and it.sd.nom == "MAIL":break
      pos=commands.index(it)
      cco=it.getObjetCommentarise()
      commands=item.getSubList()
      commands[pos].unComment()
      commands=item.getSubList()
      # on reaffecte l'objet MAIL
      for it in commands:
        if it.nom in ("AFFE_MODELE","AFFE_MATERIAU") :
           for mc in it.getSubList():
              if mc.nom == "MAILLAGE":
                 valeur,validite=mc.evalValeur("MAIL")
                 test = mc.set_valeur(valeur)
      text1=app.get_text_JDC(j,'python')
      f=open(file)
      text2=f.read()
      f.close()
      assert text1 == text2 , cdiff(text1,text2)

