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
"""
"""
# import généraux
import types,string,os,glob,imp,sys
from repr import Repr
from copy import copy,deepcopy

myrepr = Repr()
myrepr.maxstring = 100
myrepr.maxother = 100

class TreeItem:

    """Abstract class representing tree items.

    Methods should typically be overridden, otherwise a default action
    is used.

    """

    def __init__(self):
        """Constructor.  Do whatever you need to do."""

    def GetText(self):
        """Return text string to display."""

    def GetLabelText(self):
        """Return label text string to display in front of text (if any)."""

    expandable = None

    def _IsExpandable(self):
        """Do not override!  Called by TreeNode."""
        if self.expandable is None:
            self.expandable = self.IsExpandable()
        return self.expandable

    def IsExpandable(self):
        """Return whether there are subitems."""
        return 1

    def _GetSubList(self):
        """Do not override!  Called by TreeNode."""
        if not self.IsExpandable():
            return []
        sublist = self.GetSubList()
        if not sublist:
            self.expandable = 0
        return sublist

    def IsEditable(self):
        """Return whether the item's text may be edited."""

    def SetText(self, text):
        """Change the item's text (if it is editable)."""

    def GetIconName(self):
        """Return name of icon to be displayed normally."""

    def GetSelectedIconName(self):
        """Return name of icon to be displayed when selected."""

    def GetSubList(self):
        """Return list of items forming sublist."""

    def OnDoubleClick(self):
        """Called on a double-click on the item."""

class Delegate:
    def __init__(self, delegate=None):
        self.object = delegate
        self.__cache = {}

    def setdelegate(self, delegate):
        self.resetcache()
        self.object = delegate

    def getdelegate(self):
        return self.object

    def __getattr__(self, name):
        attr = getattr(self.object, name) # May raise AttributeError
        setattr(self, name, attr)
        self.__cache[name] = attr
        return attr

    def resetcache(self):
        for key in self.__cache.keys():
            try:
                delattr(self, key)
            except AttributeError:
                pass
        self.__cache.clear()

    def cachereport(self):
        keys = self.__cache.keys()
        keys.sort()
        print keys


