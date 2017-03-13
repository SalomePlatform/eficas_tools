# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
"""
"""
# Modules Python
from __future__ import absolute_import
from __future__ import print_function
import sys,re
import types
from copy import copy

from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException

# Objet re pour controler les identificateurs Python
concept_re=re.compile(r'[a-zA-Z_]\w*$')

# import rajoute suite a l'ajout de Build_sd --> a resorber
import traceback
import Noyau
from Noyau import N_Exception
from Noyau.N_Exception import AsException
import Validation
# fin import a resorber

# Modules EFICAS
from . import I_MCCOMPO
from . import CONNECTOR
from Extensions import commande_comm

class ETAPE(I_MCCOMPO.MCCOMPO):

   def ident(self):
      return self.nom

   def get_sdname(self):
      #print "SDNAME ",self.reuse,self.sd,self.sd.get_name()
      if CONTEXT.debug : 
          print(("SDNAME ",  self.reuse,  self.sd,  self.sd.get_name()))
      sdname=''
      if self.reuse != None:
        sdname= self.reuse.get_name()
      else:
        if self.sd:sdname=self.sd.get_name()
      if sdname.find('sansnom') != -1 or sdname.find('SD_') != -1:
        # dans le cas ou la SD est 'sansnom' ou 'SD_' on retourne la chaine vide
        return ''
      return sdname

   def is_reentrant(self):
      """ 
          Indique si la commande est reentrante
      """
      return self.definition.reentrant == 'o' 

   def init_modif(self):
      """
         Met l'etat de l'etape a : modifie
         Propage la modification au parent
      """
      # init_modif doit etre appele avant de realiser une modification
      # La validite devra etre recalculee apres cette modification
      # mais dans l'appel a fin_modif pour preserver l'etat modified
      # de tous les objets entre temps
      #print "init_modif",self,self.parent
      self.state = 'modified'
      if self.parent:
        self.parent.init_modif()

   def fin_modif(self):
      """
          Methode appelee une fois qu'une modification a ete faite afin de 
          declencher d'eventuels traitements post-modification
          ex : INCLUDE et POURSUITE
          Ne pas mettre de traitement qui risque d'induire des recursions (soit a peu pres rien)
      """
      CONNECTOR.Emit(self,"valid")
      if self.parent:
        self.parent.fin_modif()

   def nomme_sd(self,nom) :
      """
          Cette methode a pour fonction de donner un nom (nom) au concept 
          produit par l'etape (self).
            - si le concept n'existe pas, on essaye de le creer a condition que l'etape soit valide ET non reentrante)
            - si il existe dea, on le renomme et on repercute les changements dans les autres etapes    
          Les valeurs de retour sont :
            - 0 si le nommage n'a pas pu etre menea son terme,
            - 1 dans le cas contraire
      """
      # Le nom d'un concept doit etre un identificateur Python (toujours vrai ?)
      if not concept_re.match(nom):
         return 0, tr("Un nom de concept doit etre un identificateur Python")

      #if len(nom) > 8 and self.jdc.definition.code == 'ASTER':
      #  return 0, tr("Nom de concept trop long (maxi 8 caracteres)")

      self.init_modif()
      #
      # On verifie d'abord si les mots cles sont valides
      #
      if not self.isvalid(sd='non') : return 0,"Nommage du concept refuse : l'operateur n'est pas valide"
      #
      # Cas particulier des operateurs obligatoirement reentrants
      #
      if self.definition.reentrant == 'o':
        self.sd = self.reuse = self.jdc.get_sd_avant_etape(nom,self)
        if self.sd != None :
          self.sdnom=self.sd.nom
          self.fin_modif()
          return 1, tr("Concept existant")
        else:
          return 0, tr("Operateur reentrant mais concept non existant")
      #
      # Cas particulier des operateurs facultativement reentrants
      #
      old_reuse=None
      if self.definition.reentrant == 'f' :
        sd = self.jdc.get_sd_avant_etape(nom,self)
        if sd != None :
          if isinstance(sd,self.get_type_produit()) :
             self.sd = self.reuse = sd
             self.sdnom = sd.nom
             self.fin_modif()
             return 1, tr("Operateur reentrant et concept existant trouve")
          else:
             return 0, tr("Concept deja existant et de mauvais type")
        else :
          # il faut enlever le lien vers une SD existante car si on passe ici
          # cela signifie que l'operateur n'est pas utilise en mode reentrant.
          # Si on ne fait pas cela, on risque de modifier une SD produite par un autre operateur
          if self.reuse :
             old_reuse=self.reuse
             self.sd = self.reuse = self.sdnom = None
      #
      # On est dans le cas ou l'operateur n'est pas reentrant ou est facultativement reentrant
      # mais est utilise en mode non reentrant
      #
      if self.sd == None :
          #Pas de concept produit preexistant
          if self.parent.get_sd_autour_etape(nom,self):
            # Un concept de ce nom existe dans le voisinage de l'etape courante
            # On retablit l'ancien concept reentrant s'il existait
            if old_reuse:
               self.sd=self.reuse=old_reuse
               self.sdnom=old_reuse.nom
            return 0, tr("Nommage du concept refuse : un concept de meme nom existe deja")
          else:
            # Il n'existe pas de concept de ce nom dans le voisinage de l'etape courante
            # On peut donc creer le concept retourne
            # Il est cree sans nom mais enregistre dans la liste des concepts existants
            try:
               self.get_sd_prod()
               # Renommage du concept : Il suffit de changer son attribut nom pour le nommer
               self.sd.nom = nom
               self.sdnom=nom
               self.parent.update_concept_after_etape(self,self.sd)
               self.fin_modif()
               return 1, tr("Nommage du concept effectue")
            except:
               return 0, tr("Nommage impossible %s", str(sys.exc_info()[1]))
      else :
          #Un concept produit preexiste
          old_nom=self.sd.nom
          if old_nom.find('sansnom') :
            # Dans le cas ou old_nom == sansnom, isvalid retourne 0 alors que ...
            # par contre si le concept existe et qu'il s'appelle sansnom c'est que l'etape est valide
            # on peut donc le nommer sans test prealable
            if self.parent.get_sd_autour_etape(nom,self):
              return 0, tr("Nommage du concept refuse : un concept de meme nom existe deja")
            else:
              # Renommage du concept : Il suffit de changer son attribut nom pour le nommer
              self.sd.nom=nom
              self.sdnom=nom
              self.parent.update_concept_after_etape(self,self.sd)
              self.fin_modif()
              return 1, tr("Nommage du concept effectue")
          if self.isvalid() :
            # Normalement l appel de isvalid a mis a jour le concept produit (son type)
            # Il suffit de specifier l attribut nom de sd pour le nommer si le nom n est pas
            # deja attribue
            if self.parent.get_sd_autour_etape(nom,self):
              return 0, tr("Nommage du concept refuse : un concept de meme nom existe deja")
            else:
              # Renommage du concept : Il suffit de changer son attribut nom pour le nommer
              self.sd.nom=nom
              self.sdnom=nom
              self.parent.update_concept_after_etape(self,self.sd)
              self.fin_modif()
              return 1, tr("Nommage du concept effectue")
          else:
            # Normalement on ne devrait pas passer ici
            return 0, 'Normalement on ne devrait pas passer ici'

   def get_sdprods(self,nom_sd):
      """ 
         Fonction : retourne le concept produit par l etape de nom nom_sd
         s il existe sinon None
      """
      if self.sd:
        if self.sd.nom == nom_sd:return self.sd

   def active(self):
      """
          Rend l'etape courante active.
          Il faut ajouter la sd si elle existe au contexte global du JDC
          et a la liste des sd
      """
      if self.actif:return
      self.actif = 1
      self.init_modif()
      if self.sd :
        try:
          self.jdc.append_sdprod(self.sd)
        except:
          pass
      CONNECTOR.Emit(self,"add",None)
      CONNECTOR.Emit(self,"valid")

   def inactive(self):
      """
          Rend l'etape courante inactive
          Il faut supprimer la sd du contexte global du JDC
          et de la liste des sd
      """
      self.actif = 0
      self.init_modif()
      if self.sd :
         self.jdc.del_sdprod(self.sd)
         self.jdc.delete_concept_after_etape(self,self.sd)
      CONNECTOR.Emit(self,"supp",None)
      CONNECTOR.Emit(self,"valid")

   def control_sdprods(self,d):
      """
          Cette methode doit verifier que ses concepts produits ne sont pas
          deja definis dans le contexte
          Si c'est le cas, les concepts produits doivent etre supprimes
      """
      #print "control_sdprods",d.keys(),self.sd and self.sd.nom,self.nom
      if self.sd:
        if self.sd.nom in d :
           # Le concept est deja defini
           if self.reuse and self.reuse is d[self.sd.nom]:
              # Le concept est reutilise : situation normale
              pass
           else:
              # Redefinition du concept, on l'annule
              #XXX on pourrait simplement annuler son nom pour conserver les objets
              # l'utilisateur n'aurait alors qu'a renommer le concept (faisable??)
              self.init_modif()
              sd=self.sd
              self.sd=self.reuse=self.sdnom=None
              #supprime les references a sd dans les etapes suivantes
              self.parent.delete_concept_after_etape(self,sd)
              self.fin_modif()

   def supprime_sdprod(self,sd):
      """
         Supprime le concept produit sd s'il est produit par l'etape
      """
      if sd is not self.sd:return
      if self.sd != None :
         self.init_modif()
         self.parent.del_sdprod(sd)
         self.sd=None
         self.fin_modif()
         self.parent.delete_concept(sd)

   def supprime_sdprods(self):
      """ 
            Fonction:
            Lors d'une destruction d'etape, detruit tous les concepts produits
            Un operateur n a qu un concept produit 
            Une procedure n'en a aucun
            Une macro en a en general plus d'un
      """
      #print "supprime_sdprods",self
      if self.reuse is self.sd :return
      # l'etape n'est pas reentrante
      # le concept retourne par l'etape est a supprimer car il etait 
      # cree par l'etape
      if self.sd != None :
         self.parent.del_sdprod(self.sd)
         self.parent.delete_concept(self.sd)

   def close(self):
      return

   def update_concept(self,sd):
      for child in self.mc_liste :
          child.update_concept(sd)

   def delete_concept(self,sd):
      """ 
          Inputs :
             - sd=concept detruit
          Fonction :
          Mettre a jour les mots cles de l etape et eventuellement 
          le concept produit si reuse
          suite a la disparition du concept sd
          Seuls les mots cles simples MCSIMP font un traitement autre 
          que de transmettre aux fils
      """
      if self.reuse and self.reuse == sd:
        self.sd=self.reuse=None
        self.init_modif()
      for child in self.mc_liste :
        child.delete_concept(sd)

   def replace_concept(self,old_sd,sd):
      """
          Inputs :
             - old_sd=concept remplace
             - sd = nouveau concept 
          Fonction :
          Mettre a jour les mots cles de l etape et eventuellement
          le concept produit si reuse
          suite au remplacement  du concept old_sd
      """
      if self.reuse and self.reuse == old_sd:
        self.sd=self.reuse=sd
        self.init_modif()
      for child in self.mc_liste :
        child.replace_concept(old_sd,sd)

   def reset_context(self):
      pass

   def get_noms_sd_oper_reentrant(self):
      """ 
          Retourne la liste des noms de concepts utilisesa l'interieur de la commande
          qui sont du type que peut retourner cette commande 
      """
      liste_sd = self.get_sd_utilisees()
      l_noms = []
      if type(self.definition.sd_prod) == types.FunctionType:
        d=self.cree_dict_valeurs(self.mc_liste)
        try:
          classe_sd_prod = self.definition.sd_prod(*(), **d)
        except:
          return []
      else:
        classe_sd_prod = self.definition.sd_prod
      for sd in liste_sd :
        if sd.__class__ is classe_sd_prod : l_noms.append(sd.nom)
      l_noms.sort()
      return l_noms

   def get_genealogie_precise(self):
      return [self.nom]

   def get_genealogie(self):
      """ 
          Retourne la liste des noms des ascendants de l'objet self
          en s'arretant a la premiere ETAPE rencontree
      """
      return [self.nom]

   def verif_existence_sd(self):
     """
        Verifie que les structures de donnees utilisees dans self existent bien dans le contexte
        avant etape, sinon enleve la referea ces concepts
     """
     #print "verif_existence_sd",self.sd
     for motcle in self.mc_liste :
         motcle.verif_existence_sd()

   def update_mc_global(self):
     """
        Met a jour les mots cles globaux enregistres dans l'etape
        et dans le jdc parent.
        Une etape ne peut pas etre globale. Elle se contente de passer
        la requete a ses fils apres avoir reinitialise le dictionnaire 
        des mots cles globaux.
     """
     self.mc_globaux={}
     I_MCCOMPO.MCCOMPO.update_mc_global(self)

   def update_condition_bloc(self):
     """
        Realise l'update des blocs conditionnels fils de self
     """
     self._update_condition_bloc()

   def get_objet_commentarise(self,format):
      """
          Cette methode retourne un objet commande commentarisee
          representant la commande self
      """
      import generator
      g=generator.plugins[format]()
      texte_commande = g.gener(self,format='beautifie')
      # Il faut enlever la premiere ligne vide de texte_commande que
      # rajoute le generator
      # on construit l'objet COMMANDE_COMM repesentatif de self mais non
      # enregistre dans le jdc (pas ajoute dans jdc.etapes)
      parent=self.parent
      pos=self.parent.etapes.index(self)
      # on ajoute une fin à la commande pour pouvoir en commenter 2
      texte_commande+='\nFin Commentaire'
      commande_comment = commande_comm.COMMANDE_COMM(texte=texte_commande,
                                                     reg='non',
                                                     parent=parent)
      self.parent.suppentite(self)
      parent.addentite(commande_comment,pos)

      return commande_comment

   def modified(self):
      """Le contenu de l'etape (mots cles, ...) a ete modifie"""
      if self.nom=="DETRUIRE":
        self.parent.control_context_apres(self)


     
