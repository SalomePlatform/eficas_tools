# -*- coding: iso-8859-1 -*-
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

class ASSD(object):
   """
      Classe de base pour definir des types de structures de donnees ASTER
      equivalent d un concept ASTER
   """
   idracine="SD"

   def __init__(self,etape=None,sd=None,reg='oui'):
      """
        reg est un param�tre qui vaut oui ou non :
          - si oui (d�faut) : on enregistre la SD aupr�s du JDC
          - si non : on ne l'enregistre pas
      """
      self.etape=etape
      self.sd=sd
      self.nom=None
      if etape:
        self.parent=etape.parent
      else:
        self.parent=CONTEXT.get_current_step()
      if self.parent :
         self.jdc = self.parent.get_jdc_root()
      else:
         self.jdc = None

      if not self.parent:
        self.id=None
      elif reg == 'oui' :
        self.id = self.parent.reg_sd(self)
      else :
        self.id = self.parent.o_register(self)
      # permet de savoir si le concept a �t� calcul� (1) ou non (0)
      self.executed = 0
      # initialise la partie "sd"
      super(ASSD, self).__init__(nomj='?&?&?&?&')
      
   def __getitem__(self,key):
      return self.etape[key]

   def set_name(self, nom):
      """Positionne le nom de self (et appelle sd_init)
      """
      self.nom = nom
      # test car FORMULE n'a pas de SD associ�e
      meth = getattr(super(ASSD, self), 'set_name', None)
      if meth:
         meth(nom)
   
   def reparent_sd(self):
      """Repositionne le parent des attributs de la SD associ�e.
      """
      # test car FORMULE n'a pas de SD associ�e
      meth = getattr(super(ASSD, self), 'reparent', None)
      if meth:
         meth(None, None)
   
   def get_name(self):
      """
          Retourne le nom de self, �ventuellement en le demandant au JDC
      """
      if not self.nom :
         try:
            self.nom=self.parent.get_name(self) or self.id
         except:
            self.nom=""
      if self.nom.find('sansnom') != -1 or self.nom == '':
         self.nom = self.id
      return self.nom

   def supprime(self):
      """ 
          Cassage des boucles de r�f�rences pour destruction du JDC 
      """
      self.etape = None
      self.sd = None
      self.jdc = None
      self.parent = None

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitASSD(self)

   def __getstate__(self):
      """
          Cette methode permet de pickler les objets ASSD
          Ceci est possible car on coupe les liens avec les objets
          parent, etape et jdc qui conduiraient � pickler de nombreux 
          objets inutiles ou non picklables.
      """
      d=self.__dict__.copy()
      for key in ('parent','etape','jdc'):
          if d.has_key(key):del d[key]
      for key in d.keys():
          if key[0]=='_':del d[key]
      return d

   def par_lot(self):
      """
           Retourne True si l'ASSD est cr��e en mode PAR_LOT='OUI'.
      """
      if not hasattr(self, 'jdc') or self.jdc == None:
         val = None
      else:
         val = self.jdc.par_lot
      return val == 'OUI'

class assd(ASSD):
   def __convert__(cls,valeur):
      return valeur
   __convert__=classmethod(__convert__)
