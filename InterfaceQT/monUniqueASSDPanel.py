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
import string,types,os

# Modules Eficas
import prefs 

from qt import *

from desUniqueASSD import DUnASSD
from qtCommun      import QTPanel
from qtSaisie      import SaisieValeur
from politiquesValidation import PolitiqueUnique

# Import des panels

class MonUniqueASSDPanel(DUnASSD,QTPanel,SaisieValeur):
  """
  Classe définissant le panel associé aux mots-clés qui demandent
  à l'utilisateur de choisir une seule valeur parmi une liste de valeurs
  discrètes
  """
  def __init__(self,node, parent = None,name = None,fl = 0):
        self.editor=parent
        QTPanel.__init__(self,node,parent)
        DUnASSD.__init__(self,parent,name,fl)
        self.politique=PolitiqueUnique(node,parent)
        self.InitListBoxASSD()
        self.InitCommentaire()

  def BOkPressed(self):
        self.ClicASSD()

  def BSupPressed(self):
        QTPanel.BSupPressed(self)

  def ViewDoc(self):
      QTPanel.ViewDoc(self)

  def InitCommentaire(self): 
      mc = self.node.item.get_definition()
      try :
          type = mc.type[0].__name__
      except :
          type = str(mc.type[0])
      if len(mc.type)>1 :
          for typ in mc.type[1:] :
            try :
                l=typ.__name__
            except:
                l=str(typ)
            type = type + ' ou '+l
      commentaire="Un objet de type "+type+" est attendu"
      aideval=self.node.item.aide()
      commentaire=commentaire +"\n"+ aideval
      self.Commentaire.setText(QString(commentaire))
