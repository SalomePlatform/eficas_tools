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

# Modules Eficas
import Accas
from Noyau.N_CR import CR

class CATALOGUE:
    def __init__(self,modules_cata):
        self.modules_cata = modules_cata # tuple de modules...
        self.cr = CR()
        self.state='undetermined'
        self.entites_attributs = {}
        self.entites_fils = []
        self.build_entites_attributs()
        self.build_entites_fils()

    def build_entites_attributs(self):
        pass
        
    def build_entites_fils(self):
        niv_types = Accas.NIVEAU(nom="types",label="Liste des types")
        niv_commandes = Accas.NIVEAU(nom="commandes",label="Liste des commandes")
        self.entites_fils.append(make_commande_cata(niv_types,self))
        self.entites_fils.append(make_commande_cata(niv_commandes,self))
        for module_cata in self.modules_cata:
            for e in dir(module_cata):
                obj = getattr(module_cata,e)
                if isCMD(obj):
                    self.entites_fils[1].register(make_commande_cata(obj,self.entites_fils[1]))
                elif type(obj) == types.ClassType:
                    if issubclass(obj,Accas.ASSD):
                        self.entites_fils[0].register(TYPE_CATA(obj))

    def init_modif(self):
        self.state = 'modified'
        
    def report(self):
      """ Classe CATALOGUE
          Methode pour generation d un rapport de validite
      """
      self.cr.purge()
      self.cr.debut="DEBUT CR validation : " 
      self.cr.fin="FIN CR validation :"
      self.state = 'modified'
      self.isvalid(cr='oui')
      for fils in self.entites_fils[1].entites :
        self.cr.add(fils.report())
      return self.cr

    def isvalid(self,cr='non'):
        if self.state != 'unchanged':
            valid=1
            for fils in self.entites_fils[1].entites_fils:
                if not fils.isvalid():
                    valid=0
                    break
            self.valid = valid
            self.state='unchanged'
        return self.valid
    
def make_commande_cata(objet,pere):
    if isinstance(objet,Accas.OPER):
        return OPER_CATA(objet,pere,objet.nom)
    elif isinstance(objet,Accas.PROC):
        return PROC_CATA(objet,pere,objet.nom)
    elif isinstance(objet,Accas.MACRO):
        return MACRO_CATA(objet,pere,objet.nom)
    elif isinstance(objet,Accas.FORM):
        return MACRO_CATA(objet,pere,objet.nom)
    elif isinstance(objet,Accas.NIVEAU):
        return NIVEAU_CATA(objet,pere,objet.nom)
    else:
        print "Erreur dans make_commande_cata : on cherche à évaluer un objet non référencé ",objet

def make_mc_cata(objet,pere,nom=''):
    if isinstance(objet,Accas.BLOC):
        return BLOC_CATA(objet,pere,nom)
    elif isinstance(objet,Accas.FACT):
        return FACT_CATA(objet,pere,nom)
    elif isinstance(objet,Accas.SIMP):
        return SIMP_CATA(objet,pere,nom)
    else:
        print "Erreur dans make_mc_cata : on cherche à évaluer un objet non référencé ",objet

class TYPE_CATA:
    def __init__(self,objet):
        self.objet = objet
        self.nom = objet.__name__

    def isvalid(self,cr='non'):
        return 1

    def get_valeur_attribut(self,nom_attr):
        if nom_attr == 'nom':return self.nom
        return None
   
