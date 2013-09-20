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
import types
from Extensions.i18n import tr


#------------------
class Validation  :
#------------------
  def __init__(self,node,parent) :
         self.node=node
         self.parent=parent

  def TesteUneValeur(self,valeurentree):
         commentaire = None
         valeur,validite=self.node.item.eval_valeur(valeurentree)
         if not validite :
                  commentaire = "impossible d'evaluer : %s " %`valeurentree`
                  return valeur,validite,commentaire

         testtype,commentaire = self.node.item.object.verif_type(valeur)
         if not testtype :
                  return valeur,0,commentaire

         valide=self.node.item.valide_item(valeur)
         if type(valide) == types.TupleType:
                 validite,commentaire=valide
         else :
                 validite=valide
                 commentaire=" "

         if not validite and commentaire is None:
                  commentaire = "impossible d'évaluer : %s " %`valeurentree`
         return valeur, validite, commentaire

# ----------------------------------------------------------------------------------------
#   Methodes utilisees pour la manipulation des items en notation scientifique
#   a mettre au point
# ----------------------------------------------------------------------------------------
  def SetValeurTexte(self,texteValeur) :
         try :
                  if "R" in self.node.item.object.definition.type:
                     if texteValeur[0] != "'":
                        clef=eval(texteValeur)
                        if str(clef) != str(texteValeur) :
                           self.node.item.object.init_modif()
                           clefobj=self.node.item.object.GetNomConcept()
                           if not self.parent.appliEficas.dict_reels.has_key(clefobj):
                              self.parent.appliEficas.dict_reels[clefobj] = {}
                           self.parent.appliEficas.dict_reels[clefobj][clef]=texteValeur
                           self.parent.appliEficas.dict_reels[clefobj]
                           if clefobj=="" : 
                              if not self.parent.appliEficas.dict_reels.has_key(self.node.item.object.etape) :
                                 self.parent.appliEficas.dict_reels[self.node.item.object.etape] = {}
                              self.parent.appliEficas.dict_reels[self.node.item.object.etape][clef]=texteValeur
                           self.node.item.object.fin_modif()
         except:
            pass

  def GetValeurTexte(self,valeur) :
         valeurTexte=valeur
         from decimal import Decimal
         if  isinstance(valeur,Decimal) :
             return valeur 
         if "R" in self.node.item.object.definition.type:
                  clefobj=self.node.item.object.GetNomConcept()
                  if self.parent.appliEficas.dict_reels.has_key(clefobj):
                     if self.parent.appliEficas.dict_reels[clefobj].has_key(valeur):
                        valeurTexte=self.parent.appliEficas.dict_reels[clefobj][valeur]
         return valeurTexte

  def AjoutDsDictReel(self,texteValeur):
         # le try except est necessaire pour saisir les parametres
         # on enleve l erreur de saisie 00 pour 0
         if str(texteValeur)== '00' : return
         try :
            if "R" in self.node.item.object.definition.type:
                if str(texteValeur)[0] != "'":
                   clef=eval(texteValeur)
                   if str(clef) != str(texteValeur) :
                      clefobj=self.node.item.object.GetNomConcept()
                      if not self.parent.appliEficas.dict_reels.has_key(clefobj):
                          self.parent.appliEficas.dict_reels[clefobj] = {}
                      self.parent.appliEficas.dict_reels[clefobj][clef]=texteValeur
                      if clefobj=="" : 
                         if not self.parent.appliEficas.dict_reels.has_key(self.node.item.object.etape) :
                            self.parent.appliEficas.dict_reels[self.node.item.object.etape] = {}
                         self.parent.appliEficas.dict_reels[self.node.item.object.etape][clef]=texteValeur
                          
         except:
          pass

  def AjoutDsDictReelEtape(self):
      try:
         if self.parent.appliEficas.dict_reels.has_key(self.node.item.object) :
            self.parent.appliEficas.dict_reels[self.node.item.sdnom]=self.parent.appliEficas.dict_reels[self.node.item.object]
            del self.parent.appliEficas.dict_reels[self.node.item.object]
      except :
         pass


#------------------------------------
class PolitiqueUnique(Validation) :
#------------------------------------
  """
  classe servant pour les entrees ne demandant qu un mot clef
  """
  def __init__(self,node,parent):
        Validation.__init__(self,node,parent)

  def RecordValeur(self,valeurentree):
         if self.parent.modified == 'n' : self.parent.init_modif()
         ancienne_val = self.node.item.get_valeur()
         valeur,validite,commentaire =self.TesteUneValeur(valeurentree)
         if validite :
            validite=self.node.item.set_valeur(valeur)
            if self.node.item.isvalid():
                  commentaire = tr("Valeur du mot-cle enregistree")
                  #commentaire = "Valeur du mot-cle enregistree"
                  self.SetValeurTexte(str(valeurentree))
            else:
                  cr = self.node.item.get_cr()
                  commentaire =  tr("Valeur du mot-cle non autorisee ")+cr.get_mess_fatal()
                  self.node.item.set_valeur(ancienne_val)
         return validite, commentaire 

 
