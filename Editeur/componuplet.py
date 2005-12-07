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
import types
import Tkinter
import Pmw
from repr import Repr
from copy import copy,deepcopy

# Modules Eficas
import Objecttreeitem
import panels

#
__version__="$Name:  $"
__Id__="$Id: componuplet.py,v 1.8 2005/11/03 09:03:48 eficas Exp $"
#

myrepr = Repr()
myrepr.maxstring = 100
myrepr.maxother = 100

# Si Expandable vaut 1 les éléments du nuplet apparaissent dans l'arbre
# Si Expandable vaut 0 les éléments n'apparaissent pas
Expandable=1

class NUPLETPanel(panels.OngletPanel):
  def init(self):
      """ Initialise les frame des panneaux contextuels relatifs \340 un NUPLET """
      self.nb=Pmw.NoteBook(self,raisecommand=self.raisecmd)
      self.nb.pack(fill = 'both', expand = 1)
      self.nb.add("Valeurs",tab_text="Saisir valeurs")
      self.makeValeurPage(self.nb.page('Valeurs'))
      self.enlevebind()
      self.creebind()
      self.nb.setnaturalsize()
    
  def makeValeurPage(self,page):
    label = Tkinter.Label(page,text='Valeurs :').pack(side=Tkinter.LEFT)
    i=0
    for obj in self.node.item.object.mc_liste:
      frame_valeur=Tkinter.Frame(page)
      frame_valeur.pack(side=Tkinter.LEFT)
      if hasattr(obj,'definition'):
         objet_mc=obj.definition
      else:  
         objet_mc=None
      valeur=obj.valeur
      if type(valeur) == types.InstanceType :
        valeur=obj.getval()
      aide=self.gen_aide(obj)
      if objet_mc.into != None :
        l_choix=list(objet_mc.into)
        #obj.set_valeur(l_choix[0],evaluation='non')
        obj.set_valeur(l_choix[0])
        option=Pmw.OptionMenu (frame_valeur,
                items = l_choix,
                menubutton_width = 10,
                command = lambda e,obj=obj,s=self:s.record_valeur(val=e,obj=obj),
        )
        option.pack(side=Tkinter.LEFT,padx=1)
      else :
        entry = Tkinter.Entry(frame_valeur,relief='sunken',width=10)
        entry.pack(side=Tkinter.LEFT,padx=1)
        entry.bind("<Return>",
                lambda e,obj=obj,s=self:s.valid_valeur(e,obj=obj))
        entry.bind("<KP_Enter>",
                lambda e,obj=obj,s=self:s.valid_valeur(e,obj=obj))
        if i==0:entry.focus_set()
        #aide = Tkinter.Label(frame_valeur, text = aide)
        #aide.place(relx=0.5,rely=0.55,anchor='n')
        if valeur != None :
          entry.delete(0,Tkinter.END)
          entry.insert(0,obj.getval())
      i=i+1

  def record_valeur(self,val=None,obj=None,mess='Valeur du mot-cl\351 enregistr\351e'):
    """ 
      Enregistre  val comme valeur de self.node.item.object SANS faire de 
      test de validité
    """
    #obj.set_valeur(val,evaluation='non')
    obj.set_valeur(val)
    self.parent.appli.affiche_infos(mess)
    #self.node.parent.verif()
    #self.node.update()

  def valid_valeur(self,e,obj=None,mess='Valeur du mot-cl\351 enregistr\351e'):
    """ 
      Enregistre  val comme valeur de self.node.item.object avec
      test de validité
    """
    valeur=e.widget.get()
    e.widget.delete(0,Tkinter.END)
    anc_val=obj.getval()
    if anc_val == None:anc_val=''
    test=obj.set_valeur(valeur)
    if test:
      if obj.isvalid():
          self.parent.appli.affiche_infos('Valeur du mot-cl\351 enregistr\351e')
          e.widget.insert(0,obj.getval())
      else:
          #obj.set_valeur(anc_val,evaluation='non')
          obj.set_valeur(anc_val)
          self.parent.appli.affiche_infos("valeur du mot-cl\351 non autoris\351e")
          e.widget.insert(0,anc_val)
    else:
      print "impossible d'\351valuer : %s " %valeur
      print "test =",test
      self.parent.appli.affiche_infos("valeur du mot-cl\351 non autoris\351e")
      e.widget.delete(0,Tkinter.END)
      e.widget.insert(0,anc_val)
          
    #self.node.parent.verif()
    #self.node.update()

  def gen_aide(self,obj):
    return ""
    

class NUPLETTreeItem(Objecttreeitem.ObjectTreeItem):
  panel=NUPLETPanel

  def IsExpandable(self):
    return Expandable

  def GetText(self):
      return  ''

  def isvalid(self):
    return self.object.isvalid()

  def GetIconName(self):
    if self.object.isvalid():
      return "ast-green-los"
    elif self.object.isoblig():
      return "ast-red-los"
    else:
      return "ast-yel-los"

  def GetSubList(self):
    if not Expandable:return []
    sublist=[]
    for obj in self.object.mc_liste:
      item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj, None)    
      sublist.append(item)
    return sublist

  def additem(self,name,pos):
    raise "NUPLET"

  def suppitem(self,item) :
    raise "NUPLET"

import Accas
treeitem=NUPLETTreeItem
objet=Accas.MCNUPLET
