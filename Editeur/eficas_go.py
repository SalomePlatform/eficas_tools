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
    un ecran Splash pour faire patentier l'utilisateur
"""
# Modules Python
import Tkinter

# Modules Eficas
import import_code
import splash

def lance_eficas(code,fichier=None):
    """
        Lance l'appli EFICAS
    """

    root = Tkinter.Tk()
    splash.init_splash(root,code=code,titre="Lancement d'EFICAS pour %s" %code)
    splash._splash.configure(text="Chargement d'EFICAS en cours.\n Veuillez patienter ...")
    import eficas
    if fichier :
        eficas.EFICAS(root,code=code,fichier = fichier)
    else:
        eficas.EFICAS(root,code=code)

    root.mainloop()

