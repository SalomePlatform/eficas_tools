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
"""
    Ce module permet de lancer l'application EFICAS en affichant
    un ecran Splash pour faire patienter l'utilisateur
"""
# Modules Python
import sys
import Tkinter

# Modules Eficas
import prefs
if hasattr(prefs,'encoding'):
   # Hack pour changer le codage par defaut des strings
   import sys
   reload(sys)
   sys.setdefaultencoding(prefs.encoding)
   del sys.setdefaultencoding
   # Fin hack

import styles
from Editeur import import_code
import splash
from Editeur import session

def lance_eficas(code=None,fichier=None):
    """
        Lance l'appli EFICAS
    """
    # Analyse des arguments de la ligne de commande
    if code !=None : prefs.code=code
    if code !=None  :
    	sys.argv.append("-k")
    	sys.argv.append(code)
    options=session.parse(sys.argv)
    code=options.code

    root = Tkinter.Tk()
    splash.init_splash(root,code=code,titre="Lancement d'EFICAS pour %s" %code)
    splash._splash.configure(text="Chargement d'EFICAS en cours.\n Veuillez patienter ...")
    import eficas
    eficas.EFICAS(root,code=code,ihm="TK")

    root.mainloop()

