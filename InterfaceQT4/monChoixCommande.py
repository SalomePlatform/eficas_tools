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
from determine import monEnvQT5
if monEnvQT5 :
   from PyQt5.QtWidgets import QWidget, QAction ,QButtonGroup, QRadioButton, QLabel 
   from PyQt5.QtGui  import QIcon
   from PyQt5.QtCore import QSize
else :
   from PyQt4.QtGui  import *
   from PyQt4.QtCore import *

from Extensions.i18n import tr
import os

    
# Import des panels

class MonChoixCommande(Ui_ChoixCommandes,QWidget):
  """
  """
  def __init__(self,node, jdc_item, editor):
      QWidget.__init__(self,None)
      self.setupUi(self)

      self.repIcon=os.path.join( os.path.dirname(os.path.abspath(__file__)),'..','Editeur','icons')
      iconeFile=os.path.join(self.repIcon,'lettreRblanc30.png')
      icon = QIcon(iconeFile)
      self.RBRegle.setIcon(icon)
      self.RBRegle.setIconSize(QSize(21, 31))

      self.item = jdc_item
      self.node = node
      self.editor = editor
      self.jdc  = self.item.object.get_jdc_root()
      debutTitre=self.editor.titre
      self.listeWidget=[]
      self.dicoCmd={}
      if self.editor.fichier != None : 
          nouveauTitre=debutTitre+" "+str(os.path.basename(self.editor.fichier))
      else :
          nouveauTitre=debutTitre
      self.editor.appliEficas.setWindowTitle(nouveauTitre)


      if monEnvQT5 :
         self.RBalpha.clicked.connect(self.afficheAlpha)
         self.RBGroupe.clicked.connect(self.afficheGroupe)
         self.RBOrdre.clicked.connect(self.afficheOrdre)
         self.RBClear.clicked.connect(self.clearFiltre)
         self.RBCasse.toggled.connect(self.ajouteRadioButtons)
         self.LEFiltre.returnPressed.connect(self.ajouteRadioButtons)
         self.LEFiltre.textChanged.connect(self.ajouteRadioButtons)
      else :
         self.connect(self.RBalpha,SIGNAL("clicked()"),self.afficheAlpha)
         self.connect(self.RBGroupe,SIGNAL("clicked()"),self.afficheGroupe)
         self.connect(self.RBOrdre,SIGNAL("clicked()"),self.afficheOrdre)
         self.connect(self.RBClear,SIGNAL("clicked()"),self.clearFiltre)
         self.connect(self.RBCasse,SIGNAL("toggled(bool)"),self.ajouteRadioButtons)
         self.connect(self.LEFiltre,SIGNAL("returnPressed()"),self.ajouteRadioButtons)
      if self.node.tree.item.get_regles() == () :
         self.RBRegle.close()
         self.labelRegle.close()
      else : 
        if monEnvQT5 : self.RBRegle.clicked.connect(self.afficheRegle)
        else         : self.connect(self.RBRegle,SIGNAL("clicked()"),self.afficheRegle)

      if self.editor.Ordre_Des_Commandes == None : self.RBOrdre.close()

       
      #self.editor.labelCommentaire.setText("")
      if self.editor.widgetOptionnel!= None : 
         self.editor.fermeOptionnel()
         self.editor.widgetOptionnel=None
      self.name=None

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
      if self.editor.closeFrameRechercheCommande == True : self.frameAffichage.close()
      self.editor.restoreSplitterSizes(2) 

  def afficheRegle(self):
      self.node.tree.AppelleBuildLBRegles()

  def afficheAlpha(self):
      self.affiche_alpha=1
      self.affiche_groupe=0
      self.affiche_ordre=0
      self.ajouteRadioButtons()

  def afficheGroupe(self):
      self.affiche_alpha=0
      self.affiche_groupe=1
      self.affiche_ordre=0
      self.ajouteRadioButtons()

  def afficheOrdre(self):
      self.affiche_alpha=0
      self.affiche_groupe=0
      self.affiche_ordre=1
      self.ajouteRadioButtons()

  def mouseDoubleClickEvent(self,event):
      #print self.editor.Classement_Commandes_Ds_Arbre
      #if self.editor.Classement_Commandes_Ds_Arbre!= () : self.chercheOu()
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
      
         

  def creeListeCommande(self,filtre):
      listeGroupes,dictGroupes=self.jdc.get_groups()
      sensibleALaCasse=self.RBCasse.isChecked()
      if "CACHE" in dictGroupes.keys():
         aExclure=dictGroupes["CACHE"]
      else:
         aExclure=()
      listeACreer=[]
      for l in self.jdc.get_liste_cmd():
         if l not in aExclure : 
            if sensibleALaCasse and (filtre != None and not filtre in l) : continue
            if (not sensibleALaCasse) and filtre != None and (not filtre in l) and (not filtre.upper() in l) : continue
            listeACreer.append(l)
      return listeACreer

  def ajouteRadioButtons(self):
      #print 'ds ajouteRadioButtons'
      filtre=str(self.LEFiltre.text())
      if filtre==str("") : filtre=None
      if hasattr(self,'buttonGroup') :
         for b in self.buttonGroup.buttons():
             self.buttonGroup.removeButton(b)
             b.setParent(None)
             b.close()
      else :
         self.buttonGroup = QButtonGroup()
      for w in self.listeWidget :
         w.setParent(None)
         w.close()
      self.listeWidget=[]
      if self.affiche_alpha==1 :
         liste=self.creeListeCommande(filtre)
         for cmd in liste :
           self.dicoCmd[tr(cmd)]=cmd
           rbcmd=(QRadioButton(tr(cmd)))
           self.buttonGroup.addButton(rbcmd)
           self.commandesLayout.addWidget(rbcmd)
           rbcmd.mouseDoubleClickEvent=self.mouseDoubleClickEvent
           if monEnvQT5:
              self.buttonGroup.buttonClicked.connect(self.rbClique) 
           else :
              self.connect(self.buttonGroup, SIGNAL("buttonClicked(QAbstractButton*)"),self.rbClique) 
      elif  self.affiche_groupe==1 :
         listeGroupes,dictGroupes=self.jdc.get_groups()
         for grp in listeGroupes:
           if grp == "CACHE" : continue
           label=QLabel(self)
           if monEnvQT5 :
              text=tr('<html><head/><body><p><span style=\" font-weight:600;\">Groupe : '+tr(grp)+'</span></p></body></html>')
           else :
              text=QString.fromUtf8('<html><head/><body><p><span style=\" font-weight:600;\">Groupe : '+tr(grp)+'</span></p></body></html>')
           label.setText(text)
           self.listeWidget.append(label)
           aAjouter=1
           sensibleALaCasse=self.RBCasse.isChecked()
           for cmd in  dictGroupes[grp]:
              if sensibleALaCasse and (filtre != None and not filtre in cmd) : continue
              if (not sensibleALaCasse) and filtre != None and (not filtre in cmd) and (not filtre.upper() in cmd) : continue
              if aAjouter == 1 :
                 self.commandesLayout.addWidget(label)
                 aAjouter=0
              self.dicoCmd[tr(cmd)]=cmd
              rbcmd=(QRadioButton(tr(cmd)))
              self.buttonGroup.addButton(rbcmd)
              self.commandesLayout.addWidget(rbcmd)
              rbcmd.mouseDoubleClickEvent=self.mouseDoubleClickEvent
              if monEnvQT5:
                 self.buttonGroup.buttonClicked.connect(self.rbClique) 
              else :
                  self.connect(self.buttonGroup, SIGNAL("buttonClicked(QAbstractButton*)"),self.rbClique)
           label2=QLabel(self)
           label2.setText(" ")
           self.listeWidget.append(label2)
           self.commandesLayout.addWidget(label2)
      elif  self.affiche_ordre==1 :
         listeFiltre=self.creeListeCommande(filtre)
         liste=[]
         if self.editor.Ordre_Des_Commandes == None : Ordre_Des_Commandes=listeFiltre
         else : Ordre_Des_Commandes=self.editor.Ordre_Des_Commandes
         for cmd in Ordre_Des_Commandes :
            if cmd in listeFiltre :
                 liste.append(cmd)
         for cmd in liste :
           self.dicoCmd[tr(cmd)]=cmd
           rbcmd=(QRadioButton(tr(cmd)))
           self.buttonGroup.addButton(rbcmd)
           self.commandesLayout.addWidget(rbcmd)
           rbcmd.mouseDoubleClickEvent=self.mouseDoubleClickEvent
           if monEnvQT5:
              self.buttonGroup.buttonClicked.connect(self.rbClique) 
           else :
              self.connect(self.buttonGroup, SIGNAL("buttonClicked(QAbstractButton*)"),self.rbClique)

     

  def clearFiltre(self):
      self.LEFiltre.setText("")
      self.ajouteRadioButtons()

  def rbClique(self,id):
      self.name=self.dicoCmd[str(id.text())]
      definitionEtape=getattr(self.jdc.cata[0],self.name)
      commentaire=getattr(definitionEtape,self.jdc.lang)
      try :
        commentaire=getattr(definitionEtape,self.jdc.lang)
      except :
        try :
           commentaire=getattr(definitionEtape,"ang")
        except :
           commentaire=""
      self.editor.affiche_commentaire(commentaire)



  def setValide(self):
      #PNPN a priori pas d icone mais peut-etre a faire
      pass
