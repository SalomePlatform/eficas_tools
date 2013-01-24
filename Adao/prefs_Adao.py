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
 ('Adao','V0',os.path.join(repIni,'ADAO_Cata_V0.py'),'python','python'),
# ('Adao','V1',os.path.join(repIni,'ADAO_Cata_V1.py'),'python','python'),
 ('Adao','V2',os.path.join(repIni,'ADAO_Cata_V2.py'),'python','python'),
)

# lang indique la langue utilisée pour les chaines d'aide : fr ou ang
lang='fr'


