"""
   Ce module sert a afficher le texte du FAQ EFICAS
   et à attendre l'acquittement par l'utilisateur
"""
# Modules Python
import os
import Pmw
from Tkinter import END

# Modules Eficas
import prefs
import fontes

class FAQ:
   def __init__(self,parent):
      self.parent=parent
      self.Dialog = Pmw.Dialog(parent,
                               buttons=('Lu',),
                               title="FAQs et limitations d'EFICAS",
                               command = self.lu_FAQ)
      txt = open(os.path.join(prefs.INSTALLDIR,'Editeur','faqs.txt'),'r').read()
      Texte = Pmw.ScrolledText(self.Dialog.interior(),
                               text_font=fontes.standard)
      Texte.insert(END,txt)
      Texte.pack(expand=1,fill='both')
      self.Dialog.activate(geometry = 'centerscreenalways')

   def lu_FAQ(self,event=None):
      self.Dialog.destroy()

def affiche(parent):
   FAQ(parent)
