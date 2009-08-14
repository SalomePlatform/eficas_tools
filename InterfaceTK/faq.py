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
   Ce module sert a afficher le texte du FAQ EFICAS
   et à attendre l'acquittement par l'utilisateur
"""
# Modules Python
import os
import Pmw
from Tkinter import END

# Modules Eficas
import prefs
name='prefs_'+prefs.code
prefsCode=__import__(name)
import fontes

class FAQ:
   def __init__(self,parent):
      self.parent=parent
      self.Dialog = Pmw.Dialog(parent,
                               buttons=('Lu',),
                               title="FAQs et limitations d'EFICAS",
                               command = self.lu_FAQ)
      txt = open(os.path.join(prefsCode.INSTALLDIR,'Editeur','faqs.txt'),'r').read()
      Texte = Pmw.ScrolledText(self.Dialog.interior(),
                               text_font=fontes.standard)
      Texte.insert(END,txt)
      Texte.pack(expand=1,fill='both')
      self.Dialog.activate(geometry = 'centerscreenalways')

   def lu_FAQ(self,event=None):
      self.Dialog.destroy()

def affiche(parent):
   FAQ(parent)
