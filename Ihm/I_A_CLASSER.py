"""
"""

import string

import I_REGLE

class A_CLASSER(I_REGLE.REGLE):
  def gettext(self):
    text = 'R�gle ' + self.__class__.__name__+ ' :\n'
    t="  D'abord :\n"+' '*8
    for arg in self.args0:
      t=t+string.strip(arg)+' ou '
    text = text + t[0:-4] +'\n'
    t = "  Ensuite :\n"+' '*8
    for arg in self.args1:
      t=t+string.strip(arg)+' ou '
    text = text + t[0:-4] +'\n'
    return text

  def init_couples_permis(self):
    """ 
       Cr�e la liste des couples permis parmi les self.args, 
       c�d pour chaque �l�ment de self.args0 cr�e tous les couples possibles 
       avec un �l�ment de self.args1
    """
    liste = []
    for arg0 in self.args0:
      for arg1 in self.args1:
        liste.append((arg0,arg1))
    self.liste_couples = liste

