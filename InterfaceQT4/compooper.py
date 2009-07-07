# -*- coding: utf-8 -*-
import traceback
import string
from PyQt4 import *
from PyQt4.QtGui  import *
from PyQt4.QtCore import *


from Editeur     import Objecttreeitem
import browser
import typeNode

class Node(browser.JDCNode, typeNode.PopUpMenuNode):
    def getPanel( self ):
        """
        """
        from monCommandePanel import MonCommandePanel
        return MonCommandePanel(self,parent=self.editor)

    def createPopUpMenu(self):
        typeNode.PopUpMenuNode.createPopUpMenu(self)
        if ("AFFE_CARA_ELEM" in self.item.get_genealogie()) and self.editor.salome: 
           self.menu.insertItem( 'View3D', self.view3D )
        if  self.item.get_nom() == "DISTRIBUTION" :
           self.Graphe = QAction('Graphique',self.tree)
           self.tree.connect(self.Graphe,SIGNAL("activated()"),self.viewPng)
           self.Graphe.setStatusTip("affiche la distribution ")
           self.menu.addAction(self.Graphe)
           if self.item.isvalid() :
	      self.Graphe.setEnabled(1)
           else:
	      self.Graphe.setEnabled(0)

    def doPaste(self,node_selected):
        """
            Déclenche la copie de l'objet item avec pour cible
            l'objet passé en argument : node_selected
        """
        objet_a_copier = self.item.get_copie_objet()
        child=node_selected.doPasteCommande(objet_a_copier)
        return child

    def doPasteCommande(self,objet_a_copier):
        """
          Réalise la copie de l'objet passé en argument qui est nécessairement
          une commande
        """
        parent=self.parent
        #child = parent.item.append_child(objet_a_copier,self.item.getObject())
        child = self.append_brother(objet_a_copier)
        #if child is None:return 0
        return child

    def doPasteMCF(self,objet_a_copier):
        """
           Réalise la copie de l'objet passé en argument (objet_a_copier)
           Il s'agit forcément d'un mot clé facteur
        """
        child = self.append_child(objet_a_copier,pos='first',retour='oui')
        return child

    def view3D(self) :
        from Editeur import TroisDPal
        troisD=TroisDPal.TroisDPilote(self.item,self.editor.parent.appliEficas)
        troisD.envoievisu()

    def viewPng(self) :
        from monPixmap import MonLabelPixmap
        fichier=self.appliEficas.getName()
        widgetPng=MonLabelPixmap(self.appliEficas,fichier)
        ret=widgetPng.exec_()

class EtapeTreeItem(Objecttreeitem.ObjectTreeItem):
  """ La classe EtapeTreeItem est un adaptateur des objets ETAPE du noyau
      Accas. Elle leur permet d'etre affichés comme des noeuds
      d'un arbre graphique.
      Cette classe a entre autres deux attributs importants :
        - _object qui est un pointeur vers l'objet du noyau
        - object qui pointe vers l'objet auquel sont délégués les
          appels de méthode et les acces aux attributs
      Dans le cas d'une ETAPE, _object et object pointent vers le 
      meme objet.
  """
  itemNode=Node
  
  def IsExpandable(self):
      return 1

  def GetIconName(self):
      """
      Retourne le nom de l'icone a afficher dans l'arbre
      Ce nom dépend de la validité de l'objet
      """
      if not self.object.isactif():
         return "ast-white-square"
      elif self.object.isvalid():
         return "ast-green-square"
      else:
         valid=self.valid_child()
         valid=valid * self.valid_regles("non")
         if self.reste_val != {}:
            valid=0
         if valid==0  :
            return "ast-red-square"
         else :
            try :
            # on traite ici le cas d include materiau
            #  print self.object.definition.nom 
              if  self.object.fichier_ini != self.object.nom_mater :
                  return "ast-red-square"
            except :
              pass
            return "ast-yellow-square"

  def GetLabelText(self):
      """ Retourne 3 valeurs :
      - le texte a afficher dans le noeud représentant l'item
      - la fonte dans laquelle afficher ce texte
      - la couleur du texte
      """
      if self.object.isactif():
        # None --> fonte et couleur par défaut
        return self.labeltext,None,None
      else:
        return self.labeltext, None, None #CS_pbruno todo
      
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
      mcent = self._object.addentite(name,pos)
      return mcent
      

  def suppitem(self,item) :
      # item : item du MOCLE de l'ETAPE a supprimer
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
      # Format de fichier utilisé
      format=self.appli.format_fichier
      return self.object.get_objet_commentarise(format)

  def get_objet_commentarise_BAK(self):
      """
          Cette méthode retourne un objet commentarisé
          représentatif de self.object
      """
      import generator,string,Accas
      # Format de fichier utilisé
      format=self.appli.format_fichier
      g=generator.plugins[format]()
      texte_commande = g.gener(self.object,format='beautifie')
      # Il faut enlever la premiere ligne vide de texte_commande que 
      # rajoute le generator
      rebut,texte_commande = string.split(texte_commande,'\n',1)
      # on construit l'objet COMMANDE_COMM repésentatif de self mais non 
      # enregistré dans le jdc
      commande_comment = Accas.COMMANDE_COMM(texte=texte_commande,reg='non',
                                             parent=self.object.parent)
      commande_comment.niveau = self.object.niveau
      commande_comment.jdc = commande_comment.parent = self.object.jdc

      pos=self.object.parent.etapes.index(self.object)
      parent=self.object.parent
      self.object.parent.suppentite(self.object)
      parent.addentite(commande_comment,pos)

      return commande_comment


import Accas
treeitem = EtapeTreeItem
objet = Accas.ETAPE    

