#-*- coding: iso-8859-1 -*-
# Copyright (C) 2007-2017   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
from __future__ import absolute_import
try :
   from builtins import str
except : pass

import os
import tempfile
from PyQt5.QtWidgets import QMessageBox, QAction, QApplication
from PyQt5.QtGui  import QCursor
from PyQt5.QtCore import Qt

from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException

from Editeur     import Objecttreeitem
from . import browser
from . import typeNode

class Node(browser.JDCNode, typeNode.PopUpMenuNode):


    def select(self):
        browser.JDCNode.select(self)
        self.treeParent.tree.openPersistentEditor(self,1)
        self.monWidgetNom=self.treeParent.tree.itemWidget(self,1)
        self.monWidgetNom.returnPressed.connect(self.nomme)
        if self.item.getIconName() == "ast-red-square" : self.monWidgetNom.setDisabled(True)
        #else : self.monWidgetNom.setFocus()  ;self.monWidgetNom.setDisabled(False)

    def nomme(self):
        nom=str(self.monWidgetNom.text())
        self.editor.initModif()
        test,mess = self.item.nommeSd(nom)
        if (test== 0):
           self.editor.afficheInfos(mess,Qt.red)
           old=self.item.getText()
           self.monWidgetNom.setText(old)
        else :
           self.editor.afficheCommentaire(tr("Nommage du concept effectue"))
           self.onValid()
           try :
             self.fenetre.LENom.setText(nom)
           except :
             pass


    def getPanel(self):
        from .monWidgetCommande import MonWidgetCommande
        return MonWidgetCommande(self,self.editor,self.item.object)

    def createPopUpMenu(self):
        typeNode.PopUpMenuNode.createPopUpMenu(self)
        if ("AFFE_CARA_ELEM" in self.item.getGenealogie()) and self.editor.salome: 
           self.ViewElt = QAction(tr('View3D'),self.tree)
           self.tree.connect(self.ViewElt,SIGNAL("triggered()"),self.view3D)
           self.ViewElt.setStatusTip(tr("affiche dans Geom les elements de structure"))
           self.menu.addAction(self.ViewElt)
           if self.item.isValid() :
              self.ViewElt.setEnabled(1)
           else:
              self.ViewElt.setEnabled(0)
        if  self.item.getNom() == "DISTRIBUTION" :
           self.Graphe = QAction(tr('Graphique'),self.tree)
           self.Graphe.triggered.connect(self.viewPng)
           self.Graphe.setStatusTip(tr("affiche la distribution "))
           self.menu.addAction(self.Graphe)
           if self.item.isValid() :
              self.Graphe.setEnabled(1)
           else:
              self.Graphe.setEnabled(0)

    def view3D(self) :
        from Editeur import TroisDPal
        troisD=TroisDPal.TroisDPilote(self.item,self.editor.appliEficas)
        troisD.envoievisu()

    def viewPng(self) :
        from monPixmap import MonLabelPixmap
        import generator
        try:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            g = generator.plugins[self.appliEficas.format_fichier]()
            g.gener(self.item.object, format='beautifie')
            stdGener = g.getGenerateur()
            loi = list(g.dictMCLois.keys())[0]
            nomLoi = loi.getName()
            (fd, fichier) = tempfile.mkstemp(prefix = "openturns_graph_", suffix = ".png")
            os.close(fd)
            chemin = os.path.dirname(fichier)
            base = os.path.splitext(os.path.basename(fichier))[0]
            script = stdGener.GraphiquePDF(loi, chemin, base)
            #print script
            d = {}
            exec(script, d)
            widgetPng=MonLabelPixmap(self.appliEficas,fichier,nomLoi)
            os.remove(fichier)
            QApplication.restoreOverrideCursor()
            widgetPng.show()
        except:
            QApplication.restoreOverrideCursor()
            QMessageBox.warning(
                self.appliEficas,
                tr("Erreur interne"),
                tr("La PDF de la loi ne peut pas etre affichee."),
                tr("&Annuler"))

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
  
  def isExpandable(self):
      return 1

  def getIconName(self):
      """
      Retourne le nom de l'icone a afficher dans l'arbre
      Ce nom depend de la validite de l'objet
      """
      if not self.object.isActif():
         return "ast-white-square"
      elif self.object.isValid():
         return "ast-green-square"
      else:
         valid=self.validChild()
         valid=valid * self.validRegles("non")
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

  def getLabelText(self):
      """ Retourne 3 valeurs :
      - le texte a afficher dans le noeud représentant l'item
      - la fonte dans laquelle afficher ce texte
      - la couleur du texte
      """
      return self.labeltext,None,None
      #if self.object.isActif():
        # None --> fonte et couleur par défaut
      #  return self.labeltext,None,None
      #else:
      #  return self.labeltext, None, None #CS_pbruno todo
      
  #def get_objet(self,name) :
  #    for v in self.object.mc_liste:
  #        if v.nom == name : return v
  #    return None
      
 # def getType_sd_prod(self):
 #     """
 #        Retourne le nom du type du concept résultat de l'étape
 #     """
 #     sd_prod=self.object.getType_produit()
 #     if sd_prod:
 #        return sd_prod.__name__
 #     else:
 #        return ""

  def addItem(self,name,pos):      
      mcent = self._object.addEntite(name,pos)
      return mcent
      

  def suppItem(self,item) :
      # item : item du MOCLE de l'ETAPE a supprimer
      # item.getObject() = MCSIMP, MCFACT, MCBLOC ou MCList 
      itemobject=item.getObject()
      if itemobject.isOblig() :
          return (0,tr('Impossible de supprimer un mot-clef obligatoire '))
      if self.object.suppEntite(itemobject):
          message = tr("Mot-clef %s supprime " , itemobject.nom)
          return (1,message)
      else :
          return (0,tr('Pb interne : impossible de supprimer ce mot-clef'))

  def getText(self):
      try:
          return self.object.getSdname()
      except:
          return ''

  # PNPN ????
  #def keys(self):
  #    keys=self.object.mc_dict
  #    return keys

  def getSubList(self):
      """
         Reactualise la liste des items fils stockes dans self.sublist
      """
      if self.isActif():
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
            def setFunction(value, object=obj):
                object.setval(value)
            item = self.makeObjecttreeitem(self.appli, obj.nom + " : ", obj, setFunction)
            sublist[pos]=item
         pos=pos+1

      self.sublist=sublist
      return self.sublist

  def isValid(self):
      return self.object.isValid()

  def isCopiable(self):
      """
      Retourne 1 si l'objet est copiable, 0 sinon
      """
      return 1

  def updateDeplace(self,item):
      if item.sd and item.sd.nom:
         self.object.sd=item.sd
         self.object.sd.nom=item.sd.nom

  def update(self,item):
      if item.sd and item.sd.nom:
         self.nommeSd(item.sd.nom)

  def nommeSd(self,nom):
      """ Lance la méthode de nommage de la SD """
      oldnom=""
      if self.object.sd != None :
         oldnom=self.object.sd.nom
      test,mess= self.object.nommeSd(nom)
      if test:self.object.parent.resetContext()
      if (test and oldnom in self.appli.dict_reels ):
              self.appli.dict_reels[nom]=self.appli.dict_reels[oldnom]
      return test,mess

  def isReentrant(self):
      return self.object.isReentrant()
    
  def getNomsSdOperReentrant(self):
      return self.object.getNomsSdOperReentrant()

  def getObjetCommentarise(self):
      """
          Cette méthode retourne un objet commentarisé
          représentatif de self.object
      """
      # Format de fichier utilisé
      format=self.appli.appliEficas.format_fichier
      return self.object.getObjetCommentarise(format)

  def getObjetCommentarise_BAK(self):
      """
          Cette méthode retourne un objet commentarisé
          représentatif de self.object
      """
      import generator,Accas
      # Format de fichier utilisé
      format=self.appli.appliEficas.format_fichier
      g=generator.plugins[format]()
      texte_commande = g.gener(self.object,format='beautifie')
      # Il faut enlever la premiere ligne vide de texte_commande que 
      # rajoute le generator
      rebut,texte_commande = texte_commande.split('\n',1)
      # on construit l'objet COMMANDE_COMM repésentatif de self mais non 
      # enregistré dans le jdc
      commande_comment = Accas.COMMANDE_COMM(texte=texte_commande,reg='non',
                                             parent=self.object.parent)
      commande_comment.niveau = self.object.niveau
      commande_comment.jdc = commande_comment.parent = self.object.jdc

      pos=self.object.parent.etapes.index(self.object)
      parent=self.object.parent
      self.object.parent.suppEntite(self.object)
      parent.addEntite(commande_comment,pos)

      return commande_comment


import Accas
treeitem = EtapeTreeItem
objet = Accas.ETAPE    

