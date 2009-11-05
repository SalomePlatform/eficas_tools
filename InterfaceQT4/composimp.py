# -*- coding: utf-8 -*-
# Modules Python
import string,types,os

from copy import copy,deepcopy
import traceback
import typeNode

# Modules Eficas
from Editeur import Objecttreeitem
import browser
from Noyau.N_CR   import justify_text
    
class Node(browser.JDCNode,typeNode.PopUpMenuNodeMinimal):    
    def getPanel(self):
        """        
        """
        klass = None 
        
        # Attention l ordre des if est important        

        if self.item.wait_matrice ():
	        from monMatricePanel import MonMatricePanel
                klass=MonMatricePanel
        # l'objet prend sa (ses) valeur(s) dans un ensemble discret de valeurs
        elif self.item.has_into():
            if self.item.is_list() :
                from monPlusieursIntoPanel import MonPlusieursIntoPanel
                klass = MonPlusieursIntoPanel
            else:
                from monUniqueIntoPanel import MonUniqueIntoPanel
                klass = MonUniqueIntoPanel

        # l'objet prend une ou des valeurs a priori quelconques
        else:
            # on attend une liste de valeurs 
            if self.item.is_list() :
                # on attend une liste de SD
                if self.item.wait_tuple() :
                    from monFonctionPanel import MonFonctionPanel
                    klass = MonFonctionPanel
                elif self.item.wait_assd():
                    from monPlusieursASSDPanel import MonPlusieursASSDPanel 
                    klass = MonPlusieursASSDPanel
                else:
                    # on attend une liste de valeurs de types debase (entiers, r�els,...)
                    from monPlusieursBasePanel import MonPlusieursBasePanel 
                    klass = MonPlusieursBasePanel
            # on n'attend qu'une seule valeur 
            else:
                # on attend une SD ou un objet de la classe CO (qui n'existe pas encore)
                if self.item.wait_co():
                    if len(self.item.get_sd_avant_du_bon_type()) != 0 :
                       from monUniqueSDCOIntoPanel import MonUniqueSDCOIntoPanel
                       klass = MonUniqueSDCOIntoPanel
                    else :
                       from monUniqueSDCOPanel import MonUniqueSDCOPanel
                       klass = MonUniqueSDCOPanel

                # on attend une SD
                elif self.item.wait_assd():
                    if 'R' in self.item.GetType():
                        from monUniqueASSDPanel import MonUniqueASSDReelPanel
                        klass = MonUniqueASSDReelPanel
                    else :
                        from monUniqueASSDPanel import MonUniqueASSDPanel
                        klass = MonUniqueASSDPanel

                # on attend une valeur d'un type de base (entier,reel,...)
                else:
                        # on attend un complexe
                     if self.item.wait_complex():
                        from monUniqueCompPanel import MonUniqueCompPanel
                        klass = MonUniqueCompPanel
                     else:
                        # on attend un entier, un r�el ou une string
                        from monUniqueBasePanel import MonUniqueBasePanel
                        klass = MonUniqueBasePanel
                        
        # cas particulier des fonctions
        genea = self.item.get_genealogie()
        if "VALE" in genea or "VALE_C" in genea:
            if "DEFI_FONCTION" in genea :
                from monFonctionPanel import MonFonctionPanel
                klass = MonFonctionPanel

        print klass
        if not klass:
            return None
        return klass( self, self.editor )
        
    def createPopUpMenu(self):
        typeNode.PopUpMenuNodeMinimal.createPopUpMenu(self)

        
    
