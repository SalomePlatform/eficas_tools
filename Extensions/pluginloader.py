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
"""
    Ce module contient le chargeur dynamique de plugins (emprunté à HappyDoc)
"""

import glob,os,sys,traceback
import UserDict

class PluginLoader(UserDict.UserDict):
   def __init__(self,module):
      UserDict.UserDict.__init__(self)
      self.plugin_dir=module.__path__[0]
      self.plugin_set_name=module.__name__
      _module_list = glob.glob( os.path.join( self.plugin_dir,
                              '%s*py' % self.plugin_set_name,
                                           )
                              )
      _module_list.sort()

      for _module_name in _module_list:

        _module_name = os.path.basename(_module_name)[:-3]
        _import_name = '%s.%s' % ( self.plugin_set_name,
                                   _module_name )

        try:
          _module = __import__( _import_name )
        except:
          sys.stderr.write('\n--- Plugin Module Error ---\n')
          traceback.print_exc()
          sys.stderr.write('---------------------------\n\n')
          continue
        try:
          _module = getattr(_module, _module_name)
        except AttributeError:
          sys.stderr.write('ERROR: Could not retrieve %s\n' % _import_name)

        try:
          info = _module.entryPoint()
        except AttributeError:
          pass
        else:
          self.addEntryPoint(info)


   def addEntryPoint(self,infoDict):
      name=infoDict['name']
      factory=infoDict['factory']
      self[name]=factory

