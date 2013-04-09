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



class PRESENT_ABSENT: 
   """
      La règle vérifie que si le premier mot-clé de self.mcs est present 
          parmi les elements de args les autres mots clés de self.mcs
           doivent etre absents

      Ces arguments sont transmis à la règle pour validation sous la forme 
      d'une liste de noms de mots-clés ou d'un dictionnaire dont 
      les clés sont des noms de mots-clés.
   """
   def verif(self,args):
      """
          La methode verif effectue la verification specifique à la règle.
          args peut etre un dictionnaire ou une liste. Les éléments de args
          sont soit les éléments de la liste soit les clés du dictionnaire.
      """
      #  on verifie que si le premier de la liste est present, 
      #   les autres sont absents
      text=''
      test = 1
      args = self.liste_to_dico(args)
      mc0=self.mcs[0]
      if args.has_key(mc0):
        for mc in self.mcs[1:len(self.mcs)]:
          if args.has_key(mc):
            text = text + u"- Le mot clé "+`mc0`+ u" étant présent, il faut que : "+\
                 mc+" soit absent"+'\n'
            test = 0
      return text,test


