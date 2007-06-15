EFICAS=..

api:
	(export PYTHONPATH=$(EFICAS):$(EFICAS)/Aster;\
           epydoc -n EFICAS  --show-imports -o api_eficas -u http://eficas.der.edf.fr \
                     $(EFICAS)/Noyau/ \
                     $(EFICAS)/Validation/ \
                     $(EFICAS)/Ihm/ \
                     $(EFICAS)/Extensions/ \
                     $(EFICAS)/Accas/ \
                     $(EFICAS)/Editeur/ \
                     $(EFICAS)/generator/ \
                     $(EFICAS)/convert/*.py $(EFICAS)/convert/Parserv5/__init__.py $(EFICAS)/convert/Parserv5/conv.py \
                     $(EFICAS)/AIDE/__init__.py $(EFICAS)/AIDE/aide_gui.py $(EFICAS)/AIDE/aide_objets.py $(EFICAS)/AIDE/viewer.py \
                     $(EFICAS)/Exemples/ \
                            )
pdf:
	(export PYTHONPATH=$(EFICAS):$(EFICAS)/Aster;\
           epydoc -n EFICAS  --show-imports --pdf -o api_pdf -u http://eficas.der.edf.fr \
                     $(EFICAS)/Noyau/ \
                     $(EFICAS)/Validation/ \
                     $(EFICAS)/Ihm/ \
                     $(EFICAS)/Extensions/ \
                     $(EFICAS)/Accas/ \
                     $(EFICAS)/Editeur/ \
                     $(EFICAS)/generator/ \
                     $(EFICAS)/convert/*.py $(EFICAS)/convert/Parserv5/__init__.py $(EFICAS)/convert/Parserv5/conv.py \
                     $(EFICAS)/AIDE/__init__.py $(EFICAS)/AIDE/aide_gui.py $(EFICAS)/AIDE/aide_objets.py $(EFICAS)/AIDE/viewer.py \
                            )


debug:                       # options -v --debug pour debugger
	(export PYTHONPATH=$(EFICAS)/Aster;\
           epydoc -n EFICAS  --show-imports -v --debug -o api_debug -u http://eficas.der.edf.fr \
                     $(EFICAS)/Editeur/ \
                            )

