
class ENSEMBLE:
   """
      La règle vérifie que si un mot-clé de self.mcs est present 
          parmi les elements de args tous les autres doivent etre presents.

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
      #  on compte le nombre de mots cles presents, il doit etre egal a la liste
      #  figurant dans la regle
      text = ''
      test = 1
      args = self.liste_to_dico(args)
      pivot = None
      for mc in self.mcs:
        if args.has_key(mc):
          pivot = mc
          break
      if pivot :
        for mc in self.mcs:
          if mc != pivot :
            if not args.has_key(mc):
              text = text + "- "+ pivot + " étant présent, "+mc+" doit être présent"+'\n'
              test = 0
      return text,test



