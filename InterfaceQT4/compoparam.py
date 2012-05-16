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
"""
   Ce module contient les classes permettant de d�finir les objets graphiques
   repr�sentant un objet de type PARAMETRE, cad le panneau et l'item de l'arbre
   d'EFICAS
"""

# import modules Python
import string, types

# import modules EFICAS
from Editeur     import Objecttreeitem
import browser
import typeNode


class Node(browser.JDCNode,typeNode.PopUpMenuNodePartiel): 
    def getPanel(self):
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
    Classe servant � d�finir l'item port� par le noeud de l'arbre d'EFICAS
    qui repr�sente le PARAMETRE
    """
    itemNode=Node

    def init(self):      
      self.setfunction = self.set_valeur

# ---------------------------------------------------------------------------
#                   API du PARAMETRE pour l'arbre 
# ---------------------------------------------------------------------------

    def GetIconName(self):
      """
      Retourne le nom de l'icone associ�e au noeud qui porte self,
      d�pendant de la validit� de l'objet
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
        - le texte � afficher dans le noeud repr�sentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        return 'PARAMETRE',None,None 

    def GetText(self):
      """
      Retourne le texte � afficher apr�s le nom de la commande (ici apres 'param�tre')
      Ce texte est tronqu� � 25 caract�res
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
#       M�thodes permettant la modification et la lecture des attributs
#       du param�tre = API graphique du PARAMETRE pour Panel et EFICAS
# ---------------------------------------------------------------------------

    def get_valeur(self):
      """
      Retourne la valeur de l'objet PARAMETRE cad son texte
      """
      if self.object.valeur is None: return ''
      else: return self.object.valeur 

    def get_nom(self):
      """
      Retourne le nom du param�tre
      """
      return self.object.nom

    def set_valeur(self,new_valeur):
      """
      Affecte valeur � l'objet PARAMETRE
      """
      self.object.set_valeur(new_valeur)

    def set_nom(self,new_nom):
      """
      Renomme le param�tre
      """
      self.object.set_nom(new_nom)
      #self.object.set_attribut('nom',new_nom)

    def get_fr(self):
      """
      Retourne le fr associ� au param�tre, cad la bulle d'aide pour EFICAS
      """
      return "D�finition d'un param�tre"
    
import Extensions.parametre
treeitem =PARAMTreeItem
objet = Extensions.parametre.PARAMETRE
