#@ MODIF parseur_python Parsers  DATE 05/09/2001   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
# ======================================================================
import sys,string,re

class ENTITE_JDC :
    def __init__(self,pere):
        self.texte = ''
        pere.l_objets.append(self)

    def set_text(self,texte):
        self.texte = texte

    def append_text(self,texte):
        """
        Ajoute texte � self.texte en mettant un retour chariot � la fin de texte
        """
        texte = texte+'\n'
        self.texte = self.texte +texte

class COMMENTAIRE(ENTITE_JDC):

    def __str__(self):
        """
        Retourne une cha�ne de caract�res repr�sentants self
        sous une forme interpr�table par EFICAS
        """
        s='COMMENTAIRE("""'+self.texte+'""")\n\n'
        return s

    def append_text(self,texte):
        """
        Ajoute texte � self.texte en enlevant le # initial
        """
        texte = texte+'\n'
        if texte[0] == '#':
            self.texte = self.texte+texte[1:]
        else:
            # le di�se n'est pas sur le premier caract�re
            amont,aval = string.split(texte,'#',1) # on d�coupe suivant la premi�re occurrence de #
            self.texte = self.texte +amont + aval
        
class COMMANDE(ENTITE_JDC):

    def __str__(self):
        """
        Retourne self.texte
        """
        return self.texte+'\n'
        
    def get_nb_par(self):
        """
        Retourne la diff�rence entre le nombre de parenth�ses ouvrantes
        et le nombre de parenth�ses fermantes pr�sentes dans self.texte
        Peut donc retourner un entier n�gatif
        """
        # faire attention aux commentaires contenus dans self.texte
        # qui peuvent eux-m�mes contenir des parenth�ses !!!!
        l_lignes = string.split(self.texte,'\n')
        nb = 0
        for ligne in l_lignes:
            ligne = string.split(ligne,'#')[0]
            nb = nb + (string.count(ligne,'(')-string.count(ligne,')'))
        return nb

class AFFECTATION(ENTITE_JDC):

    def append_text(self,texte):
        """
        Ajoute texte � self.texte en enlevant tout retour chariot et tout point virgule
        """
        if texte[-1] == '\n' : texte = string.strip(texte[0:-1])
        if texte[-1] == ';' : texte = string.strip(texte[0:-1])
        self.texte = self.texte+texte
        
    def __str__(self):
        """
        Retourne une expression de l'affectation compr�hensible par ACCAS
        et exploitable par EFICAS
        """
        nom,valeur = string.split(self.texte,'=',1)
        nom = string.strip(nom)
        if valeur[-1] == '\n': valeur = valeur[:-1]
        valeur = string.strip(valeur)
        return nom+' = PARAMETRE(nom=\''+nom+'\',valeur="'+valeur+'")\n\n'

class COMMANDE_COMMENTARISEE(ENTITE_JDC):

    def append_text(self,texte):
        """
        Ajoute texte � self.texte en enlevant les doubles commentaires
        """
        texte = string.strip(texte)
        texte = string.strip(texte[2:])
        self.texte = self.texte+(len(self.texte)>0)*'\n'+texte

    def __str__(self):
        """
        Retourne une expression de la commande commentaris�e compr�hensible par ACCAS
        et exploitable par EFICAS
        """
        return "COMMANDE_COMM(texte='''"+self.texte+"''')\n"

class AFFECTATION_EVAL(ENTITE_JDC):

    def append_text(self,texte):
        """
        Ajoute texte � self.texte en enlevant tout retour chariot
        """
        if texte[-1] == '\n' : texte = texte[1:-1]
        self.texte = self.texte+texte
        
    def __str__(self):
        """
        Retourne une expression du param�tre EVAL compr�hensible par ACCAS
        et exploitable par EFICAS
        """
        nom,valeur = string.split(self.texte,'=',1)
        nom = string.strip(nom)
        if valeur[-1] == '\n': valeur = valeur[:-1]
        valeur = string.strip(valeur)
        return nom+' = PARAMETRE_EVAL(nom=\''+nom+'\',valeur=\''+valeur+'\')\n\n'
        
