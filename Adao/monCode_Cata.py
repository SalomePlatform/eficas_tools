# -*- coding: utf-8 -*-
from Accas import *

JdC = JDC_CATA (code = 'ADAO',
                execmodul = None,
                )
JdC = JDC_CATA (code = 'ADAO',
                execmodul = None,
                regles = ( AU_MOINS_UN ('ASSIMILATION_STUDY','CHECKING_STUDY'), AU_PLUS_UN ('ASSIMILATION_STUDY','CHECKING_STUDY')),
               )


ASSIMILATION_STUDY = PROC(nom="ASSIMILATION_STUDY", op=None, repetable           = "n",
        Study_name          = SIMP(statut="o", typ = "TXM"),
        Study_repertory     = SIMP(statut="f", typ = "Repertoire", min=1, max=1),
        Debug               = SIMP(statut="o", typ = "I", into=(0, 1), defaut=0),
        Algorithm           = SIMP(statut="o", typ = "TXM", into=("3DVAR", "Blue", "EnsembleBlue", "KalmanFilter", "LinearLeastSquares", "NonLinearLeastSquares", "ParticleSwarmOptimization", "QuantileRegression", )),
        Background          = FACT(statut="o",
                     regles=(UN_PARMI('SCRIPT_DATA_FILE','VECTOR_STRING'),),
                     Stored = SIMP(statut="o", typ = "I", into=(0, 1), defaut=0, fr="Choix de stockage interne ou non du concept parent", ang="Choice of the storage or not of the parent concept"),
                     SCRIPT_DATA_FILE = SIMP(statut = "f", typ = "FichierNoAbs", validators=(OnlyStr()), fr="En attente d'un nom de fichier script, avec ou sans le chemin complet pour le trouver, contenant la définition d'une variable interne de même nom que le concept parent", ang="Waiting for a script file name, with or without the full path to find it, containing the definition of an internal variable of the same name as the parent concept"),
                     VECTOR_STRING = SIMP(statut = "f", typ = "TXM", fr="En attente d'une chaine de caractères entre guillements. Pour construire un vecteur, ce doit être une suite de nombres, utilisant un espace ou une virgule pour séparer deux éléments et un point-virgule pour séparer deux lignes", ang="Waiting for a string in quotes. To build a vector, it has to be a float serie, using a space or comma to separate two elements in a line, a semi-colon to separate rows"),
                              ),

)
