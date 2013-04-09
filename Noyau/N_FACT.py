# -*- coding: iso-8859-1 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#


""" Ce module contient la classe de definition FACT
    qui permet de spécifier les caractéristiques des mots clés facteurs
"""

import types

import N_ENTITE
import N_MCFACT
import N_MCLIST
from N__F import _F
from N_types import is_sequence
from strfunc import ufmt

import N_OBJECT

class FACT(N_ENTITE.ENTITE):
   """
    Classe pour definir un mot cle facteur

    Cette classe a trois attributs de classe

      - class_instance qui indique la classe qui devra etre utilisée
        pour créer l'objet qui servira à controler la conformité d'un
        mot-clé facteur avec sa définition

      - list_instance

      - label qui indique la nature de l'objet de définition (ici, FACT)
   """
   class_instance = N_MCFACT.MCFACT
   list_instance = N_MCLIST.MCList
   label = 'FACT'

   def __init__(self,fr="",ang="",docu="",regles=(),statut='f',defaut=None,
                     min=0,max=1,validators=None,**args):

      """
          Un mot-clé facteur est caractérisé par les attributs suivants :

            - fr   :
            - ang :
            - statut :
            - defaut :
            - regles
            - min
            - max
            - position
            - docu
      """
      N_ENTITE.ENTITE.__init__(self,validators)
      # Initialisation des attributs
      self.fr=fr
      self.ang=ang
      self.docu = docu
      if type(regles)== types.TupleType:
          self.regles=regles
      else:
          self.regles=(regles,)
      self.statut=statut
      self.defaut=defaut
      self.min=min
      self.max=max
      self.entites=args
      self.position=None
      self.affecter_parente()

   def __call__(self,val,nom,parent):
      """
          Construit la structure de donnee pour un mot cle facteur a partir
          de sa definition (self) de sa valeur (val), de son nom (nom) et de
          son parent dans l arboresence (parent)

          Suivant le type de la valeur on retournera soit un objet de type
          MCFACT soit une liste de type MCLIST.

          La creation d un mot cle facteur depend de son statut
            - Si statut ='o'   il est obligatoire
            - Si statut == 'd' il est facultatif mais ses sous mots cles avec
              defaut sont visibles
            - Si statut == 'f' il est facultatif et ses sous mots avec defaut ne
              sont pas visibles
            - Si statut == 'c' il est cache ???
            - Si defaut != None, on utilise cette valeur pour calculer la valeur
              par defaut du mot cle facteur
      """
      if val is None:
        if self.defaut == None:
          val={}
        elif type(self.defaut) == types.TupleType:
          val=self.defaut
              # Est ce utile ? Le défaut pourrait etre uniquement un dict
        elif type(self.defaut) == types.DictType or isinstance(self.defaut,_F):
          val=self.defaut
        else:
          # On ne devrait jamais passer par la
          print "On ne devrait jamais passer par la"
          return None
      elif is_sequence(val) and len(val) == 0 and self.statut == 'o':
          # On est dans le cas où le mcfact est présent mais est une liste/tuple
          # vide. Il est obligatoire donc on l'initialise. Les règles, mots-clés
          # obligatoires diront si un mcfact vide est accepté.
          val = {}

      # On cree toujours une liste de mcfact
      l=self.list_instance()
      l.init(nom = nom,parent=parent)
      if type(val) in (types.TupleType, types.ListType, self.list_instance) :
         for v in val:
            if type(v) == types.DictType or isinstance(v, _F):
               objet=self.class_instance(nom=nom,definition=self,val=v,parent=parent)
               l.append(objet)
            elif isinstance(v, self.class_instance):
               l.append(v)
            else:
               l.append(N_OBJECT.ErrorObj(self,v,parent,nom))
      elif type(val) == types.DictType or isinstance(val, _F):
         objet=self.class_instance(nom=nom,definition=self,val=val,parent=parent)
         l.append(objet)
      elif isinstance(val, self.class_instance):
         l.append(val)
      else:
         l.append(N_OBJECT.ErrorObj(self,val,parent,nom))

      return l

   def verif_cata(self):
      self.check_min_max()
      self.check_fr()
      self.check_regles()
      self.check_statut()
      self.check_docu()
      self.check_validators()
      self.verif_cata_regles()
