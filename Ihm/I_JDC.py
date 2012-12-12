# -*- coding: iso-8859-1 -*-
# Copyright (C) 2007-2012   EDF R&D
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
import types,traceback,sys,os
import string,linecache

# Modules Eficas
import I_OBJECT
import Noyau
from Noyau.N_ASSD import ASSD
#from Noyau.N_LASSD import LASSD
from Noyau.N_ETAPE import ETAPE
from Noyau.N_Exception import AsException
from Extensions import commentaire,parametre,parametre_eval
import CONNECTOR
import Validation

class LASSD:
   pass

class JDC(I_OBJECT.OBJECT):
   """
   """
   def __init__(self):
      self.editmode=0
      self.etapes_niveaux=[]
      self.niveau=self
      self.params=[]
      self.fonctions=[]
      self._etape_context=None
      self.recorded_units={}
      self.old_recorded_units={}

   def get_index(self,objet):
      """
        Retourne la position d'objet dans la liste self
      """
      return self.etapes.index(objet)

   def get_sd_avant_du_bon_type(self,etape,types_permis):
      """
          Retourne la liste des concepts avant etape d'un type acceptable
      """
      d=self.get_contexte_avant(etape)
      
      
      l=[]
      for k,v in d.items():
        if type(v) != types.InstanceType and not isinstance(v,object): continue
        # On considere que seul assd indique un type quelconque pas CO
        elif self.assd in types_permis :
           l.append(k)
        elif self.est_permis(v,types_permis):
           l.append(k)
      l.sort()
      return l

   def get_variables(self,etape):
      etapeStop=etape
      l=[]
      for etapeTraitee in self.etapes :
          if etapeTraitee==etapeStop:
             break
          if etapeTraitee.nom == 'VARIABLE' :
             variable=etapeTraitee.get_mocle('ModelVariable')
             if variable != None :
                l.append(variable.nom)
      return l

   def set_Copules_recalcule_etat(self):
      for etapeTraitee in self.etapes :
          if etapeTraitee.nom == 'CORRELATION' :
             Matrix=etapeTraitee.get_child('Matrix')
             if Matrix !=None :
                Correlation=etapeTraitee.get_child('CorrelationMatrix')
                if Correlation !=None :
                   Correlation.state='arecalculer'
                Matrix.state='arecalculer'
     
   def recalcule_etat_correlation(self):
      for etapeTraitee in self.etapes :
          if etapeTraitee.nom == 'CORRELATION' :
             Matrix=etapeTraitee.get_child('Matrix')
             if Matrix !=None :
                Matrix.state='arecalculer'
                Correlation=Matrix.get_child('CorrelationMatrix')
                if Correlation !=None :
                   Correlation.state='arecalculer'
                   Correlation.isvalid()
                Matrix.isvalid()
                etapeTraitee.state='arecalculer'
             if etapeTraitee.state=='arecalculer':
                etapeTraitee.isvalid()
                
        
   def get_sd_avant_du_bon_type_pour_type_de_base(self,etape,type):
      """
          Retourne la liste des concepts avant etape d'1 type de base acceptable
          Attention different de la routine precedente : 1 seul type passe en parametre
          Teste sur issubclass et par sur le type permis
      """
      d=self.get_contexte_avant(etape)
      l=[]
      try :
         typeverif=self.cata[0].__dict__[type]
      except :
         return l
      for k,v in d.items():
        if issubclass(v.__class__,typeverif): 
           l.append(k)
      l.sort()
      return l

   def cherche_list_avant(self,etape,valeur):
       d=self.get_contexte_avant(etape)
       for k,v in d.items():
          if issubclass(v.__class__,LASSD):
             if k == valeur :
                return k
        # Attention pour enlever les . a la fin des pretendus reels
             if k == valeur[0:-1] :
                return v
       return None

   def est_permis(self,v,types_permis):
      for type_ok in types_permis:
          if type_ok in ('R','I','C','TXM') and v in self.params : 
             return 1
          elif type_ok == 'R' and v.__class__.__name__ == 'reel' : 
             return 1
          elif type_ok == 'I' and v.__class__.__name__ == 'entier' : 
             return 1
          elif type_ok == 'C' and v.__class__.__name__ == 'complexe' : 
             return 1
          elif type_ok == 'TXM' and v.__class__.__name__ == 'chaine' : 
             return 1
          elif type(type_ok) != types.ClassType and not isinstance(type_ok,type): 
             continue
          elif v.__class__ == type_ok or issubclass(v.__class__,type_ok):
             return 1
      return 0

   def addentite(self,name,pos):
      """
          Ajoute une entite :
          Si name est le nom d une commande ou un commentaire ajoute 
          une etape au JDC
          Sinon remonte une erreur
      """
      self.init_modif()
      self.editmode=1
      if name == "COMMENTAIRE" :
        # ajout d'un commentaire
        self.set_current_step()
        ind = 1
        for child in self.etapes :
          from Extensions import commentaire
          if isinstance(child,commentaire.COMMENTAIRE):
            ind = ind+1
        objet = commentaire.COMMENTAIRE('',parent=self)
        objet.nom = "_comm_"+`ind`
        if pos == None : pos = 0
        self.etapes.insert(pos,objet)
        self.reset_context()
        self.editmode=0
        self.active_etapes()
        CONNECTOR.Emit(self,"add",objet)
        self.fin_modif()
        return objet
      elif name == "PARAMETRE":
        # ajout d'un parametre
        self.set_current_step()
        nom_param = '_param_'+str(len(self.params)+1)
        objet = parametre.PARAMETRE(nom=nom_param)
        if pos == None : pos = 0
        self.etapes.insert(pos,objet)
        self.reset_context()
        self.editmode=0
        self.active_etapes()
        CONNECTOR.Emit(self,"add",objet)
        self.fin_modif()
        return objet
      elif name == "PARAMETRE_EVAL":
        # ajout d'un parametre EVAL
        self.set_current_step()
        nom_param = '_param_'+str(len(self.params)+1)
        objet = parametre_eval.PARAMETRE_EVAL(nom=nom_param)
        if pos == None : pos = 0
        self.etapes.insert(pos,objet)
        self.reset_context()
        self.editmode=0
        self.active_etapes()
        CONNECTOR.Emit(self,"add",objet)
        self.fin_modif()
        return objet
      elif type(name)==types.InstanceType:
        # on est dans le cas ou on veut ajouter une commande deja 
        # existante (par copie donc)
        # on est donc necessairement en mode editeur ...
        objet = name
        # Il ne faut pas oublier de reaffecter le parent d'obj (si copie)
        from Extensions import commentaire
        if not( isinstance (objet,commentaire.COMMENTAIRE)):
           objet.reparent(self)
        self.set_current_step()
        if isinstance(objet,ETAPE):
          if objet.nom_niveau_definition == 'JDC':
            # l'objet depend directement du JDC
            objet.niveau = self
          else:
            # l'etape depend d'un niveau et non directement du JDC :
            # il faut l'enregistrer dans le niveau de parent
            objet.parent.dict_niveaux[objet.nom_niveau_definition].register(objet)
            objet.niveau = objet.parent.dict_niveaux[objet.nom_niveau_definition]
        self.etapes.insert(pos,objet)
        self.reset_context()
        # il faut verifier que les concepts utilises par objet existent bien
        # a ce niveau d'arborescence
        objet.verif_existence_sd()
        objet.update_mc_global()
        self.editmode=0
        self.active_etapes()
        CONNECTOR.Emit(self,"add",objet)
        self.fin_modif()
        return objet
      else :
        # On veut ajouter une nouvelle commande
        #try:
        if 1 :
          self.set_current_step()
          cmd=self.get_cmd(name)
          # L'appel a make_objet n'a pas pour effet d'enregistrer l'etape
          # aupres du step courant car editmode vaut 1
          # Par contre elle a le bon parent grace a set_current_step
          e=cmd.make_objet()
          if pos == None : pos = 0
          self.etapes.insert(pos,e)
          self.reset_current_step()
          self.reset_context()
          self.editmode=0
          self.active_etapes()
          CONNECTOR.Emit(self,"add",e)
          self.fin_modif()
          return e
        #except AsException,e:
          self.reset_current_step()
          self.editmode=0
          raise AsException("Impossible d ajouter la commande "+name + '\n' +str(e))
        #except:
        else :
          traceback.print_exc()
          self.reset_current_step()
          self.editmode=0
          raise AsException("Impossible d ajouter la commande "+name)

   def close(self):
      #print "JDC.close",self
      for etape in self.etapes:
          if hasattr(etape,"close"):etape.close()
      CONNECTOR.Emit(self,"close")

   def set_current_step(self):
      CONTEXT.unset_current_step()
      CONTEXT.set_current_step(self)

   def reset_current_step(self):
      CONTEXT.unset_current_step()

   def liste_mc_presents(self):
      return []

   def get_sd_avant_etape(self,nom_sd,etape):
      return self.get_contexte_avant(etape).get(nom_sd,None)

   def get_sd_apres_etape_avec_detruire(self,nom_sd,sd,etape,avec='non'):
      """ 
           Cette methode retourne la SD sd de nom nom_sd qui est eventuellement
           definie apres etape en tenant compte des concepts detruits
           Si avec vaut 'non' exclut etape de la recherche
      """
      #print "JDC.get_sd_apres_etape_avec_detruire",nom_sd,sd
      ietap=self.etapes.index(etape)
      if avec == 'non':ietap=ietap+1
      d={nom_sd:sd}
      for e in self.etapes[ietap:]:
         if e.isactif():
            e.update_context(d)
            autre_sd=d.get(nom_sd,None)
            if autre_sd is None:
              # Le concept a ete detruit. On interrompt la recherche car il n'y a
              # pas eu de redefinition du concept (il n'y a pas de conflit potentiel).
              return None
            if autre_sd is not sd :
              # L'etape produit un concept different de meme nom. La situation n'est
              # pas saine (sauf peut etre si reuse ???)
              if hasattr(e,'reuse') and e.reuse == autre_sd:
                 # Le concept etant reutilise, on interrompt la recherche. 
                 # On considere qu'il n'y a pas de nouveau concept defini
                 # meme si dans les etapes suivantes le concept est detruit
                 # et un concept de meme nom cree.
                 # AVERIFIER : avec reuse le concept devrait etre le meme
                 # le passage par ici est tres improbable
                 return None
              else:
                 # Le concept est produit par l'etape (Il y a conflit potentiel).
                 # Le concept est redefini par une etape posterieure.
                 return autre_sd
      # Pas de destruction du concept ni de redefinition. On retourne le
      # concept initial
      return sd

   def get_sd_apres_etape(self,nom_sd,etape,avec='non'):
      """ 
           Cette methode retourne la SD de nom nom_sd qui est eventuellement
           definie apres etape 
           Si avec vaut 'non' exclut etape de la recherche
      """
      ietap=self.etapes.index(etape)
      if avec == 'non':ietap=ietap+1
      for e in self.etapes[ietap:]:
        sd=e.get_sdprods(nom_sd)
        if sd:
          if hasattr(e,'reuse'):
            if e.reuse != sd:
              return sd
      return None

   def get_sd_autour_etape(self,nom_sd,etape,avec='non'):
      """
           Fonction: retourne la SD de nom nom_sd qui est eventuellement
           definie avant ou apres etape
           Permet de verifier si un concept de meme nom existe dans le perimetre 
           d'une etape
           Si avec vaut 'non' exclut etape de la recherche
      """
      sd=self.get_sd_avant_etape(nom_sd,etape)
      if sd:return sd
      return self.get_sd_apres_etape(nom_sd,etape,avec)

   def get_contexte_apres(self,etape):
      """
         Retourne le dictionnaire des concepts connus apres etape
         On tient compte des commandes qui modifient le contexte
         comme DETRUIRE ou les macros
         Si etape == None, on retourne le contexte en fin de JDC
      """
      if not etape: return self.get_contexte_avant(etape)

      d=self.get_contexte_avant(etape)
      if etape.isactif():etape.update_context(d)
      self.index_etape_courante=self.index_etape_courante+1
      return d

   def active_etapes(self):
      """
          Cette methode a pour fonction de desactiver les etapes qui doivent
          l'etre cad, dans le cas d'ASTER, les etapes qui ne sont pas 
          comprises entre le premier DEBUT/POURSUITE et le premier FIN 
          et rendre actives les autres
      """
      if self.definition.code == 'ASTER' :
         # Seulement pour ASTER :
         # Avant DEBUT actif vaut 0
         # Apres DEBUT et avant le 1er FIN actif vaut 1
         # Apres le 1er FIN actif vaut -1
         actif=0
      else:
         actif=1
      for etape in self.etapes:
        if actif == 0 and etape.nom in ['DEBUT','POURSUITE']:actif=1
        if actif == 1:
           etape.active()
        else:
           etape.inactive()
        if etape.nom == 'FIN':actif=-1

   def deplaceEntite(self,indexNoeudACopier,indexNoeudOuColler,pos):
      """
          Pour le cut
      """
      if indexNoeudACopier==indexNoeudOuColler:return
      etapeACopier=self.etapes[indexNoeudACopier]
      try :
        sd=self.etapes[indexNoeudACopier].sd
      except :
        sd=None
      if pos=='before' and indexNoeudOuColler==0 : 
         self.etapes2=[etapeACopier,]+self.etapes[0:indexNoeudACopier]+self.etapes[indexNoeudACopier+1:]
      elif indexNoeudACopier < indexNoeudOuColler :
         self.etapes2=self.etapes[0:indexNoeudACopier]+self.etapes[indexNoeudACopier+1:indexNoeudOuColler+1]+[etapeACopier,]+self.etapes[indexNoeudOuColler+1:]
      else:
         self.etapes2=self.etapes[0:indexNoeudOuColler+1]+[etapeACopier,]+self.etapes[indexNoeudOuColler+1:indexNoeudACopier]+self.etapes[indexNoeudACopier+1:]
      self.etapes=self.etapes2
      if indexNoeudACopier < indexNoeudOuColler :
        self.delete_concept_entre_etapes(indexNoeudACopier,indexNoeudOuColler,sd)
      self.reset_context()
      for e in self.etapes :
         e.state = 'modified'
      self.control_context_apres(None)
      return 1


   def suppentite(self,etape) :
      """  
          Cette methode a pour fonction de supprimer une etape dans 
          un jeu de commandes
          Retourne 1 si la suppression a pu etre effectuee,
          Retourne 0 dans le cas contraire
      """
      #PN correction de bugs 
      if etape not in self.etapes:
         return 0

      self.init_modif()
      index_etape=self.etapes.index(etape)
      self.etapes.remove(etape)

      if etape.niveau is not self:
        # Dans ce cas l'etape est enregistree dans un niveau
        # Il faut la desenregistrer
        etape.niveau.unregister(etape)

      etape.supprime_sdprods()
      etape.close()
      etape.supprime()
      self.active_etapes()

      # Apres suppression de l'etape il faut controler que les etapes
      # suivantes ne produisent pas des concepts DETRUITS dans op_init de etape
      if index_etape > 0: 
         index_etape=index_etape-1
         etape=self.etapes[index_etape]
      else:
         etape=None
      self.control_context_apres(etape)
     
      self.reset_context()
      CONNECTOR.Emit(self,"supp",etape)
      self.fin_modif()
      return 1

   def control_context_apres(self,etape):
      """
         Cette methode verifie que les etapes apres l'etape etape
         ont bien des concepts produits acceptables (pas de conflit de 
         nom principalement)
         Si des concepts produits ne sont pas acceptables ils sont supprimes.
         Effectue les verifications sur les etapes du jdc mais aussi sur les
         jdc parents s'ils existent.
      """
      #print "control_context_apres",self,etape
      #Regularise les etapes du jdc apres l'etape etape
      self.control_jdc_context_apres(etape)

   def control_jdc_context_apres(self,etape):
      """
          Methode semblable a control_context_apres mais ne travaille
          que sur les etapes et sous etapes du jdc
      """
      #print "control_jdc_context_apres",self,etape
      if etape is None:
         # on demarre de la premiere etape
         index_etape=0
      else:
         index_etape=self.etapes.index(etape)+1

      try:
         etape=self.etapes[index_etape]
      except:
         #derniere etape du jdc : rien a faire
         return

      context=self.get_contexte_avant(etape)

      for e in self.etapes[index_etape:]:
          e.control_sdprods(context)
          e.update_context(context)

   def analyse(self):
      self.compile()
      if not self.cr.estvide():return
      self.exec_compile()
      self.active_etapes()

   def register_parametre(self,param):
      """
          Cette methode sert a ajouter un parametre dans la liste des parametres
      """
      self.params.append(param)

   def register_fonction(self,fonction):
      """
          Cette methode sert a ajouter une fonction dans la liste des fonctions
      """
      self.fonctions.append(fonction)

   def delete_param(self,param):
      """
          Supprime le parametre param de la liste des parametres
          et du contexte gobal
      """
      if param in self.params : self.params.remove(param)
      if self.g_context.has_key(param.nom) : del self.g_context[param.nom]

   def get_parametres_fonctions_avant_etape(self,etape):
      """
          Retourne deux elements :
          - une liste contenant les noms des parametres (constantes ou EVAL) 
            definis avant etape
          - une liste contenant les formules definies avant etape
      """
      l_constantes = []
      l_fonctions = []
      # on recupere le contexte avant etape
      # on ne peut mettre dans les deux listes que des elements de ce contexte
      d=self.get_contexte_avant(etape)
      # construction de l_constantes
      for param in self.params:
        nom = param.nom
        if not nom : continue
        if d.has_key(nom): l_constantes.append(nom)
      # construction de l_fonctions
      for form in self.fonctions:
        nom = form.nom
        if not nom : continue
        if d.has_key(nom): l_fonctions.append(form.get_formule())

      # on ajoute les concepts produits par DEFI_VALEUR
      # XXX On pourrait peut etre faire plutot le test sur le type
      # de concept : entier, reel, complexe, etc.
      for k,v in d.items():
         if hasattr(v,'etape') and v.etape.nom in ('DEFI_VALEUR',):
            l_constantes.append(k)

      # on retourne les deux listes
      return l_constantes,l_fonctions

   def get_nb_etapes_avant(self,niveau):
      """ 
          Retourne le nombre d etapes avant le debut de niveau
      """
      nb=0
      for niv in self.etapes_niveaux:
        if niv == niveau:break
        nb=nb+len(niv.etapes)
      return nb

   def init_modif(self):
      """
      Methode appelee au moment ou une modification va etre faite afin de 
      declencher d'eventuels traitements pre-modification
      """
      #print "init_modif",self
      self.state = 'modified'

   def fin_modif(self):
      #print "fin_modif",self
      CONNECTOR.Emit(self,"valid")
      self.isvalid()
      pass

   def deep_update_condition_bloc(self):
      # pour le moment, on ne fait rien
      raise "Not implemented"

   def update_condition_bloc(self):
      # pour le moment, on ne fait rien
      raise "Not implemented"

   def get_liste_mc_inconnus(self):
     """
     Retourne une liste contenant les mots-cles inconnus a la relecture du JDC
     """
     # cette liste a le format suivant : [etape,(bloc,mcfact,...),nom_mc,valeur_mc]
     l_mc = []
     for etape in self.etapes :
         if etape.isactif() :
            if not etape.isvalid() :
               l = etape.get_liste_mc_inconnus()
               if l : l_mc.extend(l)
     return l_mc    

   def get_genealogie(self):
      """
          Retourne la liste des noms des ascendants de l'objet self
          jusqu'a la premiere ETAPE parent.
      """
      return []

   def get_liste_cmd(self):
      """
          Retourne la liste des commandes du catalogue
      """
      return self.niveau.definition.get_liste_cmd()

   def get_groups(self):
      """
          Retourne la liste des groupes
      """
      return self.niveau.definition.liste_groupes,self.niveau.definition.dict_groupes

   def set_etape_context(self,etape):
      """
          Positionne l'etape qui sera utilisee dans NommerSdProd pour
          decider si le concept passe pourra etre  nomme
      """
      self._etape_context=etape

   def reset_context(self):
      """ 
          Cette methode reinitialise le contexte glissant pour pouvoir
          tenir compte des modifications de l'utilisateur : craation
          de commandes, nommage de concepts, etc.
      """
      #print "reset_context",self,self.nom
      self.current_context={}
      self.index_etape_courante=0
      ind={}
      for i,etape in enumerate(self.etapes):
        ind[etape]=i
      self.index_etapes=ind

   #   for etape in self.etapes:
   #       etape.reset_context()

   def del_sdprod(self,sd):
      """
          Supprime la SD sd de la liste des sd et des dictionnaires de contexte
      """
      #print "del_sdprod",self,sd
      #print "del_sdprod",self.sds
      #print "del_sdprod",self.g_context
      #print "del_sdprod",self.sds_dict
      #if sd in self.sds : self.sds.remove(sd)
      if self.g_context.has_key(sd.nom) : del self.g_context[sd.nom]
      if self.sds_dict.has_key(sd.nom) : del self.sds_dict[sd.nom]

   def del_param(self,param):
      """
          Supprime le parametre param de la liste des paramatres
          et du contexte gobal
      """
      if param in self.params : self.params.remove(param)
      if self.g_context.has_key(param.nom) : del self.g_context[param.nom]

   def del_fonction(self,fonction):
      """
          Supprime la fonction fonction de la liste des fonctions
          et du contexte gobal
      """
      if fonction in self.fonctions : self.fonctions.remove(fonction)
      if self.g_context.has_key(fonction.nom) : del self.g_context[fonction.nom]

   def append_sdprod(self,sd):
      """
          Ajoute la SD sd a la liste des sd en verifiant au prealable qu'une SD de
          meme nom n'existe pas deja
      """
      if sd == None or sd.nom == None:return

      o=self.sds_dict.get(sd.nom,None)
      if isinstance(o,ASSD):
         raise AsException("Nom de concept deja defini : %s" % sd.nom)
      self.sds_dict[sd.nom]=sd
      self.g_context[sd.nom] = sd
      #if sd not in self.sds : self.sds.append(sd)

   def append_param(self,param):
      """
          Ajoute le parametre param a la liste des params
          et au contexte global
      """
      # il faudrait verifier qu'un parametre de meme nom n'existe pas deja !!!
      if param not in self.params : self.params.append(param)
      self.g_context[param.nom]=param

   def append_fonction(self,fonction):
      """
          Ajoute la fonction fonction a la liste des fonctions
          et au contexte global
      """
      # il faudrait verifier qu'une fonction de meme nom n'existe pas deja !!!
      if fonction not in self.fonctions : self.fonctions.append(fonction)
      self.g_context[fonction.nom]=fonction

   def delete_concept(self,sd):
      """
          Inputs :
             - sd=concept detruit
          Fonction :
          Mettre a jour les etapes du JDC suite a la disparition du
          concept sd
          Seuls les mots cles simples MCSIMP font un traitement autre
          que de transmettre aux fils
      """
      for etape in self.etapes :
        etape.delete_concept(sd)
        #PN PN PN pour les matrices ????
        #self.get_variables_avant(etape)

   def replace_concept_after_etape(self,etape,old_sd,sd):
      """
          Met a jour les etapes du JDC qui sont apres etape en fonction
          du remplacement du concept sd
      """
      index = self.etapes.index(etape)+1
      if index == len(self.etapes) :
         return # etape est la derniere etape du jdc ...on ne fait rien !
      for child in self.etapes[index:]:
        child.replace_concept(old_sd,sd)

   def update_concept_after_etape(self,etape,sd):
      """
          Met a jour les etapes du JDC qui sont apres etape en fonction
          de la modification (principalement nommage) du concept sd
      """
      if etape is None:
         #On traite toutes les etapes
         index=0
      else:
         index = self.etapes.index(etape)+1
      if index == len(self.etapes) :
         return # etape est la derniere etape du jdc ...on ne fait rien !
      for child in self.etapes[index:]:
        child.update_concept(sd)

   def dump_state(self):
      print "JDC.state: ",self.state
      for etape in self.etapes :
         print etape.nom+".state: ",etape.state
      
   def change_unit(self,unit,etape,old_unit):
      #print "change_unit",unit,etape,old_unit
      #print id(self.recorded_units),self.recorded_units
      #if self.recorded_units.has_key(old_unit):del self.recorded_units[old_unit]
      self.record_unit(unit,etape)

   def record_unit(self,unit,etape):
      """Enregistre les unites logiques incluses et les infos relatives a l'etape"""
      #print "record_unit",unit,etape
      if unit is None:
         # Cas de POURSUITE
         self.recorded_units[None]=(etape.fichier_ini ,etape.fichier_text,etape.recorded_units)
      else:
         self.recorded_units[unit]=(etape.fichier_ini ,etape.fichier_text,etape.recorded_units)
      #print id(self.recorded_units),self.recorded_units
      #print self.recorded_units.get(None,(None,"",{}))[2]
      #print self.recorded_units.get(None,(None,"",{}))[2].get(None,(None,"",{}))

   def changefichier(self,fichier):
       self.fin_modif()

   def eval_in_context(self,valeur,etape):
      """ Tente d'evaluer valeur dans le contexte courant de etape
          Retourne le parametre valeur inchange si l'evaluation est impossible
      """
      #contexte initial du jdc
      context=self.condition_context.copy()
      #contexte courant des concepts. Il contient les parametres
      context.update(self.get_contexte_avant(etape))
      try :
         objet = eval(valeur,context)
         return objet
      except:
         #traceback.print_exc()
         pass
      return valeur

