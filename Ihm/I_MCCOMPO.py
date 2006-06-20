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
"""
"""
import string,types,sys
from copy import copy
import traceback

from Noyau.N_MCLIST import MCList
from Noyau.N_MCSIMP import MCSIMP
from Noyau.N_MCFACT import MCFACT
from Noyau.N_MCBLOC import MCBLOC
import I_OBJECT

import CONNECTOR

class MCCOMPO(I_OBJECT.OBJECT):
  def getlabeltext(self):
    """ 
       Retourne le label de self 
       utilis� pour l'affichage dans l'arbre
    """
    return self.nom

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
        dico=objet_cata.entites
    return objet_cata.ordre_mc

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
    # Pour corriger les exces qui pourraient etre commis dans la methode purge_liste
    # des regles, on essaie de compenser comme suit :
    # on ajoute les mots cles facteurs presents dont l'occurence n'est pas atteinte
    for k in liste_mc_presents:
      if k in liste:continue
      objet = self.get_child(k,restreint = 'oui')
      if isinstance(objet,MCFACT):
          # un mot-cl� facteur ne peut pas �tre r�p�t� plus de self.max fois
          if objet.definition.max > 1:
             liste.append(k)
      elif isinstance(objet,MCList):
          nb_occur_maxi = objet[0].definition.max
          if len(objet) < nb_occur_maxi:
              liste.append(k)
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

  def get_index_child(self,nom_fils):
      """
        Retourne l'index dans la liste des fils de self du nouveau fils de nom nom_fils
        Permet de savoir � quelle position il faut ajouter un nouveau mot-cl�
      """
      cata_ordonne = self.jdc.cata_ordonne_dico
      liste_noms_mc_ordonnee = self.get_liste_mc_ordonnee_brute(self.get_genealogie(),cata_ordonne)
      liste_noms_mc_presents = self.liste_mc_presents()
      index=0
      for nom in liste_noms_mc_ordonnee:
          if nom == nom_fils:break
          if nom not in liste_noms_mc_presents :continue
          index=index+1
      return index
          
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
    if not objet in self.mc_liste:
       # Impossible de supprimer objet. Il n'est pas dans mc_liste
       return 0

    self.init_modif()
    self.mc_liste.remove(objet)
    CONNECTOR.Emit(self,"supp",objet)
    objet.delete_mc_global()
    objet.update_condition_bloc()
    objet.supprime()
    self.fin_modif()
    return 1

  def isoblig(self):
      return 0

  def addentite(self,name,pos=None):
      """ 
          Ajoute le mot-cle name � la liste des mots-cles de
          l'objet MCCOMPOSE
      """
      self.init_modif()
      if type(name)==types.StringType :
        # on est en mode cr�ation d'un motcle 
        if self.ispermis(name) == 0 : return 0
        objet=self.definition.entites[name](val=None,nom=name,parent=self)
      else :
        # dans ce cas on est en mode copie d'un motcle
        objet = name
        # Appel de la methode qui fait le menage dans les references
        # sur les concepts produits (verification que les concepts existent
        # dans le contexte de la commande courante).
        objet.verif_existence_sd()

      # On verifie que l'ajout d'objet est autorise
      if self.ispermis(objet) == 0:
        self.jdc.send_message("L'objet %s ne peut �tre un fils de %s" %(objet.nom,
                                                                        self.nom))
        self.fin_modif()
        return 0

      # On cherche s'il existe deja un mot cle de meme nom
      old_obj = self.get_child(objet.nom,restreint = 'oui')
      if not old_obj :
         # on normalize l'objet
         objet=objet.normalize()
         # Le mot cle n'existe pas encore. On l'ajoute a la position
         # demandee (pos)
         if pos == None :
           self.mc_liste.append(objet)
         else :
           self.mc_liste.insert(pos,objet)
         # Il ne faut pas oublier de reaffecter le parent d'obj (si copie)
         objet.reparent(self)
         CONNECTOR.Emit(self,"add",objet)
         objet.update_mc_global()
         objet.update_condition_bloc()
         self.fin_modif()
         return objet
      else:
         # Le mot cle existe deja. Si le mot cle est repetable,
         # on cree une liste d'objets. Dans le cas contraire,
         # on emet un message d'erreur.
         if not old_obj.isrepetable():
            self.jdc.send_message("L'objet %s ne peut pas �tre r�p�t�" %objet.nom)
            self.fin_modif()
            return 0
         else:
            # une liste d'objets de m�me type existe d�j�
            old_obj.addentite(objet)
            self.fin_modif()
            return old_obj

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

  def update_concept(self,sd):
    for child in self.mc_liste :
        child.update_concept(sd)

  def delete_concept(self,sd):
    """ 
        Inputs :
           - sd=concept detruit
        Fonction :
        Mettre a jour les fils de l objet suite � la disparition du
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
        for mc in l_child:
           l = [self]
           l.extend(mc)
           l_mc.append(l)
     return l_mc

  def deep_update_condition_bloc(self):
     """
        Parcourt l'arborescence des mcobject et realise l'update 
        des blocs conditionnels par appel de la methode update_condition_bloc
     """
     self._update_condition_bloc()
     for mcobj in self.mc_liste:
        if hasattr(mcobj,"deep_update_condition_bloc"):
           mcobj.deep_update_condition_bloc()

  def update_condition_bloc(self):
     """
        Realise l'update des blocs conditionnels fils de self
        et propage au parent
     """
     self._update_condition_bloc()
     if self.parent:self.parent.update_condition_bloc()

  def _update_condition_bloc(self):
     """
        Realise l'update des blocs conditionnels fils de self
     """
     dict = self.cree_dict_condition(self.mc_liste,condition=1)
     for k,v in self.definition.entites.items():
        if v.label != 'BLOC' :continue
        globs= self.jdc and self.jdc.condition_context or {}
        bloc=self.get_child(k,restreint = 'oui')
        presence=v.verif_presence(dict,globs)
        if presence and not bloc:
           # le bloc doit �tre pr�sent
           # mais le bloc n'est pas pr�sent et il doit �tre cr��
           #print "AJOUT BLOC",k
           pos=self.get_index_child(k)
           self.addentite(k,pos)
        if not presence and bloc:
           # le bloc devrait �tre absent
           # le bloc est pr�sent : il faut l'enlever
           #print "SUPPRESSION BLOC",k,bloc
           self.suppentite(bloc)

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
    dict = self.cree_dict_condition(self.mc_liste,condition=1)
    for k,v in self.definition.entites.items():
      if v.label=='BLOC' :
        globs= self.jdc and self.jdc.condition_context or {}
        if v.verif_presence(dict,globs):
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

  def verif_existence_sd(self):
     """
        V�rifie que les structures de donn�es utilis�es dans self existent bien dans le contexte
        avant �tape, sinon enl�ve la r�f�rence � ces concepts
     """
     for motcle in self.mc_liste :
         motcle.verif_existence_sd()

  def update_mc_global(self):
     """
        Met a jour les mots cles globaux enregistr�s dans l'�tape parente 
        et dans le jdc parent.
        Un mot cle compose ne peut pas etre global. Il se contente de passer
        la requete a ses fils.
     """
     for motcle in self.mc_liste :
         motcle.update_mc_global()

  def delete_mc_global(self):
     for motcle in self.mc_liste :
         motcle.delete_mc_global()
