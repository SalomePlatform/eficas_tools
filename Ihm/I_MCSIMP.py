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
# fin attention

from Extensions import parametre
import I_OBJECT

class MCSIMP(I_OBJECT.OBJECT):
  def GetText(self):
    """
        Retourne le texte à afficher dans l'arbre représentant la valeur de l'objet
        pointé par self
    """
    if self.valeur == None : 
      return None
    elif type(self.valeur) == types.FloatType : 
      #txt = repr_float(self.valeur)
      # Normalement str fait un travail correct
      txt = str(self.valeur)
    elif type(self.valeur) in (types.ListType,types.TupleType) :
      txt='('
      i=0
      for val in self.valeur:
        if type(val) == types.FloatType : 
           # Normalement str fait un travail correct
           #txt=txt + i*',' + repr_float(val)
           txt=txt + i*',' + str(val)
        elif type(val) == types.InstanceType and isinstance(val,ASSD): 
           txt = txt + i*',' + val.get_name()
        else: 
           txt = txt + i*','+ myrepr.repr(val)
        i=1
      txt=txt+')'
    else:
      txt = self.getval()
    if type(txt) != types.StringType:
      if type(txt) == types.InstanceType:
        if isinstance(txt,parametre.PARAMETRE):
          return str(txt)
      return repr(txt)
    # txt peut etre une longue chaine sur plusieurs lignes.
    # Il est possible de tronquer cette chaine au premier \n et 
    # de limiter la longueur de la chaine a 30 caracteres. Cependant
    # ceci provoque une perte d'information pour l'utilisateur
    # Pour le moment on retourne la chaine telle que
    return txt

    # Partie de code inaccessible (pour memoire)
    # txt est tronquee au dela d'un certain nombre de caractères
    # et avant tout retour chariot (txt peut etre une chaine de caractères
    # sur plusieurs lignes (ex:shell)
    txt = string.split(txt,'\n')[0]
    if len(txt) < 30 :
      return txt
    else:
      return txt[0:29]

  def getval(self):
    """ 
       Retourne une chaîne de caractère représentant la valeur de self 
    """
    val=self.valeur
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

  def get_min_max(self):
    return self.definition.min,self.definition.max

  def wait_co(self):
    """
        Méthode booléenne qui retourne 1 si l'objet attend un objet ASSD 
        qui n'existe pas encore (type CO()), 0 sinon
    """
    for typ in self.definition.type:
      if type(typ) == types.ClassType :
        if issubclass(typ,CO) :
           return 1
    return 0

  def wait_assd(self):
    """ 
        Méthode booléenne qui retourne 1 si le MCS attend un objet de type ASSD 
        ou dérivé, 0 sinon
    """
    for typ in self.definition.type:
      if type(typ) == types.ClassType :
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
      if type(typ) == types.ClassType :
        if typ.__name__ in ("GEOM","ASSD","geom","assd") or issubclass(typ,GEOM) :
          return 1
    return 0

  def wait_geom(self):
    """ 
         Retourne 1 si le mot-clé simple attend un objet de type GEOM
         Retourne 0 dans le cas contraire
    """
    for typ in self.definition.type:
      if type(typ) == types.ClassType :
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

  def set_valeur(self,new_valeur,evaluation='oui'):
    """
        Remplace la valeur de self(si elle existe) par new_valeur
            - si evaluation = 'oui' : 
                        essaie d'évaluer new_valeur dans le contexte
            - si evaluation = 'non' : 
                        n'essaie pas d'évaluer (on stocke une string ou 
                        une valeur de la liste into )
    """
    if evaluation == 'oui' and not self.wait_assd_or_geom():
      valeur,test = self.eval_valeur(new_valeur)
      if test :
        self.val = new_valeur
        self.valeur = valeur
        self.init_modif()
        self.fin_modif()
        return 1
      else:
        # On n'a pas trouve de concept ni réussi à évaluer la valeur 
        # dans le contexte
        # Si le mot cle simple attend un type CO on crée un objet de ce 
        # type de nom new_valeur
        if self.wait_co():
          try:
            # Pour avoir la classe CO avec tous ses comportements
            from Accas import CO
            self.valeur=CO(new_valeur)
          except:
            traceback.print_exc()
            return 0
          self.init_modif()
          self.val=self.valeur
          self.fin_modif()
          return 1
        elif type(new_valeur)==types.StringType and self.wait_TXM():
          self.init_modif()
          self.val = new_valeur
          self.valeur = new_valeur
          self.fin_modif()
          return 1
        else:
          return 0
    else :
      # on ne fait aucune vérification ...
      self.init_modif()
      try:
        self.valeur = eval(new_valeur)
        self.val = eval(new_valeur)
        self.fin_modif()
        return 1
      except:
        self.valeur = new_valeur
        self.val = new_valeur
        self.fin_modif()
        return 1

  def eval_valeur(self,new_valeur):
    """
        Essaie d'évaluer new_valeur comme une SD, une déclaration Python 
        ou un EVAL:
           Retourne la valeur évaluée (ou None) et le test de réussite (1 ou 0)
    """
    #sd = self.jdc.get_sd_avant_etape(new_valeur,self.etape)
    sd = self.jdc.get_contexte_avant(self.etape).get(new_valeur,None)
    if sd :
      return sd,1
    else:
      d={}
      # On veut EVAL avec tous ses comportements. On utilise Accas. Perfs ??
      from Accas import EVAL
      d['EVAL']=EVAL
      try :
        objet = eval(new_valeur,d)
        return objet,1
      except Exception:
        if CONTEXT.debug : traceback.print_exc()
        return None,0

  def delete_concept(self,sd):
    """ 
        Inputs :
           sd=concept detruit
        Fonction :
           Met a jour la valeur du mot cle simple suite à la disparition 
           du concept sd
    """
    if type(self.valeur) == types.TupleType :
      if sd in self.valeur:
        self.valeur=list(self.valeur)
        self.valeur.remove(sd)
        self.init_modif()
    elif type(self.valeur) == types.ListType:
      if sd in self.valeur:
        self.valeur.remove(sd)
        self.init_modif()
    else:
      if self.valeur == sd:
        self.valeur=None
        self.val=None
        self.init_modif()

  def replace_concept(self,old_sd,sd):
    """
        Inputs :
           old_sd=concept remplacé
           sd=nouveau concept
        Fonction :
           Met a jour la valeur du mot cle simple suite au remplacement 
           du concept old_sd
    """
    if type(self.valeur) == types.TupleType :
      if old_sd in self.valeur:
        self.valeur=list(self.valeur)
        i=self.valeur.index(old_sd)
        self.valeur[i]=sd
        self.init_modif()
    elif type(self.valeur) == types.ListType:
      if old_sd in self.valeur:
        i=self.valeur.index(old_sd)
        self.valeur[i]=sd
        self.init_modif()
    else:
      if self.valeur == old_sd:
        self.valeur=sd
        self.val=sd
        self.init_modif()

  def copy(self):
    """ Retourne une copie de self """
    objet = self.makeobjet()
    # il faut copier les listes et les tuples mais pas les autres valeurs
    # possibles (réel,SD,...)
    if type(self.valeur) in (types.ListType,types.TupleType):
       objet.valeur = copy(self.valeur)
    else:
       objet.valeur = self.valeur
    objet.val = objet.valeur
    return objet

  def makeobjet(self):
    return self.definition(val = None, nom = self.nom,parent = self.parent)

  def get_sd_utilisees(self):
    """ 
        Retourne une liste qui contient la SD utilisée par self si c'est le cas
        ou alors une liste vide
    """
    l=[]
    if type(self.valeur) == types.InstanceType:
      #XXX Est ce différent de isinstance(self.valeur,ASSD) ??
      if issubclass(self.valeur.__class__,ASSD) : l.append(self.valeur)
    return l


  def set_valeur_co(self,nom_co):
      """
          Affecte à self l'objet de type CO et de nom nom_co
      """
      step=self.etape.parent
      if nom_co == None or nom_co == '':
         new_objet=None
      else:
         # Pour le moment on importe en local le CO de Accas.
         # Si problème de perfs, il faudra faire autrement
         from Accas import CO
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
         new_objet = CO(nom_co)
         CONTEXT.unset_current_step()
         CONTEXT.set_current_step(cs)
      self.init_modif()
      self.valeur = new_objet
      self.val = new_objet
      self.fin_modif()
      step.reset_context()
      # On force l'enregistrement de new_objet en tant que concept produit 
      # de la macro en appelant get_type_produit avec force=1
      self.etape.get_type_produit(force=1)
      return 1,"Concept créé"
	
  def reparent(self,parent):
     """
         Cette methode sert a reinitialiser la parente de l'objet
     """
     self.parent=parent
     self.jdc=parent.jdc
     self.etape=parent.etape

  def verif_existence_sd(self):
     """
        Vérifie que les structures de données utilisées dans self existent bien dans le contexte
	avant étape, sinon enlève la référence à ces concepts
     """
     l_sd_avant_etape = self.jdc.get_contexte_avant(self.etape).values()  
     if type(self.valeur) in (types.TupleType,types.ListType) :
       l=[]
       for sd in self.valeur:
         if isinstance(sd,ASSD) :
	    if sd in l_sd_avant_etape :
	       l.append(sd)
	 else:
	    l.append(sd)
       self.valeur=l
       # Est ce init_modif ou init_modif_up
       # Normalement init_modif va avec fin_modif
       self.init_modif()
       self.fin_modif()
     else:
       if isinstance(self.valeur,ASSD) :
	  if self.valeur not in l_sd_avant_etape :
	     self.valeur = None
             self.init_modif()
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
 
