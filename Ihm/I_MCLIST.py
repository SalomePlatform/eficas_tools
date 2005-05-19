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
import types,traceback
from copy import copy
import CONNECTOR

class MCList:
  def isMCList(self):
    """ 
       Retourne 1 si self est une MCList (liste de mots-cl�s), 0 sinon (d�faut) 
    """
    return 1

  def get_index(self,objet):
    """
        Retourne la position d'objet dans la liste self
    """
    return self.data.index(objet)

  def ajout_possible(self):
    """ 
        M�thode bool�enne qui retourne 1 si on peut encore ajouter une occurrence
        de l'�l�ment que contient self, 0 sinon 
    """
    max = self.data[0].definition.max
    if max == '**':
      return 1
    else:
      if len(self) < max :
        return 1
      else:
        return 0

  def isrepetable(self):
    """
       Indique si l'objet est r�p�table.
       Retourne 1 si le mot-cl� facteur self peut �tre r�p�t�
       Retourne 0 dans le cas contraire
    """
    if self.data[0].definition.max > 1:
       # marche avec '**'
       return 1
    else :
       return 0

  def isoblig(self):
     """
     Une MCList n'est jamais obligatoire (m�me si le MCFACT qu'elle repr�sente l'est
     """
     return self.data[0].definition.statut=='o'
  
  def suppentite(self,obj):
      """
        Supprime le mot cle facteur obj de la MCLIST
      """
      self.init_modif()
      self.remove(obj)
      CONNECTOR.Emit(self,"supp",obj)
      self.fin_modif()
      return 1

  def addentite(self,obj,pos=None):
      """
        Ajoute le mot cle facteur obj a la MCLIST a la position pos
        Retourne None si l'ajout est impossible
      """
      if type(obj)==types.StringType :
         # on est en mode cr�ation d'un motcle
         raise "traitement non prevu"

      if not self.ajout_possible():
         self.jdc.send_message("L'objet %s ne peut pas �tre ajout�" % obj.nom)
         return None

      if self.nom != obj.nom:
         return None

      if obj.isMCList():
         obj=obj.data[0]

      # Traitement du copier coller seulement 
      # Les autres cas d'ajout sont traites dans MCFACT
      self.init_modif()
      obj.verif_existence_sd()
      obj.reparent(self.parent)
      if pos is None:
         self.append(obj)
      else:
         self.insert(pos,obj)
      CONNECTOR.Emit(self,"add",obj)
      self.fin_modif()
      return obj

  def liste_mc_presents(self):
    return []

  def delete_concept(self,sd):
    """ 
        Inputs :
           - sd=concept detruit
        Fonction : Mettre a jour les fils de l objet suite � la disparition 
        du concept sd
        Seuls les mots cles simples MCSIMP font un traitement autre 
        que de transmettre aux fils
    """
    for child in self.data :
      child.delete_concept(sd)

  def replace_concept(self,old_sd,sd):
    """
        Inputs :
           - old_sd=concept remplac�
           - sd=nouveau concept
        Fonction : Mettre a jour les fils de l objet suite au remplacement 
        du concept old_sd
    """
    for child in self.data :
      child.replace_concept(old_sd,sd)

  def get_docu(self):
    return self.data[0].definition.get_docu()

  def get_liste_mc_inconnus(self):
     """
     Retourne la liste des mots-cl�s inconnus dans self
     """
     l_mc = []
     for mcfact in self.data :
        if mcfact.isvalid() : continue
        l_child = mcfact.get_liste_mc_inconnus()
        for mc in l_child:
           l = [self]
           l.extend(mc)
           l_mc.append(l)
     return l_mc

  def verif_condition_regles(self,liste_presents):
    """
        Retourne la liste des mots-cl�s � rajouter pour satisfaire les r�gles
        en fonction de la liste des mots-cl�s pr�sents
    """
    # Sans objet pour une liste de mots cl�s facteurs
    return []

  def deep_update_condition_bloc(self):
     """
        Parcourt l'arborescence des mcobject et realise l'update
        des blocs conditionnels par appel de la methode update_condition_bloc
     """
    
     #print "deep_update_condition_bloc",self
     for mcfact in self.data :
         mcfact.deep_update_condition_bloc()

  def verif_condition_bloc(self):
    """ 
        Evalue les conditions de tous les blocs fils possibles 
        (en fonction du catalogue donc de la d�finition) de self et 
        retourne deux listes :
           - la premi�re contient les noms des blocs � rajouter
           - la seconde contient les noms des blocs � supprimer
    """
    # Sans objet pour une liste de mots cl�s facteurs (a voir !!!)
    return [],[]

  def init_modif(self):
    """
       Met l'�tat de l'objet � modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def fin_modif(self):
    """
      M�thode appel�e apr�s qu'une modification a �t� faite afin de d�clencher
      d'�ventuels traitements post-modification
    """
    #print "fin_modif",self
    CONNECTOR.Emit(self,"valid")
    if self.parent:
      self.parent.fin_modif()

  def get_genealogie(self):
     """
         Retourne la liste des noms des ascendants.
         Un objet MCList n'est pas enregistr� dans la genealogie.
         XXX Meme si le MCFACT fils ne l'est pas lui non plus ????
     """
     if self.parent: 
        return self.parent.get_genealogie()
     else:
        return []

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

  def verif_existence_sd(self):
     """
        V�rifie que les structures de donn�es utilis�es dans self existent bien dans le contexte
	avant �tape, sinon enl�ve la r�f�rence � ces concepts
     """
     for motcle in self.data :
         motcle.verif_existence_sd()

  def get_fr(self):
     """
         Retourne la chaine d'aide contenue dans le catalogue
         en tenant compte de la langue
     """
     try :
        return self.data[0].get_fr()
     except:
        return ''

