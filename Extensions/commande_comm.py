#@ MODIF commande_comm Accas  DATE 02/07/2001   AUTEUR D6BHHJP J.P.LEFEBVRE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
import os,traceback,string

from Noyau.N_CR import CR
from Noyau.N_Exception import AsException

class COMMANDE_COMM:
    """
    Cette classe sert � d�finir les objets de type Commande commentaris�e
    """
    nature = "COMMANDE_COMMENTARISEE"
    idracine='_comm'
    
    def __init__(self,texte='',parent=None,reg='oui'):
        self.valeur = texte
        if not parent :
            self.jdc = self.parent = CONTEXT.get_current_step()
        else:
            self.jdc = self.parent = parent
        if hasattr(self.parent,'etape'):
          self.etape = self.parent.etape
        else :
          self.etape = None
        self.definition=self
        self.nom = ''
        self.niveau = self.parent.niveau
        self.actif=1
        #self.appel = N_utils.callee_where(niveau=2)
        if reg=='oui' : self.register()
            
    def isvalid(self):
        return 1

    def report(self):
        """
        G�n�re l'objet rapport (classe CR)
        """
        self.cr=CR()
        if not self.isvalid(): self.cr.warn("Objet commande commentaris� invalide")
        return self.cr

    def copy(self):
        """
        Retourne une copie de self cad un objet COMMANDE_COMM
        """
        # XXX self.texte ne semble pas exister ???
        return COMMANDE_COMM(self.texte,parent = self.parent,reg='non')

    def init_modif(self):
        self.state = 'modified'
        self.parent.init_modif()    

    def set_valeur(self,new_valeur):
        """
        Remplace la valeur de self(si elle existe) par new_valeur)
        """
        self.valeur = new_valeur
        self.init_modif()

    def get_valeur(self) :
        """
        Retourne la valeur de self, cad le texte de la commande commentaris�e
        """
        return self.valeur

    def register(self):
        """
        Enregistre la commande commenatris�e dans la liste des �tapes de son parent lorsque celui-ci
        est un JDC
        """
        self.parent.register(self)

    def isoblig(self):
        """
        Indique si self est obligatoire ou non : retourne toujours 0
        """
        return 0

    def ident(self):
        """
        Retourne le nom interne associ� � self
        Ce nom n'est jamais vu par l'utilisateur dans EFICAS
        """
        return self.nom

    def isrepetable(self):
        """
        Indique si self est r�p�table ou non : retourne toujours 1
        """
        return 1        

    def get_attribut(self,nom_attribut) :
        """
        Retourne l'attribut de nom nom_attribut de self (ou h�rit�)
        """
        if hasattr(self,nom_attribut) :
          return getattr(self,nom_attribut)
        else :
          return None

    def get_fr(self):
        """
        Retourne l'attribut fr de self.definition
        """
        try :
          return getattr(self.definition,'fr')
        except:
          return ''

    def liste_mc_presents(self):
        return []

    def supprime(self):
        """ 
        M�thode qui supprime toutes les boucles de r�f�rences afin que l'objet puisse
        �tre correctement d�truit par le garbage collector 
        """
        self.parent = None
        self.etape = None
        self.jdc = None
        self.niveau = None
        self.definition = None
        self.valeur = None
        self.val = None
        self.appel = None

    def supprime_sdprods(self):
        pass

    def update_context(self,d):
        """
        Update le dictionnaire d avec les concepts ou objets produits par self
        --> ne fait rien pour une commande en  commentaire
        """
        pass

    def delete_concept(self,sd):
        pass

    def get_sdprods(self,nom_sd):
        return None

    def uncomment(self):
        """
        Cette m�thode a pour but de d�commentariser l'objet courant,
        cad de retourner un tuple contenant :
        - l'objet CMD associ�
        - le nom de la sdprod �ventuellement produite (sinon None)
        """
        # on r�cup�re le contexte avant la commande commentaris�e
        context_ini = self.jdc.get_contexte_avant(self)
        try:
            # on essaie de cr�er un objet JDC...
            CONTEXT.unset_current_step()
            J=self.jdc.__class__(procedure=self.valeur,
                                 definition=self.jdc.definition,
                                 cata=self.jdc.cata,
                                 cata_ord_dico=self.jdc.cata_ordonne_dico,
                                 context_ini = context_ini,
                                )
            J.analyse()
        except Exception,e:
            traceback.print_exc()
            #self.jdc.set_context()
            raise AsException("Erreur",str(e))
        if len(J.cr.crfatal)>0 :
            # des erreurs fatales ont �t� rencontr�es
            #self.jdc.set_context()
            print 'erreurs fatales !!!'
            raise AsException("Erreurs fatales",string.join(J.cr.crfatal))
        #self.jdc.set_context()
        new_etape = J.etapes[0]
        if new_etape.sd :
            nom_sd = new_etape.sd.nom
        else:
            nom_sd = None
        return (new_etape.copy(),nom_sd)

    def active(self):
        """
        Rend l'etape courante active
        """
        self.actif = 1

    def inactive(self):
        """
        Rend l'etape courante inactive
        """
        self.actif = 0

    def isactif(self):
        """
        Bool�enne qui retourne 1 si self est valide, 0 sinon
        """
        return self.actif
    
    def verif_condition_bloc(self):
      """
          Evalue les conditions de tous les blocs fils possibles
          (en fonction du catalogue donc de la d�finition) de self et
          retourne deux listes :
          - la premi�re contient les noms des blocs � rajouter
          - la seconde contient les noms des blocs � supprimer
      """
      return [],[]

    def verif_condition_regles(self,liste_presents):
      """
          Retourne la liste des mots-cl�s � rajouter pour satisfaire les r�gles
          en fonction de la liste des mots-cl�s pr�sents
      """
      return []

