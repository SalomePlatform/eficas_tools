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
import Pmw
import Objecttreeitem
import panels

from widgets import ListeChoix

class JDCPanel(panels.OngletPanel):
  def init(self):
      """ Initialise les frame des panneaux contextuels relatifs � un JDC """
      panneau=Pmw.PanedWidget(self,orient='horizontal')
      panneau.add('left',min=0.4,max=0.6,size=0.5)
      panneau.add('right',min=0.4,max=0.6,size=0.5)
      panneau.pack(expand=1,fill='both')
      self.bouton_com.pack_forget()
      self.makeJDCPage(panneau.pane('left'))
      self.makeReglesPage(panneau.pane('right'))
    
  def makeReglesPage(self,page) :
    regles = []
    regles = self.node.item.get_regles()
    texte_regles = []
    l_regles_en_defaut=[]
    if len(regles) > 0:
      l_noms_etapes = self.node.item.get_l_noms_etapes()
      i = 0
      for regle in regles :
        texte_regles.append(regle.gettext())
        texte,test = regle.verif(l_noms_etapes)
        if test == 0 : l_regles_en_defaut.append(i)
        i = i+1
    Liste = ListeChoix(self,page,texte_regles,liste_marques=l_regles_en_defaut,active='non',titre="R�gles")
    Liste.affiche_liste()
    # aide associ�e au panneau
    bulle_aide="""Ce panneau contient la liste des r�gles qui s'appliquent � l'objet
    en cours d'�dition.
    - en noir : r�gles valides
    - en rouge : r�gles viol�es"""
    Liste.MCbox.bind("<Button-3>", lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
    Liste.MCbox.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

import treewidget
class Node(treewidget.Node):
    def doPaste_Commande(self,objet_a_copier):
        """
          R�alise la copie de l'objet pass� en argument qui est n�cessairement
          une commande
        """
        #child = self.item.append_child(objet_a_copier,pos='first')
        child = self.append_child(objet_a_copier,pos='first',retour='oui')
        #if child is None : return 0
        return child


class JDCTreeItem(Objecttreeitem.ObjectTreeItem):
  panel = JDCPanel
  itemNode=Node
  
  def IsExpandable(self):
    return 1

  def GetText(self):
      return  "    "

  def GetLabelText(self):
      # None --> fonte et couleur par d�faut
      return self.object.nom,None,None

  def get_jdc(self):
    """
    Retourne l'objet point� par self
    """
    return self.object
  
  def GetIconName(self):
    if self.object.isvalid():
      return "ast-green-square"
    else:
      return "ast-red-square"

  def keys(self):
      if self.object.etapes_niveaux != []:
          return range(len(self.object.etapes_niveaux))
      else:
          return range(len(self.object.etapes))

  def additem(self,name,pos):
      cmd = self._object.addentite(name,pos)
      return cmd

  def suppitem(self,item) :
    # item = item de l'ETAPE � supprimer du JDC
    # item.getObject() = ETAPE ou COMMENTAIRE
    # self.object = JDC
    itemobject=item.getObject()
    if self.object.suppentite(itemobject):
       if itemobject.nature == "COMMENTAIRE" :
          message = "Commentaire supprim�"
       else :
          message = "Commande " + itemobject.nom + " supprim�e"
       self.appli.affiche_infos(message)
       return 1
    else:
       self.appli.affiche_infos("Pb interne : impossible de supprimer cet objet")
       return 0

  def GetSubList(self):
    """
       Retourne la liste des items fils de l'item jdc.
       Cette liste est conservee et mise a jour a chaque appel
    """
    if self.object.etapes_niveaux != []:
        liste = self.object.etapes_niveaux
    else:
        liste = self.object.etapes
    sublist=[None]*len(liste)
    # suppression des items lies aux objets disparus
    for item in self.sublist:
       old_obj=item.getObject()
       if old_obj in liste:
          pos=liste.index(old_obj)
          sublist[pos]=item
       else:
          pass # objets supprimes ignores
    # ajout des items lies aux nouveaux objets
    pos=0
    for obj in liste:
       if sublist[pos] is None:
          # nouvel objet : on cree un nouvel item
          item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj)
          sublist[pos]=item
       pos=pos+1

    self.sublist=sublist
    return self.sublist

  def get_l_noms_etapes(self):
      """ Retourne la liste des noms des �tapes de self.object"""
      return self.object.get_l_noms_etapes()

  def get_liste_cmd(self):
      #print "get_liste_cmd",self.object.niveau.definition
      listeCmd = self.object.niveau.definition.get_liste_cmd()
      return listeCmd

import Accas
treeitem =JDCTreeItem
objet = Accas.JDC    
