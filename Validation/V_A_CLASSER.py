
import types

class A_CLASSER:
   """
      La r�gle A_CLASSER v�rifie que ...

   """
   def __init__(self,*args):
      if len(args) > 2 :
        print "Erreur � la cr�ation de la r�gle A_CLASSER(",args,")"
        return
      self.args=args
      if type(args[0]) == types.TupleType:
        self.args0 = args[0]
      elif type(args[0]) == types.StringType:
        self.args0 = (args[0],)
      else :
        print "Le premier argument de :",args," doit �tre un tuple ou une string"
      if type(args[1]) == types.TupleType:
        self.args1 = args[1]
      elif type(args[1]) == types.StringType:
        self.args1 = (args[1],)
      else :
        print "Le deuxi�me argument de :",args," doit �tre un tuple ou une string"
      # cr�ation de la liste des mcs
      liste = []
      for arg0 in self.args0:
        liste.append(arg0)
      for arg1 in self.args1:
        liste.append(arg1)
      self.mcs = liste
      self.init_couples_permis()

   def init_couples_permis(self):
      """ Cr�e la liste des couples permis parmi les self.args, c�d pour chaque �l�ment
          de self.args0 cr�e tous les couples possibles avec un �l�ment de self.args1"""
      liste = []
      for arg0 in self.args0:
        for arg1 in self.args1:
          liste.append((arg0,arg1))
      self.liste_couples = liste

   def verif(self,args):
      """

          args peut etre un dictionnaire ou une liste. Les �l�ments de args
          sont soit les �l�ments de la liste soit les cl�s du dictionnaire.
      """
      # cr�ation de la liste des couples pr�sents dans le fichier de commandes
      l_couples = []
      couple = []
      text = ''
      test = 1
      for nom in args:
        if nom in self.mcs :
          couple.append(nom)
          if len(couple) == 2 :
            l_couples.append(tuple(couple))
            couple=[]
            if nom not in self.args1:
              couple.append(nom)
      if len(couple) > 0 :
        l_couples.append(tuple(couple))
      # l_couples peut �tre vide si l'on n'a pas r�ussi � trouver au moins un
      # �l�ment de self.mcs
      if len(l_couples) == 0 :
        message = "- Il faut qu'au moins un objet de la liste : "+`self.args0`+\
                  " soit suivi d'au moins un objet de la liste : "+`self.args1`
        return message,0
      # A ce stade, on a trouv� des couples : il faut v�rifier qu'ils sont
      # tous licites
      num = 0
      for couple in l_couples :
        num = num+1
        if len(couple) == 1 :
          # on a un 'faux' couple
          if couple[0] not in self.args1:
            text = text+"- L'objet : "+couple[0]+" doit �tre suivi d'un objet de la liste : "+\
                   `self.args1`+'\n'
            test = 0
          else :
            if num > 1 :
              # ce n'est pas le seul couple --> licite
              break
            else :
              text = text+"- L'objet : "+couple[0]+" doit �tre pr�c�d� d'un objet de la liste : "+\
                   `self.args0`+'\n'
              test = 0
        elif couple not in self.liste_couples :
          text = text+"- L'objet : "+couple[0]+" ne peut �tre suivi de : "+couple[1]+'\n'
          test = 0
      return text,test

