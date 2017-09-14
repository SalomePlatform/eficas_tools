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
"""
# Modules Python
from __future__ import absolute_import
try : 
   from builtins import str
except : pass


# Modules Eficas
from Noyau import N_MCCOMPO
from Validation import V_MCCOMPO
from Extensions.i18n import tr

class MCNUPLET(V_MCCOMPO.MCCOMPO,N_MCCOMPO.MCCOMPO):
   """
   """
   nature = "MCNUPLET"
   txt_nat="Nuplet : "

   def __init__(self,val,definition,nom,parent):
      # val contient la valeur initial du nuplet
      self.val = val
      if val == None: self.val=()
      self.definition=definition
      self.nom=nom
      self.parent = parent
      # GETVAL affecte la valeur par defaut si necessaire
      self.valeur=self.GETVAL(self.val)
      if parent :
         self.jdc = self.parent.jdc
         self.niveau = self.parent.niveau
         self.etape = self.parent.etape
      else:
         # Le mot cle a ete cree sans parent
         self.jdc = None
         self.niveau = None
         self.etape = None
      self.state = 'undetermined'
      self.actif=1
      self.mc_liste=self.build_mc()

   def build_mc(self):
      """ 
          Construit la liste des sous-entites de MCNUPLET
          a partir de la liste des arguments (valeur)
      """
      args = self.valeur
      if args ==None : args =()
      mc_liste=[]

      # on cree les sous entites du NUPLET a partir des valeurs initiales
      k=0
      for v in self.definition.entites:
        if k < len(args):
          val=args[k]
        else:
          val=None
        objet=v(val=val,nom=repr(k),parent=self)
        if hasattr(objet.definition,'position'):
          if objet.definition.position == 'global' :
            self.append_mc_global(objet)
          #XXX et global_jdc ??
        mc_liste.append(objet)
        k=k+1
      # Un nuplet n'a pas de mots inconnus
      self.reste_val={}
      return mc_liste

   def isvalid(self,cr='non'):
      """
          Indique si self (MCNUPLET) est un objet valide ou non : retourne 1 si oui, 0 sinon
      """
      if self.state == 'unchanged' :
        return self.valid
      else:
        valid = 1
        if hasattr(self,'valid'):
          old_valid = self.valid
        else:
          old_valid = None
        for child in self.mc_liste :
          if not child.isvalid():
            valid = 0
            break
        if len(self.mc_liste) != len(self.definition.entites):
          valid=0
          if cr == 'oui' :
            self.cr.fatal(''.join(("Nuplet : ",self.nom,tr("Longueur incorrecte"))))
        self.valid = valid
        self.state = 'unchanged'
        if old_valid:
          if old_valid != self.valid : self.init_modif_up()
        return self.valid

   def __getitem__(self,key):
      """
          Retourne le key eme element du nuplet
      """
      # Un nuplet est toujours une liste de mots cles simples
      # On retourne donc la valeur
      return self.mc_liste[key].valeur

   def __str__(self):
      """
           Retourne une representation du nuplet sous forme de chaine
           de caracteres
      """
      s='('
      for e in self.mc_liste:
        s=s + str(e.valeur) + ','
      return s + ')'

   def __repr__(self):
      """
           Retourne une representation du nuplet sous forme de chaine
           de caracteres
      """
      s='('
      for e in self.mc_liste:
        s=s + str(e.valeur) + ','
      return s + ')'

   def get_regles(self):
      """
         Retourne la liste des regles attachees au nuplet
      """
      return []

   def verif_condition_bloc(self):
      """
          Verifie s'il y a des blocs sous le nuplet et retourne 
          les blocs en question
      """
      # Il n y a pas de BLOCs sous un NUPLET
      return [],[]

   def isrepetable(self):
      """ 
          Indique si le NUPLET peut etre repete.
          Retourne 1 si c'est le cas.
          Retourne 0 dans le cas contraire.
          L'information est donnee par le catalogue, cad la definition de self
      """
      if self.definition.min != self.definition.max :
        return 1
      else :
        return 0

   def makeobjet(self):
      return self.definition(val = None, nom = self.nom,parent = self.parent)

   def get_valeur(self):
      """
          Cette methode doit retourner la valeur de l'objet. Elle est utilisee par 
          cree_dict_valeurs pour construire un dictionnaire contenant les mots cles 
          d'une etape.
          Dans le cas d'un nuplet, on retournera comme valeur une liste des valeurs
          des mots cle simples contenus.
      """
      l=[]
      for v in self.mc_liste:
         l.append(v.valeur)
      return l

   def get_val(self):
      """
          Une autre methode qui retourne une "autre" valeur du mot cle facteur.
          Elle est utilisee par la methode get_mocle
      """
      l=[]
      for v in self.mc_liste:
         l.append(v.valeur)
      return l

   def isoblig(self):
      return self.definition.statut=='o'

   def get_fr(self):
     """
        Retourne le texte d'aide dans la langue choisie
     """
     try :
        return getattr(self.definition,self.jdc.lang)
     except:
        return ''

   def cree_dict_valeurs(self,liste=[],condition=0):
     dico={}
     return dico

   def update_condition_bloc(self):
     """
       Realise l'update des blocs conditionnels fils de self
       et propage au parent (rien a faire pour nuplet)
     """





