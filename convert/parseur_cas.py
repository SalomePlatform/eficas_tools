# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
import sys,string,re
import traceback
from Extensions.i18n import tr
import Accas

# mot cles a traiter : Discretisations_In_Space
from enumTelemac import dicoEnum

escapedQuotesRE = re.compile(r"(\\\\|\\\"|\\\')")
stringsAndCommentsRE =  \
      re.compile(u"(\"\"\".*?\"\"\"|'''.*?'''|\"[^\"]*\"|\'[^\']*\'|#.*?\n)", re.DOTALL)
allchars = string.maketrans(u"", "")
allcharsExceptNewline = allchars[: allchars.index('\n')]+allchars[allchars.index('\n')+1:]
allcharsExceptNewlineTranstable = string.maketrans(allcharsExceptNewline, '*'*len(allcharsExceptNewline))

ordreEtapes=('INITIALIZATION', 'TIDE_PARAMETERS', 'INITIAL_STATE', 'NUMERICAL_PARAMETERS', 'PHYSICAL_PARAMETERS',) 

def maskStringsAndComments(src):
    """Masque tous les caracteres de src contenus dans des commentaires ou des strings multilignes (triples
       quotes et guillemets.
       Le masquage est realise en remplacant les caracteres par des * 
       Attention : cette fonction doit etre utilisee sur un texte complet et pas ligne par ligne
    """
    src = escapedQuotesRE.sub(u"**", src)
    allstrings = stringsAndCommentsRE.split(src)
    # every odd element is a string or comment
    for i in xrange(1, len(allstrings), 2):
        if allstrings[i].startswith(u"'''")or allstrings[i].startswith('"""'):
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

# ligne commençant par /
pattern_commentaireTelemac   = re.compile(r"^\s*/.*")
# ligne commençant par &
pattern_eperluetteTelemac   = re.compile(r"^&.*")
#commentaire double precede d'un nombre quelconque de blancs (pas multiligne)
pattern_2comments   = re.compile(r"^\s*##.*")
#commentaire standard precede d'un nombre quelconque de blancs (pas multiligne)
pattern_comment   = re.compile(r"^\s*#.*")
#fin de ligne ; suivi d'un nombre quelconque de blancs (pas multiligne)
pattern_fin   = re.compile(r"; *$")
#pattern pour supprimer les blancs, tabulations et fins de ligne
pattern_blancs = re.compile(r"[ \t\r\f\v]")
#pattern_blancs = re.compile(r"[\s\n]")
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
""",re.VERBOSE|re.MULTILINE)

def construit_genea(texte,liste_mc):
    """
       Retourne un dictionnaire dont les cles sont des reels et les valeurs sont leurs representations textuelles.

       Realise un filtrage sur les reels :

         - Ne garde que les reels pour lesquels str ne donne pas une bonne representation.
         - Ne garde que les reels derriere un argument keyword dont le nom est dans liste_mc

       >>> s = '''a=+21.3e-5*85,b=-.1234,c=81.6   , d= -8 , e=_F(x=342.67,y=-1), f=+1.1, g=(1.3,-5,1.54E-3),
       ... #POMPE_PRIMA._BOUCLE_N._2_ELEMENT_NUMERO:0239
       ... h=_F(x=34.6,y=-1)'''
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


ListeMCAExclure=("Computation_Continued",)
DicoMCAExclureSiValeur={"Computation_Continued" : "NO"}
ListeMCARecalculer=('tt',)
DicoMCARecalculerSiValeur={"Computation_Continued" : "YES"}
DicoMCAReformater = {"Variables_For_Graphic_Printouts": "texteEnListe", \
                     "Solver" : "remplaceEnum" }
DicoPlusieursMC =  {"Type_Of_Advection": "decoupeAdvection" ,\
                    }

