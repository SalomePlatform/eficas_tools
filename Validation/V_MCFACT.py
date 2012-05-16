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
   Ce module contient la classe mixin MCFACT qui porte les m�thodes
   n�cessaires pour r�aliser la validation d'un objet de type MCFACT
   d�riv� de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilis�e par h�ritage multiple pour composer les traitements.
"""
# Modules EFICAS
import V_MCCOMPO
from Noyau.strfunc import ufmt

class MCFACT(V_MCCOMPO.MCCOMPO):
   """
      Cette classe a un attribut de classe :

      - txt_nat qui sert pour les comptes-rendus li�s � cette classe
   """

   txt_nat = u"Mot cl� Facteur :"

   def isvalid(self,sd='oui',cr='non'):
      """
         Methode pour verifier la validit� du MCFACT. Cette m�thode
         peut etre appel�e selon plusieurs modes en fonction de la valeur
         de sd et de cr.

         Si cr vaut oui elle cr�e en plus un compte-rendu
         sd est pr�sent pour compatibilit� de l'interface mais ne sert pas
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
        # Apr�s avoir v�rifi� la validit� de tous les sous-objets, on v�rifie
        # la validit� des r�gles
        text_erreurs,test_regles = self.verif_regles()
        if not test_regles :
          if cr == 'oui' : self.cr.fatal(_(u"R�gle(s) non respect�e(s) : %s"), text_erreurs)
          valid = 0
        #
        # On verifie les validateurs s'il y en a
        #
        if self.definition.validators and not self.definition.validators.verif(self.valeur):
           if cr == 'oui' :
              self.cr.fatal(_(u"Mot-cl� : %s devrait avoir %s"),
                                 self.nom, self.definition.validators.info())
           valid=0
        # fin des validateurs
        #
        if self.reste_val != {}:
          if cr == 'oui' :
            self.cr.fatal(_(u"Mots cl�s inconnus : %s"), ','.join(self.reste_val.keys()))
          valid=0
        self.valid = valid
        self.state = 'unchanged'
        if not old_valid or old_valid != self.valid :
           self.init_modif_up()
        return self.valid

