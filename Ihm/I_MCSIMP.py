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
import types,string
import traceback
from copy import copy
from repr import Repr
myrepr = Repr()
myrepr.maxstring = 100
myrepr.maxother = 100

from Noyau.N_utils import repr_float
import Validation
import CONNECTOR

# Attention : les classes ASSD,.... peuvent etre surchargées
# dans le package Accas. Il faut donc prendre des précautions si
# on utilise les classes du Noyau pour faire des tests (isxxxx, ...)
# Si on veut créer des objets comme des CO avec les classes du noyau
# ils n'auront pas les conportements des autres packages (pb!!!)
# Il vaut mieux les importer d'Accas mais problème d'import circulaire,
# on ne peut pas les importer au début.
# On fait donc un import local quand c'est nécessaire (peut occasionner
# des pbs de prformance).
from Noyau.N_ASSD import ASSD,assd
from Noyau.N_GEOM import GEOM,geom
from Noyau.N_CO import CO
import Accas
# fin attention

from Extensions import parametre
from Extensions import param2
import I_OBJECT
import CONNECTOR
from I_VALIDATOR import ValError,listProto

class MCSIMP(I_OBJECT.OBJECT):

  def GetNomConcept(self):
      p=self
      while p.parent :
         try :
            nomconcept=p.get_sdname()
            return nomconcept
         except:
            try :
               nomconcept= p.object.get_sdname()
               return nomconcept
            except :
               pass
         p=p.parent
      return ""

  def GetText(self):
    """
        Retourne le texte à afficher dans l'arbre représentant la valeur de l'objet
        pointé par self
    """

    if self.valeur == None : 
      return None
    elif type(self.valeur) == types.FloatType : 
      # Traitement d'un flottant isolé
      txt = str(self.valeur)
      clefobj=self.GetNomConcept()
      if self.jdc.appli.appliEficas.dict_reels.has_key(clefobj):
        if self.jdc.appli.appliEficas.dict_reels[clefobj].has_key(self.valeur):
           txt=self.jdc.appli.appliEficas.dict_reels[clefobj][self.valeur]
    elif type(self.valeur) in (types.ListType,types.TupleType) :
      # Traitement des listes
      txt='('
      sep=''
      for val in self.valeur:
        if type(val) == types.FloatType : 
           clefobj=self.GetNomConcept()
           if self.jdc.appli.appliEficas.dict_reels.has_key(clefobj):
              if self.jdc.appli.appliEficas.dict_reels[clefobj].has_key(val):
                 txt=txt + sep +self.jdc.appli.appliEficas.dict_reels[clefobj][val]
              else :
                 txt=txt + sep + str(val)
           else :
              txt=txt + sep + str(val)
        else: 
           txt = txt + sep+ str(val)
        if len(txt) > 200:
            #ligne trop longue, on tronque
            txt=txt+" ..."
            break
        sep=','
      txt=txt+')'
    else:
      # Traitement des autres cas
      txt = str(self.valeur)

    # txt peut etre une longue chaine sur plusieurs lignes.
    # Il est possible de tronquer cette chaine au premier \n et 
    # de limiter la longueur de la chaine a 30 caracteres. Cependant
    # ceci provoque une perte d'information pour l'utilisateur
    # Pour le moment on retourne la chaine telle que
    return txt

  def getval(self):
    """ 
       Retourne une chaîne de caractère représentant la valeur de self 
    """
    val=self.valeur
    if type(val) == types.FloatType : 
      clefobj=self.GetNomConcept()
      if self.jdc.appli.appliEficas.dict_reels.has_key(clefobj):
        if self.jdc.appli.appliEficas.appliEficas.dict_reels[clefobj].has_key(val):
           return self.jdc.appli.appliEficas.dict_reels[clefobj][val]
    if type(val) != types.TupleType :
      try:
        return val.get_name()
      except:
        return val
    else :
      s='( '
      for item in val :
        try :
          s=s+item.get_name()+','
        except:
          s=s+`item`+','
      s=s+' )'
      return s

  def wait_co(self):
    """
        Méthode booléenne qui retourne 1 si l'objet attend un objet ASSD 
        qui n'existe pas encore (type CO()), 0 sinon
    """
    for typ in self.definition.type:
      if type(typ) == types.ClassType or isinstance(typ,type):
        if issubclass(typ,CO) :
           return 1
    return 0

  def wait_assd(self):
    """ 
        Méthode booléenne qui retourne 1 si le MCS attend un objet de type ASSD 
        ou dérivé, 0 sinon
    """
    for typ in self.definition.type:
      if type(typ) == types.ClassType or isinstance(typ,type):
        if issubclass(typ,ASSD) and not issubclass(typ,GEOM):
          return 1
    return 0

  def wait_assd_or_geom(self):
    """ 
         Retourne 1 si le mot-clé simple attend un objet de type
         assd, ASSD, geom ou GEOM
         Retourne 0 dans le cas contraire
    """
    for typ in self.definition.type:
      if type(typ) == types.ClassType or isinstance(typ,type):
        if typ.__name__ in ("GEOM","ASSD","geom","assd") or issubclass(typ,GEOM) :
          return 1
    return 0

  def wait_geom(self):
    """ 
         Retourne 1 si le mot-clé simple attend un objet de type GEOM
         Retourne 0 dans le cas contraire
    """
    for typ in self.definition.type:
      if type(typ) == types.ClassType or isinstance(typ,type):
        if issubclass(typ,GEOM) : return 1
    return 0

  def wait_TXM(self):
    """ 
         Retourne 1 si le mot-clé simple attend un objet de type TXM
         Retourne 0 dans le cas contraire
    """
    for typ in self.definition.type:
      if typ == 'TXM' :return 1
    return 0

  def get_liste_valeurs(self):
    """
    """
    if self.valeur == None:
      return []
    elif type(self.valeur) == types.TupleType:
      return list(self.valeur)
    elif type(self.valeur) == types.ListType:
      return self.valeur
    else:
      return [self.valeur]

  def isoblig(self):
    return self.definition.statut=='o'

  def valid_val(self,valeur):
      """
        Verifie que la valeur passee en argument (valeur) est valide
        sans modifier la valeur courante 
      """
      lval=listProto.adapt(valeur)
      if lval is None:
         valid=0
         mess="None n'est pas une valeur autorisée"
      else:
         try:
            for val in lval:
                self.typeProto.adapt(val)
                self.intoProto.adapt(val)
            self.cardProto.adapt(lval)
            if self.definition.validators:
                self.definition.validators.convert(lval)
            valid,mess=1,""
         except ValError,e:
            mess=str(e)
            valid=0
      return valid,mess

  def valid_valeur(self,new_valeur):
      """
        Verifie que la valeur passee en argument (new_valeur) est valide
        sans modifier la valeur courante (evite d'utiliser set_valeur et est plus performant)
      """
      validite,mess=self.valid_val(new_valeur)
      return validite

  def valid_valeur_partielle(self,new_valeur):
      """
        Verifie que la valeur passee en argument (new_valeur) est une liste partiellement valide
        sans modifier la valeur courante du mot cle
      """
      validite=1
      try:
          for val in new_valeur:
              self.typeProto.adapt(val)
              self.intoProto.adapt(val)
              #on ne verifie pas la cardinalité
              if self.definition.validators:
                  validite=self.definition.validators.valide_liste_partielle(new_valeur)
      except ValError,e:
          validite=0

      return validite

  def update_condition_bloc(self):
      """ Met a jour les blocs conditionnels dependant du mot cle simple self
      """
      if self.definition.position == 'global' : 
         self.etape.deep_update_condition_bloc()
      elif self.definition.position == 'global_jdc' :
         self.jdc.deep_update_condition_bloc()
      else:
         self.parent.update_condition_bloc()

  def set_valeur(self,new_valeur,evaluation='oui'):
        #print "set_valeur",new_valeur
        self.init_modif()
        self.valeur = new_valeur
        self.val = new_valeur
        self.update_condition_bloc()
        self.fin_modif()
        return 1

  def eval_valeur(self,new_valeur):
    """
        Essaie d'évaluer new_valeur comme une SD, une déclaration Python 
        ou un EVAL: Retourne la valeur évaluée (ou None) et le test de réussite (1 ou 0)
    """
    sd = self.jdc.get_sd_avant_etape(new_valeur,self.etape)
    #sd = self.jdc.get_contexte_avant(self.etape).get(new_valeur,None)
    #print sd
    if sd is not None:
      return sd,1
    lsd = self.jdc.cherche_list_avant(self.etape,new_valeur) 
    if lsd :
      return lsd,1
    else:
      d={}
      # On veut EVAL avec tous ses comportements. On utilise Accas. Perfs ??
      d['EVAL']=Accas.EVAL
      try :
        objet = eval(new_valeur,d)
        return objet,1
      except Exception:
        itparam=self.cherche_item_parametre(new_valeur)
        if itparam:
             return itparam,1
        try :
             object=eval(new_valeur.valeur,d)
        except :
             pass
        if CONTEXT.debug : traceback.print_exc()
        return None,0

  def eval_val(self,new_valeur):
    """
       Tente d'evaluer new_valeur comme un objet du jdc (par appel a eval_val_item)
       ou comme une liste de ces memes objets
       Si new_valeur contient au moins un separateur (,), tente l'evaluation sur
       la chaine splittee
    """
    if type(new_valeur) in (types.ListType,types.TupleType):
       valeurretour=[]
       for item in new_valeur :
          valeurretour.append(self.eval_val_item(item))
       return valeurretour
    else:
       valeur=self.eval_val_item(new_valeur)
       return valeur

  def eval_val_item(self,new_valeur):
    """
       Tente d'evaluer new_valeur comme un concept, un parametre, un objet Python
       Si c'est impossible retourne new_valeur inchange
       argument new_valeur : string (nom de concept, de parametre, expression ou simple chaine)
    """
    if self.etape and self.etape.parent:
       valeur=self.etape.parent.eval_in_context(new_valeur,self.etape)
       return valeur
    else:
       try :
           valeur = eval(val)
           return valeur
       except:
           #traceback.print_exc()
           return new_valeur
           pass

  def cherche_item_parametre (self,new_valeur):
        try:
          nomparam=new_valeur[0:new_valeur.find("[")]
          indice=new_valeur[new_valeur.find("[")+1:new_valeur.find("]")]
          for p in self.jdc.params:
             if p.nom == nomparam :
                if int(indice) < len(p.get_valeurs()):
                   itparam=parametre.ITEM_PARAMETRE(p,int(indice))
                   return itparam
          return None
        except:
          return None

  def update_concept(self,sd):
    if type(self.valeur) in (types.ListType,types.TupleType) :
       if sd in self.valeur:self.fin_modif()
    else:
       if sd == self.valeur:self.fin_modif()

  def delete_concept(self,sd):
    """ 
        Inputs :
           - sd=concept detruit
        Fonction :
        Met a jour la valeur du mot cle simple suite à la disparition 
        du concept sd
    """
    #print "delete_concept",sd
    if type(self.valeur) == types.TupleType :
      if sd in self.valeur:
        self.init_modif()
        self.valeur=list(self.valeur)
        self.valeur.remove(sd)
        self.fin_modif()
    elif type(self.valeur) == types.ListType:
      if sd in self.valeur:
        self.init_modif()
        self.valeur.remove(sd)
        self.fin_modif()
    else:
      if self.valeur == sd:
        self.init_modif()
        self.valeur=None
        self.val=None
        self.fin_modif()

  def replace_concept(self,old_sd,sd):
    """
        Inputs :
           - old_sd=concept remplacé
           - sd=nouveau concept
        Fonction :
        Met a jour la valeur du mot cle simple suite au remplacement 
        du concept old_sd
    """
    #print "replace_concept",old_sd,sd
    if type(self.valeur) == types.TupleType :
      if old_sd in self.valeur:
        self.init_modif()
        self.valeur=list(self.valeur)
        i=self.valeur.index(old_sd)
        self.valeur[i]=sd
        self.fin_modif()
    elif type(self.valeur) == types.ListType:
      if old_sd in self.valeur:
        self.init_modif()
        i=self.valeur.index(old_sd)
        self.valeur[i]=sd
        self.fin_modif()
    else:
      if self.valeur == old_sd:
        self.init_modif()
        self.valeur=sd
        self.val=sd
        self.fin_modif()

  def set_valeur_co(self,nom_co):
      """
          Affecte à self l'objet de type CO et de nom nom_co
      """
      #print "set_valeur_co",nom_co
      step=self.etape.parent
      if nom_co == None or nom_co == '':
         new_objet=None
      else:
         # Avant de créer un concept il faut s'assurer du contexte : step 
         # courant
         sd= step.get_sd_autour_etape(nom_co,self.etape,avec='oui')
         if sd:
            # Si un concept du meme nom existe deja dans la portée de l'étape
            # on ne crée pas le concept
            return 0,"un concept de meme nom existe deja"
         # Il n'existe pas de concept de meme nom. On peut donc le créer 
         # Il faut néanmoins que la méthode NommerSdProd de step gère les 
         # contextes en mode editeur
         # Normalement la méthode  du Noyau doit etre surchargée
         # On déclare l'étape du mot clé comme etape courante pour NommerSdprod
         cs= CONTEXT.get_current_step()
         CONTEXT.unset_current_step()
         CONTEXT.set_current_step(step)
         step.set_etape_context(self.etape)
         new_objet = Accas.CO(nom_co)
         CONTEXT.unset_current_step()
         CONTEXT.set_current_step(cs)
      self.init_modif()
      self.valeur = new_objet
      self.val = new_objet
      # On force l'enregistrement de new_objet en tant que concept produit 
      # de la macro en appelant get_type_produit avec force=1
      self.etape.get_type_produit(force=1)
      self.fin_modif()
      step.reset_context()
      #print "set_valeur_co",new_objet
      return 1,"Concept créé"
        
  def verif_existence_sd(self):
     """
        Vérifie que les structures de données utilisées dans self existent bien dans le contexte
        avant étape, sinon enlève la référence à ces concepts
     """
     #print "verif_existence_sd"
     # Attention : possible probleme avec include
     # A priori il n'y a pas de raison de retirer les concepts non existants
     # avant etape. En fait il s'agit uniquement eventuellement de ceux crees par une macro
     l_sd_avant_etape = self.jdc.get_contexte_avant(self.etape).values()  
     if type(self.valeur) in (types.TupleType,types.ListType) :
       l=[]
       for sd in self.valeur:
         if isinstance(sd,ASSD) :
            if sd in l_sd_avant_etape or self.etape.get_sdprods(sd.nom) is sd:
               l.append(sd)
         else:
            l.append(sd)
       if len(l) < len(self.valeur):
          self.init_modif()
          self.valeur=tuple(l)
          self.fin_modif()
     else:
       if isinstance(self.valeur,ASSD) :
          if self.valeur not in l_sd_avant_etape and self.etape.get_sdprods(self.valeur.nom) is None:
             self.init_modif()
             self.valeur = None
             self.fin_modif()
 
  def get_min_max(self):
     """
     Retourne les valeurs min et max admissibles pour la valeur de self
     """
     return self.definition.min,self.definition.max


  def get_type(self):
     """
     Retourne le type attendu par le mot-clé simple
     """
     return self.definition.type

  def delete_mc_global(self):
      """ Retire self des declarations globales
      """
      if self.definition.position == 'global' : 
         etape = self.get_etape()
         if etape :
            del etape.mc_globaux[self.nom]
      elif self.definition.position == 'global_jdc' :
         del self.jdc.mc_globaux[self.nom]

  def update_mc_global(self):
     """
        Met a jour les mots cles globaux enregistrés dans l'étape parente
        et dans le jdc parent.
        Un mot cle simple peut etre global. 
     """
     if self.definition.position == 'global' :
        etape = self.get_etape()
        if etape :
           etape.mc_globaux[self.nom]=self
     elif self.definition.position == 'global_jdc' :
        if self.jdc:
           self.jdc.mc_globaux[self.nom]=self

  def nbrColonnes(self):
     genea = self.get_genealogie()
     if "VALE_C" in genea and "DEFI_FONCTION" in genea : return 3
     if "VALE" in genea and "DEFI_FONCTION" in genea : return 2
     return 0

  def valide_item(self,item):
      """Valide un item isolé. Cet item est candidat à l'ajout à la liste existante"""
      valid=1
      try:
          #on verifie le type
          self.typeProto.adapt(item)
          #on verifie les choix possibles
          self.intoProto.adapt(item)
          #on ne verifie pas la cardinalité
          if self.definition.validators:
              valid=self.definition.validators.verif_item(item)
      except ValError,e:
          #traceback.print_exc()
          valid=0
      return valid

  def verif_type(self,item):
      """Verifie le type d'un item de liste"""
      try:
          #on verifie le type
          self.typeProto.adapt(item)
          #on verifie les choix possibles
          self.intoProto.adapt(item)
          #on ne verifie pas la cardinalité mais on verifie les validateurs
          if self.definition.validators:
              valid=self.definition.validators.verif_item(item)
          comment=""
          valid=1
      except ValError,e:
          #traceback.print_exc()
          comment=str(e)
          valid=0
      return valid,comment

#--------------------------------------------------------------------------------
 
#ATTENTION SURCHARGE : toutes les methodes ci apres sont des surcharges du Noyau et de Validation
# Elles doivent etre reintegrees des que possible


  def verif_typeihm(self,val,cr='non'):
      try :
         val.eval()
         return 1
      except :
         traceback.print_exc()
         pass
      return self.verif_type(val,cr)

  def verif_typeliste(self,val,cr='non') :
      verif=0
      for v in val :
        verif=verif+self.verif_typeihm(v,cr)
      return verif

  def init_modif_up(self):
    Validation.V_MCSIMP.MCSIMP.init_modif_up(self)
    CONNECTOR.Emit(self,"valid")
