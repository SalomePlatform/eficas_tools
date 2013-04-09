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

class MEME_NOMBRE:
   """
      La r�gle MEME_NOMBRE v�rifie que l'on trouve au moins un des mots-cl�s
      de la r�gle parmi les arguments d'un OBJECT.

      Ces arguments sont transmis � la r�gle pour validation sous la forme
      d'une liste de noms de mots-cl�s ou d'un dictionnaire dont
      les cl�s sont des noms de mots-cl�s.
   """
   def verif(self,args):
      """
          La m�thode verif v�rifie que l'on trouve au moins un des mos-cl�s
          de la liste self.mcs parmi les �l�ments de args

          args peut etre un dictionnaire ou une liste. Les �l�ments de args
          sont soit les �l�ments de la liste soit les cl�s du dictionnaire.
      """
      #  on compte le nombre de mots cles presents
      text =''
      args = self.liste_to_dico(args)
      size = -1

      for mc in self.mcs:
        if mc not in args.keys():
          text = u"Une cl� dans la r�gle n'existe pas %s" % mc
          return text,0

        val = args[mc].valeur
        len_val = 0
        if not isinstance(val,type([])):
          len_val = 1
        else:
          len_val = len(val)

        if size == -1:
          size = len_val
        elif size != len_val:
          text = u"Pas la m�me longeur"
          return text,0
      return text,1

