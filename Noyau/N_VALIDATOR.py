# coding=utf-8
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

# ======================================================================

"""
   Ce module contient toutes les classes necessaires pour
   implanter le concept de validateur dans Accas
"""
from __future__ import absolute_import
from __future__ import print_function
try :
    from builtins import str
    from builtins import object
except : pass

import types
import traceback
import re
from .N_ASSD import ASSD
from .N_types import isInt, isFloat_or_int, isComplex, isNumber, isStr, isSequence
from Accas import A_TUPLE
from Extensions.i18n import tr



class ValError(Exception):
    pass


def cls_mro(cls):
    if hasattr(cls, "__mro__"):
        return cls.__mro__
    mro = [cls]
    for base in cls.__bases__:
        mro.extend(cls_mro(base))
    return mro


class Protocol(object):

    def __init__(self, name):
        self.registry = {}
        self.name = name
        self.args = {}

    def register(self, T, A):
        print ('register Protocol',T,A)
        self.registry[T] = A

    def adapt(self, obj):
        # (a) verifier si l'objet peut s'adapter au protocole
        adapt = getattr(obj, '__adapt__', None)
        if adapt is not None:
            # on demande à l'objet obj de réaliser lui-meme l'adaptation
            return adapt(self)

        # (b) verifier si un adapteur est enregistré (si oui l'utiliser)
        if self.registry:
            for T in cls_mro(obj.__class__):
                if T in self.registry:
                    return self.registry[T](obj, self, **self.args)

        # (c) utiliser l'adapteur par defaut
        return self.default(obj, **self.args)

    def default(self, obj, **args):
        raise TypeError("Can't adapt %s to %s" %
                        (obj.__class__.__name__, self.name))


class PProtocol(Protocol):

    """Verificateur de protocole paramétré (classe de base)"""
    # Protocole paramétré. Le registre est unique pour toutes les instances.
    # La methode register est une methode de classe
    registry = {}

    def __init__(self, name, **args):
        self.name = name
        self.args = args

    def register(cls, T, A):
        cls.registry[T] = A
    register = classmethod(register)


class ListProtocol(Protocol):

    """Verificateur de protocole liste : convertit un objet quelconque en liste pour validation ultérieure"""

    def default(self, obj):
        if type(obj) is tuple:
            if len(obj) > 0 and obj[0] in ('RI', 'MP'):
                # il s'agit d'un complexe ancienne mode. La cardinalite vaut 1
                return (obj,)
            else:
                return obj
        elif type(obj) is list:
            return obj
        elif obj == None:
            # pas de valeur affecte. La cardinalite vaut 0
            return obj
        elif isStr(obj):
            # il s'agit d'une chaine. La cardinalite vaut 1
            return (obj,)
        else:
            try:
                # si l'objet supporte len, on a la cardinalite
                length = len(obj)
                return obj
            except:
                # sinon elle vaut 1
                return (obj,)

listProto = ListProtocol("list")


class TypeProtocol(PProtocol):

    """Verificateur de type parmi une liste de types possibles"""
    # pas de registre par instance. Registre unique pour toutes les instances
    # de TypeProtocol
    registry = {}

    def __init__(self, name, typ=None):
        PProtocol.__init__(self, name, typ=typ)
        self.typ = typ

    def default(self, obj, typ):
        err = ""
        for type_permis in typ:
            if type_permis == 'createObject': continue
            if type_permis == 'R':
                if isFloat_or_int(obj):
                    return obj
            elif type_permis == 'I':
                if isInt(obj):
                    return obj
            elif type_permis == 'C':
                if self.isComplexe(obj):
                    return obj
            elif type_permis == 'TXM':
                if isStr(obj):
                    return obj
            elif type_permis == 'shell':
                if isStr(obj):
                    return obj
            elif type_permis == 'Fichier':
                import os
                try :
                    if (len(typ) > 2 and typ[2] == "Sauvegarde") or os.path.isfile(obj):
                        return obj
                    else:
                        raise ValError( "%s n'est pas un fichier valide" % repr(obj))
                except :
                    raise ValError( "%s n'est pas un fichier valide" % repr(obj))

            elif type_permis == 'FichierNoAbs':
                import os
                if (len(typ) > 2 and typ[2] == "Sauvegarde") or isinstance(obj, type("")):
                    return obj
                else:
                    raise ValError( "%s n'est pas un fichier valide" % repr(obj))

            elif type_permis == 'Repertoire':
                import os
                try :
                    if os.path.isdir(obj): return obj
                    else: raise ValError( "%s n'est pas un repertoire valide" % repr(obj))
                except :
                    raise ValError( "%s n'est pas un repertoire valide" % repr(obj))
            elif type_permis == 'FichierOuRepertoire':
                import os
                try :
                    if os.path.isdir(obj) or os.path.isfile(obj): return obj
                    else: raise ValError( "%s n'est pas un fichier ou un repertoire valide" % repr(obj))
                except :
                    raise ValError( "%s n'est pas un fichier ou un repertoire valide" % repr(obj))
            elif type(type_permis) == type or isinstance(type_permis, type):
                try:
                    if self.isObjectFrom(obj, type_permis):
                        return obj
                except Exception as err:
                    pass
            elif  isinstance(type_permis, A_TUPLE.Tuple):
                try:
                    if type_permis.__convert__(obj):
                        return obj
                except Exception as err:
                    pass
            elif  isinstance(type_permis, object):
                try:
                    if type_permis.__convert__(obj):
                        return obj
                except Exception as err:
                    pass
            else:
                print(("Type non encore gere %s" %type_permis))
        raise ValError(
            tr("%s (de type %s) n'est pas d'un type autorise: %s ") % (repr(obj), type(obj), typ))
        #import traceback; traceback.print_stack()
        #print (object, type_permis,)

    def isComplexe(self, valeur):
        """ Retourne 1 si valeur est un complexe, 0 sinon """
        if isNumber(valeur):
            # Pour permettre l'utilisation de complexes Python (accepte les
            # entiers et réels)
            return 1
        elif type(valeur) != tuple:
            # On n'autorise pas les listes pour les complexes
            return 0
        elif len(valeur) != 3:
            return 0
        else:
            # Un complexe doit etre un tuple de longueur 3 avec 'RI' ou 'MP' comme premiere
            # valeur suivie de 2 reels.
            if valeur[0].strip() in ('RI', 'MP'):
                try:
                    v1 = reelProto.adapt(valeur[1]), reelProto.adapt(valeur[2])
                    return 1
                except:
                    return 0
            else:
                return 0

    def isObjectFrom(self, objet, classe):
        """
           Retourne 1 si objet est une instance de la classe classe, 0 sinon
        """
        convert = getattr(classe, '__convert__', None)
        if convert is not None:
            # classe verifie les valeurs
            try:
                v = convert(objet)
                return v is not None
            except ValueError as err:
                raise
            except:
                return 0
        # On accepte les instances de la classe et des classes derivees
        return isinstance(objet, classe)