#ATTENTION SURCHARGE: a garder en synchro ou a reintegrer dans le Noyau
   def Build_sd(self,nom):
      """
           Methode de Noyau surchargee pour poursuivre malgre tout
           si une erreur se produit pendant la creation du concept produit
      """
      try:
         sd=Noyau.N_ETAPE.ETAPE.Build_sd(self,nom)
      except AsException as e :
         # Une erreur s'est produite lors de la construction du concept
         # Comme on est dans EFICAS, on essaie de poursuivre quand meme
         # Si on poursuit, on a le choix entre deux possibilites :
         # 1. on annule la sd associee a self
         # 2. on la conserve mais il faut la retourner
         # En plus il faut rendre coherents sdnom et sd.nom
         self.sd=None
         self.sdnom=None
         self.state="unchanged"
         self.valid=0

      return self.sd

#ATTENTION SURCHARGE: cette methode doit etre gardee en synchronisation avec Noyau
   def make_register(self):
      """
         Initialise les attributs jdc, id, niveau et realise les
         enregistrements necessaires
         Pour EFICAS, on tient compte des niveaux
         Surcharge la methode make_register du package Noyau
      """
      if self.parent :
         self.jdc = self.parent.get_jdc_root()
         self.id=   self.parent.register(self)
         self.UserError=self.jdc.UserError
         if self.definition.niveau :
            # La definition est dans un niveau. En plus on
            # l'enregistre dans le niveau
            self.nom_niveau_definition = self.definition.niveau.nom
            self.niveau = self.parent.dict_niveaux[self.nom_niveau_definition]
            self.niveau.register(self)
         else:
            # La definition est au niveau global
            self.nom_niveau_definition = 'JDC'
            self.niveau=self.parent
      else:
         self.jdc = self.parent =None
         self.id=None
         self.niveau=None
         self.UserError="UserError"

   def report(self):
     cr= Validation.V_ETAPE.ETAPE.report(self)
     #rafraichisst de la validite de l'etape (probleme avec l'ordre dans les macros : etape puis mots cles)
     self.isvalid()
     if not self.isvalid() and self.nom == "INCLUDE" :
        self.cr.fatal(('Etape : %s ligne : %r  %s'),
        self.nom, self.appel[0],  tr("\n   Include Invalide. \n  ne sera pas pris en compte"))
     return cr

