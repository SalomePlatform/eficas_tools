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
Ce module contient la classe PARAMETRE_EVAL qui sert � d�finir
des objets param�tres qui sont compr�hensibles et donc affichables
par EFICAS.
Ces objets sont cr��s � partir de la modification du fichier de commandes
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
  Cette classe permet de cr�er des objets de type PARAMETRE_EVAL
  cad des affectations directes �valu�es dans le jeu de commandes (ex: a=EVAL('''10.*SQRT(25)'''))
  qui sont interpr�t�es par le parseur de fichiers Python.
  Les objets ainsi cr��s constituent des param�tres �valu�s pour le jdc
  """
  nature = 'PARAMETRE_EVAL'
  idracine='param_eval'

  def __init__(self,nom,valeur=None):
    # parent ne peut �tre qu'un objet de type JDC
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
        Retourne le nom du param�tre �valu� comme repr�sentation de self
    """
    return self.nom

  def interprete_valeur(self,val):
    """
    Essaie d'interpr�ter val (cha�ne de caract�res ou None) comme :
    une instance de Accas.EVAL
    Retourne la valeur interpr�t�e
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
        print "Le texte %s n'est pas celui d'un param�tre �valu�" %val
        return None

  def set_valeur(self,new_valeur):
    """
    Remplace la valeur de self par new_valeur interpr�t�e.
    """
    self.valeur = self.interprete_valeur(new_valeur)
    self.val = new_valeur
    self.init_modif()

  def get_nom(self) :
    """
    Retourne le nom du param�tre
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
    Cette m�thode a pour but de v�rifier si l'expression EVAL
    est syntaxiquement correcte.
    Retourne :
        - un bool�en, qui vaut 1 si licite, 0 sinon
        - un message d'erreurs ('' si illicite)
    """
    if not exp_eval:
        if self.valeur :
            exp_eval = self.valeur.valeur[3:-3] # on enl�ve les triples guillemets
        else:
            exp_eval = None
    if exp_eval :
        # on construit un interpr�teur de formule
        formule=(self.nom,'',None,exp_eval)
        # on r�cup�re la liste des constantes et des autres fonctions pr�d�finies
        # et qui peuvent �tre utilis�es dans le corps de la formule courante
        l_ctes,l_form = self.jdc.get_parametres_fonctions_avant_etape(self)
        # on cr�e un objet v�rificateur
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
           self.cr.fatal("Le param�tre EVAL %s ne peut valoir None" % self.nom)
        return 0,"Le param�tre EVAL ne peut valoir None"

  def verif_nom(self,nom=None,cr='non'):
    """
    V�rifie si le nom pass� en argument (si aucun prend le nom courant)
    est un nom valide pour un param�tre EVAL
    Retourne :
        - un bool�en, qui vaut 1 si nom licite, 0 sinon
        - un message d'erreurs ('' si illicite)
    """
    if not nom :
        nom = self.nom
    if nom == "" :
        if cr == 'oui' : self.cr.fatal("Pas de nom donn� au param�tre EVAL")
        return 0,"Pas de nom donn� au param�tre EVAL"
    if len(nom) > 8 :
        if cr == 'oui' : self.cr.fatal("Un nom de param�tre ne peut d�passer 8 caract�res")
        return 0,"Un nom de param�tre ne peut d�passer 8 caract�res"
    sd = self.parent.get_sd_autour_etape(nom,self)
    if sd :
        if cr == 'oui' : self.cr.fatal("Un concept de nom %s existe d�j� !" %nom)
        return 0,"Un concept de nom %s existe d�j� !" %nom
    return 1,''

  def verif_parametre_eval(self,param=None,cr='non'):
    """
    V�rifie la validit� du param�tre EVAL pass� en argument.
    Ce nouveau param�tre est pass� sous la forme d'un tuple : (nom,valeur)
    Si aucun tuple pass�, prend les valeurs courantes de l'objet
    Retourne :
            - un bool�en, qui vaut 1 si EVAL licite, 0 sinon
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
    # message d'erreurs global = concat�nation des messages partiels
    erreur = ''
    if not test :
        for mess in (erreur_nom,erreur_eval):
            erreur = erreur+(len(mess) > 0)*'\n'+mess
    return test,erreur

  def update(self,param):
    """
    M�thode externe.
    Met � jour les champs nom, valeur de self
    par les nouvelles valeurs pass�es dans le tuple formule.
    On stocke les valeurs SANS v�rifications.
    """
    self.init_modif()
    self.set_nom(param[0])
    self.set_valeur('EVAL("""'+param[1]+'""")')

  def isvalid(self,cr='non'):
    """
    Retourne 1 si self est valide, 0 sinon
    Un param�tre �valu� est consid�r� comme valide si :
      - il a un nom
      - il a une valeur qui est interpr�table par l'interpr�teur de FORMULEs
    """
    resu,erreur= self.verif_parametre_eval(cr=cr)
    return resu

  def report(self):
    """
        G�n�re l'objet rapport (classe CR)
    """
    self.cr = CR()
    self.isvalid(cr='oui')
    return self.cr

  def set_nom(self,new_nom):
    """
    Remplace le nom de self par new_nom
    """
    self.nom = new_nom


