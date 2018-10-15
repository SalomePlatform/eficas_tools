# -*- coding: utf-8 -*-
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
from __future__ import absolute_import
try :
  from builtins import str
except :
  pass
import types,os
import traceback

from PyQt5.QtWidgets import QToolButton ,QWidget
from PyQt5.QtGui import QFont, QFontMetrics, QFontInfo, QPalette
from PyQt5.QtCore import Qt

from Extensions.i18n import tr

from .gereIcones import ContientIcones
from .gereIcones import FacultatifOuOptionnel
from .qtSaisie    import SaisieValeur

nomMax=230
# empirique les metrics ne fonctionnent pas 
# ---------------------------------------------------------------------- #
class Feuille(QWidget,ContientIcones,SaisieValeur,FacultatifOuOptionnel):
# --------------------------------------------------------------------- #


   def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
       #print ("Feuille", monSimpDef,nom,objSimp)
       QWidget.__init__(self,None)
       self.node=node
       self.node.fenetre=self

       # on se positionne pour les icones
       #os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__))))
       self.setupUi(self)
       self.prendLeFocus=0

       maPolice= QFont("Times", 10)
       self.setFont(maPolice)
       self.setFocusPolicy(Qt.StrongFocus)

       self.parentQt=parentQt
       self.editor=self.node.editor
       self.appliEficas=self.editor.appliEficas
       self.repIcon=self.appliEficas.repIcon
       self.monSimpDef=monSimpDef
       self.nom=nom
       self.objSimp=objSimp
       self.node.fenetre=self
       self.maCommande=commande

       self.aRedimensionner=0
       self.setSuggestion()
       self.setValeurs()
       self.setNom()
       self.setValide()
       self.setIconePoubelle()
       self.setIconesFichier()
       self.setIconesSalome()
       self.setIconesGenerales()
       self.setCommentaire()
       self.setZoneInfo()
     

   def setNom(self):
       self.debutToolTip=""
       nomTraduit=tr(self.objSimp.nom)
       #metrix= QFontMetrics(self.label.font())
       #maxLongueur = self.label.width() - 2
       #print ('______________________')
       #print (nomTraduit)
       #print (self.label.font().pixelSize())
       #longueur2 = metrix.boundingRect(nomTraduit).width()
       longueur=QFontMetrics(self.label.font()).width(nomTraduit)
       if longueur >= nomMax :
         nouveauNom=self.formate(nomTraduit)
         self.label.setText(nouveauNom)
       else :   
         self.label.setText(nomTraduit)
       #clidedText = metrics.elidedText(text, Qt.ElideRight, label.width());
       #if (clippedText != nomTraduit): self.label.setToolTip(nomTraduit)
       #self.label.setText(clippedText)

   #def agrandit(self):
       # inutile pour certains widgets
   #    if self.height() < 40 :
   #       self.setMinimumHeight(50)
   #       self.resize(self.width(),200)

   #def mousePressEvent(self, event):
     #print 'mousePressEvent'
     #import inspect
     #print (inspect.getmro(self.__class__))
     #self.__class__.mousePressEvent(self, event)


                                 
   def setValeurs(self):
      # print "passe dans setValeurs pour ", self.objSimp.nom
      # print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        pass

   def finCommentaire(self):
       return ""

   
   def finCommentaireListe(self):
        commentaire=""
        mc = self.node.item.get_definition()
        d_aides = { 'TXM' : 'chaines de caracteres',
                  'R'   : 'reels',
                  'I'   : 'entiers',
                  'C'   : 'complexes'}
        type = mc.type[0]
        if not type in d_aides :
           if mc.min == mc.max:
               commentaire=tr("Entrez ")+str(mc.min)+tr(" valeurs ")+'\n'
           else :
               if mc.max != "**" :
                  commentaire=tr("entre ")+str(mc.min)+tr(" et ")+str(mc.max)+tr(" valeurs ")+'\n'
               else :
                  commentaire=""
        else :
           if mc.min == mc.max:
               commentaire=tr("Entrez ")+str(mc.min)+" "+tr(d_aides[type])+'\n'
           elif mc.max == float('inf') :
               commentaire=tr("Entrez une liste de ") + tr(d_aides[type])+'\n'
           else :
               commentaire=tr("Entrez entre ")+"\n"+str(mc.min)+(" et  ")+str(mc.max) +" " +tr(d_aides[type])+'\n'
        aideval=self.node.item.aide()
        commentaire=commentaire +  tr(aideval)
        return str(commentaire)


   def setSuggestion(self):
      if self.monSimpDef.getSug() != None and self.monSimpDef.getSug() != "":
         suggere=str('<html><head/><body><p><span style=" font-size:8pt;">suggestion : ')+str(self.monSimpDef.getSug())+"</span></p></body></html>"
         if hasattr(self,'lineEditVal'): self.lineEditVal.setToolTip(suggere)

   def setCommentaire(self):
      c  = self.debutToolTip
      #if self.node.item.definition.validators : c+=self.node.item.definition.validators.aide()
      self.aide=c
      if self.objSimp.getFr() != None and self.objSimp.getFr() != "":
          #c2 = '<html><head/><body><p>'+c+self.objSimp.getFr().decode('latin-1','replace')+"</p></body></html>"
          c2 = '<html><head/><body><p>'+c+self.objSimp.getFr()
          #c2 = '<html><head/><body><p>'+c+self.objSimp.getFr()+"</p></body></html>"
          self.label.setToolTip(c2)
          #self.aide=self.objSimp.getFr().decode('latin-1','ignore')+" "+c
          self.aide=self.objSimp.getFr()+" "+c
      else :
         c+=self.finCommentaire()
         if c != "" and c != None :
            self.aide=c
            #c=str('<html><head/><body><p><span style=" font-size:8pt; ">')+c+"</span></p></body></html>"
            c=str('<html><head/><body><p>')+c+"</p></body></html>"
            self.label.setToolTip(c)
      if self.editor.maConfiguration.differencieSiDefaut :
            self.label.setToolTip('defaut : ' + tr(str(self.node.item.object.definition.defaut)))




   def showEvent(self, event):
      if self.prendLeFocus==1 :
         self.activateWindow()
         "il faut deriver le showEvent pour" , self.nom
         self.prendLeFocus=0
      QWidget.showEvent(self,event)

   def aideALaSaisie(self):
      mc = self.node.item.get_definition()
      mctype = mc.type[0]
      d_aides = { 'TXM' : tr(u"chaine de caracteres"),
                  'R'   : tr("reel"),
                  'I'   : tr("entier"),
                  'C'   : tr("complexe"),
                  'Matrice' : tr(u'Matrice'),
                  'Fichier' : tr(u'fichier'),
                  'FichierNoAbs' : tr(u'fichier existant'),
                  'Repertoire' : tr(u'repertoire')}

      if mc.min == mc.max: commentaire=tr("Entrez ")+" "+str(mc.min)+" "
      else :               commentaire=tr("Entrez entre ")+str(mc.min)+tr(" et ")+str(mc.max)

      try :
         if issubclass(mctype,object) : ctype = getattr(mctype, 'help_message', tr("Type de base inconnu"))
         else : ctype = d_aides.get(mctype, tr("Type de base inconnu"))
      except:                        
         ctype = d_aides.get(mctype, tr("Type de base inconnu"))
      if ctype == tr("Type de base inconnu") and "Tuple" in str(mctype): ctype=str(mctype)

      commentaire+=ctype
      if mc.max!=1 : commentaire+="s" 
      return commentaire

   def setZoneInfo(self):
      # info=str(self.nom)+'  '
      # if self.monSimpDef.getFr() != None and self.monSimpDef.getFr() != "": info+=self.monSimpDef.getSug() +" "
      # if self.monSimpDef.getSug() != None and self.monSimpDef.getSug() != "": info+="Valeur suggeree : "self.monSimpDef.getSug()
      pass

   def reaffiche(self):

      if self.editor.jdc.aReafficher==True :
         self.parentQt.reaffiche()

         #PN PN PN pas satisfaisant
         #nodeAVoir=self.parentQt.node.chercheNoeudCorrespondant(self.objSimp)
         #print nodeAVoir.fenetre
         #print "nodeAVoir.fenetre.isVisible()", nodeAVoir.fenetre.isVisible()
         #if nodeAVoir.fenetre.isVisible() : return
         #self.editor.fenetreCentraleAffichee.rendVisibleNoeud(nodeAVoir)
         #nodeAVoir.fenetre.setFocus()
         # return  # on est bien postionne

         if self.objSimp.isValid() and hasattr(self, 'AAfficher'):
            nodeAVoir=self.parentQt.node.chercheNoeudCorrespondant(self.objSimp)
            try :
               index=self.editor.fenetreCentraleAffichee.listeAffichageWidget.index(nodeAVoir.fenetre.AAfficher)
               if (index==len(self.editor.fenetreCentraleAffichee.listeAffichageWidget)-1) :
                  try :
                     nodeAVoir.fenetre.setValeursApresBouton()
                  except :
                     pass
               else :
                  self.editor.fenetreCentraleAffichee.afficheSuivant(nodeAVoir.fenetre.AAfficher)
            except :
               pass
      else :
         if self.objSimp.isValid() and hasattr(self, 'AAfficher'):
            try :
               self.setValeursApresBouton()
            except :
               pass
            self.editor.fenetreCentraleAffichee.afficheSuivant(self.AAfficher)
         else :
            if hasattr(self, 'AAfficher'): self.AAfficher.setFocus(7)

   def reaffichePourDeplier(self):
      self.parentQt.reaffiche()

   def rendVisible(self):
       pass

   #def enterEvent(self,event):
   #   print "je passe dans enterEvent", self.nom
   #   QWidget.enterEvent(self,event)

   def traiteClicSurLabel(self,texte):
       #aide=self.aide.encode('latin-1', 'ignore').decode('latin-1')+"\n"+self.aideALaSaisie().encode('latin-1', 'ignore').decode('latin-1')
       try :
          aide=self.aide+"\n"+self.aideALaSaisie()
       except :
          aide=self.aideALaSaisie()
       self.editor.afficheCommentaire(aide)

   def formate(self,t):
       l=len(t)//2
       newText=t[0:l]+'-\n'+t[l:]
       return newText
      

 
