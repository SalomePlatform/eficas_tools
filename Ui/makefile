PYUIC = pyuic
.PHONY : all
.SUFFIXES : .ui .py


PY_FILES = desChoixCata.py desCommande.py desCommentaire.py desError.py desFormule.py desInactif.py \
       desInclude.py desListeParam.py desMacro.py desMCFact.py desMCListAjout.py desParam.py \
       desPlusieursBase.py desPlusieursInto.py desPoursuite.py desRacine.py desSelectVal.py \
       desUniqueASSD.py desUniqueBase.py desUniqueComp.py desUniqueInto.py desUniqueSDCOInto.py \
       desUniqueSDCO.py desVisu.py myMain.py aideQT.py OptionsEditeur.py OptionsPdf.py

%.py:%.ui
	${PYUIC} -o $@ $<

all : $(PY_FILES)
