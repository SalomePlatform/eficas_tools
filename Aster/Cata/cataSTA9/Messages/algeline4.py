#@ MODIF algeline4 Messages  DATE 02/06/2008   AUTEUR MEUNIER S.MEUNIER 
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
 Seules les m�thodes de r�solution LDLT et MULT_FRONT sont autoris�es.
"""),

3 : _("""
 Erreur lors de la r�solution d'un syst�me lin�aire (GCPC) :
 Non convergence  avec le nombre d'iterations autoris� :  %(i1)d
   norme du residu (absolu)  :  %(r1)f
   norme du residu (relatif) :  %(r2)f

 Conseils :
  * Vous pouvez augmenter le nombre d'it�rations autoris�es (SOLVEUR/NMAX_ITER).
  * Vous pouvez aussi augmenter le niveau de remplissage pour la factorisation
    incompl�te (SOLVEUR/NIVE_REMPLISSAGE).
  * Dans une commande non-lin�aire (STAT_NON_LINE par exemple) vous pouvez aussi essayer de
    diminuer la pr�cision demand�e pour la convergence (SOLVEUR/RESI_RELA), mais c'est plus
    risqu� car cela peut empecher la convergence de l'algorithme non-lin�aire.
"""),

4 : _("""
  Manque de m�moire :
     M�moire disponible = %(i1)d
     M�moire n�cessaire = %(i2)d
"""),

5 : _("""
 Erreur donn�es : noeud d�j� existant :  %(k1)s
"""),

7 : _("""
 Erreur donn�es : maille d�j� existante :  %(k1)s
"""),

9 : _("""
 Erreur donn�es GROUP_MA d�j� existant :  %(k1)s
"""),

11 : _("""
 erreur donn�es GROUP_NO d�j� existant :  %(k1)s
"""),

19 : _("""
 Matrice masse non d�finie, il faudrait essayer l'autre algorithme de r�solution.
"""),

21 : _("""
 manque de place memoire longueur de bloc insuffisante:  %(i1)d
 le super-noeud  %(i2)d
  neccessite un bloc de  %(i3)d
"""),

24 : _("""
 %(k1)s   pour le mot cle :  %(k2)s    noeud :  %(k3)s composante :  %(k4)s
"""),

25 : _("""
 combinaison non prevue   type resultat :  %(k1)s    type matrice  :  %(k2)s
    type constante:  %(k3)s
"""),

27 : _("""
 combinaison non prevue
 type r�sultat :  %(k1)s
 type matrice  :  %(k2)s
"""),

31 : _("""
 combinaison non prevue
 type r�sultat :  %(k1)s
"""),

33 : _("""
 la normalisation doit se faire en place
 il est impossible d'avoir comme concept produit  %(k1)s et %(k2)s comme concept d'entr�e.
"""),

36 : _("""
 l'option de normalisation  %(k1)s  n'est pas implant�e. %(i1)d
"""),

37 : _("""
 probl�me(s) rencontr�(s) lors de la factorisation de la matrice : %(k1)s
"""),

38 : _("""
 appel erron� :
 code retour de rsexch : %(i1)d
 pb CHAM_NO %(k1)s
"""),

42 : _("""
 pas de produit car les valeurs de la MATRICE sont  %(k1)s
 et celles du CHAM_NO sont  %(k2)s
"""),

43 : _("""
 la maille de nom  %(k1)s  existe d�j� %(k2)s
"""),

55 : _("""
 pas d'extraction pour  %(k1)s
 pour le num�ro d'ordre  %(i1)d
"""),

56 : _("""
 pas de mode extrait pour  %(k1)s
"""),

57 : _("""
 NUME_MODE identique pour le %(i1)d
 mode d'ordre  %(i2)d
"""),

58 : _("""
  probl�me dans le pr�conditionnement de la matrice MATAS par LDLT imcomplet
  pivot nul � la ligne :  %(i1)d
"""),

60 : _("""
  incoherence n2 NBDDL sans lagranges %(i1)d NBDDL reconstitu�s %(i2)d
"""),

61 : _("""
 pas de mode statique pour le noeud :  %(k1)s  et sa composante :  %(k2)s
"""),

62 : _("""
 pour les modes statiques, on attend un :  %(k1)s
 noeud :  %(k2)s
 cmp   :  %(k3)s
