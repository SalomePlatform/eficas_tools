# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
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
from string import split,strip,lowercase,uppercase
import re,string,cPickle,os

from Extensions.i18n import tr
from Noyau.N_CR import CR

#
__Id__="$Id: analyse_catalogue.py,v 1.9.8.1.2.1 2012-05-16 09:43:00 pnoyret Exp $"
__version__="$Name: LOGILAB $"
#
l_noms_commandes = ['OPER','PROC','MACRO','FORM']
l_noms_composes=['FACT','BLOC','NUPL','FORM']
l_noms_simples=['SIMP',]
l_noms=l_noms_composes+l_noms_simples

def elimine_commentaires(text):
        """ Elimine les lignes de commentaires dans text
        Attention : supprime sauvagement tous les caractères entre # et le retour chariot ..."""
        comments = re.compile(r'#[^\n]*')
        return comments.sub(u'',text)

def cherche_nom(text):
        Whitespace = r'[ \f\t]*'
        Name = r'[a-zA-Z_]\w*'
        myexpr = '(u'+Name+')'+Whitespace+'='+Whitespace+'$'
        a=re.search(myexpr,text)
        return a.group(1)

def cherche_args(text):
        text = strip(text)
        longueur = len(text)
        if text[0] != '(u':
                return 'erreur !'
        else :
                nbpar = 1
                for i in range(1,longueur) :
                        if text[i] =='(u':
                                nbpar = nbpar + 1
                        elif text[i] == ')':
                                nbpar = nbpar - 1
                        else :
                                continue
                        if nbpar == 0:
                                break
                if nbpar != 0 :
                        return tr('Erreur ! Erreur !')
                else :
                        try :
                                return text[1:i],text[i+1:] # on enlève les première et dernière parenthèses
                        except :
                                return text[1:i],''

class ENTITE:
        def cherche_enfants(self):
                try :
                        self.text = strip(self.text)
                        liste = re.split(u'=',self.text,1)
                        if len(liste)>1 :
                                arg1=liste[0]
                                reste=liste[1]
                                reste = strip(reste)
                                if reste[0:4] in l_noms :
                                        nom_mc = cherche_nom(arg1+'=')
                                        arg_mc, self.text = cherche_args(reste[4:])
                                        self.cree_mc(nom_mc,arg_mc,reste[0:4])
                                else :
                                        self.text = reste
                                self.cherche_enfants()
                        else :
                                # pas de = rencontré
                                return
                except Exception as e:
                        self.cr.fatal(tr("Erreur rencontrée dans recherche_enfants : %s", e))
                
        def cree_mc(self,nom_mc,arg_mc,test):
                if test in l_noms_composes :
                        mc = FACT_CATA(nom_mc,arg_mc,self)
                        self.children.append(mc)
                elif test in l_noms_simples :
                        mc = SIMP_CATA(nom_mc,self)
                        self.children.append(mc)
                else :
                        print tr("Erreur dans la création du mot-clé : %s", nom_mc)

        def construit_liste_dico(self):
                l=[]
                d={}
                if len(self.children)==0:
                        self.ordre_mc = l
                        self.entites = d
                        return
                try :
                        for child in self.children:
                                l.append(child.nom)
                                d[child.nom]=child
                        self.ordre_mc = l
                        self.entites = d
                except:
                        print tr("erreur : %(v_1)s %(v_2)s", {'v_1': self.nom, 'v_2': self.__class__})
                
class COMMANDE_CATA(ENTITE) :
        def __init__(self,nom,args,parent):
                self.nom = nom
                self.args = args
                self.children = []
                self.text = args
                self.cr = CR()
                self.cr.debut = "Début commande %s" %self.nom
                self.cr.fin = "Fin commande %s" %self.nom
                self.cherche_enfants()
                self.construit_liste_dico()
                parent.cr.add(self.cr)

        def affiche(self):
                texte_cmd = '\n'
                texte_cmd = texte_cmd + 'Commande :' + self.nom + '\n'
                for child in self.children :
                        texte_cmd = texte_cmd + child.affiche(1)
                return texte_cmd

class SIMP_CATA :
        def __init__(self,nom,parent):
                self.nom = nom
                self.cr = CR()
                self.cr.debut = "Début mot-clé simple %s" %self.nom
                self.cr.fin = "Fin mot-clé simple %s" %self.nom
                parent.cr.add(self.cr)

        def affiche(self,ind):
                sep = ' '*5
                return sep*ind+self.nom+'\n'

class FACT_CATA(ENTITE) :
        def __init__(self,nom,args,parent):
                self.nom=nom
                self.args=args
                self.children = []
                self.text=args
                self.cr = CR()
                self.cr.debut = "Début mot-clé facteur ou bloc %s" %self.nom
                self.cr.fin = "Fin mot-clé facteur ou bloc %s" %self.nom
                self.cherche_enfants()
                self.construit_liste_dico()
                parent.cr.add(self.cr)

        def affiche(self,ind):
                sep = ' '*5
                text = ''
                text = text + sep*ind+self.nom+'\n'
                for child in self.children :
                        text = text + child.affiche(ind+1)
                return text
                
