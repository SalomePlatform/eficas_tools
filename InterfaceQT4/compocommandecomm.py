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
import traceback
import string

from Editeur import Objecttreeitem
from EficasException import EficasException
import compocomm

class COMMANDE_COMMTreeItem(Objecttreeitem.ObjectTreeItem):
    itemNode=compocomm.Node

    def init(self):
      self.setfunction = self.set_valeur

    def GetIconName(self):
      """
      Retourne le nom de l'icône associée au noeud qui porte self,
      dépendant de la validité de l'objet
      NB : une commande commentarisée est toujours valide ...
      """
      if self.isvalid():
          return "ast-green-percent"
      else:
          return "ast-red-percent"

    def GetLabelText(self):
        """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return 'commentaire'

    def get_valeur(self):
      """
      Retourne la valeur de la commande commentarisée cad son texte
      """
      return self.object.get_valeur() or ''
    
    def GetText(self):
        texte = self.object.valeur
        texte = string.split(texte,'\n')[0]
        if len(texte) < 25 :
            return texte
        else :
            return texte[0:24]

    def set_valeur(self,valeur):
      """
      Afefcte valeur à l'objet commande commentarisée
      """
      self.object.set_valeur(valeur)
      
    def GetSubList(self):
      """
      Retourne la liste des fils de self
      """
      return []

    def uncomment(self):
      """
      Demande à l'objet commande commentarisée de se décommentariser.
      Si l'opération s'effectue correctement, retourne l'objet commande
      et éventuellement le nom de la sd produite, sinon lève une exception
      """
      try:
        commande,nom = self.object.uncomment()
        #self.parent.children[pos].select()
      except Exception as e:
        traceback.print_exc()
        raise EficasException(e)
      return commande,nom
  
import Accas
treeitem =COMMANDE_COMMTreeItem
objet = Accas.COMMANDE_COMM    
