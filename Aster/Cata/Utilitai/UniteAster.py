#@ MODIF UniteAster Utilitai  DATE 11/05/2005   AUTEUR MCOURTOI M.COURTOIS 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2005  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY  
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY  
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR     
# (AT YOUR OPTION) ANY LATER VERSION.                                                  
#                                                                       
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT   
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF            
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU      
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.                              
#                                                                       
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE     
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,         
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.        
# ======================================================================

import types

import aster
from Cata.cata import _F, DEFI_FICHIER, INFO_EXEC_ASTER, DETRUIRE

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class UniteAster:
   """Classe pour manipuler les fichiers en Python en accord avec les unit�s
   logiques utilis�es en Fortran.
   De mani�re analogue au Fortran, les �tats possibles d'une unit� sont :
      'F' : ferm�, 'O' : ouvert, 'R' : r�serv�.

   M�thodes :
      Nom      : Retourne le nom du fichier associ� � une unit�,
      Etat     : Retourne l'�tat d'une unit�,
      Libre    : Retourne un num�ro d'unit� libre,
      EtatInit : Remet une, plusieurs ou toutes les unit�s dans leur �tat initial.

   M�thode priv�e :
      _setinfo : pour remplir le dictionnaire des 'infos'
   Attribut priv� :
      infos[num�ro unit�] = { 'nom' : x, 'etat' : x , 'etat_init' : x }
   """
#-------------------------------------------------------------------------------
   def __init__(self):
      """Initialise le dictionnaire des unit�s.
      """
      self.infos = {}

#-------------------------------------------------------------------------------
   def _setinfo(self, ul):
      """Remplit les infos de l'unit� 'ul'.
      """
      # ul peut etre un entier Aster
      try:
         unit = ul.valeur
      except:
         unit = int(ul)
      # Si la cl� n'existe pas
      ini = False
      if not self.infos.has_key(unit):
         self.infos[unit] = {}
         self.infos[unit]['nom']       = ''
         self.infos[unit]['etat']      = '?'
         self.infos[unit]['etat_init'] = '?'
         ini = True

      __tab=INFO_EXEC_ASTER(UNITE=unit, LISTE_INFO=('ETAT_UNITE'))
      
      # O:ouvert, F:ferm�, R:r�serv�
      self.infos[unit]['etat'] = __tab['ETAT_UNITE',1].strip()[0]
      if ini:
         self.infos[unit]['etat_init'] = self.infos[unit]['etat']

      # nom du fichier
      if self.infos[unit]['etat'] in ['O', 'R']:
         nomfich=''.join([__tab['NOMFIC%d' % i,1] for i in range(1,5)]).strip()
      elif self.infos[unit]['etat'] == 'F':
         nomfich='fort.'+str(unit)
      else:
         message = "Etat de l'unit� inconnu : %s" % self.infos[unit]['etat']
         print __tab.EXTR_TABLE()
         raise aster.FatalError,"<F> <UniteAster._setinfo> %s" % message
      self.infos[unit]['nom'] = nomfich
      DETRUIRE(CONCEPT=_F(NOM=__tab))

#-------------------------------------------------------------------------------
   def Libre(self, nom=None):
      """R�serve et retourne une unit� libre en y associant, s'il est fourni,
      le fichier 'nom'.
      """
      __tab=INFO_EXEC_ASTER(LISTE_INFO=('UNITE_LIBRE'))
      unit = __tab['UNITE_LIBRE',1]
      DETRUIRE(CONCEPT=_F(NOM=__tab))
      if nom==None:
         nom='fort.'+str(unit)

      # Si la cl� existe, c'est que le fichier n'�tait pas libre
      if self.infos.has_key(unit):
         message = "Cette unit� est d�j� affect�e au fichier %s" % \
            self.infos[unit]['nom']
         raise aster.FatalError,"<F> <UniteAster.Libre> %s" % message

      DEFI_FICHIER(ACTION='RESERVER', UNITE=unit , FICHIER=nom.strip())
      self.infos[unit] = {}
      self.infos[unit]['nom']       = nom.strip()
      self.infos[unit]['etat']      = 'R'
      self.infos[unit]['etat_init'] = 'F'
      return unit

#-------------------------------------------------------------------------------
   def Nom(self, ul):
      """Retourne le nom du fichier associ� � l'unit� 'ul'.
      """
      # ul peut etre un entier Aster
      try:
         unit = ul.valeur
      except:
         unit = int(ul)
      # Si la cl� n'existe pas
      if not self.infos.has_key(unit):
         self._setinfo(unit)
      return self.infos[unit]['nom']

#-------------------------------------------------------------------------------
   def Etat(self, ul, **kargs):
      """Retourne l'�tat de l'unit� si 'etat' n'est pas fourni
      et/ou change son �tat :
         kargs['etat']  : nouvel �tat,
         kargs['TYPE']  : type du fichier � ouvrir ASCII/BINARY/LIBRE,
         kargs['ACCES'] : type d'acc�s NEW/APPEND/OLD.
      """
      # ul peut etre un entier Aster
      try:
         unit = ul.valeur
      except:
         unit = int(ul)
      # Si la cl� n'existe pas
      if not self.infos.has_key(unit):
         self._setinfo(unit)
      if not kargs.has_key('etat'):
         return self.infos[unit]['etat']

      # En fonction de la demande, on bascule son �tat ou pas
      new = kargs.get('etat')
      if not new in ['R', 'F', 'O']:
         message = "Nouvel �tat de l'unit� incorrect : %s" % new
         raise aster.FatalError,"<F> <UniteAster.Etat> %s" % message

      if self.infos[unit]['etat'] == new:
         pass
      elif new == 'R':
         if self.infos[unit]['etat'] == 'O':
            DEFI_FICHIER(ACTION='LIBERER',  UNITE=unit)
         DEFI_FICHIER(ACTION  = 'RESERVER', 
                      UNITE   = unit,
                      FICHIER = self.infos[unit]['nom'])
      elif new == 'F':
         DEFI_FICHIER(ACTION='LIBERER', UNITE=unit)
      elif new == 'O':
         if self.infos[unit]['etat'] == 'R':
            DEFI_FICHIER(ACTION='LIBERER', UNITE=unit)
         DEFI_FICHIER(ACTION  ='ASSOCIER',
                      UNITE   = unit,
                      FICHIER = self.infos[unit]['nom'],
                      TYPE    = kargs.get('TYPE', 'ASCII'),
                      ACCES   = kargs.get('ACCES', 'APPEND'),)
      self.infos[unit]['etat'] = new
      return self.infos[unit]['etat']

#-------------------------------------------------------------------------------
   def EtatInit(self, ul=None):
      """Remet l'unit� 'ul' dans son �tat initial.
      Si 'ul' est omis, toutes les unit�s sont remises dans leur �tat initial.
      """
      if ul == None:
         for uli, vul in self.infos.items():
            self.Etat(uli, etat=vul['etat_init'])
      else:
         if not type(ul) in [types.ListType, types.TupleType]:
            ul=[ul,]
         for u in ul:
            # u peut etre un entier Aster
            try:
               unit = u.valeur
            except:
               unit = int(u)
            # Si la cl� n'existe pas
            if not self.infos.has_key(unit):
               self._setinfo(unit)
            else:
               self.Etat(unit, etat=self.infos[unit]['etat_init'])