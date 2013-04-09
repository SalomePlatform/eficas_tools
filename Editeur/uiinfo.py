# -*- coding: utf-8 -*-
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
   Ce module sert à construire les structures de données porteuses 
   des informations liées aux groupes de commandes
"""
import types

class UIINFO:
   """
       Pour le moment la classe UIINFO ne sait traiter que des infos
       portant sur la definition des groupes de commandes
       Les autres informations sont ignorées
   """
   def __init__(self,parent,groupes=None,**args):
      """
         Initialiseur de la classe UIINFO.
         Initialise a partir du dictionnaire UIinfo passé à
         un objet ENTITE les attributs de la classe
      """
      # L'attribut parent stocke le lien vers l'objet ENTITE relié à UIINFO
      self.parent=parent
      self.groupes=groupes
      if groupes == None:
         # L'entite n'a pas de groupe associé. On lui associe le groupe "DEFAUT"
         self.groupes=("DEFAUT",)
      if type(self.groupes) != types.TupleType:
         self.groupes=(self.groupes,)

def traite_commande(commande,niveau):
    """
        Cette fonction cree l'attribut UI de l'objet commande
        à partir des informations contenues dans UIinfo
    """
    uiinfo=commande.UIinfo or {}
    UI=UIINFO(commande,**uiinfo)
    commande.UI=UI
    #if "CACHE" in UI.groupes:
        # La commande est cachee aux utilisateurs
        #niveau.dict_groupes["CACHE"].append(commande.nom)
        #pass
    #else:
        # On ajoute la commande dans tous les groupes specifies
    for grp in UI.groupes:
        if not niveau.dict_groupes.has_key(grp): niveau.dict_groupes[grp]=[]
        niveau.dict_groupes[grp].append(commande.nom)

def traite_niveau(niveau):
   if niveau.l_niveaux == ():
       # Il n'y a pas de sous niveaux. niveau.entites ne contient que des commandes
       niveau.dict_groupes={}
       for oper in niveau.entites:
           traite_commande(oper,niveau)
       # A la fin les cles du dictionnaire dict_groupes donnent la liste des groupes
       # sans doublon
       niveau.liste_groupes=niveau.dict_groupes.keys()
       # On ordonne les listes alphabétiquement
       niveau.liste_groupes.sort()
       for v in niveau.dict_groupes.values():v.sort()
       #print niveau.liste_groupes
       #print niveau.dict_groupes
   else:
       for niv in niveau.l_niveaux:
           traite_niveau(niv)

def traite_UIinfo(cata):
   """
      Cette fonction parcourt la liste des commandes d'un catalogue (cata)
      construit les objets UIINFO à partir de l'attribut UIinfo de la commande
      et construit la liste complète de tous les groupes présents
   """
   #dict_groupes["CACHE"]=[]
   #XXX Ne doit pas marcher avec les niveaux
   if cata.JdC.l_niveaux == ():
       # Il n'y a pas de niveaux
       # On stocke la liste des groupes et leur contenu dans le JdC
       # dans les attributs liste_groupes et dict_groupes
       cata.JdC.dict_groupes={}
       for commande in cata.JdC.commandes:
           traite_commande(commande,cata.JdC)
       # A la fin les cles du dictionnaire dict_groupes donnent la liste des groupes
       # sans doublon
       cata.JdC.liste_groupes=cata.JdC.dict_groupes.keys()
       # On ordonne les listes alphabétiquement
       cata.JdC.liste_groupes.sort()
       for v in cata.JdC.dict_groupes.values():v.sort()
       #print cata.JdC.liste_groupes
       #print cata.JdC.dict_groupes
   else:
       # Le catalogue de commandes contient des définitions de niveau
       for niv in cata.JdC.l_niveaux:
          traite_niveau(niv)




