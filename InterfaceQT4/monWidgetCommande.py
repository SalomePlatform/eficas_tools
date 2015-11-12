# Copyright (C) 2007-2013   EDF R&D
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
# Modules Python
# Modules Eficas

from desWidgetCommande import Ui_WidgetCommande
from groupe import Groupe
from gereIcones import FacultatifOuOptionnel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
import Accas 
import os
import string

    
# Import des panels

class MonWidgetCommande(Ui_WidgetCommande,Groupe):
  """
  """
  def __init__(self,node,editor,etape):
      #print "MonWidgetCommande ", self
      self.listeAffichageWidget=[]
      self.inhibe=0
      self.ensure=0
      Groupe.__init__(self,node,editor,None,etape.definition,etape,1,self)

      if node.item.get_fr() != "" : self.labelDoc.setText(QString(node.item.get_fr()))
      else : self.labelDoc.close()
      
      if (etape.get_type_produit()==None): self.LENom.close()
      elif (hasattr(etape, 'sdnom')) and etape.sdnom != "sansnom" and etape.sdnom != None: self.LENom.setText(etape.sdnom) 
      else : self.LENom.setText("")

      maPolice= QFont("Times", 10,)
      self.setFont(maPolice)
      self.labelNomCommande.setText(tr(self.obj.nom))

      self.commandesLayout.addStretch()
      self.commandesLayout.focusInEvent=self.focusInEvent
      self.scrollAreaCommandes.focusInEvent=self.focusInEvent

      if self.editor.code in ['MAP','CARMELCND'] : self.bCatalogue.close()
      else : self.connect(self.bCatalogue,SIGNAL("clicked()"), self.afficheCatalogue)
      if self.editor.code in ['Adao','MAP'] : 
            self.bAvant.close()
            self.bApres.close()
      else : 
            self.connect(self.bAvant,SIGNAL("clicked()"), self.afficheAvant)
            self.connect(self.bApres,SIGNAL("clicked()"), self.afficheApres)

      
      self.connect(self.LENom,SIGNAL("returnPressed()"),self.nomChange)
      self.racine=self.node.tree.racine
      if self.node.item.GetIconName() == "ast-red-square" : self.LENom.setDisabled(True)

      self.setAcceptDrops(True)
      self.etablitOrdre()

      if self.editor.code == "CARMELCND" : 
         self.RBPoubelle.close() # JDC Fige
         return                  # Pas de MC Optionnels pour Carmel
      from monWidgetOptionnel import MonWidgetOptionnel
      #if hasattr(self.editor,'widgetOptionnel') : 
      if self.editor.widgetOptionnel!= None : 
        self.monOptionnel=self.editor.widgetOptionnel
      else :
        self.monOptionnel=MonWidgetOptionnel(self)
        self.editor.widgetOptionnel=self.monOptionnel
        self.editor.splitter.addWidget(self.monOptionnel)
      self.afficheOptionnel()
      #print "fin init de widget Commande"
      

  def donnePremier(self):
      #print "dans donnePremier"
      qApp.processEvents()
      if self.listeAffichageWidget != [] :
         self.listeAffichageWidget[0].setFocus(7)
      qApp.processEvents()
      #print self.focusWidget()


  def focusNextPrevChild(self, next):
      # on s assure que ce n est pas un chgt de fenetre
      #print "je passe dans focusNextPrevChild"
      if self.editor.fenetreCentraleAffichee != self : return True
      f=self.focusWidget()
      if f not in self.listeAffichageWidget :
         i=0
         while not hasattr (f,'AAfficher') :
           if f==None :i=-1; break
           f=f.parentWidget()
         if hasattr(f,'AAfficher') : f=f.AAfficher
         if i != -1 : i=self.listeAffichageWidget.index(f)
      else :i=self.listeAffichageWidget.index(f) 
      if (i==len(self.listeAffichageWidget) -1) and next and not self.inhibe: 
         try :
           self.listeAffichageWidget[1].setFocus(7)
           w=self.focusWidget()
           self.inhibe=1
           w.focusPreviousChild()
           self.inhibe=0
           return True
         except :
           print self.listeAffichageWidget
           print "souci ds focusNextPrevChild"
      if i==0 and next==False and not self.inhibe: 
         if hasattr(self.editor.fenetreCentraleAffichee,'scrollArea'):
            self.editor.fenetreCentraleAffichee.scrollArea.ensureWidgetVisible(self.listeAffichageWidget[-1])
         self.listeAffichageWidget[-2].setFocus(7)
         self.inhibe=1
         w=self.focusWidget()
         w.focusNextChild()
         self.inhibe=0
         return True
      return QWidget.focusNextPrevChild(self, next)

  def etablitOrdre(self):
      i=0
      while(i +1 < len(self.listeAffichageWidget)):
         self.setTabOrder(self.listeAffichageWidget[i],self.listeAffichageWidget[i+1])
         i=i+1
      # si on boucle on perd l'ordre
 
  def  afficheSuivant(self,f):
      try :
        i=self.listeAffichageWidget.index(f) 
        next=i+1
      except :
        next=1
      if (next==len(self.listeAffichageWidget) -1 ): next =0
      #self.f=next
      #QTimer.singleShot(1, self.rendVisible)
      try :
        self.listeAffichageWidget[next].setFocus(7)
      except :
        pass

  def nomChange(self):
      nom = str(self.LENom.text())
      nom = string.strip(nom)
      if nom == '' : return                  # si pas de nom, on ressort sans rien faire
      test,mess = self.node.item.nomme_sd(nom)
      self.editor.affiche_commentaire(mess)

      #Notation scientifique
      if test :
        from politiquesValidation import Validation
        validation=Validation(self.node,self.editor)
        validation.AjoutDsDictReelEtape()

  def afficheOptionnel(self):
      # N a pas de parentQt. doit donc etre redefini
      liste=self.ajouteMCOptionnelDesBlocs()
      #print "dans afficheOptionnel", self.monOptionnel
      # dans le cas ou l insertion n a pas eu leiu (souci d ordre par exemple)
      #if self.monOptionnel == None : return
      self.monOptionnel.parentMC=self
      self.monOptionnel.affiche(liste)

  #def focusInEvent(self,event):
      #print "je mets a jour dans focusInEvent de monWidget Commande "
  #    if self.editor.code == "CARMELCND" : return #Pas de MC Optionnels pour Carmel
  #    self.afficheOptionnel()


  def reaffiche(self,nodeAVoir=None):
      self.avantH=self.editor.fenetreCentraleAffichee.scrollAreaCommandes.horizontalScrollBar().sliderPosition()
      self.avantV=self.editor.fenetreCentraleAffichee.scrollAreaCommandes.verticalScrollBar().sliderPosition()
      self.inhibeExpand=True
      self.node.affichePanneau()
      #print "dans reaffiche de monWidgetCommande", self.avantH, self.avantV
      QTimer.singleShot(1, self.recentre)
      if nodeAVoir != None:
        self.f=nodeAVoir.fenetre
        if self.f==None : 
             newNode=nodeAVoir.treeParent.chercheNoeudCorrespondant(nodeAVoir.item.object)
             self.f = newNode.fenetre 
        print "dans reaffiche",self.f, nodeAVoir.item.nom
        if self.f != None and self.f.isVisible() : return
        if self.f != None : QTimer.singleShot(1, self.rendVisible)
      self.inhibeExpand=False


  def recentre(self):
      qApp.processEvents()
      s=self.editor.fenetreCentraleAffichee.scrollAreaCommandes
      s.horizontalScrollBar().setSliderPosition(self.avantH)
      s.verticalScrollBar().setSliderPosition(self.avantV)

  def rendVisibleNoeud(self,node):
      self.f=node.fenetre
      print "dans rendVisibleNoeud",self.f, node.item.nom
      QTimer.singleShot(1, self.rendVisible)
     
  def rendVisible(self):
      qApp.processEvents()
      self.f.setFocus(7)
      self.editor.fenetreCentraleAffichee.scrollAreaCommandes.ensureWidgetVisible(self.f)

  def afficheCatalogue(self):
      if self.editor.widgetOptionnel != None : self.monOptionnel.hide()
      self.racine.affichePanneau()
      if self.node : self.node.select()
      else : self.racine.select()

  def afficheApres(self):
       self.node.selectApres()

  def afficheAvant(self):
       self.node.selectAvant()

  def setValide(self):
      if not(hasattr (self,'RBValide')) : return
      icon = QIcon()
      if self.node.item.object.isvalid() :
         icon=QIcon(self.repIcon+"/ast-green-ball.png")
      else :
         icon=QIcon(self.repIcon+"/ast-red-ball.png")
      if self.node.item.GetIconName() == "ast-yellow-square" :
         icon=QIcon(self.repIcon+"/ast-yel-ball.png")
      self.RBValide.setIcon(icon)


