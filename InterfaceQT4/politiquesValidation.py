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

         if not validite :
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
                           if not self.parent.dict_reels.has_key(clefobj):
                              self.parent.dict_reels[clefobj] = {}
                           self.parent.dict_reels[clefobj][clef]=texteValeur
                           self.parent.dict_reels[clefobj]
                           self.node.item.object.fin_modif()
         except:
            pass

  def GetValeurTexte(self,valeur) :
         valeurTexte=valeur
         if "R" in self.node.item.object.definition.type:
                  clefobj=self.node.item.object.GetNomConcept()
                  if self.parent.dict_reels.has_key(clefobj):
                     if self.parent.dict_reels[clefobj].has_key(valeur):
                        valeurTexte=self.parent.dict_reels[clefobj][valeur]
         return valeurTexte

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

 
#------------------------
class PolitiquePlusieurs:
#------------------------
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
             valide=self.node.item.valide_item(valeur)
             if not valide :
                #print self.__class__
                #if not testtype :
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
                   return valide,commentaire,commentaire2,listeRetour
             # On ajoute la valeur testee a la liste courante et a la liste acceptee
             listecourante.insert(index,valeur)
             index=index+1
             listeRetour.append(valeur)

         return valide,commentaire,commentaire2,listeRetour
