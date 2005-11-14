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
    Ce module sert pour charger les param�tres de configuration d'EFICAS
"""
# Modules Python
import os,sys,string,types
import traceback

# Modules Eficas
from widgets import showinfo,showerror,askretrycancel
import utils

class CONFIG:
  def __init__(self,appli,rep_ini):
      # si appli == None on est en mode commande (hors EFICAS)
      self.appli = appli  
      if self.appli:self.parent=appli.top
      else:self.parent=None
      self.rep_ini = rep_ini
      self.rep_user = utils.get_rep_user()
      self.lecture_parametres()

  def lecture_parametres(self):
      """
         Cette m�thode teste l'existence du fichier editeur.ini au bon endroit et lance
         son interpr�tation
      """
      fic_ini = os.path.join(self.rep_ini,'editeur.ini')
      if not os.path.exists(fic_ini) or not os.path.isfile(fic_ini):
        if self.appli :
          showerror("Erreur","Impossible de trouver le fichier %s ! \n Pr�venez la maintenance ..." %fic_ini)
        else:
          print "Impossible de trouver le fichier %s ! \n Pr�venez la maintenance ..." %fic_ini
        sys.exit(0)
      self.fic_ini = fic_ini
      self.init_liste_param()
      self.lecture_fichier_ini_standard()
      self.lecture_fichier_ini_utilisateur()

  def lecture_fichier_ini_standard(self):
      """
      Relit les param�tres du fichier eficas.ini
      """
      txt = utils.read_file(self.fic_ini)
      d={}
      try:
         exec txt in d
      except:
         l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
         showerror("Erreur","Une erreur s'est produite dans la relecture du fichier de configuration : "
                       + self.fic_ini+"\n"+string.join(l[2:]))
         print "Erreur � la lecture du fichier de configuration : %s" % self.fic_ini 
         print string.join(l[2:])
         sys.exit()
      for attr in self.l_nom_param:
          nom_attr,statut,defaut = attr
          #valeur = d.get(nom_attr,None)
          valeur = d.get(nom_attr,defaut)
          if not valeur and statut=='o':
              showerror("Erreur","Une erreur s'est produite dans la relecture du fichier de configuration : "
                       + self.fic_ini+"\n EFICAS va vous demander les nouveaux param�tres")
              return
          setattr(self,nom_attr,valeur)
      self.init_liste_param()

  def lecture_fichier_ini_utilisateur(self):
      """
      Surcharge les param�tres standards par les param�tres utilisateur s'ils existent
      """
      self.fic_ini_utilisateur = os.path.join(self.rep_user,'eficas.ini')
      if not os.path.isfile(self.fic_ini_utilisateur):
          # pas de fichier de configuration utilisateur --> on passe
          return
      txt = utils.read_file(self.fic_ini_utilisateur)
      d={}
      try:
          exec txt in d
      except :
          showinfo("Erreur","Impossible d'interpr�ter le fichier de configuration utilisateur : %s" %self.fic_ini_utilisateur)
          traceback.print_exc()
          return
      for attr in self.l_nom_param:
          nom_attr,statut,defaut = attr
          valeur = d.get(nom_attr,None)
          if valeur :
              setattr(self,nom_attr,valeur)
      self.init_liste_param()

  def init_liste_param(self):
      """
      G�n�re la liste des param�tres
      l_param est une liste de tuples o� chaque tuple est de la forme :
      (label,nature,nom_var,defaut)
      """
      self.l_param=[]
      # r�pertoire initial pour OPEN/SAVE des fichiers de commande
      # Par defaut, EFICAS utilise le repertoire utilisateur $HOME/Eficas_install
      # Il est possible de specifier dans editeur.ini ou eficas.ini un autre chemin
      # Ce peut etre un chemin absolu ou le repertoire courant (os.curdir)
      if hasattr(self,'initialdir'):
          self.l_param.append(("R�pertoire initial pour Open/save des fichiers de commande",'rep','initialdir',self.initialdir))
      else:
          self.l_param.append(("R�pertoire initial pour Open/save des fichiers de commande",'rep','initialdir',self.rep_user))
      # r�pertoire de travail
      if hasattr(self,'rep_travail'):
          self.l_param.append(("R�pertoire de travail",'rep','rep_travail',self.rep_travail))
      else:
          self.l_param.append(("R�pertoire de travail",'rep','rep_travail',
                               os.path.join(self.rep_user,'uaster','tmp_eficas')))
      # r�pertoire des catalogues mat�riaux
      if hasattr(self,'rep_mat'):
          self.l_param.append(("R�pertoire materiaux",'rep','rep_mat',self.rep_mat))
      else:
          self.l_param.append(("R�pertoire materiaux",'rep','rep_mat','/aster/v4/materiau'))
      # chemin d'acc�s ex�cutable acrobat reader
      if hasattr(self,'exec_acrobat'):
          self.l_param.append(("Ligne de commande Acrobat Reader",'file','exec_acrobat',self.exec_acrobat))
      else:
          self.l_param.append(("Ligne de commande Acrobat Reader",'file','exec_acrobat',self.rep_user))
      # r�pertoire contenant la doc Aster
      if hasattr(self,'path_doc'):
          self.l_param.append(("Chemin d'acc�s � la doc Aster",'rep','path_doc',self.path_doc))
      else:
          self.l_param.append(("Chemin d'acc�s � la doc Aster",'rep','path_doc',self.rep_user))
      # chemin(s) d'acc�s au(x) catalogue(s)
      if hasattr(self,'catalogues'):
          self.l_param.append(("Versions du code ",'cata','catalogues',self.catalogues))
      else:
          self.l_param.append(("Versions du code ",'cata','catalogues',os.path.join(self.rep_ini,'..','Cata/cata.py')))
      # attribut d�veloppeur
      if hasattr(self,'isdeveloppeur'):
      #    self.l_param.append(("Etes-vous d�veloppeur ?",'YesNo','isdeveloppeur',self.isdeveloppeur))
           self.l_param.append(("Niveau de message ",'YesNo','isdeveloppeur',self.isdeveloppeur,'Deboggage','Utilisation'))
      else:
      #    self.l_param.append(("Etes-vous d�veloppeur ?",'YesNo','isdeveloppeur','NON'))
           self.l_param.append(("Niveau de message ",'YesNo','isdeveloppeur','NON','Deboggage','Utilisation'))
      # r�pertoire o� sont contenus les catalogues d�veloppeurs
      if hasattr(self,'path_cata_dev') and hasattr(self,'isdeveloppeur') and self.isdeveloppeur == 'OUI':
          self.l_param.append(("Chemin d'acc�s aux catalogues d�veloppeurs",'rep','path_cata_dev',self.path_cata_dev))
      else:
          self.l_param.append(("Chemin d'acc�s aux catalogues d�veloppeurs",'rep','path_cata_dev',
                               os.path.join(self.rep_user,'cata')))
      self.l_param = tuple(self.l_param)
      self.l_nom_param=[]
      statut='o'
      for tup in self.l_param:
          if tup[1] == 'YesNo':
              # les param�tres suivant tup sont facultatifs ...
              statut='f'
          self.l_nom_param.append((tup[2],statut,tup[3])) # nom,statut,defaut

  def affichage_fichier_ini(self):
      """
      Affichage des valeurs des param�tres relus par Eficas
      """
      import widgets
      result = widgets.Formulaire(self.parent,
                                  obj_pere = self,
                                  titre = "Param�tres n�cessaires � la configuration d'EFICAS",
                                  texte = "Voici les param�tres que requiert Eficas",
                                  items = self.l_param,
                                  mode='display',
                                  commande=('Modifier',self.creation_fichier_ini_si_possible))
      if result.resultat :
          print 'on sauvegarde les nouveaux param�tres :',result.resultat
          self.save_param_ini(result.resultat)

  def save_param_ini(self,dico):
      """
      Sauvegarde les nouveaux param�tres dans le fichier de configuration utilisateur
      """
      f=open(self.fic_ini_utilisateur,'w+')
      for k,v in dico.items():
         if k == 'catalogues' :
            f.write(k + '\t=\t' + str(v) + '\n')
         else:
            f.write(k + '\t=\t"' + str(v) + '"\n')
      f.close()
      self.lecture_fichier_ini_utilisateur()

  def creation_fichier_ini_si_possible(self):
      return self.creation_fichier_ini(mode='ignorer_annuler')

  def creation_fichier_ini(self,mode='considerer_annuler'):
      """
      R�cup�ration des valeurs des param�tres requis pour la cr�ation du fichier
      eficas.ini
      """
      import widgets
      texte = "EFICAS a besoin de certains renseignements pour se configurer\n"+\
              "Veuillez remplir TOUS les champs ci-dessous et appuyer sur 'Valider'\n"+\
              "Si vous annulez, EFICAS ne se lancera pas !!"
      items = self.l_param
      result = widgets.Formulaire(self.parent,
                                  obj_pere = self,
                                  titre = "Saisie des donn�es indispensables � la configuration d'EFICAS",
                                  texte = texte,
                                  items = items,
                                  mode='query')
      if not result.resultat :
          if mode == 'considerer_annuler':
             test = askretrycancel("Erreur","Donn�es incorrectes !")
             if not test:
                 # XXX On sort d'EFICAS, je suppose
                 self.appli.exitEFICAS()
             else:
                 self.creation_fichier_ini()
          else:
              return None
      else :
          self.save_param_ini(result.resultat)
          return result.resultat

def make_config(appli,rep):
    return CONFIG(appli,rep)


