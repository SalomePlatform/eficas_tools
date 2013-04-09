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

""" Ce module contient la classe de definition SIMP
    qui permet de sp�cifier les caract�ristiques des mots cl�s simples
"""

import types

import N_ENTITE
import N_MCSIMP
from strfunc import ufmt

class SIMP(N_ENTITE.ENTITE):
   """
    Classe pour definir un mot cle simple

    Cette classe a deux attributs de classe

    - class_instance qui indique la classe qui devra etre utilis�e
            pour cr�er l'objet qui servira � controler la conformit� d'un
            mot-cl� simple avec sa d�finition

    - label qui indique la nature de l'objet de d�finition (ici, SIMP)

   """
   class_instance = N_MCSIMP.MCSIMP
   label = 'SIMP'

   def __init__(self,typ,fr="",ang="",statut='f',into=None,defaut=None,
                     min=1,max=1,homo=1,position ='local',
                     val_min = '**',val_max='**',docu="",validators=None):

      """
          Un mot-cl� simple est caract�ris� par les attributs suivants :

          - type : cet attribut est obligatoire et indique le type de valeur attendue

          - fr   :

          - ang :

          - statut :

          - into   :

          - defaut :

          - min

          - max

          - homo

          - position

          - val_min

          - val_max

          - docu
      """
      N_ENTITE.ENTITE.__init__(self,validators)
      # Initialisation des attributs
      if type(typ) == types.TupleType :
          self.type=typ
      else :
          self.type=(typ,)
      self.fr=fr
      self.ang=ang
      self.statut=statut
      self.into=into
      self.defaut=defaut
      self.min=min
      self.max=max
      self.homo=homo
      self.position = position
      self.val_min=val_min
      self.val_max=val_max
      self.docu = docu

   def verif_cata(self):
      """
          Cette methode sert � valider les attributs de l'objet de d�finition
          de la classe SIMP
      """
      self.check_min_max()
      self.check_fr()
      self.check_statut()
      self.check_homo()
      self.check_into()
      self.check_position()
      self.check_validators()

   def __call__(self,val,nom,parent=None):
      """
          Construit un objet mot cle simple (MCSIMP) a partir de sa definition (self)
          de sa valeur (val), de son nom (nom) et de son parent dans l arboresence (parent)
      """
      return self.class_instance(nom=nom,definition=self,val=val,parent=parent)






