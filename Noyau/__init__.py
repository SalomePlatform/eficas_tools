""" 
    Ce package fournit les classes de base d'EFICAS.
    Ces classes permettent d'effectuer quelques opérations basiques :

      - la création

      - la vérification des définitions

      - la création d'objets de type OBJECT à partir d'une définition de type ENTITE
"""
# Avant toutes choses, on met le module context dans le global de l'interpreteur (__builtin__)
# sous le nom CONTEXT afin d'avoir accès aux fonctions
# get_current_step, set_current_step et unset_current_step de n'importe où
import context
import __builtin__
__builtin__.CONTEXT=context

# Classes de base
from N_SIMP import SIMP
from N_FACT import FACT
