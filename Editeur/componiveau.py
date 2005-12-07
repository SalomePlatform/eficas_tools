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

from Tkinter import *
import Pmw

import Objecttreeitem
import panels
import fontes
from Extensions import commentaire 

Fonte_Niveau = fontes.canvas_gras_italique
Fonte_Niveau_inactif = fontes.canvas_italique

class NIVEAUPanel(panels.OngletPanel):
    def init(self):
        """ Initialise les frame des panneaux contextuels relatifs à un JDC """
        panneau=Pmw.PanedWidget(self,orient='horizontal')
        panneau.add('left',min=0.4,max=0.6,size=0.5)
        panneau.add('right',min=0.4,max=0.6,size=0.5)
        panneau.pack(expand=1,fill='both')
        self.bouton_com.pack_forget()
        self.makeJDCPage(panneau.pane('left'))
	self.enlevebind()


import treewidget
class Node(treewidget.Node):pass


class NIVEAUTreeItem(Objecttreeitem.ObjectTreeItem):
  panel = NIVEAUPanel
  itemNode=Node

  def isactif(self):
      return self.object.isactif()
    
  def IsExpandable(self):
      return 1
    
  def GetLabelText(self):
      """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
      """
      if self.isactif():
          fonte = Fonte_Niveau
      else :
          fonte = Fonte_Niveau_inactif
      return self.labeltext,fonte,'#00008b'
    
  def GetIconName(self):
      if self.isactif():
          if self.object.isvalid():
              return "ast-green-text"
          else:
              return "ast-red-text"
      else:
          return "ast-white-text"
  
  def keys(self):
      if self.object.etapes_niveaux != []:
          return range(len(self.object.etapes_niveaux))
      else:
          return range(len(self.object.etapes))

  def GetSubList(self):
    sublist=[]
    for key in self.keys():
      if self.object.etapes_niveaux != []:
          liste = self.object.etapes_niveaux
      else:
          liste = self.object.etapes
      try:
        value = liste[key]
      except KeyError:
        continue
      def setfunction(value, key=key, object=liste):
        object[key] = value
      item =self.make_objecttreeitem(self.appli,value.ident() + " : ", value, setfunction)
      sublist.append(item)
    return sublist

  def additem(self,name,pos):
      if isinstance(name,Objecttreeitem.TreeItem) :
          cmd=self.object.addentite(name.getObject(),pos)
      else :
          cmd = self.object.addentite(name,pos)
      item = self.make_objecttreeitem(self.appli,cmd.nom + " : ", cmd)
      return item

  def suppitem(self,item) :
    # item = item de l'ETAPE à supprimer du JDC
    # item.getObject() = ETAPE ou COMMENTAIRE
    # self.object = JDC
    itemobject=item.getObject()
    if self.object.suppentite(itemobject):
       if isinstance(item.object,commentaire.COMMENTAIRE):
          message = "Commentaire supprimé"
       else :
          message = "Commande " + itemobject.nom + " supprimée"
       self.appli.affiche_infos(message)
       return 1
    else:
       self.appli.affiche_infos("Pb interne : impossible de supprimer cet objet")
       return 0

  def GetText(self):
      return ''

    
import Accas
treeitem = NIVEAUTreeItem
objet = Accas.ETAPE_NIVEAU    