reelProto = TypeProtocol("reel", typ=('R',))


class CardProtocol(PProtocol):

    """Verificateur de cardinalité """
    # pas de registre par instance. Registre unique pour toutes les instances
    registry = {}

    def __init__(self, name, min=1, max=1):
        PProtocol.__init__(self, name, min=min, max=max)

    def default(self, obj, min, max):
        length = len(obj)
        if (length < min) or( length > max):
            raise ValError(
                "Nombre d'arguments de %s incorrect (min = %s, max = %s)" % (repr(obj), min, max))
        return obj


class IntoProtocol(PProtocol):

    """Verificateur de choix possibles : liste discrète ou intervalle"""
    # pas de registre par instance. Registre unique pour toutes les instances
    registry = {}

    def __init__(self, name, into=None, val_min=float('-inf'), val_max=float('inf')):

        PProtocol.__init__(
            self, name, into=into, val_min=val_min, val_max=val_max)
        self.val_min = val_min
        self.val_max = val_max

    def default(self, obj, into, val_min, val_max):
        if type(into)  ==types.FunctionType :
            maListeDeValeur=into()
            into=maListeDeValeur
        if into:
            if obj not in into:
                raise ValError(
                        tr("La valeur : %s  ne fait pas partie des choix possibles %s") % (repr(obj), into))
        else:
            # on est dans le cas d'un ensemble continu de valeurs possibles
            # (intervalle)
            if isFloat_or_int(obj):
                if val_min == '**':
                    val_min = obj - 1
                if val_max == '**':
                    val_max = obj + 1
                if obj < val_min or obj > val_max:
                    raise ValError(
                     tr("La valeur : %s est en dehors du domaine de validite [ %s , %s ]") %(repr(obj), self.val_min, self.val_max))
        return obj


class MinStr(object):
    # exemple de classe pour verificateur de type
    # on utilise des instances de classe comme type (typ=MinStr(3,6), par
    # exemple)

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __convert__(self, valeur):
        if isStr(valeur) and self.min <= len(valeur) <= self.max: return valeur
        raise ValError(
            "%s n'est pas une chaine de longueur comprise entre %s et %s" % (valeur, self.min, self.max))

    def __repr__(self):
        return tr("TXM de longueur entre %s et %s" % (self.min, self.max))


class Valid(PProtocol):

    """
         Cette classe est la classe mere des validateurs Accas
         Elle doit etre derivee
         Elle presente la signature des methodes indispensables pour son bon
         fonctionnement et dans certains cas leur comportement par défaut.

         @ivar cata_info: raison de la validite ou de l'invalidite du validateur meme
         @type cata_info: C{}
    """
    registry = {}

    def __init__(self, **args):
        PProtocol.__init__(self, "valid", **args)

    def info(self):
        """
           Cette methode retourne une chaine de caractères informative sur
           la validation demandée par le validateur. Elle est utilisée
           pour produire le compte-rendu de validité du mot clé associé.
        """
        return "valeur valide"

    def aide(self):
        """
           Cette methode retourne une chaine de caractère qui permet
           de construire un message d'aide en ligne.
           En général, le message retourné est le meme que celui retourné par la
           méthode info.
        """
        return self.info()

    def infoErreurItem(self):
        """
           Cette méthode permet d'avoir un message d'erreur pour un item
           dans une liste dans le cas ou le validateur fait des vérifications
           sur les items d'une liste. Si le validateur fait seulement des
           vérifications sur la liste elle meme et non sur ses items, la méthode
           doit retourner une chaine vide.
        """
        return " "

    def infoErreurListe(self):
        """
           Cette méthode a un comportement complémentaire de celui de
           infoErreurItem. Elle retourne un message d'erreur lié uniquement
           aux vérifications sur la liste elle meme et pas sur ses items.
           Dans le cas où le validateur ne fait pas de vérification sur des
           listes, elle retourne une chaine vide
        """
        return " "

    def verif(self, valeur):
        """
            Cette methode sert a verifier si la valeur passee en argument est consideree
            comme valide ou non par le validateur. Dans le premier cas le validateur retourne 1
            (valide) sinon 0 (invalide).

            @type valeur: tout type python
            @param valeur: valeur du mot cle a valider
            @rtype: C{boolean}
            @return: indicateur de validite 1 (valide) ou 0 (invalide)
        """
        raise NotImplementedError("Must be implemented")

    def verifItem(self, valeur):
        """
           La methode verif du validateur effectue une validation complete de
           la valeur. valeur peut etre un scalaire ou une liste. Le validateur
           doit traiter les 2 aspects s'il accepte des listes (dans ce cas la
           methode isList doit retourner 1).
           La methode valid_item sert pour effectuer des validations partielles
           de liste. Elle doit uniquement verifier la validite d'un item de
           liste mais pas les caracteristiques de la liste.
        """
        return 0

    def valideListePartielle(self, liste_courante):
        """
           Cette methode retourne un entier qui indique si liste_courante est partiellement valide (valeur 1)
           ou invalide (valeur 0). La validation partielle concerne les listes en cours de construction : on
           veut savoir si la liste en construction peut etre complétée ou si elle peut déjà etre considérée
           comme invalide.
           En général un validateur effectue la meme validation pour les listes partielles et les
           listes complètes.
        """
        return self.verif(liste_courante)

    def verifCata(self):
        """
            Cette methode sert a realiser des verifications du validateur lui meme.
            Elle est facultative et retourne 1 (valide) par defaut.
            Elle retourne 0 si le validateur est lui meme invalide si par exemple ses
            parametres de definition ne sont pas corrects.
            La raison de l'invalidite est stockee dans l'attribut cata_info.

            @rtype: C{boolean}
            @return: indicateur de validite 1 (valide) ou 0 (invalide)
        """
        return 1

    def isList(self):
        """
           Cette méthode retourne un entier qui indique si le validateur
           permet les listes (valeur 1) ou ne les permet pas (valeur 0).
           Par défaut, un validateur n'autorise que des scalaires.
        """
        return 0

    def hasInto(self):
        """
           Cette méthode retourne un entier qui indique si le validateur
           propose une liste de choix (valeur 1) ou n'en propose pas.
           Par défaut, un validateur n'en propose pas.
        """
        return 0

    def getInto(self, liste_courante=None, into_courant=None):
        """
           Cette méthode retourne la liste de choix proposée par le validateur.
           Si le validateur ne propose pas de liste de choix, la méthode
           retourne None.
           L'argument d'entrée liste_courante, s'il est différent de None, donne
           la liste des choix déjà effectués par l'utilisateur. Dans ce cas, la
           méthode getInto doit calculer la liste des choix en en tenant
           compte. Par exemple, si le validateur n'autorise pas les répétitions,
           la liste des choix retournée ne doit pas contenir les choix déjà
           contenus dans liste_courante.
           L'argument d'entrée into_courant, s'il est différent de None, donne
           la liste des choix proposés par d'autres validateurs. Dans ce cas,
           la méthode getInto doit calculer la liste des choix à retourner
           en se limitant à cette liste initiale. Par exemple, si into_courant
           vaut (1,2,3) et que le validateur propose la liste de choix (3,4,5),
           la méthode ne doit retourner que (3,).

           La méthode getInto peut retourner une liste vide [], ce qui veut
           dire qu'il n'y a pas (ou plus) de choix possible. Cette situation
           peut etre normale : l''utilisateur a utilisé tous les choix, ou
           résulter d'une incohérence des validateurs :
           choix parmi (1,2,3) ET choix parmi (4,5,6). Il est impossible de
           faire la différence entre ces deux situations.
        """
        return into_courant


