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
   Ce module contient la classe COMMENTAIRE qui sert dans EFICAS
   pour gerer les commentaires dans un JDC
"""

from __future__ import absolute_import
from Noyau.N_CR import CR
from Noyau import N_OBJECT
from Ihm import I_OBJECT
from Extensions.i18n import tr

class COMMENTAIRE(N_OBJECT.OBJECT,I_OBJECT.OBJECT) :
  """ 
      Cette classe permet de creer des objets de type COMMENTAIRE 
  """
  nature = 'COMMENTAIRE'
  idracine = '_comm'

  def __init__(self,valeur,parent=None):
    # parent est un objet de type OBJECT (ETAPE ou MC ou JDC...)
    self.valeur=valeur
    if not parent :
      self.jdc = self.parent = CONTEXT.get_current_step()
    else:
      self.jdc = self.parent = parent
    # La classe COMMENTAIRE n'a pas de definition. On utilise self
    # pour completude
    self.definition=self
    self.nom=''
    self.niveau = self.parent.niveau
    self.actif=1
    self.state="unchanged"
    self.register()

  def register(self):
    """ 
        Enregistre le commentaire dans la liste des etapes de son parent
        lorsque celui-ci est un JDC 
    """
    if self.parent.nature == 'JDC':
      # le commentaire est entre deux commandes:
      # il faut l'enregistrer dans la liste des etapes
      self.parent.register(self)

  def copy(self):
    c=COMMENTAIRE(valeur=self.valeur,parent=self.jdc)
    return c

  def isvalid(self):
    """
    Retourne 1 si self est valide, 0 sinon
    Retourne toujours 1 car un commentaire est toujours valide
    """
    return 1

  def isoblig(self):
    """ Indique si self est obligatoire ou non : retourne toujours 0 """
    return 0

  def isrepetable(self):
    """ Indique si self est repetable ou non : retourne toujours 1 """
    return 1

  def active(self):
      """
      Rend l'etape courante active
      """
      self.actif = 1

  def inactive(self):
      """
      Rend l'etape courante inactive
      NB : un commentaire est toujours actif !
      """
      self.actif = 1

  def isactif(self):
      """
      Booleenne qui retourne 1 si self est valide, 0 sinon
      """
      return self.actif

  def supprime(self):
      """
      Methode qui supprime toutes les boucles de references afin que 
      l'objet puisse etre correctement detruit par le garbage collector
      """
      self.parent=None
      self.jdc=None
      self.definition = None
      self.niveau = None

  def liste_mc_presents(self):
      return []

  def get_valeur(self) :
    """ Retourne la valeur de self, cad le contenu du commentaire """
    try :
      return self.valeur
    except:
      return None

  def set_valeur(self,new_valeur):
    """ 
        Remplace la valeur de self(si elle existe) par new_valeur
    """
    self.valeur = new_valeur
    self.init_modif()

  def init_modif(self):
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def supprime_sdprods(self):
    pass

  def update_context(self,d):
    """
        Update le dictionnaire d avec les concepts ou objets produits par self
        --> ne fait rien pour un commentaire
    """
    pass

  def report(self):
    """ Genere l'objet rapport (classe CR) """
    self.cr=CR()
    if not self.isvalid(): self.cr.warn(tr("Objet commentaire non valorise"))
    return self.cr

  def ident(self):
    """ Retourne le nom interne associe a self
        Ce nom n'est jamais vu par l'utilisateur dans EFICAS
    """
    return self.nom

  def delete_concept(self,sd):
    pass

  def replace_concept (self,old_sd,sd):
    pass

  def verif_condition_bloc(self):
    """
        Evalue les conditions de tous les blocs fils possibles
        (en fonction du catalogue donc de la definition) de self et
        retourne deux listes :
          - la premiere contient les noms des blocs a rajouter
          - la seconde contient les noms des blocs a supprimer
    """
    return [],[]

  def verif_condition_regles(self,liste_presents):
    """
        Retourne la liste des mots-cles a rajouter pour satisfaire les regles
        en fonction de la liste des mots-cles presents
    """
    return []

  def get_sdprods(self,nom_sd):
     """
         Retourne les concepts produits par la commande
     """
     return None

  def verif_existence_sd(self):
     pass

  def get_fr(self):
    """
    Retourne le commentaire lui meme tronque a la 1ere ligne
    """
    return self.valeur.split('\n',1)[0]

  def control_sdprods(self,d):
      """sans objet """
      pass

  def close(self):
      pass

  def reset_context(self):
      pass


