# -*- coding: utf-8 -*-
# Copyright (C) 2007-2017   EDF R&D
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
from __future__ import absolute_import
from Extensions.i18n import tr
from . import CONNECTOR
from . import I_MCCOMPO
import Noyau

class MCFACT(I_MCCOMPO.MCCOMPO):
  def isRepetable(self):
     """ 
         Indique si l'objet est repetable.
         Retourne 1 si le mot-cle facteur self peut etre repete
         Retourne 0 dans le cas contraire
     """
     if self.definition.max > 1:
       # marche avec '**'
       return 1
     else :
       return 0

  def isOblig(self):
    if self.definition.statut != 'o' : return 0
    objet = self.parent.getChild(self.nom)
    if len(objet) > 1 : return 0
    else : return 1

  def getLabelText(self):
    """
       Retourne le label de self suivant qu'il s'agit d'un MCFACT
       isole ou d'un MCFACT appartenant a une MCList :
       utilisee pour l'affichage dans l'arbre
    """
    objet = self.parent.getChild(self.nom)
    # objet peut-etre self ou une MCList qui contient self ...
    if objet is None or objet is self:
     return tr("Erreur - mclist inexistante : %s", self.nom)

    try:
      if len(objet) > 1 :
        index = objet.getIndex(self)+1 # + 1 a cause de la numerotation qui commence a 0
        return self.nom +'_'+repr(index)+':'
      else:
        return self.nom
    except:
      return tr("Erreur - mot cle facteur de nom : %s", self.nom)

  def getGenealogiePrecise(self):
    nom=self.getLabelText() 
    if nom[-1]==':' : nom=nom[0:-1]
    if self.parent:
       l=self.parent.getGenealogiePrecise()
       l.append(nom.strip())
       return l
    else:
       return [nom.strip()]


  def initModif(self):
    """
       Met l'etat de l'objet a modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    parent= hasattr(self,"alt_parent") and self.alt_parent or self.parent
    if parent:
       parent.initModif()

  def finModif(self):
    """
      Methode appelee apres qu'une modification a ete faite afin de declencher
      d'eventuels traitements post-modification
    """
    #print "finModif",self
    # pour les objets autres que les commandes, aucun traitement specifique
    # on remonte l'info de fin de modif au parent
    CONNECTOR.Emit(self,"valid")
    parent= hasattr(self,"alt_parent") and self.alt_parent or self.parent
    if parent:
       parent.finModif()

  def normalize(self):
    """ Retourne le MCFACT normalise. Pour un MCFACT isole, l'objet normalise
        est une MCLIST de longueur 1 qui contient ce MCFACT
    """
    new_obj = self.definition.list_instance()
    new_obj.init(nom=self.nom,parent=None)
    new_obj.append(self)
    return new_obj

  def supprime(self):
    self.alt_parent=None
    Noyau.N_MCFACT.MCFACT.supprime(self)
