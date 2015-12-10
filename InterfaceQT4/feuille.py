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

nomMax=250
# ---------------------------------------------------------------------- #
class Feuille(QWidget,ContientIcones,SaisieValeur,FacultatifOuOptionnel):
# --------------------------------------------------------------------- #


   def __init__(self,node,monSimpDef,nom,objSimp,parentQt,commande):
       #print "Feuille", monSimpDef,nom,objSimp
       #print self
       QWidget.__init__(self,None)
       self.node=node
       self.node.fenetre=self

       # on se positionne pour les icones
       #os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__))))
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
       #if len(nomTraduit) >= nomMax :
       #  nom=nomTraduit[0:nomMax]+'...'
       #  self.label.setText(nomTraduit)
       #  self.debutToolTip=nomTraduit+"\n"
       longueur=QFontMetrics(self.label.font()).width(nomTraduit)
       if longueur >= nomMax :
         nouveauNom=self.formate(nomTraduit)
         self.label.setText(nouveauNom)
       else :   
         self.label.setText(nomTraduit)

   def agrandit(self):
       # inutile pour certains widgets
       if self.height() < 40 :
          self.setMinimumHeight(50)
          self.resize(self.width(),200)

                                 
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
        if not d_aides.has_key(type) :
           if mc.min == mc.max:
               commentaire=tr("Entrez ")+str(mc.min)+tr(" valeurs ")+'\n'
           else :
               commentaire=tr("Entrez entre ")+str(mc.min)+tr(" et ")+str(mc.max)+tr(" valeurs ")+'\n'
        else :
           if mc.min == mc.max:
               commentaire=tr("Entrez ")+str(mc.min)+" "+tr(d_aides[type])+'\n'
           else :
               commentaire=tr("Entrez entre ")+str(mc.min)+(" et  ")+str(mc.max) +" " +tr(d_aides[type])+'\n'
        aideval=self.node.item.aide()
        commentaire=commentaire +  QString.toUtf8(QString(aideval))
        self.monCommentaireLabel.setText(str(commentaire))
        return str(commentaire)


   def setSuggestion(self):
      if self.monSimpDef.get_sug() != None and self.monSimpDef.get_sug() != "":
         suggere=str('<html><head/><body><p><span style=" font-size:8pt;">suggestion : ')+str(self.monSimpDef.get_sug())+"</span></p></body></html>"
         if hasattr(self,'lineEditVal'): self.lineEditVal.setToolTip(suggere)

   def setCommentaire(self):
      c  = self.debutToolTip
      #if self.node.item.definition.validators : c+=self.node.item.definition.validators.aide()
      self.aide=c
      if self.objSimp.get_fr() != None and self.objSimp.get_fr() != "":
          c2 = '<html><head/><body><p>'+c+str(self.objSimp.get_fr())+"</p></body></html>"
          self.label.setToolTip(c2)
          self.aide=str(self.objSimp.get_fr())+" "+c
      else :
         c+=self.finCommentaire()
         if c != "" and c != None :
            self.aide=c
            #c=str('<html><head/><body><p><span style=" font-size:8pt; ">')+c+"</span></p></body></html>"
            c=str('<html><head/><body><p>')+c+"</p></body></html>"
            self.label.setToolTip(c)



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

      if type(mctype) == types.ClassType: ctype = getattr(mctype, 'help_message', tr("Type de base inconnu"))
      else:                               ctype = d_aides.get(mctype, tr("Type de base inconnu"))
      if ctype == tr("Type de base inconnu") and "Tuple" in str(mctype): ctype=str(mctype)

      commentaire+=ctype
      if mc.max!=1 : commentaire+="s" 
      return commentaire

   def setZoneInfo(self):
      # info=str(self.nom)+'  '
      # if self.monSimpDef.get_fr() != None and self.monSimpDef.get_fr() != "": info+=self.monSimpDef.get_sug() +" "
      # if self.monSimpDef.get_sug() != None and self.monSimpDef.get_sug() != "": info+="Valeur suggérée : "self.monSimpDef.get_sug()
      pass
      #self.editor.affiche_infos(info)

   def reaffiche(self):
      #print "dans reaffiche de feuille", self.nom
      if self.editor.jdc.aReafficher==True :
         #print " j appelle le reaffiche de parentQt"
         self.parentQt.reaffiche()

         #PN PN PN pas satisfaisant
         #nodeAVoir=self.parentQt.node.chercheNoeudCorrespondant(self.objSimp)
         #print nodeAVoir.fenetre
         #print "nodeAVoir.fenetre.isVisible()", nodeAVoir.fenetre.isVisible()
         #if nodeAVoir.fenetre.isVisible() : return
         #self.editor.fenetreCentraleAffichee.rendVisibleNoeud(nodeAVoir)
         #nodeAVoir.fenetre.setFocus()
         # return  # on est bien postionne

         if self.objSimp.isvalid() and hasattr(self, 'AAfficher'):
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
         if self.objSimp.isvalid() and hasattr(self, 'AAfficher'):
            try :
               self.setValeursApresBouton()
            except :
               self.editor.fenetreCentraleAffichee.afficheSuivant(self.AAfficher)
         else :
            if hasattr(self, 'AAfficher'): self.AAfficher.setFocus(7)

   def reaffichePourDeplier(self):
      self.parentQt.reaffiche()

   def rendVisible(self):
       #print "jjjjjjjjjjjjjjjjjjjjj"
       pass

   def traiteClicSurLabel(self,texte):
       #print self.aide 
       aide=self.aide+"\n"+self.aideALaSaisie()
       self.editor.affiche_commentaire(aide)

   def formate(self,t):
       if t.find('_')==0 :
          newText=t[0:19]+'\n'+t[19:]
       else:
          listeNom=t.split('_')
          newTexte=""
          ligne=""
          for n in listeNom:
            if len(ligne)+len(n) < 25 : 
               newTexte=newTexte+"_"+n
               ligne+="_"+n
            else :
               newTexte=newTexte+"\n_"+n
               ligne=""
          #newTexte=t[0:t.rfind('_')]+'\n'+ t[t.rfind('_'):]
          newText=newTexte[1:]
       return newText
      

 
