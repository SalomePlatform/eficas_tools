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
   Ce module contient la fonction utilitaire centerwindow
   qui sert à centrer une fenetre
"""
import types

def centerwindow(window,parent = 'avec'):
    if parent =='avec':
        parent = window.winfo_parent()
        if type(parent) == types.StringType:
            parent = window._nametowidget(parent)
    # Find size of window.
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    if width == 1 and height == 1:
        # If the window has not yet been displayed, its size is
        # reported as 1x1, so use requested size.
        width = window.winfo_reqwidth()
        height = window.winfo_reqheight()
    # Place in centre of screen:
    if parent =='avec' :
        x = (window.winfo_screenwidth() - width) / 2 - parent.winfo_vrootx()
        y = (window.winfo_screenheight() - height) / 3 - parent.winfo_vrooty()
    else:
        x = (window.winfo_screenwidth() - width) / 2 
        y = (window.winfo_screenheight() - height) / 3
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    window.geometry('+%d+%d' % (x, y))
    
