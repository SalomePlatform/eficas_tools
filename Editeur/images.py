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
    Ce module joue le role de cache pour les images stockées
    dans le repertoire ICONDIR
"""

import os
import Tkinter

if __name__ == '__main__':
   # Programme de test
   import sys
   import images
   root=Tkinter.Tk()
   frame = Tkinter.Frame(root)
   frame.pack(expand=1,fill='both')

   for name in ('About24','Save24'):
      Tkinter.Label(frame, image=images.get_image(name)).pack(side=Tkinter.TOP)

   root.mainloop()
   sys.exit()

try:
   import prefs
   ICONDIR=prefs.ICONDIR
except:
   # Par defaut on utilise le repertoire local icons
   ICONDIR=os.path.join(os.path.abspath(os.path.dirname(__file__)),'icons')

dico_images={}

def get_image(name):
    if dico_images.has_key(name):
        return dico_images[name]
    else : 
        fic_image = os.path.join(ICONDIR,name)
        if not os.path.isfile(fic_image):
           file, ext = os.path.splitext(fic_image)
           fic_image = file + '.gif'
        image = Tkinter.PhotoImage(file=fic_image)
        dico_images[name]=image
        return image

def update_cache():
   global dico_images
   dico_images={}