#ATTENTION SURCHARGE : cette methode doit etre gardee en synchronisation avec celle de Noyau
   def supprime(self):
      #print "supprime",self
      Noyau.N_JDC.JDC.supprime(self)
      for etape in self.etapes:
         etape.supprime()
      self.appli=None
      self.g_context={}
      self.const_context={}
      self.sds_dict={}
      self.mc_globaux={}
      self.current_context={}
      self.condition_context={}
      self.etapes_niveaux=[]
      self.niveau=None
      self.params=[]
      self.fonctions=[]
      self._etape_context=None
      self.etapes=[]
       
#ATTENTION SURCHARGE : cette methode doit etre gardee en synchronisation avec celle de Noyau
   def register(self,etape):
      """
           Cette methode ajoute  etape dans la liste
           des etapes self.etapes et retourne l identificateur d'etape
           fourni par l appel a g_register

           A quoi sert editmode ?
              - Si editmode vaut 1, on est en mode edition de JDC. On cherche
                a enregistrer une etape que l'on a creee avec eficas (en passant
                par addentite) auquel cas on ne veut recuperer que son numero
                d'enregistrement et c'est addentite qui l'enregistre dans
                self.etapes a la bonne place...
              - Si editmode vaut 0, on est en mode relecture d'un fichier de
                commandes et on doit enregistrer l'etape a la fin de self.etapes
                (dans ce cas l'ordre des etapes est bien l'ordre chronologique
                de leur creation   )
      """
      if not self.editmode:
         self.etapes.append(etape)
         self.index_etapes[etape] = len(self.etapes) - 1
      else:
         pass
      return self.g_register(etape)

