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
import traceback,types,string

# Modules Eficas
import I_ETAPE
from Noyau.N_ASSD import ASSD

# import rajout�s suite � l'ajout de Build_sd --> � r�sorber
import Noyau
from Noyau import N_Exception
from Noyau.N_Exception import AsException
# fin import � r�sorber

class MACRO_ETAPE(I_ETAPE.ETAPE):

  def __init__(self):
      I_ETAPE.ETAPE.__init__(self)
      # XXX CCAR : ne suis pas certain que typret doive etre 
      # initialise � None (a verifier)
      self.typret=None

  def get_sdprods(self,nom_sd):
    """ 
         Fonction : retourne le concept produit par l etape de nom nom_sd
                    s il existe sinon None
    """
    if self.sd:
      if self.sd.nom == nom_sd:
         return self.sd
    for co in self.sdprods:
      if co.nom==nom_sd:return co
    return None

  def make_contexte(self,fichier,text):    
    """
        Cette m�thode sert � cr�er un contexte en interpr�tant un texte source
        Python
    """
    # on r�cup�re le contexte d'un nouveau jdc dans lequel on interprete text
    contexte = self.get_contexte_jdc(fichier,text)
    if contexte == None :
      raise Exception("Impossible de relire le fichier")
    else:
      self.g_context = contexte
      if hasattr(self,'contexte_fichier_init'):
        self.old_contexte_fichier_init = self.contexte_fichier_init
      self.contexte_fichier_init = contexte
      # XXX la validit� ne doit pas etre forc�e � 1. Que faut-il faire exactement ???
      self.init_modif()
      #self.valid = 1
      #self.state = 'unchanged'

  def get_contexte_jdc(self,fichier,text):
    """ 
         Interpr�te text comme un texte de jdc et retourne le 
         contexte final
         cad le dictionnaire des sd disponibles � la derni�re �tape
         Si text n'est pas un texte de jdc valide, retourne None
         --> utilis�e par ops.POURSUITE et INCLUDE
    """
    try:
       # on essaie de cr�er un objet JDC...
       context_ini = self.parent.get_contexte_avant(self)

       CONTEXT.unset_current_step()
       j=self.jdc.definition(procedure=text,cata=self.jdc.cata,
                             nom=fichier,
                             context_ini = context_ini,
                             appli=self.jdc.appli)
       j.analyse()
       # XXX en passant par un jdc auxiliaire, on risque de rendre les etapes inactives
       # on les force dans l'etat actif
       for etape in j.etapes:
          etape.active()
    except:
       traceback.print_exc()
       return None
    CONTEXT.set_current_step(self)
    if not j.cr.estvide():
        raise Exception("Impossible de relire le fichier\n"+str(j.cr))

    #XXX la validit� d'un source inclus n'est pas identique � celle d'un JDC complet
    #    impossible de la tester en dehors du JDC d'accueil
    #cr=j.report()
    #if not cr.estvide():
    #    raise Exception("Le fichier contient des erreurs\n"+str(j.cr))
    j_context=j.get_contexte_avant(None)
    # XXX j.g_context doit donner le meme r�sultat
    # On retourne le contexte apres la derniere etape
    # XXX j.supprime() ???
    self.verif_contexte(j_context)
    # Le contexte est acceptable. On r�cup�re les �tapes internes (pour validation)
    self.etapes=j.etapes
    return j_context

  def verif_contexte(self,context):
     """
         On verifie que le contexte context peut etre ins�r� dans le jeu
         de commandes � la position de self
     """
     for nom_sd,sd in context.items():
        if not isinstance(sd,ASSD):continue
        if self.parent.get_sd_apres_etape(nom_sd,etape=self):
           # Il existe un concept apres self => impossible d'inserer
           raise Exception("Impossible d'inclure le fichier. Un concept de nom " + 
                           "%s existe d�j� dans le jeu de commandes." % nom_sd)

  def reevalue_sd_jdc(self):
     """
         Avec la liste des SD qui ont �t� supprim�es, propage la 
         disparition de ces SD dans totues les �tapes et descendants
     """
     l_sd = self.diff_contextes()
     if len(l_sd) == 0 : return
     for sd in l_sd:
        self.jdc.delete_concept(sd)

  def diff_contextes(self):
     """ 
         R�alise la diff�rence entre les 2 contextes 
         old_contexte_fichier_init et contexte_fichier_init
         cad retourne la liste des sd qui ont disparu 
     """
     if not hasattr(self,'old_contexte_fichier_init'):return []
     l_sd_suppressed = []
     for old_key in self.old_contexte_fichier_init.keys():
       if not self.contexte_fichier_init.has_key(old_key):
         if isinstance(self.old_contexte_fichier_init[old_key],ASSD):
           l_sd_suppressed.append(self.old_contexte_fichier_init[old_key])
     return l_sd_suppressed
      
  def supprime_sdprods(self):
      """
          Fonction:
            Lors d'une destruction d'etape, detruit tous les concepts produits
            Un op�rateur n a qu un concept produit
            Une procedure n'en a aucun
            Une macro en a en g�n�ral plus d'un
      """
      if not self.is_reentrant() :
         # l'�tape n'est pas r�entrante
         # le concept retourn� par l'�tape est � supprimer car il �tait
         # cr�� par l'�tape
         if self.sd != None :
            self.parent.del_sdprod(self.sd)
            self.parent.delete_concept(self.sd)
      # On d�truit les concepts � droite du signe =
      for co in self.sdprods:
         self.parent.del_sdprod(co)
         self.parent.delete_concept(co)
      # Si la macro a des etapes et des concepts inclus, on les detruit
      for nom_sd,co in self.g_context.items():
         if not isinstance(co,ASSD):continue
         print "Delete: ",self.nom,co.nom
         self.parent.del_sdprod(co)
         self.parent.delete_concept(co)
      # On met g_context � blanc
      self.g_context={}
         
  def Build_sd(self,nom):
     """
        Construit le concept produit de l'op�rateur. Deux cas 
        peuvent se pr�senter :

        - le parent n'est pas d�fini. Dans ce cas, l'�tape prend en charge 
          la cr�ation et le nommage du concept.

        - le parent est d�fini. Dans ce cas, l'�tape demande au parent la 
          cr�ation et le nommage du concept.

     """
     if not self.isactif():return
     # CCAR : meme modification que dans I_ETAPE
     if not self.isvalid(sd='non') : return
     else:self.state='undetermined'
     try:
        # On positionne la macro self en tant que current_step pour que les 
        # �tapes cr��es lors de l'appel � sd_prod et � op_init aient la macro
        #  comme parent 
        self.set_current_step()
        if self.parent:
           sd= self.parent.create_sdprod(self,nom)
           if type(self.definition.op_init) == types.FunctionType: 
              apply(self.definition.op_init,(self,self.parent.g_context))
        else:
           sd=self.get_sd_prod()
           if sd != None and self.reuse == None:
              # On ne nomme le concept que dans le cas de non reutilisation 
              # d un concept
              sd.nom=nom
        self.reset_current_step()
        if self.jdc and self.jdc.par_lot == "NON" :
           self.Execute()
        return sd
     except AsException,e:
        self.reset_current_step()
        raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                             'fichier : ',self.appel[1],e)
     except EOFError:
        #self.reset_current_step()
        raise
     except :
        self.reset_current_step()
        l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
        raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                          'fichier : ',self.appel[1]+'\n',
                           string.join(l))
