#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
    Ce module contient la classe Formatage qui permet le formatage d'une 
    liste de chaines de caractères dans une syntaxe représentative d'un
    jeu de commandes en un texte présentable
"""
import types,string

class Formatage :
  """ 
     Cette classe contient toutes les méthodes nécessaires au formatage
     de la chaine de caracteres issue d'un generator en un fichier
     'lisible' ie avec indentations
  """
  def __init__(self,l_jdc,code=None,mode=None,sep='=',l_max=72):
    # l_jdc représente le jeu de commandes brut sous forme de liste
    self.l_jdc = l_jdc
    self.jdc_fini =''
    self.count = 0
    self.sep=sep
    self.l_max=l_max
    if mode == '.py':
       self.sep = '='
       self.l_max = 132 
    elif code == 'ASTER':
       self.sep = ':'
       self.l_max = 72

  def formate_jdc(self):
    for etape in self.l_jdc:
      self.count = self.count+1
      self.texte_etape = ''
      if type(etape)==types.ListType:
        self.indent=[]
        self.indent.append(len(etape[0]))
        self.indent_courant = self.indent[0]
        self.texte_etape = '\n' + etape[0]
        if len(etape)>1 :
          self.formate_etape(etape[1:])
      else :
        self.indent=[]
        self.texte_etape = etape
      self.jdc_fini = self.jdc_fini + '\n' + self.texte_etape
    return self.jdc_fini

  def formate_etape(self,liste):
    ind = 0
    for element in liste :
      if type(element) == types.ListType:
        # il s'agit d'un mot-clé facteur
        # on écrit son nom
        longueur = self.longueur(self.texte_etape)
        try:
          increment = len(('\n'+self.indent_courant*' ')*ind + element[0])
        except:
          print 'ERREUR'
          print liste
          print element
        self.texte_etape = self.texte_etape + ('\n'+self.indent_courant*' ')*ind + element[0]
        length = len(self.indent)
        self.indent.insert(length,self.indent[length-1]+len(element[0]))
        self.indent_courant = self.indent[length]
        # on écrit ses fils
        self.formate_etape(element[1:])
      elif type(element) == types.StringType:
        # il s'agit d'un mot-clé simple ou de ')' ou ');' ou '),'
        if element == ')' or element == '),':
          self.texte_etape = self.texte_etape + string.strip(element)
          length = len(self.indent)
          if length > 1:
            last = self.indent[length-1]
            self.indent.remove(last)
            self.indent_courant=self.indent[length-2]
          else :
            self.indent_courant=self.indent[0]
        elif element == ');':
          length = len(self.indent)
          if length > 1:
            last = self.indent[length-1]
            self.indent.remove(last)
            self.indent_courant=self.indent[length-2]
          else :
            self.indent_courant=self.indent[0]
          self.texte_etape = self.texte_etape + string.strip(element)
        else :
          longueur = self.longueur(self.texte_etape)
          increment = len(('\n'+self.indent_courant*' ')*ind + string.strip(element))
          #self.jdc_fini = self.jdc_fini + ('\n'+self.indent_courant*' ')*ind + string.strip(element)
          if ((1-ind)*longueur+increment)  <= self.l_max :
            self.texte_etape = self.texte_etape + ('\n'+self.indent_courant*' ')*ind + string.strip(element)
          else :
            # il faut couper ...
            nom,valeur = string.split(element,self.sep,1)
            chaine = self.creer_chaine(nom,valeur,'\n'+self.indent_courant*' ',ind)+','
            #self.jdc_fini = self.jdc_fini + ('\n'+self.indent_courant*' ')*ind + string.strip(element)
            self.texte_etape = self.texte_etape + chaine
      ind = 1
      
  def longueur(self,texte):
    """ 
       texte est une string qui peut contenir des retours chariots
       Cette méthode retourne la longueur de la dernière ligne de texte 
    """
    liste = string.split(texte,'\n')
    return len(liste[-1])

  def creer_chaine(self,nom,valeur,increment,ind):
    s=''
    if len(increment + nom + self.sep) <= self.l_max:
      texte = increment*ind
      label = nom + self.sep
      s=texte + label
      longueur = len(increment + label)
      if len(string.split(valeur,'(')) == 1:
        # il s'agit d'une vraie chaîne de caractères
        val = len(valeur)
        texte = (self.l_max-2-val)*' '+valeur
        s=s+'\n'+texte
      else :
        # il s'agit d'une liste
        liste = string.split(valeur,',')
        i=0
        for arg in liste :
          ajout = string.strip(arg)
          if len(ajout) == 0 : continue
          longueur = self.longueur(texte = (texte + label)) + len(ajout +',') + (1-i)*len(increment)
          if longueur  <= self.l_max:
              if ajout[-1] != ')':
                texte = texte + ajout +','
              else :
                texte = texte + ajout
          else :
            i=1
            if ajout[-1] != ')':
              texte = texte  + increment + (len(label)+2)*' ' + ajout +','
            else :
              texte = texte  + increment + (len(label)+2)*' ' + ajout
      s=s+texte
    return s

