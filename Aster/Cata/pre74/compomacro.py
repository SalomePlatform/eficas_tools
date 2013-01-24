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
from Editeur import compomacro
import ongletpanel

#
__version__="$Name: V6_main $"
__Id__="$Id: compomacro.py,v 1.1 2004-11-19 09:06:24 eficas Exp $"
#

class MACROPanel(ongletpanel.OngletPanel,compomacro.MACROPanel) :
   """
   """
    
class MACROTreeItem(compomacro.MACROTreeItem):
  panel=MACROPanel

class INCLUDETreeItem(compomacro.INCLUDETreeItem):
  panel=MACROPanel

class INCLUDE_MATERIAUTreeItem(INCLUDETreeItem): 
  pass

class POURSUITETreeItem(INCLUDETreeItem): 
  pass

def treeitem(appli, labeltext, object, setfunction=None):
   if object.nom == "INCLUDE_MATERIAU":
      return INCLUDE_MATERIAUTreeItem(appli, labeltext, object, setfunction)
   elif object.nom == "INCLUDE":
      return INCLUDETreeItem(appli, labeltext, object, setfunction)
   elif object.nom == "POURSUITE":
      return POURSUITETreeItem(appli, labeltext, object, setfunction)
   else:
      return MACROTreeItem(appli, labeltext, object, setfunction)

import Accas
objet=Accas.MACRO_ETAPE

Accas.MACRO.itemeditor=MACROTreeItem

