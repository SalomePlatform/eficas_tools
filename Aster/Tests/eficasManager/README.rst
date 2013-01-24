
Méthode rapide pour créer un nouveau catalogue dans Eficas
==========================================================
(gboulant - 23/03/2012)

On dispose d'un catalogue ``mycata.py``::

 from Accas import * 
 
 JdC = JDC_CATA (code = 'DEMO_AUS20120329',
                 execmodul = None,
                 )
 S_TEST02_PARAM=PROC(nom='S_TEST02_PARAM',op=None,
	v=SIMP(typ='TXM',fr='',ang='',statut='o',docu='',into=['1', '2'],min=1,max=1,val_min='**',val_max='**',defaut=None),
 )
 S_TEST02_DATA=PROC(nom='S_TEST02_DATA',op=None,
	y=SIMP(typ='R',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
 	x=SIMP(typ='R',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
 	z=SIMP(typ='I',fr='',ang='',statut='o',docu='',into=None,min=1,max=1,val_min='**',val_max='**',defaut=None),
 )

Pour que Eficas se lance avec ce catalogue:

* Aujourd'hui, la conception impose que le fichier catalogue
  ``mycata.py`` soit préalablement enregistré dans le dictionnaire des
  catalogues d'Eficas (pour être tout à fait précis, il faut le
  déclarer dans la liste des catalogues associées à un CODE, par
  exemple Code_Aster).
* Pour Code_Aster, cela se fait en ajoutant le tuple suivant à la
  liste ``catalogues`` définies dans le fichier de préférence
  prefs_ASTER.py::

  ('ASTER','STA11','cataSTA11.py','python','defaut')

* Le catalogue est caractérisé par un mot clé identifiant ("STA11"
  dans l'exemple ci-dessus), que l'on peut utiliser pour y faire
  référence lorsque l'on souhaite lancer Eficas avec ce catalogue (au
  moyen de l'option ``-c``::

  $ <eficasroot>/Aster/qtEficas_Aster.py -c STA11

* On ne fait pas directement référence au fichier, mais à
  l'identifiant qui est associé au fichier dans la liste des
  catalogues d'eficas

Méthode pour créer un nouveau catalogue de manière dynamique
============================================================

Nécessite une évolution de prefs_ASTER: fonction addCatalog qui crée
le tuple à partir du couple (id,path) et qui l'ajoute au catalogue
ASTER. On peut alors s'en servir depuis un lanceur spécifique::

  import prefs
  import prefs_ASTER
  prefs_ASTER.addCatalog(catalogName="demo", catalogPath="mycata.py")
  
  from InterfaceQT4 import eficas_go
  eficas_go.lance_eficas(code=prefs.code)

Pour simplifier on crée un module ``eficasManager`` qui sait ajouter un
catalogue puis lancer Eficas.
