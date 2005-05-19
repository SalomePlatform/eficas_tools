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
import CONNECTOR
import I_MCCOMPO

class MCFACT(I_MCCOMPO.MCCOMPO):
  def isrepetable(self):
     """ 
         Indique si l'objet est r�p�table.
         Retourne 1 si le mot-cl� facteur self peut �tre r�p�t�
         Retourne 0 dans le cas contraire
     """
     if self.definition.max > 1:
       # marche avec '**'
       return 1
     else :
       return 0

  def isoblig(self):
    return self.definition.statut=='o'

  def getlabeltext(self):
    """
       Retourne le label de self suivant qu'il s'agit d'un MCFACT
       isol� ou d'un MCFACT appartenant � une MCList :
       utilis�e pour l'affichage dans l'arbre
    """
    objet = self.parent.get_child(self.nom)
    # objet peut-�tre self ou une MCList qui contient self ...
    if objet is None or objet is self:
      return "Erreur - mclist inexistante: "+self.nom

    try:
      if len(objet) > 1 :
        index = objet.get_index(self)+1 # + 1 � cause de la num�rotation qui commence � 0
        return self.nom +'_'+`index`+':'
      else:
        return self.nom
    except:
        return "Erreur - mot cl� facteur de nom: "+self.nom

  def init_modif(self):
    """
       Met l'�tat de l'objet � modified et propage au parent
       qui vaut None s'il n'existe pas
    """
    self.state = 'modified'
    parent= hasattr(self,"alt_parent") and self.alt_parent or self.parent
    if parent:
       parent.init_modif()

  def fin_modif(self):
    """
      M�thode appel�e apr�s qu'une modification a �t� faite afin de d�clencher
      d'�ventuels traitements post-modification
    """
    #print "fin_modif",self
    # pour les objets autres que les commandes, aucun traitement sp�cifique
    # on remonte l'info de fin de modif au parent
    CONNECTOR.Emit(self,"valid")
    parent= hasattr(self,"alt_parent") and self.alt_parent or self.parent
    if parent:
       parent.fin_modif()

