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
    Ce module contient la classe de d�finition pour les nuplets NUPL
"""
# Modules Python
import types

# Modules Eficas
from Noyau import N_ENTITE,N_MCLIST,N_CR
from Ihm import I_ENTITE
from Extensions.i18n import tr
import mcnuplet

class NUPL(N_ENTITE.ENTITE,I_ENTITE.ENTITE):
   """
   """
   class_instance = mcnuplet.MCNUPLET
   list_instance = N_MCLIST.MCList
   label='NUPLET'
   CR=N_CR.CR

   def __init__(self,fr="",ang="",docu="",statut='f',defaut=None,min=0,max=1,
                    elements=None):
      N_ENTITE.ENTITE.__init__(self)
      I_ENTITE.ENTITE.__init__(self)
      self.fr=fr
      self.ang=ang
      self.docu=docu
      self.statut=statut
      self.defaut=defaut
      self.min=min
      self.max=max
      self.entites=elements
      self.regles=()
      # on force le statut des sous entites a obligatoire
      for e in elements:e.statut='o'
      self.idracine="NUPLET"
      self.affecter_parente()

   def verif_cata(self):
      """
          Cette methode sert � valider les attributs de l'objet de d�finition
          de la classe NUPL
      """
      if type(self.min) != types.IntType :
        if self.min != '**':
          self.cr.fatal(tr("L'attribut 'min' doit etre un entier : ")+str(self.min))
      if type(self.max) != types.IntType :
        if self.max != '**' :
          self.cr.fatal(tr("L'attribut 'max' doit etre un entier : ")+str(self.max))
      if self.min > self.max :
         self.cr.fatal(tr("Nombres d'occurrence min et max invalides :") +str(self.min)+","+str(self.max))
      if type(self.fr) != types.StringType :
        self.cr.fatal(tr("L'attribut 'fr' doit etre une chaine de caracteres"))
      if self.statut not in ['o','f','c','d']:
        self.cr.fatal(tr("L'attribut 'statut' doit valoir 'o','f','c' ou 'd'"))
      if type(self.docu) != types.StringType :
        self.cr.fatal(tr("L'attribut 'docu' doit etre une chaine de caracteres"))
      self.verif_cata_regles()

   def __call__(self,val,nom,parent):
      """
         Construit la structure de donnees pour un NUPLET a partir de sa definition (self)
         de sa valeur (val), de son nom (nom) et de son parent dans l arboresence (parent)
      """
      if (type(val) == types.TupleType or type(val) == types.ListType) and type(val[0]) == types.TupleType:
        # On est en presence d une liste de nuplets
        l=self.list_instance()
        l.init(nom=nom,parent=parent)
        for v in val:
          objet=self.class_instance(nom=nom,definition=self,val=v,parent=parent)
          l.append(objet)
        return l
      else:
        # on est en presence d un seul nuplet
        return self.class_instance(nom=nom,definition=self,val=val,parent=parent)

   def report(self):
      """ 
           M�thode qui cr�e le rapport de v�rification du catalogue du nuplet 
      """
      self.cr = self.CR()
      self.verif_cata()
      for v in self.entites :
        cr = v.report()
        cr.debut =tr("D�but ")+v.__class__.__name__+ ' : '
        cr.fin =tr("Fin ")+v.__class__.__name__+ ' : '
        self.cr.add(cr)
      return self.cr

   def affecter_parente(self):
      """
          Cette methode a pour fonction de donner un nom et un pere aux
          sous entit�s qui n'ont aucun moyen pour atteindre leur parent 
          directement
          Il s'agit principalement des mots cles
      """
      k=0
      for v in self.entites:
        v.pere = self
        v.nom = str(k)
        k=k+1

