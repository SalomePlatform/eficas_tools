# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
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

# Question : Doit-on installer le repertoire Patrons meme s'il est vide ?

# Installation des fichiers d'aide : Open TURNS
#if (WITH_OPENTURNS)
#  install ( DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/OPENTURNS_STUDY
#            DESTINATION ${CMAKE_INSTALL_PREFIX}/Editeur/Patrons
#            FILES_MATCHING PATTERN *.comm
#            PATTERN CVS EXCLUDE
#	  )
#endif (WITH_OPENTURNS)

# Installation des fichiers d'aide : Aster
if (WITH_ASTER)
  install ( DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/ASTER
            DESTINATION ${CMAKE_INSTALL_PREFIX}/Editeur/Patrons
	    FILES_MATCHING PATTERN *.comm
            PATTERN CVS EXCLUDE
	  )
endif (WITH_ASTER)

### Local Variables:
### mode: cmake
### End:
