#@ MODIF cataelem Messages  DATE 18/09/2007   AUTEUR DURAND C.DURAND 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2006  EDF R&D                  WWW.CODE-ASTER.ORG
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
 l option :  %(k1)s  est probablement compos�e (vieillot)
"""),

2: _("""
 l option :  %(k1)s  a plusieurs param�tres de memes noms.
"""),

3: _("""
 mode local incorrect
 pour le param�tre:  %(k1)s
 pour l'option    :  %(k2)s
 pour le type     :  %(k3)s 
"""),

4: _("""
 le param�tre :  %(k1)s  pour l'option :  %(k2)s
 existe pour le type :  %(k3)s mais n'existe pas dans l'option.
"""),

5: _("""
 le param�tre :  %(k1)s  pour l'option :  %(k2)s  et pour le TYPE_ELEMENT :  %(k3)s
 n'est pas associe � la bonne grandeur.
"""),

6: _("""
 le param�tre :  %(k1)s  pour l'option :  %(k2)s  et pour le TYPE_ELEMENT :  %(k3)s
 n'a pas le bon nombre de noeuds.
"""),

7: _("""
 le param�tre :  %(k1)s  pour l option :  %(k2)s  et pour le TYPE_ELEMENT :  %(k3)s 
 n'est pas du bon type:  %(k4)s 
"""),

8: _("""
 les grandeurs : %(k1)s  et  %(k2)s  doivent avoir exactement les memes cmps.
"""),

9: _("""
 erreurs de coh�rence dans les catalogues d'�lements finis.
"""),

20: _("""
 Erreur lors de l'acc�s � la composante %(i1)d dans le champ de nom %(k1)s et de type %(k2)s.
 Les arguments sont hors bornes ou la composante est d�j� affect�e (�crasement).
 Contactez le support.
"""),

}