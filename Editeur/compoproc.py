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
import compooper

class PROCPanel(panels.OngletPanel):
  def init(self):
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    nb.pack(fill = 'both', expand = 1)
    self.nb=nb
    nb.add('Mocles', tab_text='Ajouter mots-clés')
    nb.add('Commande', tab_text='Nouvelle Commande')
    nb.add('Commentaire',tab_text='Paramètre/Commentaire')
    panneau=Pmw.PanedWidget(nb.page("Mocles"),
                            orient='horizontal')
    panneau.add('left',min=0.4,max=0.6,size=0.5)
    panneau.add('right',min=0.4,max=0.6,size=0.5)
    panneau.pack(expand=1,fill='both')
    self.makeCommandePage(nb.page("Commande"))
    self.makeMoclesPage(panneau.pane('left'))
    self.makeReglesPage(panneau.pane('right'))
    self.makeParamCommentPage_for_etape(nb.page("Commentaire"))
    nb.setnaturalsize()
    self.affiche()

class ProcEtapeTreeItem(compooper.EtapeTreeItem):
  panel = PROCPanel
  
  def IsExpandable(self):
    return 1

  def GetIconName(self):
      """
      Retourne le nom de l'icône à afficher dans l'arbre
      Ce nom dépend de la validité de l'objet
      """
      if self.object.isactif():
        if self.object.isvalid():
          return "ast-green-square"
        else:
          return "ast-red-square"
      else:
        return "ast-white-square"

  def GetLabelText(self):
      """ Retourne 3 valeurs :
      - le texte à afficher dans le noeud représentant l'item
      - la fonte dans laquelle afficher ce texte
      - la couleur du texte
      """
      if self.object.isactif():
        # None --> fonte et couleur par défaut
        return self.labeltext,None,None
      else:
        return self.labeltext,fontes.standard_italique,None
      
  def get_objet(self,name) :
      for v in self.object.mc_liste:
          if v.nom == name : return v
      return None
      
  def additem(self,name,pos):
      if isinstance(name,Objecttreeitem.ObjectTreeItem) :
          mcent = self.object.addentite(name.object,pos)
      else :
          mcent = self.object.addentite(name,pos)
      self.expandable=1
      if mcent == 0 :
          # on ne peut ajouter l'élément de nom name
          return 0
      def setfunction(value, object=mcent):
          object.setval(value)
      item = self.make_objecttreeitem(self.appli,mcent.nom + " : ", mcent, setfunction)
      return item

  def suppitem(self,item) :
    # item : item du MOCLE de l'ETAPE à supprimer
    # item.object = MCSIMP, MCFACT, MCBLOC ou MCList 
    if item.object.isoblig() :
        self.appli.affiche_infos('Impossible de supprimer un mot-clé obligatoire ')
        return 0
    else :
        self.object.suppentite(item.object)
        message = "Mot-clé " + item.object.nom + " supprimé"
        self.appli.affiche_infos(message)
        return 1

  def GetText(self):
      try:
          #return  myrepr.repr(self.object.get_sdname())
          return self.object.get_sdname()
      except:
          return ''

  def keys(self):
    keys=self.object.mc_dict.keys()
    return keys

  def GetSubList(self):
    sublist=[]
    for obj in self.object.mc_liste:
      def setfunction(value, object=obj):
        object.setval(value)
      item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj, setfunction)
      sublist.append(item)
    return sublist

  def isvalid(self):
    return self.object.isvalid()

  def iscopiable(self):
    return 1

  def isCommande(self):
      """
      Retourne 1 si l'objet pointé par self est une Commande, 0 sinon
      """
      return 1
  
  def verif_condition_bloc(self):
    return self.object.verif_condition_bloc()

  def get_noms_sd_oper_reentrant(self):
      return self.object.get_noms_sd_oper_reentrant()        

import Accas
treeitem = ProcEtapeTreeItem
objet = Accas.PROC_ETAPE    

