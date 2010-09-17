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

# Installation de tous les fichiers Python du repertoire et des sous-repertoires (sauf CVS)
install ( FILES browser.py compobase.py compobloc.py compocommandecomm.py compocomm.py
                compoerror.py compofact.py compoformule.py compojdc.py compomacro.py
                compomclist.py componiveau.py componuplet.py compooper.py compoparam.py
                compoproc.py composimp.py editor.py eficas_go.py 
                __init__.py monChoixCata.py monCommandePanel.py
                monCommentairePanel.py monFonctionPanel.py monFormulePanel.py
                monInactifPanel.py monIncludePanel.py monListeParamPanel.py
                monMacroPanel.py monMatricePanel.py monMCFactPanel.py
                monMCListAjoutPanel.py monOptionsPdf.py monParamPanel.py monPixmap.py
                monPlusieursASSDPanel.py monPlusieursBasePanel.py monPlusieursIntoPanel.py
                monPoursuitePanel.py monRacinePanel.py monSelectVal.py
                monUniqueASSDPanel.py monUniqueBasePanel.py monUniqueCompPanel.py monUniqueIntoPanel.py
                monUniqueSDCOIntoPanel.py monUniqueSDCOPanel.py monVisu.py
                politiquesValidation.py qtCommun.py qtEficas.py
                qtSaisie.py readercata.py typeNode.py utilIcons.py viewManager.py
          DESTINATION ${CMAKE_INSTALL_PREFIX}/InterfaceQT4
	)

# Installation des fichiers : OpenTURNS
if (WITH_OPENTURNS)
  install ( FILES monOptions_OPENTURNS_STUDY.py monOptions_OPENTURNS_WRAPPER.py
            DESTINATION ${CMAKE_INSTALL_PREFIX}/InterfaceQT4
          )
endif (WITH_OPENTURNS)

# Installation des fichiers : Aster
if (WITH_ASTER)
  install ( FILES gereTraduction.py monOptions_ASTER.py ssIhm.py
            DESTINATION ${CMAKE_INSTALL_PREFIX}/InterfaceQT4
          )
endif (WITH_ASTER)

# Installatiion des fichiers : MAP
if (WITH_MAP)
  install ( FILES monChoixMap.py 
            DESTINATION ${CMAKE_INSTALL_PREFIX}/InterfaceQT4
          )
endif (WITH_MAP)

#monOptions_CUVE2DG.py

### Local Variables:
### mode: cmake
### End:
