#!/usr/bin/env python
"""
    Ce module sert à lancer EFICAS configuré pour Code_Saturne
"""
# Modules Python
import sys

# Modules Eficas
import prefs
sys.path[:0]=[prefs.INSTALLDIR]

import Editeur
from Editeur import eficas_go

if len(sys.argv) > 1 :
    # on veut ouvrir un fichier directement au lancement d'Eficas
    eficas_go.lance_eficas(code='SATURNE',fichier = sys.argv[1])
else:
    # on veut ouvrir Eficas 'vide'
    eficas_go.lance_eficas(code='SATURNE')