class ListVal(Valid):

    """
        Cette classe sert de classe mère pour tous les validateurs qui acceptent
        des listes.
    """

    def isList(self):
        return 1

    def getInto(self, liste_courante=None, into_courant=None):
        """
           Cette méthode getInto effectue un traitement général qui consiste
           a filtrer la liste de choix into_courant, si elle existe, en ne
           conservant que les valeurs valides (appel de la méthode valid).
        """
        if into_courant is None:
            return None
        else:
            liste_choix = []
            for e in into_courant:
                if self.verif(e):
                    liste_choix.append(e)
            return liste_choix

    def convert(self, valeur):
        """
           Méthode convert pour les validateurs de listes. Cette méthode
           fait appel à la méthode convertItem sur chaque élément de la
           liste.
        """
        if isSequence(valeur):
            for val in valeur:
                self.convertItem(val)
            return valeur
        else:
            return self.convertItem(valeur)

    def verif(self, valeur):
        """
           Méthode verif pour les validateurs de listes. Cette méthode
           fait appel à la méthode verifItem sur chaque élément de la
           liste. Si valeur est un paramètre, on utilise sa valeur effective
           valeur.valeur.
        """
        if isSequence(valeur):
            for val in valeur:
                if not self.verifItem(val):
                    return 0
            return 1
        else:
            return self.verifItem(valeur)


class Compulsory(ListVal):
    """
        Validateur operationnel
        Verification de la présence obligatoire d'un élément dans une liste
    """
    registry = {}

    def __init__(self, elem=()):
        if not isSequence(elem):
            elem = (elem,)
        Valid.__init__(self, elem=elem)
        self.elem = elem
        self.cata_info = ""

    def info(self):
        return (tr(u"valeur %s obligatoire") % self.elem)

    def default(self, valeur, elem):
        return valeur

    def verifItem(self, valeur):
        return 1

    def convert(self, valeur):
        elem = list(self.elem)
        for val in valeur:
            v = self.adapt(val)
            if v in elem:
                elem.remove(v)
        if elem:
            raise ValError(
                tr("%s ne contient pas les elements obligatoires : %s ") % (valeur, elem))
        return valeur

    def hasInto(self):
        return 1

    def verif(self, valeur):
        if not isSequence(valeur):
            liste = list(valeur)
        else:
            liste = valeur
        for val in self.elem:
            if val not in liste:
                return 0
        return 1

    def infoErreurItem(self):
        return tr("La valeur n'est pas dans la liste des choix possibles")


class Together(ListVal):
    """
        Validateur operationnel
        si un des éléments est présent les autres doivent aussi l'être
    """
    registry = {}

    def __init__(self, elem=()):
        if not isSequence(elem):
            elem = (elem,)
        Valid.__init__(self, elem=elem)
        self.elem = elem
        self.cata_info = ""

    def info(self):
        return (tr("%s present ensemble") % self.elem)

    def default(self, valeur, elem):
        return valeur

    def verifItem(self, valeur):
        return 1

    def convert(self, valeur):
        elem = list(self.elem)
        for val in valeur:
            v = self.adapt(val)
            if v in elem: elem.remove(v)
        if ( len(elem) == 0 ): return valeur
        if len(elem) != len(list(self.elem)) :
            raise ValError(tr("%s ne contient pas les elements devant etre presents ensemble: %s ") %( valeur, elem))
        return valeur

    def hasInto(self):
        return 1

    def verif(self, valeur):
        if not isSequence(valeur):
            liste = list(valeur)
        else:
            liste = valeur
        compte = 0
        for val in self.elem:
            if val in liste: compte += 1
        if ( compte == 0 ): return 1
        if ( compte != len( list(self.elem) ) ): return 0
        return 1

    def infoErreurItem(self):
        return tr("La valeur n'est pas dans la liste des choix possibles")


