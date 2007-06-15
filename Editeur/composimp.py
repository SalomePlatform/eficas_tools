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
import string,types,os
from Tkinter import *
import Pmw
from copy import copy,deepcopy
import traceback

# Modules Eficas
import Objecttreeitem
import prefs
import panels
import images
from widgets import ListeChoix
from widgets import FenetreDeSelection

from Noyau.N_CR import justify_text
from utils import substract_list

      
class SIMPTreeItem(Objecttreeitem.AtomicObjectTreeItem):
  from newsimppanel import newSIMPPanel
  panel = newSIMPPanel

  def init(self) :
      self.expandable = 0
      self.affect_panel()


  def affect_panel(self):
      """
      Cette méthode attribue le panel à l'objet pointé par self en fonction de la
      nature de la valeur demandée pour cet objet
      """
      from uniquepanel import UNIQUE_Panel
      from plusieurspanel import PLUSIEURS_Panel

      #print "affect_panel : ",self.nom,self.is_list(),self.has_into()
      # Attention l ordre des if est important

      if self.wait_shell():
          # l'objet attend un shell
          from shellpanel import SHELLPanel
          self.panel = SHELLPanel
      elif self.has_into():
          # l'objet prend sa (ses) valeur(s) dans un ensemble discret de valeurs
          if self.is_list() :
             from plusieursintopanel import PLUSIEURS_INTO_Panel
             self.panel = PLUSIEURS_INTO_Panel
          else:
             from uniqueintopanel import UNIQUE_INTO_Panel
             self.panel = UNIQUE_INTO_Panel
      else:
          # l'objet prend une ou des valeurs à priori quelconques
          if self.is_list() :
              # on attend une liste de valeurs mais de quel type ?
              if self.wait_assd():
                  # on attend une liste de SD
                  from plusieursassdpanel import PLUSIEURS_ASSD_Panel
                  self.panel = PLUSIEURS_ASSD_Panel
              else:
                  # on attend une liste de valeurs de types debase (entiers, réels,...)
                  #from plusieursbasepanel import PLUSIEURS_BASE_OR_UNELISTE_Panel
                  #self.panel = PLUSIEURS_BASE_OR_UNELISTE_Panel
                  from plusieursbasepanel import PLUSIEURS_BASE_Panel
                  self.panel = PLUSIEURS_BASE_Panel
          else:
              # on n'attend qu'une seule valeur mais de quel type ?
              if self.wait_co():
                  # on attend une SD ou un objet de la classe CO (qui n'existe pas encore)
                  from uniquesdcopanel import UNIQUE_SDCO_Panel
                  self.panel = UNIQUE_SDCO_Panel
              elif self.wait_assd():
                  # on attend une SD
                  from uniqueassdpanel import UNIQUE_ASSD_Panel
                  from uniqueassdpanel import UNIQUE_ASSD_Panel_Reel
                  if 'R' in self.GetType():
                     self.panel = UNIQUE_ASSD_Panel_Reel
                  else :
                     self.panel = UNIQUE_ASSD_Panel
              else:
                  # on attend une valeur d'un type de base (entier,réel,...)
                  if self.wait_complex():
                      # on attend un complexe
                      from uniquecomppanel import UNIQUE_COMP_Panel
                      self.panel = UNIQUE_COMP_Panel
                  else:
                      # on attend un entier, un réel ou une string
                      from uniquebasepanel import UNIQUE_BASE_Panel
                      self.panel = UNIQUE_BASE_Panel
      # cas particulier des fonctions
      genea = self.get_genealogie()
      if "VALE" in genea or "VALE_C" in genea:
         if "DEFI_FONCTION" in genea :
            from fonctionpanel import FONCTION_Panel
            self.panel=FONCTION_Panel
      #---------------------------------------------------------
      # PN ajout pour lancement de Salome
      #---------------------------------------------------------
      if hasattr( self.appli, 'salome' ):
          import panelsSalome

          self.select_noeud_maille=0
          self.clef_fonction="SALOME"
          for i in range(0,len( genea )) :
             self.clef_fonction=self.clef_fonction+"_"+ genea[i]
             #if genea[i] == "GROUP_NO" or genea[i] == "GROUP_MA":
          if "GROUP_NO" in genea[len(genea)-1] or "GROUP_MA" in genea[len(genea)-1]:
             self.select_noeud_maille=1

          recherche=panelsSalome.dict_classes_salome[self.panel]
          if hasattr(recherche,self.clef_fonction):
             self.panel=recherche
          if self.select_noeud_maille==1 :
             self.panel=recherche


  #-----------------------------------------------
  #
  # Methodes liees aux informations sur le Panel
  # ou au mot-clef simple
  #
  #-----------------------------------------------
  # is_list
  # get_into                a priori inutile --> commentee
  # has_into
  # wait_into                a priori inutile --> commentee
  # GetMinMax
  # GetMultiplicite
  # GetIntervalle
  # GetListeValeurs
  # get_liste_possible

  def is_list(self):
      """
          Cette méthode indique si le mot cle simple attend une liste (valeur de retour 1)
          ou s'il n'en attend pas (valeur de retour 0)

          Deux cas principaux peuvent se presenter : avec validateurs ou bien sans.
          Dans le cas sans validateur, l'information est donnée par l'attribut max
          de la definition du mot cle.
          Dans le cas avec validateur, il faut combiner l'information précédente avec
          celle issue de l'appel de la méthode is_list sur le validateur.On utilisera
          l'operateur ET pour effectuer cette combinaison (AndVal).
      """
      is_a_list=0
      min,max = self.GetMinMax()
      assert (min <= max)
      if max > 1 :
                is_a_list=1
      # Dans le cas avec validateurs, pour que le mot cle soit considéré
      # comme acceptant une liste, il faut que max soit supérieur a 1
      # ET que la méthode is_list du validateur retourne 1. Dans les autres cas
      # on retournera 0 (n'attend pas de liste)
      if self.definition.validators :
         is_a_list= self.definition.validators.is_list() * is_a_list
      return is_a_list 

  #def get_into(self,liste_courante=None):
  #    """
  #        Cette méthode retourne la liste de choix proposée par le mot cle. Si le mot cle ne propose
  #        pas de liste de choix, la méthode retourne None.
  #        L'argument d'entrée liste_courante, s'il est différent de None, donne la liste des choix déjà
  #        effectués par l'utilisateur. Dans ce cas, la méthode get_into doit calculer la liste des choix
  #        en en tenant compte.
  #        Cette méthode part du principe que la relation entre into du mot clé et les validateurs est
  #        une relation de type ET (AndVal).
  #    """
  #    if not self.object.definition.validators :
  #       return self.object.definition.into
  #    else:
  #       return self.object.definition.validators.get_into(liste_courante,self.definition.into)

  def has_into(self):
      """
          Cette méthode indique si le mot cle simple propose un choix (valeur de retour 1)
          ou s'il n'en propose pas (valeur de retour 0)

          Deux cas principaux peuvent se presenter : avec validateurs ou bien sans.
          Dans le cas sans validateur, l'information est donnée par l'attribut into
          de la definition du mot cle.
          Dans le cas avec validateurs, pour que le mot cle soit considéré
          comme proposant un choix, il faut que into soit présent OU
          que la méthode has_into du validateur retourne 1. Dans les autres cas
          on retournera 0 (ne propose pas de choix)
      """
      has_an_into=0
      if self.definition.into:
               has_an_into=1
      elif self.definition.validators :
         has_an_into= self.definition.validators.has_into()
      return has_an_into

