_root=None
_cata=None
debug=0

def set_current_step(step):
   """
      Fonction qui permet de changer la valeur de l'étape courante
   """
   global _root
   if _root : raise "Impossible d'affecter _root. Il devrait valoir None"
   _root=step

def get_current_step():
   """
      Fonction qui permet d'obtenir la valeur de l'étape courante
   """
   return _root

def unset_current_step():
   """
      Fonction qui permet de remettre à None l'étape courante
   """
   global _root
   _root=None

def set_current_cata(cata):
   """
      Fonction qui permet de changer l'objet catalogue courant
   """
   global _cata
   if _cata : raise "Impossible d'affecter _cata. Il devrait valoir None"
   _cata=cata

def get_current_cata():
   """
      Fonction qui retourne l'objet catalogue courant
   """
   return _cata

def unset_current_cata():
   """
      Fonction qui permet de remettre à None le catalogue courant
   """
   global _cata
   _cata=None

