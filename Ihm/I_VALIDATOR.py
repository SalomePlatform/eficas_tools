# -*- coding: utf-8 -*-

from Noyau.N_VALIDATOR import *

class Compulsory(Compulsory):
      def has_into(self):
          return 0
      def valide_liste_partielle(self,liste_courante=None):
          return 1

class OrdList(OrdList):
      def valide_liste_partielle(self,liste_courante=None):
          """
           Méthode de validation de liste partielle pour le validateur OrdList
          """
          try:
             self.convert(liste_courante)
             valid=1
          except:
             valid=0
          return valid