#ATTENTION SURCHARGE : cette methode doit etre gardee en synchronisation avec celle de Noyau
   def NommerSdprod(self,sd,sdnom,restrict='non'):
      """
          Nomme la SD apres avoir verifie que le nommage est possible :
          nom non utilise
          Si le nom est deja utilise, leve une exception
          Met le concept cree dans le concept global g_context
      """
      # XXX En mode editeur dans EFICAS, le nommage doit etre gere differemment
      # Le dictionnaire g_context ne represente pas le contexte
      # effectif avant une etape.
      # Il faut utiliser get_contexte_avant avec indication de l'etape
      # traitee.
      # Cette etape est indiquee par l'attribut _etape_context qui a ete
      # positionne prealablement par un appel a set_etape_context

      if CONTEXT.debug : print "JDC.NommerSdprod ",sd,sdnom

      if self._etape_context:
         o=self.get_contexte_avant(self._etape_context).get(sdnom,None)
      else:
         o=self.sds_dict.get(sdnom,None)

      if isinstance(o,ASSD):
         raise AsException("Nom de concept deja defini : %s" % sdnom)

      # ATTENTION : Il ne faut pas ajouter sd dans sds car il s y trouve deja.
      # Ajoute a la creation (appel de reg_sd).
      self.sds_dict[sdnom]=sd
      sd.nom=sdnom

      # En plus si restrict vaut 'non', on insere le concept dans le contexte du JDC
      if restrict == 'non':
         self.g_context[sdnom]=sd

   def delete_concept_entre_etapes(self,index1,index2,sd):
      if index2 <= index1 :return
      for child in self.etapes[index1:index2]:
        child.delete_concept(sd)

   def delete_concept_after_etape(self,etape,sd):
      """
          Met a jour les etapes du JDC qui sont apres etape en fonction
          de la disparition du concept sd
      """
      index = self.etapes.index(etape)+1
      if index == len(self.etapes) :
         return # etape est la derniere etape du jdc ...on ne fait rien !
      for child in self.etapes[index:]:
        child.delete_concept(sd)

