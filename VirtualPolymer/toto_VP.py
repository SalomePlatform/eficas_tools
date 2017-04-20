def model_saved(listeparam) :
    editor=listeparam[0]
    print (editor)
    print (editor.process_VP())

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
	'Equation':((model_saved,"model_saved",('editor','self'),False,True,""),),
               }
