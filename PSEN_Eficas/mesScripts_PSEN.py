def exportToCsv(editor,cmd) :
    #from PyQt4.QtGui import QFileDialog
    # selection fichier
    #fn = QFileDialog.getOpenFileName()
    #if not fn : return
    #FichieraTraduire=str(fn)
    print "je suis la"
    print editor
    print cmd

def importFromCsv(editor,cmd) :
    print "et ici"

# le dictionnaire des commandes a la structure suivante :
# la clef est la commande qui va proposer l action
# puis un tuple qui contient
#	- la fonction a appeler
#       - le label dans le menu du clic droit
#	- un tuple contenant les parametres attendus par la fonction
#	- appelable depuis Salome uniquement -)
#	- appelable depuis un item valide uniquement 
#	- toolTip
dict_commandes={
   'N_1_GENERATORS':( 
           (exportToCsv,"exportToCsv",('editor','self'),False,False,"export values to cvs File"),
           (importFromToCsv,"importFromToCsv",('editor','self'),False,False,"import values from cvs File"),
                    )
               }
