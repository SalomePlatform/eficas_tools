"""
   Ce module contient la classe mixin qui porte les méthodes
   pour traiter les niveaux au sein d'un JDC
"""
import etape_niveau

class JDC:
  def __init__(self):
    self.dict_niveaux={}
    self.build_niveaux()

  def build_niveaux(self):
    for niveau in self.definition.l_niveaux:
      etape_niv = etape_niveau.ETAPE_NIVEAU(niveau,self)
      self.etapes_niveaux.append(etape_niv)
      self.dict_niveaux[niveau.nom]=etape_niv
      self.dict_niveaux.update(etape_niv.dict_niveaux)

