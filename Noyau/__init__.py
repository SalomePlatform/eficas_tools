""" 
    Ce package fournit les classes de base d'EFICAS.
    Ces classes permettent d'effectuer quelques op�rations basiques :

      - la cr�ation

      - la v�rification des d�finitions

      - la cr�ation d'objets de type OBJECT � partir d'une d�finition de type ENTITE
"""
# Avant toutes choses, on met le module context dans le global de l'interpreteur (__builtin__)
# sous le nom CONTEXT afin d'avoir acc�s aux fonctions
# get_current_step, set_current_step et unset_current_step de n'importe o�
import context
import __builtin__
__builtin__.CONTEXT=context

# Classes de base
from N_SIMP import SIMP
from N_FACT import FACT
