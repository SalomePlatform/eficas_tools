""" 
   Ce module contient la classe AsException
"""

# Modules Python
import types

class AsException(Exception):
  def __str__(self):
    if not self.args:
      return ''
    elif len(self.args) == 1:
      return str(self.args[0])
    else:
      s=''
      for e in self.args:
        if type(e) == types.StringType: s=s+ ' ' + e
        else:s=s+ ' ' + str(e)
      return s

