# -*- coding: iso-8859-1 -*-

# modules de base
import commands
import sys
from tkFileDialog import *

cartouche = "DEBUT();\n\n"
cartouche = cartouche + "%(MATERIAU)s\n\n"
cartouche = cartouche + "MAIL=LIRE_MAILLAGE(UNITE=21,\n"
cartouche = cartouche + "                   FORMAT='MED',\n"
cartouche = cartouche + "                   INFO_MED=2,);\n\n"
cartouche = cartouche + "%(MODELISATION)s\n\n"
cartouche = cartouche + "MATE=AFFE_MATERIAU(MAILLAGE=MAIL,\n"
cartouche = cartouche + "                   AFFE=_F(TOUT='OUI',\n"
cartouche = cartouche + "                           MATER=MA,),);\n\n"
cartouche = cartouche + "%(CHARGEMENT)s\n\n"
cartouche = cartouche + "RESU=MECA_STATIQUE(MODELE=MODE,\n"
cartouche = cartouche + "                   CHAM_MATER=MATE,\n"
cartouche = cartouche + "                   EXCIT=_F(CHARGE=CHAR,),);\n\n"
cartouche = cartouche + "RESU=CALC_ELEM(reuse =RESU,\n"
cartouche = cartouche + "               MODELE=MODE,\n"
cartouche = cartouche + "               CHAM_MATER=MATE,\n"
cartouche = cartouche + "               RESULTAT=RESU,\n"
cartouche = cartouche + "               OPTION=('SIEF_ELGA_DEPL','SIGM_ELNO_DEPL','EQUI_ELNO_SIGM',),\n"
cartouche = cartouche + "               EXCIT=_F(\n"
cartouche = cartouche + "               CHARGE=CHAR,),);\n\n"
cartouche = cartouche + "RESU=CALC_NO(reuse =RESU,\n"
cartouche = cartouche + "             RESULTAT=RESU,\n"
cartouche = cartouche + "             OPTION=('EQUI_NOEU_SIGM','SIGM_NOEU_DEPL',),);\n\n"
cartouche = cartouche + "IMPR_RESU(FORMAT='MED',\n"
cartouche = cartouche + "          UNITE=80,\n"
cartouche = cartouche + "          RESU=_F(MAILLAGE=MAIL,\n"
cartouche = cartouche + "                  RESULTAT=RESU,\n"
cartouche = cartouche + "                  NOM_CHAM=('SIGM_NOEU_DEPL','EQUI_NOEU_SIGM','DEPL',),),);\n\n"
cartouche = cartouche + "FIN();"

dict_fichier = {}

class Fichier:
    """
    réalise la création du fichier de commandes avec les valeurs saisies à partir de la chaine cartouche
    - utilisation du % export dico
    """
    def __init__(self, appli, salomeRef):
        self.appli = appli

	# initialisation pour la publication dans l'arbre d'étude
        self.salome = salomeRef
    
    def creer(self):
        """
        crée le fichier de commandes
        """
	# définition de MATERIAU
        s = 'MA=DEFI_MATERIAU(ELAS=_F(E='
        tmp = str(self.appli.etude.materiau_e.latin1())
        s = s + tmp
        s = s + ', \n'
        s = s + '\t\t\t NU='
        tmp = str(self.appli.etude.materiau_nu.latin1())
        s = s + tmp
        s = s + ',),);\n\n'

	dict_fichier['MATERIAU'] = s
       
        # définition de MODELISATION
        s = 'MODE=AFFE_MODELE(MAILLAGE=MAIL,\n'
	s = s + "\t\tAFFE=_F(TOUT='OUI',\n"
	s = s + "\t\t\t\tPHENOMENE='MECANIQUE',\n"
	s = s + "\t\t\t\tMODELISATION="
	s = s + "'" + self.appli.etude.modelisation + "'"
	s = s + ',),);\n\n'

	dict_fichier['MODELISATION'] = s
       
        # définition des ddls et pressions
	s = 'CHAR=AFFE_CHAR_MECA(MODELE=MODE,\n'
	s = s + '\t\t\tFACE_IMPO=('
	for i in range(0, len(self.appli.etude.ddls), 3):
           liste = self.appli.etude.ddls[i:i+3]
           if liste[0][2] == '' and liste[1][2] == '' and liste[2][2] == '':
              pass
           else:
              s = s + "\n\t\t\t\t_F(GROUP_MA='" + str(liste[0][0]) + "',"
              for i in range(3):
                  if liste[i][2] != '':
                     s = s + "\n\t\t\t\t\t\t" + str(liste[i][1]) + "=" + str(liste[i][2]) + ","
              s = s + '),'
        s = s + '),\n'
            
        s = s + '\t\t\tPRES_REP=('
        for pres in self.appli.etude.chargements:
            if pres[1] != '':
               s = s + "\n\t\t\t\t_F(GROUP_MA='" + pres[0] + "',"
               s = s + "\n\t\t\t\t\t\tPRES=" + pres[1] + ",),"
        s = s + "),);"
       
        dict_fichier['CHARGEMENT'] = s 

        ch = cartouche % dict_fichier

        # si flag = E enregistrement manuel du fichier
	# si flag = A enregistrement automatique
	if self.appli.flagEficasOrAster == 'A':
	   # ouverture du nouveau fichier en écriture
           f_temp = open('/tmp/temporaire.comm', 'w')

           # écriture du fichier
	   f_temp.write(ch)

           # fermeture du fichier créé
           f_temp.close()

	   # publication du fichier dans l'arbre d'étude Salome
           import eficasEtude
           self.salome.rangeInStudy('/tmp/temporaire.comm')
        elif self.appli.flagEficasOrAster == 'E':
           # on demande Ã|  l'utilisateur dans quel fichier il veut sauvegarder
           filesave = asksaveasfilename(defaultextension = '.comm',
                                        initialdir = commands.getoutput("echo $HOME"),
                                        title="Sauvegarde du fichier de commandes")
	   # ouverture du nouveau fichier en écriture
           f_temp = open(filesave, 'w')
           # écriture du fichier
           f_temp.write(ch)
           # fermeture du fichier créé
           f_temp.close()

	   # publication du fichier dans l'arbre d'étude Salome
           import eficasEtude
           self.salome.rangeInStudy(filesave)
        else:
           print "Erreur flag enreigstrement fichier .comm (A pour Aster, E pour Eficas)"
	   sys.exit()
							       
