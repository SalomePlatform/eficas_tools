#@ MODIF utilitai7 Messages  DATE 19/06/2007   AUTEUR VIVAN L.VIVAN 
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

cata_msg={

1: _("""
 Erreur dans les donn�es, le param�tre %(k1)s n'existe pas dans la table %(k2)s 
"""),

2: _("""
  Erreur dans les donn�es, pas de tri sur les complexes, param�tre:  %(k1)s 
"""),

3: _("""
  Erreur dans les donn�es, on n'a pas trouv� de ligne dans la table %(k1)s pour le param�tre %(k2)s
"""),

4: _("""
  Le num�ro d'occurrence est invalide %(i1)d pour le mot cl� facteur %(k1)s 
"""),

5: _("""
  Le num�ro de la composante (pour VARI_R) est trop grand.
    MAILLE : %(k1)s 
    NUME_MAXI : %(i1)d 
    NUME_CMP demand� : %(i2)d 
"""),

6: _("""
  Le sch�ma d'int�gration temporelle %(k1)s et le param�tre %(k2)s sont incompatibles.
"""),

7: _("""
  Le param�tre %(k1)s ne fait pas parti des choix possibles.
"""),

8: _("""
 L'utilisation de la macro pour un concept de type DYNA_HARMO n'est pas encore pr�vue
 """),

9: _("""
 Si on utilise l'option normale pour les changements de rep�re, il faut donner
 une �quation suppl�mentaire avec le mot-cl� VECT_X ou VECT_Y
 """),

10: _("""
 Seuls les champs de type ELGA (champs par �l�ment aux points de Gauss)
 sont autoris�s pour NOM_CHAM de POST_ELEM/INTEGRALE.
"""),

11: _("""
  Erreur dans les donn�es, probl�me lors du traitement du mot cl� facteur FILTRE
  
  -> Risque & Conseil :
   soit le param�tre n'existe pas
   soit aucune ligne ne correspond au param�tre donn�
"""),

99: _("""
  Arret dans le programme %(k1)s.
"""),

}