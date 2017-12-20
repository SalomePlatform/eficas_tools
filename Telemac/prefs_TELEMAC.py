# -*- coding: utf-8 -*-
#            maConfiguration MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================

from __future__ import absolute_import
import os,sys
# repIni sert a localiser le fichier editeur.ini
# Obligatoire
repIni=os.path.dirname(os.path.abspath(__file__))
INSTALLDIR=os.path.join(repIni,'..')
sys.path[:0]=[INSTALLDIR]


# lang indique la langue utilisee pour les chaines d'aide : fr ou ang
lang='ang'
#lang='fr'
#force_langue=True

# Codage des strings qui accepte les accents (en remplacement de 'ascii')
encoding='iso-8859-1'
docPath=repIni

#
catalogues=(
   #('TELEMAC','default',os.path.join(repIni,'Telemac_Cata_nouveau.py'),'TELEMAC','python'),
   #('TELEMAC','cas',os.path.join(repIni,'Telemac_Cata.py'),'TELEMAC','TELEMAC'),
   #('2D','cas',os.path.join(repIni,'Telemac2d_Cata_auto.py'),'TELEMAC','TELEMAC'),
   ('TELEMAC','pn',os.path.join(repIni,'telemac2d_V6_cata.py'),'TELEMAC','TELEMAC'),
   #('2222D','cas',os.path.join(repIni,'telemac2d_V6_cata.py'),'TELEMAC','TELEMAC'),
   #('TELEMAC','cas',os.path.join(repIni,'Telemac_Cata.py'),'python','TELEMAC3'),
   #('YOHAN','cas',os.path.join(repIni,'Cata.py'),'TELEMAC','TELEMAC'),
   #('TELEMAC','comm',os.path.join(repIni,'Telemac_Cata.py'),'TELEMAC2','python'),
)
mode_nouv_commande="figee"
affiche         = "ordre"
translatorFichier = os.path.join(repIni,'labelCataToIhm')
closeFrameRecherche=True
