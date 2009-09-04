# -*- coding: utf-8 -*-

"""
Ce module contient les classes permettant de définir les objets graphiques
représentant un objet de type FORMULE, cad le panneau et l'item de l'arbre
d'EFICAS
"""

import string
import compooper
import browser
import typeNode


class FormuleNode(browser.JDCNode,typeNode.PopUpMenuNode):
        
    def getPanel(self):
      
      from monFormulePanel import MonFormulePanel
      return MonFormulePanel(self,parent=self.editor)
        
   
    def createPopUpMenu(self):
      typeNode.PopUpMenuNode.createPopUpMenu(self)


    def doPaste(self,node_selected):
        """
            Déclenche la copie de l'objet item avec pour cible
            l'objet passé en argument : node_selected
        """
        objet_a_copier = self.item.get_copie_objet()
        child=node_selected.doPasteCommande(objet_a_copier)
        return child

            
class FORMULETreeItem(compooper.EtapeTreeItem):
    """
    Classe servant a définir l'item porté par le noeud de l'arbre d'EFICAS
    qui représente la FORMULE
    """
    itemNode=FormuleNode

    def init(self):
      self.setfunction = self.set_valeur

# ---------------------------------------------------------------------------
#                   API de FORMULE pour l'arbre 
# ---------------------------------------------------------------------------
    def GetSubList(self):
      """
      Retourne la liste des fils de self
      On considére que FORMULE n'a pas de fils
      --> modification par rapport a MACRO classique
      """
      # dans EFICAS on ne souhaite pas afficher les mots-clés fils de FORMULE
      # de façon traditionnelle
      return []

    def GetIconName(self):
      """
      Retourne le nom de l'icone à afficher dans l'arbre
      Ce nom dépend de la validité de l'objet
      """
      if self.object.isactif():
        self.object.state="modified"
        if self.object.isvalid():
          return "ast-green-square"
        else:
          return "ast-red-square"
      else:
        return "ast-white-text"

    def GetLabelText(self):
      """ Retourne 3 valeurs :
      - le texte a afficher dans le noeud représentant l'item
      - la fonte dans laquelle afficher ce texte
      - la couleur du texte
      """
      if self.object.isactif():
        # None --> fonte et couleur par défaut
        return self.labeltext,None,None
      else:
        return self.labeltext,None,None
        #return self.labeltext,fontes.standard_italique,None
    
# ---------------------------------------------------------------------------
#       Méthodes permettant la modification et la lecture des attributs
#       du paramètre = API graphique de la FORMULE pour Panel et EFICAS
# ---------------------------------------------------------------------------

    def get_nom(self):
      """
      Retourne le nom de la FORMULE
      """
      return self.object.get_nom()

    def get_type(self):
      """
      Retourne le type de la valeur retournée par la FORMULE
      """
      return self.object.type_retourne

    def get_args(self):
      """
      Retourne les arguments de la FORMULE
      """
      args=""
      for mot in self.object.mc_liste:
          if mot.nom == 'NOM_PARA':
             args=mot.valeur
             break
      if args :
          if args[0] == "(" and args[-1] ==")":
             args=args[1:-1]
          # transforme en tuple si ce n est pas déja le casa
          try :
             args=string.split(args,',')
          except :
             pass
      return args

    def get_corps(self):
      """
      Retourne le corps de la FORMULE
      """
      corps=""
      for mot in self.object.mc_liste:
          if mot.nom == 'VALE':
             corps=mot.valeur
             break
      return corps


    def get_liste_types_autorises(self):
      """
         Retourne la liste des types autorises pour les valeurs de sortie 
         d'une FORMULE
      """
      return self.object.l_types_autorises

    def save_formule(self,new_nom,new_typ,new_arg,new_exp):
      """
      Vérifie si (new_nom,new_typ,new_arg,new_exp) définit bien une FORMULE 
      licite :
          - si oui, stocke ces paramètres comme nouveaux paramètres de la 
            FORMULE courante et retourne 1
          - si non, laisse les paramètres anciens de la FORMULE inchangés et 
            retourne 0
      """
      test,erreur = self.object.verif_formule_python(formule=(new_nom,new_typ,new_arg,
                                                       new_exp))
      if test :
          # la formule est bien correcte : on sauve les nouveaux paramètres
          test=self.object.update_formule_python(formule=(new_nom,new_typ,new_exp,new_arg))
      return test,erreur

# ---------------------------------------------------------------------------
#          Accès aux méthodes de vérification de l'objet FORM_ETAPE
# ---------------------------------------------------------------------------

    def verif_nom(self,nom):
        """
        Lance la vérification du nom passé en argument
        """
        return self.object.verif_nom(nom)

    def verif_arguments(self,arguments):
        """
        Lance la vérification des arguments passés en argument
        """
        return self.object.verif_arguments('('+arguments+')')

    def verif_formule(self,formule):
        """
        Lance la vérification de FORMULE passée en argument
        """
        return self.object.verif_formule(formule=formule)


    def verif_formule_python(self,formule):
        """
        Lance la vérification de FORMULE passée en argument
        """
        return self.object.verif_formule_python(formule=formule)

import Accas
treeitem =FORMULETreeItem
objet = Accas.FORM_ETAPE