#ATTENTION : toutes les methodes ci apres sont des surcharges du Noyau et de Validation
# Elles doivent etre reintegrees des que possible

  def isvalid(self,cr='non'):
      """
         Cette méthode retourne un indicateur de validité de l'objet
         de type MCSIMP

         - 0 si l'objet est invalide

         - 1 si l'objet est valide

         Le paramètre cr permet de paramétrer le traitement. 
         Si cr == 'oui'
             la méthode construit également un comte-rendu de validation
             dans self.cr qui doit avoir été créé préalablement.
      """
      if self.state == 'unchanged':
        return self.valid
      else:
        valid = 1
        if hasattr(self,'valid'):
          old_valid = self.valid
        else:
          old_valid = None
        v=self.valeur
        #  presence
        if self.isoblig() and v == None :
          if cr == 'oui' :
            self.cr.fatal(string.join(("Mot-clé : ",self.nom," obligatoire non valorisé")))
          valid = 0
        # type,into ...
        valid = self.verif_type(cr=cr)*self.verif_into(cr=cr)*self.verif_card(cr=cr)
        self.valid = valid
        self.state = 'unchanged'
        # Si la validité du mot clé a changé, on le signale à l'objet parent
        if not old_valid:
          self.init_modif_up()
        elif old_valid != self.valid : 
          self.init_modif_up()
        return self.valid

 
 
 
 
 
 
 
 
 
 
 
 
 
