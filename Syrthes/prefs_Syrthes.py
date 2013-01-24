# -*- coding: utf-8 -*-
import os,sys

# repIni sert à localiser le fichier editeur.ini
# Obligatoire
repIni=os.path.dirname(os.path.abspath(__file__))
INSTALLDIR=os.path.join(repIni,'..')
sys.path[:0]=[INSTALLDIR]


# Codage des strings qui accepte les accents (en remplacement de 'ascii')
encoding='iso-8859-1'

# Choix des catalogues
# format du Tuple (code,version,catalogue,formatOut, finit par defaut Ãventuellement)
catalogues = (

# catalogue avec generation Phys et materiaux reels
 ('Syrthes','V0',os.path.join(repIni,'cata_martine.py'),'python','python'),
)


# lang indique la langue utilisée pour les chaines d'aide : fr ou ang
lang='fr'


