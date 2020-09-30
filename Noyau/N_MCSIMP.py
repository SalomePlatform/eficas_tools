# coding=utf-8
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


"""
    Ce module contient la classe MCSIMP qui sert à controler la valeur
    d'un mot-clé simple par rapport à sa définition portée par un objet
    de type ENTITE
"""

from __future__ import absolute_import
from copy import copy

from Noyau.N_ASSD import ASSD
from Noyau.N_CO import CO
from . import N_OBJECT
from .N_CONVERT import ConversionFactory
from .N_types import forceList, isSequence


class MCSIMP(N_OBJECT.OBJECT):

    """
    """
    nature = 'MCSIMP'

    def __init__(self, val, definition, nom, parent,objPyxbDeConstruction):
        """
           Attributs :

            - val : valeur du mot clé simple
            - definition
            - nom
            - parent

          Autres attributs :

            - valeur : valeur du mot-clé simple en tenant compte de la valeur par défaut

        """
        #print (self, val, definition, nom, parent)
        self.definition = definition
        self.nom = nom
        self.val = val
        self.parent = parent
        self.objPyxbDeConstruction = objPyxbDeConstruction
        if parent:
            self.jdc = self.parent.jdc
            if self.jdc : self.cata = self.jdc.cata
            else        : self.cata = None
            self.niveau = self.parent.niveau
            self.etape  = self.parent.etape
        else:
            # Le mot cle simple a été créé sans parent
            # est-ce possible ?
            print ('je suis dans le else sans parent du build')
            print (poum)
            self.jdc    = None
            self.cata   = None
            self.niveau = None
            self.etape  = None
        if self.definition.creeDesObjets : 
           self.convProto = ConversionFactory('UserASSD', self.definition.creeDesObjetsDeType)
        else : 
           self.convProto = ConversionFactory('type', typ=self.definition.type)
        self.valeur = self.getValeurEffective(self.val)
        if self.definition.utiliseUneReference :
          if self.valeur != None: 
             if not type(self.valeur) in (list, tuple): self.valeur.ajoutUtilisePar(self)
             else : 
               #PNPN --> chgt pour Vimmp
               for v in self.valeur : 
                   try : v.ajoutUtilisePar(self)
                   except : print ('il y a un souci ici', self.nom, self.valeur)
        self.buildObjPyxb()
        self.listeNomsObjsCrees = []

    def getValeurEffective(self, val):
        """
            Retourne la valeur effective du mot-clé en fonction
            de la valeur donnée. Defaut si val == None
        """
        if (val is None and hasattr(self.definition, 'defaut')): val = self.definition.defaut
        if self.jdc != None and val in list(self.jdc.sdsDict.keys()): return self.jdc.sdsDict[val]
         # dans le cas de lecture de .comm, il est possible que l objet est deja ete cree
         # peut-etre devrait on aussi verifier que val est de type string ?
        if self.definition.creeDesObjets : 
           # isinstance(val, self.definition.creeDesObjetsDeType) ne fonctionne pas car il y a un avec cata devant et l autre non
           if val != None :
             if  (not(val.__class__.__name__ == self.definition.creeDesObjetsDeType.__name__)) : 
                 val=self.convProto.convert(val)
             else :
                 if val.nom=='sansNom' : 
                    for leNom,laVariable in self.jdc.g_context.items():
                      if id(laVariable)== id(val) and (leNom != 'sansNom'):
                         val.initialiseNom(leNom)
                 if val.parent== None : val.initialiseParent(self) 
           return val
        if self.convProto:
           val = self.convProto.convert(val)
        return val

    def creeUserASSDetSetValeur(self, val):
        self.state='changed'
        nomVal=val
        if nomVal in self.jdc.sdsDict.keys():
           if isinstance(self.jdc.sdsDict[nomVal],self.definition.creeDesObjetsDeType): return (0, 'concept deja reference')
           else : return (0, 'concept d un autre type existe deja')
        if self.convProto:
            objVal = self.convProto.convert(nomVal)
            objVal.initialiseNom(nomVal)
            if objVal.parent== None : objVal.initialiseParent(self) 
            p=self.parent
            while p in self.parent :
                  print ('mise a jour de ',p)
                  if hasattr(p, 'listeDesReferencesCrees') : p.listeDesReferencesCrees.append(objVal)
                  else : p.listeDesReferencesCrees=(objVal,)
                  p=p.parent
        return (self.setValeur(objVal), 'reference creee')

    def creeUserASSD(self, val):
        self.state='changed'
        nomVal=val
        if nomVal in self.jdc.sdsDict.keys():
           if isinstance(self.jdc.sdsDict[nomVal],self.definition.creeDesObjetsDeType): return (0,None, 'concept deja reference')
           else : return (0, None, 'concept d un autre type existe deja')
        if self.convProto:
            objVal = self.convProto.convert(nomVal)
            objVal.initialiseNom(nomVal)
        return (1, objVal, 'reference creee')

    def rattacheUserASSD(self, objASSD):
        if objASSD.parent== None : objASSD.initialiseParent(self) 
        p=self.parent
        while p in self.parent :
           if hasattr(p, 'listeDesReferencesCrees') : p.listeDesReferencesCrees.append(objASSD)
           else : p.listeDesReferencesCrees=(objASSD,)
           p=p.parent

      
    def getValeur(self):
        """
            Retourne la "valeur" d'un mot-clé simple.
            Cette valeur est utilisée lors de la création d'un contexte
            d'évaluation d'expressions à l'aide d'un interpréteur Python
        """
        v = self.valeur
        # Si singleton et max=1, on retourne la valeur.
        # Si une valeur simple et max='**', on retourne un singleton.
        # (si liste de longueur > 1 et max=1, on sera arrêté plus tard)
        # Pour accepter les numpy.array, on remplace : "type(v) not in (list, tuple)"
        # par "not has_attr(v, '__iter__')".
        if v is None:
            pass
        elif isSequence(v) and len(v) == 1 and self.definition.max == 1:
            v = v[0]
        elif not isSequence(v) and self.definition.max != 1:
            v = (v, )
        # traitement particulier pour les complexes ('RI', r, i)
        if 'C' in self.definition.type and self.definition.max != 1 and v != None and v[0] in ('RI', 'MP'):
            v = (v, )
        return v

    def getVal(self):
        """
            Une autre méthode qui retourne une "autre" valeur du mot clé simple.
            Elle est utilisée par la méthode getMocle
        """
        return self.valeur

    def accept(self, visitor):
        """
           Cette methode permet de parcourir l'arborescence des objets
           en utilisant le pattern VISITEUR
        """
        visitor.visitMCSIMP(self)

    def copy(self):
        """ Retourne une copie de self """
        objet = self.makeobjet()
        # il faut copier les listes et les tuples mais pas les autres valeurs
        # possibles (réel,SD,...)
        if type(self.valeur) in (list, tuple):
            objet.valeur = copy(self.valeur)
        else:
            objet.valeur = self.valeur
        objet.val = objet.valeur
        return objet

    def makeobjet(self):
        return self.definition(val=None, nom=self.nom, parent=self.parent)

    def reparent(self, parent):
        """
           Cette methode sert a reinitialiser la parente de l'objet
        """
        self.parent = parent
        self.jdc = parent.jdc
        self.etape = parent.etape

    def getSd_utilisees(self):
        """
            Retourne une liste qui contient la ou les SD utilisée par self si c'est le cas
            ou alors une liste vide
        """
        l = []
        if isinstance(self.valeur, ASSD):
            l.append(self.valeur)
        elif type(self.valeur) in (list, tuple):
            for val in self.valeur:
                if isinstance(val, ASSD):
                    l.append(val)
        return l

    def getSd_mcs_utilisees(self):
        """
            Retourne la ou les SD utilisée par self sous forme d'un dictionnaire :
              - Si aucune sd n'est utilisée, le dictionnaire est vide.
              - Sinon, la clé du dictionnaire est le mot-clé simple ; la valeur est
                la liste des sd attenante.

                Exemple ::
                        { 'VALE_F': [ <Cata.cata.fonction_sdaster instance at 0x9419854>,
                                      <Cata.cata.fonction_sdaster instance at 0x941a204> ] }
        """
        l = self.getSd_utilisees()
        dico = {}
        if len(l) > 0:
            dico[self.nom] = l
        return dico


    def getMcsWithCo(self, co):
        """
            Cette methode retourne l'objet MCSIMP self s'il a le concept co
            comme valeur.
        """
        if co in forceList(self.valeur):
            return [self, ]
        return []

    def getAllCo(self):
        """
            Cette methode retourne la liste de tous les concepts co
            associés au mot cle simple
        """
        return [co for co in forceList(self.valeur)
                if isinstance(co, CO) and co.isTypCO()]

    def supprime(self):
        if hasattr(self, 'val') and hasattr(self.val, 'supprime') :self.val.supprime()
        N_OBJECT.OBJECT.supprime(self)
