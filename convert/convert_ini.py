"""
    Ce module contient le plugin convertisseur de fichier
    au format ini pour EFICAS.
    Le convertisseur supporte le format de sortie eval

    Le format eval est un texte Python qui peut etre 
    evalu� avec la commande eval de Python. Il doit donc 
    etre une expression Python dont l'�valuation permet d'obtenir un objet

"""
import traceback

from ConfigParser import ConfigParser
from Noyau import N_CR

def entryPoint():
   """
       Retourne les informations n�cessaires pour le chargeur de plugins
       Ces informations sont retourn�es dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'ini',
        # La factory pour cr�er une instance du plugin
          'factory' : IniParser,
          }


class IniParser(ConfigParser):
   """
       Ce convertisseur lit un fichier au format ini avec la 
       methode readfile : convertisseur.readfile(nom_fichier)
       et retourne le texte au format outformat avec la 
       methode convertisseur.convert(outformat)

       Ses caract�ristiques principales sont expos�es dans 2 attributs 
       de classe :

       - extensions : qui donne une liste d'extensions de fichier pr�conis�es

       - formats : qui donne une liste de formats de sortie support�s
   """
   # Les extensions de fichier pr�conis�es
   extensions=('.ini','.conf')
   # Les formats de sortie support�s (eval ou exec)
   formats=('eval','dict')

   def __init__(self,cr=None):
      ConfigParser.__init__(self)
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR convertisseur format ini',
                         fin='fin CR format ini')

   def readfile(self,filename):
      try:
         self.read(filename)
      except Exception,e:
         self.cr.fatal(str(e))

   def convert(self,outformat):
      if outformat == 'eval':
         return self.getdicttext()
      elif outformat == 'dict':
         return self.getdict()
      else:
         raise "Format de sortie : %s, non support�"

   def getdicttext(self):
      s='{'
      for section in self.sections():
         s=s+ "'" + section + "' : {"
         options=self.options(section)
         for option in options:
            value=self.get(section,option)
            if value == '':value="None"
            s=s+"'%s' : %s," % (option, value)
         s=s+"}, "
      s=s+"}"
      return s

   def getdict(self):
      s={}
      for section in self.sections():
         s[section]=d={}
         options=self.options(section)
         for option in options:
            value=self.get(section,option)
            if value == '':
               d[option]=None
            else:
               d[option]=eval(value)
      return s

