import I_ETAPE
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
             suite à la disparition du concept sd
             Seuls les mots cles simples MCSIMP font un traitement autre
             que de transmettre aux fils
      """
      for child in self.mc_liste :
        child.delete_concept(sd)

