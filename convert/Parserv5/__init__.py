try:
   import mx.TextTools
   import sys
   sys.modules['TextTools']=mx.TextTools
except:
   # Le package mx n'est pas installé. On essaie d'importer
   # directement TextTools au cas ou
   try:
      import TextTools
   except:
      # Aucun des deux packages n'est installé
      print """ Le package mx.TextTools ou TextTools doit etre
   installé pour pouvoir relire des fichiers de commandes 
   au format Aster V5
   voir : http://www.lemburg.com/python/mxExtensions.html
   """
