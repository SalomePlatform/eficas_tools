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
import os

def substract_list(liste1,liste2):
  """ 
      Enlève tous les éléments de liste2 présents dans liste1 et retourne liste1
  """
  for item in liste2:
    try:
      liste1.remove(item)
    except:
      pass
  return liste1

def get_rep_user():
  """
      Détermine sur quelle plate-forme s'exécute Eficas et recherche
      le répertoire de l'utilisateur /$home/Eficas_install
  """
  if os.name not in ('posix','nt'):
    print "Système non reconnu par Eficas"
    print "Prévenir la maintenance"
    sys.exit(0)
  if os.name == 'nt':
    try:
      drive = os.environ['HOMEDRIVE']
      nom_user = os.environ['USERNAME']
      rep_user_eficas = drive+'\\'+nom_user+'\\'+'Eficas_install'
    except:
      rep_user_eficas = os.path.join('C:','Eficas_install')
  else :
    rep_user_eficas = os.path.join(os.environ['HOME'],'Eficas_install')
  if os.path.exists(rep_user_eficas):
    if os.path.isfile(rep_user_eficas) :
      print "Un fichier de nom %s existe déjà : impossible de créer un répertoire de même nom" %rep_user_eficas
      sys.exit(0)
  else :
    try:
      os.mkdir(rep_user_eficas)
    except:
      print "Création du répertoire %s impossible\n Vérifiez vos droits d'accès" %rep_user_eficas
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

def save_in_file(file,text):
  """
      crée le fichier file (ou l'écrase s'il existe) et écrit text dedans
      retourne 1 si OK 0 sinon
  """
  try :
    f=open(file,'w+')
    f.write(text)
    f.close()
    return 1
  except:
    return 0

def extension(pathAndFile):
    """ Return ext if path/filename.ext is given """
    return os.path.splitext(pathAndFile)[1][1:]

def stripPath(pathAndFile):
    """ Return filename.ext if path/filename.ext is given """
    return os.path.split(pathAndFile)[1]

