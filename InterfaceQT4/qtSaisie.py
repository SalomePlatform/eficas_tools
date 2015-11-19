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
import string,types,os
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr


# Import des panels

class SaisieValeur:
  """
  Classe contenant les méthodes communes aux  panels
  permettant de choisir des valeurs 
  """
  def __init__(self):
       pass


  def LEValeurPressed(self,valeur=None):
         if valeur == None :
            nouvelleValeur=str(self.lineEditVal.text())
         else :
            if hasattr(self,"lineEditVal"):self.lineEditVal.setText(QString(valeur.nom))
            nouvelleValeur=valeur
         nouvelleValeurFormat=self.politique.GetValeurTexte(nouvelleValeur)
         validite,commentaire=self.politique.RecordValeur(nouvelleValeurFormat)
         if commentaire != "" :
            #PNPNPNP Il faut trouver une solution pour les 2 cas 
            #   self.editor.affiche_infos(commentaire)
            #self.Commentaire.setText(QString(commentaire))
            if validite :
                self.editor.affiche_commentaire(commentaire)
            else :
                self.editor.affiche_infos(commentaire,Qt.red)
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

        if type(valeur)  in (types.ListType,types.TupleType) :
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

        elif type(valeur) == types.StringType:
             listeValeurs=valeur.split(',')
        else:
          listeValeurs.append(valeurBrute)

        return listeValeurs,1

class SaisieSDCO :

  def LESDCOReturnPressed(self):
        """
           Lit le nom donné par l'utilisateur au concept de type CO qui doit être
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
                                                                                         
