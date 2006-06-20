# -*- coding: utf-8 -*-
"""
    Ce module permet de définir la variable DEVELOPPEUR indiquant
    que l'utilisateur courant fait partie de la liste des développeurs.
    Ce qui lui donne un accès aux versions actives des fonctions
    ICI, MESSAGE, SCRUTE, ... définies dans le module Utilites
    à condition qu'ils utilisent le module sur une station cli*.

    Pour ajouter un nouveau développeur, il faut modifier le dictionaire
    d_dev ci-dessous
"""


DEVELOPPEUR=None

import os
def hostname() :
        return os.uname()[1]
group_eficas=108
group_salome=107


# Test pour identifier un utilisateur développeur d'Eficas
groups = os.getgroups()
test_devel = hostname()[0:3]=="cli" and ( group_eficas in groups or group_salome in groups )
if test_devel :
    d_dev = { 10618 : "antoine" , 10621 : "Pascale" , 20132 : "chris" , 10214 : "salome" }
    if os.getuid() in d_dev.keys() :
        DEVELOPPEUR=d_dev[ os.getuid() ]
        import sys
        sortie=sys.stderr
        sortie.write( "import de "+__name__+" : $Id: developpeur.py,v 1.2.8.1 2006/03/10 15:09:53 eficas Exp $" )
        sortie.write( "\n" )


if __name__ == "__main__" :
    print DEVELOPPEUR
