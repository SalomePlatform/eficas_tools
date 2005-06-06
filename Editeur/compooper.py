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
import traceback
import Objecttreeitem
import panels
import fontes

class OPERPanel(panels.OngletPanel):

  def init(self):
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    nb.pack(fill = 'both', expand = 1)
    self.nb=nb
    nb.add('Mocles', tab_text='Nouveau mot-clé')
    nb.add('Concept', tab_text='Nommer concept')
    nb.add('Commande', tab_text='Nouvelle Commande')
    nb.add('Commentaire',tab_text='Paramètre/Commentaire')
    panneau=Pmw.PanedWidget(nb.page("Mocles"),
                            orient='horizontal')
    panneau.add('left',min=0.4,max=0.6,size=0.5)
    panneau.add('right',min=0.4,max=0.6,size=0.5)
    panneau.pack(expand=1,fill='both')
    self.makeCommandePage(nb.page("Commande"))
    self.makeConceptPage_oper(nb.page("Concept"))
    self.makeMoclesPage(panneau.pane('left'))
    self.makeReglesPage(panneau.pane('right'))
    #self.makeCommentairePage(nb.page("Commentaire"))
    self.makeParamCommentPage_for_etape(nb.page("Commentaire"))
    nb.tab('Mocles').focus_set()
    nb.setnaturalsize()
    self.affiche()

  def makeConceptPage_oper(self,page):
      """ Crée la page de saisie du nom du concept """
      if self.node.item.is_reentrant():
          # commande obligatoirement reentrante
          self.makeConceptPage_reentrant(page)
      else:
          # commande non reentrante ou facultativement reentrante
          self.makeConceptPage(page)

  def makeConceptPage_reentrant(self,page):
      """ Crée la page de saisie du nom de concept pour un opérateur reentrant
      cad propose dans la liste des SD utilisées dans la commande celle(s) dont le
      type est compatible avec celui que retourne l'opérateur """
      liste_noms_sd = self.node.item.get_noms_sd_oper_reentrant()
      self.listbox = Pmw.ScrolledListBox(page,
                                         items=liste_noms_sd,
                                         labelpos='n',
                                         label_text="Structure(s) de données à enrichir par l'opérateur courant :",
                                         listbox_height = 6,
                                         selectioncommand=self.select_valeur_from_list,
                                         dblclickcommand=lambda s=self,c=self.execConcept : s.choose_valeur_from_list(c))
      self.listbox.place(relx=0.5,rely=0.3,relheight=0.4,anchor='center')
      Label(page,text='Structure de donnée choisie :').place(relx=0.05,rely=0.6)
      self.valeur_choisie = StringVar()
      self.label_valeur = Label(page,textvariable=self.valeur_choisie)
      self.label_valeur.place(relx=0.45,rely=0.6)
      if len(liste_noms_sd) == 1 :
          self.valeur_choisie.set(liste_noms_sd[0])

  def select_valeur_from_list(self):
      try:
          choix = self.listbox.getcurselection()[0]
          self.valeur_choisie.set(choix)
      except:
          traceback.print_exc()
	  

  def choose_valeur_from_list(self,command):
      try:
          choix = self.listbox.getcurselection()[0]
          self.valeur_choisie.set(choix)
          apply(command,(),{})
      except:
          traceback.print_exc()

import treewidget
class Node(treewidget.Node):
    def doPaste(self,node_selected):
        """
            Déclenche la copie de l'objet item avec pour cible
            l'objet passé en argument : node_selected
        """
        objet_a_copier = self.item.get_copie_objet()
        child=node_selected.doPaste_Commande(objet_a_copier)
        return child

    def doPaste_Commande(self,objet_a_copier):
        """
          Réalise la copie de l'objet passé en argument qui est nécessairement
          une commande
        """
        parent=self.parent
        #child = parent.item.append_child(objet_a_copier,self.item.getObject())
        child = self.append_brother(objet_a_copier,retour='oui')
        #if child is None:return 0
        return child

    def doPaste_MCF(self,objet_a_copier):
        """
           Réalise la copie de l'objet passé en argument (objet_a_copier)
           Il s'agit forcément d'un mot clé facteur
        """
        child = self.append_child(objet_a_copier,pos='first',retour='oui')
        return child


