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
    Ce module contient la classe mere pour les classes de definition des regles d exclusion.

    La classe REGLE est la classe de base : elle est virtuelle, elle ne doit pas etre instanciee.

    Les classes regles d�riv�es qui seront instanci�es doivent implementer la methode verif
    dont l argument est le dictionnaire des mots cles effectivement presents
    sur lesquels sera operee la verification de la regle

    A la creation de l'objet regle on lui passe la liste des noms de mots cles concernes

    Exemple ::

    # Cr�ation de l'objet r�gle UNPARMI
    r=UNPARMI("INFO","AFFE")
    # V�rification de la r�gle r sur le dictionnaire pass� en argument
    r.verif({"INFO":v1,"AFFE":v2)
"""

import types

class REGLE:
   def __init__(self,*args):
      """
          Les classes d�riv�es peuvent utiliser cet initialiseur par d�faut ou
          le surcharger
      """
      self.mcs=args

   def verif(self,args):
      """
         Les classes d�riv�es doivent impl�menter cette m�thode
         qui doit retourner une paire dont le premier �l�ment est une chaine de caract�re
         et le deuxi�me un entier.
 
         L'entier peut valoir 0 ou 1. -- s'il vaut 1, la r�gle est v�rifi�e
          s'il vaut 0, la r�gle n'est pas v�rifi�e et le texte joint contient
         un commentaire de la non validit�.
      """
      raise NotImplementedError('class REGLE should be derived')

   def liste_to_dico(self,args):
      """
         Cette m�thode est utilitaire pour les seuls besoins
         des classes d�riv�es. 

         Elle transforme une liste de noms de mots cl�s en un 
         dictionnaire �quivalent dont les cl�s sont les noms des mts-cl�s

         Ceci permet d'avoir un traitement identique pour les listes et les dictionnaires
      """
      if type(args) == types.DictionaryType:
        return args
      elif type(args) == types.ListType:
        dico={}
        for arg in args :
          dico[arg]=0
        return dico
      else :
        raise Exception("Erreur ce n'est ni un dictionnaire ni une liste %s" % args)


