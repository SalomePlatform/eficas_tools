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
import string

# Modules Eficas
from Noyau import N_MCCOMPO
from Validation import V_MCCOMPO

class MCNUPLET(V_MCCOMPO.MCCOMPO,N_MCCOMPO.MCCOMPO):
   """
   """
   nature = "MCNUPLET"
   txt_nat="Nuplet : "

   def __init__(self,val,definition,nom,parent):
      # val contient la valeur initial du nuplet
      self.val = val
      if val == None: self.val=()
      self.definition=definition
      self.nom=nom
      self.parent = parent
      # GETVAL affecte la valeur par defaut si necessaire
      self.valeur=self.GETVAL(self.val)
      if parent :
         self.jdc = self.parent.jdc
         self.niveau = self.parent.niveau
         self.etape = self.parent.etape
      else:
         # Le mot cle a été créé sans parent
         self.jdc = None
         self.niveau = None
         self.etape = None
      self.state = 'undetermined'
      self.actif=1
      self.mc_liste=self.build_mc()

   def build_mc(self):
      """ 
          Construit la liste des sous-entites de MCNUPLET
          à partir de la liste des arguments (valeur)
      """
      args = self.valeur
      if args ==None : args =()
      mc_liste=[]

      # on crée les sous entites du NUPLET a partir des valeurs initiales
      k=0
      for v in self.definition.entites:
        if k < len(args):
          val=args[k]
        else:
          val=None
        objet=v(val=val,nom=`k`,parent=self)
        if hasattr(objet.definition,'position'):
          if objet.definition.position == 'global' :
            self.append_mc_global(objet)
          #XXX et global_jdc ??
        mc_liste.append(objet)
        k=k+1
      # Un nuplet n'a pas de mots inconnus
      self.reste_val={}
      return mc_liste

   def isvalid(self,cr='non'):
      """
          Indique si self (MCNUPLET) est un objet valide ou non : retourne 1 si oui, 0 sinon
      """
      if self.state == 'unchanged' :
        return self.valid
      else:
        valid = 1
        if hasattr(self,'valid'):
          old_valid = self.valid
        else:
          old_valid = None
        for child in self.mc_liste :
          if not child.isvalid():
            valid = 0
            break
        if len(self.mc_liste) != len(self.definition.entites):
          valid=0
          if cr == 'oui' :
            self.cr.fatal(string.join(("Nuplet : ",self.nom," Longueur incorrecte")))
        self.valid = valid
        self.state = 'unchanged'
        if old_valid:
          if old_valid != self.valid : self.init_modif_up()
        return self.valid

   def __getitem__(self,key):
      """
          Retourne le key ème élément du nuplet
      """
      # Un nuplet est toujours une liste de mots cles simples
      # On retourne donc la valeur
      return self.mc_liste[key].valeur

   def __str__(self):
      """
           Retourne une représentation du nuplet sous forme de chaine
           de caractères
      """
      s='('
      for e in self.mc_liste:
        s=s + str(e.valeur) + ','
      return s + ')'

   def __repr__(self):
      """
           Retourne une représentation du nuplet sous forme de chaine
           de caractères
      """
      s='('
      for e in self.mc_liste:
        s=s + str(e.valeur) + ','
      return s + ')'

   def get_regles(self):
      """
         Retourne la liste des règles attachées au nuplet
      """
      return []

   def verif_condition_bloc(self):
      """
          Vérifie s'il y a des blocs sous le nuplet et retourne 
          les blocs en question
      """
      # Il n y a pas de BLOCs sous un NUPLET
      return [],[]

   def isrepetable(self):
      """ 
          Indique si le NUPLET peut etre répété.
          Retourne 1 si c'est le cas.
          Retourne 0 dans le cas contraire.
          L'information est donnée par le catalogue, cad la définition de self
      """
      if self.definition.min != self.definition.max :
        return 1
      else :
        return 0

   def makeobjet(self):
      return self.definition(val = None, nom = self.nom,parent = self.parent)

   def get_valeur(self):
      """
          Cette méthode doit retourner la valeur de l'objet. Elle est utilisée par 
          cree_dict_valeurs pour construire un dictionnaire contenant les mots clés 
          d'une étape.
          Dans le cas d'un nuplet, on retournera comme valeur une liste des valeurs
          des mots clé simples contenus.
      """
      l=[]
      for v in self.mc_liste:
         l.append(v.valeur)
      return l

   def get_val(self):
      """
          Une autre méthode qui retourne une "autre" valeur du mot clé facteur.
          Elle est utilisée par la méthode get_mocle
      """
      l=[]
      for v in self.mc_liste:
         l.append(v.valeur)
      return l

   def isoblig(self):
      return self.definition.statut=='o'

   def get_fr(self):
     """
        Retourne le texte d'aide dans la langue choisie
     """
     try :
        return getattr(self.definition,prefs.lang)
     except:
        return ''



