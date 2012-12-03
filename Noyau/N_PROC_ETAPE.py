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
    Ce module contient la classe PROC_ETAPE qui sert � v�rifier et � ex�cuter
    une proc�dure
"""

# Modules Python
import types,sys,string
import traceback

# Modules EFICAS
import N_MCCOMPO, N_ETAPE
from N_Exception import AsException
import N_utils

class PROC_ETAPE(N_ETAPE.ETAPE):
   """
      Cette classe h�rite de ETAPE. La seule diff�rence porte sur le fait
      qu'une proc�dure n'a pas de concept produit

   """
   nature = "PROCEDURE"
   def __init__(self, oper=None, reuse=None, args={}):
      """
      Attributs :
       - definition : objet portant les attributs de d�finition d'une �tape de type op�rateur. Il
                      est initialis� par l'argument oper.
       - valeur : arguments d'entr�e de type mot-cl�=valeur. Initialis� avec l'argument args.
       - reuse : forc�ment None pour une PROC
      """
      N_ETAPE.ETAPE.__init__(self, oper, reuse=None, args=args, niveau=5)
      self.reuse = None

   def Build_sd(self):
      """
          Cette methode applique la fonction op_init au contexte du parent
          et lance l'ex�cution en cas de traitement commande par commande
          Elle doit retourner le concept produit qui pour une PROC est toujours None
          En cas d'erreur, elle leve une exception : AsException ou EOFError
      """
      if not self.isactif():return
      try:
         if self.parent:
            if type(self.definition.op_init) == types.FunctionType: 
               apply(self.definition.op_init,(self,self.parent.g_context))
         else:
            pass
      except AsException,e:
        raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                              'fichier : ',self.appel[1],e)
      except EOFError:
        raise
      except :
        l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
        raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                          'fichier : ',self.appel[1]+'\n',
                          string.join(l))

      self.Execute()
      return None

   def supprime(self):
      """
         M�thode qui supprime toutes les r�f�rences arri�res afin que l'objet puisse
         etre correctement d�truit par le garbage collector
      """
      N_MCCOMPO.MCCOMPO.supprime(self)
      self.jdc=None
      self.appel=None

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitPROC_ETAPE(self)

   def update_context(self,d):
      """
         Met � jour le contexte de l'appelant pass� en argument (d)
         Une PROC_ETAPE n ajoute pas directement de concept dans le contexte
         Seule une fonction enregistree dans op_init pourrait le faire
      """
      if type(self.definition.op_init) == types.FunctionType:
        apply(self.definition.op_init,(self,d))



