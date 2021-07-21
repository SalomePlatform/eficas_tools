# Copyright (C) 2007-2021   EDF R&D
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
from __future__ import print_function
from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

from Extensions.i18n import tr

from .gereIcones import FacultatifOuOptionnel
import Accas 
import traceback

    
# Import des panels

class Groupe(QWidget,FacultatifOuOptionnel):
  """
  """
  def __init__(self,node,editor,parentQt,definition,obj,niveau,commande=None):
      #print ("groupe : ",self.node.item.nom," ",self.node.fenetre)
      QWidget.__init__(self,None)
      self.node=node
      self.node.fenetre=self
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
      self.jdc=self.node.item.getJdc()
      self.setIconePoubelle()
      self.setIconesGenerales()
      self.setRun()
      self.setValide()
      self.setReglesEtAide()
      self.afficheMots()
      self.listeMCAAjouter=[]
      self.dictMCVenantDesBlocs={}
      if hasattr(self,'RBDeplie')  : self.RBDeplie.clicked.connect(self.setDeplie)
      if hasattr(self,'RBPlie')    : self.RBPlie.clicked.connect( self.setPlie)

      self.setAcceptDrops(True)
      #if hasattr (self, 'commandesLayout'): 
      #   print (' j ajoute un spacer dans ', self.node.item.nom)
      #   spacerItem = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)
      #   self.commandesLayout.addItem(spacerItem)
     
  def donneFocus(self):
      for fenetre in self.listeFocus:
          if fenetre==None : return
          if fenetre.node.item.isValid() == 0 :
             fenetre.prendLeFocus=1
             fenetre.hide()
             fenetre.show()
      

  def afficheMots(self):
      #print ("ds afficheMots ",self.node.item.nom,self.node.plie)
      for node in self.node.children:
           # non return mais  continue car il faut tenir compte des blocs
           if node.appartientAUnNoeudPlie==True : continue
           widget=node.getPanelGroupe(self,self.maCommande)
           #print ("widget pour ", node.item.nom, widget)
           self.listeFocus.append(node.fenetre)
      #print "fin pour " , self.node.item.nom

       
  def calculOptionnel(self):
        self.listeMc=[]
        self.listeMcRegle=[]
        self.dictToolTipMc={}
        genea =self.obj.getGenealogie()
        # Attention : les mots clefs listes (+sieurs fact )
        # n ont pas toutes ces methodes
        try :
        #if 1 :
           self.listeMc     = self.obj.getListeMcOrdonnee(genea,self.jdc.cata_ordonne_dico)
           listeNomsPresents=self.obj.dictMcPresents()
           for regle in self.obj.getRegles():
               (monToolTip,regleOk)=regle.verif(listeNomsPresents)
               if regleOk : continue
               for mc in regle.mcs :
                   self.listeMcRegle.append(mc)
                   self.dictToolTipMc[mc]=monToolTip
        except :
           #print ('in except')
           #print (self)
           return
        
  def afficheOptionnel(self):
        if self.editor.maConfiguration.closeOptionnel : return
        liste,liste_rouge=self.ajouteMCOptionnelDesBlocs()
        self.monOptionnel=self.editor.widgetOptionnel
        self.monOptionnel.afficheOptionnel(liste,liste_rouge,self)
           

  def ajouteMCOptionnelDesBlocs(self):
      self.dictMCVenantDesBlocs={}
      i=0
      self.calculOptionnel()
      liste=self.listeMc
      liste_rouge=self.listeMcRegle
      for MC in self.listeMc : self.dictMCVenantDesBlocs[MC]=self
      # ce cas est le cas machine tournant sr le plie
      try :
        while i < self.commandesLayout.count():
          from .monWidgetBloc import MonWidgetBloc
          widget=self.commandesLayout.itemAt(i).widget()
          i=i+1
          if not(isinstance(widget,MonWidgetBloc)) : continue
          widget.calculOptionnel()
          listeW,listeW_rouge=widget.ajouteMCOptionnelDesBlocs() 
          for MC in widget.dictMCVenantDesBlocs:
              if MC in self.dictMCVenantDesBlocs: print ("Pb Sur les MC" )
              else : self.dictMCVenantDesBlocs[MC]=widget.dictMCVenantDesBlocs[MC]
          liste=liste+listeW
          liste_rouge=liste_rouge+listeW_rouge
      except : 
        pass
      return (liste,liste_rouge)


  def reaffiche(self,nodeAVoir=None):
      #print "dans reaffiche de groupe.py", nodeAVoir
      self.parentQt.reaffiche(nodeAVoir)

  def recalculeListeMC(self,listeMC):
      #print "pas si peu utile"
      #on ajoute et on enleve
      listeNode=[]
      for name in listeMC :
          nodeAEnlever=self.node.appendChild(name)
          if nodeAEnlever.item.isMCList(): 
             nodeAEnlever=nodeAEnlever.children[-1]
          listeNode.append(nodeAEnlever)
      self.afficheOptionnel()
      self.monOptionnel.affiche(self.listeMc)
      if len(listeNode) == 0 : return
      if len(listeNode) == 1 : 
         listeNode[0].delete()
         self.editor.afficheInfos("")
         return
      for noeud in listeNode:
          noeud.treeParent.item.suppItem(noeud.item)
      noeud.treeParent.buildChildren()
      self.editor.afficheInfos("")

  def ajoutMC(self,texteListeNom):
      listeNom=texteListeNom.split("+")[1:]
      firstNode=None
      for nom in listeNom:
        if nom not in self.dictMCVenantDesBlocs:
           #print "bizarre, bizarre"
           self.editor.initModif()
           nouveau=self.node.appendChild(nom)
        else :
           self.editor.initModif()
           widget=self.dictMCVenantDesBlocs[nom]
           nouveau=widget.node.appendChild(nom)
        if firstNode==None : firstNode=nouveau 
        if nouveau == None or nouveau == 0  : 
           self.editor.afficheInfos(tr('insertion impossible a cet endroit pour '+nom),Qt.red)
      try :
       self.reaffiche(firstNode)
       if firstNode!=None and firstNode !=0 and firstNode.item!=None : firstNode.select()
      except :
       pass


  def setPlie(self):
      self.node.setPlie()
      self.reaffiche(self.node) 

  def setDeplie(self):
      #print ('je passe ds setDeplie de groupe', self.obj.nom)
      self.node.firstDeplie = False
      self.node.setDeplie()
      self.reaffiche(self.node) 
    

  def traiteClicSurLabel(self,texte):
      if self.editor.code != "CARMELCND" : self.afficheOptionnel()


  def propageChange(self,leType):
      self.parentQt.propageChange(leType)

