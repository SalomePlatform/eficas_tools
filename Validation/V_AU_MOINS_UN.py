
class AU_MOINS_UN:
   """
      La règle AU_MOINS_UN vérifie que l'on trouve au moins un des mots-clés
      de la règle parmi les arguments d'un OBJECT.

      Ces arguments sont transmis à la règle pour validation sous la forme 
      d'une liste de noms de mots-clés ou d'un dictionnaire dont 
      les clés sont des noms de mots-clés.
   """
   def verif(self,args):
      """
          La méthode verif vérifie que l'on trouve au moins un des mos-clés
          de la liste self.mcs parmi les éléments de args

          args peut etre un dictionnaire ou une liste. Les éléments de args
          sont soit les éléments de la liste soit les clés du dictionnaire.
      """
      #  on compte le nombre de mots cles presents
      text =''
      count=0
      args = self.liste_to_dico(args)
      for mc in self.mcs:
        if args.has_key(mc):count=count+1
      if count == 0:
          text =  "- Il faut au moins un mot-clé parmi : "+`self.mcs`+'\n'
          return text,0
      return text,1

