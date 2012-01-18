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
    Ce module contient des utilitaires divers
"""
import os,re
import glob
import traceback
import codecs,types

def substract_list(liste1,liste2):
  """ 
      Enleve tous les elements de liste2 presents dans liste1 et retourne liste1
  """
  for item in liste2:
    try:
      liste1.remove(item)
    except:
      pass
  return liste1

def get_rep_user():
  """
      Determine sur quelle plate-forme s'execute Eficas et recherche
      le repertoire de l'utilisateur /$home/Eficas_install
  """
  if os.name not in ('posix','nt'):
    print "Systeme non reconnu par Eficas"
    print "Prevenir la maintenance"
    sys.exit(0)
  if os.name == 'nt':
    try:
      drive = os.environ['HOMEDRIVE']
      nom_user = os.environ['USERNAME']
      rep_user_eficas = drive+'\\'+nom_user+'\\'+'Eficas_install'
    except:
      rep_user_eficas = os.path.join('C:','Eficas_install')
  else :
    rep_user_eficas= os.path.join(os.environ['HOME'],'.Eficas_install')
  if os.path.exists(rep_user_eficas):
    if os.path.isfile(rep_user_eficas) :
      print "Un fichier de nom %s existe deja : impossible de creer un repertoire de meme nom" %rep_user_eficas
      sys.exit(0)
  else :
    try:
      os.mkdir(rep_user_eficas)
    except:
      print "Creation du repertoire %s impossible\n Verifiez vos droits d'acces" %rep_user_eficas
  return rep_user_eficas

def read_file(file):
  """
      ouvre le fichier file et retourne son contenu
      si pbe retourne None
  """
  try :
    f=open(file)
    text=f.read()
    f.close()
    return text
  except:
    return None

def save_in_file(file,text,dir=None):
  """
      cree le fichier file (ou l'ecrase s'il existe) et ecrit text dedans
      retourne 1 si OK 0 sinon
  """
  try :
      import string
      #file=string.split(file,"/")[-1]
      if dir != None:
         os.chdir(dir)
      f=open(file,'w')
      f.write(text)
      f.close()
      return 1
  except:
      return 0

def extension_fichier(pathAndFile):
    """ Return ext if path/filename.ext is given """
    return os.path.splitext(pathAndFile)[1][1:]

def stripPath(pathAndFile):
    """ Return filename.ext if path/filename.ext is given """
    return os.path.split(pathAndFile)[1]

def init_rep_cata_dev(fic_cata,rep_goal):
  """ 
      Initialise le repertoire des catalogues developpeurs (chemin d'acces donne
      dans le fichier eficas.ini cad :
        - le cree s'il n'existe pas encore
        - copie dedans les 3 fichiers necessaires :
          * __init__.py (pour que ce repertoire puisse etre interprete comme un package)
          * entete.py (pour realiser les import necessaires a l'interpretation des catalogues)
          * declaration_concepts.py (idem)
        - cree le fichier cata_developpeur.py qui sera par la suite importe
  """
  try :
    if not os.path.isdir(rep_goal) :
      os.mkdir(rep_goal)
    #texte_entete = get_entete_cata(fic_cata)
    texte_entete=""
    # rep_goal doit contenir les catalogues du developpeur sous la forme *.capy
    # il faut creer le catalogue developpeur par concatenation de entete,declaration_concepts
    # et de tous ces fichiers
    cur_dir = os.getcwd()
    os.chdir(rep_goal)
    l_cata_dev = glob.glob('*.capy')
    if os.path.isfile('cata_developpeur.py') : os.remove('cata_developpeur.py')
    if len(l_cata_dev) :
      # des catalogues developpeurs sont effectivement presents : on cree cata_dev.py dans rep_goal
      str = ''
      str = str + texte_entete+'\n'
      for file in l_cata_dev :
        str = str + open(file,'r').read() +'\n'
      open('cata_developpeur.py','w+').write(str)
    os.chdir(cur_dir)
  except:
    traceback.print_exc()
    print "Impossible de transferer les fichiers requis dans :",rep_goal

def get_entete_cata(fic_cata):
  """ Retrouve l'entete du catalogue """
  l_lignes = open(fic_cata,'r').readlines()
  txt = ''
  flag = 0
  for ligne in l_lignes :
    if re.match("# debut entete",ligne) : flag = 1
    if re.match("# fin entete",ligne) : break
    if not flag : continue
    txt = txt + ligne
  return txt

