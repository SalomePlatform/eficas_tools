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
import string,re,sys,exceptions,types

from Noyau.N_CR import CR

def group(*choices): return '(' + string.join(choices, '|') + ')'
def any(*choices): return apply(group, choices) + '*'
def maybe(*choices): return apply(group, choices) + '?'

Intnumber = r'[1-9]\d*'
Exponent = r'[eEdD][-+]?\d+'
Pointfloat = group(r'\d+\.\d*', r'\.\d+') + maybe(Exponent)
Expfloat = r'[1-9]\d*' + Exponent
Floatnumber = group(Pointfloat, Expfloat)

pat_number = re.compile(r'^([+-]?)([0-9]+)(\.\d*)?(.*)')
pat_number_complet = re.compile(r'^([+-]?)([0-9]+)(\.\d*)?([eEdD][+-]?\d+)(.*)')
pat_constante = re.compile(r'^([+-]?)([a-zA-Z][a-zA-Z_0-9]*\s*)(.*)')

def cmp_function(arg1,arg2):
    """
    Fonction de comparaison permettant de classer les listes de
    fonctions unaires et binaires selon la longueur de leurs arguments
    On classe les arguments les plus longs en premier
    """
    if len(arg1) > len(arg2):
        return -1
    elif len(arg1) == len(arg2):
        return 0
    else:
        return 1
    
class InterpreteurException(exceptions.Exception):
    """
    Classe servant � d�finir les exceptions lev�es par l'interpr�teur de formule
    """
    def __init__(self,args=None):
        self.args = args

    def __str__(self):
        return self.args

