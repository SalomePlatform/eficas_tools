import types
class Tuple:
    def __init__(self,ntuple):
        self.ntuple=ntuple

    def __convert__(self,valeur):
        try:
            if isinstance(valeur, basestring) : return None
        except NameError:
            if isinstance(valeur, str): return None
        if len(valeur) != self.ntuple: return None
        return valeur

    def info(self):
        return "Tuple de %s elements" % self.ntuple
