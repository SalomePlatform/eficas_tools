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
import string,types
from copy import copy

from Noyau.N_MCLIST import MCList
from Noyau.N_MCSIMP import MCSIMP
from Noyau.N_MCFACT import MCFACT
from Noyau.N_MCBLOC import MCBLOC
import I_OBJECT

class MCCOMPO(I_OBJECT.OBJECT):
  def getlabeltext(self):
    """ 
       Retourne le label de self suivant qu'il s'agit d'un MCFACT, 
       d'un MCBLOC ou d'un MCFACT appartenant à une MCList : 
       utilisée pour l'affichage dans l'arbre
    """
    objet = self.parent.get_child(self.nom)
    # objet peut-être self ou une MCList qui contient self ...
    if isinstance(objet,MCList) :
      index = objet.get_index(self)+1 # + 1 à cause de la numérotation qui commence à 0
      label = self.nom +'_'+`index`+':'
      return label
    else:
      return self.nom

  def get_liste_mc_ordonnee(self,liste,dico):
    """
       Retourne la liste ordonnée (suivant le catalogue) des mots-clés
       d'une entité composée dont le chemin complet est donné sous forme
       d'une liste du type :ETAPE + MCFACT ou MCBLOC + ...
       il faut encore réarranger cette liste (certains mots-clés déjà
       présents ne doivent plus être proposés, règles ...)
    """
    return self.filtre_liste_mc(self.get_liste_mc_ordonnee_brute(liste,dico))

  def get_liste_mc_ordonnee_brute(self,liste,dico):
    """
       Retourne la liste ordonnée (suivant le catalogue) BRUTE des mots-clés
       d'une entité composée dont le chemin complet est donné sous forme
       d'une liste du type :ETAPE + MCFACT ou MCBLOC + ...
    """
    for arg in liste:
        objet_cata = dico[arg]
        dico=objet_cata.entites
    return objet_cata.ordre_mc

  def filtre_liste_mc(self,liste_brute):
    """ 
       Cette méthode est appelée par EFICAS afin de présenter à 
       l'utilisateur la liste des enfants possibles de self actualisée 
       en fonction du contexte de self. En clair, sont supprimés de la
       liste des possibles (fournie par la définition), les mots-clés
       exclus par les règles de self et les mots-clés ne pouvant plus 
       être répétés
    """
    liste = copy(liste_brute)
    liste_mc_presents = self.liste_mc_presents()
    # on enlève les mots-clés non permis par les règles
    for regle in self.definition.regles:
       # la méthode purge_liste est à développer pour chaque règle qui
       # influe sur la liste de choix à proposer à l'utilisateur
       # --> EXCLUS,UN_PARMI,PRESENT_ABSENT
       liste = regle.purge_liste(liste,liste_mc_presents)
    # on enlève les mots-clés dont l'occurrence est déjà atteinte
    liste_copy = copy(liste)
    for k in liste_copy:
      objet = self.get_child(k,restreint = 'oui')
      if objet != None :
        # l'objet est déjà présent : il faut distinguer plusieurs cas
        if isinstance(objet,MCSIMP):
          # un mot-clé simple ne peut pas être répété
          liste.remove(k)
        elif isinstance(objet,MCBLOC):
          # un bloc conditionnel ne doit pas apparaître dans la liste de choix
          liste.remove(k)
        elif isinstance(objet,MCFACT):
          # un mot-clé facteur ne peut pas être répété plus de self.max fois
          if objet.definition.max == 1:
            liste.remove(k)
        elif isinstance(objet,MCList):
          try :
            nb_occur_maxi = objet[0].definition.max
            if len(objet) >= nb_occur_maxi:
              liste.remove(k)
          except:
            pass
        else :
          #XXX CCAR : les MCNUPLET ne sont pas traités
          if CONTEXT.debug : print '   ',k,' est un objet de type inconnu :',type(objet)
      else :
        # l'objet est absent : on enlève de la liste les blocs
        if self.definition.entites[k].statut=='c' :
          liste.remove(k)
        if self.definition.entites[k].label=='BLOC':
          liste.remove(k)
    # Pour corriger les exces qui pourraient etre commis dans la methode purge_liste
    # des regles, on essaie de compenser comme suit :
    # on ajoute les mots cles facteurs presents dont l'occurence n'est pas atteinte
    for k in liste_mc_presents:
      if k in liste:continue
      objet = self.get_child(k,restreint = 'oui')
      if isinstance(objet,MCFACT):
          # un mot-clé facteur ne peut pas être répété plus de self.max fois
          if objet.definition.max > 1:
             liste.append(k)
      elif isinstance(objet,MCList):
          nb_occur_maxi = objet[0].definition.max
          if len(objet) < nb_occur_maxi:
              liste.append(k)
    return liste

  def liste_mc_presents(self):
    """ 
       Retourne la liste des noms des mots-clés fils de self présents construite
       à partir de self.mc_liste 
    """
    l=[]
    for v in self.mc_liste:
      k=v.nom
      l.append(k)
    return l

  def ordonne_liste_mc(self,liste_mc_a_ordonner,liste_noms_mc_ordonnee):
    """
        Retourne liste_mc_a_ordonner ordonnée suivant l'ordre 
        donné par liste_noms_mc_ordonnee
    """
    liste = []
    # on transforme liste_a_ordonner en un dictionnaire (plus facile à consulter)
    d_mc = {}
    for mc in liste_mc_a_ordonner:
      d_mc[mc.nom]=mc
    # on construit la liste des objets ordonnés
    for nom_mc in liste_noms_mc_ordonnee:
      if d_mc.has_key(nom_mc):
        liste.append(d_mc.get(nom_mc))
    # on la retourne
    return liste

  def suppentite(self,objet) :
    """ 
        Supprime le fils 'objet' de self : 
        Retourne 1 si la suppression a pu être effectuée,
        Retourne 0 dans le cas contraire
    """
    self.init_modif()
    if not objet in self.mc_liste:
       # Impossible de supprimer objet. Il n'est pas dans mc_liste
       self.fin_modif()
       return 0

    try :
      if hasattr(objet.definition,'position'):
          if objet.definition.position == 'global' :
            self.delete_mc_global(objet)
          elif objet.definition.position == 'global_jdc' :
            self.delete_mc_global_jdc(objet)
      self.mc_liste.remove(objet)
      self.fin_modif()
      return 1
    except:
      self.fin_modif()
      return 0

  def isoblig(self):
      return 0

  def addentite(self,name,pos=None):
      """ 
          Ajoute le mot-cle name à la liste des mots-cles de
          l'objet MCCOMPOSE
      """
      self.init_modif()
      if type(name)==types.StringType :
        # on est en mode création d'un motcle 
        if self.ispermis(name) == 0 : return 0
        objet=self.definition.entites[name](val=None,nom=name,parent=self)
        if hasattr(objet.definition,'position'):
          if objet.definition.position == 'global' :
            self.append_mc_global(objet)
          elif objet.definition.position == 'global_jdc' :
            self.append_mc_global_jdc(objet)
      else :
        # dans ce cas on est en mode copie d'un motcle
        objet = name
	objet.verif_existence_sd()
      # si un objet de même nom est déjà présent dans la liste
      # et si l'objet est répétable
      # il faut créer une MCList et remplacer l'objet de la liste
      # par la MCList
      test1 = objet.isrepetable()
      old_obj = self.get_child(objet.nom,restreint = 'oui')
      test2 = self.ispermis(objet)
      #print "test1,test2=",test1,test2
      if test1 == 0 and old_obj :
        self.jdc.send_message("L'objet %s ne peut pas être répété" %objet.nom)
        self.fin_modif()
        return 0
      if test2 == 0:
        self.jdc.send_message("L'objet %s ne peut être un fils de %s" %(objet.nom,self.nom))
        self.fin_modif()
        return 0
      if test1 :
        if old_obj :
          #if not isinstance(old_obj,MCList):
          if not old_obj.isMCList():
            # un objet de même nom existe déjà mais ce n'est pas une MCList
            # Il faut en créer une 
            # L'objet existant (old_obj) est certainement un MCFACT 
            # qui pointe vers un constructeur
            # de MCList : definition.liste_instance
            #print "un objet de même type existe déjà"
            index = self.mc_liste.index(old_obj)
            #XXX remplacé par definition.list_instance : new_obj = MCList()
            new_obj = old_obj.definition.list_instance()
            new_obj.init(objet.nom,self)
            new_obj.append(old_obj)
            new_obj.append(objet)
            # Il ne faut pas oublier de reaffecter le parent d'obj
            objet.reparent(self)
            self.mc_liste.remove(old_obj)
            self.mc_liste.insert(index,new_obj)
            self.fin_modif()
            return new_obj
          else :
            # une liste d'objets de même type existe déjà
            #print "une liste d'objets de même type existe déjà"
            old_obj.append(objet)
            # Il ne faut pas oublier de reaffecter le parent d'obj
            objet.reparent(self)
            self.fin_modif()
            return old_obj
      if pos == None :
        self.mc_liste.append(objet)
      else :
        self.mc_liste.insert(pos,objet)
      # Il ne faut pas oublier de reaffecter le parent d'obj (si copie)
      objet.reparent(self)
      self.fin_modif()
      return objet

  def ispermis(self,fils):
    """ 
        Retourne 1 si l'objet de nom nom_fils 
        est bien permis, cad peut bien être un fils de self, 
        Retourne 0 sinon 
    """
    if type(fils) == types.StringType :
      # on veut juste savoir si self peut avoir un fils de nom 'fils'
      if self.definition.entites.has_key(fils):
        return 1
      else :
        return 0
    elif type(fils) == types.InstanceType:
      # fils est un objet (commande,mcf,mclist)
      # on est dans le cas d'une tentative de copie de l'objet
      # on veut savoir si l'objet peut bien être un fils de self :
      # la vérification du nom de suffit pas (plusieurs commandes
      # ont le même mot-clé facteur AFFE ... et c'est l'utilisateur
      # qui choisit le père d'où un risque d'erreur)
      if not self.definition.entites.has_key(fils.nom):
        return 0
      else:
        if fils.parent.nom != self.nom : return 0
      return 1

  def liste_mc_presents(self):
    """ 
         Retourne la liste des noms des mots-clés fils de self présents 
         construite à partir de self.mc_liste 
    """
    l=[]
    for v in self.mc_liste:
      k=v.nom
      l.append(k)
    return l

  def delete_concept(self,sd):
    """ 
        Inputs :
           - sd=concept detruit
        Fonction :
        Mettre a jour les fils de l objet suite à la disparition du
        concept sd
        Seuls les mots cles simples MCSIMP font un traitement autre que 
        de transmettre aux fils
    """
    for child in self.mc_liste :
      child.delete_concept(sd)

  def replace_concept(self,old_sd,sd):
    """
        Inputs :
           - old_sd=concept remplace
           - sd = nouveau concept
        Fonction :
        Mettre a jour les fils de l objet suite au remplacement  du
        concept old_sd
    """
    for child in self.mc_liste :
      child.replace_concept(old_sd,sd)

  def delete_mc_global(self,mc):
    """ 
        Supprime le mot-clé mc de la liste des mots-clés globaux de l'étape 
    """
    etape = self.get_etape()
    if etape :
      nom = mc.nom
      del etape.mc_globaux[nom]

  def delete_mc_global_jdc(self,mc):
    """ 
        Supprime le mot-clé mc de la liste des mots-clés globaux du jdc 
    """
    nom = mc.nom
    del self.jdc.mc_globaux[nom]

  def get_liste_mc_inconnus(self):
     """
     Retourne la liste des mots-clés inconnus dans self
     """
     l_mc = []
     if self.reste_val != {}:
        for k,v in self.reste_val.items() :
	    l_mc.append([self,k,v])
     for child in self.mc_liste :
        if child.isvalid() : continue
        l_child = child.get_liste_mc_inconnus()
        for mc in l_child:
	   l = [self]
	   l.extend(mc)
	   l_mc.append(l)
     return l_mc

  def verif_condition_bloc(self):
    """ 
        Evalue les conditions de tous les blocs fils possibles 
        (en fonction du catalogue donc de la définition) de self
        et retourne deux listes :
          - la première contient les noms des blocs à rajouter
          - la seconde contient les noms des blocs à supprimer
    """
    liste_ajouts = []
    liste_retraits = []
    dict = self.cree_dict_condition(self.mc_liste)
    for k,v in self.definition.entites.items():
      if v.label=='BLOC' :
        globs= self.jdc and self.jdc.condition_context or {}
        if v.verif_presence(dict,globs):
          # le bloc doit être présent
          if not self.get_child(k,restreint = 'oui'):
            # le bloc n'est pas présent et il doit être créé
            liste_ajouts.append(k)
        else :
          # le bloc doit être absent
          if self.get_child(k,restreint = 'oui'):
            # le bloc est présent : il faut l'enlever
            liste_retraits.append(k)
    return liste_ajouts,liste_retraits

  def verif_existence_sd(self):
     """
        Vérifie que les structures de données utilisées dans self existent bien dans le contexte
	avant étape, sinon enlève la référence à ces concepts
     """
     for motcle in self.mc_liste :
         motcle.verif_existence_sd()