class OBJET_CATA:
    attributs=[]
    attributs_defauts={}
    def __init__(self,objet,pere,nom):
        self.objet = objet
        self.nom = nom
        self.pere = pere
        self.cr = CR()
        self.state='undetermined'
        self.entites_fils = []
        self.entites_attributs = {}
        self.build_entites_attributs()
        self.build_entites_fils()

    def __str__(self):
        s=''
        s=self.__class__.__name__+' : '+self.nom
        return s
    
    def build_entites_attributs(self):        
        for attribut in self.attributs:
            if hasattr(self.objet,attribut):
                self.entites_attributs[attribut]=ATTR_CATA(attribut,getattr(self.objet,attribut))
            else:
                if self.attributs_defauts.has_key(attribut):
                    self.entites_attributs[attribut]=ATTR_CATA(attribut,self.attributs_defauts[attribut])
                else:
                    self.entites_attributs[attribut]=ATTR_CATA(attribut,None)

    def build_entites_fils(self):
        for k,v in self.objet.entites.items():
            self.entites_fils.append(make_mc_cata(v,self,nom=k))

    def get_valeur_attribut(self,nom_attr):
        if nom_attr in self.entites_attributs.keys():
            return self.entites_attributs[nom_attr].valeur
        elif nom_attr in self.attributs_defauts.keys():
            return self.attributs_defauts[nom_attr]
        elif nom_attr == 'domaine_validité':
            if self.entites_attributs['into'].valeur != None :
                return 'discret'
            else:
                return 'continu'

    def isvalid(self,cr='non'):
        if self.state =='unchanged':
            return self.valid
        else:
            valid = 1
            if hasattr(self,'valid'):
                old_valid = self.valid
            else:
                old_valid = None
            # on teste self lui-meme
            if self.nom == '' or self.nom == None : valid=0
            # on teste les attributs
            for attribut in self.entites_attributs.values():
                if not attribut.isvalid() : valid =0
                break
            # on teste les fils
            for fils in self.entites_fils:
                if not fils.isvalid(): valid = 0
                break
        self.valid = valid
        self.state = 'unchanged'
        if old_valid:
            if old_valid != self.valid : self.init_modif_up()
        return self.valid

    def init_modif_up(self):
        self.pere.state='modified'
      
    def report(self):
        self.cr.purge()
        self.cr.debut="Debut "+self.__class__.__name__+' : '+self.nom
        self.cr.fin = "Fin "+self.__class__.__name__+' : '+self.nom
        self.isvalid(cr='oui')
        for attribut in self.entites_attributs.values():
            self.cr.add(attribut.report())
        for fils in self.entites_fils :
            self.cr.add(fils.report())
        return self.cr
        
    def set_valeur_attribut(self,nom_attr,valeur):
        """
        Affecte la valeur 'valeur' à l'attribut de nom 'nom-attr'
        """
        # il faudra être prudent sur les changements de nom : interdire de changer
        # le nom d'un mot-clé qui serait utilisé dans une règle ???
        self.entites_attributs[nom_attr].valeur = valeur
        
    def addentite(self,name,pos):
        """
        Permet d'ajouter un nouveau fils a self
        """
        self.init_modif()
        if name == 'new_simp':
            objet = Accas.SIMP(typ=('bidon',))
        objet_cata = make_mc_cata(objet,self)
        self.entites_fils.insert(pos,objet_cata)
        return objet_cata

    def init_modif(self):
        self.state = 'modified'
        if hasattr(self,'pere'):
            self.pere.init_modif()

    def verif_nom(self,cr='non'):
        """
        Méthode appelée par EFICAS et ACCAS
        Booléenne : retourne 1 si l'attribut nom est valide, 0 sinon
        """
        if self.entites_attributs['nom'].valeur == '':
            if cr == 'oui' : self.cr.fatal("L'objet de type %s n'est pas nommé" %self.__class__.__name__)
            return 0
        return 1
    
    def verif_defaut(self,cr='non'):
        """
        Méthode de vérification de validité du défaut
        """
        defaut = self.get_valeur_attribut('defaut')
        if self.get_valeur_attribut('domaine_validite') == 'discret' :
            if defaut not in self.get_valeur_attribut('into'):
                if cr == 'oui' : self.cr.fatal("La valeur %s n'est pas autorisée" %str(defaut))
                return 0
            return 1
        else:
            if defaut == None : return 1
            typ = self.get_valeur_attribut('type')
            # on attend un TXM ?
            if 'TXM' in typ :
                if type(defaut) == types.StringType : return 1
            val_min = self.get_valeur_attribut('val_min')
            val_max = self.get_valeur_attribut('val_max')
            # on attend un reel ?
            if 'R' in typ :
                if type(defaut) == types.StringType:
                    try :
                        nb = string.atof(defaut)
                    except:
                        nb=None
                else:
                    nb = defaut
                if nb != None :
                    test = 1
                    if val_min != '**' : test = (nb >= val_min)
                    if val_max != '**' : test = test*(nb <= val_max)
                    if test : return 1
            # on attend un entier ?
            if 'I' in typ :
                if type(defaut)==types.StringType:
                    try:
                        nb = string.atoi(defaut)
                    except:
                        pass
                else:
                    nb = defaut
                if nb != None :
                    test = 1
                    if val_min != '**' : test = (nb >= val_min)
                    if val_max != '**' : test = test*(nb <= val_max)
                    if test : return 1
            # si on passe par là, c'est que l'on n'a pas su évaluer defaut
            if cr == 'oui' : self.cr.fatal("La valeur %s n'est pas une valeur permise" %str(defaut))
            return 0

    def verif_val_min(self,cr='non'):
        """
        Méthode de vérification de val_min.
        Booléenne : retourne 1 si val_min est valide, 0 sinon
        """
        val_min = self.get_valeur_attribut('val_min')
        if not val_min :
            if cr == 'oui' : self.cr.fatal('val_min ne peut valoir None')
            return 0
        if val_min == '**': return 1
        # val_min doit à ce stade être :
        # - soit un entier ou un réel
        # - soit une chaîne de caractères représentant un entier ou un réel (provient d'EFICAS)
        if type(val_min) == types.StringType :
            try :
                val_min = string.atoi(val_min)
            except:
                try:
                    val_min = string.atof(val_min)
                except:
                    if cr == 'oui' : self.cr.fatal("%s n'est ni un entier ni un réel" %str(val_min))
                    return 0
        # A ce stade, val_min doit être un entier ou un réel : on vérifie ...
        if type(val_min) not in (types.IntType,types.FloatType) :
            if cr == 'oui' : self.cr.fatal("%s n'est pas d'un type autorisé" %str(val_min))
            return 0
        # A ce stade valeur est un entier ou un réel : on peut comparer à val_max
        val_max = self.get_valeur_attribut('val_max')
        if val_max == '**' or val_min < val_max : return 1
        # erreur : val_min est supérieur à val_max !!!
        if cr == 'oui' : self.cr.fatal("%s n'est pas inférieur à %s" %(str(val_min),str(val_max)))
        return 0

    def verif_val_max(self,cr='non'):
        """
        Méthode de vérification de val_max.
        Booléenne : retourne 1 si val_max est valide, 0 sinon
        """
        val_max = self.get_valeur_attribut('val_max')
        if not val_max :
            if cr == 'oui' : self.cr.fatal('val_max ne peut valoir None')
            return 0
        if val_max == '**': return 1
        # val_max doit à ce stade être :
        # - soit un entier ou un réel
        # - soit une chaîne de caractères représentant un entier ou un réel (provient d'EFICAS)
        if type(val_max) == types.StringType :
            try :
                val_max = string.atoi(val_max)
            except:
                try:
                    val_max = string.atof(val_max)
                except:
                    if cr == 'oui' : self.cr.fatal("%s n'est ni un entier ni un réel" %str(val_max))
                    return 0
        # A ce stade, val_max doit être un entier ou un réel : on vérifie ...
        if type(val_max) not in (types.IntType,types.FloatType) :
            if cr == 'oui' : self.cr.fatal("%s n'est pas d'un type autorisé" %str(val_max))
            return 0
        # A ce stade valeur est un entier ou un réel : on peut comparer à val_max
        val_min = self.get_valeur_attribut('val_min')
        if val_min == '**' or val_min < val_max : return 1
        # erreur : val_min est supérieur à val_max !!!
        if cr == 'oui' : self.cr.fatal("%s n'est pas supérieur à %s" %(str(val_max),str(val_min)))
        return 0
    
