""" 
    Ce module contient la classe ETAPE qui sert � v�rifier et � ex�cuter
    une commande
"""

# Modules Python
import types,sys,string,os
import linecache
import traceback

# Modules EFICAS
import N_MCCOMPO
from N_Exception import AsException
import N_utils
from N_utils import AsType

class ETAPE(N_MCCOMPO.MCCOMPO):
   """
      Cette classe h�rite de MCCOMPO car ETAPE est un OBJECT composite

   """
   nature = "OPERATEUR"

   # L'attribut de classe codex est utilis� pour rattacher le module de calcul �ventuel (voir Build)
   # On le met � None pour indiquer qu'il n'y a pas de module de calcul rattach�
   codex=None

   def __init__(self,oper=None,reuse=None,args={}):
      """
         Attributs :

          - definition : objet portant les attributs de d�finition d'une �tape de type op�rateur. Il
                         est initialis� par l'argument oper.

          - reuse : indique le concept d'entr�e r�utilis�. Il se trouvera donc en sortie
                    si les conditions d'ex�cution de l'op�rateur l'autorise

          - valeur : arguments d'entr�e de type mot-cl�=valeur. Initialis� avec l'argument args.

      """
      self.definition=oper
      self.reuse=reuse
      self.valeur=args
      self.nettoiargs()
      self.parent=CONTEXT.get_current_step()
      self.etape = self
      self.nom=oper.nom
      self.idracine=oper.label
      self.appel=N_utils.callee_where()
      self.mc_globaux={}
      self.sd=None
      self.actif=1
      self.make_register()

   def make_register(self):
      """
         Initialise les attributs jdc, id, niveau et r�alise les 
         enregistrements n�cessaires
      """
      if self.parent :
         self.jdc = self.parent.get_jdc_root()
         self.id=self.parent.register(self)
         self.niveau=None
      else:
         self.jdc = self.parent =None
         self.id=None
         self.niveau=None

   def nettoiargs(self):
      """
         Cette methode a pour fonction de retirer tous les arguments egaux � None
         de la liste des arguments. Ils sont suppos�s non pr�sents et donc retir�s.
      """
      for k in self.valeur.keys():
         if self.valeur[k] == None:del self.valeur[k]

   def McBuild(self):
      """
         Demande la construction des sous-objets et les stocke dans l'attribut
         mc_liste.
      """
      self.mc_liste=self.build_mc()

   def Build_sd(self,nom):
      """
         Construit le concept produit de l'op�rateur. Deux cas 
         peuvent se pr�senter :
        
         - le parent n'est pas d�fini. Dans ce cas, l'�tape prend en charge la cr�ation 
           et le nommage du concept.

         - le parent est d�fini. Dans ce cas, l'�tape demande au parent la cr�ation et 
           le nommage du concept.

      """
      if not self.isactif():return
      try:
         if self.parent:
            sd= self.parent.create_sdprod(self,nom)
            if type(self.definition.op_init) == types.FunctionType: 
               apply(self.definition.op_init,(self,self.parent.g_context))
         else:
            sd=self.get_sd_prod()
            # On n'utilise pas self.definition.op_init car self.parent 
            # n'existe pas
            if sd != None and self.reuse == None:
               # On ne nomme le concept que dans le cas de non reutilisation 
               # d un concept
               sd.nom=nom
         if self.jdc and self.jdc.par_lot == "NON" :
            self.Execute()
         return sd
      except AsException,e:
         raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                              'fichier : ',self.appel[1],e)
      except EOFError:
         # XXX Normalement le contexte courant doit etre le parent.
         # Il n'y a pas de raison de remettre le contexte au parent
         #self.reset_current_step()
         raise
      except :
         l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
         raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                           'fichier : ',self.appel[1]+'\n',
                            string.join(l))

   def Execute(self):
      """
         Cette methode est prevue pour faire une execution dans le cas
         ou par_lot == 'NON'
         Par defaut, elle ne fait rien
      """
      return

   def get_sd_prod(self):
      """
          Retourne le concept r�sultat de l'�tape
          Deux cas :
                   cas 1 : sd_prod de oper n'est pas une fonction
                           il s'agit d'une sous classe de ASSD
                           on construit le sd � partir de cette classe
                           et on le retourne
                   cas 2 : il s'agit d'une fonction
                           on l'�value avec les mots-cl�s de l'�tape (mc_liste)
                           on construit le sd � partir de la classe obtenue
                           et on le retourne
      """
      if type(self.definition.sd_prod) == types.FunctionType:
        d=self.cree_dict_valeurs(self.mc_liste)
        try:
          sd_prod= apply(self.definition.sd_prod,(),d)
        except EOFError:
          raise
        except:
          if CONTEXT.debug: traceback.print_exc()
          l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],
                                       sys.exc_info()[2])
          raise AsException("impossible d affecter un type au resultat",
                             string.join(l[2:]))
          #         sys.exc_info()[0],sys.exc_info()[1],)
      else:
        sd_prod=self.definition.sd_prod
      # on teste maintenant si la SD est r�utilis�e ou s'il faut la cr�er
      if self.reuse:
        if AsType(self.reuse) != sd_prod:
          raise AsException("type de concept reutilise incompatible avec type produit")
        self.sd=self.reuse
      else:
        self.sd= sd_prod(etape=self)
        if self.definition.reentrant == 'o':
          self.reuse = self.sd
      return self.sd

   def get_type_produit(self):
      """
          Retourne le type du concept r�sultat de l'�tape
          Deux cas :
           cas 1 : sd_prod de oper n'est pas une fonction
                   il s'agit d'une sous classe de ASSD
                   on retourne le nom de la classe
           cas 2 : il s'agit d'une fonction
                    on l'�value avec les mots-cl�s de l'�tape (mc_liste)
                   et on retourne son r�sultat
      """
      if type(self.definition.sd_prod) == types.FunctionType:
        d=self.cree_dict_valeurs(self.mc_liste)
        try:
          sd_prod= apply(self.definition.sd_prod,(),d)
        except:
          #traceback.print_exc()
          return None
      else:
        sd_prod=self.definition.sd_prod
      return sd_prod

   def get_etape(self):
      """
         Retourne l'�tape � laquelle appartient self
         Un objet de la cat�gorie etape doit retourner self pour indiquer que
         l'�tape a �t� trouv�e
         XXX fait double emploi avec self.etape ????
      """
      return self

   def supprime(self):
      """
         M�thode qui supprime toutes les r�f�rences arri�res afin que l'objet puisse
         �tre correctement d�truit par le garbage collector
      """
      N_MCCOMPO.MCCOMPO.supprime(self)
      self.jdc=None
      self.appel=None
      if self.sd : self.sd.supprime()

   def isactif(self):
      """ 
         Indique si l'�tape est active (1) ou inactive (0)
      """
      return self.actif

   def set_current_step(self):
      """
          Methode utilisee pour que l etape self se declare etape
          courante. Utilise par les macros
      """
      #print "set_current_step ",self.nom
      #traceback.print_stack(limit=3,file=sys.stdout)
      cs= CONTEXT.get_current_step()
      if self.parent != cs :
         raise "L'�tape courante %s devrait etre le parent de self : %s" % (cs,self)
      else :
         CONTEXT.unset_current_step()
         CONTEXT.set_current_step(self)

   def reset_current_step(self):
      """ 
            Methode utilisee par l'etape self qui remet son etape parent comme 
             etape courante 
      """
      #print "reset_current_step ",self.nom
      #traceback.print_stack(limit=3,file=sys.stdout)
      cs= CONTEXT.get_current_step()
      if self != cs :
         raise "L'�tape courante %s devrait etre self : %s" % (cs,self)
      else :
         CONTEXT.unset_current_step()
         CONTEXT.set_current_step(self.parent)

   def issubstep(self,etape):
      """ 
          Cette methode retourne un entier indiquant si etape est une
          sous etape de self ou non
          1 = oui
          0 = non
          Une �tape simple n'a pas de sous etape
      """
      return 0

   def get_file(self,unite=None,fic_origine=''):
      """ 
         Retourne le nom du fichier associe a l unite logique unite (entier)
         ainsi que le source contenu dans le fichier
      """
      if self.jdc : return self.jdc.get_file(unite=unite,fic_origine=fic_origine)
      else :
         file = None
         if unite != None:
            if os.path.exists("fort."+str(unite)):
               file= "fort."+str(unite)
         if file == None : 
            raise AsException("Impossible de trouver le fichier correspondant a l unite %s" % unite)
         if not os.path.exists(file): 
            raise AsException("%s n'est pas un fichier existant" % unite)
         fproc=open(file,'r')
         text=string.replace(fproc.read(),'\r\n','\n')
         fproc.close()
         linecache.cache[file]=0,0,string.split(text,'\n'),file
         return file,text

   def accept(self,visitor):
      """
         Cette methode permet de parcourir l'arborescence des objets
         en utilisant le pattern VISITEUR
      """
      visitor.visitETAPE(self)

   def update_context(self,d):
      """
          Cette methode doit updater le contexte fournit par
          l'appelant en argument (d) en fonction de sa definition
      """
      if type(self.definition.op_init) == types.FunctionType:
        apply(self.definition.op_init,(self,d))
      if self.sd:
        d[self.sd.nom]=self.sd




