# -*- coding: utf-8 -*-
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
import string,types,os
import traceback

from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Extensions.i18n import tr

from gereIcones import ContientIcones
from gereIcones import FacultatifOuOptionnel
from qtSaisie    import SaisieValeur

# ---------------------------------------------------------------------- #
class Feuille(QWidget,ContientIcones,SaisieValeur,FacultatifOuOptionnel):
# --------------------------------------------------------------------- #


   def __init__(self,node,monSimpDef,nom,objSimp,parentQt):
       #print "Feuille", monSimpDef,nom,objSimp
       QWidget.__init__(self,None)
       self.node=node
       self.node.fenetre=self
       self.setupUi(self)
       self.prendLeFocus=0

       maPolice= QFont("Times", 10)
       self.setFont(maPolice)

       self.parentQt=parentQt
       self.editor=self.node.editor
       self.appliEficas=self.editor.appliEficas
       self.repIcon=self.appliEficas.repIcon
       self.monSimpDef=monSimpDef
       self.nom=nom
       self.objSimp=objSimp
       self.node.fenetre=self

       self.aRedimensionner=0
       self.setSuggestion()
       self.setValeurs()
       self.setNom()
       self.setValide()
       self.setPoubelle()
       self.setIcones()
       self.setCommentaire()
       self.setZoneInfo()
          

   def setNom(self):
       self.debutToolTip=""
       if len(self.objSimp.nom) >= 17 :
         nom=self.objSimp.nom[0:15]+'...'
         self.label.setText(nom)
         self.debutToolTip=self.objSimp.nom+"\n"
       else :   
         self.label.setText(self.objSimp.nom)

                                 
   def setValeurs(self):
      # print "passe dans setValeurs pour ", self.objSimp.nom
      # print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        pass

   def finCommentaire(self):
       return ""

   def setSuggestion(self):
      if self.monSimpDef.get_sug() != None and self.monSimpDef.get_sug() != "":
         suggere=str('<html><head/><body><p><span style=" font-size:8pt;">suggestion : ')+str(self.monSimpDef.get_sug())+"</span></p></body></html>"
         if hasattr(self,'lineEditVal'): self.lineEditVal.setToolTip(suggere)

   def setCommentaire(self):
      #print "dans setCommentaire"
     
      c  = self.debutToolTip
      if self.objSimp.get_fr() != None and self.objSimp.get_fr() != "":
          c2 = '<html><head/><body><p><span style=" font-size:8pt;">'+c+str(self.objSimp.get_fr())+"</span></p></body></html>"
          self.label.setToolTip(c2)
      else :
         c+=self.finCommentaire()
         if c != "" and c != None :
            c=str('<html><head/><body><p><span style=" font-size:8pt; ">')+c+"</span></p></body></html>"
            self.label.setToolTip(c)

   def setIcones(self):

       mctype = self.monSimpDef.type[0]
       # selon 
       if ( hasattr(self,"BFichier")): 
          if mctype == "Repertoire":
             self.BRepertoire=self.BFichier
	     #icon = QIcon(self.repIcon+"/fichier.png")
             #self.BRepertoire.setIcon(icon)
             self.connect(self.BRepertoire,SIGNAL("clicked()"),self.BRepertoirePressed)
             #self.BVisuFichier.close()
          else :
	     #icon = QIcon(self.repIcon+"/visuFichier.png")
             #self.BVisuFichier.setIcon(icon)
             self.connect(self.BFichier,SIGNAL("clicked()"),self.BFichierPressed)
             self.connect(self.BVisuFichier,SIGNAL("clicked()"),self.BFichierVisu)
          return

       if ( hasattr(self,"BSalome")): 
          enable_salome_selection = self.editor.salome and \
              (('grma' in repr(mctype)) or ('grno' in repr(mctype)) or ('SalomeEntry' in repr(mctype)) or
               (hasattr(mctype, "enable_salome_selection") and mctype.enable_salome_selection))
          if  enable_salome_selection:
              self.connect(self.BSalome,SIGNAL("pressed()"),self.BSalomePressed)
              #icon = QIcon(self.repIcon+"/flecheSalome.png")
              #self.BSalome.setIcon(icon)

              if not(('grma' in repr(mctype)) or ('grno' in repr(mctype))) or not(self.editor.salome):
                self.BView2D.close()
              else :
	        #icon = QIcon(self.repIcon+"/salomeLoupe.png")
                #self.BView2D.setIcon(icon)
                self.connect(self.BView2D,SIGNAL("clicked()"),self.BView2DPressed)
          else:
              self.BSalome.close()
              self.BView2D.close()


   def showEvent(self, event):
      if self.prendLeFocus==1 :
         self.activateWindow()
         "il faut deriver le showEvent pour" , self.nom
         self.prendLeFocus=0
      QWidget.showEvent(self,event)

   def aideALaSaisie(self):
      return
      mc = self.node.item.get_definition()
      mctype = mc.type[0]
      d_aide = { 'TXM' : tr(u"chaine de caracteres"),
                  'R'   : tr("reel"),
                  'I'   : tr("entier"),
                  'C'   : tr("complexe"),
                  'Matrice' : tr(u'Matrice'),
                  'Fichier' : tr(u'fichier'),
                  'FichierNoAbs' : tr(u'fichier existant'),
                  'Repertoire' : tr(u'repertoire')}
      if mc.min == mc.max: commentaire=tr("Entrez ")+str(mc.min)
      else :               commentaire=tr("Entrez entre ")+str(mc.min)+tr(" et ")+str(mc.max)

      if type(mctype) == types.ClassType: ctype = getattr(mctype, 'help_message', tr("Type de base inconnu"))
      else:                               ctype = d_aides.get(mctype, tr("Type de base inconnu"))
      if ctype == tr("Type de base inconnu") and "Tuple" in str(mctype): ctype=str(mctype)

      commentaire+=ctype
      if self.max!=1 : commentaire+="s" 
      return commentaire

   def setZoneInfo(self):
      # info=str(self.nom)+'  '
      # if self.monSimpDef.get_fr() != None and self.monSimpDef.get_fr() != "": info+=self.monSimpDef.get_sug() +" "
      # if self.monSimpDef.get_sug() != None and self.monSimpDef.get_sug() != "": info+="Valeur suggérée : "self.monSimpDef.get_sug()
      pass
      #self.editor.affiche_infos(info)
