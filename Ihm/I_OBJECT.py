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
import string

import Noyau

class OBJECT:
  from Noyau.N_CO import CO
  from Noyau.N_ASSD import assd

  def isMCList(self):
    """ 
        Retourne 1 si self est une MCList (liste de mots-cl�s), 
                 0 sinon (d�faut) 
    """
    return 0

  def get_regles(self):
    """ 
       Retourne les r�gles de self 
    """
    if hasattr(self,'definition'):
      return self.definition.regles
    elif hasattr(self,'regles'):
      return self.regles
    else :
      return []

  def init_modif(self):
    """
       Met l'�tat de l'objet � modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    if self.parent:
      self.parent.init_modif()

  def fin_modif(self):
      """
      M�thode appel�e apr�s qu'une modification a �t� faite afin de d�clencher
      d'�ventuels traitements post-modification
      """
      # pour les objets autres que les commandes, aucun traitement sp�cifique 
      # on remonte l'info de fin de modif au parent
      if self.parent:
        self.parent.fin_modif()

  def isrepetable(self):
    """
         Indique si l'objet est r�p�table
    """
    return 0

  def liste_mc_presents(self):
    """
         Retourne la liste des noms des mots cl�s pr�sents
    """
    return []

  def get_docu(self):
    return self.definition.get_docu()

  def get_liste_mc_inconnus(self):
     """
     Retourne la liste des mots-cl�s inconnus dans self
     """
     return []

  def verif_condition_regles(self,liste_presents):
    """ 
        Retourne la liste des mots-cl�s � rajouter pour satisfaire les r�gles
        en fonction de la liste des mots-cl�s pr�sents 
    """
    liste=[]
    for regle in self.definition.regles:
        liste=regle.verif_condition_regle(liste,liste_presents)
    return liste

  def verif_condition_bloc(self):
    """ 
        Evalue les conditions de tous les blocs fils possibles 
        (en fonction du catalogue donc de la d�finition) de self et
        retourne deux listes :
        - la premi�re contient les noms des blocs � rajouter
        - la seconde contient les noms des blocs � supprimer
    """
    return [],[]

  def get_genealogie(self):
    """ 
        Retourne la liste des noms des ascendants (noms de MCSIMP,MCFACT,MCBLOC
        ou ETAPE) de self jusqu'au premier objet etape rencontr�
    """
    if self.parent:
       l=self.parent.get_genealogie()
       l.append(string.strip(self.nom))
       return l
    else:
       return [string.strip(self.nom)]

  def reparent(self,parent):
     """
         Cette methode sert a reinitialiser la parente de l'objet
     """
     self.parent=parent
     self.jdc=parent.jdc


