#@ MODIF componiveau Editeur  DATE 02/07/2001   AUTEUR D6BHHJP J.P.LEFEBVRE 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2001  EDF R&D                  WWW.CODE-ASTER.ORG
#              SEE THE FILE "LICENSE.TERMS" FOR INFORMATION ON USAGE AND
#              REDISTRIBUTION OF THIS FILE.
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

class NIVEAUTreeItem(Objecttreeitem.ObjectTreeItem):
  panel = NIVEAUPanel

  def isactif(self):
      return self.object.isactif()
    
  def IsExpandable_old(self):
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
  
  def keys_old(self):
    return range(len(self.object.etapes))

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
          cmd=self.object.addentite(name.object,pos)
      else :
          cmd = self.object.addentite(name,pos)
      item = self.make_objecttreeitem(self.appli,cmd.nom + " : ", cmd)
      return item

  def suppitem(self,item) :
    # item = item de l'ETAPE à supprimer du JDC
    # item.object = ETAPE ou COMMENTAIRE
    # self.object = JDC
    self.object.suppentite(item.object)
    if isinstance(item.object,commentaire.COMMENTAIRE):
        message = "Commentaire supprimé"
        self.appli.affiche_infos(message)
    else :
        message = "Commande " + item.object.nom + " supprimée"
        self.appli.affiche_infos(message)
    return 1

  def GetText(self):
      return ''

    
import Accas
treeitem = NIVEAUTreeItem
objet = Accas.ETAPE_NIVEAU    
