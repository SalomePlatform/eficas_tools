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
    Ce module contient la classe NIVEAU qui sert à définir
    des groupes de commandes dans le catalogue
"""

class NIVEAU:
  def __init__(self,nom='',label='',niveaux=(),valide_vide=1,actif=1):
    self.nom = nom
    self.label = label
    self.statut='o'
    self.min = 1
    self.max = 1
    self.entites = []
    self.l_noms_entites=[]
    self.valide_vide = valide_vide
    self.actif = actif
    self.d_niveaux = {}
    self.l_niveaux = niveaux
    for niveau in niveaux:
      self.d_niveaux[niveau.nom]=niveau
      self.d_niveaux.update(niveau.d_niveaux)

  def enregistre(self,commande):
    self.entites.append(commande)
    self.l_noms_entites.append(commande.nom)

  def get_liste_cmd(self):
    self.l_noms_entites.sort()
    return self.l_noms_entites

