"""
"""
# Modules Python
import Tkinter

class STATUSBAR:
   def __init__(self,parent):
      self.parent=parent
      self.frame = Tkinter.Frame(parent,bd=1, relief=Tkinter.RAISED)
      self.frame.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
      self.label = Tkinter.Label (self.frame,
                                        fg='black',
                                        text='',
                                        justify='left',
                                        relief='sunken',
                                        bg='gray95')
      self.label.pack(side='left',expand=1,fill='both')

   def affiche_infos(self,texte):
      if len(texte)>150 :
          texte_infos=texte[0:150]
      else :
          texte_infos=texte
      self.label.configure(text=texte_infos)


   def reset_affichage_infos(self):
      """ Efface tout message présent dans le panneau en bas d'EFICAS """
      self.affiche_infos('')

