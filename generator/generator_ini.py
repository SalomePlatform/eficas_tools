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
    Ce module contient le plugin generateur de fichier
    au format ini pour EFICAS.


"""
import traceback
import types,string

from Noyau import N_CR
from Accas import MCSIMP,MCFACT

def entryPoint():
   """
       Retourne les informations n�cessaires pour le chargeur de plugins
       Ces informations sont retourn�es dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'ini',
        # La factory pour cr�er une instance du plugin
          'factory' : IniGenerator,
          }


class IniGenerator:
   """
       Ce generateur parcourt un objet de type MCFACT et produit
       un fichier au format ini 
       L'acquisition et le parcours sont r�alis�s par le m�thode
       generator.gener(objet_mcfact)
       L'�criture du fichier au format ini par appel de la m�thode
       generator.writefile(nom_fichier)

       Ses caract�ristiques principales sont expos�es dans des attributs 
       de classe :

       - extensions : qui donne une liste d'extensions de fichier pr�conis�es

   """
   # Les extensions de fichier pr�conis�es
   extensions=('.ini','.conf')

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR generateur format ini',
                         fin='fin CR format ini')
      # Le texte au format ini est stock� dans l'attribut text
      self.text=''

   def writefile(self,filename):
      fp=open(filename,'w')
      fp.write(self.text)
      fp.close()

   def gener(self,obj):
      """
         Tous les mots-cl�s simples du niveau haut sont mis dans la section DEFAUT
         Tous les mots-cl�s facteurs sont convertis en sections
         Un mot-cl� facteur ne peut contenir que des mots-cl�s simples. Sinon => erreur
      """
      liste_mcfact=[]
      sect_defaut=''
      for mocle in obj.mc_liste:
         if isinstance(mocle,MCFACT):
            liste_mcfact.append(self.generMCFACT(mocle))
         elif isinstance(mocle,MCSIMP):
            sect_defaut=sect_defaut+self.generMCSIMP(mocle)
         else:
            self.cr.fatal("Entite inconnue ou interdite : "+`mocle`)
      self.text=''
      if sect_defaut != '':
         self.text="[DEFAULT]\n"+sect_defaut
      self.text=self.text + string.join(liste_mcfact,'\n')
      return self.text

   def generMCFACT(self,obj):
      """
         Cette m�thode convertit un mot-cl� facteur ne contenant que des mots-cl�s
         simples en une chaine de caract�res
      """
      sect_text='[%s]\n' % obj.nom
      for mocle in obj.mc_liste:
         if isinstance(mocle,MCSIMP):
            sect_text=sect_text+self.generMCSIMP(mocle)
         else:
            self.cr.fatal("Entite inconnue ou interdite : "+`mocle`+" Elle est ignor�e")
      return sect_text

   def generMCSIMP(self,obj):
      """
         Cette m�thode convertit un mot-cl� simple en une chaine de caract�res
         au format ini
      """
      s=''
      if type(obj.valeur) == types.TupleType :
         self.cr.fatal("Les tuples ne sont pas support�s pour le format ini : "+ obj.nom)
         s="%s = %s\n" % (obj.nom,"ERREUR")
      else :
         try:
            s="%s = %s\n" % (obj.nom,obj.valeur)
         except Exception,e :
            self.cr.fatal("Type de valeur non support� par le format ini : "+ obj.nom + '\n'+str(e))
            s="%s = %s\n" % (obj.nom,"ERREUR")
      return s

