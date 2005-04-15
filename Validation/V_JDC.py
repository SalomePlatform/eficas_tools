#@ MODIF V_JDC Validation  DATE 14/09/2004   AUTEUR MCOURTOI M.COURTOIS 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
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
#                                                                       
#                                                                       
# ======================================================================


"""
   Ce module contient la classe mixin JDC qui porte les m�thodes
   n�cessaires pour r�aliser la validation d'un objet de type JDC
   d�riv� de OBJECT.

   Une classe mixin porte principalement des traitements et est
   utilis�e par h�ritage multiple pour composer les traitements.
"""
# Modules Python
import string,types

# Modules EFICAS
import V_MCCOMPO
from Noyau.N_Exception import AsException
from Noyau.N_utils import AsType

class JDC(V_MCCOMPO.MCCOMPO):
   """
   """

   def report(self):
      """ 
          Methode pour generation d un rapport de validite
      """
      self.cr.purge()
      self.cr.debut="DEBUT CR validation : "+self.nom
      self.cr.fin="FIN CR validation :"+self.nom
      for e in self.etapes :
        if e.isactif():
          self.cr.add(e.report())
      self.state = 'modified'
      self.isvalid(cr='oui')
      return self.cr

   def isvalid(self,cr='non'):
      """
        M�thode bool�enne qui retourne 0 si le JDC est invalide, 1 sinon
      """
      # FR : on prend en compte l'�tat du JDC ('unchanged','modified','undetermined')
      # afin d'acc�l�rer le test de validit� du JDC 
      if self.state == 'unchanged':
        return self.valid
      else:
        valid = 1
        texte,test = self.verif_regles()
        if test == 0:
          if cr == 'oui': self.cr.fatal(string.strip(texte))
          valid = 0
        if valid :
          for e in self.etapes:
            if not e.isactif() : continue
            if not e.isvalid():
              valid = 0
              break
        self.state="unchanged"
        self.valid = valid
        return self.valid

   def verif_regles(self):
      """ 
         Effectue la v�rification de validit� des r�gles du jeu de commandes 
      """
      l_noms_etapes=self.get_l_noms_etapes()
      texte_global = ''
      test_global = 1
      for regle in self.regles :
        texte,test = regle.verif(l_noms_etapes)
        texte_global = texte_global + texte
        test_global = test_global*test
      return texte_global,test_global

   def get_l_noms_etapes(self):
      """ 
          Retourne la liste des noms des �tapes de self 
      """
      l=[]
      for etape in self.etapes:
        l.append(etape.nom)
      return l
