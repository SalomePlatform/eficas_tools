PYUIC = pyuic4
QTRELEASE = lrelease-qt4
.PHONY : all
.SUFFIXES : .ui .py .ts .qm


PY_FILES = desSelectVal.py desViewTexte.py  desChoixCommandes.py desWidgetCommande.py \
        desWidgetSimpBase.py desWidget4a6RadioButton.py desWidgetRadioButton.py  desWidgetBloc.py \
        desWidgetCB.py desWidgetPlusieursBase.py desWidgetFact.py desWidgetFactPlie.py \
        desWidgetSimpBool.py desWidgetSimpComplexe.py  myMain.py \
        desChoixCata.py desWidgetPlusieursInto.py desWidgetPlusieursIntoOrdonne.py desBaseWidget.py desWidgetOptionnel.py \
        desWidgetSimpFichier.py desWidgetSimpTxt.py desRecherche.py desWidgetCommentaire.py\
	desWidgetTuple2.py desWidgetTuple3.py desWidgetParam.py desWidgetHeure.py desWidgetDate.py\
        desWidgetVide.py desWidgetInformation.py desVisu.py

QM_FILES=eficas_en.qm 

%.py:%.ui
	${PYUIC} -x -o $@ $<

%.qm:%.ts
	${QTRELEASE}  -qm $@ $<

all : $(PY_FILES) $(QM_FILES)
clean :
	-rm -rf $(PY_FILES) *.pyc

