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

set ( _PYFILES )
macro ( eficas_compile_ui uifile )
  get_filename_component ( _file_we ${uifile} NAME_WE )
  set ( _pyfile "${_file_we}.py" )
  add_custom_command ( OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${_pyfile}
                       COMMAND ${PYUIC4} ARGS -x -o ${CMAKE_CURRENT_BINARY_DIR}/${_pyfile} ${CMAKE_CURRENT_SOURCE_DIR}/${uifile}
		       MAIN_DEPENDENCY ${CMAKE_CURRENT_SOURCE_DIR}/${uifile}
		       COMMENT "Compiling ${uifile}"
		     )
  list ( APPEND _PYFILES ${CMAKE_CURRENT_BINARY_DIR}/${_pyfile} )
endmacro ( eficas_compile_ui )

eficas_compile_ui ( OptionsCuve.ui )
eficas_compile_ui ( OptionsEditeur.ui )
eficas_compile_ui ( OptionsOT.ui )
eficas_compile_ui ( OptionsPdf.ui )
eficas_compile_ui ( aideQT.ui )
eficas_compile_ui ( desChoixCata.ui )
eficas_compile_ui ( desChoixCode.ui )
eficas_compile_ui ( desChoixMap.ui )
eficas_compile_ui ( desCommande.ui )
eficas_compile_ui ( desCommentaire.ui )
eficas_compile_ui ( desError.ui )
eficas_compile_ui ( desFormule.ui )
eficas_compile_ui ( desInactif.ui )
eficas_compile_ui ( desInclude.ui )
eficas_compile_ui ( desListeParam.ui )
eficas_compile_ui ( desMCFact.ui )
eficas_compile_ui ( desMCListAjout.ui )
eficas_compile_ui ( desMatrice.ui )
eficas_compile_ui ( desParam.ui )
eficas_compile_ui ( desPixmap.ui )
eficas_compile_ui ( desPlusieursBase.ui )
eficas_compile_ui ( desPlusieursInto.ui )
eficas_compile_ui ( desPoursuite.ui )
eficas_compile_ui ( desRacine.ui )
eficas_compile_ui ( desRecherche.ui )
eficas_compile_ui ( desSelectVal.ui )
eficas_compile_ui ( desUniqueASSD.ui )
eficas_compile_ui ( desUniqueBase.ui )
eficas_compile_ui ( desUniqueBool.ui )
eficas_compile_ui ( desUniqueComp.ui )
eficas_compile_ui ( desUniqueInto.ui )
eficas_compile_ui ( desUniqueSDCO.ui )
eficas_compile_ui ( desUniqueSDCOInto.ui )
eficas_compile_ui ( desViewTexte.ui )
eficas_compile_ui ( desVisu.ui )
eficas_compile_ui ( myMain.ui )

add_custom_target ( CompileUI ALL DEPENDS ${_PYFILES}
                    COMMENT "Built UI files"
                  )

install ( FILES ${_PYFILES}
          DESTINATION ${CMAKE_INSTALL_PREFIX}/UiQT4
        )

# Rules to compile TS files
SET(TSFILES eficas_en.ts
            eficas_fr.ts)

SET(QMFILES)
FOREACH(input ${TSFILES})
  GET_FILENAME_COMPONENT(base ${input} NAME_WE)
  SET(output ${CMAKE_CURRENT_BINARY_DIR}/${base}.qm)
  SET(QMFILES ${QMFILES} ${output})
  ADD_CUSTOM_COMMAND(OUTPUT ${output}
    COMMAND ${QT_LRELEASE_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/${input} -qm ${output}
    MAIN_DEPENDENCY ${input})
ENDFOREACH(input ${TSFILES})

ADD_CUSTOM_TARGET(CompileTS ALL DEPENDS ${QMFILES})
INSTALL(FILES ${QMFILES} DESTINATION ${CMAKE_INSTALL_PREFIX}/UiQT4)

### Local Variables:
### mode: cmake
### End:
