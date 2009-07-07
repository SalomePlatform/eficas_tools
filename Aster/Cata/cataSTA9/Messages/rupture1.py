#@ MODIF rupture1 Messages  DATE 04/02/2008   AUTEUR GALENNE E.GALENNE 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2008  EDF R&D                  WWW.CODE-ASTER.ORG
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
L'option de lissage 'LAGRANGE_REGU' n'a pas �t� d�velopp�e lorsque
le nombre de noeuds d'un fond de fissure ferm� est pair.
-> Risque et Conseil :
Veuillez utiliser une autre option de lissage
(par exemple, le lissage 'LAGRANGE' pour le champ theta)
"""),

2: _("""
%(k1)s n'est pas un GROUP_NO ou un GROUP_MA.
"""),

6: _("""
Le rayon R_SUP (ou R_SUP_FO) doit obligatoirement etre sup�rieur au rayon
R_INF (resp. R_INF_FO).
-> Risque et Conseil :
Veuillez revoir votre mise en donn�es.
"""),

7: _("""
Probl�me dans RINF et RSUP.
-> Risque et Conseil :
Veuillez revoir les valeurs fournies aux mots-cl�s R_INF ou R_INF_FO 
ou R_SUP ou R_SUP_FO.
"""),

8: _("""
Le groupe %(k1)s n'appartient pas au maillage : %(k2)s
"""),

9: _("""
Le fond de fissure n'est pas complet.
-> Risque et Conseil :
Veuillez revoir la mise en donn�es de l'op�rateur DEFI_FOND_FISS.
"""),

10: _("""
Le fond de fissure ne doit etre d�fini que par un noeud.
-> Risque et Conseil :
Veuillez revoir le contenu du mot-cl� GROUP_NO ou NOEUD ou FOND_FISS.
"""),

11: _("""
Il faut un mot cl� parmis FOND_FISS ou FISSURE pour l'option %(k1)s
Veuillez le renseigner.
"""),

12: _("""
Aucun champ initial trouv�.
"""),

13: _("""
%(k1)s : champ initial impossible avec cette option.
"""),

14: _("""
Nombre de bornes erron�.
-> Risque et Conseil :
On doit en avoir autant que de num�ros d'ordre.
"""),

15: _("""
Le r�sultat n'est pas un EVOL_NOLI.
"""),

16: _("""
Le champ %(k1)s n'a pas �t� trouv�.
"""),

17: _("""
L'association: lissage du champ THETA par les polynomes de Lagrange
               lissage de G autre que par des polynomes de Lagrange
