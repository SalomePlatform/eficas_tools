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
"""
import string,traceback

from Accas import MACRO_ETAPE,MACRO
from Extensions import interpreteur_formule


class FORM_ETAPE(MACRO_ETAPE):

    interpreteur = interpreteur_formule.Interpreteur_Formule

    def McBuild(self):
        self.mc_liste=self.build_mc()
        # on cr�e la liste des types autoris�s (liste des noms de mots-cl�s
        # simples dans le catalogue de FORMULE)
        self.l_types_autorises = self.definition.entites.keys()
        # en plus de la construction traditionnelle des fils de self
        # il faut pour les FORMULE d�cortiquer l'expression ...
        self.type_retourne,self.arguments,self.corps = self.analyse_formule()

    def analyse_formule(self):
        """
        Cette m�thode d�cortique l'expression de la FORMULE.
        Elle retourne 3 valeurs:
            - le type retourn� par la FORMULE
            - les arguments de la FORMULE
            - le corps de la FORMULE, cad son expression
        """
        if len(self.mc_liste) == 0:
            # pas de fils pour self --> la FORMULE est incompl�te
            return None,None,None
        child = self.mc_liste[0] # child est un MCSIMP
        type_retourne = child.definition.nom
        valeur = child.getval()
        # c'est dans valeur que se trouvent la liste des arguments et le corps de la fonction
        try:
            l_args,corps = string.split(valeur,'=',1)
        except:
            # pas de signe = --> la formule est fausse
            return type_retourne,None,None
        l_args = string.strip(l_args)
        corps = string.strip(corps)
        return type_retourne,l_args,corps

    def get_nom(self):
        """
        Retourne le nom de la FORMULE, cad le nom de la SD si elle existe,
        la string vide sinon
        """
        if self.sd :
            return self.sd.get_name()
        else:
            return ''

    def get_formule(self):
        """
        Retourne un tuple d�crivant la formule :
        (nom,type_retourne,arguments,corps)
        """
        t,a,c = self.analyse_formule()
        n = self.get_nom()
        return (n,t,a,c)

    def verif_arguments(self,arguments = None):
        """
        V�rifie si les arguments pass�s en argument (si aucun prend les arguments courants)
        sont des arguments valide pour une FORMULE.
        Retourne :
            - un bool�en, qui vaut 1 si arguments licites, 0 sinon
            - un message d'erreurs ('' si illicites)
        """
        if not arguments :
            arguments = self.arguments
        if not arguments :
            return 0,"Une formule doit avoir au minimum un argument"
        # il faut au pr�alable enlever les parenth�ses ouvrantes et fermantes
        # encadrant les arguments
        arguments = string.strip(arguments)
        if arguments[0] != '(':
            return 0,"La liste des arguments d'une formule doit �tre entre parenth�ses : parenth�se ouvrante manquante"
        if arguments[-1] != ')':
            return 0,"La liste des arguments d'une formule doit �tre entre parenth�ses : parenth�se fermante manquante"
        # on peut tester la syntaxe de chaque argument maintenant
        erreur=''
        test = 1
        arguments = arguments[1:-1] # on enl�ve les parenth�ses ouvrante et fermante
        l_arguments = string.split(arguments,',')
        for argument in l_arguments:
            argument = string.strip(argument)
            try:
                typ,nom = string.split(argument,':')
                # pas de v�rification sur le nom de l'argument
                # v�rification du type de l'argument
                typ = string.strip(typ)
                if typ not in self.l_types_autorises :
                    test = 0
                    erreur = erreur + "Le type "+typ+" n'est pas un type permis pour "+nom+'\n'
            except:
                # l'argument ne respecte pas la syntaxe : typ_arg : nom_arg
                test = 0
                erreur = erreur+"Syntaxe argument non valide : "+argument+'\n'
        return test,erreur

    def verif_corps(self,corps=None,arguments=None):
        """
        Cette m�thode a pour but de v�rifier si le corps de la FORMULE
        est syntaxiquement correct.
        Retourne :
            - un bool�en, qui vaut 1 si corps de FORMULE licite, 0 sinon
            - un message d'erreurs ('' si illicite)
        """
        if not corps :
            corps = self.corps
	if not arguments :
	    arguments = self.arguments
        formule=(self.get_nom(),self.type_retourne,arguments,corps)
        # on r�cup�re la liste des constantes et des autres fonctions pr�d�finies
        # et qui peuvent �tre utilis�es dans le corps de la formule courante
        l_ctes,l_form = self.jdc.get_parametres_fonctions_avant_etape(self)
        # on cr�e un objet v�rificateur
        try:
            verificateur = self.interpreteur(formule=formule,
                                             constantes = l_ctes,
                                             fonctions = l_form)
        except :
            traceback.print_exc()
            return 0,"Impossible de r�aliser la v�rification de la formule"
        return verificateur.isvalid(),verificateur.report()

    def verif_nom(self,nom=None):
        """
        V�rifie si le nom pass� en argument (si aucun prend le nom courant)
        est un nom valide pour une FORMULE.
        Retourne :
            - un bool�en, qui vaut 1 si nom licite, 0 sinon
            - un message d'erreurs ('' si illicite)
        """
        if not nom :
            nom = self.get_nom()
        if nom == "" :
            return 0,"Pas de nom donn� � la FORMULE"
        if len(nom) > 8 :
            return 0,"Un nom de FORMULE ne peut d�passer 8 caract�res"
        sd = self.parent.get_sd_autour_etape(nom,self)
        if sd :
            return 0,"Un concept de nom %s existe d�j� !" %nom
        return 1,''

    def verif_type(self,type=None):
        """
        V�rifie si le type pass� en argument (si aucun prend le type courant)
        est un type valide pour une FORMULE.
        Retourne :
            - un bool�en, qui vaut 1 si type licite, 0 sinon
            - un message d'erreurs ('' si illicite)
        """
        if not type:
            type = self.type_retourne
        if not type :
            return 0,"Le type de la valeur retourn�e n'est pas sp�cifi�"
        if type not in self.l_types_autorises:
            return 0,"Une formule ne peut retourner une valeur de type : %s" %type
        return 1,''

    def verif_formule(self,formule=None):
        """
        V�rifie la validit� de la formule pass�e en argument.
        Cette nouvelle formule est pass�e sous la forme d'un tuple : (nom,type_retourne,arguments,corps)
        Si aucune formule pass�e, prend les valeurs courantes de la formule
        Retourne :
            - un bool�en, qui vaut 1 si formule licite, 0 sinon
            - un message d'erreurs ('' si illicite)
        """
        if not formule :
            formule = (None,None,None,None)
        test_nom,erreur_nom = self.verif_nom(formule[0])
        test_type,erreur_type = self.verif_type(formule[1])
        if formule[2]:
            args = '('+formule[2]+')'
        else:
            args = None
        test_arguments,erreur_arguments = self.verif_arguments(args)
        test_corps,erreur_corps = self.verif_corps(corps = formule[3], arguments = args)
        # test global = produit des tests partiels
        test = test_nom*test_type*test_arguments*test_corps
        # message d'erreurs global = concat�nation des messages partiels
        erreur = ''
        if not test :
            for mess in (erreur_nom,erreur_type,erreur_arguments,erreur_corps):
                erreur = erreur+(len(mess) > 0)*'\n'+mess
        return test,erreur

    def update(self,formule):
        """
        M�thode externe.
        Met � jour les champs nom, type_retourne,arguments et corps de la FORMULE
        par les nouvelles valeurs pass�es dans le tuple formule.
        On stocke les valeurs SANS v�rifications.
        """
        self.init_modif()
        self.type_retourne = formule[1]
        self.arguments = '('+formule[2]+')'
        self.corps = formule[3]
        # il faut ajouter le mot-cl� simple correspondant dans mc_liste
        # pour cela on utilise la m�thode g�n�rale build_mc
        # du coup on est oblig� de modifier le dictionnaire valeur de self ...
        self.valeur = {}
        self.valeur[self.type_retourne] = self.arguments+' = ' + self.corps
        self.McBuild()
        sd = self.get_sd_prod()
        if sd:
            sd.nom = formule[0]

    def active(self):
        """
        Rend l'etape courante active.
        Il faut ajouter la formule au contexte global du JDC
        """
        self.actif = 1
        nom = self.get_nom()
        if nom == '' : return
        try:
            self.jdc.append_fonction(self.sd)
        except:
            pass

    def inactive(self):
        """
        Rend l'etape courante inactive
        Il faut supprimer la formule du contexte global du JDC
        """
        self.actif = 0
        if not self.sd : return
        self.jdc.del_fonction(self.sd)

    def delete_concept(self,sd):
        """ 
         Inputs :
           - sd=concept detruit
         Fonction :
         Mettre a jour les mots cles de l etape et eventuellement le concept produit si reuse
         suite � la disparition du concept sd
         Seuls les mots cles simples MCSIMP font un traitement autre que de transmettre aux fils,
	 sauf les objets FORM_ETAPE qui doivent v�rifier que le concept d�truit n'est pas 
	 utilis� dans le corps de la fonction
        """
        self.init_modif()
         
    def replace_concept(self,old_sd,sd):
        """
         Inputs :
           - old_sd=concept remplace
           - sd = nouveau concept
         Fonction :
         Les objets FORM_ETAPE devraient v�rifier que le concept remplac� n'est pas
         utilis� dans le corps de la fonction
        """
        self.init_modif()

class FORM(MACRO):
   class_instance=FORM_ETAPE

