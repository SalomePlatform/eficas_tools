"""
    Ce module réalise toutes les mises à jour du chemin pour 
    les imports de modules Python
"""
import sys
import prefs
# Ce chemin permet d'importer les modules Noyau et Validation
# représentant le code utilisé (si fourni)
if prefs.CODE_PATH:
   sys.path[:0]=[prefs.CODE_PATH]
   import Noyau,Validation
   del sys.path[0]

# Ensuite on utilise les packages de l'intallation
sys.path[:0]=[prefs.INSTALLDIR]
import Accas
