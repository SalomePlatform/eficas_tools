
class UN_PARMI:
   """
      La r�gle v�rifie que l'on trouve un des mots-cl�s
      de la r�gle parmi les arguments d'un OBJECT.

      Ces arguments sont transmis � la r�gle pour validation sous la forme 
      d'une liste de noms de mots-cl�s ou d'un dictionnaire dont 
      les cl�s sont des noms de mots-cl�s.
   """
   def verif(self,args):
      """
          La m�thode verif v�rifie que l'on trouve un des mos-cl�s
          de la liste self.mcs parmi les �l�ments de args

          args peut etre un dictionnaire ou une liste. Les �l�ments de args
          sont soit les �l�ments de la liste soit les cl�s du dictionnaire.
      """
      #  on compte le nombre de mots cles presents
      text =''
      count=0
      args = self.liste_to_dico(args)
      for mc in self.mcs:
        if args.has_key(mc):count=count+1
      if count != 1:
          text = "- Il ne faut qu'un mot-cl� parmi : "+`self.mcs`+'\n'
          return text,0
      return text,1

