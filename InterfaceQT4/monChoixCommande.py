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

from desChoixCommandes import Ui_ChoixCommandes
from PyQt4  import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr
import os

    
# Import des panels

class MonChoixCommande(Ui_ChoixCommandes,QtGui.QWidget):
  """
  """
  def __init__(self,node, jdc_item, editor):
      QtGui.QWidget.__init__(self,None)
      self.setupUi(self)
      #self.labelIcone.setText('<img src="/local00/home/A96028/Install_EficasV1/KarineEficas/InterfaceQT4/loopOff.png">');

      self.item = jdc_item
      self.node = node
      self.editor = editor
      self.jdc  = self.item.object.get_jdc_root()
      debutTitre=self.editor.titre
      self.listeWidget=[]
      if self.editor.fichier != None : 
          nouveauTitre=debutTitre+" "+str(os.path.basename(self.editor.fichier))
      else :
          nouveauTitre=debutTitre
      self.editor.appliEficas.setWindowTitle(nouveauTitre)

      #print self.node.tree

      self.connect(self.RBalpha,SIGNAL("clicked()"),self.afficheAlpha)
      self.connect(self.RBGroupe,SIGNAL("clicked()"),self.afficheGroupe)
      self.connect(self.RBOrdre,SIGNAL("clicked()"),self.afficheOrdre)
      if self.node.tree.item.get_regles() == () :
         self.RBRegle.close()
         self.labelRegle.close()
      else : self.connect(self.RBRegle,SIGNAL("clicked()"),self.afficheRegle)

      if self.editor.Ordre_Des_Commandes == None : self.RBOrdre.close()

       
      self.editor.labelCommentaire.setText("")
      if self.editor.widgetOptionnel!= None : 
         self.editor.widgetOptionnel.close()
         self.editor.widgetOptionnel=None
      self.name=None
      self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.AjouteRadioButton)

      self.affiche_alpha=0
      self.affiche_groupe=0
      self.affiche_ordre=0
      if self.editor.affiche=="alpha"  : 
         self.affiche_alpha==1;  
         self.RBalpha.setChecked(True);
         self.afficheAlpha()
      elif self.editor.affiche=="groupe" : 
         self.affiche_groupe==1; 
         self.RBGroupe.setChecked(True); 
         self.afficheGroupe()
      elif self.editor.affiche=="ordre"  : 
         self.affiche_ordre==1;  
         self.RBOrdre.setChecked(True);  
         self.afficheOrdre()
      if self.editor.code == "Adao" : self.frameAffichage.close()

  def afficheRegle(self):
      self.node.tree.AppelleBuildLBRegles()

  def afficheAlpha(self):
      self.affiche_alpha=1
      self.affiche_groupe=0
      self.affiche_ordre=0
      self.AjouteRadioButton()

  def afficheGroupe(self):
      self.affiche_alpha=0
      self.affiche_groupe=1
      self.affiche_ordre=0
      self.AjouteRadioButton()

  def afficheOrdre(self):
      self.affiche_alpha=0
      self.affiche_groupe=0
      self.affiche_ordre=1
      self.AjouteRadioButton()

  def mouseDoubleClickEvent(self,event):
      nodeCourrant=self.node.tree.currentItem()
      if nodeCourrant==None: nodeCourrant=self.node.tree.racine
      if self.name != None :
         plier=self.editor.afficheCommandesPliees
         if nodeCourrant==self.node : nouveau=self.node.append_child(self.name,'first',plier)
         else : nouveau=nodeCourrant.append_brother(self.name,plier=plier)
      else :
         nouveau = 0
      if nouveau == 0 : return # on n a pas insere le noeud
      nouveau.setDeplie()
      #if self.editor.afficheApresInsert==True : nouveau.plieToutEtReaffiche()
      if self.editor.afficheApresInsert == True :
           #if self.editor.affichePlie==True:  nouveau.plieToutEtReaffiche()
           if self.editor.afficheCommandesPliees ==True:  nouveau.plieToutEtReaffiche()
           else : nouveau.deplieToutEtReaffiche()
           nouveau.fenetre.donnePremier()
           #nouveau.deplieToutEtReaffiche()
      else :
           self.node.setSelected(False)
           nouveau.setSelected(True)
           self.node.tree.setCurrentItem(nouveau)
      event.accept()
      

  def CreeListeCommande(self,filtre):
      listeGroupes,dictGroupes=self.jdc.get_groups()
      if "CACHE" in dictGroupes.keys():
         aExclure=dictGroupes["CACHE"]
      else:
         aExclure=()
      listeACreer=[]
      for l in self.jdc.get_liste_cmd():
         if l not in aExclure : 
            if filtre != None and not filtre in l : continue
            listeACreer.append(l)
      return listeACreer

  def AjouteRadioButton(self):
      filtre=str(self.LEFiltre.text())
      if filtre==str("") : filtre=None
      if hasattr(self,'buttonGroup') :
         for b in self.buttonGroup.buttons():
             self.buttonGroup.removeButton(b)
             b.close()
      else :
         self.buttonGroup = QButtonGroup()
      for w in self.listeWidget :
         w.close()
      self.listeWidget=[]
      if self.affiche_alpha==1 :
         liste=self.CreeListeCommande(filtre)
         for cmd in liste :
           rbcmd=(QRadioButton(tr(cmd)))
           self.buttonGroup.addButton(rbcmd)
           self.commandesLayout.addWidget(rbcmd)
           rbcmd.mouseDoubleClickEvent=self.mouseDoubleClickEvent
           self.connect(self.buttonGroup, SIGNAL("buttonClicked(QAbstractButton*)"),self.rbClique) 
      elif  self.affiche_groupe==1 :
         listeGroupes,dictGroupes=self.jdc.get_groups()
         for grp in listeGroupes:
           if grp == "CACHE" : continue
           label=QLabel(self)
           text=QString.fromUtf8('<html><head/><body><p><span style=\" font-weight:600;\">Groupe : '+tr(grp)+'</span></p></body></html>')
           label.setText(text)
           self.listeWidget.append(label)
           aAjouter=1
           for cmd in  dictGroupes[grp]:
              if filtre != None and not filtre in cmd : continue
              if aAjouter == 1 :
                 self.commandesLayout.addWidget(label)
                 aAjouter=0
              rbcmd=(QRadioButton(tr(cmd)))
              self.buttonGroup.addButton(rbcmd)
              self.commandesLayout.addWidget(rbcmd)
              rbcmd.mouseDoubleClickEvent=self.mouseDoubleClickEvent
              self.connect(self.buttonGroup, SIGNAL("buttonClicked(QAbstractButton*)"),self.rbClique)
           label2=QLabel(self)
           label2.setText(" ")
           self.listeWidget.append(label2)
           self.commandesLayout.addWidget(label2)
      elif  self.affiche_ordre==1 :
         listeFiltre=self.CreeListeCommande(filtre)
         liste=[]
         if self.editor.Ordre_Des_Commandes == None : Ordre_Des_Commandes=listeFiltre
         else : Ordre_Des_Commandes=self.editor.Ordre_Des_Commandes
         for cmd in Ordre_Des_Commandes :
            if cmd in listeFiltre :
                 liste.append(cmd)
         for cmd in liste :
           rbcmd=(QRadioButton(tr(cmd)))
           self.buttonGroup.addButton(rbcmd)
           self.commandesLayout.addWidget(rbcmd)
           rbcmd.mouseDoubleClickEvent=self.mouseDoubleClickEvent
           self.connect(self.buttonGroup, SIGNAL("buttonClicked(QAbstractButton*)"),self.rbClique) 

     
  def LEfiltreReturnPressed(self):
      self.AjouteRadioButton(filtre)


  def rbClique(self,id):
      self.name=str(id.text().toLatin1())
      definitionEtape=getattr(self.jdc.cata[0],self.name)
      commentaire=getattr(definitionEtape,self.jdc.lang)
      try :
        commentaire=getattr(definitionEtape,self.jdc.lang)
      except :
        try :
           commentaire=getattr(definitionEtape,"ang")
        except :
           commentaire=""
      self.editor.labelCommentaire.setText(commentaire)



  def setValide(self):
      #PNPN a priori pas d icone mais peut-etre a faire
      pass
