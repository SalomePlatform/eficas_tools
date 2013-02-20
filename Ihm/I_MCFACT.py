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
from Extensions.i18n import tr
import CONNECTOR
import I_MCCOMPO
import Noyau

class MCFACT(I_MCCOMPO.MCCOMPO):
  def isrepetable(self):
     """ 
         Indique si l'objet est répétable.
         Retourne 1 si le mot-clé facteur self peut être répété
         Retourne 0 dans le cas contraire
     """
     if self.definition.max > 1:
       # marche avec '**'
       return 1
     else :
       return 0

  def isoblig(self):
    return self.definition.statut=='o'

  def getlabeltext(self):
    """
       Retourne le label de self suivant qu'il s'agit d'un MCFACT
       isole ou d'un MCFACT appartenant a une MCList :
       utilisee pour l'affichage dans l'arbre
    """
    objet = self.parent.get_child(self.nom)
    # objet peut-etre self ou une MCList qui contient self ...
    if objet is None or objet is self:
     return tr("Erreur - mclist inexistante : %s", self.nom)

    try:
      if len(objet) > 1 :
        index = objet.get_index(self)+1 # + 1 à cause de la numérotation qui commence à 0
        return self.nom +'_'+`index`+':'
      else:
        return self.nom
    except:
      return tr("Erreur - mot cle facteur de nom : %s", self.nom)

  def init_modif(self):
    """
       Met l'état de l'objet à modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    parent= hasattr(self,"alt_parent") and self.alt_parent or self.parent
    if parent:
       parent.init_modif()

  def fin_modif(self):
    """
      Méthode appelée après qu'une modification a été faite afin de déclencher
      d'éventuels traitements post-modification
    """
    #print "fin_modif",self
    # pour les objets autres que les commandes, aucun traitement spécifique
    # on remonte l'info de fin de modif au parent
    CONNECTOR.Emit(self,"valid")
    parent= hasattr(self,"alt_parent") and self.alt_parent or self.parent
    if parent:
       parent.fin_modif()

  def normalize(self):
    """ Retourne le MCFACT normalisé. Pour un MCFACT isolé, l'objet normalisé
        est une MCLIST de longueur 1 qui contient ce MCFACT
    """
    new_obj = self.definition.list_instance()
    new_obj.init(nom=self.nom,parent=None)
    new_obj.append(self)
    return new_obj

  def supprime(self):
    self.alt_parent=None
    Noyau.N_MCFACT.MCFACT.supprime(self)
