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
       d'un MCBLOC ou d'un MCFACT appartenant � une MCList : 
       utilis�e pour l'affichage dans l'arbre
    """
    objet = self.parent.get_child(self.nom)
    # objet peut-�tre self ou une MCList qui contient self ...
    if isinstance(objet,MCList) :
      index = objet.get_index(self)+1 # + 1 � cause de la num�rotation qui commence � 0
      label = self.nom +'_'+`index`+':'
      return label
    else:
      return self.nom

  def get_genealogie(self):
    """ 
        Retourne la liste des noms des ascendants (noms de MCSIMP,MCFACT,MCBLOC
        ou ETAPE) de self jusqu'au premier objet etape rencontr�
    """
    l=[]
    objet = self
    while objet.nature != 'JDC' :
      if not objet.isMCList() :
        l.append(string.strip(objet.nom))
      else :
        pass
      # Si objet.etape == etape c'est que objet est l'�tape origine de la g�n�alogie
      if objet.etape == objet: break
      objet = objet.parent
    l.reverse()
    return l

  def get_liste_mc_ordonnee(self,liste,dico):
    """
       Retourne la liste ordonn�e (suivant le catalogue) des mots-cl�s
       d'une entit� compos�e dont le chemin complet est donn� sous forme
       d'une liste du type :ETAPE + MCFACT ou MCBLOC + ...
       il faut encore r�arranger cette liste (certains mots-cl�s d�j�
       pr�sents ne doivent plus �tre propos�s, r�gles ...)
    """
    return self.filtre_liste_mc(self.get_liste_mc_ordonnee_brute(liste,dico))

  def get_liste_mc_ordonnee_brute(self,liste,dico):
    """
       Retourne la liste ordonn�e (suivant le catalogue) BRUTE des mots-cl�s
       d'une entit� compos�e dont le chemin complet est donn� sous forme
       d'une liste du type :ETAPE + MCFACT ou MCBLOC + ...
    """
    for arg in liste:
        objet_cata = dico[arg]
        dico=objet_cata.dico
    return objet_cata.liste

  def filtre_liste_mc(self,liste_brute):
    """ 
       Cette m�thode est appel�e par EFICAS afin de pr�senter � 
       l'utilisateur la liste des enfants possibles de self actualis�e 
       en fonction du contexte de self. En clair, sont supprim�s de la
       liste des possibles (fournie par la d�finition), les mots-cl�s
       exclus par les r�gles de self et les mots-cl�s ne pouvant plus 
       �tre r�p�t�s
    """
    liste = copy(liste_brute)
    liste_mc_presents = self.liste_mc_presents()
    # on enl�ve les mots-cl�s non permis par les r�gles
    for regle in self.definition.regles:
       # la m�thode purge_liste est � d�velopper pour chaque r�gle qui
       # influe sur la liste de choix � proposer � l'utilisateur
       # --> EXCLUS,UN_PARMI,PRESENT_ABSENT
       liste = regle.purge_liste(liste,liste_mc_presents)
    # on enl�ve les mots-cl�s dont l'occurrence est d�j� atteinte
    liste_copy = copy(liste)
    for k in liste_copy:
      objet = self.get_child(k,restreint = 'oui')
      if objet != None :
        # l'objet est d�j� pr�sent : il faut distinguer plusieurs cas
        if isinstance(objet,MCSIMP):
          # un mot-cl� simple ne peut pas �tre r�p�t�
          liste.remove(k)
        elif isinstance(objet,MCBLOC):
          # un bloc conditionnel ne doit pas appara�tre dans la liste de choix
          liste.remove(k)
        elif isinstance(objet,MCFACT):
          # un mot-cl� facteur ne peut pas �tre r�p�t� plus de self.max fois
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
          #XXX CCAR : les MCNUPLET ne sont pas trait�s
          if CONTEXT.debug : print '   ',k,' est un objet de type inconnu :',type(objet)
      else :
        # l'objet est absent : on enl�ve de la liste les blocs
        if self.definition.entites[k].statut=='c' :
          liste.remove(k)
        if self.definition.entites[k].label=='BLOC':
          liste.remove(k)
    return liste

  def liste_mc_presents(self):
    """ 
       Retourne la liste des noms des mots-cl�s fils de self pr�sents construite
       � partir de self.mc_liste 
    """
    l=[]
    for v in self.mc_liste:
      k=v.nom
      l.append(k)
    return l

  def ordonne_liste_mc(self,liste_mc_a_ordonner,liste_noms_mc_ordonnee):
    """
        Retourne liste_mc_a_ordonner ordonn�e suivant l'ordre 
        donn� par liste_noms_mc_ordonnee
    """
    liste = []
    # on transforme liste_a_ordonner en un dictionnaire (plus facile � consulter)
    d_mc = {}
    for mc in liste_mc_a_ordonner:
      d_mc[mc.nom]=mc
    # on construit la liste des objets ordonn�s
    for nom_mc in liste_noms_mc_ordonnee:
      if d_mc.has_key(nom_mc):
        liste.append(d_mc.get(nom_mc))
    # on la retourne
    return liste

  def suppentite(self,objet) :
    """ 
        Supprime le fils 'objet' de self : 
        Retourne 1 si la suppression a pu �tre effectu�e,
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
    return self.definition.statut=='o'

  def addentite(self,name,pos=None):
      """ 
          Ajoute le mot-cle name � la liste des mots-cles de
          l'objet MCCOMPOSE
      """
      self.init_modif()
      if type(name)==types.StringType :
        if self.ispermis(name) == 0 : return 0
        objet=self.definition.entites[name](val=None,nom=name,parent=self)
        if hasattr(objet.definition,'position'):
          if objet.definition.position == 'global' :
            self.append_mc_global(objet)
          elif objet.definition.position == 'global_jdc' :
            self.append_mc_global_jdc(objet)
      else :
        objet = name
      # si un objet de m�me nom est d�j� pr�sent dans la liste
      # et si l'objet est r�p�table
      # il faut cr�er une MCList et remplacer l'objet de la liste
      # par la MCList
      test1 = objet.isrepetable()
      old_obj = self.get_child(objet.nom,restreint = 'oui')
      test2 = self.ispermis(objet)
      #print "test1,test2=",test1,test2
      if test1 == 0 and old_obj :
        self.jdc.send_message("L'objet %s ne peut pas �tre r�p�t�" %objet.nom)
        self.fin_modif()
        return 0
      if test2 == 0:
        self.jdc.send_message("L'objet %s ne peut �tre un fils de %s" %(objet.nom,self.nom))
        self.fin_modif()
        return 0
      if test1 :
        if old_obj :
          #if not isinstance(old_obj,MCList):
          if not old_obj.isMCList():
            # un objet de m�me nom existe d�j� mais ce n'est pas une MCList
            # Il faut en cr�er une 
            # L'objet existant (old_obj) est certainement un MCFACT 
            # qui pointe vers un constructeur
            # de MCList : definition.liste_instance
            #print "un objet de m�me type existe d�j�"
            index = self.mc_liste.index(old_obj)
            #XXX remplac� par definition.list_instance : new_obj = MCList()
            new_obj = old_obj.definition.list_instance()
            new_obj.init(objet.nom,self)
            new_obj.append(old_obj)
            new_obj.append(objet)
            self.mc_liste.remove(old_obj)
            self.mc_liste.insert(index,new_obj)
            self.fin_modif()
            return new_obj
          else :
            # une liste d'objets de m�me type existe d�j�
            #print "une liste d'objets de m�me type existe d�j�"
            old_obj.append(objet)
            self.fin_modif()
            return old_obj
      if pos == None :
        self.mc_liste.append(objet)
      else :
        self.mc_liste.insert(pos,objet)
      self.fin_modif()
      return objet

  def ispermis(self,fils):
    """ 
        Retourne 1 si l'objet de nom nom_fils 
        est bien permis, cad peut bien �tre un fils de self, 
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
      # on veut savoir si l'objet peut bien �tre un fils de self :
      # la v�rification du nom de suffit pas (plusieurs commandes
      # ont le m�me mot-cl� facteur AFFE ... et c'est l'utilisateur
      # qui choisit le p�re d'o� un risque d'erreur)
      if not self.definition.entites.has_key(fils.nom):
        return 0
      else:
        if fils.parent.nom != self.nom : return 0
      return 1

  def liste_mc_presents(self):
    """ 
         Retourne la liste des noms des mots-cl�s fils de self pr�sents 
         construite � partir de self.mc_liste 
    """
    l=[]
    for v in self.mc_liste:
      k=v.nom
      l.append(k)
    return l

  def delete_concept(self,sd):
    """ 
        Inputs :
           sd=concept detruit
        Fonction :
           Mettre a jour les fils de l objet suite � la disparition du
           concept sd
           Seuls les mots cles simples MCSIMP font un traitement autre que 
           de transmettre aux fils
    """
    for child in self.mc_liste :
      child.delete_concept(sd)

  def delete_mc_global(self,mc):
    """ 
        Supprime le mot-cl� mc de la liste des mots-cl�s globaux de l'�tape 
    """
    etape = self.get_etape()
    if etape :
      nom = mc.nom
      del etape.mc_globaux[nom]

  def delete_mc_global_jdc(self,mc):
    """ 
        Supprime le mot-cl� mc de la liste des mots-cl�s globaux du jdc 
    """
    nom = mc.nom
    del self.jdc.mc_globaux[nom]

  def copy(self):
    """ Retourne une copie de self """
    objet = self.makeobjet()
    # FR : attention !!! avec makeobjet, objet a le m�me parent que self
    # ce qui n'est pas du tout bon dans le cas d'une copie !!!!!!!
    # FR : peut-on passer par l� autrement que dans le cas d'une copie ???
    # FR --> je suppose que non
    objet.parent = None
    objet.valeur = copy(self.valeur)
    objet.val = copy(self.val)
    objet.mc_liste=[]
    for obj in self.mc_liste:
      new_obj = obj.copy()
      new_obj.parent = objet
      objet.mc_liste.append(new_obj)
    return objet

  def get_sd_utilisees(self):
    """ 
        Retourne la liste des concepts qui sont utilis�s � l'int�rieur de self
        ( comme valorisation d'un MCS) 
    """
    l=[]
    for child in self.mc_liste:
      l.extend(child.get_sd_utilisees())
    return l

  def get_liste_mc_inconnus(self):
     """
     Retourne la liste des mots-cl�s inconnus dans self
     """
     l_mc = []
     if self.reste_val != {}:
        for k,v in self.reste_val.items() :
	    l_mc.append([self,k,v])
     for child in self.mc_liste :
        if child.isvalid() : continue
        l_child = child.get_liste_mc_inconnus()
	if l_child :
	   l = [self]
	   l.extend(l_child)
	   l_mc.append(l)
     return l_mc

  def verif_condition_bloc(self):
    """ 
        Evalue les conditions de tous les blocs fils possibles 
        (en fonction du catalogue donc de la d�finition) de self
        et retourne deux listes :
        - la premi�re contient les noms des blocs � rajouter
        - la seconde contient les noms des blocs � supprimer
    """
    liste_ajouts = []
    liste_retraits = []
    dict = self.cree_dict_valeurs(self.mc_liste)
    for k,v in self.definition.entites.items():
      #dict = self.cree_dict_valeurs(self.mc_liste)
      if v.label=='BLOC' :
        if v.verif_presence(dict) :
          # le bloc doit �tre pr�sent
          if not self.get_child(k,restreint = 'oui'):
            # le bloc n'est pas pr�sent et il doit �tre cr��
            liste_ajouts.append(k)
        else :
          # le bloc doit �tre absent
          if self.get_child(k,restreint = 'oui'):
            # le bloc est pr�sent : il faut l'enlever
            liste_retraits.append(k)
    return liste_ajouts,liste_retraits

