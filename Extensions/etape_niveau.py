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
    Ce module contient la classe ETAPE_NIVEAU qui sert a 
    concretiser les niveaux au sein d'un JDC
"""
import traceback

from Noyau import N_OBJECT
import prefs

class ETAPE_NIVEAU(N_OBJECT.OBJECT):

  def __init__(self,niveau,parent):
    self.parent = parent
    self.jdc = self.parent.get_jdc_root()
    self.niveau = self
    self.definition = niveau
    self.etapes=[]
    self.etapes_niveaux = []
    self.dict_niveaux={}
    self.editmode = 0
    self.state="undetermined"
    self.build_niveaux()

  def build_niveaux(self):
    for niveau in self.definition.l_niveaux:
      etape_niveau = ETAPE_NIVEAU(niveau,self)
      self.etapes_niveaux.append(etape_niveau)
      self.dict_niveaux[niveau.nom]=etape_niveau

  def register(self,etape):
    """ 
          Enregistre la commande �tape :
          - si editmode = 0 : on est en mode relecture d'un fichier de commandes
          auquel cas on ajoute etape � la fin de la liste self.etapes
          - si editmode = 1 : on est en mode ajout d'�tape depuis eficas auquel cas
          cette m�thode ne fait rien, c'est addentit� qui enregistre etape
          � la bonne place dans self.etapes 
    """
    if self.editmode : return
    self.etapes.append(etape)

  def unregister(self,etape):
    """
        Desenregistre l'etape du niveau
    """
    self.etapes.remove(etape)

  def ident(self):
    return self.definition.label

  def isactif(self):
    #print 'Niveau : ',self.definition.nom
    #print '\tactif =',self.definition.actif
    if self.definition.actif == 1 :
      return 1
    else :
      # self.actif est une condition � �valuer dans un certain contexte ...
      d = self.cree_dict_valeurs()
      try:
        t=eval(self.definition.actif,d)
        return t
      except:
        traceback.print_exc()
        return 0

  def cree_dict_valeurs(self):
    """
    Retourne le dictionnaire des fr�res a�n�s de self compos� des couples :
    {nom_fr�re isvalid()}
    """
    d={}
    for niveau in self.parent.etapes_niveaux:
      if niveau is self : break
      d[niveau.definition.nom]=niveau.isvalid()
    return d

  def isvalid(self):
    """ M�thode bool�enne qui retourne 0 si le niveau est invalide, 1 sinon """
    if self.etapes_niveaux == []:
      if len(self.etapes) == 0:
        return self.definition.valide_vide
      else:
        for etape in self.etapes :
          if not etape.isvalid() : return 0
        return 1
    else:
      for etape_niveau in self.etapes_niveaux :
        if not etape_niveau.isvalid() : return 0
      return 1

  def accept(self,visitor):
    visitor.visitETAPE_NIVEAU(self)

  def addentite(self,name,pos_rel):
    self.editmode = 1
    try :
      pos_abs=self.jdc.get_nb_etapes_avant(self)+pos_rel
      cmd = self.jdc.addentite(name,pos_abs)
      self.etapes.insert(pos_rel,cmd)
      self.editmode = 0
      return cmd
    except:
      traceback.print_exc()
      self.editmode = 0
      return None

  def suppentite(self,etape) :
    """ Classe ETAPE_NIVEAU
        Supprime une �tape 
    """
    self.jdc.suppentite(etape)


  def get_fr(self):
     """
        Retourne le texte d'aide dans la langue choisie
     """
     try :
        return getattr(self.definition,prefs.lang)
     except:
        return ''

