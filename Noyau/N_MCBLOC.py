# -*- coding: iso-8859-1 -*-
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

""" 
    Ce module contient la classe MCBLOC qui sert � controler la valeur
    d'un bloc de mots-cl�s par rapport � sa d�finition port�e par un objet
    de type ENTITE
"""

import types

import N_MCCOMPO

class MCBLOC(N_MCCOMPO.MCCOMPO):
   """
      Classe support d'un bloc de mots-cl�s.
  
   """

   nature = "MCBLOC"
   def __init__(self,val,definition,nom,parent):
      """
         Attributs :

          - val : valeur du bloc (dictionnaire dont les cl�s sont des noms de mots-cl�s et les valeurs
                  les valeurs des mots-cl�s)

          - definition : objet de d�finition de type BLOC associ� au bloc (porte les attributs de d�finition)

          - nom : nom du bloc. Ce nom lui est donn� par celui qui cr�e le bloc de mot-cl�

          - parent : le cr�ateur du bloc. Ce peut etre un mot-cl� facteur ou un autre objet composite de type
                     OBJECT. Si parent vaut None, le bloc ne poss�de pas de contexte englobant.

          - mc_liste : liste des sous-objets du bloc construite par appel � la m�thode build_mc

      """
      self.definition=definition
      self.nom=nom
      self.val = val
      self.parent = parent
      self.valeur = val
      if parent :
         self.jdc = self.parent.jdc
         self.niveau = self.parent.niveau
         self.etape = self.parent.etape
      else:
         # Le mot cle a �t� cr�� sans parent
         self.jdc = None
         self.niveau = None
         self.etape = None
      self.mc_liste=self.build_mc()
         
   def get_valeur(self):
      """
         Retourne la "valeur" de l'objet bloc. Il s'agit d'un dictionnaire dont
         les cl�s seront les noms des objets de self.mc_liste et les valeurs
         les valeurs des objets de self.mc_liste obtenues par application de 
         la m�thode get_valeur.

         Dans le cas particulier d'un objet bloc les �l�ments du dictionnaire
         obtenu par appel de la m�thode get_valeur sont int�gr�s au niveau
         sup�rieur.
          
      """
      dico={}
      for mocle in self.mc_liste:
        if mocle.isBLOC():
           # Si mocle est un BLOC, on inclut ses items dans le dictionnaire
           # repr�sentatif de la valeur de self. Les mots-cl�s fils de blocs sont
           # donc remont�s au niveau sup�rieur.
           dico.update(mocle.get_valeur())
        else:
           dico[mocle.nom]=mocle.get_valeur()

      # On rajoute tous les autres mots-cl�s locaux possibles avec la valeur
      # par d�faut ou None
      # Pour les mots-cl�s facteurs, on ne traite que ceux avec statut d�faut ('d')
      # et cach� ('c')
      # On n'ajoute aucune information sur les blocs. Ils n'ont pas de d�faut seulement
      # une condition.
      for k,v in self.definition.entites.items():
        if not dico.has_key(k):
           if v.label == 'SIMP':
              # Mot cl� simple
              dico[k]=v.defaut
           elif v.label == 'FACT':
                if v.statut in ('c','d') :
                   # Mot cl� facteur avec d�faut ou cach� provisoire
                   dico[k]=v(val=None,nom=k,parent=self)
                   # On demande la suppression des pointeurs arrieres
                   # pour briser les eventuels cycles
                   dico[k].supprime()
                else:
                   dico[k]=None

      return dico

   def isBLOC(self):
      """
          Indique si l'objet est un BLOC
      """
      return 1

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitMCBLOC(self)

   def makeobjet(self):
      return self.definition(val = None,  nom = self.nom,parent = self.parent)
