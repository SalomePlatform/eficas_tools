# -*- coding: iso-8859-15 -*-
"""
Ce module centralise les informations issues de la ligne de commande.

La ligne de commande est parsee avec l'aide du module python optparse.
Les options possibles sont : -c, -j, -p, -d, -i, -f comme definies ci-dessous.

Un exemple typique d'utilisation est :
>>> ./appli.py -c V7.3 -d 1 -j aa -i 11 iii -p ppp -i 22 ii -j bb -f ff

qui demande a l'application d'ouvrir trois jeux de commandes.

Le premier (aa) a un include (11,iii) et est la suite du fichier poursuite ppp 
qui a lui meme un include (22,ii).

Le deuxieme bb est un jeu de commandes simple.

Le troisieme est decrit dans le fichier ff de type .ini
qui est parse par le module ConfigParser.
Chaque section du fichier decrit un jeu de commandes.
Un include est specifie par: numero logique=nom du fichier
Une poursuite est specifiee par: poursuite=reference a un jeu de commande 
Cette reference correspond a un nom de section decrivant le jeu de commandes.
Le jeu de commandes maitre est donne par l'entree globale jdc dans la section jdc.

Exemple:
[jdc]
jdc=a
[a]
comm=aa
poursuite=pours
11=iii
[pours]
comm=ppp
22=ii

La session utilisera le catalogue V7.3 en mode debug.
"""

try:
   import optparse
   from optparse import OptionValueError
except:
   from Tools import optparse
   from Tools.optparse import OptionValueError

import os,traceback
import ConfigParser
import re

# Les valeurs decodees par optparse sont mises dans un objet dictionnaire-like.
# On l'utilise comme environnement de session.
d_env={}
#
# L'attribut "studies" de d_env est une liste dans laquelle on range les etudes de niveau global.
# Une etude est stockee dans un dictionnaire.
# La cle "comm" du dictionnaire donne le nom du fichier de commandes principal
# La cle (optionnelle) "pours" du dictionnaire donne les informations pour une poursuite
# La valeur associee a la cle est un dictionnaire qui contient les informations sur
# le nom du fichier de commandes de la poursuite (cle "comm"), une eventuelle poursuite
# (cle "pours") et les includes (cles entieres associees a des noms de fichier).
#
#
#
# Les informations (dictionnaire) associees au fichier de commandes en cours de traitement 
# sont stockees dans parser.values.current
# En general, il faut utiliser current et pas parser.values.studies car les informations
# sont stockees hierarchiquement
#

def check_comm(option, opt_str, value, parser):
    if not hasattr(parser.values,"studies"):
       parser.values.studies=[]
       parser.values.comm=[]
    if not os.path.isfile(value):
       raise OptionValueError("le fichier de commandes %s n'existe pas" % value)
    parser.values.comm.append(value)
    d_study={"comm":value}
    parser.values.current=d_study
    parser.values.studies.append(d_study)

def check_poursuite(option, opt_str, value, parser):
    if parser.values.comm is None:
       raise OptionValueError("un fichier de commandes doit etre defini avant une poursuite %s" % value)
    if not os.path.isfile(value):
       raise OptionValueError("le fichier poursuite %s n'existe pas" % value)
    #current : fichier de commandes en cours de traitement (dictionnaire des infos)
    comm=parser.values.current
    d_study={"comm":value}
    comm["pours"]=d_study
    parser.values.current=d_study

def check_include(option, opt_str, value, parser):
    try:
       args=[int(parser.rargs[0]),parser.rargs[1]]
    except:
       raise OptionValueError("include mal defini %s" % parser.rargs[0:2])

    del parser.rargs[0]
    del parser.rargs[0]

    if parser.values.comm is None:
       raise OptionValueError("un fichier de commandes doit etre defini avant un include %s" % args)
    if not os.path.isfile(args[1]):
       raise OptionValueError("le fichier include %s n'existe pas" % args[1])

    comm=parser.values.current
    comm[args[0]]=args[1]


def check_jdc(config,jdc,parser,fich):
    """
        Fonction : analyse une section de fichier .ini pour en extraire
        les informations sur les fichiers poursuite et includes
        définis dans cette section

        parser : objet analyseur de la ligne de commande
        fich : nom du fichier .ini en cours d'analyse
        config : objet de la classe ConfigParser permettant de parser le fichier fich
        jdc : nom de la section du fichier fich à analyser
    """
    d_study={}

    for o in config.options(jdc):
       if o == "poursuite":
          p=config.get(jdc,"poursuite")

          if not config.has_option(p,"comm"):
             raise OptionValueError("jdc %s manque fichier comm dans section %s" % (fich,p))
          comm=config.get(p,"comm")
          if not os.path.isfile(comm):
             raise OptionValueError("jdc %s, le fichier de commandes %s n'existe pas" % (fich,comm))

          pours=check_jdc(config,p,parser,fich)
          pours["comm"]=comm
          d_study["pours"]=pours
          continue

       try:
          unit=int(o)
          # si le parametre est un entier, il s'agit d'un include
          inc=config.get(jdc,o)
       except:
          continue
       if not os.path.isfile(inc):
          raise OptionValueError("jdc %s fichier include %s, %s n'existe pas" % (fich,unit,inc))
       d_study[unit]=inc

    return d_study

