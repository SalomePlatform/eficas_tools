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
# Modules Python
import types,traceback
import string,linecache

# Modules Eficas
import I_OBJECT
from Noyau.N_ASSD import ASSD
from Noyau.N_ETAPE import ETAPE
from Noyau.N_Exception import AsException
from Extensions import commentaire,parametre,parametre_eval

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

   def get_sd_avant_du_bon_type(self,etape,types_permis):
      """
          Retourne la liste des concepts avant etape d'un type acceptable
      """
      d=self.get_contexte_avant(etape)
      l=[]
      for k,v in d.items():
        if type(v) != types.InstanceType : continue
        # On consid�re que seul assd indique un type quelconque pas CO
        elif self.assd in types_permis :
           l.append(k)
        elif self.est_permis(v,types_permis):
           l.append(k)
      l.sort()
      return l

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
          elif type(type_ok) != types.ClassType : 
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
          if isinstance(child,commentaire.COMMENTAIRE):
            ind = ind+1
        objet = commentaire.COMMENTAIRE('',parent=self)
        objet.nom = "_comm_"+`ind`
        if pos == None : pos = 0
        self.etapes.insert(pos,objet)
        self.editmode=0
        self.active_etapes()
        return objet
      elif name == "PARAMETRE":
        # ajout d'un parametre
        self.set_current_step()
        nom_param = '_param_'+str(len(self.params)+1)
        objet = parametre.PARAMETRE(nom=nom_param)
        if pos == None : pos = 0
        self.etapes.insert(pos,objet)
        self.editmode=0
        self.reset_context()
        self.active_etapes()
        return objet
      elif name == "PARAMETRE_EVAL":
        # ajout d'un parametre EVAL
        self.set_current_step()
        nom_param = '_param_'+str(len(self.params)+1)
        objet = parametre_eval.PARAMETRE_EVAL(nom=nom_param)
        if pos == None : pos = 0
        self.etapes.insert(pos,objet)
        self.editmode=0
        self.reset_context()
        self.active_etapes()
        return objet
      elif type(name)==types.InstanceType:
        # on est dans le cas o� on veut ajouter une commande d�j� 
        # existante (par copie donc)
        # on est donc n�cessairement en mode editeur ...
        objet = name
        # Il ne faut pas oublier de reaffecter le parent d'obj (si copie)
        objet.reparent(self)
        self.set_current_step()
        if isinstance(objet,ETAPE):
          if objet.nom_niveau_definition == 'JDC':
            # l'objet d�pend directement du JDC
            objet.niveau = self
          else:
            # l'�tape d�pend d'un niveau et non directement du JDC :
            # il faut l'enregistrer dans le niveau de parent
            objet.parent.dict_niveaux[objet.nom_niveau_definition].register(objet)
            objet.niveau = objet.parent.dict_niveaux[objet.nom_niveau_definition]
        self.etapes.insert(pos,objet)
	# il faut v�rifier que les concepts utilis�s par objet existent bien
	# � ce niveau d'arborescence
	objet.verif_existence_sd()
        self.active_etapes()
        self.editmode=0
        self.reset_context()
        return objet
      else :
        # On veut ajouter une nouvelle commande
        try:
          self.set_current_step()
          cmd=self.get_cmd(name)
          # L'appel a make_objet n'a pas pour effet d'enregistrer l'�tape
          # aupr�s du step courant car editmode vaut 1
          # Par contre elle a le bon parent grace a set_current_step
          e=cmd.make_objet()
          if pos == None : pos = 0
          self.etapes.insert(pos,e)
          self.reset_current_step()
          self.editmode=0
          self.reset_context()
          self.active_etapes()
          return e
        except AsException,e:
          self.reset_current_step()
          self.editmode=0
          raise AsException("Impossible d ajouter la commande "+name + '\n' +str(e))
        except:
          traceback.print_exc()
          self.reset_current_step()
          self.editmode=0
          raise AsException("Impossible d ajouter la commande "+name)

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
           Cette m�thode retourne la SD sd de nom nom_sd qui est �ventuellement
           d�finie apres etape en tenant compte des concepts detruits
           Si avec vaut 'non' exclut etape de la recherche
      """
      ietap=self.etapes.index(etape)
      if avec == 'non':ietap=ietap+1
      d={nom_sd:sd}
      for e in self.etapes[ietap:]:
         if e.isactif():
            e.update_context(d)
            autre_sd=d.get(nom_sd,None)
            if autre_sd is None:
              # Le concept a ete detruit
              return None
            if autre_sd is not sd :
              # L'etape produit un concept de meme nom
              if hasattr(e,'reuse') and e.reuse == autre_sd:
                 # Le concept etant reutilise, on interrompt la recherche. 
                 # On considere qu'il n'y a pas de nouveau concept defini
                 # meme si dans les etapes suivantes le concept est detruit
                 # et un concept de meme nom cr��.
                 return None
              else:
                 # Le concept est produit par l'etape
                 return autre_sd
      # On n'a rien trouve. Pas de concept de nom nom_sd
      return None

   def get_sd_apres_etape(self,nom_sd,etape,avec='non'):
      """ 
           Cette m�thode retourne la SD de nom nom_sd qui est �ventuellement
           d�finie apres etape 
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
           Fonction: retourne la SD de nom nom_sd qui est �ventuellement
           d�finie avant ou apres etape
           Permet de v�rifier si un concept de meme nom existe dans le p�rim�tre 
           d'une �tape
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
          Cette m�thode a pour fonction de d�sactiver les �tapes qui doivent
          l'�tre cad, dans le cas d'ASTER, les �tapes qui ne sont pas 
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

   def suppentite(self,etape) :
      """  
          Cette methode a pour fonction de supprimer une �tape dans 
          un jeu de commandes
          Retourne 1 si la suppression a pu �tre effectu�e,
          Retourne 0 dans le cas contraire
      """
      self.init_modif()
      # On memorise le contexte avant l'etape a supprimer
      d=self.get_contexte_avant(etape)
      index_etape=self.etapes.index(etape)

      self.etapes.remove(etape)
      if etape.niveau is not self:
        # Dans ce cas l'�tape est enregistr�e dans un niveau
        # Il faut la d�senregistrer
        etape.niveau.unregister(etape)
      etape.supprime_sdprods()
      self.active_etapes()

      # Apres suppression de l'etape il faut controler que les etapes
      # suivantes ne produisent pas des concepts DETRUITS dans op_init de etape
      for e in self.etapes[index_etape:]:
         e.control_sdprods(d)
      
      self.reset_context()
      self.fin_modif()
      return 1

   def analyse(self):
      self.compile()
      if not self.cr.estvide():return
      self.exec_compile()
      self.active_etapes()

   def register_parametre(self,param):
      """
          Cette m�thode sert � ajouter un param�tre dans la liste des param�tres
      """
      self.params.append(param)

   def register_fonction(self,fonction):
      """
          Cette m�thode sert � ajouter une fonction dans la liste des fonctions
      """
      self.fonctions.append(fonction)

   def delete_param(self,param):
      """
          Supprime le param�tre param de la liste des param�tres
          et du contexte gobal
      """
      if param in self.params : self.params.remove(param)
      if self.g_context.has_key(param.nom) : del self.g_context[param.nom]

   def get_parametres_fonctions_avant_etape(self,etape):
      """
          Retourne deux �l�ments :
          - une liste contenant les noms des param�tres (constantes ou EVAL) 
            d�finis avant etape
          - une liste contenant les formules d�finies avant etape
      """
      l_constantes = []
      l_fonctions = []
      # on r�cup�re le contexte avant etape
      # on ne peut mettre dans les deux listes que des �l�ments de ce contexte
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

   def send_message(self,message):
      if self.appli:
         self.appli.send_message(message)

   def init_modif(self):
      """
      M�thode appel�e au moment o� une modification va �tre faite afin de 
      d�clencher d'�ventuels traitements pr�-modification
      """
      self.state = 'modified'

   def fin_modif(self):
      self.isvalid()
      pass

   def get_liste_mc_inconnus(self):
     """
     Retourne une liste contenant les mots-cl�s inconnus � la relecture du JDC
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
          jusqu'� la premi�re ETAPE parent.
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
          decider si le concept pass� pourra etre  nomm�
      """
      self._etape_context=etape

   def reset_context(self):
      """ 
          Cette methode reinitialise le contexte glissant pour pouvoir
          tenir compte des modifications de l'utilisateur : cr�ation
          de commandes, nommage de concepts, etc.
      """
      self.current_context={}
      self.index_etape_courante=0

   def del_sdprod(self,sd):
      """
          Supprime la SD sd de la liste des sd et des dictionnaires de contexte
      """
      if sd in self.sds : self.sds.remove(sd)
      if self.g_context.has_key(sd.nom) : del self.g_context[sd.nom]
      if self.sds_dict.has_key(sd.nom) : del self.sds_dict[sd.nom]

   def del_param(self,param):
      """
          Supprime le param�tre param de la liste des param�tres
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
          Ajoute la SD sd � la liste des sd en v�rifiant au pr�alable qu'une SD de
          m�me nom n'existe pas d�j�
      """
      if sd == None or sd.nom == None:return

      o=self.sds_dict.get(sd.nom,None)
      if isinstance(o,ASSD):
         raise AsException("Nom de concept deja defini : %s" % sd.nom)
      self.sds_dict[sd.nom]=sd
      self.g_context[sd.nom] = sd
      if sd not in self.sds : self.sds.append(sd)

   def append_param(self,param):
      """
          Ajoute le param�tre param � la liste des params
          et au contexte global
      """
      # il faudrait v�rifier qu'un param�tre de m�me nom n'existe pas d�j� !!!
      if param not in self.params : self.params.append(param)
      self.g_context[param.nom]=param

   def append_fonction(self,fonction):
      """
          Ajoute la fonction fonction � la liste des fonctions
          et au contexte global
      """
      # il faudrait v�rifier qu'une fonction de m�me nom n'existe pas d�j� !!!
      if fonction not in self.fonctions : self.fonctions.append(fonction)
      self.g_context[fonction.nom]=fonction

   def delete_concept(self,sd):
      """
          Inputs :
             - sd=concept detruit
          Fonction :
          Mettre a jour les etapes du JDC suite � la disparition du
          concept sd
          Seuls les mots cles simples MCSIMP font un traitement autre
          que de transmettre aux fils
      """
      for etape in self.etapes :
        etape.delete_concept(sd)

   def replace_concept_after_etape(self,etape,old_sd,sd):
      """
          Met � jour les �tapes du JDC qui sont apr�s etape en fonction
          du remplacement du concept sd
      """
      index = self.etapes.index(etape)+1
      if index == len(self.etapes) :
         return # etape est la derni�re �tape du jdc ...on ne fait rien !
      for child in self.etapes[index:]:
        child.replace_concept(old_sd,sd)

   def dump_state(self):
      print "dump_state"
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

