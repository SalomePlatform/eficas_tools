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
    Ce module contient la classe de définition pour les nuplets NUPL
"""
# Modules Python
import types

# Modules Eficas
from Noyau import N_ENTITE,N_MCLIST,N_CR
from Ihm import I_ENTITE
import mcnuplet

class NUPL(N_ENTITE.ENTITE,I_ENTITE.ENTITE):
   """
   """
   class_instance = mcnuplet.MCNUPLET
   list_instance = N_MCLIST.MCList
   label='NUPLET'
   CR=N_CR.CR

   def __init__(self,fr="",ang="",docu="",statut='f',defaut=None,min=0,max=1,
                    elements=None):
      N_ENTITE.ENTITE.__init__(self)
      I_ENTITE.ENTITE.__init__(self)
      self.fr=fr
      self.ang=ang
      self.docu=docu
      self.statut=statut
      self.defaut=defaut
      self.min=min
      self.max=max
      self.entites=elements
      self.regles=()
      # on force le statut des sous entites a obligatoire
      for e in elements:e.statut='o'
      self.idracine="NUPLET"
      self.affecter_parente()

   def verif_cata(self):
      """
          Cette methode sert à valider les attributs de l'objet de définition
          de la classe NUPL
      """
      if type(self.min) != types.IntType :
        if self.min != '**':
          self.cr.fatal("L'attribut 'min' doit être un entier : "+`self.min`)
      if type(self.max) != types.IntType :
        if self.max != '**' :
          self.cr.fatal("L'attribut 'max' doit être un entier : "+`self.max`)
      if self.min > self.max :
         self.cr.fatal("Nombres d'occurrence min et max invalides : %s %s" %(`self.min`,`self.max`))
      if type(self.fr) != types.StringType :
        self.cr.fatal("L'attribut 'fr' doit être une chaîne de caractères : %s" +`self.fr`)
      if self.statut not in ['o','f','c','d']:
        self.cr.fatal("L'attribut 'statut' doit valoir 'o','f','c' ou 'd' : %s" %`self.statut`)
      if type(self.docu) != types.StringType :
        self.cr.fatal("L'attribut 'docu' doit être une chaîne de caractères : %s" %`self.docu`)
      self.verif_cata_regles()

   def __call__(self,val,nom,parent):
      """
         Construit la structure de donnees pour un NUPLET a partir de sa definition (self)
         de sa valeur (val), de son nom (nom) et de son parent dans l arboresence (parent)
      """
      if (type(val) == types.TupleType or type(val) == types.ListType) and type(val[0]) == types.TupleType:
        # On est en presence d une liste de nuplets
        l=self.list_instance()
        l.init(nom=nom,parent=parent)
        for v in val:
          objet=self.class_instance(nom=nom,definition=self,val=v,parent=parent)
          l.append(objet)
        return l
      else:
        # on est en presence d un seul nuplet
        return self.class_instance(nom=nom,definition=self,val=val,parent=parent)

   def report(self):
      """ 
           Méthode qui crée le rapport de vérification du catalogue du nuplet 
      """
      self.cr = self.CR()
      self.verif_cata()
      for v in self.entites :
        cr = v.report()
        cr.debut = "Début "+v.__class__.__name__+ ' : '
        cr.fin = "Fin "+v.__class__.__name__+ ' : '
        self.cr.add(cr)
      return self.cr

   def affecter_parente(self):
      """
          Cette methode a pour fonction de donner un nom et un pere aux
          sous entités qui n'ont aucun moyen pour atteindre leur parent 
          directement
          Il s'agit principalement des mots cles
      """
      k=0
      for v in self.entites:
        v.pere = self
        v.nom = str(k)
        k=k+1

