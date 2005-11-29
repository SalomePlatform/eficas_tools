# coding=utf-8
from Accas import SIMP,ASSD
class maillage(ASSD):pass
class maillage_sdaster(ASSD):pass

import unittest

class TestMCSimpCase(unittest.TestCase):
   def setUp(self):
      self.cata=SIMP(typ='I',statut='o')

   def tearDown(self):
      del self.cata

   def test001(self):
      cata=SIMP(typ='I',max=5)
      o=cata((1,2,'aa','bb',7,'cc'),'mcs1',None)
      cr=o.report()
      expected_cr="""Mot-clé simple : mcs1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! 'aa' n'est pas d'un type autorisé !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Nombre d'arguments de (1, 2, 'aa', 'bb', 7, 'cc') incorrect pour mcs1 (min = 1, !
   ! max = 5)                                                                        !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs1
"""
      self.assertEqual(str(cr) , expected_cr,msg='Erreur :\n%s\n!=\n%s' % (str(cr),expected_cr))

   def test002(self):
      cata=SIMP(typ='I',max=7,into=(1,2,'aa','bb',7,'cc'))
      o=cata((1,2,'aa','bb',7,'cc'),'mcs1',None)
      cr=o.report()
      expected_cr="""Mot-clé simple : mcs1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! 'aa' n'est pas d'un type autorisé !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs1
"""
      self.assertEqual(str(cr) , expected_cr,msg='Erreur :\n%s\n!=\n%s' % (str(cr),expected_cr))

   def test003(self):
      cata=SIMP(typ='R',max=7,into=(1,2,7))
      o=cata((1,2,7,3,4,5,6),'mcs1',None)
      cr=o.report()
      expected_cr="""Mot-clé simple : mcs1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! La valeur : 3  n'est pas permise pour le mot-clé : mcs1 !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs1
"""
      self.assertEqual(str(cr) , expected_cr,msg='Erreur :\n%s\n!=\n%s' % (str(cr),expected_cr))

   def test004(self):
      cata=SIMP(typ='R',max=7,val_max=6)
      o=cata((1,2,7,3,4,5,6),'mcs1',None)
      cr=o.report()
      expected_cr="""Mot-clé simple : mcs1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! La valeur : 7  du mot-clé  mcs1  est en dehors du domaine de validité [ 6 , 6 ] !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs1
"""
      self.assertEqual(str(cr) , expected_cr,msg='Erreur :\n%s\n!=\n%s' % (str(cr),expected_cr))

   def test005(self):
      cata=SIMP(typ='R',max=6,val_max=6)
      o=cata((1,2,7,3,4,5,6),'mcs1',None)
      cr=o.report()
      expected_cr="""Mot-clé simple : mcs1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! La valeur : 7  du mot-clé  mcs1  est en dehors du domaine de validité [ 6 , 6 ] !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Nombre d'arguments de (1, 2, 7, 3, 4, 5, 6) incorrect pour mcs1 (min = 1, max = !
   ! 6)                                                                              !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs1
"""
      self.assertEqual(str(cr) , expected_cr,msg='Erreur :\n%s\n!=\n%s' % (str(cr),expected_cr))

   def test006(self):
      cata=SIMP(typ='R',max=6,val_max=6)
      o=cata((1,2,7,"aa",4,"bb",6),'mcs1',None)
      cr=o.report()
      expected_cr="""Mot-clé simple : mcs1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! 'aa' n'est pas d'un type autorisé !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! La valeur : 7  du mot-clé  mcs1  est en dehors du domaine de validité [ 6 , 6 ] !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Nombre d'arguments de (1, 2, 7, 'aa', 4, 'bb', 6) incorrect pour mcs1 (min = 1, !
   ! max = 6)                                                                        !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs1
"""
      self.assertEqual(str(cr) , expected_cr,msg='Erreur :\n%s\n!=\n%s' % (str(cr),expected_cr))

   def test007(self):
      """
        La liste devrait etre homogene en type
      """
      cata=SIMP(typ=('R','TXM'),max=6,val_max=6)
      o=cata((1,2,7,"aa",4,"bb",6),'mcs1',None)
      cr=o.report()
      expected_cr="""Mot-clé simple : mcs1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! 'aa' n'est pas d'un type autorisé !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! La valeur : 7  du mot-clé  mcs1  est en dehors du domaine de validité [ 6 , 6 ] !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Nombre d'arguments de (1, 2, 7, 'aa', 4, 'bb', 6) incorrect pour mcs1 (min = 1, !
   ! max = 6)                                                                        !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs1
"""
      self.assertEqual(str(cr) , expected_cr,msg='Erreur :\n%s\n!=\n%s' % (str(cr),expected_cr))

