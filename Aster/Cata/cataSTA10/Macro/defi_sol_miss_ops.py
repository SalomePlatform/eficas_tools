#@ MODIF defi_sol_miss_ops Macro  DATE 14/06/2010   AUTEUR COURTOIS M.COURTOIS 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2010  EDF R&D                  WWW.CODE-ASTER.ORG
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
# ======================================================================
# RESPONSABLE COURTOIS M.COURTOIS

import os

def defi_sol_miss_ops(self, MATERIAU, COUCHE, TITRE, INFO, **args):
   """Macro DEFI_SOL_MISS :
   d�finir les caract�ristiques du sol pour un calcul MISS3D
   """
   import aster

   from Accas              import _F
   from Utilitai.Utmess    import UTMESS
   from Utilitai.Table     import Table
   CREA_TABLE    = self.get_cmd("CREA_TABLE")

   ier = 0
   # La macro compte pour 1 dans la numerotation des commandes
   self.set_icmd(1)

   # Le concept sortant (de type table_sdaster) est tabout
   self.DeclareOut("tabout", self.sd)

   # 1. Cr�ation des dictionnaires des MATERIAUX
   l_mate = []
   for Mi in MATERIAU:
      dM = Mi.cree_dict_valeurs(Mi.mc_liste)
      l_mate.append(dM)
   nb_mate = len(l_mate)

   # 2. Cr�ation des dictionnaires des COUCHES
   l_couche = []
   n_substr = 0
   for Ci in COUCHE:
      dC = Ci.cree_dict_valeurs(Ci.mc_liste)
      if dC.get("SUBSTRATUM") == "OUI":
         n_substr += 1
      l_couche.append(dC)
   if n_substr != 1:
      UTMESS("F", "MISS0_3")
   nb_couche = len(l_couche)

   # 3. d�finition de la table
   # para/typ pr�-trie les colonnes
   tab = Table(para=["NUME_COUCHE", "EPAIS", "RHO", "E", "NU", "AMOR_HYST", "RECEPTEUR", "SOURCE", "NUME_MATE", "SUBSTRATUM"],
               typ=["I", "R", "R", "R", "R", "R", "K8", "K8", "I", "K8"])
   idc = 0
   for couche in l_couche:
      idc += 1
      id_mate = couche["NUME_MATE"]
      if id_mate > nb_mate:
         UTMESS("F", "MISS0_4", vali=(idc, nb_mate, id_mate))
      id_mate = id_mate - 1
      couche["NUME_COUCHE"] = idc
      couche.update(l_mate[id_mate])
      if couche.get("SUBSTRATUM") is None:
         del couche["SUBSTRATUM"]
      if couche["EPAIS"] is None:
         couche["EPAIS"] = 0.
      tab.append(couche)

   # 4. surcharge par le titre fourni
   if TITRE != None:
      if type(TITRE) not in (list, tuple):
         TITRE = [TITRE]
      tab.titr = os.linesep.join(TITRE)

   if INFO == 2:
      print tab

   # 5. cr�ation de la table
   dprod = tab.dict_CREA_TABLE()
   tabout = CREA_TABLE(**dprod)

