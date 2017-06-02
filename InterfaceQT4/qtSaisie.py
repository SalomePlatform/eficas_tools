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
# Modules Python
from __future__ import absolute_import
try :
   from builtins import str
   from builtins import range
except : pass

import types,os
from Extensions.i18n import tr

from PyQt5.QtCore import Qt


# Import des panels

class SaisieValeur(object):
  """
  Classe contenant les methodes communes aux  panels
  permettant de choisir des valeurs 
  """
  def __init__(self):
       pass


  def LEValeurPressed(self,valeur=None):
         if not hasattr(self, 'inSaisieValeur' ) : self.inSaisieValeur=False
         if self.inSaisieValeur : return
         self.inSaisieValeur=True
         if valeur == None :
            try :
              nouvelleValeur=str(self.lineEditVal.text())
            except UnicodeEncodeError as e :
               self.editor.affiche_infos("pb d encoding", Qt.red)
               validite,commentaire=self.politique.RecordValeur(None)
               self.lineEditVal.setText('')
               self.setValide()
               self.inSaisieValeur=False
               return
         else :
            #PN PN PN ???? la 1 ligne est tres bizarre.
            try : 
              if hasattr(self,"lineEditVal"):self.lineEditVal.setText(tr(valeur.nom))
            except : 
              if hasattr(self,"lineEditVal"):self.lineEditVal.setText(valeur)
            nouvelleValeur=valeur
         if self.node.item.definition.validators != None :
          if self.node.item.definition.validators.verif_item(nouvelleValeur) !=1 :
                commentaire=self.node.item.definition.validators.info_erreur_item()
                self.editor.affiche_infos(commentaire,Qt.red)
                self.inSaisieValeur=False
                return
         nouvelleValeurFormat=self.politique.GetValeurTexte(nouvelleValeur)
         validite,commentaire=self.politique.RecordValeur(nouvelleValeurFormat)
         if commentaire != "" :
            #PNPNPNP Il faut trouver une solution pour les 2 cas 
            #   self.editor.affiche_infos(commentaire)
            #self.Commentaire.setText(tr(commentaire))
            if validite :
                self.editor.affiche_commentaire(commentaire)
            else :
                self.editor.affiche_infos(commentaire,Qt.red)
         self.inSaisieValeur=False
         self.setValide()


  #def TraiteLEValeurTuple(self,valeurBrute=None) :
  #      listeValeurs=[]
  #      if valeurBrute== None :valeurBrute=str(self.LEValeur.text())
  #      listeValeursSplit=valeurBrute.split(',')
  #      for val in listeValeursSplit :
  #          try :
  #             valeur=eval(val,{})        
  #          except :
  #             valeur=val
  #          listeValeurs.append(valeur)
  #      return listeValeurs

  def TraiteLEValeur(self,valeurTraitee=None) :
        # lit la chaine entree dans le line edit
        # et la tranforme en chaine de valeurs
        # a traiter. renvoie eventuellement des complexes
        listeValeurs=[]
        if valeurTraitee == None :
           valeurBrute=str(self.LEValeur.text())
        else :
           valeurBrute=valeurTraitee
        if valeurBrute == str("") : return listeValeurs,1

        try :
            valeur=eval(valeurBrute,{})        
        except :
            valeur=valeurBrute

        if type(valeur)  in (list,tuple) :
           if self.node.item.wait_complex() :
              indice = 0
              while (indice < len(valeur)):
                 v=valeur[indice]

                 if (v== 'RI' or v == 'MP'):
                    try :
                       t=tuple([v,valeur[indice+1],valeur[indice+2]])
                       listeValeurs.append(t)
                       indice=indice+3
                    except :
                       commentaire = tr("Veuillez entrer le complexe sous forme aster ou sous forme python")
                       self.editor.affiche_infos(commentaire)
                       return listeValeurs,0
                       

                 else :     # ce n'est pas un tuple a la mode aster
                    listeValeurs.append(v)
                    indice = indice + 1

           else:  # on n'attend pas un complexe
             listeValeurs=valeurBrute.split(',')

        elif type(valeur) == bytes:
             listeValeurs=valeur.split(',')
        else:
          #listeValeurs.append(valeurBrute)
          listeValeurs.append(valeur)

        return listeValeurs,1

class SaisieSDCO(object) :

  def LESDCOReturnPressed(self):
        """
           Lit le nom donne par l'utilisateur au concept de type CO qui doit être
           la valeur du MCS courant et stocke cette valeur
        """
        self.editor.init_modif()
        anc_val = self.node.item.get_valeur()
        if anc_val != None:
          # il faut egalement propager la destruction de l'ancien concept
          self.node.item.delete_valeur_co(valeur=anc_val)
          # et on force le recalcul des concepts de sortie de l'etape
          self.node.item.object.etape.get_type_produit(force=1)
          # et le recalcul du contexte
          self.node.item.object.etape.parent.reset_context()
        nomConcept = str(self.LESDCO.text())
        if nomConcept == "" : return

        test,commentaire=self.node.item.set_valeur_co(nomConcept)
        if test:
           commentaire=tr("Valeur du mot-clef enregistree")
           self.node.update_node_valid()
        else :
           cr = self.node.item.get_cr()
           commentaire = tr("Valeur du mot-clef non autorisee :")+cr.get_mess_fatal()
                                                                                         
