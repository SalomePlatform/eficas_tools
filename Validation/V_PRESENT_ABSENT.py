
class PRESENT_ABSENT: 
   """
      La r�gle v�rifie que si le premier mot-cl� de self.mcs est present 
          parmi les elements de args les autres mots cl�s de self.mcs
           doivent etre absents

      Ces arguments sont transmis � la r�gle pour validation sous la forme 
      d'une liste de noms de mots-cl�s ou d'un dictionnaire dont 
      les cl�s sont des noms de mots-cl�s.
   """
   def verif(self,args):
      """
          La methode verif effectue la verification specifique � la r�gle.
          args peut etre un dictionnaire ou une liste. Les �l�ments de args
          sont soit les �l�ments de la liste soit les cl�s du dictionnaire.
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


