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