class OPER_CATA(OBJET_CATA):
    attributs = ['ang','docu','fr','niveau','nom','op','op_init','reentrant','regles','repetable','sd_prod']
  
class PROC_CATA(OBJET_CATA):
    attributs = ['ang','docu','fr','niveau','nom','op','op_init','regles','repetable']

class MACRO_CATA(OBJET_CATA):
    attributs = ['ang','docu','fr','niveau','nom','op','op_init','reentrant','regles','repetable','sd_prod']
    
class BLOC_CATA(OBJET_CATA):
    attributs = ['ang','condition','docu','fr','nom','regles']

class FACT_CATA(OBJET_CATA):
    attributs=['ang','defaut','docu','fr','max','min','nom','regles','statut']

class SIMP_CATA(OBJET_CATA):
    attributs=['ang','defaut','docu','fr','homo','into','max','min','nom','position','statut','type','val_min','val_max']
    attributs_defauts={'ang':'','defaut':None,'fr':'','homo':1,'into':None,'max':1,'min':1,'nom' : '','position':'local',
                       'regles':None,'statut':'f','type':None,'val_min':'**','val_max':'**','docu':''}
                
    def build_entites_fils(self):
        pass

    def isvalid(self,cr='non'):
        """
        Mde appelpar l'externe (EFICAS et ACCAS).
        Boolne : retourne 1 si l'objet est valide, 0 sinon
        """
        if self.state == 'unchanged':
            return self.valid
        else:
            valid = 1
            valid = valid*self.verif_nom(cr=cr)
            valid = valid*self.verif_defaut(cr=cr)
            valid = valid*self.verif_val_min(cr=cr)*self.verif_val_max(cr=cr)
            if hasattr(self,'valid'):
                old_valid = self.valid
            else:
                old_valid = None
            self.valid = valid
            self.state='unchanged'
            if old_valid :
                if old_valid != self.valid : self.init_modif_up()
            return self.valid

