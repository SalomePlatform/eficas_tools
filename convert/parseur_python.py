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
import sys,string,re
import traceback

escapedQuotesRE = re.compile(r"(\\\\|\\\"|\\\')")
stringsAndCommentsRE =  \
      re.compile("(\"\"\".*?\"\"\"|'''.*?'''|\"[^\"]*\"|\'[^\']*\'|#.*?\n)", re.DOTALL)
allchars = string.maketrans("", "")
allcharsExceptNewline = allchars[: allchars.index('\n')]+allchars[allchars.index('\n')+1:]
allcharsExceptNewlineTranstable = string.maketrans(allcharsExceptNewline, '*'*len(allcharsExceptNewline))

def maskStringsAndComments(src):
    """Masque tous les caracteres de src contenus dans des commentaires ou des strings multilignes (triples
       quotes et guillemets.
       Le masquage est realise en remplacant les caracteres par des * 
       Attention : cette fonction doit etre utilisee sur un texte complet et pas ligne par ligne
    """
    src = escapedQuotesRE.sub("**", src)
    allstrings = stringsAndCommentsRE.split(src)
    # every odd element is a string or comment
    for i in xrange(1, len(allstrings), 2):
        if allstrings[i].startswith("'''")or allstrings[i].startswith('"""'):
            allstrings[i] = allstrings[i][:3]+ \
                           allstrings[i][3:-3].translate(allcharsExceptNewlineTranstable)+ \
                           allstrings[i][-3:]
        else:
            allstrings[i] = allstrings[i][0]+ \
                           allstrings[i][1:-1].translate(allcharsExceptNewlineTranstable)+ \
                           allstrings[i][-1]

    return "".join(allstrings)

implicitContinuationChars = (('(', ')'), ('[', ']'), ('{', '}'))
linecontinueRE = re.compile(r"\\\s*(#.*)?$")
emptyHangingBraces = [0,0,0,0,0]

class ParserException(Exception): pass
class FatalError(Exception): pass

#commentaire double precede d'un nombre quelconque de blancs (pas multiligne)
pattern_2comments   = re.compile(r"^\s*##.*")
#commentaire standard precede d'un nombre quelconque de blancs (pas multiligne)
pattern_comment   = re.compile(r"^\s*#.*")
#fin de ligne ; suivi d'un nombre quelconque de blancs (pas multiligne)
pattern_fin   = re.compile(r"; *$")
#pattern pour supprimer les blancs, tabulations et fins de ligne
pattern_blancs = re.compile(r"[\s\n]")
number_kw_pattern=re.compile(r"""
(
    #groupe nombre decimal
    (?:
        #signe : on ignore le signe +
        [-]?
        #groupe (avec ?: n'apparait pas en tant que groupe dans le resultat)
        (?:
            #mantisse forme entiere.fractionnaire
            \d+(?:\.\d*)?
            |
            #ou forme .fractionnaire
            \.\d+
        )
        (?:[eE][+-]?\d+)?
    )
    |
    #argument keyword
    [a-zA-Z_]\w*=
)
""",re.VERBOSE)

def construit_genea(texte,liste_mc):
    """Retourne un dictionnaire dont les cles sont des reels et les valeurs sont leurs representations textuelles.
       Realise un filtrage sur les reels :
         - Ne garde que les reels pour lesquels str ne donne pas une bonne representation.
         - Ne garde que les reels derriere un argument keyword dont le nom est dans liste_mc
    >>> s = 'a=+21.3e-5*85,b=-.1234,c=81.6   , d= -8 , e=_F(x=342.67,y=-1), f=+1.1, g=(1.3,-5,1.54E-3)'
    >>> construit_genea(s,['a','x'])
    {0.000213: '21.3e-5'}
    """
    d={}
    mot=""
    #on masque les strings et commentaires pour ne pas identifier de faux reels
    for m in number_kw_pattern.findall(maskStringsAndComments(texte)):
        if m[-1] == '=':
            #argument keyword
            mot=m[:-1]
        else:
            if mot not in liste_mc:continue
            #valeur
            key=eval(m)
            if str(key) != m: d[key]=m
    return d


class ENTITE_JDC :
    """Classe de base pour tous les objets créés lors de la conversion
       Tout objet dérivé est enregistré auprès de son père à sa création
    """
    def __init__(self,pere):
        self.texte = ''
        pere.l_objets.append(self)

    def set_text(self,texte):
        self.texte = texte

    def append_text(self,texte):
        """
        Ajoute texte à self.texte en mettant un retour chariot à la fin de texte
        """
        texte = texte+'\n'
        self.texte = self.texte +texte

    def __str__(self):
        return self.texte

