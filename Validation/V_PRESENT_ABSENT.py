
class PRESENT_ABSENT: 
   """
      La règle vérifie que si le premier mot-clé de self.mcs est present 
          parmi les elements de args les autres mots clés de self.mcs
           doivent etre absents

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
      #  on verifie que si le premier de la liste est present, 
      #   les autres sont absents
      text=''
      test = 1
      args = self.liste_to_dico(args)
      mc0=self.mcs[0]
      if args.has_key(mc0):
        for mc in self.mcs[1:len(self.mcs)]:
          if args.has_key(mc):
            text = text + "- Le mot cle "+`mc0`+" etant present, il faut que : "+\
                 mc+" soit absent"+'\n'
            test = 0
      return text,test


