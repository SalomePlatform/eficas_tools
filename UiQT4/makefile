PYUIC = pyuic4
.PHONY : all
.SUFFIXES : .ui .py


PY_FILES = desChoixCata.py desCommande.py desCommentaire.py desError.py desFormule.py desInactif.py \
	desInclude.py desListeParam.py  desMCFact.py desMCListAjout.py desParam.py \
	desPlusieursBase.py desPlusieursInto.py desPoursuite.py desRacine.py desSelectVal.py \
	desUniqueASSD.py desUniqueBase.py desUniqueComp.py desUniqueInto.py desUniqueSDCOInto.py \
	desUniqueSDCO.py desVisu.py  aideQT.py OptionsEditeur.py OptionsPdf.py myMain.py \
	desViewTexte.py desPixmap.py desMatrice.py OptionsOT.py OptionsCuve.py desChoixMap.py \
        OptionsMAP.py desImage.py desChoixCode.py desRecherche.py

%.py:%.ui
	${PYUIC} -x -o $@ $<

all : $(PY_FILES)
clean :
	-rm -rf $(PY_FILES) *.pyc

