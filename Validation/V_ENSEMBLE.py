# coding=utf-8
# ======================================================================
# Copyright (C) 2007-2015   EDF R&D
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



class ENSEMBLE:

    """
       La règle vérifie que si un mot-clé de self.mcs est present
           parmi les elements de args tous les autres doivent etre presents.

       Ces arguments sont transmis à la règle pour validation sous la forme
       d'une liste de noms de mots-clés ou d'un dictionnaire dont
       les clés sont des noms de mots-clés.
    """

    def verif(self, args):
        """
            La methode verif effectue la verification specifique à la règle.
            args peut etre un dictionnaire ou une liste. Les éléments de args
            sont soit les éléments de la liste soit les clés du dictionnaire.
        """
        #  on compte le nombre de mots cles presents, il doit etre egal a la liste
        #  figurant dans la regle
        text = ''
        test = 1
        args = self.liste_to_dico(args)
        pivot = None
        for mc in self.mcs:
            if args.has_key(mc):
                pivot = mc
                break
        if pivot:
            for mc in self.mcs:
                if mc != pivot:
                    if not args.has_key(mc):
                        text = text + "- " + pivot + u" étant présent, " + \
                            mc + u" doit être présent" + '\n'
                        test = 0
        return text, test