n'est pas possible.
-> Risque et Conseil :
Veuillez consulter la documentation U4.82.03 pour d�terminer une
association satisfaisante.
"""),

19: _("""
Il faut d�finir la normale au fond de fissure.
-> Risque et Conseil :
Veuillez revoir la mise en donn�es de l'op�rateur DEFI_FOND_FISS
(mot-cl� NORMALE).
"""),

20: _("""
Une d�formation initiale est pr�sente dans la charge. Ceci est incompatible 
avec la contrainte initiale sigma_init.
-> Risque et Conseil :
On ne peut pas faire de calcul en introduisant simultan�ment une contrainte
initiale ET une d�formation initiale. Veuillez revoir les donn�es.
"""),

21: _("""
Seule une loi de comportement �lastique isotrope est valide pour
le calcul de DG.
"""),

22: _("""
Le calcul de DG n'a pas �t� �tendu � la plasticit� !
"""),

23: _("""
CALC_G - option CALC_G : d�tection de chargements non nuls sur l'axe, 
le calcul est impossible.
-> Risque et Conseil :
En 2D-axi, le calcul de G n'est pas possible pour les �l�ments de l'axe de
sym�trie si un chargement est impos� sur ceux-ci.
Modifier les couronnes R_INF et R_SUP pour qu'elles soient toutes les deux
plus petites que le rayon du fond de fissure. 
"""),

24: _("""
L'option CALC_K_G est incompatible avec les comportements incr�mentaux,
avec les comportements non lin�aires et avec la d�formation GREEN.
"""),

25: _("""
Il faut affecter les �l�ments de bord (E et NU) pour le calcul des fic.
-> Risque et Conseil :
Veuillez revoir la mise en donn�es des op�rateurs DEFI_MATERIAU
et AFFE_MATERIAU.
"""),

26: _("""
La masse volumique RHO n'a pas �t� d�finie.
-> Risque et Conseil :
Pour l'option K_G_MODA, il est indispensable de fournir la masse volumique
du mat�riau consid�r�. Veuillez revoir la mise en donn�es de l'op�rateur
DEFI_MATERIAU.
"""),

27: _("""
L'option est incompatible avec les comportements incr�mentaux ainsi
qu'avec la d�formation Green.
"""),

28: _("""
Le champ de nom symbolique %(k1)s existe d�j� dans la SD RESULTAT  %(k1)s.
"""),

29: _("""
Arret sur erreur(s) 'utilisateur': deux mailles du fond de fissure sont
non cons�cutives dans la num�rotation des noeuds.
-> Risque et Conseil :
Veuillez revoir l'ordre des mailles fournies au mot-cl� MAILLE.
"""),

30: _("""
Il faut donner 3 composantes de la direction.
-> Risque et Conseil :
Si vous utilisez CALC_THETA/THETA_2D ou CALG_G/THETA en 2d, veuillez fournir
une valeur nulle pour la 3eme composante.
"""),

31: _("""
Option non op�rationnelle:
Seule l'option COURONNE est � utiliser dans le cas ou
on emploie le mot cl� THETA_3D ou THETA_2D.
"""),

32: _("""
Option inexistante:
Seule l'option BANDE est � utiliser dans le cas ou on emploie
le mot cl� THETA_BANDE .
"""),

33: _("""
La tangente � l'origine n'est pas orthogonale � la normale au plan de la fissure.
Normale au plan :  (%(r1)f,%(r2)f,%(r3)f)
-> Risque et Conseil :
La tangente � l'origine DTAN_ORIG est n�cessairement dans le plan de la fissure, 
donc orthogonale � la normale au plan, calcul�e � partir des fonctions de niveaux
(level set) qui d�finissent la fissure. V�rifier les donn�es.
"""),

34: _("""
La tangente � l'extr�mit� n'est pas orthogonale � la normale au plan de la fissure.
Normale au plan :  (%(r1)f,%(r2)f,%(r3)f)
-> Risque et Conseil :
La tangente � l'extr�mit� DTAN_EXTR est n�cessairement dans le plan de la fissure, 
donc orthogonale � la normale au plan, calcul�e � partir des fonctions de niveaux
(level set) qui d�finissent la fissure. V�rifier les donn�es.
"""),

35: _("""
Les directions normales au plan de la fissure entre les points %(i1)d et %(i2)d successifs du fond forment un angle 
sup�rieur � 10 degr�s.
-> Risque et Conseils
L'interpolation des sauts de d�placements est bas�e sur les champs singuliers 
correspondants � une fissure plane. La fissure utilis�e ici est trop irr�guli�re et 
il y a donc un risque d'obtenir des r�sultats impr�cis.
"""),

36: _("""
La tangente � l'origine n'est pas orthogonale � la normale au plan de la fissure 
d�fini par VECT_K1.
-> Risque et Conseil :
La tangente � l'origine DTAN_ORIG est n�cessairement dans le plan de la fissure, 
donc orthogonale au VECT_K1 fourni. V�rifier les donn�es.
"""),

37: _("""
La tangente � l'extr�mit� n'est pas orthogonale � la normale au plan de la fissure 
d�fini par VECT_K1.
-> Risque et Conseil :
La tangente � l'extr�mit� DTAN_EXTR est n�cessairement dans le plan de la fissure, 
donc orthogonale au VECT_K1 fourni. V�rifier les donn�es.
"""),
}