class COMMENTAIRE(ENTITE_JDC):

    def __str__(self):
        """
        Retourne une chaîne de caractères représentants self
        sous une forme interprétable par EFICAS
        """
        t=repr(self.texte)
        return "COMMENTAIRE("+t+")\n"

        #s='COMMENTAIRE("""'+self.texte+'""")\n\n'
        #return s

    def append_text(self,texte):
        """
        Ajoute texte à self.texte en enlevant le # initial
        """
        texte = texte+'\n'
        if texte[0] == '#':
            self.texte = self.texte+texte[1:]
        else:
            # le dièse n'est pas sur le premier caractère
            amont,aval = string.split(texte,'#',1) # on découpe suivant la première occurrence de #
            self.texte = self.texte +amont + aval
        
class COMMANDE(ENTITE_JDC):

    def __str__(self):
        """
        Retourne self.texte
        """
        return self.texte+'\n'
        
    def get_nb_par(self):
        """
        Retourne la différence entre le nombre de parenthèses ouvrantes
        et le nombre de parenthèses fermantes présentes dans self.texte
        Peut donc retourner un entier négatif
        """
        # faire attention aux commentaires contenus dans self.texte
        # qui peuvent eux-mêmes contenir des parenthèses !!!!
        l_lignes = string.split(self.texte,'\n')
        nb = 0
        for ligne in l_lignes:
            ligne = string.split(ligne,'#')[0]
            nb = nb + (string.count(ligne,'(')-string.count(ligne,')'))
        return nb

class AFFECTATION(ENTITE_JDC):

    def append_text(self,texte):
        """
        Ajoute texte à self.texte en enlevant tout retour chariot et tout point virgule
        PN et tout commentaire
        """
        if texte[-1] == '\n' : texte = string.rstrip(texte[0:-1])
        if texte[-1] == ';' : texte = string.rstrip(texte[0:-1])
        self.texte = self.texte+texte+'\n'
        
    def __str__(self):
        """
        Retourne une expression de l'affectation compréhensible par ACCAS
        et exploitable par EFICAS
        """
        nom,valeur = string.split(self.texte,'=',1)
        n = string.rstrip(nom)
        nom = string.lstrip(n)
        if valeur[-1] == '\n': valeur = valeur[:-1]
        return n + ' = PARAMETRE(nom=\''+nom+'\',valeur='+valeur+')\n'

class COMMANDE_COMMENTARISEE(ENTITE_JDC):

    def append_text(self,texte):
        """
        Ajoute texte à self.texte en enlevant les doubles commentaires
        """
        texte = string.strip(texte)
        texte = string.strip(texte[2:])
        self.texte = self.texte+(len(self.texte)>0)*'\n'+texte

    def __str__(self):
        """
        Retourne une expression de la commande commentarisée compréhensible par ACCAS
        et exploitable par EFICAS
        """
        return "COMMANDE_COMM(texte="+repr(self.texte)+")\n"
        #return "COMMANDE_COMM(texte='''"+self.texte+"''')\n"

class AFFECTATION_EVAL(ENTITE_JDC):

    def append_text(self,texte):
        """
        Ajoute texte à self.texte en enlevant tout retour chariot
        """
        if texte[-1] == '\n' : texte = texte[1:-1]
        self.texte = self.texte+texte
        
    def __str__(self):
        """
        Retourne une expression du paramètre EVAL compréhensible par ACCAS
        et exploitable par EFICAS
        """
        nom,valeur = string.split(self.texte,'=',1)
        nom = string.strip(nom)
        if valeur[-1] == '\n': valeur = valeur[:-1]
        valeur = string.strip(valeur)
        return nom+' = PARAMETRE_EVAL(nom=\''+nom+'\',valeur=\''+valeur+'\')\n\n'
        
