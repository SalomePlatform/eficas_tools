""" Ce module contient la classe de definition SIMP
    qui permet de sp�cifier les caract�ristiques des mots cl�s simples
"""

import types

import N_ENTITE
import N_MCSIMP

class SIMP(N_ENTITE.ENTITE):
   """
    Classe pour definir un mot cle simple 

    Cette classe a deux attributs de classe 

    - class_instance qui indique la classe qui devra etre utilis�e 
            pour cr�er l'objet qui servira � controler la conformit� d'un 
            mot-cl� simple avec sa d�finition

    - label qui indique la nature de l'objet de d�finition (ici, SIMP)

   """
   class_instance = N_MCSIMP.MCSIMP
   label = 'SIMP'

   def __init__(self,typ,fr="",ang="",statut='f',into=None,defaut=None,
                     min=1,max=1,homo=1,position ='local',
                     val_min = '**',val_max='**',docu=""):
     
      """
          Un mot-cl� simple est caract�ris� par les attributs suivants :

          - type : cet attribut est obligatoire et indique le type de valeur attendue 

          - fr   :

          - ang :

          - statut :

          - into   :

          - defaut :

          - min

          - max

          - homo

          - position

          - val_min

          - val_max

          - docu
      """
      N_ENTITE.ENTITE.__init__(self)
      # Initialisation des attributs
      if type(typ) == types.TupleType :
          self.type=typ
      else :
          self.type=(typ,)
      self.fr=fr
      self.ang=ang
      self.statut=statut
      self.into=into
      self.defaut=defaut
      self.min=min
      self.max=max
      self.homo=homo
      self.position = position
      self.val_min=val_min
      self.val_max=val_max
      self.docu = docu

   def verif_cata(self):
      """
          Cette methode sert � valider les attributs de l'objet de d�finition 
          de la classe SIMP
      """
      if type(self.min) != types.IntType :
         if self.min != '**':
            self.cr.fatal("L'attribut 'min' doit �tre un entier : "+`self.min`)
      if type(self.max) != types.IntType :
         if self.max != '**' :
            self.cr.fatal("L'attribut 'max' doit �tre un entier : "+`self.max`)
      if self.min > self.max :
         self.cr.fatal("Nombres d'occurrence min et max invalides : %s %s" %(`self.min`,`self.max`))
      if type(self.fr) != types.StringType :
         self.cr.fatal("L'attribut 'fr' doit �tre une cha�ne de caract�res : %s" +`self.fr`)
      if self.statut not in ['o','f','c','d']:
         self.cr.fatal("L'attribut 'statut' doit valoir 'o','f','c' ou 'd' : %s" %`self.statut`)
      if self.homo != 0 and self.homo != 1 :
         self.cr.fatal("L'attribut 'homo' doit valoir 0 ou 1 : %s" %`self.homo`)
      if self.into != None :
         if type(self.into) != types.TupleType :
            self.cr.fatal("L'attribut 'into' doit �tre un tuple : %s" %`self.into`)
      if self.position not in ['local','global','global_jdc']:
         self.cr.fatal("L'attribut 'position' doit valoir 'local','global' ou 'global_jdc' : %s" %`self.position`)


   def __call__(self,val,nom,parent=None):
      """
          Construit un objet mot cle simple (MCSIMP) a partir de sa definition (self)
          de sa valeur (val), de son nom (nom) et de son parent dans l arboresence (parent)
      """
      return self.class_instance(nom=nom,definition=self,val=val,parent=parent)