#--------------------------------------
class PolitiquePlusieurs(Validation):
#--------------------------------------
  """
  classe servant pour les entrees ne demandant qu un mot clef
  """
  def __init__(self,node,parent) :
         self.node=node
         self.parent=parent


  def AjoutValeurs(self,listevaleur,index,listecourante):
         listeRetour=[]
         commentaire="Nouvelle valeur acceptée"
         commentaire2=""
         valide=1
         if listevaleur==None: return
         if listevaleur=="": return
         if not( type(listevaleur)  in (types.ListType,types.TupleType)) :
            listevaleur=tuple(listevaleur)
         # on verifie que la cardinalite max n a pas ete atteinte
         min,max = self.node.item.GetMinMax()
         if len(listecourante) + len(listevaleur) > max :
            commentaire="La liste atteint le nombre maximum d'elements : "+ str(max) +" ,ajout refuse"
            return False,commentaire,commentaire2,listeRetour

         for valeur in listevaleur :
             # On teste le type de la valeur
             valeurScientifique=valeur
             valide=self.node.item.valide_item(valeur)
             if not valide :
                try :
                   valeur,valide=self.node.item.eval_valeur(valeur)
                   valide,commentaire2 = self.node.item.object.verif_type(valeur)
                except :
                   #return testtype,commentaire,"",listeRetour
                   pass
             if not valide:
                if commentaire.find("On attend un chaine") > 1 :
                   commentaire="Valeur "+str(valeur)+ " incorrecte : ajout a la liste refuse: On attend une chaine de caracteres < 8"
                else :
                   commentaire="Valeur "+str(valeur)+ " incorrecte : ajout a la liste refuse"
                if commentaire2== "" :commentaire2=self.node.item.info_erreur_item()
                return valide,commentaire,commentaire2,listeRetour

             # On valide la liste obtenue
             encorevalide=self.node.item.valide_liste_partielle(valeur,listecourante)
             #print encorevalide
             if not encorevalide :
                commentaire2=self.node.item.info_erreur_liste()
                # On traite le cas ou la liste n est pas valide pour un pb de cardinalite
                min,max = self.node.item.GetMinMax()
                if len(listecourante) + 1 >= max :
                   commentaire="La liste atteint le nombre maximum d'elements : "+ str(max) +" ,ajout refuse"
                   return valide,commentaire,commentaire2,listeRetour
                if len(listecourante) + 1 > min :
                   commentaire=""
                   return valide,commentaire,commentaire2,listeRetour
             # On ajoute la valeur testee a la liste courante et a la liste acceptee
             self.AjoutDsDictReel(valeurScientifique)
             listecourante.insert(index,valeur)
             index=index+1
             listeRetour.append(valeur)

         return valide,commentaire,commentaire2,listeRetour

  def AjoutTuple(self,valeurTuple,index,listecourante):
         listeRetour=[]
         commentaire="Nouvelle valeur acceptee"
         commentaire2=""
         valide=1
         if valeurTuple==None: return
         if valeurTuple==['']: return
         # On teste le type de la valeur
         valide=self.node.item.valide_item(valeurTuple)
         if not valide :
            try :
                valeur,valide=self.node.item.eval_valeur(valeurTuple)
                valide = self.node.item.valide_item(valeur)
            except :
                pass
         if not valide:
            commentaire="Valeur "+str(valeurTuple)+ " incorrecte : ajout a la liste refuse"
            commentaire2=self.node.item.info_erreur_item()
            return valide,commentaire,commentaire2,listeRetour

         # On valide la liste obtenue
         encorevalide=self.node.item.valide_liste_partielle(valeurTuple,listecourante)
         if not encorevalide :
            commentaire2=self.node.item.info_erreur_liste()
            return valide,commentaire,commentaire2,listeRetour
         #min,max = self.node.item.GetMinMax()
         #if len(listecourante)  >= max :
         #   commentaire="La liste a deja atteint le nombre maximum d'elements,ajout refuse"
         #   valide=0
         #   return valide,commentaire,commentaire2,listeRetour
         listeRetour.append(valeurTuple)
         return valide,commentaire,commentaire2,listeRetour
