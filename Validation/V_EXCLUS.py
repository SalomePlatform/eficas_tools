
class EXCLUS:
   """
      La règle vérifie qu'un seul mot-clé de self.mcs est present 
          parmi les elements de args.

      Ces arguments sont transmis à la règle pour validation sous la forme 
      d'une liste de noms de mots-clés ou d'un dictionnaire dont 
      les clés sont des noms de mots-clés.
   """
   def verif(self,args):
      """
          La methode verif effectue la verification specifique à la règle.
          args peut etre un dictionnaire ou une liste. Les éléments de args
          sont soit les éléments de la liste soit les clés du dictionnaire.
      """
      #  on compte le nombre de mots cles presents
      text =''
      count=0
      args = self.liste_to_dico(args)
      for mc in self.mcs:
        if args.has_key(mc):count=count+1
      if count > 1:
          text= "- Il ne faut qu un mot cle parmi : "+`self.mcs`+'\n'
          return text,0
      return text,1


