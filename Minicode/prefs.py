# -*- coding: utf-8 -*-
import os,sys

# REPINI sert � localiser le fichier editeur.ini
# Obligatoire
REPINI=os.path.dirname(os.path.abspath(__file__))

# INSTALLDIR sert � localiser l'installation d'Eficas
# Obligatoire
INSTALLDIR=os.path.join(REPINI,'..')

# CODE_PATH sert � localiser Noyau et Validation �ventuellement
# non contenus dans la distribution EFICAS
# Par d�faut on utilise les modules de INSTALLDIR
# Peut valoir None (defaut)
CODE_PATH = None
#CODE_PATH = os.path.join(REPINI,'../../Superv')
#CODE_PATH = "/home01/chris/projet_Eficas/Devel/SUPER6_3/Aster6_3/bibpyt"

# la variable code donne le nom du code a selectionner
code="MINICODE"

# lang indique la langue utilis�e pour les chaines d'aide : fr ou ang
lang='fr'

# Codage des strings qui accepte les accents (en remplacement de 'ascii')
encoding='iso-8859-1'

sys.path[:0]=[INSTALLDIR]

# ICONDIR sert � localiser le r�pertoire contenant les icones
# Par d�faut on utilise le r�pertoire icons dans Editeur
ICONDIR=os.path.join(INSTALLDIR,'Editeur','icons')
