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

install ( FILES __init__.py parseur_python.py convert_python.py
          DESTINATION ${CMAKE_INSTALL_PREFIX}/convert
        )

# Installation des fichiers : Open TURNS
if (WITH_OPENTURNS)
  install ( FILES convert_openturns_study.py convert_openturns_wrapper.py
            DESTINATION ${CMAKE_INSTALL_PREFIX}/convert
          )
endif (WITH_OPENTURNS)

# Installation des fichiers : Aster
if (WITH_ASTER)
  install ( FILES convert_asterv5.py
            DESTINATION ${CMAKE_INSTALL_PREFIX}/convert
          )
  install ( DIRECTORY Parserv5
            DESTINATION ${CMAKE_INSTALL_PREFIX}/convert
	    FILES_MATCHING PATTERN *.py PATTERN *.tag PATTERN README
            PATTERN CVS EXCLUDE
          )
endif (WITH_ASTER)

# Installation des fichiers : MAP
if (WITH_MAP)
  install ( FILES convert_map.py
            DESTINATION ${CMAKE_INSTALL_PREFIX}/convert
          )
endif (WITH_MAP)

# Installation des fichiers : SEP
if (WITH_SEP)
  install ( FILES convert_SEP.py
            DESTINATION ${CMAKE_INSTALL_PREFIX}/convert
          )
endif (WITH_SEP)

### Local Variables:
### mode: cmake
### End:
