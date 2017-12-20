# -*- coding: utf-8 -*-
import os,sys

# repIni sert a localiser le fichier editeur.ini

repIni=os.path.dirname(os.path.abspath(__file__))
INSTALLDIR=os.path.join(repIni,'..')
sys.path[:0]=[INSTALLDIR]


# Codage des strings qui accepte les accents (en remplacement de 'ascii')
encoding='iso-8859-1'

# Choix des catalogues
# format du Tuple (code,version,catalogue,formatOut, finit par defaut eventuellement)
catalogues = (
# ('Adao','V1',os.path.join(repIni,'ADAO_Cata_V1.py'),'python','python'),
# ('Adao','V770',os.path.join(repIni,'ADAO_Cata_V0_V7_7_0.py'),'python','python'),
# ('Adao','V83',os.path.join(repIni,'ADAO_Cata_V0_V8_3_0_DEV.py'),'dicoImbrique','dico'),
# ('Adao','dico',os.path.join(repIni,'ADAO_Cata_V0_V8_3_0_DEV.py'),'dico','dico'),
 ('Adao','V83',os.path.join(repIni,'ADAO_Cata_V0_V8_3_0_DEV.py'),'python','python'),
# ('Adao','V751',os.path.join(repIni,'ADAO_Cata_V0_V7_5_1.py'),'python','python'),
)

# lang indique la langue utilisee pour les chaines d'aide : fr ou ang

lang='fr'
closeAutreCommande = True
closeFrameRechercheCommande = True
#closeEntete = True
closeArbre = True
translatorFichier = os.path.join(repIni,'Adao')
nombreDeBoutonParLigne=1

