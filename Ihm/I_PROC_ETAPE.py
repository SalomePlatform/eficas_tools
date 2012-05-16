# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
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
import I_ETAPE


# import rajoutés suite à l'ajout de Build_sd --> à résorber
import sys
import traceback,types,string
import Noyau
from Noyau import N_Exception
from Noyau.N_Exception import AsException
# fin import à résorber

class PROC_ETAPE(I_ETAPE.ETAPE):
   def get_sdname(self):
      return ""

   def get_sdprods(self,nom_sd):
      """ 
         Fonction : retourne le concept produit par l etape de nom nom_sd
         s il existe sinon None
         Une PROC ne produit aucun concept
      """
      return None

   def supprime_sdprods(self):
      """
         Fonction: Lors d'une destruction d'etape, detruit tous les concepts produits
         Une procedure n'en a aucun
      """
      return

   def delete_concept(self,sd):
      """
          Fonction : Mettre a jour les mots cles de l etape 
          suite à la disparition du concept sd
          Seuls les mots cles simples MCSIMP font un traitement autre
          que de transmettre aux fils

          Inputs :
             - sd=concept detruit
      """
      for child in self.mc_liste :
        child.delete_concept(sd)

   def replace_concept(self,old_sd,sd):
      """
          Fonction : Mettre a jour les mots cles de l etape
          suite au remplacement du concept old_sd

          Inputs :
             - old_sd=concept remplacé
             - sd=nouveau concept
      """
      for child in self.mc_liste :
        child.replace_concept(old_sd,sd)

#ATTENTION SURCHARGE: a garder en synchro ou a reintegrer dans le Noyau
   def Build_sd(self):
      """
           Methode de Noyau surchargee pour poursuivre malgre tout
           si une erreur se produit pendant la creation du concept produit
      """
      try:
         sd=Noyau.N_PROC_ETAPE.PROC_ETAPE.Build_sd(self)
      except AsException,e:
         # Une erreur s'est produite lors de la construction du concept
         # Comme on est dans EFICAS, on essaie de poursuivre quand meme
         # Si on poursuit, on a le choix entre deux possibilités :
         # 1. on annule la sd associée à self
         # 2. on la conserve mais il faut la retourner
         # En plus il faut rendre coherents sdnom et sd.nom
         self.sd=None
         self.sdnom=None
         self.state="unchanged"
         self.valid=0

