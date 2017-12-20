# -*- coding: utf-8 -*-
#
#  Copyright (C) 2012-2013 EDF
#
#  This file is part of SALOME HYDRO module.
#
#  SALOME HYDRO module is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SALOME HYDRO module is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SALOME HYDRO module.  If not, see <http://www.gnu.org/licenses/>.

import types
from Accas import *

def get_list_var_api(module):
#    """
#    Returns the list of variables avaialable throught the API for module
#
#    @param One of the modules of TELEMAC-MASCARET
#    """
     return ('A','B','C')
#    if module == 'TELEMAC2D':
#        from TelApy.api.t2d import Telemac2d
#        model = Telemac2d('dummy.cas')
#    elif module == 'TELEMAC3D':
#        from TelApy.api.t3d import Telemac3d
#        model = Telemac3d('dummy.cas')
#    elif module == 'SISYPHE':
#        from TelApy.api.sis import Sisyphe
#        model = Sisyphe('dummy.cas')
#    else:
#        return ['No variable available']

#    varnames, _ = model.list_variables()
#    del(model)
#    return sorted(varnames)

class Tuple:
  def __init__(self,ntuple):
    self.ntuple=ntuple

  def __convert__(self,valeur):
    if type(valeur) == types.StringType:
      return None
    if len(valeur) != self.ntuple:
      return None
    return valeur

  def info(self):
    return "Tuple de %s elements" % self.ntuple

  __repr__=info
  __str__=info

JdC = JDC_CATA(regles = (UN_PARMI('TELEMAC2D',)),
                        )



