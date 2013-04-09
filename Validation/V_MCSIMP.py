# -*- coding: iso-8859-1 -*-
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
   Ce module contient la classe mixin MCSIMP qui porte les m�thodes
   n�cessaires pour r�aliser la validation d'un objet de type MCSIMP
   d�riv� de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilis�e par h�ritage multiple pour composer les traitements.
"""
# Modules Python
import traceback

# Modules EFICAS
from Noyau import N_CR
from Noyau.N_Exception import AsException
from Noyau.N_VALIDATOR import ValError,TypeProtocol,CardProtocol,IntoProtocol
from Noyau.N_VALIDATOR import listProto
from Noyau.strfunc import ufmt

class MCSIMP:
   """
      COMMENTAIRE CCAR:
      Cette classe est quasiment identique � la classe originale d'EFICAS
      a part quelques changements cosm�tiques et des chagements pour la
      faire fonctionner de facon plus autonome par rapport � l'environnement
      EFICAS

      A mon avis, il faudrait aller plus loin et r�duire les d�pendances
      amont au strict n�cessaire.

          - Est il indispensable de faire l'�valuation de la valeur dans le contexte
            du jdc dans cette classe.

          - Ne pourrait on pas doter les objets en pr�sence des m�thodes suffisantes
            pour �viter les tests un peu particuliers sur GEOM, PARAMETRE et autres. J'ai
            d'ailleurs modifi� la classe pour �viter l'import de GEOM
   """

   CR=N_CR.CR

   def __init__(self):
      self.state='undetermined'
      self.typeProto=TypeProtocol("type",typ=self.definition.type)
      self.intoProto=IntoProtocol("into",into=self.definition.into,val_min=self.definition.val_min,val_max=self.definition.val_max)
      self.cardProto=CardProtocol("card",min=self.definition.min,max=self.definition.max)

   def get_valid(self):
       if hasattr(self,'valid'):
          return self.valid
       else:
          self.valid=None
          return None

   def set_valid(self,valid):
       old_valid=self.get_valid()
       self.valid = valid
       self.state = 'unchanged'
       if not old_valid or old_valid != self.valid :
           self.init_modif_up()

   def isvalid(self,cr='non'):
      """
         Cette m�thode retourne un indicateur de validit� de l'objet de type MCSIMP

           - 0 si l'objet est invalide
           - 1 si l'objet est valide

         Le param�tre cr permet de param�trer le traitement. Si cr == 'oui'
         la m�thode construit �galement un comte-rendu de validation
         dans self.cr qui doit avoir �t� cr�� pr�alablement.
      """
      if self.state == 'unchanged':
        return self.valid
      else:
        valid = 1
        v=self.valeur
        #  verification presence
        if self.isoblig() and v == None :
          if cr == 'oui' :
            self.cr.fatal(_(u"Mot-cl� : %s obligatoire non valoris�"), self.nom)
          valid = 0

        lval=listProto.adapt(v)
        if lval is None:
           valid=0
           if cr == 'oui' :
              self.cr.fatal(_(u"None n'est pas une valeur autoris�e"))
        else:
           # type,into ...
           #typeProto=TypeProtocol("type",typ=self.definition.type)
           #intoProto=IntoProtocol("into",into=self.definition.into,val_min=self.definition.val_min,val_max=self.definition.val_max)
           #cardProto=CardProtocol("card",min=self.definition.min,max=self.definition.max)
           #typeProto=self.definition.typeProto
           #intoProto=self.definition.intoProto
           #cardProto=self.definition.cardProto
           typeProto=self.typeProto
           intoProto=self.intoProto
           cardProto=self.cardProto
           if cr == 'oui' :
               #un cr est demand� : on collecte tous les types d'erreur
               try:
                   for val in lval:
                       typeProto.adapt(val)
               except ValError,e:
                   valid=0
                   self.cr.fatal(*e)
               try:
                   for val in lval:
                       intoProto.adapt(val)
               except ValError,e:
                   valid=0
                   self.cr.fatal(*e)
                   #self.cr.fatal(unicode(e))
               try:
                   cardProto.adapt(lval)
               except ValError,e:
                   valid=0
                   self.cr.fatal(*e)
                   #self.cr.fatal(unicode(e))
               #
               # On verifie les validateurs s'il y en a et si necessaire (valid == 1)
               #
               if valid and self.definition.validators:
                   try:
                       self.definition.validators.convert(lval)
                   except ValError,e:
                       self.cr.fatal(_(u"Mot-cl� %s invalide : %s\nCrit�re de validit�: %s"),
                            self.nom, str(e), self.definition.validators.info())
                       valid=0
           else:
               #si pas de cr demande, on sort a la toute premiere erreur
               try:
                   for val in lval:
                       typeProto.adapt(val)
                       intoProto.adapt(val)
                   cardProto.adapt(lval)
                   if self.definition.validators:
                       if hasattr(self.definition.validators,'set_MCSimp'):
                          self.definition.validators.set_MCSimp(self)
                       self.definition.validators.convert(lval)
               except ValError,e:
                   valid=0

        self.set_valid(valid)
        return self.valid

   def isoblig(self):
      """ indique si le mot-cl� est obligatoire
      """
      return self.definition.statut=='o'

   def init_modif_up(self):
      """
         Propage l'�tat modifi� au parent s'il existe et n'est l'objet
         lui-meme
      """
      if self.parent and self.parent != self :
        self.parent.state = 'modified'

   def report(self):
      """ g�n�re le rapport de validation de self """
      self.cr=self.CR()
      self.cr.debut = u"Mot-cl� simple : "+self.nom
      self.cr.fin = u"Fin Mot-cl� simple : "+self.nom
      self.state = 'modified'
      try:
        self.isvalid(cr='oui')
      except AsException,e:
        if CONTEXT.debug : traceback.print_exc()
        self.cr.fatal(_(u"Mot-cl� simple : %s %s"), self.nom, e)
      return self.cr