class Absent(ListVal):
    """
        Validateur operationnel
        si un des éléments est présent non valide
    """
    registry = {}

    def __init__(self, elem=()):
        if not isSequence(elem):
            elem = (elem,)
        Valid.__init__(self, elem=elem)
        self.elem = elem
        self.cata_info = ""

    def info(self):
        return (tr("%s absent") % self.elem)

    def default(self, valeur, elem):
        return valeur

    def verifItem(self, valeur):
        return 1

    def convert(self, valeur):
        elem = list(self.elem)
        for val in valeur:
            v = self.adapt(val)
            if v in elem:
                raise ValError(tr("%s n'est pas autorise : %s ")% (v, elem))
        return valeur

    def hasInto(self):
        return 1

    def verif(self, valeur):
        if not isSequence(valeur):
            liste = list(valeur)
        else:
            liste = valeur
        for val in self.elem:
            if val in liste: return 0
        return 1

    def infoErreurItem(self):
        return tr("La valeur n'est pas dans la liste des choix possibles")


class NoRepeat(ListVal):
    """
        Validateur operationnel
        Verification d'absence de doublons dans la liste.
    """
    def __init__(self):
        Valid.__init__(self)
        self.cata_info = ""

    def info(self):
        return tr("Pas de doublon dans la liste")

    def infoErreurListe(self):
        return tr("Les doublons ne sont pas permis")

    def default(self, valeur):
        if valeur in self.liste:
            raise ValError( tr("%s est un doublon") % valeur)
        return valeur

    def convert(self, valeur):
        self.liste = []
        for val in valeur:
            v = self.adapt(val)
            self.liste.append(v)
        return valeur

    def verifItem(self, valeur):
        return 1

    def verif(self, valeur):
        if isSequence(valeur):
            liste = list(valeur)
            for val in liste:
                if liste.count(val) != 1:
                    return 0
            return 1
        else:
            return 1

    def getInto(self, liste_courante=None, into_courant=None):
        """
        Methode getInto spécifique pour validateur NoRepeat, on retourne
        une liste de choix qui ne contient aucune valeur de into_courant
        déjà contenue dans liste_courante
        """
        if into_courant is None:
            liste_choix = None
        else:
            liste_choix = []
            for e in into_courant:
                if e in liste_choix:
                    continue
                if liste_courante is not None and e in liste_courante:
                    continue
                liste_choix.append(e)
        return liste_choix


class LongStr(ListVal):

    """
        Validateur operationnel
        Verification de la longueur d une chaine
    """

    def __init__(self, low, high):
        ListVal.__init__(self, low=low, high=high)
        self.low = low
        self.high = high
        self.cata_info = ""

    def info(self):
        return (tr("longueur de la chaine entre %s et %s") %( self.low, self.high))

    def infoErreurItem(self):
        return tr("Longueur de la chaine incorrecte")

    def convert(self, valeur):
        for val in valeur:
            v = self.adapt(val)
        return valeur

    def verifItem(self, valeur):
        try:
            self.adapt(valeur)
            return 1
        except:
            return 0

    def default(self, valeur, low, high):
        if not isStr(valeur):
            raise ValError ("%s n'est pas une chaine" % repr(valeur))
        if valeur[0] == "'" and valeur[-1] == "'":
            low = low + 2
            high = high + 2
        if len(valeur) < low or len(valeur) > high:
            raise ValError(
                "%s n'est pas de la bonne longueur" % repr(valeur))
        return valeur


class OnlyStr(ListVal):

    """
        Validateur operationnel
        Valide que c'est une chaine
    """

    def __init__(self):
        ListVal.__init__(self)
        self.cata_info = ""

    def info(self):
        return tr("regarde si c'est une chaine")

    def infoErreurItem(self):
        return tr("Ce n'est pas une chaine")

    def convert(self, valeur):
        for val in valeur:
            v = self.adapt(val)
        return valeur

    def verifItem(self, valeur):
        try:
            self.adapt(valeur)
            return 1
        except:
            return 0

    def default(self, valeur):
        if not isStr(valeur):
            raise ValError (tr("%s n'est pas une chaine") % repr(valeur))
        return valeur


class OrdList(ListVal):

    """
        Validateur operationnel
        Verification qu'une liste est croissante ou decroissante
    """

    def __init__(self, ord):
        ListVal.__init__(self, ord=ord)
        self.ord = ord
        self.cata_info = ""

    def info(self):
        return ("liste %s" % self.ord)

    def infoErreurListe(self):
        return (tr("La liste doit etre en ordre %s") % self.ord)

    def convert(self, valeur):
        self.val = None
        self.liste = valeur
        for v in valeur:
            self.adapt(v)
        return valeur

    def default(self, valeur, ord):
        if self.ord == 'croissant':
            if self.val is not None and valeur < self.val:
                raise ValError(
                    (tr("%s n'est pas par valeurs croissantes") % repr(self.liste)))
        elif self.ord == 'decroissant':
            if self.val is not None and valeur > self.val:
                raise ValError(
                    (tr("%s n'est pas par valeurs decroissantes") % repr(self.liste)))
        self.val = valeur
        return valeur

    def verifItem(self, valeur):
        return 1

    def getInto(self, liste_courante=None, into_courant=None):
        """
        Methode getInto spécifique pour validateur OrdList, on retourne
        une liste de choix qui ne contient aucune valeur de into_courant
        dont la valeur est inférieure à la dernière valeur de
        liste_courante, si elle est différente de None.
        """
        if into_courant is None:
            return None
        elif not liste_courante:
            return into_courant
        else:
            liste_choix = []
            last_val = liste_choix[-1]
            for e in into_courant:
                if self.ord == 'croissant' and e <= last_val:
                    continue
                if self.ord == 'decroissant' and e >= last_val:
                    continue
                liste_choix.append(e)
            return liste_choix


