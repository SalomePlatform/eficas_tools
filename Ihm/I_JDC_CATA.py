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
from Noyau import N_JDC_CATA

class JDC_CATA:
  def __init__(self):
    self.l_noms_entites=[]

#ATTENTION SURCHARGE: cette methode doit etre synchronisée avec celle du Noyau
  def enregistre(self,commande):
    """ 
        Cette méthode surcharge la méthode de la classe du Noyau
        Marche avec Noyau mais si un autre package l'a déjà surchargée ???
    """
    N_JDC_CATA.JDC_CATA.enregistre(self,commande)
    self.l_noms_entites.append(commande.nom)

  def get_liste_cmd(self):
    self.l_noms_entites.sort()
    return self.l_noms_entites

