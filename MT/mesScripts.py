def view_zone(listeparam) :
    item=listeparam[0]
    import visu_geom
    visu_zone = visu_geom.VisuGeom(from_eficas=True,
                          eficas_item=item,
                          ligne_arbre=False)
    visu_zone.visualize()

def view_ligne_arbre(listeparam) :
    item=listeparam[0]
    import visu_geom
    visu_arbre = visu_geom.VisuGeom(from_eficas=True,
                           eficas_item=item,
                           ligne_arbre=True)
    visu_arbre.visualize()

def import_zone(listeparam):
    
    from PyQt4.QtGui import QFileDialog

    # selection fichier
    fn = QFileDialog.getOpenFileName()
    if not fn : return
    FichieraTraduire=str(fn)

    # lancement traduction
    import traduire_catalogue_zone
    tr=traduire_catalogue_zone.TraductionZone(file1=FichieraTraduire)
    result,texte=tr.traduireZone()
    

    if result==True :
         txt="sansnom="+texte
         editor=listeparam[0]
         itemWidget=listeparam[1]
         editor.updateJdc(itemWidget,txt)

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
	'LIGNE_ARBRE':((view_ligne_arbre,"View",('item',),False,True,"affiche dans Geom la representation de la ligne d'arbre"),),
 	'ZONE':(
               (view_zone,"View",('item',),False,True,"affiche dans Geom la representation de la zone "),
               (import_zone,"import_zone",('editor','self'),False,False,"import de fichier zone"),)
               }
