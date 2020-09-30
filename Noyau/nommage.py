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
   Ce module sert à nommer les concepts produits par les commandes.
   Le nom du concept est obtenu en appelant la fonction getNomConceptResultat
   du module avec le nom de la commande en argument.

   Cette fonction parcourt le source dans lequel la commande se trouve, parse le
   fichier et retrouve le nom du concept qui se trouve à gauche du signe = précédant
   le nom de la commande.

   Cette fonction utilise la fonction cur_frame du module N_utils qui retourne la frame
   d'exécution Python située 2 niveaux au-dessus. C'est à partir de cette frame que
   l'on retrouve le fichier source et le numéro de ligne où se trouve l'appel à la commande.

"""

# Modules Python
from __future__ import absolute_import
try :
   from builtins import str
except :
   pass
import re
import linecache
import sys
from functools import partial

# Modules EFICAS
from . import N_utils
from .strfunc import getEncoding

regex1 = '=?\s*%s\s*\('
# commentaire standard precede d'un nombre quelconque de blancs (pas
# multiligne)
pattern_comment = re.compile(r"^\s*#.*")


def _getNomConceptResultat(ope, level=2):
    """
       Cette fonction recherche dans la pile des appels, l'appel à la commande
       qui doit etre situé à 2 niveaux au-dessus (cur_frame(2)).
       On retrouve d'abord la frame d'exécution f. Puis le numéro de la ligne
       dans le source f.f_lineno et le nom du fichier source (f.f_code.co_filename).
       A partir de là, on récupère la ligne de source avec linecache.getline
       et on vérifie que cette ligne correspond véritablement à l'appel.

       En effet, lorsque les commandes tiennent sur plusieurs lignes, on retrouve
       la dernière ligne. Il faut donc remonter dans le source jusqu'à la première
       ligne.

       Enfin la fonction evalnom forme un nom acceptable lorsque le concept est un
       élément d'une liste, par exemple.

    """
    f = N_utils.cur_frame(level)
    lineno = f.f_lineno     # XXX Too bad if -O is used
    # lineno = f_lineno(f)  # Ne marche pas toujours
    co = f.f_code
    if sys.version_info >= (3,0) :
       filename = co.co_filename
    else : 
       import six
       filename = six.text_type(co.co_filename, getEncoding())
    name = co.co_name
    # pattern pour identifier le debut de la commande
    pattern_oper = re.compile(regex1 % ope)

    list = []
    while lineno > 0:
        line = linecache.getline(filename, lineno)
        lineno = lineno - 1
        if pattern_comment.match(line):
            continue
        list.append(line)
        if pattern_oper.search(line):
            l = pattern_oper.split(line)
            list.reverse()
            # On suppose que le concept resultat a bien ete
            # isole en tete de la ligne de source
            m = evalnom(l[0].strip(), f.f_locals)
            # print "NOMS ",m
            if m != []:
                return m[-1]
            else:
                return ''
    # print "appel inconnu"
    return ""


def evalnom(text, d):
    """
     Retourne un nom pour le concept resultat identifie par text
     Pour obtenir ce nom il y a plusieurs possibilites :
      1. text est un identificateur python c'est le nom du concept
      2. text est un element d'une liste on construit le nom en
        evaluant la partie indice dans le contexte de l'appelant d
    """
    l = re.split('([\[\]]+)', text)
    if l[-1] == '':
        l = l[:-1]
    lll = []
    i = 0
    while i < len(l):
        s = l[i]
        ll = re.split('[ ,]+', s)
        if ll[0] == '':
            ll = ll[1:]
        if len(ll) == 1:
            id0 = ll[0]
        else:
            lll = lll + ll[0:-1]
            id0 = ll[-1]
        if i + 1 < len(l) and l[i + 1] == '[':  # le nom est suivi d un subscript
            sub = l[i + 2]
            nom = id0 + '_' + str(eval(sub, d))
            i = i + 4
        else:
            nom = id0
            i = i + 1
        lll.append(nom)
    return lll


def f_lineno(f):
    """
       Calcule le numero de ligne courant
       Devrait marcher meme avec -O
       Semble ne pas marcher en présence de tuples longs
    """
    c = f.f_code
    if not hasattr(c, 'co_lnotab'):
        return f.f_lineno
    tab = c.co_lnotab
    line = c.co_firstlineno
    stopat = f.f_lasti
    addr = 0
    for i in range(0, len(tab), 2):
        addr = addr + ord(tab[i])
        if addr > stopat:
            break
        line = line + ord(tab[i + 1])
    return line


class NamingSystem(N_utils.Singleton):

    """Cette classe définit un système de nommage dynamique des concepts."""
    _singleton_id = 'nommage.NamingSystem'

    def __init__(self):
        """Initialisation"""
        self.native = _getNomConceptResultat
        self.useGlobalNaming()

    def useNamingFunction(self, function):
        """Utilise une fonction particulière de nommage."""
        self.naming_func = function

    def useGlobalNaming(self):
        """Utilise la fonction native de nommage."""
        self.naming_func = partial(self.native, level=3)

    def __call__(self, *args):
        """Appel à la fonction de nommage."""
        return self.naming_func(*args)

getNomConceptResultat = NamingSystem()
