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
import Pmw
import Objecttreeitem
import panels

class FACTPanel(panels.OngletPanel) :
  def init(self) :
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    nb.pack(fill = 'both', expand = 1) 
    self.nb=nb
    nb.add('Mocles', tab_text='Ajouter mots-clés')
    #nb.add('Commentaire',tab_text='Insérer commentaire')
    panneau=Pmw.PanedWidget(nb.page("Mocles"),
                            orient='horizontal')
    panneau.add('left',min=0.4,max=0.6,size=0.5)
    panneau.add('right',min=0.4,max=0.6,size=0.5)
    panneau.pack(expand=1,fill='both')
    self.makeMoclesPage(panneau.pane('left'))
    self.makeReglesPage(panneau.pane('right'))
    #self.makeCommentairePage(nb.page("Commentaire"))
    nb.tab('Mocles').focus_set()
    nb.setnaturalsize()
    self.affiche()


class FACTTreeItem(Objecttreeitem.ObjectTreeItem):
  panel = FACTPanel
  
  def IsExpandable(self):
    return 1

  def GetText(self):
      return  ''

  def GetLabelText(self):
      """ Retourne 3 valeurs :
        - le texte à afficher dans le noeud représentant l'item
        - la fonte dans laquelle afficher ce texte
        - la couleur du texte
      """
      # None --> fonte et couleur par défaut
      return self.object.getlabeltext(),None,None

  def isvalid(self):
    return self.object.isvalid()

  def iscopiable(self):
    return 1

  def isMCFact(self):
      """
      Retourne 1 si l'objet pointé par self est un MCFact, 0 sinon
      """
      return 1
    
  def GetIconName(self):
    if self.object.isvalid():
      return "ast-green-los"
    elif self.object.isoblig():
      return "ast-red-los"
    else:
      return "ast-yel-los"

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

  def additem(self,name,pos):
    if isinstance(name,Objecttreeitem.ObjectTreeItem) :
        objet = self.object.addentite(name.object,pos)
    else :
        objet = self.object.addentite(name,pos)
    self.expandable = 1
    if objet == 0 :
        # on ne peut ajouter l'élément de nom name
        return 0
    def setfunction(value, object=objet):
      object.setval(value)
    item = self.make_objecttreeitem(self.appli,objet.nom + " : ", objet, setfunction)
    return item

  def suppitem(self,item) :
      """ 
         Cette methode a pour fonction de supprimer l'item passé en argument
         des fils de l'item FACT qui est son pere
           - item = item du MOCLE à supprimer du MOCLE père
           - item.object = MCSIMP ou MCBLOC 
      """
      if item.object.isoblig() :
          self.appli.affiche_infos('Impossible de supprimer un mot-clé obligatoire ')
          return 0
      else :
          self.object.suppentite(item.object)
          message = "Mot-clé " + item.object.nom + " supprimé"
          self.appli.affiche_infos(message)
          return 1

  def verif_condition_bloc(self):
      return self.object.verif_condition_bloc()

import Accas
objet = Accas.MCFACT
treeitem = FACTTreeItem
