"""
"""

import I_REGLE

class EXCLUS(I_REGLE.REGLE):
  def purge_liste(self,liste_a_purger,liste_mc_presents):
     regle_active=0
     for mc_present in liste_mc_presents:
        if mc_present in self.mcs:
           regle_active=1
           break
     if not regle_active : return liste_a_purger

     for mc in self.mcs:
        if mc in liste_a_purger:
           liste_a_purger.remove(mc)
     return liste_a_purger