"""),

63 : _("""
 champ inexistant.
 champ    :  %(k1)s
 noeud    :  %(k2)s
 cmp      :  %(k3)s
"""),

64 : _("""
 d�tection d'un terme nul sur la sur diagonale
 valeur de BETA   %(r1)f
 valeur de ALPHA  %(r2)f
"""),

65 : _("""
 on a la  %(i1)d -�me fr�quence du syst�me r�duit  est complexe =  %(r1)f
  et partie_imaginaire/r�elle =  %(r2)f
"""),

66 : _("""
 la valeur propre est :   %(r1)f
"""),

68: _("""
 la valeur propre est :   %(r1)f
"""),

74 : _("""
 calcul d'erreur modale :
 une valeur propre r�elle est detectee %(k1)s � partir du couple (fr�quence, amortissement r�duit)
 on ne peut plus la reconstruire %(k2)s
 par convention l'erreur modale est fix�e � : %(r1)f
"""),

75 : _("""
 probl�me g�n�ralis� complexe
 amortissement (reduit) de d�calage sup�rieur en valeur absolue �  %(r1)f
 on le ram�ne � la valeur :  %(r2)f
"""),

76 : _("""
 la r�orthogonalisation diverge apr�s  %(i1)d  it�ration(s)   %(i2)d
"""),

77 : _("""
 l'option de normalisation  %(k1)s  n'est pas implant�e.
"""),

79 : _("""
 champ inexistant  %(k1)s impossible de r�cup�rer NEQ %(k2)s
"""),

80 : _("""
 type de valeurs inconnu   %(k1)s
"""),

81 : _("""
 champ inexistant  %(k1)s
"""),

82 : _("""
 incoh�rence de certains param�tres modaux propres � ARPACK
 num�ro d'erreur  %(i1)d
"""),

83 : _("""
 nombre de valeurs propres converg�es  %(i1)d < nombre de fr�quences demand�es  %(i2)d
 erreur ARPACK num�ro :  %(i3)d
 --> le calcul continue, la prochaine fois
 -->   augmenter DIM_SOUS_ESPACE =  %(i4)d
 -->   ou NMAX_ITER_SOREN =  %(i5)d
 -->   ou PREC_SOREN =  %(r1)f
"""),

85 : _("""
 appel erron� mode num�ro %(i1)d position modale %(i2)d
 code retour de RSEXCH : %(i3)d
 pb CHAM_NO %(k1)s
"""),

86 : _("""
 la r�orthogonalisation diverge apr�s  %(i1)d  it�ration(s) %(i2)d
       vecteur trait� :  %(i3)d
       vecteur test�  :  %(i4)d
 arret de la r�orthogonalisation %(k1)s
"""),

87 : _("""
 pour le probleme r�duit
 valeur(s) propre(s) r�elle(s)                  :  %(i1)d
 valeur(s) propre(s) complexe(s) avec conjugu�e :  %(i2)d
 valeur(s) propre(s) complexe(s) sans conjugu�e :  %(i3)d
"""),

88 : _("""
 votre probl�me est fortement amorti.
 valeur(s) propre(s) r�elle(s)                  :  %(i1)d
 valeur(s) propre(s) complexe(s) avec conjugu�e :  %(i2)d
 valeur(s) propre(s) complexe(s) sans conjugu�e :  %(i3)d
"""),

94 : _("""
 probl�me quadratique complexe
 amortissement (r�duit) de d�calage sup�rieur en valeur absolue �  %(r1)f
 on le ram�ne � la valeur :  %(r2)f
"""),

95 : _("""
 probl�me quadratique
 amortissement (r�duit) de d�calage sup�rieur en valeur absolue �  %(r1)f
 on le ram�ne � la valeur :  %(r2)f
"""),

98 : _("""
 nombre de valeurs propres converg�es  %(i1)d < nombre de fr�quences demand�es  %(i2)d
 erreur ARPACK num�ro :  %(i3)d
 --> le calcul continue, la prochaine fois
 -->   augmenter DIM_SOUS_ESPACE =  %(i4)d
 -->   ou NMAX_ITER_SOREN =  %(i5)d
 -->   ou PREC_SOREN =  %(r1)f
 si votre probl�me est fortement amorti, il est possible que
 des modes propres non calcul�s soient sur-amortis
 --> diminuez le nombre de fr�quences demand�es
"""),

}