class OrVal(Valid):

    """
        Validateur operationnel
        Cette classe est un validateur qui controle une liste de validateurs
        Elle verifie qu'au moins un des validateurs de la liste valide la valeur
    """

    def __init__(self, validators=()):
        if not isSequence(validators):
            validators = (validators,)
        self.validators = []
        for validator in validators:
            if type(validator) == types.FunctionType:
                self.validators.append(FunctionVal(validator))
            else:
                self.validators.append(validator)
        self.cata_info = ""

    def info(self):
        return "\n ou ".join([v.info() for v in self.validators])

    def convert(self, valeur):
        for validator in self.validators:
            try:
                return validator.convert(valeur)
            except:
                pass
        raise ValError(tr("%s n'est pas du bon type")% repr(valeur))

    def infoErreurItem(self):
        l = []
        for v in self.validators:
            err = v.infoErreurItem()
            if err != " ":
                l.append(err)
        chaine = " \n ou ".join(l)
        return chaine

    def infoErreurListe(self):
        l = []
        for v in self.validators:
            err = v.infoErreurListe()
            if err != " ":
                l.append(err)
        chaine = " \n ou ".join(l)
        return chaine

    def isList(self):
        """
           Si plusieurs validateurs sont reliés par un OU
           il suffit qu'un seul des validateurs attende une liste
           pour qu'on considère que leur union attend une liste.
        """
        for validator in self.validators:
            v = validator.isList()
            if v:
                return 1
        return 0

    def verif(self, valeur):
        for validator in self.validators:
            v = validator.verif(valeur)
            if v:
                return 1
        return 0

    def verifItem(self, valeur):
        for validator in self.validators:
            v = validator.verifItem(valeur)
            if v:
                return 1
        return 0

    def verifCata(self):
        infos = []
        for validator in self.validators:
            v = validator.verifCata()
            if not v:
                infos.append(validator.cata_info)
        if infos:
            self.cata_info = "\n".join(infos)
            return 0
        self.cata_info = ""
        return 1

    def hasInto(self):
        """
        Dans le cas ou plusieurs validateurs sont reliés par un OU
        il faut que tous les validateurs proposent un choix pour
        qu'on considère que leur union propose un choix.
        Exemple : Enum(1,2,3) OU entier pair, ne propose pas de choix
        En revanche, Enum(1,2,3) OU Enum(4,5,6) propose un choix (1,2,3,4,5,6)
        """
        for validator in self.validators:
            v = validator.hasInto()
            if not v:
                return 0
        return 1

    def getInto(self, liste_courante=None, into_courant=None):
        """
        Dans le cas ou plusieurs validateurs sont reliés par un OU
        tous les validateurs doivent proposer un choix pour
        qu'on considère que leur union propose un choix. Tous les choix
        proposés par les validateurs sont réunis (opérateur d'union).
        Exemple : Enum(1,2,3) OU entier pair, ne propose pas de choix
        En revanche, Enum(1,2,3) OU Enum(4,5,6) propose un
        choix (1,2,3,4,5,6)
        """
        validator_into = []
        for validator in self.validators:
            v_into = validator.getInto(liste_courante, into_courant)
            if v_into is None:
                return v_into
            validator_into.extend(v_into)
        return validator_into

    def valideListePartielle(self, liste_courante=None):
        """
         Méthode de validation de liste partielle pour le validateur Or.
         Si un des validateurs gérés par le validateur Or considère la
         liste comme valide, le validateur Or la considère comme valide.
        """
        for validator in self.validators:
            v = validator.valideListePartielle(liste_courante)
            if v:
                return 1
        return 0


class AndVal(Valid):

    """
        Validateur operationnel
        Cette classe est un validateur qui controle une liste de validateurs
        Elle verifie que tous les validateurs de la liste valident la valeur
    """

    def __init__(self, validators=()):
        if not isSequence(validators):
            validators = (validators,)
        self.validators = []
        for validator in validators:
            if type(validator) == types.FunctionType:
                self.validators.append(FunctionVal(validator))
            else:
                self.validators.append(validator)
            if hasattr(validator, 'fonctions'):
                for fonction in validator.fonctions:
                    f = getattr(validator, fonction)
                    setattr(self, fonction, f)
        self.cata_info = ""

    def info(self):
        return "\n et ".join([v.info() for v in self.validators])

    def convert(self, valeur):
        for validator in self.validators:
            valeur = validator.convert(valeur)
        return valeur

    def infoErreurItem(self):
        chaine = ""
        a = 1
        for v in self.validators:
            if v.infoErreurItem() != " ":
                if a == 1:
                    chaine = v.infoErreurItem()
                    a = 0
                else:
                    chaine = chaine + " \n et " + v.infoErreurItem()
        return chaine

    def infoErreurListe(self):
        chaine=""
        a = 1
        for v in self.validators:
            if v.infoErreurListe() != " ":
                if a == 1:
                    chaine = v.infoErreurListe()
                    a = 0
                else:
                    chaine = chaine + " \n et " + v.infoErreurListe()
        return chaine

    def verif(self, valeur):
        for validator in self.validators:
            v = validator.verif(valeur)
            if not v:
                self.local_info = validator.info()
                return 0
        return 1

    def verifItem(self, valeur):
        for validator in self.validators:
            v = validator.verifItem(valeur)
            if not v:
                # L'info n'est probablement pas la meme que pour verif ???
                self.local_info = validator.info()
                return 0
        return 1

    def verifCata(self):
        infos = []
        for validator in self.validators:
            v = validator.verifCata()
            if not v:
                infos.append(validator.cata_info)
        if infos:
            self.cata_info = "\n".join(infos)
            return 0
        self.cata_info = ""
        return 1

    def valideListePartielle(self, liste_courante=None):
        """
         Méthode de validation de liste partielle pour le validateur And.
         Tous les validateurs gérés par le validateur And doivent considérer
         la liste comme valide, pour que le validateur And la considère
         comme valide.
        """
        for validator in self.validators:
            v = validator.valideListePartielle(liste_courante)
            if not v:
                return 0
        return 1

    def isList(self):
        """
        Si plusieurs validateurs sont reliés par un ET
        il faut que tous les validateurs attendent une liste
        pour qu'on considère que leur intersection attende une liste.
        Exemple Range(2,5) ET Card(1) n'attend pas une liste
        Range(2,5) ET Pair attend une liste
        """
        for validator in self.validators:
            v = validator.isList()
            if v == 0:
                return 0
        return 1

    def hasInto(self):
        """
        Dans le cas ou plusieurs validateurs sont reliés par un ET
        il suffit qu'un seul validateur propose un choix pour
        qu'on considère que leur intersection propose un choix.
        Exemple : Enum(1,2,3) ET entier pair, propose un choix
        En revanche, entier pair ET superieur à 10 ne propose pas de choix
        """
        for validator in self.validators:
            v = validator.hasInto()
            if v:
                return 1
        return 0

    def getInto(self, liste_courante=None, into_courant=None):
        """
        Dans le cas ou plusieurs validateurs sont reliés par un ET
        il suffit qu'un seul validateur propose un choix pour
        qu'on considère que leur intersection propose un choix. Tous les
        choix proposés par les validateurs sont croisés (opérateur
        d'intersection)
        Exemple : Enum(1,2,3) ET entier pair, propose un choix (2,)
        En revanche, Enum(1,2,3) ET Enum(4,5,6) ne propose pas de choix.
        """
        for validator in self.validators:
            into_courant = validator.getInto(liste_courante, into_courant)
            if into_courant in ([], None):
                break
        return into_courant


