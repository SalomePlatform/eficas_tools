# -*- coding: utf-8 -*-
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
"""
   Ce module contient les classes permettant de définir les objets graphiques
   représentant un objet de type PARAMETRE, cad le panneau et l'item de l'arbre
   d'EFICAS
"""

# import modules Python
import string, types
from Extensions.i18n import tr

# import modules EFICAS
from Editeur     import Objecttreeitem
import browser
import typeNode


class Node(browser.JDCNode,typeNode.PopUpMenuNodePartiel): 
    def getPanel2(self):
        """        
        """    
        from monParamPanel  import MonParamPanel
        return MonParamPanel(self, parent=self.editor )

    def createPopUpMenu(self):
        typeNode.PopUpMenuNodePartiel.createPopUpMenu(self)
        self.menu.removeAction(self.Documentation)

    def doPaste(self,node_selected):
        return None



class PARAMTreeItem(Objecttreeitem.ObjectTreeItem):
    """
    Classe servant à définir l'item porté par le noeud de l'arbre d'EFICAS
    qui représente le PARAMETRE
    """
    itemNode=Node

    def init(self):      
      self.setfunction = self.set_valeur

# ---------------------------------------------------------------------------
#                   API du PARAMETRE pour l'arbre 
# ---------------------------------------------------------------------------

    def GetIconName(self):
      """
      Retourne le nom de l'icone associée au noeud qui porte self,
      dépendant de la validité de l'objet
      NB : un PARAMETRE est toujours valide ...
      """
      if self.isactif():
          if self.isvalid():
              return "ast-green-square"
          else:
              return "ast-red-square"
      else:
          return "ast-white-square"

    def GetLabelText(self):
        """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return tr('PARAMETRE'),None,None 

    def GetText(self):
      """
      Retourne le texte à afficher aprês le nom de la commande (ici apres 'parametre')
      Ce texte est tronqué à 25 caractêres
      """
      texte=self.object.nom+"="+str(self.object.valeur)
      if type(self.object.valeur) == types.ListType :
          texte=self.nom+' = ['
          for l in self.object.valeur :
            texte=texte+str(l) +","
          texte=texte[0:-1]+']'
      texte = string.split(texte,'\n')[0]
      if len(texte) < 25 :
          return texte
      else :
          return texte[0:24]+'...'

    def GetSubList(self):
      """
      Retourne la liste des fils de self
      """
      return []
    
# ---------------------------------------------------------------------------
#       Méthodes permettant la modification et la lecture des attributs
#       du parametre = API graphique du PARAMETRE pour Panel et EFICAS
# ---------------------------------------------------------------------------

    def get_valeur(self):
      """
      Retourne la valeur de l'objet PARAMETRE cad son texte
      """
      if self.object.valeur is None: return ''
      else: return self.object.valeur 

    def get_nom(self):
      """
      Retourne le nom du parametre
      """
      return self.object.nom

    def set_valeur(self,new_valeur):
      """
      Affecte valeur à l'objet PARAMETRE
      """
      self.object.set_valeur(new_valeur)

    def set_nom(self,new_nom):
      """
      Renomme le parametre
      """
      self.object.set_nom(new_nom)
      #self.object.set_attribut('nom',new_nom)

    def get_fr(self):
      """
      Retourne le fr associé au parametre, cad la bulle d'aide pour EFICAS
      """
      return tr("Definition d'un parametre")
    
import Extensions.parametre
treeitem =PARAMTreeItem
objet = Extensions.parametre.PARAMETRE
