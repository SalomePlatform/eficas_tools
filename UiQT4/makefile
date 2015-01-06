PYUIC = pyuic4
QTRELEASE = lrelease-qt4
.PHONY : all
.SUFFIXES : .ui .py .ts .qm


PY_FILES = desSelectVal.py desViewTexte.py  desChoixCommandes.py desWidgetCommande.py \
        desWidgetSimpBase.py desWidget4a6RadioButton.py desWidgetRadioButton.py  desWidgetBloc.py \
        desWidgetCB.py desWidgetPlusieursBase.py desWidgetFact.py desWidgetFactPlie.py \
        desWidgetSimpBool.py desWidgetComplexe.py desWidgetSimpTuple.py myMain.py \
        desChoixCata.py desWidgetPlusieursInto.py desBaseWidget.py desWidgetOptionnel.py \
        desWidgetSimpFichier.py desWidgetSimpTxt.py desRecherche.py

QM_FILES=eficas_en.qm 

%.py:%.ui
	${PYUIC} -x -o $@ $<

%.qm:%.ts
	${QTRELEASE}  -qm $@ $<

all : $(PY_FILES) $(QM_FILES)
clean :
	-rm -rf $(PY_FILES) *.pyc