#ATTENTION SURCHARGE : cette methode doit etre gard�e en synchronisation avec celle de Noyau
   def register(self,etape):
      """
           Cette m�thode ajoute  etape dans la liste
           des etapes self.etapes et retourne l identificateur d'�tape
           fourni par l appel a g_register

           A quoi sert editmode ?
              - Si editmode vaut 1, on est en mode edition de JDC. On cherche
                � enregistrer une �tape que l'on a cr��e avec eficas (en passant
                par addentite) auquel cas on ne veut r�cup�rer que son num�ro
                d'enregistrement et c'est addentit� qui l'enregistre dans
                self.etapes � la bonne place...
              - Si editmode vaut 0, on est en mode relecture d'un fichier de
                commandes et on doit enregistrer l'�tape � la fin de self.etapes
                (dans ce cas l'ordre des �tapes est bien l'ordre chronologique
                de leur cr�ation   )
      """
      if not self.editmode:
         self.etapes.append(etape)
      else:
         pass
      return self.g_register(etape)

#ATTENTION SURCHARGE : cette methode doit etre gard�e en synchronisation avec celle de Noyau
   def NommerSdprod(self,sd,sdnom,restrict='non'):
      """
          Nomme la SD apres avoir verifie que le nommage est possible :
          nom non utilise
          Si le nom est deja utilise, leve une exception
          Met le concept cr�� dans le concept global g_context
      """
      # XXX En mode editeur dans EFICAS, le nommage doit etre g�r� diff�remment
      # Le dictionnaire g_context ne repr�sente pas le contexte
      # effectif avant une �tape.
      # Il faut utiliser get_contexte_avant avec indication de l'�tape
      # trait�e.
      # Cette etape est indiquee par l'attribut _etape_context qui a ete
      # positionn� pr�alablement par un appel � set_etape_context

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

#ATTENTION SURCHARGE : cette methode doit etre gard�e en synchronisation avec celle de Noyau
   def delete_concept_after_etape(self,etape,sd):
      """
          Met � jour les �tapes du JDC qui sont apr�s etape en fonction
          de la disparition du concept sd
      """
      index = self.etapes.index(etape)+1
      if index == len(self.etapes) :
         return # etape est la derni�re �tape du jdc ...on ne fait rien !
      for child in self.etapes[index:]:
        child.delete_concept(sd)

#ATTENTION SURCHARGE : les methodes ci-dessous surchargent des methodes de Noyau et Validation : a reintegrer

