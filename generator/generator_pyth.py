# -*- coding: utf-8 -*-
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
    Ce module contient le plugin generateur de fichier au format pyth pour EFICAS.


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
          'name' : 'pyth',
        # La factory pour cr�er une instance du plugin
          'factory' : PythGenerator,
          }


class PythGenerator:
   """
       Ce generateur parcourt un objet de type MCFACT et produit
       un fichier au format pyth

       L'acquisition et le parcours sont r�alis�s par la m�thode
       generator.gener(objet_mcfact)

       L'�criture du fichier au format ini par appel de la m�thode
       generator.writefile(nom_fichier)

       Ses caract�ristiques principales sont expos�es dans des attributs 
       de classe :
          - extensions : qui donne une liste d'extensions de fichier pr�conis�es

   """
   # Les extensions de fichier pr�conis�es
   extensions=('.py','.comm')

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR generateur format ini',
                         fin='fin CR format ini')
      # Le texte au format pyth est stock� dans l'attribut text
      self.text=''

   def writefile(self,filename):
      fp=open(filename,'w')
      fp.write(self.text)
      fp.close()

   def gener(self,obj,format='standard'):
      """
         Tous les mots-cl�s simples du niveau haut sont transform�s en variables 

         Tous les mots-cl�s facteurs sont convertis en dictionnaires

         Les mots-cl�s multiples ne sont pas trait�s
      """
      s=''
      for mocle in obj.mc_liste:
         if isinstance(mocle,MCFACT):
            valeur=self.generMCFACT(mocle)
            s=s+"%s = %s\n" % (mocle.nom,valeur)
         elif isinstance(v,MCSIMP):
            valeur = self.generMCSIMP(mocle)
            s=s+"%s = %s\n" % (mocle.nom,valeur)
         else:
            self.cr.fatal("Entite inconnue ou interdite : "+`mocle`)
      self.text=s
      return self.text

   def generMCFACT(self,obj):
      """
         Cette m�thode convertit un mot-cl� facteur 
         en une chaine de caract�res repr�sentative d'un dictionnaire
      """
      s = '{'
      for mocle in obj.mc_liste:
         if isinstance(mocle,MCSIMP):
            valeur = self.generMCSIMP(mocle)
            s=s+"'%s' : %s,\n" % (mocle.nom,valeur)
         elif isinstance(mocle,MCFACT):
            valeur=self.generMCFACT(mocle)
            s=s+"'%s' : %s,\n" % (mocle.nom,valeur)
         else:
            self.cr.fatal("Entite inconnue ou interdite : "+`mocle`+" Elle est ignor�e")
      s=s+'}'
      return s

   def generMCSIMP(self,obj):
      """
         Cette m�thode convertit un mot-cl� simple en une chaine de caract�res
         au format pyth
      """
      try:
         s="%s" % obj.valeur
      except Exception,e :
         self.cr.fatal("Type de valeur non support� par le format pyth : "+ obj.nom + '\n'+str(e))
         s="ERREUR"
      return s