class Interpreteur_Formule:
    """
    Cette classe sert � construire un interpr�teur de formules Aster
    """
    l_fonctions_binaires = ['+','-','*','/','**','=','MOD','MIN','MAX','ATAN2']
    l_fonctions_unaires = ['+','-','INT','REAL','AIMAG','ABS','SQRT','EXP','LOG',
                           'LOG10','SIN','COS','TAN','ASIN','ACOS','ATAN','SINH',
                           'COSH','TANH','HEAVYSID']
    l_constantes = ['PI','RD_RG','DG_RD']
 
    def __init__(self,formule=None,constantes=[],fonctions=[],parent=None):
        """
        Constructeur d'interpr�teurs de formule Aster
        - formule = tuple (nom,type,arguments,corps)
        - constantes = liste des noms de constantes externes
        - fonctions_unaires = dictionnaire {nom_fonction externe : nb arguments de cette fonction}
        """
        self.new_constantes = constantes
        self.new_fonctions_unaires = fonctions
        self.cr = CR()
        self.l_operateurs = []
        self.parent = parent
        self.l_children = []
        if formule :
            self.set_formule(formule)
        if self.parent :
            self.parent.enregistre(self)

    def set_formule(self,formule):
        """
        Stocke formule (tuple) dans l'attribut t_formule
        M�thode externe
        """
        if type(formule) != types.TupleType:
            raise InterpreteurException,"La formule pass�e � l'interpr�teur doit �tre sous forme de tuple"
        self.t_formule = formule
        self.init_cr()
        self.modify_listes()
        self.ordonne_listes()

    def init_cr(self):
        """
        Initialise le cr,cad valorise les cha�nes debut et fin
        """
        nom = self.t_formule[0]
        if nom :
            if nom[0] in ('+','-') : nom = nom[1:]
        self.cr.debut = "D�but Fonction %s" %nom
        self.cr.fin = "Fin Fonction %s" %nom
        
    def str(self):
        """
        Retourne une liste de cha�nes de caract�res repr�sentant la formule
        """
        l_txt = []
        l_txt.append(self.t_formule[0])
        for oper in self.l_operateurs:
            # oper est ici une liste d�crivant oper
            txt = []
            for elem in oper:
                txt.append(str(elem))
            l_txt.append(txt)
        return l_txt

    def report(self,decalage=1):
        """
        Retourne le rapport de FORMULE
        """
        txt = self.cr.report()
        return txt
    
    def enregistre(self,fils):
        """
        Enregistre un op�rateur fils dans la liste des children
        """
        self.l_children.append(fils)
        self.cr.add(fils.cr)
        
    def isvalid(self):
        """
        Bool�enne qui retourne 1 si la formule est valide, 0 sinon
        M�thode externe
        """
        self.l_operateurs = []
        self.cr.purge() # on vide le cr 
        self.init_cr() # on initialise le cr
        self.interprete_formule()
        return self.cr.estvide()

    def interprete_formule(self):
        """
        R�alise l'interpr�tation du corps de la formule
        """
        texte = self.t_formule[3]
        if not texte : return
        if type(texte) != types.ListType:
            texte = [texte,]
        for text_arg in texte:
            text_arg = string.replace(text_arg,'\n','')
            # Enleve les espaces
            text_arg = string.replace(text_arg,' ','')
            try:
                self.l_operateurs.append(self.split_operateurs(text_arg))
            except InterpreteurException,e:
                self.cr.fatal(str(e))

    def modify_listes(self):
        """
        Modifie la liste des constantes en lui ajoutant le nom des param�tres
        de la fonction � interpr�ter
        """
        args = self.t_formule[2]
        # l'interpr�teur de formule sert aussi � �valuer les EVAL
        # dans ce cas il n'y a pas d'arguments puisque pas de fonction ...
        if args :
            args = args[1:-1] # on enl�ve les parenth�ses ouvrante et fermante
            l_args = string.split(args,',')
            for arg in l_args:
                typ,nom = string.split(arg,':')
                nom = string.strip(nom)
                self.l_constantes.append(nom)
        # on consid�re que les fonctions unaires de base sont toutes � un seul argument :
        l_f = []
        self.d_fonctions_unaires = {}
        for fct in self.l_fonctions_unaires:
            self.d_fonctions_unaires[fct]=1
        # on ajoute les constantes externes
        for cte in self.new_constantes:
            self.l_constantes.append(cte)
        # on ajoute les fonctions unaires externes au dictionnaire des fonctions unaires
        for new_fonc in self.new_fonctions_unaires:
            self.d_fonctions_unaires[new_fonc[0]] = self.get_nb_args(new_fonc)
        #self.d_fonctions_unaires.update(self.new_fonctions_unaires)
        self.l_fonctions_unaires = self.d_fonctions_unaires.keys()
        
    def ordonne_listes(self):
        """
        Ordonne les listes de fonctions unaires et binaires
        """
        self.l_fonctions_binaires.sort(cmp_function)
        self.l_fonctions_unaires.sort(cmp_function)
        self.l_constantes.sort(cmp_function)
        

    def split_operateurs(self,texte):
        """
        Splite le texte pass� en argument en op�rateurs plus �l�mentaires.
        N'analyse pas l'int�rieur des op�rateurs (ne fait qu'une passe)
        """
        l_operateurs = []
        texte = string.strip(texte)
        # on recherche un nombre en d�but de texte
        try:
            oper,reste = self.cherche_nombre(texte)
        except InterpreteurException,e:
            raise InterpreteurException,str(e)
        if not oper :
            # on recherche une constante en d�but de texte
            try:
                oper,reste = self.cherche_constante(texte)
            except InterpreteurException,e:
                raise InterpreteurException,str(e)
            if not oper :
                # on recherche une expression entre parenth�ses...
                try:
                    oper,reste = self.cherche_expression_entre_parentheses(texte)
                except InterpreteurException,e:
                    raise InterpreteurException,str(e)
                if not oper :
                    # on recherche le d�but d'un op�rateur unaire en d�but de texte
                    try:
                        oper,reste = self.cherche_operateur_unaire(texte)
                    except InterpreteurException,e:
                        raise InterpreteurException,str(e)
                    if not oper :
                        type_objet,nom_objet = self.get_type(texte)
                        if type_objet == 'constante':
                            raise InterpreteurException, "Constante %s inconnue" %nom_objet
                        elif type_objet == 'fonction':
                            raise InterpreteurException, "Fonction %s inconnue dans %s" %(nom_objet,texte)
                        else:
                            raise InterpreteurException, "Impossible d'interpr�ter : %s" %texte
        # on a trouv� un op�rateur (nombre, constante ou unaire)
        # il faut encore v�rifier que l'on est en fin de texte ou qu'il est bien suivi
        # d'un op�rateur binaire
        l_operateurs.append(oper)
        if reste :
            texte = string.strip(reste)
            oper,reste = self.cherche_operateur_binaire(texte)
            if not oper :
                # on a un reste et pas d'op�rateur binaire --> erreur
                raise InterpreteurException,"L'op�rateur %s doit �tre suivi d'un op�rateur binaire" %l_operateurs[-1]
            else:
                # on a bien trouv� un op�rateur binaire:
                l_operateurs.append(oper)
                # il faut recommencer l'analyse du reste par split_operateurs ...
                try:
                    l_op = self.split_operateurs(reste)
                except InterpreteurException,e:
                    raise InterpreteurException,str(e)
                l_operateurs.extend(l_op)
                return l_operateurs
        else:
            # on a fini d'analyser texte
            return l_operateurs

    def cherche_nombre(self,texte):
        """
        Cherche un nombre en d�but de texte
        Retourne ce nombre et le reste ou None et le texte initial
        Peut lever une InterpreteurException dans le cas o� le nombre n'est pas valide
        """
        texte = string.strip(texte)
        m = pat_number_complet.match(texte)
        if m:
            # on a trouv� un nombre avec exposant
            l_groups = m.groups()
            sgn = l_groups[0]
            nb = l_groups[1]
            if l_groups[2]:
                nb = nb+l_groups[2]
            if l_groups[3]:
                nb = nb+l_groups[3]
            nombre = sgn+nb
            return nombre,l_groups[4]
        else:
            m = pat_number.match(texte)
            if m :
                # on a trouv� un nombre sans exposant
                l_groups = m.groups()
                sgn = l_groups[0]
                nb = l_groups[1]
                if l_groups[2]:
                    nb = nb+l_groups[2]
                nombre = sgn+nb
                # il faut v�rifier si ce nombre n'est pas suivi d'un exposant incomplet ...
                reste = string.strip(l_groups[3])
                if reste == '':
                    return nombre,l_groups[3]
                if reste[0] in ('e','E','d','D') :
                    raise InterpreteurException,"La syntaxe de l'exposant de %s est erron�e " %nb
                else:
                    return nombre,l_groups[3]
            else:
                # on n'a pas trouv� de nombre
                return None,texte
        
    def cherche_constante_old(self,texte):
        """
        Recherche une constante en d�but de texte parmi la liste des constantes.
        Retourne le texte repr�sentant la constante et le reste du texte ou
        Retourne None,texte si aucune constante trouv�e
        """
        txt = None
        texte = string.strip(texte)
        for cte in self.l_constantes:
            index = string.find(texte,cte)
            #if index == 0 : print 'on a trouv� %s dans %s en %d' %(cte,texte,index)
            if index == 0 :
                txt = cte
                zz,reste = string.split(texte,cte,1)
                break
        if txt :
            return txt,reste
        else:
            # aucune constante trouv�e
            return None,texte

    def cherche_constante(self,texte):
        """
        Recherche une constante en d�but de texte parmi la liste des constantes.
        Retourne le texte repr�sentant la constante et le reste du texte ou
        Retourne None,texte si aucune constante trouv�e
        """
        txt = None
        texte = string.strip(texte)
        m = pat_constante.match(texte)
        if m :
            # on a trouv� un identificateur en d�but de texte
            l_groups = m.groups()
            sgn = l_groups[0]
            identificateur = string.strip(l_groups[1])
            reste = l_groups[2]
            # il faut v�rifier qu'il ne s'agit pas d'un appel � une fonction
            if reste :
                if reste[0] == '(' :
                    # --> appel de fonction
                    return None,texte
            # il faut encore v�rifier qu'elle est bien dans la liste des constantes...
            if identificateur not in self.l_constantes :
                raise InterpreteurException,"La constante %s est inconnue dans %s" %(identificateur,texte)
            else:
                return sgn+identificateur,reste
        else:
            # aucune constante trouv�e
            return None,texte
        
    def cherche_args(self,texte):
        """
        Cherche au d�but de texte une liste d'arguments entre parenth�ses
        """
        if texte[0]!='(':
            return None,texte
        else:
            n=0
            cpt=1
            while cpt != 0:
                n=n+1
                if n>= len(texte):
                    # on a atteint la fin de texte sans avoir trouv� la parenth�se fermante --> erreur
                    raise InterpreteurException,"Manque parenth�se fermante dans %s" %texte
                if texte[n] == '(':
                    cpt=cpt+1
                elif texte[n]==')':
                    cpt=cpt-1
            if (n+1 < len(texte)):
                return texte[0:n+1],texte[n+1:]
            else:
                # on a fini d'analyser le texte : reste = None
                return texte,None
                    
    def cherche_operateur_unaire_old(self,texte):
        """
        Cherche dans texte un operateur unaire
        """
        txt = None
        texte = string.strip(texte)
        for oper in self.l_fonctions_unaires:
            index = string.find(texte,oper)
            if index == 0 :
                txt = oper
                zz,reste = string.split(texte,oper,1)
                break
        if txt :
            #print 'on a trouv� :',txt
            operateur = txt
            texte = reste
            try:
                args,reste = self.cherche_args(texte)
            except InterpreteurException,e:
                raise InterpreteurException,str(e)
            if not args :
                # op�rateur unaire sans arguments
                raise InterpreteurException,'op�rateur unaire  %s sans arguments' %operateur
            else:
                #operateur = operateur+args
                args = self.split_args(txt,args,self.d_fonctions_unaires[operateur])
                formule_operateur = (txt,'',self.t_formule[2],args)
                operateur = Interpreteur_Formule(formule = formule_operateur,
                                                 constantes = self.new_constantes,
                                                 fonctions_unaires = self.new_fonctions_unaires,
                                                 parent = self)
                operateur.interprete_formule()
                texte = reste
                return operateur,reste
        else:
            # aucun op�rateur unaire trouv�
            return None,texte

    def cherche_operateur_unaire(self,texte):
        """
        Cherche dans texte un operateur unaire
        """
        txt = None
        texte = string.strip(texte)
        m = pat_constante.match(texte)
        if m :
            # on a trouv� un identificateur en d�but de texte
            # il faut encore v�rifier que l'on a bien � faire � un appel de fonction ...
            l_groups = m.groups()
            sgn = l_groups[0]
            identificateur = string.strip(l_groups[1])
            reste = l_groups[2]
            try:
                args,reste = self.cherche_args(reste)
            except InterpreteurException,e:
                raise InterpreteurException,str(e)
            if not args :
                # op�rateur unaire sans arguments
                # en principe on ne doit jamais �tre dans ce cas car il est d�j� trapp� par cherche_constante ...
                raise InterpreteurException,'Fonction %s sans arguments !' %identificateur
            else:
                # il faut encore v�rifier que l'on a bien � faire � une fonction connue
                if identificateur not in self.l_fonctions_unaires:
                    raise InterpreteurException,'Fonction %s inconnue dans %s !' %(identificateur,texte)
                args = self.split_args(identificateur,args,self.d_fonctions_unaires[identificateur])
                formule_operateur = (sgn+identificateur,'',self.t_formule[2],args)
                operateur = Interpreteur_Formule(formule = formule_operateur,
                                                 constantes = self.new_constantes,
                                                 fonctions = self.new_fonctions_unaires,
                                                 parent = self)
                operateur.interprete_formule()
                texte = reste
                return operateur,reste
        elif texte[0] == '-':
            # Il faut pouvoir trapper les expressions du type exp(-(x+1)) ...
            try :
               args,reste = self.cherche_args(texte[1:])
            except InterpreteurException,e:
                raise InterpreteurException,str(e)
            if not args :
               # Il ne s'agit pas de '-' comme op�rateur unaire --> on retourne None
               return None,texte
            else:
               identificateur = '-'
               args = self.split_args(identificateur,args,self.d_fonctions_unaires[identificateur])
               formule_operateur = (identificateur,'',self.t_formule[2],args)
               operateur = Interpreteur_Formule(formule = formule_operateur,
                                                 constantes = self.new_constantes,
                                                 fonctions = self.new_fonctions_unaires,
                                                 parent = self)
               operateur.interprete_formule()
               texte = reste
               return operateur,reste
        else:
            return None,texte
            
    def cherche_operateur_binaire(self,texte):
        """
        Cherche dans texte un operateur unaire
        """
        txt = None
        texte = string.strip(texte)
        for oper in self.l_fonctions_binaires:
            index = string.find(texte,oper)
            #if index != -1 : print 'on a trouv� %s dans %s en %d' %(oper,texte,index)
            if index == 0 :
                txt = oper
                zz,reste = string.split(texte,oper,1)
                break
        if txt :
            return txt,reste
        else:
            # aucun op�rateur unaire trouv�
            return None,texte

    def cherche_expression_entre_parentheses(self,texte):
        """
        Cherche en d�but de texte une expression entre parentheses
        """
        args,reste = self.cherche_args(string.strip(texte))
        if not args :
            return None,texte
        else:
            # on a trouv� une expression entre parenth�ses en d�but de texte
            # --> on retourne un objet Interpreteur_Formule
            formule_operateur = ('','',self.t_formule[2],args[1:-1])
            operateur = Interpreteur_Formule(formule = formule_operateur,
                                             constantes = self.new_constantes,
                                             fonctions = self.new_fonctions_unaires,
                                             parent = self)
            operateur.interprete_formule()
            texte = reste
            return operateur,reste
            
    def split_args(self,nom_fonction,args,nb_args):
        """
        Tente de partager args en nb_args �l�ments
        Retourne une liste de cha�nes de caract�res (liste de longueur nb_args)
        """
        args = args[1:-1] # on enl�ve les parenth�ses ouvrante et fermante
        if nb_args == 1 : return args
        l_args = string.split(args,',')
        if len(l_args) != nb_args:
            raise InterpreteurException,"La fonction %s requiert %d arguments : %d fourni(s)" %(nom_fonction,nb_args,len(l_args))
        else:
            return l_args

    def get_type(self,texte):
        """
        Retourne le type de l'objet d�fini dans texte, � savoir:
        - constante
        - fonction
        - unknown
        et son nom
        """
        texte = string.strip(texte)
        if '(' not in texte:
            return 'constante',texte
        if texte[-1] != ')':
            return 'unknown',''
        nom_oper,args = string.split(texte,'(',1)
        return 'fonction',nom_oper

    def get_nb_args(self,formule):
        """
        Retourne le nombre d'arguments dans la d�finition de formule (sous forme de tuple)
        """
        args = formule[2][1:-1] # on enl�ve les parenth�ses ouvrante et fermante
        l_args = string.split(args,',')
        return len(l_args)

