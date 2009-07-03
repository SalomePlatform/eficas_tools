# -*- coding: utf-8 -*-
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
   Module de chargement des composants et de mapping des objets du noyau
   Accas vers les items d'EFICAS

     - composants : dictionnaire de stockage des relations entre types
       d'objet du noyau et types d'item
     - charger_composants() : fonction de chargement des composants. Retourne
       le dictionnaire composants.
     - gettreeitem(object) -> type d'item : fonction qui retourne un type
       d'item correspondant au type de l'objet noyau fourni.
     - make_objecttreeitem(appli,labeltext, object, setfunction=None) -> item : fonction qui retourne un item
       correspondant à l'objet noyau fourni.
"""
# import généraux
import os,glob,types

# Dictionnaire {object : item} permettant d'associer un item à un object
# Ce dictionnaire est renseigné par la méthode charger_composants 
composants = {}

def charger_composants(Ihm="TK"):
    """
        Cette fonction a pour but de charger tous les modules composants graphiques
        (fichiers compo*.py dans le même répertoire que ce module )
        et de remplir le dictionnaire composants utilisé par make_objecttreeitem
    """
    reper=os.path.dirname(__file__)
    if Ihm == "TK" :
       repertoire=reper+"/../InterfaceTK"
       package="InterfaceTK"
    else :
       repertoire=reper+"/../InterfaceQT4"
       package="InterfaceQT4"
       #repertoire=reper+"/../InterfaceQT"
       #package="InterfaceQT"
    listfich=glob.glob(os.path.join(repertoire, "compo*.py"))
    for fichier in listfich:
        m= os.path.basename(fichier)[:-3]
        module=__import__(package,globals(),locals(),[m])
        module = getattr(module, m)
        composants[module.objet]=module.treeitem
    return composants

def gettreeitem(object):
    """
      Cette fonction retourne la classe item associée à l'objet object.
      Cette classe item dépend bien sûr de la nature de object, d'où
      l'interrogation du dictionnaire composants
    """
    # Si la definition de l'objet a un attribut itemeditor, il indique 
    # la classe a utiliser pour l'item
    try:
       return object.definition.itemeditor
    except:
       pass

    # On cherche ensuite dans les composants (plugins)
    try:
       itemtype= composants[object.__class__]
       return itemtype
    except:
       pass

    # Puis une eventuelle classe heritee (aleatoire car sans ordre)
    for e in composants.keys():
        if e and isinstance(object,e):
           itemtype= composants[e]
           return itemtype

    # Si on n'a rien trouve dans les composants on utilise l'objet par defaut
    itemtype=composants[None]
    return itemtype

def make_objecttreeitem(appli,labeltext, object, setfunction=None):
    """
       Cette fonction permet de construire et de retourner un objet
       de type item associé à l'object passé en argument.
    """
    c = gettreeitem(object)
    return c(appli,labeltext, object, setfunction)

