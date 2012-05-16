# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
"""
Contient la description des fichiers d'aide et leur structuration

chaque panneau est un tuple de 3 éléments :

- élément 1 : titre de la page
- élément 2 : URL du fichier à afficher quand on visualise cette page d'aide ou None si aucun
- élément 3 : tuple contenant les sous-panneaux de ce panneau (tuple de 3-tuples) ou None si aucun

La variable repertoire est initialisee avec le chemin du repertoire local
"""

import os

items =("Aide en ligne EFICAS",None,
            ( 
               ("FAQs",os.path.join(repertoire,"..","Editeur","faqs.txt"),None),
               ("Install",os.path.join(repertoire,"..","INSTALL"), 
                                ( 
                                   ("Procedure d'installation",os.path.join(repertoire,"..","INSTALL"),None), 
                                )
              ),
            ),
       )