def do_liste(validators):
    """
       Convertit une arborescence de validateurs en OrVal ou AndVal
       validators est une liste de validateurs ou de listes ou de tuples
    """
    valids = []
    for validator in validators:
        if type(validator) == types.FunctionType:
            valids.append(FunctionVal(validator))
        elif type(validator) is tuple:
            valids.append(OrVal(do_liste(validator)))
        elif type(validator) is list:
            valids.append(AndVal(do_liste(validator)))
        else:
            valids.append(validator)
    return valids


def validatorFactory(validator):
    if type(validator) == types.FunctionType:
        return FunctionVal(validator)
    elif type(validator) is tuple:
        return OrVal(do_liste(validator))
    elif type(validator) is list:
        return AndVal(do_liste(validator))
    else:
        return validator

# Ci-dessous : exemples de validateur (peu testés)


class RangeVal(ListVal):

    """
        Exemple de classe validateur : verification qu'une valeur
        est dans un intervalle.
        Pour une liste on verifie que tous les elements sont
        dans l'intervalle
        Susceptible de remplacer les attributs "vale_min" "vale_max"
        dans les catalogues
    """

    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.cata_info = (tr("%s doit etre inferieur a %s") % (low, high))

    def info(self):
        return (tr("valeur dans l'intervalle %s , %s") %( self.low, self.high))

    def convertItem(self, valeur):
        if valeur > self.low and valeur < self.high:
            return valeur
        raise ValError(tr("%s devrait etre comprise entre %s et %s") % (valeur, self.low, self.high))

    def verifItem(self, valeur):
        return valeur > self.low and valeur < self.high

    def infoErreurItem(self):
        return (tr("la valeur %s doit etre comprise entre %s et %s") % (valeur, self.low, self.high))


    def verifCata(self):
        if self.low > self.high:
            return 0
        return 1


class CardVal(Valid):

    """
        Exemple de classe validateur : verification qu'une liste est
        d'une longueur superieur a un minimum (min) et inferieure
        a un maximum (max).
        Susceptible de remplacer les attributs "min" "max" dans les
        catalogues
    """

    def __init__(self, min=float('-inf'), max=float('inf')):
        self.min = min
        self.max = max
        self.cata_info = (tr("%s doit etre inferieur a %s") %(min, max))

    def info(self):
        return (tr("longueur de liste comprise entre  %s et %s") %(self.min, self.max))

    def infoErreurListe(self):
        return (tr("Le cardinal de la liste doit etre compris entre %s et %s") % (self.min, self.max))

    def isList(self):
        return self.max == '**' or self.max > 1

    def getInto(self, liste_courante=None, into_courant=None):
        if into_courant is None:
            return None
        elif liste_courante is None:
            return into_courant
        elif self.max == '**':
            return into_courant
        elif len(liste_courante) < self.max:
            return into_courant
        else:
            return []

    def convert(self, valeur):
        if isSequence(valeur):
            l = len(valeur)
        elif valeur is None:
            l = 0
        else:
            l = 1
        if self.max != '**' and l > self.max:
            raise ValError(
                tr("%s devrait etre de longueur inferieure a %s") % (valeur, self.max))
        if self.min != '**' and l < self.min:
            raise ValError(
                tr("%s devrait etre de longueur superieure a %s") % (valeur, self.min))
        return valeur

    def verifItem(self, valeur):
        return 1

    def verif(self, valeur):
        if isSequence(valeur):
            if self.max != '**' and len(valeur) > self.max:
                return 0
            if self.min != '**' and len(valeur) < self.min:
                return 0
            return 1
        else:
            if self.max != '**' and 1 > self.max:
                return 0
            if self.min != '**' and 1 < self.min:
                return 0
            return 1

    def verifCata(self):
        if self.min != '**' and self.max != '**' and self.min > self.max:
            return 0
        return 1

    def valideListePartielle(self, liste_courante=None):
        validite = 1
        if liste_courante != None:
            if len(liste_courante) > self.max:
                validite = 0
        return validite