if __name__ == '__main__':
    constantes = ['FREQ3','AMOR1']
    fonctions_unaires=[('ACC','REEL','(REEL:x)','''bidon'''),]
    f1 = ('f1','REEL','(REEL:x)','''SIN(x)+3*x''')
    f2 = ('f2','REEL','(REEL:x)','''ATAN(x+3)+3*x''')
    f3 = ('f3','REEL','(REEL:INST)','''ACC(INST,FREQ3,AMOR1)''')
    f4 = ('f4','REEL','(REEL:INST)','''ACC(INST,FREQ2,AMOR1)''')
    f5 = ('f5','REEL','(REEL:INST,REEL:Y)','''ACC(INST,FREQ3,AMOR1)+Y*INST''')
    f6 = ('f6','REEL','(REEL:x)','''(x+ 3)/ 35.698''')
    f7 = ('f7','REEL','(REEL:x)','''(x+ 3)/ 35.698E-10''')
    f8 = ('f8','REEL','(REEL:x)','''(x+ 3)/ 35.698E''')
    f9 = ('f9','REEL','(REEL:INSTA,REEl:INSTB)','''2.*SIN((PI/4)+((INSTA-INSTB)/2.))* COS((PI/4)-((INSTA+INSTB)/2.))''')
    f10 = ('f10','REEL','(REEL:X)','''EXP(-(X+1))''')
    for formule in (f1,f2,f3,f4,f5,f6,f7,f8,f9,f10):
        i = Interpreteur_Formule(formule = formule,
                                 constantes = constantes,
                                 fonctions = fonctions_unaires)
        txt = i.str()
        print '\nformule %s = %s' %(str(formule),txt)
        if i.isvalid() :
            print "\n\tPas d'erreur !"
        else:
            print i.report()
