# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
import traceback
import string

from Editeur import Objecttreeitem
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
      except Exception,e:
        traceback.print_exc()
        raise e
      return commande,nom
  
import Accas
treeitem =COMMANDE_COMMTreeItem
objet = Accas.COMMANDE_COMM    
