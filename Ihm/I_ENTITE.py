class ENTITE:
  def get_docu(self):
    if hasattr(self,'docu') :
      if self.docu != "" : return self.docu
      else:
        if hasattr(self,'pere'):
          return self.pere.get_docu()
        else:
          return None
    else:
      return None