class PairVal(ListVal):

    """
        Exemple de classe validateur : verification qu'une valeur
        est paire.
        Pour une liste on verifie que tous les elements sont
        pairs
    """

    def __init__(self):
        ListVal.__init__(self)
        self.cata_info = ""

    def info(self):
        return _(u"valeur paire")

    def infoErreurItem(self):
        return tr("La valeur saisie doit etre paire")

    def convert(self, valeur):
        for val in valeur:
            v = self.adapt(val)
            if v % 2 != 0:
                raise ValError(
                    tr("%s contient des valeurs non paires") % repr(valeur))
        return valeur

    def default(self, valeur):
        return valeur

    def verifItem(self, valeur):
        if type(valeur) not in six.integer_types:
            return 0
        return valeur % 2 == 0

    def verif(self, valeur):
        if isSequence(valeur):
            for val in valeur:
                if val % 2 != 0:
                    return 0
            return 1
        else:
            if valeur % 2 != 0:
                return 0
            return 1


class EnumVal(ListVal):

    """
        Exemple de classe validateur : verification qu'une valeur
        est prise dans une liste de valeurs.
        Susceptible de remplacer l attribut "into" dans les catalogues
    """

    def __init__(self, into=()):
        if not isSequence(into):
            into = (into,)
        self.into = into
        self.cata_info = ""

    def info(self):
        return ("valeur dans %s" % self.into)

    def convertItem(self, valeur):
        if valeur in self.into:
            return valeur
        raise ValError(
            tr("%s contient des valeurs hors des choix possibles: %s ") % (valeur, self.into))

    def verifItem(self, valeur):
        if valeur not in self.into:
            return 0
        return 1

    def hasInto(self):
        return 1

    def getInto(self, liste_courante=None, into_courant=None):
        if into_courant is None:
            liste_choix = list(self.into)
        else:
            liste_choix = []
            for e in into_courant:
                if e in self.into:
                    liste_choix.append(e)
        return liste_choix

    def infoErreurItem(self):
        return tr("La valeur n'est pas dans la liste des choix possibles")


def ImpairVal(valeur):
    """
          Exemple de validateur
        Cette fonction est un validateur. Elle verifie que la valeur passee
        est bien un nombre impair.
    """
    if isSequence(valeur):
        for val in valeur:
            if val % 2 != 1:
                return 0
        return 1
    else:
        if valeur % 2 != 1:
            return 0
        return 1

ImpairVal.info = "valeur impaire"


class F1Val(Valid):

    """
        Exemple de validateur
        Cette classe est un validateur de dictionnaire (mot cle facteur ?). Elle verifie
        que la somme des cles A et B vaut une valeur donnee
        en parametre du validateur
    """

    def __init__(self, somme=10):
        self.somme = somme
        self.cata_info = ""

    def info(self):
        return (tr("valeur %s pour la somme des cles A et B ") % self.somme)

    def verif(self, valeur):
        if isSequence(valeur):
            for val in valeur:
                if not "A" in val:
                    return 0
                if not "B" in val:
                    return 0
                if val["A"] + val["B"] != self.somme:
                    return 0
            return 1
        else:
            if not "A" in valeur:
                return 0
            if not "B" in valeur:
                return 0
            if valeur["A"] + valeur["B"] != self.somme:
                return 0
            return 1


class FunctionVal(Valid):

    """
        Exemple de validateur
        Cette classe est un validateur qui est initialise avec une fonction
    """

    def __init__(self, function):
        self.function = function

    def info(self):
        return self.function.info

    def infoErreurItem(self):
        return self.function.info

    def verif(self, valeur):
        return self.function(valeur)

    def verifItem(self, valeur):
        return self.function(valeur)

    def convert(self, valeur):
        return valeur

# MC ca ne devrait plus servir !
# PN : commenter le 22.11.19
#CoercableFuncs = {int:     int,
#                  int:    int,
#                  float:   float,
#                  complex: complex,
#                  str: six.text_type}



class TypeVal(ListVal):

    """
        Exemple de validateur
        Cette classe est un validateur qui controle qu'une valeur
        est bien du type Python attendu.
        Pour une liste on verifie que tous les elements sont du bon type.
        Semblable a InstanceVal mais ici on fait le test par tentative de conversion
        alors qu'avec InstanceVal on ne teste que si isinstance est vrai.
    """

    def __init__(self, aType):
        # Si aType n'est pas un type, on le retrouve a l'aide de la fonction type
        # type(1) == int;type(0.2)==float;etc.
        if type(aType) != type:
            aType = type(aType)
        self.aType = aType
        try:
            self.coerce = CoercableFuncs[aType]
        except:
            self.coerce = self.identity

    def info(self):
        return (tr("valeur de %s") % self.aType)

    def identity(self, value):
        if type(value) == self.aType:
            return value
        raise ValError

    def convertItem(self, valeur):
        return self.coerce(valeur)

    def verifItem(self, valeur):
        try:
            self.coerce(valeur)
        except:
            return 0
        return 1


class InstanceVal(ListVal):

    """
        Exemple de validateur
        Cette classe est un validateur qui controle qu'une valeur est
        bien une instance (au sens Python) d'une classe
        Pour une liste on verifie chaque element de la liste
    """

    def __init__(self, aClass):
        # Si aClass est une classe on la memorise dans self.aClass
        # sinon c'est une instance dont on memorise la classe
        #if type(aClass) == types.InstanceType:
        if type(aClass) == object :
            # instance ancienne mode
            aClass = aClass.__class__
        elif type(aClass) == type:
            # classe ancienne mode
            aClass = aClass
        elif type(aClass) == type:
            # classe nouvelle mode
            aClass = aClass
        elif isinstance(aClass, object):
            # instance nouvelle mode
            aClass = type(aClass)
        else:
            raise ValError(tr("type non supporté"))

        self.aClass = aClass

    def info(self):
        return (tr("valeur d'instance de %s") % self.aClass.__name__)

    def verifItem(self, valeur):
        if not isinstance(valeur, self.aClass):
            return 0
        return 1


