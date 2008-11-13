# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
# THIS PROGRAM IS FREE SOFTWARE; YOU CAN REDISTRIBUTE IT AND/OR MODIFY
# IT UNDER THE TERMS OF THE GNU GENERAL PUBLIC LICENSE AS PUBLISHED BY
# THE FREE SOFTWARE FOUNDATION; EITHER VERSION 2 OF THE LICENSE, OR
# (AT YOUR OPTION) ANY LATER VERSION.
#
# THIS PROGRAM IS DISTRIBUTED IN THE HOPE THAT IT WILL BE USEFUL, BUT
# WITHOUT ANY WARRANTY; WITHOUT EVEN THE IMPLIED WARRANTY OF
# MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. SEE THE GNU
# GENERAL PUBLIC LICENSE FOR MORE DETAILS.
#
# YOU SHOULD HAVE RECEIVED A COPY OF THE GNU GENERAL PUBLIC LICENSE
# ALONG WITH THIS PROGRAM; IF NOT, WRITE TO EDF R&D CODE_ASTER,
#    1 AVENUE DU GENERAL DE GAULLE, 92141 CLAMART CEDEX, FRANCE.
#
#
# ======================================================================
"""
   Ce module contient la classe JDCDISPLAY qui réalise l'affichage
   du jeu de commandes sous la forme d'un arbre et de panneaux qui portent
   les informations attachées au noeud de l'arbre sélectionné
"""
# Modules Python
import types,sys
import traceback
import Tkinter
import Pmw

# Modules Eficas
import panels
from treeitemincanvas import TREEITEMINCANVAS
from widgets import showinfo,showerror

class CONFIG:
   isdeveloppeur='NON'