class NIVEAU_CATA(OBJET_CATA):
  def __init__(self,objet,pere,nom):
    self.pere = pere
    self.nom = nom
    self.state = 'undetermined'
    self.cr = CR()
    self.objet = objet
    self.entites_fils=[]
    self.entites_attributs = {}

  def register(self,fils):
    """ 
        Enregistre la commande êµ¡pe :
         - si editmode = 0 : on est en mode relecture d'un fichier de commandes
         auquel cas on ajoute etape à¡¬a fin de la liste self.etapes
         - si editmode = 1 : on est en mode ajout d'êµ¡pe depuis eficas auquel cas
         cette mode ne fait rien, c'est addentité enregistre etape à¡¬a bonne place
         dans self.etapes 
    """
    self.entites_fils.append(fils)

  def unregister(self,etape):
    self.entites_fils.remove(etape)

  def isvalid(self,cr='non'):
    """ Mode boolne qui retourne 0 si le niveau est invalide, 1 sinon """
    if self.state == 'unchanged':
        return self.valid
    else:
        valid = 1
        if len(self.entites_fils) == 0:
            #valid = self.Accas.valide_vide
            valid = 1
        else:
            for commande in self.entites_fils :
                if hasattr(commande,'isvalid'):
                    if not commande.isvalid() :
                        valid = 0
                        break
                else:
                    print str(commande)," n'a pas de methode isvalid"
        if hasattr(self,'valid'):
            old_valid = self.valid
        else:
            old_valid = None
        self.valid = valid
        self.state='unchanged'
        if old_valid:
            if old_valid != self.valid : self.init_modif_up()
        return self.valid
            

class ATTR_CATA(OBJET_CATA):
    def __init__(self,nom,valeur=None):
        self.nom = nom
        self.valeur = valeur
        self.cr = CR()
        self.state='undetermined'
        self.entites_attributs={}
        self.entites_fils=()

    def isvalid(self,cr='non'):
        return 1

def isCMD(cmd):
   return isinstance(cmd,Accas.OPER) or isinstance(cmd,Accas.PROC) or isinstance(cmd,Accas.MACRO) or isinstance(cmd,Accas.FORM)