class VerifTypeTuple(ListVal):

    def __init__(self, typeDesTuples):
        self.typeDesTuples = typeDesTuples
        Valid.__init__(self)
        self.cata_info = ""

    def info(self):
        return tr(": verifie les \ntypes dans un tuple")

    def infoErreurListe(self):
        return tr("Les types entres ne sont pas permis")

    def default(self, valeur):
        return valeur

    def isList(self):
        return 1

    def convertItem(self, valeur):
        if len(valeur) != len(self.typeDesTuples):
            raise ValError(
                tr("%s devrait etre de type  %s ") %( valeur, self.typeDesTuples))
        for i in range(len(valeur)):
            ok = self.verifType(valeur[i], self.typeDesTuples[i])
            if ok != 1:
                raise ValError(
                    tr("%s devrait etre de type  %s ") % (valeur, self.typeDesTuples))
        return valeur

    def verifItem(self, valeur):
        try:
            if len(valeur) != len(self.typeDesTuples):
                return 0
            for i in range(len(valeur)):
                ok = self.verifType(valeur[i], self.typeDesTuples[i])
                if ok != 1:
                    return 0
        except:
            return 0
        return 1

    def verifType(self, valeur, type_permis):
        if type_permis == 'R':
            if type(valeur) in (int, float, int):
                return 1
        elif type_permis == 'I':
            if type(valeur) in (int, int):
                return 1
        elif type_permis == 'C':
            if self.isComplexe(valeur):
                return 1
        elif type_permis == 'TXM':
            if type(valeur) == bytes or type(valeur) == str:
                return 1
        elif isinstance(valeur, type_permis):
            return 1
        return 0

    def verif(self, valeur):
        if type(valeur) in (list, tuple):
            liste = list(valeur)
            for val in liste:
                if self.verifItem(val) != 1:
                    return 0
            return 1


class VerifExiste(ListVal):

    """
       fonctionne avec into
       Met une liste à jour selon les mot clefs existant
       exemple si into = ("A","B","C")
       si au niveau N du JDC les objets "A" et "C" existe
       alors la liste des into deviendra ( "A","C")

       niveauVerif est le niveau du JDC dans lequel va s effectuer la verification
       niveauVerif est defini par rapport au Noeud :
       exemple niveauVerif = 1 : on verifie les freres
               niveauVerif = 2 : on verifie les oncles..
    """

    def __init__(self, niveauVerif):
        ListVal.__init__(self)
        self.niveauVerif = niveauVerif
        self.MCSimp = None
        self.listeDesFreres = ()
        self.fonctions = ('verifieListe', 'set_MCSimp')

    def isList(self):
        return 1

    def verifieListe(self, liste):
        self.set_MCSimp(self.MCSimp)
        for item in liste:
            if not(item in self.listeDesFreres):
                return 0
        return 1

    def verifItem(self, valeur):
        self.set_MCSimp(self.MCSimp)
        if valeur in self.listeDesFreres:
            return 1
        return 0

    def set_MCSimp(self, MCSimp):
        self.MCSimp = MCSimp
        k = self.niveauVerif
        mc = MCSimp
        while (k != 0):
            parent = mc.parent
            mc = parent
            k = k - 1
        # on met la liste à jour
        parent.forceRecalcul = self.niveauVerif
        self.listeDesFreres = parent.listeMcPresents()

    def convertItem(self, valeur):
        if valeur in self.listeDesFreres:
            return valeur
        raise ValError(
            tr("%s n'est pas dans %s") % (valeur, self.listeDesFreres))


class RegExpVal(ListVal):

    """
    Vérifie qu'une chaîne de caractère corresponde à l'expression régulière 'pattern'
    """

    errormsg = 'La chaîne "%(value)s" ne correspond pas au motif "%(pattern)s"'

    def __init__(self, pattern):
        self.pattern = pattern
        self.compiled_regexp = re.compile(pattern)

    def info(self):
        return tr('Une chaîne correspondant au motif ') + str(self.pattern) + tr(" est attendue")

    def infoErreurItem(self):
        return tr('Une chaîne correspondant au motif ') + str(self.pattern) + tr(" est attendue")

    def verifItem(self, valeur):
        if self.compiled_regexp.match(valeur):
            return 1
        else:
            return (0, self.errormsg % {"value": valeur, "pattern": self.pattern})

    def convertItem(self, valeur):
        if self.compiled_regexp.match(valeur):
            return valeur
        else:
            raise ValError(self.errormsg %
                           {"value": valeur, "pattern": self.pattern})


class FileExtVal(RegExpVal):

    """
    Vérifie qu'une chaîne de caractère soit un nom de fichier valide avec l'extension 'ext'
    """

    def __init__(self, ext):
        self.ext = ext
        self.errormsg = '"%%(value)s" n\'est pas un nom de fichier %(ext)s valide' % {
            "ext": ext}
        #PNPN Modif pour Adao
        RegExpVal.__init__(self, "^\S+\.%s$" % self.ext)


    def info(self):
        return ('Un nom de fichier se terminant par ".%s" est attendu.' % self.ext)

    def infoErreurItem(self):
        return ('Un nom de fichier se terminant par ".%s" est attendu.' % self.ext)

class CreeMotClef(object):
    def __init__(self,MotClef ):
        self.MotClef=MotClef
        self.MCSimp=None

    def convert(self, lval):
        try : valeur=lval[0]
        except  : return lval

        parent= self.MCSimp.parent
        if hasattr(parent, 'inhibeValidator') and parent.inhibeValidator: return lval


        if parent.getChild(self.MotClef) == None : longueur=0
        else : longueur=len(parent.getChild(self.MotClef))

        pos=parent.getIndexChild(self.MCSimp.nom)+1
        while longueur < valeur :
            parent.inhibeValidator=1
            parent.addEntite(self.MotClef,pos)
            pos=pos+1
            parent.inhibeValidator=0
            longueur=len(parent.getChild(self.MotClef))

        if longueur > valeur :
            parent.inhibeValide=1
            parentObj=parent.getChild(self.MotClef)
            obj=parent.getChild(self.MotClef)[-1]
            parentObj.suppEntite(obj)
            longueur=len(parent.getChild(self.MotClef))
            parent.inhibeValide=0
        return lval

    def info(self):
        return "Cree le bon nombre de Mot %s"  % self.MotClef

    def verifItem(self, valeur):
        return 1

    def set_MCSimp(self, MCSimp):
        #print "dans set_MCSimp"
        self.MCSimp=MCSimp
