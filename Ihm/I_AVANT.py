#@ MODIF V_AU_MOINS_UN Validation  DATE 14/09/2004   AUTEUR PNOYRET  
# -*- coding: iso-8859-1 -*-
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

import types


class I_AVANT:
   """
      La règle I_AVANT vérifie que l'on trouve l ordre  des mots-clés
      de la règle parmi les arguments d'un JDC.

      Ces arguments sont transmis à la règle pour validation sous la forme 
      d'une liste de noms de mots-clés ou d'un dictionnaire dont 
      les clés sont des noms de mots-clés.
   """

   def __init__(self,*args):
      if len(args) > 2 :
        print "Erreur à la création de la règle A_CLASSER(",args,")"
        return
      if type(args[0]) == types.TupleType:
	 self.listeAvant=args[0]
      else :
	 self.listeAvant=(args[0],)
      if type(args[1]) == types.TupleType:
	 self.listeApres=args[1]
      else :
	 self.listeApres=(args[1],)

   def verif(self,args):
      """
          args peut etre un dictionnaire ou une liste. Les éléments de args
          sont soit les éléments de la liste soit les clés du dictionnaire.
      """
      #  on compte le nombre de mots cles presents
      text =''
      boolListeAvant=0
      boolListeApres=0
      boolOK=1
      for nom in args:
	  if nom in self.listeAvant :
             boolListeAvant=1
	     if boolListeApres == 1 :
                boolOK = 0
          if nom in self.listeApres :
             boolListeApres=1
      if boolListeAvant == 0 and boolListeApres == 1 : boolOK = 0
      return text,boolOK


   def gettext(self):
       text = "Regle de classement "' :\n'
       for mc in self.listeAvant : 
           text = text + mc + ', '
       text = text  + " \nAvant : \n" 
       for mc in self.listeApres : 
           text = text + mc + ','
       return text