#  def wait_into(self):
#      """ Méthode booléenne qui retourne 1 si l'objet pointé par self
#      prend ses valeurs dans un ensemble discret (into), 0 sinon """
#      if self.object.definition.into != None :
#          return 1
#      else:
#          return 0

  def GetMinMax(self):
      """ Retourne les valeurs min et max de la définition de object """
      return self.object.get_min_max()

  def GetMultiplicite(self):
      """ A préciser.
          Retourne la multiplicité des valeurs affectées à l'objet
          représenté par l'item. Pour le moment retourne invariablement 1.
      """
      return 1

  def GetIntervalle(self):
      """ 
           Retourne le domaine de valeur attendu par l'objet représenté 
           par l'item.
      """
      return self.object.getintervalle()

  def GetListeValeurs(self) :
      """ Retourne la liste des valeurs de object """
      valeurs=self.object.get_liste_valeurs()
      try :
        if "R" in self.object.definition.type:
           clef=self.object.GetNomConcept()
           if self.appli.dict_reels.has_key(clef):
              if type(valeurs) == types.TupleType:
                 valeurs_reelles=[]
                 for val in valeurs :
                    if self.appli.dict_reels[clef].has_key(val) : 
                       valeurs_reelles.append(self.appli.dict_reels[clef][val])
                    else :
                       valeurs_reelles.append(val)
              else :
                 if self.appli.dict_reels[clef].has_key(valeurs):
                    valeurs_reelles=self.appli.dict_reels[clef][valeurs]
              valeurs=valeurs_reelles
      except :
        pass
      return valeurs
    
  def get_liste_possible(self,listeActuelle=[]):
      if hasattr(self.definition.validators,'into'):
         valeurspossibles = self.definition.validators.into 
      else:
         valeurspossibles = self.get_definition().into

      #On ne garde que les items valides
      listevalideitem=[]
      for item in valeurspossibles:
          encorevalide=self.valide_item(item)
          if encorevalide :
             listevalideitem.append(item)

      #on ne garde que les choix possibles qui passent le test de valide_liste_partielle
      listevalideliste=[]
      for item in listevalideitem:
          encorevalide=self.valide_liste_partielle(item,listeActuelle)
          if encorevalide :
              listevalideliste.append(item)
      return listevalideliste

  def get_liste_param_possible(self):
      liste_param=[]
      for param in self.object.jdc.params:
          encorevalide=self.valide_item(param.valeur)
          if encorevalide:
             type_param=param.valeur.__class__.__name__
             for typ in self.definition.type:
                 if typ=='R':
                     liste_param.append(param)
                 if typ=='I' and type_param=='int':
                     liste_param.append(param)
                 if typ=='TXM' and type_param=='str':
                     liste_param.append(repr(param))
      return liste_param

  #--------------------------------------------------
  #
  # Methodes liees a la validite des valeurs saisies
  #
  #---------------------------------------------------
  # valide_item
  # valide_liste_partielle
  # valide_liste_complete
  # info_erreur_item
  # info_erreur_liste
  # IsInIntervalle
  # isvalid

  def valide_item(self,item):
      """
        La validation est réalisée directement par l'objet
      """
      return self.object.valide_item(item)
     
  def valide_liste_partielle(self,item,listecourante):
      #On protege la liste en entree en la copiant
      valeur=listecourante[:]
      valeur.append(item)
      return self.object.valid_valeur_partielle(valeur)

  def valide_liste_complete (self,valeur):
      return self.object.valid_valeur(valeur)

  def valide_val (self,valeur):
      return self.object.valid_val(valeur)

  def info_erreur_item(self) :
      commentaire=""
      if self.definition.validators :
         commentaire=self.definition.validators.info_erreur_item()
      return commentaire
      
  def aide(self) :
      commentaire=""
      if self.definition.validators :
         commentaire=self.definition.validators.aide()
      return commentaire

  def info_erreur_liste(self) :
      commentaire=""
      if self.definition.validators :
         commentaire=self.definition.validators.info_erreur_liste()
      return commentaire

  def IsInIntervalle(self,valeur):
      """ 
          Retourne 1 si la valeur est dans l'intervalle permis par
          l'objet représenté par l'item.
      """
      return self.valide_item(valeur)

  def isvalid(self):
    valide=self.object.isvalid()
    return valide

  #--------------------------------------------------
  #
  # Autres ...
  #
  #---------------------------------------------------
  # SetText         a priori inutilisee --> commentee
  # GetIconName
  # GetText
  # getval     a  priori inutilisee --> commentee
  # set_valeur_co
  # get_sd_avant_du_bon_type
  # verif        a  priori inutilisee --> commentee
  # delete_valeur_co

  #def SetText(self, text):
  #  try:
  #    value = eval(text)
  #    self.object.setval(value)
  #  except:
  #    pass

  def GetIconName(self):
    if self.isvalid():
      return "ast-green-ball"
    elif self.object.isoblig():
      return "ast-red-ball"
    else:
      return "ast-yel-ball"

  def GetText(self):
    """
    Classe SIMPTreeItem
    Retourne le texte à afficher dans l'arbre représentant la valeur de l'objet
    pointé par self 
    """
    text= self.object.GetText()
    return text
    
  #def getval(self):
  #    return self.object.getval()

  def set_valeur_co(self,nom_co):
      """
      Affecte au MCS pointé par self l'objet de type CO et de nom nom_co
      """
      ret = self.object.set_valeur_co(nom_co)
      #print "set_valeur_co",ret
      return ret
      
  def get_sd_avant_du_bon_type(self):
      """
      Retourne la liste des noms des SD présentes avant l'étape qui contient
      le MCS pointé par self et du type requis par ce MCS
      """
      a=self.object.etape.parent.get_sd_avant_du_bon_type(self.object.etape,self.object.definition.type)
      return a

  def get_sd_avant_du_bon_type_pour_type_de_base(self):
      a=self.object.jdc.get_sd_avant_du_bon_type_pour_type_de_base(self.object.etape,"LASSD")
      return a



  #def verif(self):
  #    pass

  def delete_valeur_co(self,valeur=None):
      """
           Supprime la valeur du mot cle (de type CO)
           il faut propager la destruction aux autres etapes
      """
      if not valeur : valeur=self.object.valeur
      # XXX faut il vraiment appeler del_sdprod ???
      #self.object.etape.parent.del_sdprod(valeur)
      self.object.etape.parent.delete_concept(valeur)

  #-----------------------------------------------
  #
  # Methodes liees au type de l objet attendu
  #
  #-----------------------------------------------
  # wait_co 
  # wait_geom
  # wait_complex
  # wait_reel
  # wait_shell
  # wait_assd
  # GetType

  def wait_co(self):
      """
      Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un objet de type ASSD qui n'existe pas encore (type CO()),
      0 sinon
      """
      return self.object.wait_co()

  def wait_geom(self):
      """
      Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un objet GEOM, 0 sinon
      """
      return self.object.wait_geom()
    
  def wait_complex(self):
      """ Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un complexe, 0 sinon """
      if 'C' in self.object.definition.type:
          return 1
      else:
          return 0

  def wait_reel(self):
      """ Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un réel, 0 sinon """
      if 'R' in self.object.definition.type:
          return 1
      else:
          return 0
        
  def wait_shell(self):
      """ Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un shell, 0 sinon """
      if 'shell' in self.object.definition.type:
          return 1
      else:
          return 0

  def wait_assd(self):
      """Méthode booléenne qui retourne 1 si l'objet pointé par self
      attend un objet de type ASSD ou dérivé, 0 sinon """
      return self.object.wait_assd()
    
  def wait_assd_or_type_base(self) :
      boo=0
      if len(self.object.definition.type) > 1 :
         if self.wait_reel() :
            boo = 1
         if 'I' in self.object.definition.type :
            boo = 1
      return boo

   
  def GetType(self):
      """ 
          Retourne le type de valeur attendu par l'objet représenté par l'item.
      """
      return self.object.get_type()

  #-----------------------------------------------------
  #
  # Methodes liees  a l evaluation de la valeur saisie
  #
  #-----------------------------------------------------
  # eval_valeur
  # eval_valeur_item
  # is_CO
  # traite_reel

  def eval_valeur(self,valeur):
      """ Lance l'interprétation de 'valeur' (chaîne de caractères) comme valeur de self :
             - retourne l'objet associé si on a pu interpréter (entier, réel, ASSD,...)
             - retourne 'valeur' (chaîne de caractères) sinon
      """
      newvaleur=self.eval_val(valeur)
      return newvaleur,1

  def eval_valeur_BAK(self,valeur):
      """ Lance l'interprétation de 'valeur' (chaîne de caractères) comme valeur
      de l'objet pointé par self :
        - retourne l'objet associé si on a pu interpréter (entier, réel, ASSD,...)
        - retourne 'valeur' (chaîne de caractères) sinon
        - retourne None en cas d invalidite
        - retourne invalide si 1 des objets du tuple l est
      """
      validite=1
      if type(valeur) in (types.ListType,types.TupleType) :
         valeurretour=[]
         for item in valeur :
             newvaleur,validiteitem=self.eval_valeur_item(item)
             valeurretour.append(newvaleur)
             if validiteitem == 0:
                validite=0
      else :
         valeurretour,validite= self.eval_valeur_item(valeur)
      if validite == 0 :
         valeurretour = None
      return valeurretour,validite

  def eval_valeur_item(self,valeur):
      """ Lance l'interprétation de 'valeur' qui doit ne pas etre un tuple 
          - va retourner la valeur de retour et la validite
            selon le type de l objet attendu
          - traite les reels et les parametres 
      """ 
      #print "eval_valeur_item",valeur
      if valeur==None or valeur == "" :
         return None,0
      validite=1
      if self.wait_reel():
             valeurinter = self.traite_reel(valeur)
             if valeurinter != None :
                valeurretour,validite= self.object.eval_valeur(valeurinter)
             else:
                valeurretour,validite= self.object.eval_valeur(valeur)
      elif self.wait_geom():
             valeurretour,validite = valeur,1
      else :
             valeurretour,validite= self.object.eval_valeur(valeur)
      #print "eval_valeur_item",valeurretour,validite

      if validite == 0:
         if type(valeur) == types.StringType and self.object.wait_TXM():
            essai_valeur="'" + valeur + "'"
            valeurretour,validite= self.object.eval_valeur(essai_valeur)

      if hasattr(valeurretour,'__class__'):
         #if valeurretour.__class__.__name__ in ('PARAMETRE','PARAMETRE_EVAL'):
         if valeurretour.__class__.__name__ in ('PARAMETRE',):
            validite=1

      #if self.wait_co():
         # CCAR : il ne faut pas essayer de creer un concept
         # il faut simplement en chercher un existant ce qui a du etre fait par self.object.eval_valeur(valeur)
         #try:
            #valeurretour=Accas.CO(valeur)
         #except:
            #valeurretour=None
            #validite=0
      # on est dans le cas où on a évalué et où on n'aurait pas du
      if self.object.wait_TXM() :
          if type(valeurretour) != types.StringType:
             valeurretour=str(valeur)
             validite=1
      return valeurretour,validite
      
  def is_CO(self,valeur=None):
      """
         Indique si valeur est un concept produit de la macro
         Cette méthode n'a de sens que pour un MCSIMP d'une MACRO
         Si valeur vaut None on teste la valeur du mot cle
      """
      # Pour savoir si un concept est un nouveau concept de macro
      # on regarde s'il est présent dans l'attribut sdprods de l'étape
      # ou si son nom de classe est CO.
      # Il faut faire les 2 tests car une macro non valide peut etre
      # dans un etat pas tres catholique avec des CO pas encore types
      # et donc pas dans sdprods (resultat d'une exception dans type_sdprod)
      if not valeur:valeur=self.object.valeur
      if valeur in self.object.etape.sdprods:return 1
      if type(valeur) is not types.InstanceType:return 0
      if valeur.__class__.__name__ == 'CO':return 1
      return 0

  def is_param(self,valeur) :
      for param in self.jdc.params:
          if (repr(param) == valeur):
             return 1
      return 0

  def traite_reel(self,valeur):
      """
      Cette fonction a pour but de rajouter le '.' en fin de chaîne pour un réel
      ou de détecter si on fait référence à un concept produit par DEFI_VALEUR
      ou un EVAL ...
      """
      valeur = string.strip(valeur)
      liste_reels = self.get_sd_avant_du_bon_type()
      if valeur in liste_reels:
          return valeur
      if len(valeur) >= 3 :
          if valeur[0:4] == 'EVAL' :
              # on a trouvé un EVAL --> on retourne directement la valeur
              return valeur
      if string.find(valeur,'.') == -1 :
          # aucun '.' n'a été trouvé dans valeur --> on en rajoute un à la fin
          if (self.is_param(valeur)):
              return valeur
          else:
              if string.find(valeur,'e') != -1:
                 # Notation scientifique ?
                 try :
                    r=eval(valeur)
                    return valeur
                 except :
                    return None
              else :
                 return valeur+'.'
      else:
          return valeur
        

import Accas
treeitem = SIMPTreeItem
objet = Accas.MCSIMP