class PARSEUR_PYTHON:
    """
    Cette classe sert à générer un objet PARSEUR_PYTHON qui réalise l'analyse d'un texte 
    représentant un JDC Python en distinguant :
      - les commentaires inter commandes
      - les affectations
      - les commandes
    """
    pattern_commande   = re.compile(r'^([A-Z][A-Z0-9_]+)([ \t\r\f\v]*)\(([\w\W]*)')
    pattern_eval       = re.compile(r'^(EVAL)([ \t\r\f\v]*)\(([\w\W]*)')
    pattern_ligne_vide = re.compile(r'^[\t\r\f\v\n]+')
    pattern_name       = re.compile(r'[a-zA-Z_]\w*')
    
    def __init__(self,texte):
        self.texte = texte
        self.l_objets=None
        self.appli=None

    def is_affectation(self,texte):
        """
        Méthode booléenne qui retourne 1 si le texte est celui d'une affectation dans un jeu de commandes
        Aster, 0 sinon
        """
        if '=' not in texte : return 0
        if self.pattern_commande.match(texte):
            # cas d'une procédure ...
            return 0
        amont,aval = string.split(texte,'=',1)
        aval = string.strip(aval)
        if self.pattern_commande.match(aval):
            return 0
        else:
            s= string.strip(amont)
            m= self.pattern_name.match(s)
            if m is None : return 0
            if m.start() != 0 :return 0
            if m.end() != len(s):return 0
            #print texte,amont,aval
            return 1

    def is_eval(self,texte):
        """
        Méthode booléenne qui retourne 1 si le texte est celui d'une affectation de type EVAL
        dans un jeu de commandes Aster, 0 sinon
        """
        if '=' not in texte : return 0
        if self.pattern_commande.match(texte):
            # cas d'une procédure ...
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
        Méthode booléenne qui retourne 1 si le texte est celui d'une commande dans un jeu de commandes
        Aster, 0 sinon
        """
        if self.pattern_commande.match(texte):
            # cas d'une procédure ...
            return 1
        # A ce stade il faut avoir un OPER ou une MACRO, bref un '=' !
        if '=' not in texte : return 0
        # on a un texte de la forme xxxx = yyyyy
        # --> reste à analyser yyyy
        amont,aval = string.split(texte,'=',1)
        aval = string.strip(aval)
        if self.pattern_commande.match(aval):
            return 1
        else:
            return 0

    def analyse(self):
        """
        Eclate la chaine self.texte en self.l_objets une liste lignes d'instructions
        et de commentaires (parmi lesquels des instructions "commentarisées").
        """
        l_lignes = string.split(self.texte,'\n')
        commentaire_courant             = None
        commande_courante               = None
        affectation_courante            = None
        commande_commentarisee_courante = None
        self.l_objets = []

        #initialisation du nombre de parentheses non fermees et de commentaires non termines
        #Attention a reinitialiser en fin de ligne logique
        #Une ligne logique peut s'etendre sur plusieurs lignes physiques avec des caracteres de continuation
        #explicites ou implicites
        hangingBraces = list(emptyHangingBraces)
        hangingComments = 0

        #Masquage des commentaires et strings multilignes
        srcMasked=maskStringsAndComments('\n'.join(l_lignes))
        #print srcMasked
        masked_lines=srcMasked.split('\n')
        lineno=0

        for ligne in l_lignes :
            line=masked_lines[lineno]
            lineno=lineno+1
            #print "ligne:",line
            # mise a jour du nombre total de parentheses ouvertes (non fermees)
            # et du nombre de commentaires non termines
            for i in range(len(implicitContinuationChars)):
                contchar = implicitContinuationChars[i]
                numHanging = hangingBraces[i]
                hangingBraces[i] = numHanging+line.count(contchar[0]) - line.count(contchar[1])

            hangingComments ^= line.count('"""') % 2
            hangingComments ^= line.count("'''") % 2
            #print hangingComments,hangingBraces
            if hangingBraces[0] < 0 or hangingBraces[1] < 0 or hangingBraces[2] < 0: 
                raise ParserException()

            if string.strip(ligne) == '':
                # il s'agit d'un saut de ligne
                # --> on l'ignore
                continue

            if pattern_2comments.match(ligne):
                #on a trouvé une commande commentarisée : double commentaire sans rien devant à part des blancs
                if commentaire_courant:
                    #Si un commentaire ordinaire est en cours on le termine
                    commentaire_courant = None

                if commande_courante :
                    # on a un objet commentarisé à l'intérieur d'une commande
                    # --> non traité pour l'instant : on l'ajoute simplement a la commande courante comme
                    # un commentaire ordinaire
                    commande_courante.append_text(ligne)
                elif commande_commentarisee_courante :
                    # commande_commentarisee en cours : on ajoute la ligne
                    commande_commentarisee_courante.append_text(ligne)
                else:
                    # debut de commande commentarisée : on crée un objet commande_commentarisee_courante
                    commande_commentarisee_courante = COMMANDE_COMMENTARISEE(self)
                    commande_commentarisee_courante.append_text(ligne)

                #on passe à la ligne suivante
                continue

            if pattern_comment.match(ligne):
                #commentaire ordinaire avec seulement des blancs devant
                if commande_commentarisee_courante :
                    # commande_commentarisee en cours : on la clot
                    commande_commentarisee_courante = None

                if commande_courante :
                    # il s'agit d'un commentaire à l'intérieur d'une commande --> on ne fait rien de special
                    #on l'ajoute au texte de la commande 
                    commande_courante.append_text(ligne)
                elif commentaire_courant :
                    # il s'agit de la nième ligne d'un commentaire entre deux commandes
                    # --> on ajoute cette ligne au commentaire courant
                    commentaire_courant.append_text(ligne)
                else :
                    # il s'agit d'un nouveau commentaire entre deux commandes
                    # --> on le crée et il devient le commentaire courant
                    commentaire_courant = COMMENTAIRE(self)
                    commentaire_courant.append_text(ligne)

                #on passe à la ligne suivante
                continue

            # la ligne contient des données autre qu'un éventuel commentaire
            if commentaire_courant :
                # on clôt un éventuel commentaire courant
                commentaire_courant = None

            if commande_commentarisee_courante :
                # on clôt une éventuelle commande commentarisee courante
                commande_commentarisee_courante = None

            if commande_courante :
                #on a une commande en cours. On l'enrichit ou on la termine
                commande_courante.append_text(ligne)
                if not linecontinueRE.search(line) and (hangingBraces == emptyHangingBraces) and not hangingComments:
                    #la commande est terminée 
                    #print "fin de commande"
                    self.analyse_reel(commande_courante.texte)
                    commande_courante = None

                #on passe à la ligne suivante
                continue

            if affectation_courante != None :
                #poursuite d'une affectation
                affectation_courante.append_text(ligne)
                if not linecontinueRE.search(line) and (hangingBraces == emptyHangingBraces) and not hangingComments:
                    #L'affectation est terminée
                    affectation_courante=None
                #on passe à la ligne suivante
                continue

            # il peut s'agir d'une commande ou d'une affectation ...
            # ou d'un EVAL !!!
            if self.is_eval(ligne):
                # --> affectation de type EVAL
                if affectation_courante : affectation_courante = None
                affectation = AFFECTATION_EVAL(self)
                affectation.append_text(ligne)
                #on passe à la ligne suivante
                continue

            if self.is_affectation(ligne):
                # --> affectation
                text=ligne
                #traitement des commentaires en fin de ligne
                compos=line.find("#")
                if compos > 2:
                    #commentaire en fin de ligne
                    #on cree un nouveau commentaire avant le parametre
                    COMMENTAIRE(self).append_text(ligne[compos:])
                    text=ligne[:compos]
                #si plusieurs instructions separees par des ; sur la meme ligne
                inspos=line.find(";")
                if inspos > 2:
                    #on garde seulement la premiere partie de la ligne
                    #si on a que des blancs apres le point virgule
                    if string.strip(text[inspos:]) == ";":
                        text=text[:inspos]
                    else:
                        raise FatalError("Eficas ne peut pas traiter plusieurs instructions sur la meme ligne : %s" % ligne)

                affectation_courante = AFFECTATION(self)
                affectation_courante.append_text(text)
                if not linecontinueRE.search(line) and (hangingBraces == emptyHangingBraces) and not hangingComments:
                    #L'affectation est terminée
                    affectation_courante=None
                #on passe à la ligne suivante
                continue

            if self.is_commande(ligne):
                # --> nouvelle commande
                affectation_courante = None
                commande_courante = COMMANDE(self)
                commande_courante.append_text(ligne)
                #si la commande est complète, on la termine
                if not linecontinueRE.search(line) and (hangingBraces == emptyHangingBraces) and not hangingComments:
                    #la commande est terminée 
                    #print "fin de commande"
                    self.analyse_reel(commande_courante.texte)
                    commande_courante = None
                #on passe à la ligne suivante
                continue

    def enleve (self,texte) :
        """Supprime de texte tous les caracteres blancs, fins de ligne, tabulations
           Le nouveau texte est retourné
        """
        i=0
        chaine=""
        while (i<len(texte)):
          if (texte[i] == " " or texte[i] == "\n" or texte[i] == "\t") :
             i=i+1
          else :
             chaine=chaine+texte[i]
             i=i+1
        return chaine 
            
    def construit_genea(self,texte):
        indiceC=0
        mot=""
        dict_reel_concept={}

        # traitement pour chaque caractere
        while (indiceC < len(texte)): 
           c=texte[indiceC]
           if ( c == "," or c == "(" or c == ")"):
              mot=""
           elif ( c== "="):
              #on doit trouver derriere soit une valeur soit une parenthese
              valeur=""
              nouvelindice=indiceC+1
              if texte[nouvelindice] != "(":
                 #pas de parenthese ouvrante derriere un signe =, on a une valeur.
                 while ( texte[nouvelindice] != "," and texte[nouvelindice] != ")"):
                    valeur=valeur+texte[nouvelindice]
                    nouvelindice=nouvelindice+1
                    if nouvelindice == len(texte) :
                        nouvelindice=nouvelindice -1
                        break
                 if mot in self.appli.liste_simp_reel:
                    if valeur[0] != "'":
                       try :
                         clef=eval(valeur)
                         if str(clef) != str(valeur) :
                            dict_reel_concept[clef]=valeur
                       except :
                         pass
                 mot=""
                 indiceC=nouvelindice
              else:
                 #parenthese ouvrante derriere un signe =, on a un tuple de valeur ou de mots cles facteurs.
                 # s agit -il d un tuple 
                 if texte[nouvelindice+1] != "(":
                    #le suivant n'est pas une parenthese ouvrante : on a un tuple de valeurs ou un mot cle facteur
                    tuple=False
                    #on avance jusqu'a la fin du tuple de valeurs ou jusqu'a la fin du premier mot cle simple
                    #contenu dans le mot cle facteur
                    while ( texte[nouvelindice] != "="):
                       if texte[nouvelindice] == ")" :
                          tuple=True
                          break
                       else :
                          nouvelindice=nouvelindice+1
                          if nouvelindice == len(texte) :
                             nouvelindice=nouvelindice -1
                             break
                    if tuple :
                       #cas du tuple de valeurs
                       valeur=texte[indiceC+1:nouvelindice+1]
                       indiceC=nouvelindice+1 
                       if mot in self.appli.liste_simp_reel:
                          valeur=valeur[1:-1]
                          for val in valeur.split(',') :
                          # Attention la derniere valeur est""
                             try :
                                if val[0] != "'":
                                  clef=eval(val)
                                  if str(clef) != str(val) :
                                     dict_reel_concept[clef]=val
                             except :
                                  pass
                       mot=""
               # ou de ( imbriqueés
                 else :
                    #cas du mocle facteur simple ou 
                    mot=""
           else :
              mot=mot+texte[indiceC]
           indiceC=indiceC+1
        # traitement du dernier inutile
        # c est un ; 
        return dict_reel_concept

    def analyse_reel(self,commande) :
        nomConcept=None
        # On verifie qu on a bien un OPER
        # et pas une MACRO
        if commande.find("=") > commande.find("(") :
           return
        if commande.find("=") > 0:
           #epure1=self.enleve(commande)
           epure1=pattern_blancs.sub("",commande)
           nomConcept,corps=epure1.split("=",1)
           epure2=corps.replace("_F(","(")
           #nomConcept=epure1.split("=")[0]
           #index=epure1.find("=")
           #epure2=epure1[index+1:len(epure1)].replace("_F(","(")
           #dict_reel_concept=self.construit_genea(epure2)
           dict_reel_concept=construit_genea(epure2,self.appli.liste_simp_reel)
        if nomConcept !=None :
           if len(dict_reel_concept) != 0:
              self.appli.dict_reels[nomConcept]=dict_reel_concept

    def get_texte(self,appli=None):
        """
        Retourne le texte issu de l'analyse
        """
        self.appli=appli
        try:
            if not self.l_objets : self.analyse()
            txt=''
            for obj in self.l_objets:
                txt = txt+str(obj)
        except ParserException:
            #Impossible de convertir le texte, on le retourne tel que
            txt=self.texte
        return txt

