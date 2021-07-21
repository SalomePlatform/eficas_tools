# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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
from __future__ import absolute_import
import Noyau

from . import CONNECTOR
import re
conceptRE=re.compile(r'[a-zA-Z_]\w*$')

class OBJECT:
  from Noyau.N_CO import CO
  from Noyau.N_ASSD import assd

  def isMCList(self):
    """ 
        Retourne 1 si self est une MCList (liste de mots-cles), 0 sinon (defaut) 
    """
    return 0

  def getRegles(self):
    """ 
       Retourne les regles de self 
    """
    if hasattr(self,'definition'):
      return self.definition.regles
    elif hasattr(self,'regles'):
      return self.regles
    else :
      return []

  def initModif(self):
    """
       Met l'etat de l'objet a modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    if self.parent:
      self.parent.initModif()

  def finModif(self):
      """
      Methode appelee apres qu'une modification a ete faite afin de declencher
      d'eventuels traitements post-modification
      """
      #print "finModif",self
      # pour les objets autres que les commandes, aucun traitement specifique 
      # on remonte l'info de fin de modif au parent
      CONNECTOR.Emit(self,"valid")
      if self.parent:
        self.parent.finModif()

  def isRepetable(self):
    """
         Indique si l'objet est repetable
    """
    return 0

  def listeMcPresents(self):
    """
         Retourne la liste des noms des mots cles presents
    """
    return []

  def getDocu(self):
    return self.definition.getDocu()

  def getListeMcInconnus(self):
     """
     Retourne la liste des mots-cles inconnus dans self
     """
     return []

  def verifConditionRegles(self,liste_presents):
    """ 
        Retourne la liste des mots-cles a rajouter pour satisfaire les regles
        en fonction de la liste des mots-cles presents 
    """
    liste=[]
    for regle in self.definition.regles:
        liste=regle.verifConditionRegle(liste,liste_presents)
    return liste

  def verifConditionBloc(self):
    """ 
        Evalue les conditions de tous les blocs fils possibles 
        (en fonction du catalogue donc de la definition) de self et
        retourne deux listes :
          - la premiere contient les noms des blocs a rajouter
          - la seconde contient les noms des blocs a supprimer
    """
    return [],[]

  def getGenealogiePrecise(self):
    if self.parent:
       l=self.parent.getGenealogiePrecise()
       l.append(self.nom.strip())
       return l
    else:
       return [self.nom.strip()]


  def getGenealogie(self):
    """ 
        Retourne la liste des noms des ascendants (noms de MCSIMP,MCFACT,MCBLOC
        ou ETAPE) de self jusqu'au premier objet etape rencontre
    """
    if self.parent:
       l=self.parent.getGenealogie()
       l.append(self.nom.strip())
       return l
    else:
       return [self.nom.strip()]

  def getFr(self):
     """
         Retourne la chaine d'aide contenue dans le catalogue
         en tenant compte de la langue
     """
     try:
     #if 1 :
        c=getattr(self.definition,self.jdc.lang)
        return c
     except:
     #else:
        try :
            c=getattr(self.definition,"fr")
            return c
        except :
            return ''

  def updateConcept(self,sd):
     pass

  def normalize(self):
     """ Retourne l'objet normalise. En general self sauf si
         pour etre insere dans l'objet pere il doit etre 
         wrappe dans un autre objet (voir mot cle facteur).
     """
     return self

  def deleteMcGlobal(self):
     return

  def updateMcGlobal(self):
     return

  #def __del__(self):
  #   print "__del__",self

  def nommeSd(self):
  # surcharge dans I_ETAPE.py
      if ( nom in dir(self.jdc.cata)) : return (0, nom + tr("mot reserve"))
      if not conceptRE.match(nom):
         return 0, tr("Un nom de concept doit etre un identificateur Python")
      self.initModif()
      #self.getSdProd()
      #self.sd.nom = nom
      #self.sdnom=nom
      #self.parent.updateConceptAfterEtape(self,self.sd)
      #self.finModif()
      #return 1, tr("Nommage du concept effectue")

  def deleteRef(self):
  # doit etre surcharge dans MC_COMPO et MC_SIMP 
      pass

  def demandeRedessine(self):
      CONNECTOR.Emit(self,"redessine")



class ErrorObj(OBJECT):pass