class ObjectTreeItem(TreeItem,Delegate):
    def __init__(self, appli, labeltext, object, setfunction=None):
        self.labeltext = labeltext
        self.appli = appli
        Delegate.__init__(self,object)
        #self.object = object
        self.setfunction = setfunction
        self.expandable = 1
        self.init()

    def init(self):
        return

    def copy(self):
        """
        Crée un item copie de self
        """
        object = self.object.copy()
        appli = copy(self.appli)
        labeltext = copy(self.labeltext)
        fonction = deepcopy(self.setfunction)
        item = make_objecttreeitem(appli,labeltext,object,fonction)
        return item
    
    def isactif(self):
        if hasattr(self.object,'actif'):
            return self.object.actif
        else:
            return 1
    
    def GetLabelText(self):
        """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
        """
        # None --> fonte et couleur par défaut
        return self.labeltext,None,None

    #def get_attribut(self,nom_attribut) :
    #    """ 
    #       Retourne l'attribut de nom nom_attribut de l'objet sur lequel
    #       pointe self s'il existe, None sinon
    #    """
    #    return self.object.get_attribut(nom_attribut)

    def get_nature(self) :
        """ 
            Retourne la nature de l'item et de l'objet
        """ 
        return self.object.nature

    def get_regles(self):
        """ retourne les règles de l'objet pointé par self """
        return self.object.get_regles()
    
    def get_liste_mc_presents(self):
        """ Retourne la liste des mots-clés fils de l'objet pointé par self """
        return self.object.liste_mc_presents()
    
    def get_val(self):
        """ Retourne le nom de la valeur de l'objet pointé par self dans le cas
            où celle-ci est un objet (ASSD) """
        return self.object.getval()
    
    def get_definition(self):
        """ 
           Retourne l'objet definition de l'objet pointé par self 
        """
        return self.object.definition

    def get_liste_mc_ordonnee(self,liste,dico):
        """ retourne la liste ordonnée (suivant le catalogue) brute des mots-clés
            d'une entité composée dont le chemin complet est donné sous forme
            d'une liste du type :ETAPE + MCFACT ou MCBLOC + ...
            il faut encore réarranger cette liste (certains mots-clés déjà
            présents ne doivent plus être proposés, règles ...)"""
        return self.object.get_liste_mc_ordonnee(liste,dico)

    def get_liste_mc_ordonnee_brute(self,liste,dico):
        """
        retourne la liste ordonnée (suivant le catalogue) BRUTE des mots-clés
        d'une entité composée dont le chemin complet est donné sous forme
        d'une liste du type :ETAPE + MCFACT ou MCBLOC + ...
        """
        return self.object.get_liste_mc_ordonnee_brute(liste,dico)
   
    def get_genealogie(self):
        """
        Retourne la liste des noms des ascendants (noms de MCSIMP,MCFACT,MCBLOC ou ETAPE)
        de l'objet pointé par self
        """
        return self.object.get_genealogie()

    def get_index_child(self,nom_fils):
        """
        Retourne l'index dans la liste des fils de self du nouveau fils de nom nom_fils
        Nécessaire pour savoir à quelle position dans la liste des fils il faut ajouter
        le nouveau mot-clé
        """
        liste_noms_mc_ordonnee = self.get_liste_mc_ordonnee_brute(self.get_genealogie(),self.get_jdc().cata_ordonne_dico)
        liste_noms_mc_presents = self.object.liste_mc_presents()
        l=[]
        for nom in liste_noms_mc_ordonnee:
            if nom in liste_noms_mc_presents or nom == nom_fils:
                l.append(nom)
        # l contient les anciens mots-clés + le nouveau dans l'ordre
        return l.index(nom_fils)
        
    def get_nom_etape(self):
        """Retourne le nom de self """
        return self.object.get_nom_etape()

    def get_copie_objet(self):
        """ Retourne une copie de l'objet pointé par self """
        return self.object.copy()
    
    def get_position(self):
        """ Retourne la valeur de l'attribut position de l'objet pointé par self """
        definition = self.get_definition()
        try:
            return getattr(definition,'position')
        except AttributeError:
            return 'local'
        
    def get_nom(self):
        """ Retourne le nom de l'objet pointé par self """
        return self.object.nom

    def get_jdc(self):
        """ Retourne le jdc auquel appartient l'objet pointé par self """
        return self.object.jdc
        #return self.object.get_attribut('jdc')
    
    def get_valeur(self):
        """ Retourne la valeur de l'objet pointé par self """
        return self.object.valeur

    def get_cr(self):
        """ Retourne le compte-rendu CR de self """
        return self.object.report()

    def get_objet_commentarise(self):
        """
        Cette méthode retourne un objet commentarisé
        représentatif de self.object
        --> à surcharger par les différents items
        """
        pass
        
    def isvalid(self):
        """ Retourne 1 si l'objet pointé par self est valide, 0 sinon"""
        return self.object.isvalid()

    def iscopiable(self):
        """
        Retourne 1 si l'objet est copiable, 0 sinon
        Par défaut retourne 0
        """
        return 0
    
    def isMCList(self):
        """ Retourne 1 si l'objet pointé par self est une MClist, 0 sinon"""
        #if isinstance(self.object,MCList) :
        if self.object.__class__.__name__ == 'MCList':
            return 1
        else :
            return 0

    def isCommande(self):
        """
        Retourne 1 si l'objet pointé par self est une Commande, 0 sinon
        """
        return 0

    def isJdc(self):
        """
        Retourne 1 si l'objet pointé par self est un JDC, 0 sinon
        """
        return 0

    def isMCFact(self):
        """
        Retourne 1 si l'objet pointé par self est un MCFact, 0 sinon
        """
        return 0
    
    def get_mc_presents(self):
        """ Retourne le dictionnaire des mots-clés présents de l'objet pointé par self """
        return self.object.dict_mc_presents()

    def verif_condition_regles(self,l_mc_presents):
        return self.object.verif_condition_regles(l_mc_presents)

    def get_fr(self):
        """ Retourne le fr de l'objet pointé par self """
        return self.object.get_fr()

    def get_docu(self):
        """ Retourne la clé de doc de l'objet pointé par self """
        return self.object.get_docu()

    def set_valeur(self,new_valeur,evaluation='oui'):
        """ Remplace la valeur de l'objet pointé par self par new_valeur """
        return self.object.set_valeur(new_valeur,evaluation=evaluation)
        
    def GetText(self):
        return myrepr.repr(self.object)
    
    def GetIconName(self):
        if not self.IsExpandable():
            return "python"

    def IsEditable(self):
        return self.setfunction is not None

    def SetText(self, text):
        try:
            value = eval(text)
            self.setfunction(value)
        except:
            pass
