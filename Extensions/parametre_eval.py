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
Ce module contient la classe PARAMETRE_EVAL qui sert à définir
des objets paramètres qui sont compréhensibles et donc affichables
par EFICAS.
Ces objets sont créés à partir de la modification du fichier de commandes
de l'utilisateur par le parseur de fichiers Python
"""
# import de modules Python
import string,types,re
import traceback

# import modules Eficas
import interpreteur_formule
from Noyau.N_CR import CR
import parametre

pattern_eval       = re.compile(r'^(EVAL)([ \t\r\f\v]*)\(([\w\W]*)')

class PARAMETRE_EVAL(parametre.PARAMETRE) :
  """
  Cette classe permet de créer des objets de type PARAMETRE_EVAL
  cad des affectations directes évaluées dans le jeu de commandes (ex: a=EVAL('''10.*SQRT(25)'''))
  qui sont interprétées par le parseur de fichiers Python.
  Les objets ainsi créés constituent des paramètres évalués pour le jdc
  """
  nature = 'PARAMETRE_EVAL'
  idracine='param_eval'

  def __init__(self,nom,valeur=None):
    # parent ne peut être qu'un objet de type JDC
    import Accas
    self.Accas_EVAL=Accas.EVAL
    self.valeur = self.interprete_valeur(valeur)
    self.val    = valeur
    self.nom = nom
    self.jdc = self.parent = CONTEXT.get_current_step()
    self.definition=self
    self.niveau = self.parent.niveau
    self.actif=1
    self.state='undetermined'
    # Ceci est-il indispensable ???
    #self.appel = N_utils.callee_where(niveau=2)
    self.register()

  def __repr__(self):
    """
        Donne un echo de self sous la forme nom = valeur
    """
    return self.nom+' = '+ repr(self.valeur) 

  def __str__(self):
    """
        Retourne le nom du paramètre évalué comme représentation de self
    """
    return self.nom

  def interprete_valeur(self,val):
    """
    Essaie d'interpréter val (chaîne de caractères ou None) comme :
    une instance de Accas.EVAL
    Retourne la valeur interprétée
    """
    if not val : return None
    d={}
    val = string.strip(val)
    if val[-1] == ';' : val = val[0:-1]
    d['EVAL'] = self.Accas_EVAL
    try:
        valeur = eval(val,{},d)
        return valeur
    except:
        traceback.print_exc()
        print "Le texte %s n'est pas celui d'un paramètre évalué" %val
        return None

  def set_valeur(self,new_valeur):
    """
    Remplace la valeur de self par new_valeur interprétée.
    """
    self.valeur = self.interprete_valeur(new_valeur)
    self.val = new_valeur
    self.init_modif()

  def get_nom(self) :
    """
    Retourne le nom du paramètre
    """
    return self.nom

  def get_valeur(self):
    """
    Retourne la valeur de self, cad le texte de l'objet class_eval.EVAL
    """
    if self.valeur :
        return self.valeur.valeur
    else:
        return ''

  def verif_eval(self,exp_eval=None,cr='non'):
    """
    Cette méthode a pour but de vérifier si l'expression EVAL
    est syntaxiquement correcte.
    Retourne :
        - un booléen, qui vaut 1 si licite, 0 sinon
        - un message d'erreurs ('' si illicite)
    """
    if not exp_eval:
        if self.valeur :
            exp_eval = self.valeur.valeur[3:-3] # on enlève les triples guillemets
        else:
            exp_eval = None
    if exp_eval :
        # on construit un interpréteur de formule
        formule=(self.nom,'',None,exp_eval)
        # on récupère la liste des constantes et des autres fonctions prédéfinies
        # et qui peuvent être utilisées dans le corps de la formule courante
        l_ctes,l_form = self.jdc.get_parametres_fonctions_avant_etape(self)
        # on crée un objet vérificateur
        verificateur = interpreteur_formule.Interpreteur_Formule(formule=formule,
                                                                 constantes = l_ctes,
                                                                 fonctions = l_form)
        if cr == 'oui' :
          if not verificateur.cr.estvide():
            self.cr.fatal(verificateur.cr.get_mess_fatal())
        return verificateur.isvalid(),string.join(verificateur.cr.crfatal)
    else:
        # pas d'expression EVAL --> self non valide
        if cr == 'oui' : 
           self.cr.fatal("Le paramètre EVAL %s ne peut valoir None" % self.nom)
        return 0,"Le paramètre EVAL ne peut valoir None"

  def verif_nom(self,nom=None,cr='non'):
    """
    Vérifie si le nom passé en argument (si aucun prend le nom courant)
    est un nom valide pour un paramètre EVAL
    Retourne :
        - un booléen, qui vaut 1 si nom licite, 0 sinon
        - un message d'erreurs ('' si illicite)
    """
    if not nom :
        nom = self.nom
    if nom == "" :
        if cr == 'oui' : self.cr.fatal("Pas de nom donné au paramètre EVAL")
        return 0,"Pas de nom donné au paramètre EVAL"
    if len(nom) > 8 :
        if cr == 'oui' : self.cr.fatal("Un nom de paramètre ne peut dépasser 8 caractères")
        return 0,"Un nom de paramètre ne peut dépasser 8 caractères"
    sd = self.parent.get_sd_autour_etape(nom,self)
    if sd :
        if cr == 'oui' : self.cr.fatal("Un concept de nom %s existe déjà !" %nom)
        return 0,"Un concept de nom %s existe déjà !" %nom
    return 1,''

  def verif_parametre_eval(self,param=None,cr='non'):
    """
    Vérifie la validité du paramètre EVAL passé en argument.
    Ce nouveau paramètre est passé sous la forme d'un tuple : (nom,valeur)
    Si aucun tuple passé, prend les valeurs courantes de l'objet
    Retourne :
            - un booléen, qui vaut 1 si EVAL licite, 0 sinon
            - un message d'erreurs ('' si illicite)
    """
    if not param :
        if self.valeur :
            param = (self.nom,self.valeur.valeur)
        else:
            param = (self.nom,None)
    test_nom,erreur_nom   = self.verif_nom(param[0],cr=cr)
    test_eval,erreur_eval = self.verif_eval(param[1],cr=cr)
    # test global = produit des tests partiels
    test = test_nom*test_eval
    # message d'erreurs global = concaténation des messages partiels
    erreur = ''
    if not test :
        for mess in (erreur_nom,erreur_eval):
            erreur = erreur+(len(mess) > 0)*'\n'+mess
    return test,erreur

  def update(self,param):
    """
    Méthode externe.
    Met à jour les champs nom, valeur de self
    par les nouvelles valeurs passées dans le tuple formule.
    On stocke les valeurs SANS vérifications.
    """
    self.init_modif()
    self.set_nom(param[0])
    self.set_valeur('EVAL("""'+param[1]+'""")')

  def isvalid(self,cr='non'):
    """
    Retourne 1 si self est valide, 0 sinon
    Un paramètre évalué est considéré comme valide si :
      - il a un nom
      - il a une valeur qui est interprétable par l'interpréteur de FORMULEs
    """
    resu,erreur= self.verif_parametre_eval(cr=cr)
    return resu

  def report(self):
    """
        Génère l'objet rapport (classe CR)
    """
    self.cr = CR()
    self.isvalid(cr='oui')
    return self.cr

  def set_nom(self,new_nom):
    """
    Remplace le nom de self par new_nom
    """
    self.nom = new_nom


