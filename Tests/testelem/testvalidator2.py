# coding=utf-8
from Accas import *
from Extensions.param2 import Variable

import unittest
import compare
OK="""Mot-cl� simple : mcs
Fin Mot-cl� simple : mcs
"""
from cata5 import entier

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
           self.assert_(valid,msg=msg)

   def test001(self):
       """ Validateur LongStr(3,5) """
       cata=SIMP(typ='TXM',validators=LongStr(3,5))
       liste=(("aa",
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : 'aa' n'est pas de la bonne longueur !
   ! Critere de validite: longueur de la chaine entre 3 et 5    !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),("aaa",OK),
              ("aaaa",OK),("aaaaa",OK),
              ("axyzaa",
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : 'axyzaa' n'est pas de la bonne longueur !
   ! Critere de validite: longueur de la chaine entre 3 et 5        !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),("bbbbaaa",
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : 'bbbbaaa' n'est pas de la bonne longueur !
   ! Critere de validite: longueur de la chaine entre 3 et 5         !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
              (Variable('x',"aaa"),OK),
              (Variable('x',"aaaaaaaaaaaa"),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : 'aaaaaaaaaaaa' n'est pas de la bonne longueur !
   ! Critere de validite: longueur de la chaine entre 3 et 5              !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
             )
       self._test(cata,liste)

   def test010(self):
       cata=SIMP(statut='o',typ='TXM',min=1,max=6,validators=NoRepeat())
       liste=(
              ("aa",OK),("aaa",OK),
              (("aaaa","aaaaa","axyzaa","bbbbaaa","zzz"),OK),
              (("aaaa","aaaa","axyz","bbbb","zzz"),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : aaaa est un doublon                      !
   ! Critere de validite: : pas de pr�sence de doublon dans la liste !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
              (("aaaa","axyz","bbbb","zzz"),OK),
              ("aaaa",OK),("aaaaa",OK),
              ("axyzaa",OK),("bbbbaaa",OK),
              (("aaa",Variable('x',"bbb")),OK),
              (("aaa",Variable('x',"aaa")),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : aaa est un doublon                       !
   ! Critere de validite: : pas de pr�sence de doublon dans la liste !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
              (Variable('x',("aaa","bbb")),OK),
              (Variable('x',("aaa","bbb","bbb")),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : bbb est un doublon                       !
   ! Critere de validite: : pas de pr�sence de doublon dans la liste !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
             )
       self._test(cata,liste)

   def test011(self):
       cata=SIMP(statut='o',typ='TXM',min=1,max=6,into =( "TUTU","TATA","CCCC"),validators=NoRepeat())
       liste=(
              ("TUTU",OK),("TATA",OK),
              (("TUTU","TATA","CCCC"),OK),
              (("TUTU","TATA","CCCC","TUTU","TATA","CCCC"),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : TUTU est un doublon                      !
   ! Critere de validite: : pas de pr�sence de doublon dans la liste !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
              (("TUTU","TATA","CCCC","TUTU","TATA","CCCC","TUTU","TATA","CCCC"),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Nombre d'arguments de ('TUTU', 'TATA', 'CCCC', 'TUTU', 'TATA', 'CCCC', 'TUTU', !
   ! 'TATA', 'CCCC') incorrect (min = 1, max = 6)                                   !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
             )
       self._test(cata,liste)

   def test016(self):
       """Test du validateur ET : pas de doublon ET valeur paire """
       cata=SIMP(statut='o',typ='I',min=1,max=6,validators=[NoRepeat(),PairVal()])
       liste=( ((2,),OK),(None,
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� :  mcs  obligatoire non valoris� !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! None n'est pas une valeur autoris�e !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),((1,3,5),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : (1, 3, 5) contient des valeurs non paires !
   ! Critere de validite: : pas de pr�sence de doublon dans la liste  !
   !  et valeur paire                                                 !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
               ((2,4,6),OK),
               ((2,4,4),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : 4 est un doublon                         !
   ! Critere de validite: : pas de pr�sence de doublon dans la liste !
   !  et valeur paire                                                !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
             )
       self._test(cata,liste)

   def test017(self):
       """Test du validateur NoRepeat avec objet entier """
       cata=SIMP(statut='o',typ='I',min=1,max=6,validators=NoRepeat())
       i=entier()
       liste=( (i,OK),
               ((i,i),OK),
               ((1,i,i),OK),
               ((i,1,i,i),OK),
               ((1,1,i,i),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : 1 est un doublon                         !
   ! Critere de validite: : pas de pr�sence de doublon dans la liste !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
""" ),
               )
       self._test(cata,liste)

   def test018(self):
       """Test du validateur OrdList('croissant') avec objet entier """
       cata=SIMP(statut='o',typ='I',min=1,max=6,validators=OrdList('croissant'))
       i=entier()
       liste=( (i,OK),
               ((i,i),OK),
               ((1,i,i),OK),
               ((i,1,i,i),OK),
               ((2,1,i,i),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : (2, 1, <concept entier>, <concept entier>) n'est pas par !
   ! valeurs croissantes                                                             !
   ! Critere de validite: liste croissant                                            !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
"""),
               )
       self._test(cata,liste)

   def test019(self):
       """Test du validateur Compulsory avec objet entier """
       cata=SIMP(statut='o',typ='I',min=1,max=6,validators=Compulsory((5,6,7)))
       i=entier()
       liste=( ((5,6,7),OK),
               ((5,6,7,i),OK),
               ((i,5,6,7,i),OK),
               ((i,5,7,i),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : (<concept entier>, 5, 7, <concept entier>) ne contient !
   ! pas les elements obligatoires : [6]                                           !
   ! Critere de validite: valeur (5, 6, 7) obligatoire                             !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
""" ),
               )
       self._test(cata,liste)

   def test020(self):
       """Test du validateur NoRepeat OU Compulsory avec objet entier """
       cata=SIMP(statut='o',typ='I',min=1,max=6,validators=(NoRepeat(),Compulsory((5,6,7))))
       i=entier()
       liste=( ((5,6,7),OK),
               ((5,6,7,i),OK),
               ((i,5,6,7,i),OK),
               ((i,5,7,i), OK ),
               )
       self._test(cata,liste)

   def test021(self):
       """Test du validateur NoRepeat ET Compulsory avec objet entier """
       cata=SIMP(statut='o',typ='I',min=1,max=6,validators=[NoRepeat(),Compulsory((5,6,7))])
       i=entier()
       liste=( ((5,6,7),OK),
               ((5,6,7,i),OK),
               ((i,5,6,7,i),OK),
               ((i,5,7,i),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : (<concept entier>, 5, 7, <concept entier>) ne contient !
   ! pas les elements obligatoires : [6]                                           !
   ! Critere de validite: : pas de pr�sence de doublon dans la liste               !
   !  et valeur (5, 6, 7) obligatoire                                              !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
""" ),
               )
       self._test(cata,liste)

   def test022(self):
       """Test du validateur Compulsory(5,6,7) ET OrdList('croissant') avec objet entier """
       cata=SIMP(statut='o',typ='I',min=1,max=6,validators=[Compulsory((5,6,7)),OrdList('croissant')])
       i=entier()
       liste=( ((5,6,7),OK),
               ((5,6,7,i),OK),
               ((i,5,6,7,i),OK),
               ((i,5,7,i),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : (<concept entier>, 5, 7, <concept entier>) ne contient !
   ! pas les elements obligatoires : [6]                                           !
   ! Critere de validite: valeur (5, 6, 7) obligatoire                             !
   !  et liste croissant                                                           !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
""" ),
               ((i,5,7,i,6),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : (<concept entier>, 5, 7, <concept entier>, 6) n'est pas !
   ! par valeurs croissantes                                                        !
   ! Critere de validite: valeur (5, 6, 7) obligatoire                              !
   !  et liste croissant                                                            !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
""" ),
               )
       self._test(cata,liste)

   def test023(self):
       """Test du validateur Compulsory(5,6,7) ET OrdList('croissant') ET NoRepeat() avec objet entier """
       cata=SIMP(statut='o',typ='I',min=1,max=6,validators=[Compulsory((5,6,7)),OrdList('croissant'),NoRepeat()])
       i=entier()
       liste=( ((5,6,7),OK),
               ((5,6,7,i),OK),
               ((i,5,6,7,i),OK),
               ((i,5,7,i),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : (<concept entier>, 5, 7, <concept entier>) ne contient !
   ! pas les elements obligatoires : [6]                                           !
   ! Critere de validite: valeur (5, 6, 7) obligatoire                             !
   !  et liste croissant                                                           !
   !  et : pas de pr�sence de doublon dans la liste                                !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
""" ),
               ((i,5,7,i,6),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : (<concept entier>, 5, 7, <concept entier>, 6) n'est pas !
   ! par valeurs croissantes                                                        !
   ! Critere de validite: valeur (5, 6, 7) obligatoire                              !
   !  et liste croissant                                                            !
   !  et : pas de pr�sence de doublon dans la liste                                 !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
""" ),
               ((i,5,i,6,7,7),
"""Mot-cl� simple : mcs
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   ! Mot-cl� mcs invalide : 7 est un doublon           !
   ! Critere de validite: valeur (5, 6, 7) obligatoire !
   !  et liste croissant                               !
   !  et : pas de pr�sence de doublon dans la liste    !
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Fin Mot-cl� simple : mcs
""" ),
               ((i,5,6,7,i,8),OK),
               )
       self._test(cata,liste)
