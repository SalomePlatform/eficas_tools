"""
   Ce module contient des modifications mineures du comportement
   du noyau ou de validation
"""
import string

if 1:
   # Modification de la fonction justify_text de Noyau.N_CR
   separateurs=(' ',',','/')
   def split(ligne,cesure):
       ligne= string.rstrip(ligne)
       if len(ligne) <= cesure : 
          return ligne
       else:
          coupure=cesure
          while ligne[coupure] not in separateurs and coupure > 0:
             coupure = coupure - 1
          if coupure == 0:
             # Il faut augmenter la cesure
             coupure =cesure
             while ligne[coupure] not in separateurs and coupure < len(ligne)-1 :
                coupure = coupure + 1
          if coupure == len(ligne)-1:
             return ligne
          else:
             return ligne[:coupure+1]+ '\n' + split(ligne[coupure+1:],cesure)

   def justify_text(texte='',cesure=50):
       texte = string.strip(texte)
       liste_lignes = string.split(texte,'\n')
       l=[split(l,cesure) for l in liste_lignes]
       texte_justifie=string.join(l,'\n')
       return texte_justifie
   try:
      import Noyau.N_CR
      Noyau.N_CR.justify_text=justify_text
   except:
      pass

def encadre_message(texte,motif):
  """
     Retourne la chaine de caractères texte entourée d'un cadre formés
     d'éléments 'motif'
  """
  texte = justify_text(texte,cesure=80)
  lignes = string.split(texte,'\n')
  longueur = 0
  for ligne in lignes :
    if len(ligne)> longueur : longueur = len(ligne)
  longueur = longueur + 4
  txt = motif*longueur+'\n'
  for ligne in lignes :
    txt = txt + motif + ' '+ligne+' '*(longueur-len(motif+ligne)-2)+motif+'\n'
  txt = txt + motif*longueur+'\n'
  return txt

if __name__ == "__main__":
   print encadre_message(motif='!',
texte="""- Il faut au moins un mot-clé parmi : ('DEBUT', 'POURSUITE')     
- Il faut au moins un mot-clé parmi : ('FIN',)               
- Il faut qu'au moins un objet de la liste : ('DEBUT', 'POURSUITE') soit suivi d'au moins un objet de la liste : ('FIN',) 
ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,yyyyyyyyyyyyyyyy
""")



