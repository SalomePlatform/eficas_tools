def inverseDico(dicoSource) :
#---------------------------
    dicoInverse = {}
    for (clef,valeur) in dicoSource.items():
        if not(type(valeur) is tuple):
           dicoInverse[valeur]=clef
           continue
        (elt,att)=valeur
        if elt not in dicoInverse : dicoInverse[elt]={}
        dicoInverse[elt][att]=clef
    return dicoInverse
     
dictSIMPEficasXML= { 'typ'        : 'typeAttendu',
                     'statut'     : 'statut', 
                     'min'        : 'minOccurences',
                     'max'        : 'maxOccurences', 
                     'homo'       : 'homo'       , 
                     'position'   : 'portee', 
                     'validators' : 'validators' , 
                     'sug'        : 'valeurSugg',
                     'defaut'     : 'valeurDef' , 
                     'into'       : ('plageValeur','into'), 
                     'val_min'    : ('plageValeur','borneInf'), 
                     'val_max'    : ('plageValeur','borneSup'),
                     'ang'        : ('doc','ang'), 
                     'fr'         : ('doc','fr',),
                     'docu'       : ('doc','docu'),
                   }

dictSIMPXMLEficas= inverseDico(dictSIMPEficasXML)

 

dictFACTEficasXML = { 'statut'     : 'statut', 
                      'min'        : 'minOccurences',
                      'max'        : 'maxOccurences', 
                      'ang'        : ('doc','ang'), 
                      'fr'         : ('doc','fr',),
                      'docu'       : ('doc','docu'),
                      'validators' : 'validators' ,
                    }

dictFACTXMLEficas =  inverseDico(dictFACTEficasXML)

dictPROCEficasXML =  { 'nom'        : 'nom',
                       'regles'     : 'regles',
                       'ang'        : ('doc','ang'), 
                       'fr'         : ('doc','fr',),
                       'docu'       : ('doc','docu'),
                      }
     #                  'UIinfo' : 'UIinfo'
     #                  'reentrant'
     #                  'repetable'
     #                  'op_init'
     #                  'fenetreIhm' : 'fenetreIhm'

dictPROCXMLEficas = inverseDico(dictPROCEficasXML)

listeParamDeTypeTypeAttendu = ( 'defaut', 'sug', 'val_min', 'val_max', 'into')
listeParamDeTypeStr         = ('fr', 'docu', 'ang', 'nom' )
dicoPourCast                = { 'I' : int, 'R' : float }

listeParamTjsEnListe        = ('into')
listeParamEnListeSiMax      = ('defaut', 'into', 'sug') 

if __name__ == "__main__":
   import pprint
   pp=pprint.PrettyPrinter(indent=4)
   print ('dictSIMPEficasXML')
   pp.pprint(dictSIMPEficasXML)
   print ('\n\n')
   print ('dictSIMPXMLEficas')
   pp.pprint(dictSIMPXMLEficas)
   print ('\n\n')
   print ('dictFACTEficasXML')
   pp.pprint(dictFACTEficasXML)
   print ('\n\n')
   print ('dictFACTXMLEficas')
   pp.pprint(dictFACTXMLEficas)
   print ('\n\n')
   print ('dictPROCEficasXML')
   pp.pprint(dictPROCEficasXML)
   print ('\n\n')
   print ('dictPROCXMLEficas')
   pp.pprint(dictPROCXMLEficas)
