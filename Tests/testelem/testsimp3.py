# coding=utf-8
from Accas import SIMP,ASSD
from Extensions.param2 import Variable,cos

import unittest

class TestSimpCase(unittest.TestCase):
   def setUp(self):
       pass

   def tearDown(self):
       pass

   def test001(self):
       a=Variable("n",25.6)
       self.assertEqual(repr(a),"Variable('n',25.6)")
       self.assertEqual(str(a),"n")
       self.assertEqual(a.eval(),25.6)
       b=-a
       self.assertEqual(str(b),"-(n)")
       self.assertEqual(b.eval(),-25.6)
       b=-a*100+3/2
       self.assertEqual(str(b),'((-(n) * 100) + 1)')
       self.assertEqual(b.eval(),-2559)
       b=a/10
       self.assertEqual(str(b),'(n / 10)')
       self.assertEqual(b.eval(),2.56)
       c=Variable('q',[1,a,3])
       d=c[1]/3
       self.assertEqual(str(d),'((q[1]) / 3)')
       self.assertEqual(d.eval(),25.6/3)
       f=cos(d)
       self.assertEqual(str(f),'cos(((q[1]) / 3))')
       self.assertEqual(f.eval(),-0.628288791022798)
       g=a**2
       self.assertEqual(str(g),'(n ** 2)')
       self.assertEqual(g.eval(),655.36000000000013)
       h=2*Variable("x",2)
       g=a**h
       self.assertEqual(str(g),'(n ** (2 * x))')
       self.assertEqual(g.eval(),429496.72960000008)

   def test003(self):
       cata=SIMP(statut='o',typ='R',max=3)
       liste=((1,1),(Variable('x',(0.,1.)),1), (1.,1),(Variable('x',(0.,1.)),1), (('RI',1,0),0),
              (1+0j,0), ("('RI',1,0)",0), ("toto",0), (None,0),
             )
       for valeur,valid in liste:
           o=cata(valeur,'mcs',None)
           print o.val,o.valeur
           msg="erreur sur le test %s %s" % (valeur,valid)+'\n'+str(o.report())
           self.assertEqual(o.isvalid(),valid,msg=msg)
