""" 
    Ce module contient la classe de definition OPER
    qui permet de sp�cifier les caract�ristiques d'un op�rateur
"""

import types,string,traceback

import N_ENTITE
import N_ETAPE
import nommage

class OPER(N_ENTITE.ENTITE):
   """
    Classe pour definir un op�rateur

    Cette classe a trois attributs de classe 

    - class_instance qui indique la classe qui devra etre utilis�e 
            pour cr�er l'objet qui servira � controler la conformit� d'un 
            op�rateur avec sa d�finition

    - label qui indique la nature de l'objet de d�finition (ici, OPER)

    - nommage qui est un module Python qui fournit la fonctionnalit� de nommage

    et les attributs d'instance suivants :

    - nom   : son nom

    - op   : le num�ro d'op�rateur

    - sd_prod : le type de concept produit. C'est une classe ou une fonction qui retourne
                      une classe

    - reentrant : vaut 'n' ou 'o'. Indique si l'op�rateur est r�entrant ou pas. Un op�rateur
                        r�entrant peut modifier un concept d'entr�e et le produire comme concept de sortie

    - repetable : vaut 'n' ou 'o'. Indique si l'op�rateur est r�petable ou pas. Un op�rateur
                        non r�p�table ne doit apparaitre qu'une fois dans une ex�cution. C'est du ressort
                        de l'objet g�rant le contexte d'ex�cution de v�rifier cette contrainte.

    - fr   : commentaire associ� en fran�ais

    - ang : commentaire associ� en anglais

    - docu : cl� de documentation associ�e

    - regles : liste des r�gles associ�es

    - op_init : cet attribut vaut None ou une fonction. Si cet attribut ne vaut pas None, cette
                      fonction est ex�cut�e lors des phases d'initialisation de l'�tape associ�e.

    - niveau : indique le niveau dans lequel est rang� l'op�rateur. Les op�rateurs peuvent �tre
                     rang�s par niveau. Ils apparaissent alors exclusivement dans leur niveau de rangement.
                     Si niveau vaut None, l'op�rateur est rang� au niveau global.

    - entites : dictionnaire dans lequel sont stock�s les sous entit�s de l'op�rateur. Il s'agit
                      des entit�s de d�finition pour les mots-cl�s : FACT, BLOC, SIMP. Cet attribut
                      est initialis� avec args, c'est � dire les arguments d'appel restants.


   """
   class_instance = N_ETAPE.ETAPE
   label = 'OPER'
   nommage = nommage

   def __init__(self,nom,op,sd_prod,reentrant='n',repetable='o',fr="",ang="",
                docu="",regles=(),op_init=None,niveau = None,**args):
      """
         M�thode d'initialisation de l'objet OPER. Les arguments sont utilis�s pour initialiser
         les attributs de meme nom
      """
      self.nom=nom
      self.op=op
      self.sd_prod=sd_prod
      self.reentrant=reentrant
      self.fr=fr
      self.ang=ang
      self.repetable = repetable
      self.docu=docu
      if type(regles)== types.TupleType:
          self.regles=regles
      else:
          self.regles=(regles,)
      # Attribut op_init : Fonction a appeler a la construction de l operateur sauf si == None
      self.op_init=op_init
      self.entites=args
      current_cata=CONTEXT.get_current_cata()
      if niveau == None:
         self.niveau=None
         current_cata.enregistre(self)
      else:
         self.niveau=current_cata.get_niveau(niveau)
         self.niveau.enregistre(self)
      self.affecter_parente()

   def __call__(self,reuse=None,**args):
      """
          Construit l'objet ETAPE a partir de sa definition (self),
          puis demande la construction de ses sous-objets et du concept produit.
      """
      nomsd=self.nommage.GetNomConceptResultat(self.nom)
      etape= self.class_instance(oper=self,reuse=reuse,args=args)
      etape.McBuild()
      return etape.Build_sd(nomsd)

   def make_objet(self,mc_list='oui'):
      """ 
           Cette m�thode cr�e l'objet ETAPE dont la d�finition est self sans
            l'enregistrer ni cr�er sa sdprod.
           Si l'argument mc_list vaut 'oui', elle d�clenche en plus la construction 
           des objets MCxxx.
      """
      etape= self.class_instance(oper=self,reuse=None,args={})
      if mc_list == 'oui':etape.McBuild()
      return etape

   def verif_cata(self):
      """
          M�thode de v�rification des attributs de d�finition
      """
      if type(self.regles) != types.TupleType :
        self.cr.fatal("L'attribut 'regles' doit �tre un tuple : %s" %`self.regles`)
      if type(self.fr) != types.StringType :
        self.cr.fatal("L'attribut 'fr' doit �tre une cha�ne de caract�res : %s" %`self.fr`)
      if self.reentrant not in ('o','n','f'):
        self.cr.fatal("L'attribut 'reentrant' doit valoir 'o','n' ou 'f' : %s" %`self.reentrant`)
      if type(self.docu) != types.StringType :
        self.cr.fatal("L'attribut 'docu' doit �tre une cha�ne de caract�res : %s" %`self.docu` )
      if type(self.nom) != types.StringType :
        self.cr.fatal("L'attribut 'nom' doit �tre une cha�ne de caract�res : %s" %`self.nom`)
      if type(self.op) != types.IntType :
        self.cr.fatal("L'attribut 'op' doit �tre un entier sign� : %s" %`self.op`)
      self.verif_cata_regles()

   def supprime(self):
      """
          M�thode pour supprimer les r�f�rences arri�res susceptibles de provoquer
          des cycles de r�f�rences
      """
      self.niveau=None


