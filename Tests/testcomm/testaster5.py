import os,glob,sys
import unittest

from Editeur import appli

from config import ASTERDIR

class TestCase(unittest.TestCase):
   app=None
   def setUp(self):
      if self.app == None:
         self.app=appli.STANDALONE(version='v8.3')
      pass

   def tearDown(self):
      CONTEXT.unset_current_step()

   i=0
   for f in glob.glob(os.path.join(ASTERDIR,"ssl[a-l]*.comm")):
      ff=open(f)
      text=ff.read()
      ff.close()
      if text.find("VISU_EFICAS='NON'") != -1:continue
      for o in ('3','2','1','0','m'):
       f=f[:-1]+o
       if os.path.isfile(f):
          ff=open(f)
          text=ff.read()
          ff.close()
          if text.find("VISU_EFICAS='NON'") == -1: break
      i=i+1
      exec """def test%s(self,file="%s"):
                  "fichier:%s"
                  self.commtest(file)
""" % (i,f,f)
   del i,f,o,ff,text

   def commtest(self,file):
      """ Test generique"""
      j=self.app.openJDC(file=file)
      assert j.isvalid(),j.report()
      j.supprime()
      assert sys.getrefcount(j) == 2,sys.getrefcount(j)

