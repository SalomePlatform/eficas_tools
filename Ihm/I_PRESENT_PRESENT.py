"""
"""

import I_REGLE

class PRESENT_PRESENT(I_REGLE.REGLE):
  def verif_condition_regle(self,liste,l_mc_presents):
    mc0=self.mcs[0]
    for mc_present in l_mc_presents:
      if mc_present == mc0 :
        for mc in self.mcs[1:]:
          nb = l_mc_presents.count(mc)
          if nb == 0 : liste.append(mc)
        return liste
    return liste


