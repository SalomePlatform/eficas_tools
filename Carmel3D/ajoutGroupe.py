# -*- coding: iso-8859-1 -*-

def handleAjoutGroupFiltre(editor,listeGroup):
        """CARMEL3D : obtention des groupes de maille du maillage selectionne dans Salome
        Les groupes de mailles sont filtres en utilisant une liste des  prefixes autorises pour code Code_Carmel3D,
        i.e. un nom de groupe de mailles est DIEL_toto_foo par exemple, qui deviendra toto_foo.
        La creation du MESH_GROUPE est type (materiau ou source), d'après le prefixe.
        ATTENTION! Le nom devenant un concept, i.e. une variable Python, certains signes sont interdits dans le nom du groupe,
        e.g. les signes moins (-), plus (+), etc. Une erreur est retournee en ce cas.
        """
        from string import join
        debug = True
        listePrefixesMateriaux = ('DIEL', 'NOCOND','COND', 'ZS', 'ZJ', 'NILMAT') # liste des prefixes pour les materiaux
        listePrefixesSources = ('CURRENT', 'EPORT', 'HPORT') # liste des prefixes pour les sources
        listePrefixes = listePrefixesMateriaux + listePrefixesSources # liste de tous les prefixes autorises
        listePrefixesGroupesMultiples = ('CURRENT', ) # listes des prefixes autorises pour groupes multiples, i.e. plusieurs groupes de mailles associes en une seule caracteistique materiau ou source
        sep = '_' # separateur entre le prefixe et le nom reel du groupe (qui peut lui aussi contenir ce separateur)
        dictGroupesMultiplesNomsPossibles = {} # dictionnaire contenant les noms reels possibles de groupes multiples et leur occurence dans la liste, i.e. 1 par defaut et > 1 pour une groupe multiple, e.g. pour un inducteur bobine en plusieurs morceaux CURRENT_toto_1, CURRENT_toto_2, ce dictionnaire contiendra 'toto':2 
        listeGroupesMultiples = [] # liste contenant les noms possibles de groupes multiples, e.g. pour un inducteur bobine en plusieurs morceaux CURRENT_toto_1, CURRENT_toto_2, cette liste contiendra 'toto'
        for groupe in listeGroup:
            partiesGroupe = groupe.split(sep) # parties du nom, separees initialement par le separateur du prefixe, e.g. 'CURRENT_toto_foo' devient ['CURRENT','toto','foo'] et 'toto' devient ['toto']
            prefix = partiesGroupe[0] # prefixe possible de ce nom, ou nom lui-meme
            if len(partiesGroupe) >= 2 and prefix in listePrefixesGroupesMultiples: # prefixe existant et autorise
                nomGroupeMultiple = partiesGroupe[1] # nom possible d'un groupe multiple
                if dictGroupesMultiplesNomsPossibles.has_key(nomGroupeMultiple): # comptage du nombre d'occurrences de ce nom de groupe multiple possible
                    dictGroupesMultiplesNomsPossibles[nomGroupeMultiple] += 1
                else:
                    dictGroupesMultiplesNomsPossibles[nomGroupeMultiple] = 1
        for nom in dictGroupesMultiplesNomsPossibles: # suppression des noms avec une seule occurence, i.e. ils ne sont pas des groupes multiples
            if dictGroupesMultiplesNomsPossibles[nom] > 1: listeGroupesMultiples.append(nom)
        if debug:
            print "listeGroup=", listeGroup
            print "dictGroupesMultiplesNomPossibles=", dictGroupesMultiplesNomsPossibles
            print "listeGroupesMultiples=", listeGroupesMultiples
            print "listePrefixes=", listePrefixes
        # retourne le dernier element du JdC, ou None si le JdC est vide, afin de savoir a quelle place ajouter les MESH_GROUPE (en dernier)
        try:
            dernier=editor.tree.racine.children[-1]
        except:
            dernier=None
        for groupe in listeGroup: # parcours de la liste de tous les groupes de maille trouves (volumiques et les autres)
            if debug: print 'groupe=', groupe
            partiesGroupe = groupe.split(sep) # parties du nom, separees initialement par le separateur du prefixe, e.g. 'CURRENT_toto_foo' devient ['CURRENT','toto','foo'] et 'toto' devient ['toto']
            prefix = partiesGroupe[0] # prefixe possible de ce nom, ou nom lui-meme
            if len(partiesGroupe) == 1: # pas de prefixe
                print u"ERREUR: ce nom de groupe ("+groupe+") ne peut pas etre utilise car il n'a pas de prefixe"
            elif len(partiesGroupe) >= 2 and prefix in listePrefixes: # prefixe existant et autorise
                nomReel = None # initialisation du nom reel, qui provoquera une erreur par la suite (evaluation de None=None) s'il reste ainsi
                if prefix in listePrefixesGroupesMultiples: # ce groupe pourrait faire partie d'un groupe multiple
                    nomGroupeMultiple = partiesGroupe[1] # nom possible d'un groupe multiple
                    if nomGroupeMultiple in listeGroupesMultiples: # ce groupe est multiple et n'a pas encore ete cree
                        nomReel = nomGroupeMultiple # ce groupe pourrait etre utilise...
                        listeGroupesMultiples.remove(nomGroupeMultiple) #... une seule fois
                        if debug: print u"ce nom de groupe ("+nomReel+") est multiple et sera utilise une fois seulement"
                    elif dictGroupesMultiplesNomsPossibles[nomGroupeMultiple] == 1: # ce groupe existe dans le dictionnaire et n'est pas multiple (occurence =1)
                        nomReel = join(partiesGroupe[1:], sep) # reconstruction du nom reel, i.e. sans le prefixe
                        if debug: print u"ce nom de groupe ("+nomReel+") n'est pas multiple et sera utilise"
                    else: # ce groupe est multiple et a deja ete utilise
                        if debug: print u"ce nom de groupe ("+groupe+") est multiple et a deja ete utilise"
                else: # ce groupe n'est pas multiple, il pourrait etre utilise tel quel
                    nomReel = join(partiesGroupe[1:], sep) # reconstruction du nom reel, i.e. sans le prefixe
                if nomReel is not None: # on a un nom de groupe possible, il faut realiser des tests plus pousses
                    try: # test de conformite du nom pour un concept, i.e. une variable Python
                        exec(nomReel+'=None') # le test consiste a tenter de creer une variable, initialisee a None, a partir du nom, e.g. toto=None est bon mais toto-foo=None ne fonctionne pas.
                        # creation du groupe MESH_GROUPE
                        if dernier != None:
                            new_node = dernier.append_brother("MESHGROUP",'after')
                        else:
                            new_node=editor.tree.racine.append_child("MESHGROUP",pos='first')
                        test,mess = new_node.item.nomme_sd(nomReel) # precision du nom (de concept) du groupe
                        if debug: print u"ce nom de groupe ("+nomReel+") est utilise..."
                        if prefix in listePrefixesMateriaux: # ce groupe est associe a un materiau
                            new_node.append_child('MATERIAL') # on rajoute la propriete de materiau, qu'il suffit d'associer ensuite a la liste des materiaux presents
                            if debug: print u" et c'est un materiau."
                        elif prefix in listePrefixesSources: # ce groupe est associe a une source
                            new_node.append_child('SOURCE') # on rajoute la propriete de la source, qu'il suffit d'associer ensuite a la liste des sources presentes
                            if debug: print u" et c'est une source."
                        else: # ce cas ne devrait pas se produire
                            pass
                        dernier=new_node # mise a jour du dernier noeud du JdC, afin de rajouter les autres MESH_GROUPE eventuels a sa suite
                    except:
                        print u"ERREUR: ce nom de groupe ("+nomReel+") ne peut pas etre utilise car il ne peut pas servir de concept a cause de caractères interdits, e.g. signes moins (-), plus (+), etc."
                else: # ce nom de groupe est ecarte car le groupe multiple  deja ete cree
                        print u"Ce nom de groupe ("+groupe+") ne peut pas etre utilise car il appartient a un groupe multiple qui a deja ete cree."
            else: # prefixe existant mais non autorise
                print u"ERREUR: ce nom de groupe ("+groupe+") ne peut pas etre utilise car son prefixe ("+partiesGroupe[0]+") n'est pas dans la liste autorisee "+str(listePrefixes)

