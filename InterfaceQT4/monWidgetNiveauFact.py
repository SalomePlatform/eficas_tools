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
# Modules Python
# Modules Eficas

from __future__ import absolute_import
try :
   from builtins import str
except : pass

import types

from desWidgetNiveauFact import Ui_WidgetNiveauFact
from InterfaceQT4.groupe import Groupe
#from .gereIcones import FacultatifOuOptionnel

from PyQt5.QtWidgets  import  QWidget
#from PyQt5.QtWidgets  import QApplication, QWidget, QSpacerItem, QSizePolicy
#from PyQt5.QtGui import QFont, QIcon
#from PyQt5.QtCore import QTimer
#from PyQt5.QtCore import Qt



from Extensions.i18n import tr
import Accas 
import os

    
# Import des panels

class MonWidgetNiveauFact(Ui_WidgetNiveauFact,Groupe):
  """
  """
  def __init__(self,node,editor,definition,obj):
      #QWidget.__init__(self,editor)
      #self.setupUi(self)
      self.listeAffichageWidget=[]
      Groupe.__init__(self,node,editor,None,definition,obj,1,self)

  def reaffiche(self,nodeAVoir=None):
      print ('PNPNPN a programmer')
#
#      self.listeAffichageWidget=[]
#      self.inhibe=0
#      self.ensure=0
#      editor.inhibeSplitter=1
#      editor.inhibeSplitter=0
#
#      self.frameAffichage.setMinimumHeight(20)
#      if node.item.getFr() != "" : self.labelDoc.setText(node.item.getFr())
#      else : 
#        self.labelDoc.close()
#        self.frameAffichage.resize(self.frameAffichage.width(),50)
#      
#      #if (etape.getType_produit()==None): self.LENom.close()
#      #test,mess = self.node.item.nommeSd('ee')
#      if not(hasattr(etape.definition,'sd_prod')) or (etape.definition.sd_prod==None): self.LENom.close()
#      elif (hasattr(etape.definition,'sd_prod') and type(etape.definition.sd_prod)== types.FunctionType):self.LENom.close()
#      elif (hasattr(etape, 'sdnom')) and etape.sdnom != "sansnom" and etape.sdnom != None: self.LENom.setText(etape.sdnom)
#      else : self.LENom.setText("")
#
#
#      maPolice= QFont("Times", 10,)
#      self.setFont(maPolice)
#      self.labelNomCommande.setText(tr(self.obj.nom))
#
#
#      if self.editor.closeAutreCommande == True  : self.closeAutreCommande()
#      else :
#        try :
#           self.bCatalogue.clicked.connect(self.afficheCatalogue)
#           self.bAvant.clicked.connect(self.afficheAvant)
#           self.bApres.clicked.connect(self.afficheApres)
#        except :
#           pass
#        self.LENom.returnPressed.connect(self.nomChange)
#   
#      if self.editor.code in ['Adao','ADAO'] and self.editor.closeFrameRechercheCommande==True  : 
#                      self.frameAffichage.close()
#
#      if self.editor.code in ['CARMELCND',] : self.closeAutreCommande()
#      self.racine=self.node.tree.racine
#      if self.node.item.getIconName() == "ast-red-square" : self.LENom.setDisabled(True)
#
#      self.setAcceptDrops(True)
#      self.etablitOrdre()
#
#      if self.editor.code == "CARMELCND" : 
#         self.RBPoubelle.close() # JDC Fige
#         return                  # Pas de MC Optionnels pour Carmel
#
#      from .monWidgetOptionnel import MonWidgetOptionnel
#      if self.editor.widgetOptionnel!= None : 
#        self.monOptionnel=self.editor.widgetOptionnel
#      else :
#        self.editor.inhibeSplitter=1
#        self.monOptionnel=MonWidgetOptionnel(self.editor)
#        self.editor.widgetOptionnel=self.monOptionnel
#        self.editor.splitter.addWidget(self.monOptionnel)
#        self.editor.ajoutOptionnel()
#        self.editor.inhibeSplitter=0
#      self.afficheOptionnel()
#      #self.editor.restoreSplitterSizes()
#
#      #print "fin init de widget Commande"
#      
#
#  def closeAutreCommande(self):
#      self.bCatalogue.close()
#      self.bAvant.close()
#      self.bApres.close()
#
#  def donnePremier(self):
#      #print "dans donnePremier"
#      QApplication.processEvents()
#      if self.listeAffichageWidget != [] :
#         self.listeAffichageWidget[0].setFocus(7)
#      QApplication.processEvents()
#      #print self.focusWidget()
#
#
#  def focusNextPrevChild(self, next):
#      # on s assure que ce n est pas un chgt de fenetre
#      #print "je passe dans focusNextPrevChild"
#      if self.editor.fenetreCentraleAffichee != self : return True
#      f=self.focusWidget()
#      if f not in self.listeAffichageWidget :
#         i=0
#         while not hasattr (f,'AAfficher') :
#           if f==None :i=-1; break
#           f=f.parentWidget()
#         if hasattr(f,'AAfficher') : f=f.AAfficher
#         if i != -1 : i=self.listeAffichageWidget.index(f)
#      else :i=self.listeAffichageWidget.index(f) 
#      if (i==len(self.listeAffichageWidget) -1) and next and not self.inhibe: 
#         try :
#           self.listeAffichageWidget[1].setFocus(7)
#           w=self.focusWidget()
#           self.inhibe=1
#           w.focusPreviousChild()
#           self.inhibe=0
#           return True
#         except :
#           pass
#           #print self.listeAffichageWidget
#           #print "souci ds focusNextPrevChild"
#      if i==0 and next==False and not self.inhibe: 
#         if hasattr(self.editor.fenetreCentraleAffichee,'scrollArea'):
#            self.editor.fenetreCentraleAffichee.scrollArea.ensureWidgetVisible(self.listeAffichageWidget[-1])
#         self.listeAffichageWidget[-2].setFocus(7)
#         self.inhibe=1
#         w=self.focusWidget()
#         w.focusNextChild()
#         self.inhibe=0
#         return True
#      if i==0 and next==True and not self.inhibe:
#         self.listeAffichageWidget[0].setFocus(7)
#         self.inhibe=1
#         w=self.focusWidget()
#         w.focusNextChild()
#         self.inhibe=0
#         return True
#      if i>0 and next==False and not self.inhibe:
#         if isinstance(self.listeAffichageWidget[i-1],QRadioButton):
#           self.listeAffichageWidget[i-1].setFocus(7)
#           return True
#      return QWidget.focusNextPrevChild(self, next)
#
#  def etablitOrdre(self):
#      i=0
#      while(i +1 < len(self.listeAffichageWidget)):
#         self.setTabOrder(self.listeAffichageWidget[i],self.listeAffichageWidget[i+1])
#         i=i+1
#      # si on boucle on perd l'ordre
# 
#  def  afficheNieme(self,n):
#      #print ('ds afficheNieme')
#      self.listeAffichageWidget[n].setFocus(7)
#
#  def  afficheSuivant(self,f):
#      #print ('ds afficheSuivant')
#      try :
#        i=self.listeAffichageWidget.index(f) 
#        next=i+1
#      except :
#        next=1
#      if (next==len(self.listeAffichageWidget) ): next =0
#      #self.f=next
#      #QTimer.singleShot(1, self.rendVisible)
#      try :
#        self.listeAffichageWidget[next].setFocus(7)
#      except :
#        pass
#
#
#  def afficheOptionnel(self):
#      # N a pas de parentQt. doit donc etre redefini
#      liste,liste_rouge=self.ajouteMCOptionnelDesBlocs()
#      #print "dans afficheOptionnel", self.monOptionnel
#      # dans le cas ou l insertion n a pas eu leiu (souci d ordre par exemple)
#      #if self.monOptionnel == None : return
#      self.monOptionnel.parentCommande=self
#      self.monOptionnel.titre(self.obj.nom)
#      self.monGroupe=self.monOptionnel.afficheOptionnel(liste,liste_rouge,self)
#      
#
#  def focusInEvent(self,event):
#      #print "je mets a jour dans focusInEvent de monWidget Commande "
#      if self.editor.code == "CARMELCND" : return #Pas de MC Optionnels pour Carmel
#      self.afficheOptionnel()
#
#
#  def reaffiche(self,nodeAVoir=None):
#      # Attention delicat. les appels de fonctions ne semblent pas pouvoir etre supprimes!
#      self.avantH=self.editor.fenetreCentraleAffichee.scrollAreaCommandes.horizontalScrollBar().sliderPosition()
#      self.avantV=self.editor.fenetreCentraleAffichee.scrollAreaCommandes.verticalScrollBar().sliderPosition()
#      self.inhibeExpand=True
#      self.node.affichePanneau()
#      #QTimer.singleShot(1, self.recentre)
#      if nodeAVoir != None and nodeAVoir!=0:
#        self.f=nodeAVoir.fenetre
#        if self.f==None : 
#             newNode=nodeAVoir.treeParent.chercheNoeudCorrespondant(nodeAVoir.item.object)
#             self.f = newNode.fenetre 
#        if self.f != None and self.f.isVisible() : self.inhibeExpand=False; return
#        if self.f != None : self.rendVisible()
#        else : self.recentre()
#      else : self.recentre()
#      self.inhibeExpand=False
#
#  def reafficheSeulement(self,nodeAReafficher,index):
#      #print ('ds reafficheSeulement', nodeAReafficher)
#      parentNodeAReafficher=nodeAReafficher.parentQt
#      index=parentNodeAReafficher.commandesLayout.indexOf(nodeAReafficher)
#      oldFenetre=nodeAReafficher.node.fenetre
#      newWidget=nodeAReafficher.node.getPanelGroupe(parentNodeAReafficher,self,index)
#      nodeAReafficher.node.fenetre=newWidget
#      oldFenetre.setParent(None)
#      oldFenetre.close()
#      oldFenetre.deleteLater()
#      #print ("fin pour " , self.node.item.nom)
#
#
#  def recentre(self):
#      QApplication.processEvents()
#      s=self.editor.fenetreCentraleAffichee.scrollAreaCommandes
#      s.horizontalScrollBar().setSliderPosition(self.avantH)
#      s.verticalScrollBar().setSliderPosition(self.avantV)
#
#  def rendVisibleNoeud(self,node):
#      self.f=node.fenetre
#      #print "dans rendVisibleNoeud",self.f
#      QTimer.singleShot(1, self.rendVisible)
#     
#  def rendVisible(self):
#      #print "dans rendVisible",self.f
#      QApplication.processEvents()
#      self.f.setFocus(7)
#      self.editor.fenetreCentraleAffichee.scrollAreaCommandes.ensureWidgetVisible(self.f)
#
#  def afficheCatalogue(self):
#      if self.editor.widgetOptionnel != None : self.monOptionnel.hide()
#      self.racine.affichePanneau()
#      if self.node : self.node.select()
#      else : self.racine.select()
#
#  def afficheApres(self):
#       self.node.selectApres()
#
#  def afficheAvant(self):
#       self.node.selectAvant()
#
#  def setValide(self):
#      if not(hasattr (self,'RBValide')) : return
#      icon = QIcon()
#      if self.node.item.object.isValid() :
#         icon=QIcon(self.repIcon+"/ast-green-ball.png")
#      else :
#         icon=QIcon(self.repIcon+"/ast-red-ball.png")
#      if self.node.item.getIconName() == "ast-yellow-square" :
#         icon=QIcon(self.repIcon+"/ast-yel-ball.png")
#      self.LENom.setDisabled(False)
#      if self.node.item.getIconName() == "ast-red-square" : self.LENom.setDisabled(True)
#      self.RBValide.setIcon(icon)
#
