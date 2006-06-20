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
# Modules Python
from Tkinter import Label,Button

#Modules Eficas
from Noyau.N_OBJECT import ErrorObj
import Objecttreeitem
import panels

class ERRORPanel(panels.Panel_Inactif):
    def creer_texte(self):
        texte = """Le noeud sélectionné correspond à un objet erroné """
        label = Label(self,text=texte,justify='center')
        label.place(relx=0.5,rely=0.4,relwidth=0.8,anchor='center')
        bouton = Button(self,text = "Supprimer", command=self.supprimer)
        bouton.place(relx=0.5,rely=0.5,anchor='center')

class ERRORTreeItem(Objecttreeitem.AtomicObjectTreeItem):
    panel = ERRORPanel
    def GetIconName(self):
        return "ast-red-ball"


treeitem =ERRORTreeItem
objet = ErrorObj

