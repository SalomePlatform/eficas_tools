
class ENSEMBLE:
   """
      La r�gle v�rifie que si un mot-cl� de self.mcs est present 
          parmi les elements de args tous les autres doivent etre presents.

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
              text = text + "- "+ pivot + " �tant pr�sent, "+mc+" doit �tre pr�sent"+'\n'
              test = 0
      return text,test