# Modif de ma part CCar : je ne comprend pas a quoi ca sert
# ca parait meme incorrect
      #  else:
      #      self.object = value

    def IsExpandable(self):
        return 1
        
    def GetSubList(self):
        keys = dir(self.object)
        sublist = []
        for key in keys:
            try:
                value = getattr(self.object, key)
            except AttributeError:
                continue
            item = make_objecttreeitem(
                self.appli,
                str(key) + " =",
                value,
                lambda value, key=key, object=self.object:
                    setattr(object, key, value))
            sublist.append(item)
        return sublist

    def wait_fichier_init(self):
        """ Retourne 1 si l'object pointé par self attend un fichier d'initialisation
        (ex: macros POURSUITE et INCLUDE de Code_Aster), 0 SINON """
        return self.object.definition.fichier_ini

    def make_objecttreeitem(self,appli,labeltext, object, setfunction=None):
        """
           Cette methode, globale pour les objets de type item, permet de construire et de retourner un objet
           de type item associé à l'object passé en argument.
        """
        c = gettreeitem(object)
        return c(appli,labeltext, object, setfunction)

class AtomicObjectTreeItem(ObjectTreeItem):
    def IsExpandable(self):
        return 0

class SequenceTreeItem(ObjectTreeItem):
    def IsExpandable(self):
        return len(self.object) > 0

    def __len__(self) :
        return len(self.object)
   
    def keys(self):
        return range(len(self.object))

    def GetIconName(self):
        if self.object.isvalid():
          return "ast-green-los"
        elif self.object.isoblig():
          return "ast-red-los"
        else:
          return "ast-yel-los"

    def ajout_possible(self):
        return self.object.ajout_possible()

    def get_index(self,child):
        """ Retourne le numéro de child dans la liste des enfants de self """
        return self.object.get_index(child.object)

    def GetText(self):
      return  "    "

    def additem(self,obj,pos):
        # XXX Passer par addentite  de MCList ???
        self.object.insert(pos,obj)
        item = self.make_objecttreeitem(self.appli, obj.nom + ":", obj)
        return item

    def suppitem(self,item):
        if not self.object.isMCList():return 1
        try :
            self.object.remove(item.object)
            # la liste peut être retournée vide !
            message = "Mot-clé " + item.object.nom + " supprimé"
            self.appli.affiche_infos(message)
            return 1
        except:
            return 0

    def GetSubList(self):
        sublist = []
        for obj in self.object.data:
            def setfunction(value, object=obj):
                object = value
            item = make_objecttreeitem(self.appli, obj.nom + ":", obj, setfunction)
            sublist.append(item)
        return sublist

def gettreeitem(object):
    """
       Cette fonction retourne la classe item associée à l'objet object.
       Cette classe item dépend bien sûr de la nature de object, d'où
       l'interrogation du dictionnaire composants
    """
    if type(object) == types.InstanceType:
      # On cherche d abord dans les composants (plugins)
      try:
        return composants[object.__class__]
      except:
        # On cherche une eventuelle classe heritee (aleatoire car sans ordre)
        for e in composants.keys():
          if isinstance(object,e):return composants[e]
    # On n'a rien trouve dans les composants
    return ObjectTreeItem

def charger_composants():
    """
        Cette fonction a pour but de charger tous les modules composants graphiques
        (fichiers compo*.py dans le même répertoire que ce module )
        et de remplir le dictionnaire composants utilisé par make_objecttreeitem
    """
    composants={}
    repertoire=os.path.dirname(__file__)
    listfich=glob.glob(os.path.join(repertoire, "compo*.py"))
    for fichier in listfich:
        m= os.path.basename(fichier)[:-3]
        module=__import__(m,globals(),locals())
        composants[module.objet]=module.treeitem
    return composants

def make_objecttreeitem(appli,labeltext, object, setfunction=None):
    """
       Cette fonction permet de construire et de retourner un objet
       de type item associé à l'object passé en argument.
    """
    c = gettreeitem(object)
    return c(appli,labeltext, object, setfunction)

# Dictionnaire {object : item} permettant d'associer un item à un object
# Ce dictionnaire est renseigné par la méthode charger_composants 
composants = charger_composants()

