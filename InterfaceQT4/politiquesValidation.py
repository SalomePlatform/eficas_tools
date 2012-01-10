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
# Modules Python
import types


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
                  commentaire = "impossible d'évaluer : %s " %`valeurentree`
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
#   Méthodes utilisées pour la manipulation des items en notation scientifique
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
         if "R" in self.node.item.object.definition.type:
                  clefobj=self.node.item.object.GetNomConcept()
                  if self.parent.appliEficas.dict_reels.has_key(clefobj):
                     if self.parent.appliEficas.dict_reels[clefobj].has_key(valeur):
                        valeurTexte=self.parent.appliEficas.dict_reels[clefobj][valeur]
         return valeurTexte

  def AjoutDsDictReel(self,texteValeur):
         # le try except est nécessaire pour saisir les paramétres
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
                  commentaire = "Valeur du mot-clé enregistrée"
                  self.SetValeurTexte(str(valeurentree))
            else:
                  cr = self.node.item.get_cr()
                  commentaire =  "Valeur du mot-clé non autorisée "+cr.get_mess_fatal()
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
         for valeur in listevaleur :
             # On teste le type de la valeur
             valeurScientifique=valeur
             valide=self.node.item.valide_item(valeur)
             if not valide :
                try :
                   valeur,valide=self.node.item.eval_valeur(valeur)
                   valide,commentaire = self.node.item.object.verif_type(valeur)
                except :
                   #return testtype,commentaire,"",listeRetour
                   pass
             if not valide:
                commentaire="Valeur "+str(valeur)+ " incorrecte : ajout à la liste refusé"
                commentaire2=self.node.item.info_erreur_item()
                return valide,commentaire,commentaire2,listeRetour

             # On valide la liste obtenue
             encorevalide=self.node.item.valide_liste_partielle(valeur,listecourante)
             if not encorevalide :
                commentaire2=self.node.item.info_erreur_liste()
                # On traite le cas ou la liste n est pas valide pour un pb de cardinalite
                min,max = self.node.item.GetMinMax()
                if len(listecourante) + 1 >= max :
                   commentaire="La liste a déjà atteint le nombre maximum d'éléments,ajout refusé"
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
         commentaire="Nouvelle valeur acceptée"
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
            commentaire="Valeur "+str(valeurTuple)+ " incorrecte : ajout à la liste refusé"
            commentaire2=self.node.item.info_erreur_item()
            return valide,commentaire,commentaire2,listeRetour

         # On valide la liste obtenue
         encorevalide=self.node.item.valide_liste_partielle(valeurTuple,listecourante)
         if not encorevalide :
            commentaire2=self.node.item.info_erreur_liste()
            # On traite le cas ou la liste n est pas valide pour un pb de cardinalite
            min,max = self.node.item.GetMinMax()
            if len(listecourante) + 1 >= max :
               commentaire="La liste a déjà atteint le nombre maximum d'éléments,ajout refusé"
               return valide,commentaire,commentaire2,listeRetour
         listeRetour.append(valeurTuple)
         return valide,commentaire,commentaire2,listeRetour
