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
   Ce module contient la classe 3Dpilote qui va creer les ordres 
   de pilotage de l idl PAL pour un element de structure
"""
import generator

class TroisDPilote:

   def __init__(self,node,appli):
      self.node=node
      self.appli=appli

   def envoievisu(self):
      """ 
      """
      format="vers3DSalome"
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         g=generator.plugins[format]()
         g.init_jdc(self.node.get_jdc())
         texte=g.gener(self.node)
      else:
         print "Le generateur n a pas ete trouvé"
         print "Erreur ! Erreur!"
         return ""
      self.appli.envoievisu(texte)

