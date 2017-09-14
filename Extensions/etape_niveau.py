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
"""
    Ce module contient la classe ETAPE_NIVEAU qui sert a 
    concretiser les niveaux au sein d'un JDC
"""
from __future__ import absolute_import
import traceback

from Noyau import N_OBJECT

class ETAPE_NIVEAU(N_OBJECT.OBJECT):

  def __init__(self,niveau,parent):
    self.parent = parent
    self.jdc = self.parent.get_jdc_root()
    self.niveau = self
    self.definition = niveau
    self.etapes=[]
    self.etapes_niveaux = []
    self.dict_niveaux={}
    self.editmode = 0
    self.state="undetermined"
    self.build_niveaux()

  def build_niveaux(self):
    for niveau in self.definition.l_niveaux:
      etape_niveau = ETAPE_NIVEAU(niveau,self)
      self.etapes_niveaux.append(etape_niveau)
      self.dict_niveaux[niveau.nom]=etape_niveau

  def register(self,etape):
    """ 
          Enregistre la commande etape :
          - si editmode = 0 : on est en mode relecture d'un fichier de commandes
          auquel cas on ajoute etape a la fin de la liste self.etapes
          - si editmode = 1 : on est en mode ajout d'etape depuis eficas auquel cas
          cette methode ne fait rien, c'est addentite qui enregistre etape
          a la bonne place dans self.etapes 
    """
    if self.editmode : return
    self.etapes.append(etape)

  def unregister(self,etape):
    """
        Desenregistre l'etape du niveau
    """
    self.etapes.remove(etape)

  def ident(self):
    return self.definition.label

  def isactif(self):
    #print 'Niveau : ',self.definition.nom
    #print '\tactif =',self.definition.actif
    if self.definition.actif == 1 :
      return 1
    else :
      # self.actif est une condition a evaluer dans un certain contexte ...
      d = self.cree_dict_valeurs()
      try:
        t=eval(self.definition.actif,d)
        return t
      except:
        traceback.print_exc()
        return 0

  def cree_dict_valeurs(self):
    """
    Retourne le dictionnaire des freres aines de self compose des couples :
    {nom_frere isvalid()}
    """
    d={}
    for niveau in self.parent.etapes_niveaux:
      if niveau is self : break
      d[niveau.definition.nom]=niveau.isvalid()
    return d

  def isvalid(self):
    """ Methode booleenne qui retourne 0 si le niveau est invalide, 1 sinon """
    if self.etapes_niveaux == []:
      if len(self.etapes) == 0:
        return self.definition.valide_vide
      else:
        for etape in self.etapes :
          if not etape.isvalid() : return 0
        return 1
    else:
      for etape_niveau in self.etapes_niveaux :
        if not etape_niveau.isvalid() : return 0
      return 1

  def accept(self,visitor):
    visitor.visitETAPE_NIVEAU(self)

  def addentite(self,name,pos_rel):
    self.editmode = 1
    try :
      pos_abs=self.jdc.get_nb_etapes_avant(self)+pos_rel
      cmd = self.jdc.addentite(name,pos_abs)
      self.etapes.insert(pos_rel,cmd)
      self.editmode = 0
      return cmd
    except:
      traceback.print_exc()
      self.editmode = 0
      return None

  def suppentite(self,etape) :
    """ Classe ETAPE_NIVEAU
        Supprime une etape 
    """
    self.jdc.suppentite(etape)


  def get_fr(self):
     """
        Retourne le texte d'aide dans la langue choisie
     """
     try :
        return getattr(self.definition,self.jdc.lang)
     except:
        return ''

