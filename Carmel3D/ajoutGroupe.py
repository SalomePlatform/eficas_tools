# -*- coding: utf-8 -*-

#------------------------------------#
def handleAjoutGroupFiltre(listeGroup):
#-------------------------------------#
        """CARMEL3D : obtention des groupes de maille du maillage sélectionné dans Salomé
    Les groupes de mailles sont filtrés en utilisant une liste des  prefixes autorisés pour code Code_Carmel3D,
    i.e. un nom de groupe de mailles est DIEL_toto_foo par exemple, qui deviendra toto_foo.
    La création du MESH_GROUPE est typé (matériau ou source), d'après le préfixe.
    ATTENTION! Le nom devenant un concept, i.e. une variable Python, certains signes sont interdits dans le nom du groupe,
    e.g. les signes moins (-), plus (+), etc. Une erreur est retournée en ce cas.
        """

        return ('a','b'), ('c','d') 
        from string import join
        debug = True
        listePrefixesMateriaux = ('DIEL', 'NOCOND','COND', 'ZS', 'ZJ', 'NILMAT') # liste des préfixes pour les matériaux
        listePrefixesSources = ('CURRENT', 'EPORT', 'HPORT') # liste des préfixes pour les sources
        listePrefixes = listePrefixesMateriaux + listePrefixesSources # liste de tous les préfixes autorisés
        listePrefixesGroupesMultiples = ('CURRENT', ) # listes des préfixes autorisés pour groupes multiples, i.e. plusieurs groupes de mailles associés en une seule caractéistique matériau ou source
        sep = '_' # séparateur entre le préfixe et le nom réel du groupe (qui peut lui aussi contenir ce séparateur)
        dictGroupesMultiplesNomsPossibles = {} # dictionnaire contenant les noms réels possibles de groupes multiples et leur occurence dans la liste, i.e. 1 par défaut et > 1 pour une groupe multiple, e.g. pour un inducteur bobiné en plusieurs morceaux CURRENT_toto_1, CURRENT_toto_2, ce dictionnaire contiendra 'toto':2 
        listeGroupesMultiples = [] # liste contenant les noms possibles de groupes multiples, e.g. pour un inducteur bobiné en plusieurs morceaux CURRENT_toto_1, CURRENT_toto_2, cette liste contiendra 'toto'
        for groupe in listeGroup:
            partiesGroupe = groupe.split(sep) # parties du nom, séparées initialement par le séparateur du préfixe, e.g. 'CURRENT_toto_foo' devient ['CURRENT','toto','foo'] et 'toto' devient ['toto']
            prefix = partiesGroupe[0] # préfixe possible de ce nom, ou nom lui-meme
            if len(partiesGroupe) >= 2 and prefix in listePrefixesGroupesMultiples: # préfixe existant et autorisé
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
        # retourne le dernier élément du JdC, ou None si le JdC est vide, afin de savoir à quelle place ajouter les MESH_GROUPE (en dernier)
        try:
            dernier=self.tree.racine.children[-1]
        except:
            dernier=None
        for groupe in listeGroup: # parcours de la liste de tous les groupes de maille trouvés (volumiques et les autres)
            if debug: print 'groupe=', groupe
            partiesGroupe = groupe.split(sep) # parties du nom, séparées initialement par le séparateur du préfixe, e.g. 'CURRENT_toto_foo' devient ['CURRENT','toto','foo'] et 'toto' devient ['toto']
            prefix = partiesGroupe[0] # préfixe possible de ce nom, ou nom lui-meme
            if len(partiesGroupe) == 1: # pas de préfixe
                print u"ERREUR: ce nom de groupe ("+groupe+") ne peut pas être utilisé car il n'a pas de préfixe"
            elif len(partiesGroupe) >= 2 and prefix in listePrefixes: # préfixe existant et autorisé
                nomReel = None # initialisation du nom réel, qui provoquera une erreur par la suite (evaluation de None=None) s'il reste ainsi
                if prefix in listePrefixesGroupesMultiples: # ce groupe pourrait faire partie d'un groupe multiple
                    nomGroupeMultiple = partiesGroupe[1] # nom possible d'un groupe multiple
                    if nomGroupeMultiple in listeGroupesMultiples: # ce groupe est multiple et n'a pas encore été créé
                        nomReel = nomGroupeMultiple # ce groupe pourrait être utilisé...
                        listeGroupesMultiples.remove(nomGroupeMultiple) #... une seule fois
                        if debug: print u"ce nom de groupe ("+nomReel+") est multiple et sera utilisé une fois seulement"
                    elif dictGroupesMultiplesNomsPossibles[nomGroupeMultiple] == 1: # ce groupe existe dans le dictionnaire et n'est pas multiple (occurence =1)
                        nomReel = join(partiesGroupe[1:], sep) # reconstruction du nom réel, i.e. sans le préfixe
                        if debug: print u"ce nom de groupe ("+nomReel+") n'est pas multiple et sera utilisé"
                    else: # ce groupe est multiple et a déjà été utilisé
                        if debug: print u"ce nom de groupe ("+groupe+") est multiple et a déjà été utilisé"
                else: # ce groupe n'est pas multiple, il pourrait être utilisé tel quel
                    nomReel = join(partiesGroupe[1:], sep) # reconstruction du nom réel, i.e. sans le préfixe
                if nomReel is not None: # on a un nom de groupe possible, il faut réaliser des tests plus poussés
                    try: # test de conformité du nom pour un concept, i.e. une variable Python
                        exec(nomReel+'=None') # le test consiste à tenter de créer une variable, initialisée à None, à partir du nom, e.g. toto=None est bon mais toto-foo=None ne fonctionne pas.
                        # création du groupe MESH_GROUPE
                        if dernier != None:
                            new_node = dernier.append_brother("MESHGROUP",'after')
                        else:
                            new_node=self.tree.racine.append_child("MESHGROUP",pos='first')
                        test,mess = new_node.item.nomme_sd(nomReel) # précision du nom (de concept) du groupe
                        if debug: print u"ce nom de groupe ("+nomReel+") est utilisé..."
                        if prefix in listePrefixesMateriaux: # ce groupe est associé à un matériau
                            new_node.append_child('MATERIAL') # on rajoute la propriété de matériau, qu'il suffit d'associer ensuite à la liste des matériaux présents
                            if debug: print u" et c'est un matériau."
                        elif prefix in listePrefixesSources: # ce groupe est associé à une source
                            new_node.append_child('SOURCE') # on rajoute la propriété de la source, qu'il suffit d'associer ensuite à la liste des sources présentes
                            if debug: print u" et c'est une source."
                        else: # ce cas ne devrait pas se produire
                            pass
                        dernier=new_node # mise à jour du dernier noeud du JdC, afin de rajouter les autres MESH_GROUPE éventuels à sa suite
                    except:
                        print u"ERREUR: ce nom de groupe ("+nomReel+") ne peut pas être utilisé car il ne peut pas servir de concept à cause de caractères interdits, e.g. signes moins (-), plus (+), etc."
                else: # ce nom de groupe est écarté car le groupe multiple  déjà été créé
                        print u"Ce nom de groupe ("+groupe+") ne peut pas être utilisé car il appartient à un groupe multiple qui a déjà été créé."
            else: # préfixe existant mais non autorisé
                print u"ERREUR: ce nom de groupe ("+groupe+") ne peut pas être utilisé car son préfixe ("+partiesGroupe[0]+") n'est pas dans la liste autorisée "+str(listePrefixes)

