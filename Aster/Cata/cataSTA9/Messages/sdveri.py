#@ MODIF sdveri Messages  DATE 19/02/2008   AUTEUR COURTOIS M.COURTOIS 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2007  EDF R&D                  WWW.CODE-ASTER.ORG
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

def _(x) : return x

cata_msg = {

1 : _("""
 Impossible d'importer le catalogue de la structure de donn�es '%(k1)s'
"""),

2 : _("""
 Objet %(k1)s inexistant.
"""),

4 : _("""
 Arguments incoh�rents :
      Nom des param�tres : %(k1)s
   Valeur des param�tres : %(k2)s
"""),

5 : _("""
 Arguments invalide : 'nomres' vide !
"""),

30 : _("""
 Erreur de programmation (catalogue des SD) :
   V�rification d'une structure de donn�e :
   certains objets JEVEUX sont incorrects :
"""),

31 : _("""
      Objet : '%(k1)s'    Message : %(k2)s
"""),

32 : _("""
      Fin Message 30
"""),

40 : _("""
 Erreur de programmation (catalogue des SD) :
   V�rification d'une structure de donn�e :
   Les objets suivants sont interdits dans les SD de type : %(k1)s
"""),

41 : _("""
   Objet '%(k1)s'   INTERDIT
"""),

42 : _("""
      Fin Message 40
"""),

45 : _("""
      Erreur Python : voir traceback ci-dessous
"""),

}