#ATTENTION SURCHARGE : les methodes ci-dessus surchargent des methodes de Noyau et Validation : a reintegrer

   def get_file(self,unite=None,fic_origine=''):
      """
          Retourne le nom du fichier correspondant a un numero d'unite
          logique (entier) ainsi que le source contenu dans le fichier
      """
      if self.appli is not None:
         # Si le JDC est relie a une application maitre, on delegue la recherche
         file,text= self.appli.get_file(unite,fic_origine)
      else:
         file = None
         if unite != None:
            if os.path.exists("fort."+str(unite)):
               file= "fort."+str(unite)
         if file == None :
            raise AsException("Impossible de trouver le fichier correspondant"
                               " a l unite %s" % unite)
         if not os.path.exists(file):
            raise AsException("%s n'est pas un fichier existant" % unite)
         fproc=open(file,'r')
         text=fproc.read()
         fproc.close()
      #if file == None : return None,None
      text=string.replace(text,'\r\n','\n')
      if file:
         linecache.cache[file]=0,0,string.split(text,'\n'),file
      return file,text

   def isvalid(self,cr='non'):
     if hasattr(self,'valid'): old_valid=self.valid
     else:old_valid=0
     valid=Validation.V_JDC.JDC.isvalid(self,cr)
     if valid != old_valid:
       CONNECTOR.Emit(self,"valid")
     return valid

   def get_l_noms_etapes(self):
      """ 
          Retourne la liste des noms des étapes de self 
      """
      l=[]
      for etape in self.etapes:
        l.append(etape.nom)
      return l