class JDCDISPLAY:
   """
       Cette classe ajoute à la class TREEITEMINCANVAS l'affichage des infos
       attachées au noeud sélectionné dans un notebook
       L'objet item associé au jdc est créé par la classe TREEITEMINCANVAS
   """
   def __init__(self,jdc,nom_jdc,appli=None,parent=None):
      self.jdc=jdc
      self.nom_jdc=nom_jdc
      self.fichier=None
      self.panel_courant=None

      if not appli:
         class Appli:
            def __init__(self):
               self.CONFIGURATION=CONFIG()
            def affiche_infos(self,message):
               print message
               return

            def efface_aide(self,event):
               return

            def affiche_aide(self,event,aide):
               print aide
               return

         appli=Appli()
      self.appli=appli

      if not parent:
         parent=Tkinter.Tk()
         Pmw.initialise(parent)
      self.parent=parent
      self.node_selected = None
      self.modified='n'

      self.pane=Pmw.PanedWidget(self.parent,orient='horizontal')
      self.pane.add('treebrowser',min=0.4,size=0.5)
      self.pane.add('selected',min=0.4)
      self.pane.pack(expand=1,fill='both')
      self.tree=TREEITEMINCANVAS(jdc,nom_jdc,self.pane.pane('treebrowser'),
                 self.appli,self.select_node,self.make_rmenu)

   def make_rmenu(self,node,event):
      if hasattr(node.item,'rmenu_specs'):
         rmenu = Tkinter.Menu(self.pane.pane('treebrowser'), tearoff=0)
         #node.select()
         self.cree_menu(rmenu,node.item.rmenu_specs,node)
         rmenu.tk_popup(event.x_root,event.y_root)

   def cree_menu(self,menu,itemlist,node):
      """
            Ajoute les items du tuple itemlist
            dans le menu menu
      """
      number_item=0
      radio=None
      for item in itemlist:
         number_item=number_item + 1
         if not item :
            menu.add_separator()
         else:
            label,method=item
            if type(method) == types.TupleType:
                 # On a un tuple => on cree une cascade
                 menu_cascade=Tkinter.Menu(menu)
                 menu.add_cascade(label=label,menu=menu_cascade)
                 self.cree_menu(menu_cascade,method,node)
            elif method[0] == '&':
                 # On a une chaine avec & en tete => on cree un radiobouton
                 try:
                    command=getattr(node.item,method[1:])
                    menu.add_radiobutton(label=label,command=lambda a=self.appli,c=command,n=node:c(a,n))
                    if radio == None:radio=number_item
                 except:pass
            else:
                 try:
                    command=getattr(node.item,method)
                    menu.add_command(label=label,command=lambda a=self.appli,c=command,n=node:c(a,n))
                 except:pass
      # Si au moins un radiobouton existe on invoke le premier
      if radio:menu.invoke(radio)

   def select(self):
      return

   def unselect(self):
      return

   def select_node(self,node):
      """
          Cette méthode est appelée à chaque fois qu'un noeud est sélectionné
          dans l'arbre.
          Elle permet l'affichage du panneau correspondant au noeud sélectionné
      """
      if node is not self.node_selected :
         #ATTENTION: il faut affecter l'attribut node_selected avant d'appeler 
         # create_panel pour eviter une recursion infinie entre create_panel, 
         # Emit, onValid, select_node
         self.node_selected = node
         self.create_panel(node)
      elif self.panel_courant:
         self.panel_courant.update_panel()

   def create_panel(self,node):
      """
         Lance la génération du panneau contextuel de l'objet sélectionné 
         dans l'arbre
      """
      if self.panel_courant:
          # On detruit le panneau
          self.panel_courant.destroy()
          o=self.panel_courant
          self.panel_courant=None
          # Mettre à 1 pour verifier les cycles entre objets
          # pour les panneaux
          withCyclops=0
          if withCyclops:
             from Misc import Cyclops
             z = Cyclops.CycleFinder()
             z.register(o)
             del o
             z.find_cycles()
             z.show_stats()
             z.show_cycles()

      if node is None:
          self.panel_courant=None
          return self.panel_courant

      if node.item.isactif():
          if hasattr(node.item,"panel"):
              self.panel_courant=node.item.panel(self,self.pane.pane('selected'),node)
          else:
              raise Exception("Le noeud sélectionné n'a pas de panel associé")
      else:
          self.panel_courant = panels.Panel_Inactif(self,self.pane.pane('selected'),node)
      return self.panel_courant

   def init_modif(self):
      """
          Met l'attribut modified à 'o' : utilisé par Eficas pour savoir 
          si un JDC doit être sauvegardé avant destruction ou non
      """
      self.modified = 'o'

   def stop_modif(self):
      """
          Met l'attribut modified à 'n' : utilisé par Eficas pour savoir 
          si un JDC doit être sauvegardé avant destruction ou non
      """
      self.modified = 'n'

   def mainloop(self):
      self.parent.mainloop()

   def ReplaceObjectNode(self,node,new_object,nom_sd=None):
      """
      Cette méthode sert à remplacer l'objet pointé par node par
      new_object.
      Si nom_sd : on remplace un OPER et on essaie de renommer la
      nouvelle sd par nom_sd
      """
      child = node.append_brother(new_object,retour='oui')
      if child == 0:
          self.appli.affiche_infos("Impossible de remplacer l'objet du noeud courant")
      else:
          self.init_modif()
          node.delete()
          #if nom_sd:
              #child.item.nomme_sd(nom_sd)
          child.select()
          #child.update()

   def doCut(self):
      """
      Stocke dans Eficas.noeud_a_editer le noeud à couper
      """
      if not self.node_selected.item.iscopiable():
          showinfo("Copie impossible",
                   "Cette version d'EFICAS ne permet que la copie d'objets de type 'Commande' ou mot-clé facteur")
          return
      self.appli.edit="couper"
      self.appli.noeud_a_editer = self.node_selected

   def doCopy(self):
      """
      Stocke dans Eficas.noeud_a_editer le noeud à copier
      """
      if not self.node_selected.item.iscopiable():
          showinfo("Copie impossible",
                   "La copie d'un tel objet n'est pas permise")
          return
      self.appli.edit="copier"
      self.appli.noeud_a_editer = self.node_selected

   def doPaste(self):
      """
      Lance la copie de l'objet placé dans self.appli.noeud_a_editer
      Ne permet que la copie d'objets de type Commande ou MCF
      """
      try:
         child=self.appli.noeud_a_editer.doPaste(self.node_selected)
      except:
         #traceback.print_exc()
         showinfo("Action de coller impossible",
                  "L'action de coller apres un tel objet n'est pas permise")
         return

      if child == 0:
          if self.appli.message != '':
             showerror("Copie refusée",self.appli.message)
             self.appli.message = ''
          self.appli.affiche_infos("Copie refusée")
          return

      # il faut déclarer le JDCDisplay_courant modifié
      self.init_modif()
      # suppression éventuelle du noeud sélectionné
      # si possible on renomme l objet comme le noeud couper
      if self.appli.edit == "couper":
         #nom = self.appli.noeud_a_editer.item.object.sd.nom
         item=self.appli.noeud_a_editer.item
         self.appli.noeud_a_editer.delete()
         child.item.update(item)
         #test,mess = child.item.nomme_sd(nom)
         child.select()
      # on rend la copie à nouveau possible en libérant le flag edit
      self.appli.edit="copier"

   def update(self):
      """Cette methode est utilisee par le JDC associe pour 
         signaler des modifications globales du JDC
      """
      self.tree.update()

   def supprime(self):
      #print "supprime",self
      self.select_node(None)
      self.tree.supprime()
      self.tree=None
      self.pane.destroy()

   #def __del__(self):
   #   print "__del__",self