class CATALOGUE_CATA:
        def __init__(self,parent,fichier):
                self.parent = parent
                self.fichier=fichier
                self.cr = CR()
                self.cr.debut = "Début compte-rendu catalogue %s" %self.fichier
                self.cr.fin = "Fin compte-rendu catalogue %s" %self.fichier
                self.ouvrir_fichier()
                self.liste_commandes=[]
                self.liste_textes_commandes=[]

        def ouvrir_fichier(self):
                try :
                        f=open(self.fichier,'r')
                        self.texte_complet=f.read()
                        f.close()
                except :
                        print tr("Impossible d'ouvrir le fichier : %s ", self.fichier)
                        self.cr.fatal(tr("Impossible d'ouvrir le fichier : %s ", self.fichier))

        def constr_list_txt_cmd(self,text):
                text = elimine_commentaires(text)
                pattern = '\) *;'
                liste=re.split(pattern,text)
                for i in range(0,len(liste)-1):
                        self.liste_textes_commandes.append(liste[i]+')')

        def analyse_commande_old(self,text):
                #if strip(text) == '' or strip(text) ==')': return
                liste = re.split(u'OPER *\(u',text,1)
                if len(liste) < 2 :
                        liste = re.split(u'PROC *\(u',text,1)
                if len(liste) < 2 :
                        liste = re.split(u'MACRO *\(u',text,1)
                if len(liste) < 2 :
                        print tr("le texte à analyser n'est pas celui d'une commande ou \
                                 d'un opérateur : %s", text)
                        self.cr.fatal(tr("le texte à analyser n'est pas celui d'une commande ou \
                                         d'un opérateur : %s", text))
                        return
                debut = liste[0]
                fin = liste[1]
                nom_cmd = cherche_nom(debut)
                if nom_cmd == 'erreur !':
                        print tr("Erreur dans la recherche \
                                        du nom de la commande : %s", debut)
                args_cmd,toto = cherche_args(u'(u'+fin)
                if args_cmd == 'erreur !':
                        print tr("Erreur dans la recherche des \
                                 args de la commande : %s", debut)
                cmd=COMMANDE_CATA(nom_cmd,args_cmd,self)
                self.liste_commandes.append(cmd)

        def analyse_commande(self,text):
                #if strip(text) == '' or strip(text) ==')': return
                for nom_cmd in l_noms_commandes:
                        liste = re.split(nom_cmd+' *\(u',text,1)
                        if len(liste) == 2 : break
                if len(liste) < 2 :
                        print tr("le texte à analyser n'est pas celui d'une commande connue : \
                                        %(v_1)s %(v_2)s", {'v_1': str(l_noms_commandes), 'v_2': text})
                        self.cr.fatal(tr("le texte à analyser n'est pas celui d'une commande connue : \
                                         %(v_1)s %(v_2)s", {'v_1': str(l_noms_commandes), 'v_2': text}))
                        return
                debut = liste[0]
                fin = liste[1]
                nom_cmd = cherche_nom(debut)
                if nom_cmd == 'erreur !':
                        print tr("Erreur dans la recherche du \
                                 nom de la commande : %s", debut)
                args_cmd,toto = cherche_args(u'(u'+fin)
                if args_cmd == 'erreur !':
                        print tr("Erreur dans la recherche des args \
                                 de la commande : %s", debut)
                        print tr(fin)
                cmd=COMMANDE_CATA(nom_cmd,args_cmd,self)
                self.liste_commandes.append(cmd)
                
        def analyse_texte(self,texte):
                self.constr_list_txt_cmd(texte)
                try:
                        self.parent.configure_barre(len(self.liste_textes_commandes))
                except:
                        pass
                for texte_commande in self.liste_textes_commandes :
                        try:
                                self.parent.update_barre()
                        except:
                                pass
                        self.analyse_commande(texte_commande)
                self.construit_liste_dico()

        def ecrit_lcmd(self):
                f=open(u'U:\\EFICAS\\Accas\\cata.txt','w')
                for cmd in self.liste_commandes :
                        f.write(cmd.affiche())
                f.close()

        def construit_liste_dico(self):
                l=[]
                d={}
                for cmd in self.liste_commandes:
                        l.append(cmd.nom)
                        d[cmd.nom]=cmd
                self.ordre_mc = l
                self.entites = d

        def report(self):
                """ retourne l'objet rapport du catalogue de commande """
                return self.cr

def analyse_catalogue(parent,nom_cata):
        cata = CATALOGUE_CATA(parent,nom_cata)
        cata.analyse_texte(cata.texte_complet)
        return cata

def analyse_catalogue_commande(parent,nom_cata):
        cata = CATALOGUE_CATA(parent,nom_cata)
        cata.analyse_commande(cata.texte_complet)
        cata.construit_liste_dico()
        return cata


def make_cata_pickle(fic_cata):
        """
        Lance l'analyse de l'ordre des mots-clés dans le catalogue dont le nom
        est passé en argument et sauvegarde ces infos dans le fichier pickle relu
        par Eficas
        """
        fic_cata_p = os.path.splitext(fic_cata)[0]+'_pickled.py'
        cata_ordonne = analyse_catalogue(None,fic_cata)
        f = open(fic_cata_p,'w+')
        p = cPickle.Pickler(f)
        p.dump(cata_ordonne.entites)
        f.close()
        
if __name__ == "__main__" :
        import profile
        profile.run(u"analyse_catalogue(None,'U:\\EFICAS\\Cata\\cata_saturne.py')")











                                
                                
