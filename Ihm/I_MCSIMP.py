import types,string
import traceback
from copy import copy
from repr import Repr
myrepr = Repr()
myrepr.maxstring = 100
myrepr.maxother = 100

from Noyau.N_utils import repr_float
from Noyau.N_ASSD import ASSD,assd
from Noyau.N_GEOM import GEOM,geom
from Noyau.N_CO import CO
from Noyau.N_EVAL import EVAL
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
      txt = repr_float(self.valeur)
    elif type(self.valeur) in (types.ListType,types.TupleType) :
      txt='('
      i=0
      for val in self.valeur:
        if type(val) == types.FloatType : 
           txt=txt + i*',' + repr_float(val)
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
    # il faut tronquer txt au delà d'un certain nombre de caractères
    # et avant tout retour chariot (txt peut être une chaîne de caractères
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
        if typ is CO : return 1
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
        if typ in (GEOM,ASSD,geom,assd) or issubclass(typ,GEOM) :
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
        return 1
      else:
        # On n'a pas trouve de concept ni réussi à évaluer la valeur 
        # dans le contexte
        # Si le mot cle simple attend un type CO on crée un objet de ce 
        # type de nom new_valeur
        if self.wait_co():
          try:
            self.valeur=CO(new_valeur)
          except:
            traceback.print_exc()
            return 0
          self.val=self.valeur
          self.init_modif()
          return 1
        elif type(new_valeur)==types.StringType and self.wait_TXM():
          self.val = new_valeur
          self.valeur = new_valeur
          self.init_modif()
          return 1
        else:
          return 0
    else :
      # on ne fait aucune vérification ...
      try:
        self.valeur = eval(new_valeur)
        self.val = eval(new_valeur)
        self.init_modif()
        return 1
      except:
        self.valeur = new_valeur
        self.val = new_valeur
        self.init_modif()
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

  def copy(self):
    """ Retourne une copie de self """
    objet = self.makeobjet()
    #XXX est ce utile ??
    objet.valeur = copy(self.valeur)
    objet.val = copy(self.val)
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

