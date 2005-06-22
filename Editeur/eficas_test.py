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
"""
    Ce module permet de lancer l'application EFICAS en affichant
    un ecran Splash pour faire patentier l'utilisateur
"""
# Modules Python
import sys
import Tkinter

# Modules Eficas
import import_code
import session

def lance_eficas(code,fichier=None):
    """
        Lance l'appli EFICAS
    """
    options=session.parse(sys.argv)
    root = Tkinter.Tk()
    import eficas
    if fichier :
        a=eficas.EFICAS(root,code=code,fichier = fichier,test=1)
        bureau=a.getBureau()
    else:
        eficas.EFICAS(root,code=code)

    print bureau.JDC.report()
    bureau.closeJDC()

def duplique_fichier(code,fichier=None,root=None):
    print code
    print fichier
    if root == None :
       root = Tkinter.Tk()
    import eficas
    import convert
    import generator
    import utils
    import string

    appli=eficas.EFICAS(root,code=code,fichier = fichier,test=1)
    format='homard'
    if convert.plugins.has_key(format):
       p=convert.plugins[format]()
       p.readfile(fichier)
       text=p.convert('exec',appli)
       text2=convertir(text)
       cata=appli.readercata.cata
       J=cata[0].JdC(procedure=text2,cata=cata)
       J.analyse()
       fileName=fichier+"_init"
       if generator.plugins.has_key(format):
          g=generator.plugins[format]()
          jdc_formate=g.gener(J,format='beautifie')
          print jdc_formate
          jdc_fini = string.replace(jdc_formate,'\r\n','\n')
          print jdc_fini
          utils.save_in_file(fileName+".comm",jdc_fini,None)

def convertir(texte):
    import re
    dict_change={"FICHIER_MED_MAILLAGE_N=":"FICHIER_MED_MAILLAGE_NP1","NOM_MED_MAILLAGE_N=":"NOM_MED_MAILLAGE_NP1"}
    for mot in dict_change.keys():
        if( re.search(mot,texte)):
          indicenouveau=re.search(mot,texte).end()
          indicefinnouveau= texte.find(",",indicenouveau)
          avant=dict_change[mot]
          if( re.search(avant,texte)):
             indiceancien=re.search(avant,texte).end()+1
             indicefinancien= texte.find(",",indiceancien)
             valeur=texte[indiceancien:indicefinancien]
             texte=texte[0:indicenouveau]+valeur+texte[indicefinnouveau:]
    liste_mot_clef_None=['CRIT_RAFF_ABS','CRIT_RAFF_REL','CRIT_RAFF_PE','CRIT_DERA_ABS','CRIT_DERA_REL','CRIT_DERA_PE','NITER','NOM_MED_MAILLAGE_NP1','FICHIER_MED_MAILLAGE_NP1']

    for mot in liste_mot_clef_None:
        if( re.search(mot,texte)):
           indice=re.search(mot,texte).end()+1
           indicefin= texte.find(",",indice)
           texte=texte[0:indice]+"None"+texte[indicefin:]
    return texte
        
