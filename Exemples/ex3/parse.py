
from ConfigParser import ConfigParser

class MyConfParser(ConfigParser):
   def getdicttext(self):
      s='{'
      for section in self.sections():
         s=s+ "'" + section + "' : {"
         options=self.options(section)
         for option in options:
            value=self.get(section,option)
            s=s+"'%s' : %s," % (option, value)
         s=s+"}, "
      s=s+"}"
      return s

   def getdict(self):
      return eval(self.getdicttext())
         
if __name__ == '__main__':
   p=MyConfParser()
   p.read("toto.ini")
   print p.getdicttext()
   print p.getdict()