if __name__ == "__main__" :
    import time
    #fichier = 'D:/Eficas_dev/Tests/zzzz100a.comm'
    fichier = 'U:/Eficas_dev/Tests/test_eval.comm'
    fichier = '/local/chris/ASTER/Eficas/Eficas1_10/EficasV1/Tests/testcomm/b.comm'
    fichier = '/local/chris/ASTER/instals/STA8.2/astest/forma12c.comm'
    fichier = 'titi.comm'
    fichier = '../Aster/sdls300a.comm'
    texte = open(fichier,'r').read()
    class appli:
       dict_reels={}
       liste_simp_reel=["VALE","VALE_C","GROUP_MA","RAYON"]
    a=appli()

    if 1:
        t0=time.clock()
        txt = PARSEUR_PYTHON(texte).get_texte(a)
        print t0,time.clock()-t0
    else:
        import hotshot, hotshot.stats
        prof = hotshot.Profile("stones.prof")
        txt = prof.runcall(PARSEUR_PYTHON(texte).get_texte,a)
        prof.close()
        stats = hotshot.stats.load("stones.prof")
        stats.strip_dirs()
        stats.sort_stats('time', 'calls')
        stats.print_stats(20)

    print txt
    compile(txt, '<string>', 'exec')
    print a.dict_reels
