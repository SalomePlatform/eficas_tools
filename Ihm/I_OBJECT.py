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
"""
import string
import Noyau

import CONNECTOR

class OBJECT:
  from Noyau.N_CO import CO
  from Noyau.N_ASSD import assd

  def isMCList(self):
    """ 
        Retourne 1 si self est une MCList (liste de mots-cles), 0 sinon (defaut) 
    """
    return 0

  def get_regles(self):
    """ 
       Retourne les regles de self 
    """
    if hasattr(self,'definition'):
      return self.definition.regles
    elif hasattr(self,'regles'):
      return self.regles
    else :
      return []

  def init_modif(self):
    """
       Met l'etat de l'objet a modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def fin_modif(self):
      """
      Methode appelee apres qu'une modification a ete faite afin de declencher
      d'eventuels traitements post-modification
      """
      #print "fin_modif",self
      # pour les objets autres que les commandes, aucun traitement specifique 
      # on remonte l'info de fin de modif au parent
      CONNECTOR.Emit(self,"valid")
      if self.parent:
        self.parent.fin_modif()

  def isrepetable(self):
    """
         Indique si l'objet est repetable
    """
    return 0

  def liste_mc_presents(self):
    """
         Retourne la liste des noms des mots cles presents
    """
    return []

  def get_docu(self):
    return self.definition.get_docu()

  def get_liste_mc_inconnus(self):
     """
     Retourne la liste des mots-cles inconnus dans self
     """
     return []

  def verif_condition_regles(self,liste_presents):
    """ 
        Retourne la liste des mots-cles a rajouter pour satisfaire les regles
        en fonction de la liste des mots-cles presents 
    """
    liste=[]
    for regle in self.definition.regles:
        liste=regle.verif_condition_regle(liste,liste_presents)
    return liste

  def verif_condition_bloc(self):
    """ 
        Evalue les conditions de tous les blocs fils possibles 
        (en fonction du catalogue donc de la definition) de self et
        retourne deux listes :
          - la premiere contient les noms des blocs a rajouter
          - la seconde contient les noms des blocs a supprimer
    """
    return [],[]

  def get_genealogie(self):
    """ 
        Retourne la liste des noms des ascendants (noms de MCSIMP,MCFACT,MCBLOC
        ou ETAPE) de self jusqu'au premier objet etape rencontre
    """
    if self.parent:
       l=self.parent.get_genealogie()
       l.append(string.strip(self.nom))
       return l
    else:
       return [string.strip(self.nom)]

  def get_fr(self):
     """
         Retourne la chaine d'aide contenue dans le catalogue
         en tenant compte de la langue
     """
     try :
        return getattr(self.definition,self.jdc.lang)
     except:
        try :
            return getattr(self.definition,"fr")
        except :
            return ''

  def update_concept(self,sd):
     pass

  def normalize(self):
     """ Retourne l'objet normalise. En general self sauf si
         pour etre insere dans l'objet pere il doit etre 
         wrappe dans un autre objet (voir mot cle facteur).
     """
     return self

  def delete_mc_global(self):
     return

  def update_mc_global(self):
     return

  #def __del__(self):
  #   print "__del__",self

class ErrorObj(OBJECT):pass

