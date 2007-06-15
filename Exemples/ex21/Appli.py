# -*- coding: utf-8 -*-
import Tkinter
import Pmw
from Editeur import comploader

class CONFIG:
   isdeveloppeur='NON'

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

   def showtext(self,texte):
      if len(texte)>150 :
          texte_infos=texte[0:150]
      else :
          texte_infos=texte
      self.label.configure(text=texte_infos)

class Appli:
   def __init__(self):
      self.CONFIGURATION=CONFIG()
      self.root=Tkinter.Tk()
      Pmw.initialise(self.root)
      comploader.charger_composants()
      self.init()

   def init(self):
      self.dict_reels={}
      self.statusbar=STATUSBAR(self.root)

   def affiche_infos(self,message):
      self.statusbar.showtext(message)
      #print message
      return

   def efface_aide(self,event):
      return

   def affiche_aide(self,event,aide):
      #print aide
      return

