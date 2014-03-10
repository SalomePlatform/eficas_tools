PYUIC = pyuic4
QTRELEASE = lrelease-qt4
.PHONY : all
.SUFFIXES : .ui .py .ts .qm


PY_FILES = desChoixCata.py desCommande.py desCommentaire.py desError.py desFormule.py desInactif.py \
	desInclude.py desListeParam.py  desMCFact.py desMCListAjout.py desParam.py \
	desPlusieursBase.py desPlusieursInto.py desPoursuite.py desRacine.py desSelectVal.py \
	desUniqueASSD.py desUniqueBase.py desUniqueComp.py desUniqueInto.py desUniqueSDCOInto.py \
	desUniqueSDCO.py desVisu.py  aideQT.py OptionsEditeur.py OptionsPdf.py myMain.py \
	desViewTexte.py desPixmap.py desMatrice.py OptionsOT.py OptionsCuve.py desChoixMap.py \
        OptionsMAP.py desImage.py desChoixCode.py desRecherche.py desUniqueBool.py\
        desRacineOnglet.py desBoutonSalome.py

QM_FILES=eficas_en.qm 

%.py:%.ui
	${PYUIC} -x -o $@ $<

%.qm:%.ts
	${QTRELEASE}  -qm $@ $<

all : $(PY_FILES) $(QM_FILES)
clean :
	-rm -rf $(PY_FILES) *.pyc

