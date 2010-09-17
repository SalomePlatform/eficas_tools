# -*- coding: utf-8 -*-
import os
import aide_objets
import aide_gui
import viewer

def go(fichier=None,master=None):
    if not fichier :
       fichier=os.path.join(os.path.dirname(__file__),"../Aide/fichiers_ASTER","index.html")
       print fichier
    o=viewer.HTMLViewer(master)
    o.display(fichier)
    return o

def go2(fichier=None,master=None):
    if not fichier :
       fichier=os.path.join(os.path.dirname(__file__),"index_aide.py")
    index = aide_objets.INDEX(fichier)
    index.build()
    o = aide_gui.AIDE_GUI(index,master=master)
    o.build()
    return o

def go3(fichier=None,parent=None):
    if not fichier :
       pathDoc=os.path.join(os.path.dirname(__file__),"fichiers")
    viewer.HTMLQTViewer(parent,pathDoc)

