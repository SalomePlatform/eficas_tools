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
   Ce module contient la classe  de base MCCOMPO qui sert � factoriser
   les traitements des objets composites de type OBJECT
"""
# Modules Python
import os
import traceback

# Modules EFICAS
from Noyau import N_CR
from Noyau.N_Exception import AsException
from Noyau.strfunc import ufmt, to_unicode

class MCCOMPO:
   """
       L'attribut mc_liste a �t� cr�� par une classe d�riv�e de la
       classe MCCOMPO du Noyau
   """

   CR=N_CR.CR

   def __init__(self):
      self.state = 'undetermined'
      # d�fini dans les classes d�riv�es
      self.txt_nat = ''

   def init_modif_up(self):
      """
         Propage l'�tat modifi� au parent s'il existe et n'est pas l'objet
         lui-meme
      """
      if self.parent and self.parent != self :
        self.parent.state = 'modified'

   def report(self):
      """
          G�n�re le rapport de validation de self
      """
      self.cr=self.CR()
      self.cr.debut = self.txt_nat+self.nom
      self.cr.fin = u"Fin "+self.txt_nat+self.nom
      for child in self.mc_liste:
        self.cr.add(child.report())
      self.state = 'modified'
      try:
        self.isvalid(cr='oui')
      except AsException,e:
        if CONTEXT.debug : traceback.print_exc()
        self.cr.fatal(' '.join((self.txt_nat, self.nom, str(e))))
      return self.cr

   def verif_regles(self):
      """
         A partir du dictionnaire des mots-cl�s pr�sents, v�rifie si les r�gles
         de self sont valides ou non.

         Retourne une chaine et un bool�en :

           - texte = la chaine contient le message d'erreur de la (les) r�gle(s) viol�e(s) ('' si aucune)

           - testglob = bool�en 1 si toutes les r�gles OK, 0 sinon
      """
      # On verifie les regles avec les defauts affect�s
      dictionnaire = self.dict_mc_presents(restreint='non')
      texte = ['']
      testglob = 1
      for r in self.definition.regles:
        erreurs,test = r.verif(dictionnaire)
        testglob = testglob*test
        if erreurs != '':
            texte.append(to_unicode(erreurs))
      texte = os.linesep.join(texte)
      return texte, testglob

   def dict_mc_presents(self,restreint='non'):
      """
          Retourne le dictionnaire {mocle : objet} construit � partir de self.mc_liste
          Si restreint == 'non' : on ajoute tous les mots-cl�s simples du catalogue qui ont
          une valeur par d�faut
          Si restreint == 'oui' : on ne prend que les mots-cl�s effectivement entr�s par
          l'utilisateur (cas de la v�rification des r�gles)
      """
      dico={}
      # on ajoute les couples {nom mot-cl�:objet mot-cl�} effectivement pr�sents
      for v in self.mc_liste:
        if v == None : continue
        k=v.nom
        dico[k]=v
      if restreint == 'oui' : return dico
      # Si restreint != 'oui',
      # on ajoute les couples {nom mot-cl�:objet mot-cl�} des mots-cl�s simples
      # possibles pour peu qu'ils aient une valeur par d�faut
      for k,v in self.definition.entites.items():
        if v.label != 'SIMP' : continue
        if not v.defaut : continue
        if not dico.has_key(k):
          dico[k]=v(nom=k,val=None,parent=self)
      #on ajoute l'objet detenteur de regles pour des validations plus sophistiquees (a manipuler avec precaution)
      dico["self"]=self
      return dico



