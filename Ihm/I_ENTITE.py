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
_no=0

def number_entite(entite):
   """
      Fonction qui attribue un numero unique a tous les objets du catalogue
      Ce numero permet de conserver l'ordre des objets
   """
   global _no
   _no=_no+1
   entite._no=_no

class ENTITE:
  def __init__(self):
     number_entite(self)
    
  def get_docu(self):
    if hasattr(self,'docu') :
      if self.docu != "" : return self.docu
      else:
        if hasattr(self,'pere'):
          return self.pere.get_docu()
        else:
          return None
    else:
      return None

  def check_definition(self, parent):
      """Verifie la definition d'un objet composite (commande, fact, bloc)."""
      args = self.entites.copy()
      mcs = set()
      for nom, val in args.items():
         if val.label == 'SIMP':
            mcs.add(nom)
            #XXX
            #if val.max != 1 and val.type == 'TXM':
                #print "#CMD", parent, nom
         elif val.label == 'FACT':
            val.check_definition(parent)
            #PNPNPN surcharge
            # CALC_SPEC !
            #assert self.label != 'FACT', \
            #   'Commande %s : Mot-clef facteur present sous un mot-clef facteur : interdit !' \
            #   % parent
         else:
            continue
         del args[nom]
      # seuls les blocs peuvent entrer en conflit avec les mcs du plus haut niveau
      for nom, val in args.items():
         if val.label == 'BLOC':
            mcbloc = val.check_definition(parent)
            #XXX
            #print "#BLOC", parent, re.sub('\s+', ' ', val.condition)
            #assert mcs.isdisjoint(mcbloc), "Commande %s : Mot(s)-clef(s) vu(s) plusieurs fois : %s" \
            #   % (parent, tuple(mcs.intersection(mcbloc)))
      return mcs

