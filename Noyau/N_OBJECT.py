# coding=utf-8
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


"""
    Ce module contient la classe OBJECT classe mère de tous les objets
    servant à controler les valeurs par rapport aux définitions
"""
from __future__ import absolute_import
try :
   from builtins import object
except :
   pass 
from .N_CR import CR


class OBJECT(object):

    """
       Classe OBJECT : cette classe est virtuelle et sert de classe mère
       aux classes de type ETAPE et MOCLES.
       Elle ne peut etre instanciée.
       Une sous classe doit obligatoirement implémenter les méthodes :

       - __init__

    """

    def get_etape(self):
        """
           Retourne l'étape à laquelle appartient self
           Un objet de la catégorie etape doit retourner self pour indiquer que
           l'étape a été trouvée
           XXX double emploi avec self.etape ???
        """
        if self.parent == None:
            return None
        return self.parent.get_etape()

    def supprime(self):
        """
           Méthode qui supprime les références arrières suffisantes pour
           que l'objet puisse etre correctement détruit par le
           garbage collector
        """
        self.parent = None
        self.etape = None
        self.jdc = None
        self.niveau = None

    def get_val(self):
        """
            Retourne la valeur de l'objet. Cette méthode fournit
            une valeur par defaut. Elle doit etre dérivée pour chaque
            type d'objet
        """
        return self

    def isBLOC(self):
        """
            Indique si l'objet est un BLOC
        """
        return 0

    def get_jdc_root(self):
        """
            Cette méthode doit retourner l'objet racine c'est à dire celui qui
            n'a pas de parent
        """
        if self.parent:
            return self.parent.get_jdc_root()
        else:
            return self

    def GETVAL(self, val):
        """
            Retourne la valeur effective du mot-clé en fonction
            de la valeur donnée. Defaut si val == None
        """
        if (val is None and hasattr(self.definition, 'defaut')):
            return self.definition.defaut
        else:
            return val

    def reparent(self, parent):
        """
           Cette methode sert a reinitialiser la parente de l'objet
        """
        self.parent = parent
        self.jdc = parent.jdc


class ErrorObj(OBJECT):

    """Classe pour objets errones : emule le comportement d'un objet tel mcsimp ou mcfact
    """

    def __init__(self, definition, valeur, parent, nom="err"):
        self.nom = nom
        self.definition = definition
        self.valeur = valeur
        self.parent = parent
        self.mc_liste = []
        if parent:
            self.jdc = self.parent.jdc
            # self.niveau = self.parent.niveau
            # self.etape = self.parent.etape
        else:
            # Pas de parent
            self.jdc = None
            # self.niveau = None
            # self.etape = None

    def isvalid(self, cr='non'):
        return 0

    def report(self):
        """ génère le rapport de validation de self """
        self.cr = CR()
        self.cr.debut = u"Mot-clé invalide : " + self.nom
        self.cr.fin = u"Fin Mot-clé invalide : " + self.nom
        self.cr.fatal(_(u"Type non autorisé pour le mot-clé %s : '%s'"),
                      self.nom, self.valeur)
        return self.cr
