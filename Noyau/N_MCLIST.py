#@ MODIF N_MCLIST Noyau  DATE 27/03/2002   AUTEUR DURAND C.DURAND 
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
    Ce module contient la classe MCList qui sert � controler la valeur
    d'une liste de mots-cl�s facteur par rapport � sa d�finition port�e par un objet
    de type ENTITE
"""

import UserList

class MCList(UserList.UserList):
   """ Liste semblable a la liste Python
       mais avec quelques methodes en plus
       = liste de MCFACT
   """
   nature = 'MCList'
   def init(self,nom,parent):
      self.definition = None
      self.nom = nom
      self.parent=parent
      if parent :
         self.jdc = self.parent.jdc
         self.niveau = self.parent.niveau
         self.etape = self.parent.etape
      else:
         # Le mot cle a �t� cr�� sans parent
         self.jdc = None
         self.niveau = None
         self.etape = None

   def get_valeur(self):
      """
         Retourne la "valeur" d'un objet MCList. Sert � construire
         un contexte d'�valuation pour une expression Python.
         On retourne l'objet lui-meme.
      """
      return self

   def get_val(self):
      """
          Une autre m�thode qui retourne une "autre" valeur d'une MCList
          Elle est utilis�e par la m�thode get_mocle
      """
      return self

   def supprime(self):
      """ 
         M�thode qui supprime toutes les r�f�rences arri�res afin que l'objet puisse
         etre correctement d�truit par le garbage collector 
      """
      self.parent = None
      self.etape = None
      self.jdc = None
      self.niveau = None
      for child in self.data :
         child.supprime()

   def get_child(self,name):
      """ 
          Retourne le fils de nom name s'il est contenu dans self
          Par d�faut retourne le fils du premier de la liste 
      """
      obj = self.data[0]
      # Phase 1 : on cherche dans les fils directs de obj
      for child in obj.mc_liste :
        if child.nom == name: return child
      # Phase 2 : on cherche dans les blocs de self
      for child in obj.mc_liste:
        if child.isBLOC() :
          resu = child.get_child(name)
          if resu != None : return resu
      # Phase 3 : on cherche dans les entites possibles pour les d�fauts
      for k,v in obj.definition.entites.items():
        #if k == name: return v.defaut
        if k == name:
          if v.defaut != None : return v(None,k,None)
      # si on passe ici, c'est que l'on demande un fils qui n'est pas possible --> erreur
      #print "Erreur : %s ne peut etre un descendant de %s" %(name,self.nom)
      return None

   def isBLOC(self):
      """
           Indique si l'objet est de type BLOC
      """
      return 0

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitMCList(self)

