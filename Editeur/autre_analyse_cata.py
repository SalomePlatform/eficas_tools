def traite_entite(entite):
   """
       Cette fonction ajoute a l'objet entite un attribut de nom ordre_mc
       qui est une liste contenant le nom des sous entites dans l'ordre 
       de leur apparition dans le catalogue.
       L'ordre d'apparition dans le catalogue est donné par l'attribut _no
       de l'entite
       La fonction active le meme type de traitement pour les sous entites
       de entite
   """
   l=[]
   for k,v in entite.entites.items():
      traite_entite(v)
      l.append((v._no,k))
   l.sort()
   entite.ordre_mc=[ item for index, item in l ]

def analyse_catalogue(cata):
   """
      Cette fonction analyse le catalogue cata pour construire avec l'aide
      de traite_entite la structure de données ordre_mc qui donne l'ordre
      d'apparition des mots clés dans le catalogue
   """
   cata_ordonne_dico={}
   for oper in cata.JdC.commandes:
       traite_entite(oper)
       cata_ordonne_dico[oper.nom]=oper
   return cata_ordonne_dico