TELEMAC2D = PROC(
    nom = "TELEMAC2D", op = None,
    fr = u"Définition d'un cas d'étude Telemac2D",
    ang = u"Definition of a Telemac2D study case",
    STEERING_FILE = SIMP(statut = "o", typ = 'Fichier',
                       fr = u"Fichier de description du cas",
                       ang = u"Case description file",
    ),
    USER_FORTRAN = SIMP(statut = "f", typ = 'FichierOuRepertoire',
                        fr = "Fichier Fortran utilisateur",
                        ang = u"Fortran user file",
    ),
    WORKING_DIRECTORY = SIMP(statut = "o", typ = 'Repertoire',
                             defaut = '/tmp',
                             fr = "Repertoire de travail",
                             ang = u"Working directory user file",
    ),
    RESULT_DIRECTORY = SIMP(statut = "f", typ = 'Repertoire',
                            fr = "Repertoire de travail",
                            ang = u"Working directory user file",
    ),
    RESULTS_FILE_NAME = SIMP(statut = "f", typ = 'TXM',
                             fr = u"Fichier des resultats (Ecrasera celui dans le fichier cas)",
                             ang = u"Results file (Will replace the one in the steering file)"
    ),
    Consigne = SIMP(statut ="o", homo="information", typ="TXM",
                    defaut = "All index are in Python numbering (Starting from 0)",
    ),
    INPUT_VARIABLE = FACT(statut = 'f', max = '**',
                          fr = u"Variable d'entrée du calcul",
                          ang = u"Computation input variable",

        NAME = SIMP(statut = "o", typ = 'TXM',
                    fr = u"Nom de la variable (format Python)",
                    ang = u"Variable name (Python format)"
        ),
        VAR_INFO = FACT(statut = "o",
                        fr = u'Variable du modèle Telemac2D',
                        ang = u'Telemac2D model variable',

            VAR_NAME = SIMP(statut = "o", typ = 'TXM',
                            #max='**',
                            #intoSug = ('A','B','C'),
                            intoSug=get_list_var_api('TELEMAC2D'),
                            fr = u'Nom de la variable du modèle (ex: "MODEL.DEBIT")',
                            ang = u'Model variable name (ex: "MODEL.DEBIT")'
            ),
            DEFAULT_VALUE = SIMP(statut = "o", typ = 'TXM',
                                 fr = u'Valeur par défaut',
                                 ang = u'Default value',
            ),
            ZONE_DEF = FACT(statut = "o",
                            ang = u'Variable definition area',
                            fr = u'Zone de définition de la variable',

                TYPE = SIMP(statut = "o", typ = 'TXM',
                            into = ['INDEX', 'RANGE', 'POLYGON', 'POLYGON_FILE'],
                            fr = u'Type de definition de la variable',
                            ang = u'Type of definition for the variable',
                ),

                b_INDEX = BLOC(condition = "TYPE == 'INDEX'",
                    INDEX = SIMP(statut = "o", typ = Tuple(3),
                                 max='**',
                                 defaut = (0, 0, 0),
                                 ang = "Index of the variable",
                                 fr = u"Indice de la variable",
                                 validators = VerifTypeTuple(('I', 'I', 'I')),
                    ),
                ),
                b_RANGE = BLOC(condition = "TYPE == 'RANGE'",
                    RANGE = SIMP(statut = "o", typ = 'TXM',
                                 fr = u"Liste d'index pour des tableaux à une dimension ex: [1,3:8,666]",
                                 ang = "Range of index for one dimension arrays ex: [1,3:8,666]",
                    ),
                    Consigne = SIMP(statut ="o", homo="information", typ="TXM",
                                    defaut = "Format [0,2:8,50:88,666]",
                    ),
                ),
                b_POLYGON = BLOC(condition = "TYPE == 'POLYGON'",
                    POLYGON = SIMP(statut = "o",
                                   typ = Tuple(2),
                                   max = '**',
                                   fr = u"Liste des sommets (coordonnées X,Y) du "
                                        u"polygone définissant le contour de la zone",
                                   ang = "List of points (X,Y coordinates) of the "
                                         "polygon defining the border of the area",
                                   validators = VerifTypeTuple(('R', 'R')),
                    ),
                ),
                b_POLYGON_FILE = BLOC(condition = "TYPE == 'POLYGON_FILE'",
                    POLYGON_FILE = FACT(statut = "o",
                                        fr = u"Polygon dans un fichier",
                                        ang = "Polygone in a file",
                        FILE_NAME = SIMP(statut = "o", typ = 'Fichier',
                                         fr = u"Fichier contenant les info du polygone",
                                         ang = "File containing the polygon info",
                        ),
                        SEPARATOR = SIMP(statut = "o", typ = 'TXM',
                                         defaut = ',',
                                         fr = u"Separateur pour le fichier de polygone",
                                         ang = "Separator for the polygon file",
                        ),
                    ),
                ),
            ),
        ),
    ),
    OUTPUT_VARIABLE = FACT(statut = 'f', max = '**',
                           fr = u"Variable de sortie du calcul",
                           ang = u"Computation output variable",
        NAME = SIMP(statut = "o", typ = 'TXM',
                   fr = u"Nom de la variable",
                   ang = u"Variable name",
        ),
        VAR_INFO = FACT(statut = "o",
                        fr = u'Variable du modèle Telemac2D',
                        ang = u'Telemac2D model variable',
            VAR_NAME = SIMP(statut = "o", typ = 'TXM',
                            into = get_list_var_api('TELEMAC2D'),
                            fr = u'Nom de la variable du modèle (ex: "MODEL.DEBIT")',
                            ang = u'Model variable name (ex: "MODEL.DEBIT")',
            ),
            ZONE_DEF = FACT(statut = "o",
                            ang = u'Variable definition area',
                            fr = u'Zone de définition de la variable',
                INDEX = SIMP(statut = "o", typ = Tuple(3),
                             defaut = (0, 0, 0, ),
                             ang = "Index of the point / border",
                             fr = u"Indice du point ou de la frontière",
                             validators = VerifTypeTuple(('I', 'I', 'I')),
                ),
            ),
        ),
    ),
)

TEXTE_NEW_JDC="TELEMAC2D()"
