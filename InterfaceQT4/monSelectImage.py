# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
# Modules Python
# Modules Eficas

from desImage import Ui_DSelImage
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DSelImage(Ui_DSelImage,QDialog):
   def __init__(self,parent ,modal ) :
       QDialog.__init__(self,parent)
       self.setupUi(self)

class MonImage (QWidget):
  def __init__(self,file,parent):
       QWidget.__init__(self,parent)
       self.file=file
       self.QtParent=parent
       self.monRectangle=None
       self.dessine=0
       self.readImage()
       

  def readImage(self):
        if self.file == "" : return
        self.image=QPixmap(self.file)

  def paintEvent(self,paintEvent):
        self.p= QPainter(self);
        self.resize(self.image.width(),self.image.height())
        if self.monRectangle != None:
           self.p.eraseRect(self.monRectangle)
        self.p.drawPixmap(0,0,self.image.width(),self.image.height(),self.image)
        if self.dessine==1:
           self.monRectangle=QRect(QPoint(self.xdeb,self.ydeb),QPoint(self.xfin,self.yfin))
           self.p.drawRect(self.monRectangle)

  def changedEvent(self,e):
      QWidget.changedEvent(self,e)

  def mousePressEvent(self,e):
      self.xdeb=e.x()
      self.ydeb=e.y()
      self.dessine=0
      self.update()
      QWidget.mousePressEvent(self,e)
      
  def mouseMoveEvent(self,e):
      self.xfin=e.x()
      self.yfin=e.y()
      self.dessine=1
      self.update()
      QWidget.mouseMoveEvent(self,e)

class MonSelectImage(DSelImage):
  """
  """
  def __init__(self,file,parent,name = None,fl = 0):
        DSelImage.__init__(self,parent,0)
        self.file=file 
        self.parentQT=parent
        self.image=MonImage(self.file,self)
        

  def accept(self) :
        if (not hasattr(self.image,'xdeb')) :self.close()
        name='RECT'
        self.parentQT.editor.init_modif()
        child=self.parentQT.node.append_brother(name)
        child.item.set_valeur((self.image.xdeb,self.image.ydeb,self.image.xfin,self.image.yfin))
        child.affichePanneau()
        self.close()