class PARSEUR_CAS:
  

    pattern_ligne_vide = re.compile(r'^[\t\r\f\v\n]+')
    
    def __init__(self,texte):
        self.texte = texte
        self.l_objets=None
        self.appli=None

    def get_texte(self,appli=None):
        """
        Retourne le texte issu de l'analyse
        """
        self.appli=appli
        self.dicoInverse=self.appli.readercata.dicoInverse

        try:
            self.analyse()
            txt=self.texteComm
        except  ParserException:
            #Impossible de convertir le texte, on le retourne tel que
            txt=self.texte
        return txt

    def analyse(self):
        """
        Eclate la chaine self.texte en self.l_objets une liste lignes d'instructions
        et de commentaires (parmi lesquels des instructions "commentarisées").
        """
        l_lignes = string.split(self.texte,'\n')
        affectation_courante            = None
        self.l_objets = []

        #Masquage des commentaires et strings multilignes
        #srcMasked=maskStringsAndComments('\n'.join(l_lignes))
        #print srcMasked
        #masked_lines=srcMasked.split('\n')

        lineno=0
        self.listeNomValeur=[]
        for ligne in l_lignes :
            #line=masked_lines[lineno]
            lineno=lineno+1

            if string.strip(ligne) == '': continue
            if pattern_commentaireTelemac.match(ligne) : continue
            if pattern_eperluetteTelemac.match(ligne)  : continue
            # On remplace les : par un =
            # On s assure que les = soient entoures d espace
            # On remplace les espaces successifs par un seul
            # On enleve les blancs en debut et fin de ligne
            # On remplace les ' ; ' par des ;
            ligne=ligne.replace(':','=')
            ligne=ligne.replace('=',' = ')
            ligne=re.sub(r';\s*',';',ligne)
            ligne=re.sub(r'\s*;',';',ligne)
            ligne=re.sub(r' \s*',' ',ligne)
            ligne=re.sub(r'^\s','',ligne)
            ligne=re.sub(r'\s$','',ligne)
            listeMot=ligne.split(" ")
            while listeMot != [] :
               nom,listeMot    = self.construitNom(listeMot)
               valeur,listeMot = self.construitValeur(listeMot)
               bTraite, nom, valeur =self.verifieNom(nom,valeur)
               if bTraite : self.listeNomValeur.append((nom, valeur))
        self.construitTexteFinal()
               
               
    def construitNom(self,liste):
        nomEficas=''
        index=0
        for mot in liste :
           index+=1
           if mot in (":","=") : break
           motE=mot[0].upper()+mot[1:].lower()
           nomEficas+=motE+'_'
        nouveauNom=nomEficas[0:-1].replace('-','_')
        nouvelleListe=liste[index:]
        return nouveauNom,nouvelleListe

    def construitValeur(self,liste):
        index=0
        if liste[0][0]=="'" :
           valeur=''
           for mot in liste :
               index+=1
               valeur+=str(mot)+" "
               if mot[-1]=="'":
                  valeur=valeur[0:-1]
                  break
        elif liste[0].find(';') > -1 :
          valeur=liste[0].split(';')
          index=1
        else : 
          valeur=liste[0]
          index=1
        nouvelleListe=liste[index:]
        return valeur,nouvelleListe
               

    def verifieNom(self,nom,valeur):
        if nom in ListeMCAExclure : return (False, nom, valeur) 
        if nom in DicoMCAExclureSiValeur.keys() :
          if valeur != DicoMCAExclureSiValeur[nom] :  print "prevoir Traitement pour ", nom, valeur
          return (False, nom, valeur)

        bTrue=True
        if nom in DicoMCAReformater.keys() :
           bTrue,nom,valeur=apply(PARSEUR_CAS.__dict__[DicoMCAReformater[nom]],(self,nom,valeur))
        if nom in DicoPlusieursMC.keys() :
           bTrue,nom,valeur=apply(PARSEUR_CAS.__dict__[DicoPlusieursMC[nom]],(self,nom,valeur))
           return (bTrue,nom,valeur)
        if nom not in self.dicoInverse.keys() : 
           print  "******** ", nom, " non encore connu ***********"
           bTrue=False
        return (bTrue, nom, valeur)

    def remplaceEnum(self,nom,valeur):
       newValeur=dicoEnum[nom][valeur]
       return (True,nom,newValeur)
       


    def texteEnListe(self,nom,valeur): 
       print "je passe dans decoupeEnListe pour ", nom,valeur
       v1=re.sub(r'^\'','',valeur)
       v2=re.sub(r'\'$','',v1)
       newValeur=v2.split(',')
       return (True,nom,newValeur)

    def decoupeAdvection(self,nom,valeur):
        # on met a jour la liste des valeurs ici : il y a plusieurs MC calcule
        print "je passe dans decoupeAdvection pour",nom,valeur
        self.listeNomValeur.append(('Advection_Of_U_And_V',True)) 
        v=dicoEnum['Type_Of_Advection'][valeur[0]]
        self.listeNomValeur.append(('Type_Of_Advection_U_And_V',v) )
        if len(valeur)==1: return  (False,nom,valeur)

        self.listeNomValeur.append(('Advection_Of_H',True)) 
        v=dicoEnum['Type_Of_Advection'][valeur[1]]
        self.listeNomValeur.append(('Type_Of_Advection_H',v)) 
        if len(valeur)==2: return (False,nom,valeur)

        self.listeNomValeur.append(('Advection_Of_Tracers',True)) 
        v=dicoEnum['Type_Of_Advection'][valeur[2]]
        self.listeNomValeur.append(('Type_Of_Advection_Tracers',v)) 
        if len(valeur)==3: return (False,nom,valeur)

        self.listeNomValeur.append(('Advection_Of_K_And_Epsilon',True)) 
        v=dicoEnum['Type_Of_Advection'][valeur[3]]
        self.listeNomValeur.append(('Type_Of_Advection_K_And_Epsilon',v)) 
        # on retourne False, l append est deja fait
        return (False,nom,valeur)

    def construitTexteFinal(self):
        self.dicoTexte={}
        self.dicoNature={}
        print self.listeNomValeur
        for nomMC,valeur in self.listeNomValeur:
            mc,objmc=self.dicoInverse[nomMC][0]
            if nomMC=="Solver_Option" : print self.dicoInverse[nomMC][0]
            self.dicoNature[mc]=objmc
            liste=self.dicoInverse[nomMC][1:]
            liste.reverse()
            dico=self.dicoTexte
            for (nom,obj) in liste:
               if isinstance(obj,Accas.A_BLOC.BLOC) :
                  continue
               self.dicoNature[nom]=obj
               if not(isinstance(obj,Accas.A_PROC.PROC)) and  not(isinstance(obj,Accas.A_FACT.FACT)) :
                  print "******** ", nom,obj, "********"
                  continue
               if not nom in dico.keys(): dico[nom]={}
               dico=dico[nom]
            dico[nomMC]=valeur
        self.texteComm=""
        for etape in ordreEtapes :
            print etape
            if etape in self.dicoTexte.keys():
               self.texteComm+=etape+"("
               self.traiteEtape(self.dicoTexte[etape])
               self.texteComm+=");\n"
        print self.texteComm

    def traiteEtape(self,dico):
        for mc in dico.keys() :
            valeur=dico[mc]
            if isinstance(self.dicoNature[mc],Accas.A_SIMP.SIMP):
               if 'TXM' in  self.dicoNature[mc].type and valeur[0] !="'" : valeur="'"+valeur
               if 'TXM' in  self.dicoNature[mc].type and valeur[-1] !="'" : valeur=valeur+"'"
               if 'Fichier' in  self.dicoNature[mc].type and valeur[0] !="'" : valeur="'"+valeur
               if 'Fichier' in  self.dicoNature[mc].type and valeur[-1] !="'" : valeur=valeur+"'"
               if 'Repertoire' in  self.dicoNature[mc].type and valeur[0] !="'" : valeur="'"+valeur
               if 'Repertoire' in  self.dicoNature[mc].type and valeur[-1] !="'" : valeur=valeur+"'"
               print self.dicoNature[mc].type
               #self.texteComm+=mc+" = '"+str(valeur)+"',"
               #else : self.texteComm+=mc+" = "+str(valeur)+","
               self.texteComm+=mc+" = "+str(valeur)+","
               continue
            self.texteComm+=mc+"=_F("
            self.traiteEtape(valeur)
            self.texteComm+="),\n"
