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

