# coding=utf-8
from Accas import *

import unittest
import compare
OK="""Mot-clé simple : mcs
Fin Mot-clé simple : mcs
"""

class TestValidCase(unittest.TestCase):
   def setUp(self):
       pass

   def tearDown(self):
       pass

   def _test(self,cata,liste):
       for valeur,report in liste:
           o=cata(valeur,'mcs',None)
           msg=""
           rep=str(o.report())
           valid=compare.check(rep,report)
           if not valid:
              msg="le rapport d'erreur est incorrect.\n valeur = %s\n expected =\n%s\n got =\n%s " % (valeur,report,rep)
              print msg
           self.assert_(valid,msg=msg)

   def test001(self):
       """ Validateur LongStr(3,5) """
       cata=SIMP(typ='TXM',validators=LongStr(3,5))
       liste=(("aa",
"""Mot-clé simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-clé :  mcs devrait avoir  longueur de la chaine entre 3 et 5 !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs
"""),("aaa",OK),
              ("aaaa",OK),("aaaaa",OK),
              ("axyzaa",
"""Mot-clé simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-clé :  mcs devrait avoir  longueur de la chaine entre 3 et 5 !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs
"""),("bbbbaaa",
"""Mot-clé simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-clé :  mcs devrait avoir  longueur de la chaine entre 3 et 5 !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs
"""),
             )
       self._test(cata,liste)

   def test010(self):
       cata=SIMP(statut='o',typ='TXM',min=1,max=6,validators=NoRepeat())
       liste=(
              ("aa",OK),("aaa",OK),
              (("aaaa","aaaaa","axyzaa","bbbbaaa","zzz"),OK),
              (("aaaa","aaaa","axyz","bbbb","zzz"),
"""Mot-clé simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-clé :  mcs devrait avoir  : pas de présence de doublon dans la liste !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs
"""),
              (("aaaa","axyz","bbbb","zzz"),OK),
              ("aaaa",OK),("aaaaa",OK),
              ("axyzaa",OK),("bbbbaaa",OK),
             )
       self._test(cata,liste)

   def test011(self):
       cata=SIMP(statut='o',typ='TXM',min=1,max=6,into =( "TUTU","TATA","CCCC"),validators=NoRepeat())
       liste=(
              ("TUTU",OK),("TATA",OK),
              (("TUTU","TATA","CCCC"),OK),
              (("TUTU","TATA","CCCC","TUTU","TATA","CCCC"),
"""Mot-clé simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-clé :  mcs devrait avoir  : pas de présence de doublon dans la liste !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs
"""),
              (("TUTU","TATA","CCCC","TUTU","TATA","CCCC","TUTU","TATA","CCCC"),
"""Mot-clé simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Nombre d'arguments de ('TUTU', 'TATA', 'CCCC', 'TUTU', 'TATA', 'CCCC', 'TUTU', !
   ! 'TATA', 'CCCC') incorrect pour mcs (min = 1, max = 6)                          !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs
"""),
             )
       self._test(cata,liste)

   def test016(self):
       """Test du validateur ET : pas de doublon ET valeur paire """
       cata=SIMP(statut='o',typ='I',min=1,max=6,validators=[NoRepeat(),PairVal()])
       liste=( ((2,),OK),(None,
"""Mot-clé simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-clé :  mcs  obligatoire non valorisé !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! None n'est pas une valeur autorisée !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs
"""),((1,3,5),
"""Mot-clé simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-clé :  mcs devrait avoir  : pas de présence de doublon dans la liste !
   !  et valeur paire                                                         !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs
"""),
               ((2,4,6),OK),
               ((2,4,4),
"""Mot-clé simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-clé :  mcs devrait avoir  : pas de présence de doublon dans la liste !
   !  et valeur paire                                                         !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-clé simple : mcs
"""),
             )
       self._test(cata,liste)