def check_fich(option, opt_str, fich, parser):
    """
        Fonction : parse le fichier fich (format .ini)
        
        option : option en cours de traitement
        opt_str : chaine de caracteres utilisee par l'utilisateur
        fich : nom du fichier .ini donné par l'utilisateur
        parser : objet parseur des options de la ligne de commande
    """
    if not os.path.isfile(fich):
       raise OptionValueError("le fichier jdc %s n'existe pas" % fich)
    if parser.values.fich is None:
       parser.values.fich=[]
    parser.values.fich.append(fich)
    if not hasattr(parser.values,"studies"):
       parser.values.studies=[]
       parser.values.comm=[]
    config = ConfigParser.ConfigParser()
    config.read([fich])
    if not config.has_option("jdc","jdc"):
       raise OptionValueError("jdc %s manque option jdc dans section jdc")
    jdc=config.get("jdc","jdc")

    if not config.has_option(jdc,"comm"):
       raise OptionValueError("jdc %s manque fichier comm dans section %s" % (fich,jdc))
    comm=config.get(jdc,"comm")
    if not os.path.isfile(comm):
       raise OptionValueError("jdc %s, le fichier de commandes %s n'existe pas" % (fich,comm))
    parser.values.comm.append(comm)

    d_study=check_jdc(config,jdc,parser,fich)
    d_study["comm"]=comm
    parser.values.studies.append(d_study)

def print_pours(d_pours,dec=''):
    # Les fichiers includes d'abord
    for k,v in d_pours.items():
       if k in ("pours","comm"):continue
       print dec+" include",k," :",v

    if d_pours.has_key("pours"):
       # Description de la poursuite
       print dec+" fichier poursuite:",d_pours["pours"]["comm"]
       print_pours(d_pours["pours"],dec=dec+"++")

def print_d_env():
    #print d_env
    if d_env.studies is None:return
    for study in d_env.studies:
       print "nom etude:",study["comm"]
       print_pours(study,dec="++")
       print

def create_parser():
    # creation du parser des options de la ligne de commande
    #import prefs
    parser=optparse.OptionParser(usage="usage: %prog [options]",version="%prog 1.13")

    parser.add_option("-j","--jdc",dest="comm",type='string',
                    action="callback",callback=check_comm,
                    help="nom du fichier de commandes")

    parser.add_option("-p","--poursuite", type="string",dest="pours",
                  action="callback", callback=check_poursuite,
                  help="nom du fichier poursuite")

    parser.add_option("-i","--include", 
                  action="callback", callback=check_include,
                  nargs=2, help="numero d'unite suivi du nom du fichier include")

    parser.add_option("-f","--fich", type="string",dest="fich",
                  action="callback", callback=check_fich,
                  help="fichier decrivant une etude")

    parser.add_option("-c","--cata", action="store", type="string",dest="cata",
                  help="version de catalogue a utiliser")

    parser.add_option("-k","--kode", action="store", type="string",dest="code",
                  help="nom du code a utiliser")

    parser.add_option("-d","--debug", action="store", type="int",dest="debug",
                  help="niveau de debug")

    parser.add_option("-s","--schema", action="store", type="string",dest="ssCode",
                  help="schema")


    return parser

def parse(args):
    parser=create_parser()
    (options,args)=parser.parse_args(args[1:])
    if not hasattr(options,"studies"):
       options.studies=[]
       options.comm=[]
    try:
       del parser.values.current
    except:
       pass

    for file in args:
         if os.path.isfile(file):
            options.comm.append(file)
            options.studies.append({"comm":file})
         elif len(args)==1 and re.search('.comm',file):
            try :
                f=open(file,'w')
                f.close()
            except :
                parser.error("incorrect number of arguments")
            options.comm.append(file)
            options.studies.append({"comm":file})
         else:
            parser.error("incorrect number of arguments")

    global d_env
    d_env=options
    #print_d_env()
    return options

def get_unit(d_study,appli):
    """
       Fonction : construit et retourne un dictionnaire contenant les informations
       sur les fichiers poursuite et includes sous la forme adaptée
       pour EFICAS ::

                  [None : nom_fichier, texte_source, unites_associees,           # poursuite
                   numero_include : nom_fichier, texte_source, unites_associees, # include
                    ...] 

       d_study : dictionnaire de l'etude
       appli : objet application EFICAS (permet d'acceder aux services comme get_source)
    """
    return get_dunit(d_study,appli)

def get_dunit(d_unit,appli):
    d={}
    if d_unit.has_key("pours"):
       # on a une poursuite
       comm=d_unit["pours"]["comm"]
       g=get_dunit(d_unit["pours"],appli)
       text=appli.get_source(comm)
       d[None]=comm,text,g

    for k,v in d_unit.items():
       if k in ("pours","comm"): continue
       text=appli.get_source(v)
       d[k]=v,text,d

    return d