class PARSEUR_PYTHON:
    """
    Cette classe sert � g�n�rer un objet PARSEUR_PYTHON qui r�alise l'analyse d'un texte 
    repr�sentant un JDC Python en distinguant :
    - les commentaires inter commandes
    - les affectations
    - les commandes
    """
    pattern_commande   = re.compile(r'^([A-Z][A-Z0-9_]+)([ \t\r\f\v]*)\(([\w\W]*)')
    pattern_eval       = re.compile(r'^(EVAL)([ \t\r\f\v]*)\(([\w\W]*)')
    pattern_ligne_vide = re.compile(r'^[\t\r\f\v\n]+')
    
    def __init__(self,texte):
        self.texte = texte
        self.l_objets=None

    def is_affectation(self,texte):
        """
        M�thode bool�enne qui retourne 1 si le texte est celui d'une affectation dans un jeu de commandes
        Aster, 0 sinon
        """
        if '=' not in texte : return 0
        if self.pattern_commande.match(texte):
            # cas d'une proc�dure ...
            return 0
        amont,aval = string.split(texte,'=',1)
        aval = string.strip(aval)
        if self.pattern_commande.match(aval):
            return 0
        else:
            return 1

    def is_eval(self,texte):
        """
        M�thode bool�enne qui retourne 1 si le texte est celui d'une affectation de type EVAL
        dans un jeu de commandes Aster, 0 sinon
        """
        if '=' not in texte : return 0
        if self.pattern_commande.match(texte):
            # cas d'une proc�dure ...
            return 0
        amont,aval = string.split(texte,'=',1)
        aval = string.strip(aval)
        if not self.pattern_commande.match(aval) : return 0
        if self.pattern_eval.match(aval):
            return 1
        else:
            return 0
            
    def is_commande(self,texte):
        """
        M�thode bool�enne qui retourne 1 si le texte est celui d'une commande dans un jeu de commandes
        Aster, 0 sinon
        """
        if self.pattern_commande.match(texte):
            # cas d'une proc�dure ...
            return 1
        # A ce stade il faut avoir un OPER ou une MACRO, bref un '=' !
        if '=' not in texte : return 0
        # on a un texte de la forme xxxx = yyyyy
        # --> reste � analyser yyyy
        amont,aval = string.split(texte,'=',1)
        aval = string.strip(aval)
        if self.pattern_commande.match(aval):
            return 1
        else:
            return 0

    def analyse(self):
        """
        Transforme dans self.fichier les commentaires Python (#...) par un objet
        commentaire qui pourra donc �tre interpr�t� par EFICAS.
        Stocke le r�sultat dans self.texte
        """
        #l_lignes = open(self.fichier,'r').readlines()
        l_lignes = string.split(self.texte,'\n')
        commentaire_courant             = None
        commande_courante               = None
        affectation_courante            = None
        commande_commentarisee_courante = None
        self.l_objets = []
        cpt = 0
        for ligne in l_lignes :
            cpt = cpt+1
            if string.strip(ligne) == '':
                # il s'agit d'un saut de ligne
                # --> on l'ignore
                continue
            else:
                liste = string.split(ligne,'##',1)
                if len(liste) > 1:
                    # on a trouv� un double commentaire dans la ligne
                    before,after = liste
                    if string.strip(before) == '':
                        # il s'agit d'une commande commentaris�e
                        if commentaire_courant :
                            commentaire_courant = None
                        elif commande_courante :
                            # on a un objet commentaris� � l'int�rieur d'une commande
                            # --> non trait� pour l'instant
                            commande_courante.append_text(ligne)
                        elif commande_commentarisee_courante :
                            # commande_commentarisee en cours : on ajoute la ligne
                            commande_commentarisee_courante.append_text(ligne)
                        else:
                            # on cr�e un objet commande_commentarisee_courante
                            commande_commentarisee_courante = COMMANDE_COMMENTARISEE(self)
                            commande_commentarisee_courante.append_text(ligne)
                        continue
                    else:
                        # on a un double commentaire en fin de ligne
                        # --> pour l'instant on ne fait rien
                        pass
                new_ligne = string.split(ligne,'#')[0] # on enl�ve toute la partie commentaire de la ligne
                new_ligne = string.strip(new_ligne)
                if new_ligne == '' :
                    # la ligne n'est qu'un commentaire pr�c�d� d'�ventuels blancs
                    if commande_courante :
                        # il s'agit d'un commentaire � l'int�rieur d'une commande --> on ne fait rien
                        commande_courante.append_text(ligne)
                    elif commentaire_courant :
                        # il s'agit de la ni�me ligne d'un commentaire entre deux commandes
                        # --> on ajoute cette ligne au commentaire courant
                        commentaire_courant.append_text(ligne)
                    else :
                        # il s'agit d'un commentaire entre deux commandes
                        # --> on le cr�e et il devient le commentaire courant
                        commentaire_courant = COMMENTAIRE(self)
                        commentaire_courant.append_text(ligne)
                else:
                    # la ligne contient des donn�es autre qu'un �ventuel commentaire
                    if commentaire_courant :
                        # on cl�t un �ventuel commentaire courant
                        commentaire_courant = None
                    if commande_courante :
                        commande_courante.append_text(ligne)
                        if commande_courante.get_nb_par() == 0:
                            # la commande courante est termin�e (autant de parenth�ses fermantes qu'ouvrantes)
                            commande_courante = None
                    else:
                        # il peut s'agir d'une commande ou d'une affectation ...
                        # ou de la poursuite d'une affectation !!!!!
                        # ou d'un EVAL !!!
                        if self.is_eval(new_ligne):
                            # --> affectation de type EVAL
                            if affectation_courante : affectation_courante = None
                            affectation = AFFECTATION_EVAL(self)
                            affectation.append_text(ligne)
                        elif self.is_affectation(new_ligne):
                            # --> affectation
                            affectation_courante = AFFECTATION(self)
                            affectation_courante.append_text(ligne)
                        elif self.is_commande(new_ligne):
                            # --> commande
                            commande_courante = COMMANDE(self)
                            commande_courante.append_text(ligne)
                            affectation_courante = None
                            if commande_courante.get_nb_par() == 0:
                                # la commande courante est termin�e (autant de parenth�ses fermantes qu'ouvrantes)
                                commande_courante = None
                        else:
                            #--> poursuite d'une affectation
                            affectation_courante.append_text(ligne)
                                
    def get_texte(self):
        """
        Retourne le texte issu de l'analyse
        """
        if not self.l_objets : self.analyse()
        txt=''
        for obj in self.l_objets:
            txt = txt+str(obj)
        return txt

if __name__ == "__main__" :
    #fichier = 'D:/Eficas_dev/Tests/zzzz100a.comm'
    fichier = 'U:/Eficas_dev/Tests/test_eval.comm'
    texte = open(fichier,'r').read()
    txt = PARSEUR_PYTHON(texte).get_texte()
    print txt
    
