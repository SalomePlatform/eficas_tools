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

from determine import monEnvQT5
if monEnvQT5:
   from PyQt5.QtWidgets import QWidget
   from PyQt5.QtCore import Qt
else :
   from PyQt4.QtGui import *
   from PyQt4.QtCore import *
from Extensions.i18n import tr

from Extensions.i18n import tr
from gereIcones import FacultatifOuOptionnel
import Accas 

    
# Import des panels

class Groupe(QWidget,FacultatifOuOptionnel):
  """
  """
  def __init__(self,node,editor,parentQt,definition,obj,niveau,commande=None):
      QWidget.__init__(self,None)
      self.node=node
      self.node.fenetre=self
      #print "groupe : ",self.node.item.nom," ",self.node.fenetre
      self.setupUi(self)
      self.editor=editor
      self.obj=obj
      self.niveau=niveau
      self.definition=definition
      self.parentQt=parentQt
      self.maCommande=commande
      self.listeFocus=[]
      self.appliEficas=self.editor.appliEficas
      self.repIcon=self.appliEficas.repIcon
      self.jdc=self.node.item.get_jdc()
      self.setIconePoubelle()
      self.setIconesGenerales()
      self.setRun()
      self.setValide()
      self.setReglesEtAide()
      self.afficheMots()
      self.listeMCAAjouter=[]
      self.dictMCVenantDesBlocs={}
      if hasattr(self,'RBDeplie') and not monEnvQT5 : self.connect(self.RBDeplie,SIGNAL("clicked()"), self.Deplie)
      if hasattr(self,'RBPlie')  and not monEnvQT5: self.connect(self.RBPlie,SIGNAL("clicked()"), self.Plie)
      if hasattr(self,'RBDeplie')  and monEnvQT5: self.RBDeplie.clicked.connect(self.Deplie)
      if hasattr(self,'RBPlie')  and monEnvQT5: self.RBPlie.clicked.connect( self.Plie)
      self.setAcceptDrops(True)
      #self.donneFocus()
     
  def donneFocus(self):
      for fenetre in self.listeFocus:
          if fenetre==None : return
          if fenetre.node.item.isvalid() == 0 :
             fenetre.prendLeFocus=1
             fenetre.hide()
             fenetre.show()
      

  def afficheMots(self):
      #print "ds afficheMots ",self.node.item.nom
      for node in self.node.children:
           #if node.item.nom == "Background" :print "afficheMots ",node," " ,node.item.nom, " ",node.plie ," ", node.appartientAUnNoeudPlie,node.getPanelGroupe
           #if node.item.nom == "BackgroundError" :print "afficheMots ",node," " ,node.item.nom, " ",node.plie ," ", node.appartientAUnNoeudPlie,node.getPanelGroupe
           # non return mais  continue car il faut tenir compte des blocs
           if node.appartientAUnNoeudPlie==True : continue
           #print "je suis apres le if pour ",node.item.nom
           widget=node.getPanelGroupe(self,self.maCommande)
           #print "widget pour ", node.item.nom, widget
           self.listeFocus.append(node.fenetre)
      #print "fin pour " , self.node.item.nom

       
  def calculOptionnel(self):
        self.liste_mc=[]
        genea =self.obj.get_genealogie()
        # Attention : les mots clefs listes (+sieurs fact )
        # n ont pas toutes ces methodes
        try :
           self.liste_mc=self.obj.get_liste_mc_ordonnee(genea,self.jdc.cata_ordonne_dico)
        except :
           return
        
  def afficheOptionnel(self):
        liste=self.ajouteMCOptionnelDesBlocs()
        self.monOptionnel=self.editor.widgetOptionnel
        self.monOptionnel.afficheOptionnel(liste,self)
        #self.monOptionnel.affiche(liste)
           

  def ajouteMCOptionnelDesBlocs(self):
      #print "Je passe dans ajouteMCOptionnelDesBlocs pour", self.node.item.nom
      self.dictMCVenantDesBlocs={}
      i=0
      self.calculOptionnel()
      liste=self.liste_mc
      for MC in self.liste_mc : self.dictMCVenantDesBlocs[MC]=self
      while i < self.commandesLayout.count():
          from monWidgetBloc import MonWidgetBloc
          widget=self.commandesLayout.itemAt(i).widget()
          i=i+1
          if not(isinstance(widget,MonWidgetBloc)) : continue
          widget.calculOptionnel()
          listeW=widget.ajouteMCOptionnelDesBlocs() 
          for MC in widget.dictMCVenantDesBlocs.keys():
              if MC in self.dictMCVenantDesBlocs.keys(): print "Pb Sur les MC" 
              else : self.dictMCVenantDesBlocs[MC]=widget.dictMCVenantDesBlocs[MC]
          liste=liste+listeW
      return liste


  def reaffiche(self,nodeAVoir=None):
      #print "dans reaffiche de groupe.py", nodeAVoir
      self.parentQt.reaffiche(nodeAVoir)

  def recalculeListeMC(self,listeMC):
      #print "pas si peu utile"
      #on ajoute et on enleve
      listeNode=[]
      for name in listeMC :
          nodeAEnlever=self.node.append_child(name)
          if nodeAEnlever.item.isMCList(): 
             nodeAEnlever=nodeAEnlever.children[-1]
          listeNode.append(nodeAEnlever)
      self.afficheOptionnel()
      self.monOptionnel.affiche(self.liste_mc)
      if len(listeNode) == 0 : return
      if len(listeNode) == 1 : 
         listeNode[0].delete()
         self.editor.affiche_infos("")
         return
      for noeud in listeNode:
          noeud.treeParent.item.suppitem(noeud.item)
      noeud.treeParent.build_children()
      self.editor.affiche_infos("")

  def ajoutMC(self,texteListeNom):
      listeNom=texteListeNom.split("+")[1:]
      firstNode=None
      for nom in listeNom:
        if nom not in self.dictMCVenantDesBlocs.keys():
           #print "bizarre, bizarre"
           self.editor.init_modif()
           nouveau=self.node.append_child(nom)
        else :
           self.editor.init_modif()
           widget=self.dictMCVenantDesBlocs[nom]
           nouveau=widget.node.append_child(nom)
        if firstNode==None : firstNode=nouveau 
        if nouveau == None or nouveau == 0  : 
           self.editor.affiche_infos(tr('insertion impossible a cet endroit pour '+nom),Qt.red)
      self.reaffiche(firstNode)
      if firstNode!=None and firstNode !=0 and firstNode.item!=None :
        firstNode.select()


  def Plie(self):
      self.node.setPlie()
      self.reaffiche(self.node) 

  def Deplie(self):
      self.node.setDeplie()
      self.reaffiche(self.node) 

  def traiteClicSurLabel(self,texte):
      if self.editor.code != "CARMELCND" : self.afficheOptionnel()

