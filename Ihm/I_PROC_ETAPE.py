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
import I_ETAPE


# import rajout�s suite � l'ajout de Build_sd --> � r�sorber
import traceback,types
import Noyau
from Noyau import N_Exception
from Noyau.N_Exception import AsException
# fin import � r�sorber

class PROC_ETAPE(I_ETAPE.ETAPE):
   def get_sdname(self):
      return ""

   def get_sdprods(self,nom_sd):
      """ 
         Fonction : retourne le concept produit par l etape de nom nom_sd
                    s il existe sinon None
         Une PROC ne produit aucun concept
      """
      return None

   def delete_concept(self,sd):
      """
          Inputs :
             sd=concept detruit
          Fonction :
             Mettre a jour les mots cles de l etape 
             suite � la disparition du concept sd
             Seuls les mots cles simples MCSIMP font un traitement autre
             que de transmettre aux fils
      """
      for child in self.mc_liste :
        child.delete_concept(sd)

   def Build_sd(self):
      """
          Cette methode applique la fonction op_init au contexte du parent
          et lance l'ex�cution en cas de traitement commande par commande
          Elle doit retourner le concept produit qui pour une PROC est toujours None
          En cas d'erreur, elle leve une exception : AsException ou EOFError
      """
      if not self.isactif():return
      try:
         if self.parent:
            if type(self.definition.op_init) == types.FunctionType: 
               apply(self.definition.op_init,(self,self.parent.g_context))
         else:
            pass
         if self.jdc.par_lot == "NON" :
            self.Execute()
      except AsException,e:
        raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                              'fichier : ',self.appel[1],e)
      except EOFError:
        self.reset_current_step()
        raise
      except :
        l=traceback.format_exception(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
        raise AsException("Etape ",self.nom,'ligne : ',self.appel[0],
                          'fichier : ',self.appel[1]+'\n',
                          string.join(l))
