# -*- coding: utf-8 -*-
"""
   Ce module contient des classes permettant de définir des validateurs
   pour EFICAS. Ces classes constituent un complément à des classes existantes
   dans Noyau/N_VALIDATOR.py ou de nouvelles classes de validation.
   Ces classes complémentaires ne servent que pour l'IHM d'EFICAS.
   Elles servent essentiellement à ajouter des comportements spécifiques
   IHM aux classes existantes dans le Noyau.
   Ces comportements pourront etre rapatries dans le Noyau quand leur
   interface sera stabilisée.
"""

import types

class Valid:
   """
        Cette classe est la classe mere de toutes les classes complémentaires
        que l'on trouve dans Ihm.
   """

class ListVal(Valid):pass

class RangeVal(ListVal):pass

class CardVal(Valid):pass

class PairVal(ListVal):pass

class EnumVal(ListVal):pass
          
class NoRepeat(ListVal):pass

class LongStr(ListVal):pass

class OrdList(ListVal):pass

CoercableFuncs = { types.IntType:     int,
                   types.LongType:    long,
                   types.FloatType:   float,
                   types.ComplexType: complex,
                   types.UnicodeType: unicode }

class TypeVal(ListVal):pass

class InstanceVal(ListVal):pass

class FunctionVal(Valid):pass

class OrVal(Valid):pass

class AndVal(Valid):pass