class SIMPTreeItem(Objecttreeitem.AtomicObjectTreeItem):
  itemNode=Node

  def init(self) :
      self.expandable = 0
  

  #-----------------------------------------------
  #
  # Methodes liees aux informations sur le Panel
  # ou au mot-clef simple
  #
  #-----------------------------------------------
  # is_list
  # get_into                a priori inutile --> commentee
  # has_into
  # wait_into                a priori inutile --> commentee
  # GetMinMax
  # GetMultiplicite
  # GetIntervalle
  # GetListeValeurs
  # get_liste_possible

  def is_list(self):
      """
          Cette m�thode indique si le mot cle simple attend une liste (valeur de retour 1)
          ou s'il n'en attend pas (valeur de retour 0)

          Deux cas principaux peuvent se presenter : avec validateurs ou bien sans.
          Dans le cas sans validateur, l'information est donn�e par l'attribut max
          de la definition du mot cle.
          Dans le cas avec validateur, il faut combiner l'information pr�c�dente avec
          celle issue de l'appel de la m�thode is_list sur le validateur.On utilisera
          l'operateur ET pour effectuer cette combinaison (AndVal).
      """
      is_a_list=0
      min,max = self.GetMinMax()
      assert (min <= max)
      if max > 1 :
                is_a_list=1
      # Dans le cas avec validateurs, pour que le mot cle soit consid�r�
      # comme acceptant une liste, il faut que max soit sup�rieur a 1
      # ET que la m�thode is_list du validateur retourne 1. Dans les autres cas
      # on retournera 0 (n'attend pas de liste)
      if self.definition.validators :
         is_a_list= self.definition.validators.is_list() * is_a_list
      return is_a_list 


  def has_into(self):
      """
          Cette m�thode indique si le mot cle simple propose un choix (valeur de retour 1)
          ou s'il n'en propose pas (valeur de retour 0)

          Deux cas principaux peuvent se presenter : avec validateurs ou bien sans.
          Dans le cas sans validateur, l'information est donn�e par l'attribut into
          de la definition du mot cle.
          Dans le cas avec validateurs, pour que le mot cle soit consid�r�
          comme proposant un choix, il faut que into soit pr�sent OU
          que la m�thode has_into du validateur retourne 1. Dans les autres cas
          on retournera 0 (ne propose pas de choix)
      """
      has_an_into=0
      if self.definition.into:
               has_an_into=1
      elif self.definition.validators :
         has_an_into= self.definition.validators.has_into()
      return has_an_into


  def GetMinMax(self):
      """ Retourne les valeurs min et max de la d�finition de object """
      return self.object.get_min_max()

  def GetMultiplicite(self):
      """ A pr�ciser.
          Retourne la multiplicit� des valeurs affect�es a l'objet
          repr�sent� par l'item. Pour le moment retourne invariablement 1.
      """
      return 1

  def GetIntervalle(self):
      """ 
           Retourne le domaine de valeur attendu par l'objet repr�sent� 
           par l'item.
      """
      return self.object.getintervalle()

  def GetListeValeurs(self) :
      """ Retourne la liste des valeurs de object """
      valeurs=self.object.get_liste_valeurs()
      try :
        if "R" in self.object.definition.type:
           clef=self.object.GetNomConcept()
           if self.appli.dict_reels.has_key(clef):
              if type(valeurs) == types.TupleType:
                 valeurs_reelles=[]
                 for val in valeurs :
                    if self.appli.dict_reels[clef].has_key(val) : 
                       valeurs_reelles.append(self.appli.dict_reels[clef][val])
                    else :
                       valeurs_reelles.append(val)
              else :
                 if self.appli.dict_reels[clef].has_key(valeurs):
                    valeurs_reelles=self.appli.dict_reels[clef][valeurs]
              valeurs=valeurs_reelles
      except :
        pass
      return valeurs
    
  def get_liste_possible(self,listeActuelle=[]):
      if hasattr(self.definition.validators,'into'):
         valeurspossibles = self.definition.validators.into 
      else:
         valeurspossibles = self.get_definition().into

      #On ne garde que les items valides
      listevalideitem=[]
      if type(valeurspossibles) in (types.ListType,types.TupleType) :
         pass
      else :
         valeurspossibles=(valeurspossibles,)
      for item in valeurspossibles:
          encorevalide=self.valide_item(item)
          if encorevalide :
             listevalideitem.append(item)

      #on ne garde que les choix possibles qui passent le test de valide_liste_partielle
      listevalideliste=[]
      for item in listevalideitem:
          encorevalide=self.valide_liste_partielle(item,listeActuelle)
          if encorevalide :
              listevalideliste.append(item)
      return listevalideliste

  def get_liste_param_possible(self):
      liste_param=[]
      for param in self.object.jdc.params:
          encorevalide=self.valide_item(param.valeur)
          if encorevalide:
             type_param=param.valeur.__class__.__name__
             for typ in self.definition.type:
                 if typ=='R':
                     liste_param.append(param)
                 if typ=='I' and type_param=='int':
                     liste_param.append(param)
                 if typ=='TXM' and type_param=='str':
                     liste_param.append(repr(param))
                 if ('grma' in repr(typ)) and type_param=='str':
                     liste_param.append(param.nom)
      return liste_param

  #--------------------------------------------------
  #
  # Methodes liees a la validite des valeurs saisies
  #
  #---------------------------------------------------
  # valide_item
  # valide_liste_partielle
  # valide_liste_complete
  # info_erreur_item
  # info_erreur_liste
  # IsInIntervalle
  # isvalid

  def valide_item(self,item):
      """
        La validation est r�alis�e directement par l'objet
      """
      return self.object.valide_item(item)
     
  def valide_liste_partielle(self,item,listecourante):
      #On protege la liste en entree en la copiant
      valeur=listecourante[:]
      valeur.append(item)
      return self.object.valid_valeur_partielle(valeur)

  def valide_liste_complete (self,valeur):
      return self.object.valid_valeur(valeur)

  def valide_val (self,valeur):
      return self.object.valid_val(valeur)

  def info_erreur_item(self) :
      commentaire=""
      if self.definition.validators :
         commentaire=self.definition.validators.info_erreur_item()
      return commentaire
      
  def aide(self) :
      commentaire=""
      if self.definition.validators :
         commentaire=self.definition.validators.aide()
      return commentaire

  def info_erreur_liste(self) :
      commentaire=""
      if self.definition.validators :
         commentaire=self.definition.validators.info_erreur_liste()
      return commentaire

  def IsInIntervalle(self,valeur):
      """ 
          Retourne 1 si la valeur est dans l'intervalle permis par
          l'objet repr�sent� par l'item.
      """
      return self.valide_item(valeur)

  def isvalid(self):
    valide=self.object.isvalid()
    return valide

  #--------------------------------------------------
  #
  # Autres ...
  #
  #---------------------------------------------------
  # GetIconName
  # GetText
  # set_valeur_co
  # get_sd_avant_du_bon_type
  # delete_valeur_co


  def GetIconName(self):
    if self.isvalid():
      return "ast-green-ball"
    elif self.object.isoblig():
      return "ast-red-ball"
    else:
      return "ast-yel-ball"

  def GetText(self):
    """
    Classe SIMPTreeItem
    Retourne le texte a afficher dans l'arbre repr�sentant la valeur de l'objet
    point� par self 
    """
    text= self.object.GetText()
    if text == None : text=""
    return text
    

  def set_valeur_co(self,nom_co):
      """
      Affecte au MCS point� par self l'objet de type CO et de nom nom_co
      """
      ret = self.object.set_valeur_co(nom_co)
      #print "set_valeur_co",ret
      return ret
      
  def get_sd_avant_du_bon_type(self):
      """
      Retourne la liste des noms des SD pr�sentes avant l'�tape qui contient
      le MCS point� par self et du type requis par ce MCS
      """
      a=self.object.etape.parent.get_sd_avant_du_bon_type(self.object.etape,self.object.definition.type)
      return a

  def get_sd_avant_du_bon_type_pour_type_de_base(self):
      a=self.object.jdc.get_sd_avant_du_bon_type_pour_type_de_base(self.object.etape,"LASSD")
      return a




  def delete_valeur_co(self,valeur=None):
      """
           Supprime la valeur du mot cle (de type CO)
           il faut propager la destruction aux autres etapes
      """
      if not valeur : valeur=self.object.valeur
      # XXX faut il vraiment appeler del_sdprod ???
      #self.object.etape.parent.del_sdprod(valeur)
      self.object.etape.parent.delete_concept(valeur)

  #-----------------------------------------------
  #
  # Methodes liees au type de l objet attendu
  #
  #-----------------------------------------------
  # wait_co 
  # wait_geom
  # wait_complex
  # wait_reel
  # wait_assd
  # GetType

  def wait_co(self):
      """
      M�thode bool�enne qui retourne 1 si l'objet point� par self
      attend un objet de type ASSD qui n'existe pas encore (type CO()),
      0 sinon
      """
      return self.object.wait_co()

  def wait_geom(self):
      """
      M�thode bool�enne qui retourne 1 si l'objet point� par self
      attend un objet GEOM, 0 sinon
      """
      return self.object.wait_geom()
    
  def wait_complex(self):
      """ M�thode bool�enne qui retourne 1 si l'objet point� par self
      attend un complexe, 0 sinon """
      if 'C' in self.object.definition.type:
          return 1
      else:
          return 0

  def wait_reel(self):
      """ M�thode bool�enne qui retourne 1 si l'objet point� par self
      attend un r�el, 0 sinon """
      if 'R' in self.object.definition.type:
          return 1
      else:
          return 0
        
  def wait_tuple(self):
      """ M�thode bool�enne qui retourne 1 si l'objet point� par self
      attend un Tuple, 0 sinon """
      for ss_type in self.object.definition.type:
          if repr(ss_type).find('Tuple') != -1 :
             return 1
      return 0

  def wait_matrice(self):
      """ M�thode bool�enne qui retourne 1 si l'objet point� par self
      attend un Tuple, 0 sinon """
      for ss_type in self.object.definition.type:
          if repr(ss_type).find('Matrice') != -1 :
             return 1
      return 0

  def wait_assd(self):
      """M�thode bool�enne qui retourne 1 si l'objet point� par self
      attend un objet de type ASSD ou d�riv�, 0 sinon """
      return self.object.wait_assd()
    
  def wait_assd_or_type_base(self) :
      boo=0
      if len(self.object.definition.type) > 1 :
         if self.wait_reel() :
            boo = 1
         if 'I' in self.object.definition.type :
            boo = 1
      return boo

   
  def GetType(self):
      """ 
          Retourne le type de valeur attendu par l'objet repr�sent� par l'item.
      """
      return self.object.get_type()

  #-----------------------------------------------------
  #
  # Methodes liees  a l evaluation de la valeur saisie
  #
  #-----------------------------------------------------
  # eval_valeur
  # eval_valeur_item
  # is_CO
  # traite_reel

  def eval_valeur(self,valeur):
      """ Lance l'interpr�tation de 'valeur' (chaine de caract�res) comme valeur de self :
             - retourne l'objet associ� si on a pu interpr�ter (entier, r�el, ASSD,...)
             - retourne 'valeur' (chaine de caract�res) sinon
      """
      newvaleur=self.eval_val(valeur)
      return newvaleur,1

  def eval_valeur_BAK(self,valeur):
      """ Lance l'interpr�tation de 'valeur' (chaine de caract�res) comme valeur
      de l'objet point� par self :
        - retourne l'objet associ� si on a pu interpr�ter (entier, r�el, ASSD,...)
        - retourne 'valeur' (chaine de caract�res) sinon
        - retourne None en cas d invalidite
        - retourne invalide si 1 des objets du tuple l est
      """
      validite=1
      if type(valeur) in (types.ListType,types.TupleType) :
         valeurretour=[]
         for item in valeur :
             newvaleur,validiteitem=self.eval_valeur_item(item)
             valeurretour.append(newvaleur)
             if validiteitem == 0:
                validite=0
      else :
         valeurretour,validite= self.eval_valeur_item(valeur)
      if validite == 0 :
         valeurretour = None
      return valeurretour,validite

  def eval_valeur_item(self,valeur):
      """ Lance l'interpr�tation de 'valeur' qui doit ne pas etre un tuple 
          - va retourner la valeur de retour et la validite
            selon le type de l objet attendu
          - traite les reels et les parametres 
      """ 
      #print "eval_valeur_item",valeur
      if valeur==None or valeur == "" :
         return None,0
      validite=1
      if self.wait_reel():
             valeurinter = self.traite_reel(valeur)
             if valeurinter != None :
                valeurretour,validite= self.object.eval_valeur(valeurinter)
             else:
                valeurretour,validite= self.object.eval_valeur(valeur)
      elif self.wait_geom():
             valeurretour,validite = valeur,1
      else :
             valeurretour,validite= self.object.eval_valeur(valeur)
      #print "eval_valeur_item",valeurretour,validite

      if validite == 0:
         if type(valeur) == types.StringType and self.object.wait_TXM():
            essai_valeur="'" + valeur + "'"
            valeurretour,validite= self.object.eval_valeur(essai_valeur)

      if hasattr(valeurretour,'__class__'):
         #if valeurretour.__class__.__name__ in ('PARAMETRE','PARAMETRE_EVAL'):
         if valeurretour.__class__.__name__ in ('PARAMETRE',):
            validite=1

      #if self.wait_co():
         # CCAR : il ne faut pas essayer de creer un concept
         # il faut simplement en chercher un existant ce qui a du etre fait par self.object.eval_valeur(valeur)
         #try:
            #valeurretour=Accas.CO(valeur)
         #except:
            #valeurretour=None
            #validite=0
      # on est dans le cas ou on a �valu� et ou on n'aurait pas du
      if self.object.wait_TXM() :
          if type(valeurretour) != types.StringType:
             valeurretour=str(valeur)
             validite=1
      return valeurretour,validite
      
  def is_CO(self,valeur=None):
      """
         Indique si valeur est un concept produit de la macro
         Cette m�thode n'a de sens que pour un MCSIMP d'une MACRO
         Si valeur vaut None on teste la valeur du mot cle
      """
      # Pour savoir si un concept est un nouveau concept de macro
      # on regarde s'il est pr�sent dans l'attribut sdprods de l'�tape
      # ou si son nom de classe est CO.
      # Il faut faire les 2 tests car une macro non valide peut etre
      # dans un etat pas tres catholique avec des CO pas encore types
      # et donc pas dans sdprods (resultat d'une exception dans type_sdprod)
      if not valeur:valeur=self.object.valeur
      if valeur in self.object.etape.sdprods:return 1
      if type(valeur) is not types.InstanceType:return 0
      if valeur.__class__.__name__ == 'CO':return 1
      return 0

  def is_param(self,valeur) :
      for param in self.jdc.params:
          if (repr(param) == valeur):
             return 1
      return 0

  def traite_reel(self,valeur):
      """
      Cette fonction a pour but de rajouter le '.' en fin de chaine pour un r�el
      ou de d�tecter si on fait r�f�rence a un concept produit par DEFI_VALEUR
      ou un EVAL ...
      """
      valeur = string.strip(valeur)
      liste_reels = self.get_sd_avant_du_bon_type()
      if valeur in liste_reels:
          return valeur
      if len(valeur) >= 3 :
          if valeur[0:4] == 'EVAL' :
              # on a trouv� un EVAL --> on retourne directement la valeur
              return valeur
      if string.find(valeur,'.') == -1 :
          # aucun '.' n'a �t� trouv� dans valeur --> on en rajoute un a la fin
          if (self.is_param(valeur)):
              return valeur
          else:
              if string.find(valeur,'e') != -1:
                 # Notation scientifique ?
                 try :
                    r=eval(valeur)
                    return valeur
                 except :
                    return None
              else :
                 return valeur+'.'
      else:
          return valeur
        

import Accas
treeitem = SIMPTreeItem
objet = Accas.MCSIMP