class EtapeTreeItem(Objecttreeitem.ObjectTreeItem):
  """ La classe EtapeTreeItem est un adaptateur des objets ETAPE du noyau
      Accas. Elle leur permet d'etre affichés comme des noeuds
      d'un arbre graphique.
      Cette classe a entre autres deux attributs importants :
        - _object qui est un pointeur vers l'objet du noyau
        - object qui pointe vers l'objet auquel sont délégués les
          appels de méthode et les accès aux attributs
      Dans le cas d'une ETAPE, _object et object pointent vers le 
      meme objet.
  """
  panel = OPERPanel
  itemNode=Node
  
  def IsExpandable(self):
      return 1

  def GetIconName(self):
      """
      Retourne le nom de l'icône à afficher dans l'arbre
      Ce nom dépend de la validité de l'objet
      """
      if not self.object.isactif():
         return "ast-white-square"
      elif self.object.isvalid():
         return "ast-green-square"
      else:
         return "ast-red-square"

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
      
  def get_type_sd_prod(self):
      """
         Retourne le nom du type du concept résultat de l'étape
      """
      sd_prod=self.object.get_type_produit()
      if sd_prod:
         return sd_prod.__name__
      else:
         return ""

  def additem(self,name,pos):
      #print "compooper.additem",name,pos
      mcent = self._object.addentite(name,pos)
      return mcent

  def suppitem(self,item) :
      # item : item du MOCLE de l'ETAPE à supprimer
      # item.getObject() = MCSIMP, MCFACT, MCBLOC ou MCList 
      itemobject=item.getObject()
      if itemobject.isoblig() :
          self.appli.affiche_infos('Impossible de supprimer un mot-clé obligatoire ')
          return 0
      if self.object.suppentite(itemobject):
          message = "Mot-clé " + itemobject.nom + " supprimé"
          self.appli.affiche_infos(message)
          return 1
      else :
          self.appli.affiche_infos('Pb interne : impossible de supprimer ce mot-clé')
          return 0

  def GetText(self):
      try:
          return self.object.get_sdname()
      except:
          return ''

  def keys(self):
      keys=self.object.mc_dict.keys()
      return keys

  def GetSubList(self):
      """
         Reactualise la liste des items fils stockes dans self.sublist
      """
      if self.isactif():
         liste=self.object.mc_liste
      else:
         liste=[]

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
            def setfunction(value, object=obj):
                object.setval(value)
            item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj, setfunction)
            sublist[pos]=item
         pos=pos+1

      self.sublist=sublist
      return self.sublist

  def GetSubList_BAK(self):
      raise "OBSOLETE"
      if self.isactif():
         liste=self.object.mc_liste
      else:
         liste=[]

      sublist=[]
      isublist=iter(self.sublist)
      iliste=iter(liste)

      while(1):
         old_obj=obj=None
         for item in isublist:
            old_obj=item.getObject()
            if old_obj in liste:break

         for obj in iliste:
            if obj is old_obj:break
            # nouvel objet : on cree un nouvel item
            def setfunction(value, object=obj):
                object.setval(value)
            it = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj, setfunction)
            sublist.append(it)

         if old_obj is None and obj is None:break
         if old_obj is obj:
            sublist.append(item)

      self.sublist=sublist
      return self.sublist

  def isvalid(self):
      return self.object.isvalid()

  def iscopiable(self):
      """
      Retourne 1 si l'objet est copiable, 0 sinon
      """
      return 1

  def update(self,item):
      if item.sd and item.sd.nom:
         self.nomme_sd(item.sd.nom)

  def nomme_sd(self,nom):
      """ Lance la méthode de nommage de la SD """
      oldnom=""
      if self.object.sd != None :
         oldnom=self.object.sd.nom
      test,mess= self.object.nomme_sd(nom)
      if test:self.object.parent.reset_context()
      if (test and self.appli.dict_reels.has_key(oldnom) ):
              self.appli.dict_reels[nom]=self.appli.dict_reels[oldnom]
      return test,mess

  def is_reentrant(self):
      return self.object.is_reentrant()
    
  def get_noms_sd_oper_reentrant(self):
      return self.object.get_noms_sd_oper_reentrant()

  def get_objet_commentarise(self):
      """
          Cette méthode retourne un objet commentarisé
          représentatif de self.object
      """
      import generator,string,Accas
      # Format de fichier utilisé
      format=self.appli.format_fichier.get()
      g=generator.plugins[format]()
      texte_commande = g.gener(self.object,format='beautifie')
      # Il faut enlever la première ligne vide de texte_commande que 
      # rajoute le generator
      rebut,texte_commande = string.split(texte_commande,'\n',1)
      # on construit l'objet COMMANDE_COMM repésentatif de self mais non 
      # enregistré dans le jdc
      commande_comment = Accas.COMMANDE_COMM(texte=texte_commande,reg='non',
                                             parent=self.object.parent)
      commande_comment.niveau = self.object.niveau
      commande_comment.jdc = commande_comment.parent = self.object.jdc

      pos=self.object.parent.etapes.index(self.object)
      self.object.parent.suppentite(self.object)
      self.object.parent.addentite(commande_comment,pos)

      return commande_comment

  def additem_BAK(self,name,pos):
      raise "OBSOLETE"
      mcent=self.addentite(name,pos)

      self.expandable=1
      if mcent == 0 :
          # on ne peut ajouter l'élément de nom name
          return 0
      def setfunction(value, object=mcent):
          object.setval(value)
      item = self.make_objecttreeitem(self.appli,mcent.nom + " : ", mcent, setfunction)
      return item

  def GetSubList_BAK(self):
      raise "OBSOLETE"
      sublist=[]
      for obj in self.object.mc_liste:
        def setfunction(value, object=obj):
          object.setval(value)
        item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj, setfunction)
        sublist.append(item)
      return sublist

  def verif_condition_bloc_BAK(self):
      raise "OBSOLETE"
      return self.object.verif_condition_bloc()

  def replace_child_BAK(self,old_item,new_item):
     """
     Remplace old_item.getObject() par new_item.getObject() dans 
     les fils de self.object
     """
     raise "OBSOLETE"
     old_itemobject=old_item.getObject()
     index = self.object.mc_liste.index(old_itemobject)
     self.object.init_modif()
     self.object.mc_liste.remove(old_itemobject)
     self.object.mc_liste.insert(index,new_item.getObject())
     self.object.fin_modif()
     
import Accas
treeitem = EtapeTreeItem
objet = Accas.ETAPE    

