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

