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
