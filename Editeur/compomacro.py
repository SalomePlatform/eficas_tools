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
# Modules Python
import os,sys,string
import types
import Tkinter
import Pmw
from tkFileDialog import *
from tkMessageBox import showinfo,showerror
import traceback

# Modules Eficas
import Objecttreeitem
import panels
import fontes
import compooper
import convert
from widgets import Fenetre

#
__version__="$Name:  $"
__Id__="$Id: compomacro.py,v 1.3 2002/04/05 06:32:38 eficas Exp $"
#

class MACROPanel(panels.OngletPanel):
  def init(self):
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    nb.pack(fill = 'both', expand = 1)
    self.nb=nb
    nb.add('Mocles', tab_text='Ajouter mots-clés')
    typsd=self.node.item.object.get_type_produit()
    ficini = self.node.item.wait_fichier_init()
    if typsd != None:
      nb.add('Concept', tab_text='Nommer concept')
    if ficini == 1:
      nb.add('Fichierinit',tab_text = 'Fichier %s' %self.node.item.get_nom())
    nb.add('Commande', tab_text='Insérer Commande')
    nb.add('Commentaire',tab_text='Paramètre/Commentaire')
    panneau=Pmw.PanedWidget(nb.page("Mocles"),
                            orient='horizontal')
    panneau.add('left',min=0.4,max=0.6,size=0.5)
    panneau.add('right',min=0.4,max=0.6,size=0.5)
    panneau.pack(expand=1,fill='both')
    self.makeCommandePage(nb.page("Commande"))
    if typsd != None:
      self.makeConceptPage(nb.page("Concept"))
    if ficini == 1 :
      self.makeFichierPage(nb.page('Fichierinit'))
    self.makeMoclesPage(panneau.pane('left'))
    self.makeReglesPage(panneau.pane('right'))
    self.makeParamCommentPage_for_etape(nb.page("Commentaire"))
    nb.tab('Mocles').focus_set()
    nb.setnaturalsize()
    #self.monmenu=Tkinter.Menu(self.parent.appli.menubar,tearoff=0)
    #self.monmenu.add_command(label='Build',command=self.Build)
    #self.monmenu.add_command(label='View',command=self.View)
    #self.parent.appli.add_menu(label="Macro",menu=self.monmenu)    
    self.affiche()

  def Build(self):
    print "Build"
    self.node.item.object.Build()

  def View(self):
    print "View"
    MacroDisplay(self.parent.appli,self.node.item.object,self.node.item.object.nom)

  def makeFichierPage(self,page):
    """
    Affiche la page d'onglet correspondant au changement du fichier
    dont a besoin la macro
    """
    titre = Tkinter.Label(page,text="La commande %s requiert un fichier " %self.node.item.get_nom())
    titre.place(relx=0.5,rely=0.3,anchor='center')
    Tkinter.Label(page,text="Fichier :").place(relx=0.1,rely=0.5,relwidth=0.2)
    self.entry = Tkinter.Entry(page,relief='sunken',bg='white')
    self.entry.place(relx=0.35,rely=0.5,relwidth=0.55)
    Tkinter.Button(page,text='Valider',command = self.change_fichier_init).place(relx=0.3,rely=0.8)
    Tkinter.Button(page,text='Browse',command = self.browse_fichier_init).place(relx=0.5,rely=0.8)
    Tkinter.Button(page,text='Annuler',command = self.annule_fichier_init).place(relx=0.7,rely=0.8)
    if hasattr(self.node.item.object,'fichier_init'):
      if self.node.item.object.fichier_init :
        self.entry.insert(0,self.node.item.object.fichier_init)
    self.entry.focus()

  def convert_file(self,file):
     """
         Methode pour convertir le fichier file dans le format courant
     """
     format=self.parent.appli.format_fichier.get()
     if convert.plugins.has_key(format):
         # Le convertisseur existe on l'utilise
         p=convert.plugins[format]()
         p.readfile(file)
         text=p.convert('execnoparseur')
         if not p.cr.estvide():
            self.parent.appli.affiche_infos("Erreur à la conversion")
            Fenetre(self,
                    titre="compte-rendu d'erreurs, EFICAS ne sait pas convertir ce fichier",
                    texte = str(p.cr))
            return None
         return text
     else:
         # Il n'existe pas c'est une erreur
         self.parent.appli.affiche_infos("Type de fichier non reconnu")
         showerror("Type de fichier non reconnu","EFICAS ne sait pas ouvrir ce type de fichier")
         return None

  def change_fichier_init(self,event=None):
    """ 
        Effectue le changement de fichier d'initialisation s'il est valide 
    """
    if not hasattr(self.node.item.object,'fichier_init'):
       self.node.item.object.fichier_init=None
    old_fic = self.node.item.object.fichier_init
    new_fic = self.entry.get()
    if not os.path.isfile(new_fic) :
      showinfo("Fichier introuvable","Le fichier que vous avez saisi\n"+
               "n'est pas un nom de fichier valide !")
      self.parent.appli.affiche_infos("Fichier introuvable")
      return
    # On convertit le fichier
    text=self.convert_file(new_fic)
    if not text:return
    try:
      self.node.item.object.make_contexte(new_fic,text)
      self.parent.appli.affiche_infos("Fichier %s modifié" %self.node.item.get_nom())
    except:
      #traceback.print_exc()
      l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
      showinfo("Fichier invalide",
               "Erreur dans l'interprétation du nouveau fichier ...\n"+
               "L'ancien va être restauré\n"+string.join(l))

      self.entry.delete(0,Tkinter.END)
      self.parent.appli.affiche_infos("Fichier invalide")

      if old_fic:
         # On convertit le fichier
         #text=self.convert_file(old_fic)
         #if not text:return
         #self.node.item.object.make_contexte(old_fic,text)
         self.node.item.object.fichier_init=old_fic
         self.entry.insert(0,self.node.item.object.fichier_init)
         self.parent.appli.affiche_infos("Fichier invalide ... Ancien fichier restauré")
      return
    # si on passe ici, c'est que le new_fic a bien été correctement 
    #  interprété ...
    self.node.item.object.fichier_init = new_fic
    # il faut lancer la réévaluation de tout le jdc ... 
    self.node.item.object.reevalue_sd_jdc()
    self.node.racine.update()

  def annule_fichier_init(self,event=None):
    """ retaure dans self.entry le nom de fichier_init"""
    self.entry.delete(0,Tkinter.END)
    self.entry.insert(0,self.node.item.object.fichier_init)

  def browse_fichier_init(self,event=None):
    """ 
         Propose à l'utilisateur une Bsf et retourne le fichier 
         sélectionné dans self.entry 
    """
    file = askopenfilename(title="Choix du fichier %s" %self.node.item.get_nom(),
                         #  filetypes = ( ("Aster", ".comm"),("Python", ".py")),
                         #  defaultextension=".comm"
                          )
    if file != '' :
      self.entry.delete(0,Tkinter.END)
      self.entry.insert(0,file)
    
    
class MACROTreeItem(compooper.EtapeTreeItem):
  panel=MACROPanel

  def IsExpandable(self):
      return 1

  def GetIconName(self):
      """
      Retourne le nom de l'icône à afficher dans l'arbre
      Ce nom dépend de la validité de l'objet
      """
      if self.object.isactif():
        if self.object.state != 'unchanged':
           # Si des modifications ont eu lieu on force le calcul des concepts de sortie
           # et celui du contexte glissant
           self.object.get_type_produit(force=1)
           self.object.parent.reset_context()
        if self.object.isvalid():
          return "ast-green-square"
        else:
          return "ast-red-square"
      else:
        return "ast-white-square"

  def GetLabelText(self):
      """ Retourne 3 valeurs :
      - le texte à afficher dans le noeud représentant l'item
      - la fonte dans laquelle afficher ce texte
      - la couleur du texte
      """
      if self.object.isactif():
        # None --> fonte et couleur par défaut
        return self.labeltext,None,None
      else:
        return self.labeltext,fontes.standard_italique,None
      
  def get_objet(self,name) :
      for v in self.object.mc_liste:
          if v.nom == name : return v
      return None
      
  def additem(self,name,pos):
      if isinstance(name,Objecttreeitem.ObjectTreeItem) :
          mcent = self.object.addentite(name.object,pos)
      else :
          mcent = self.object.addentite(name,pos)
      self.expandable=1
      if mcent == 0 :
          # on ne peut ajouter l'élément de nom name
          return 0
      def setfunction(value, object=mcent):
          object.setval(value)
      item = self.make_objecttreeitem(self.appli,mcent.nom + " : ", mcent, setfunction)
      return item

  def suppitem(self,item) :
      # item : item du MOCLE de l'ETAPE à supprimer
      # item.object = MCSIMP, MCFACT, MCBLOC ou MCList 
      if item.object.isoblig() :
          self.appli.affiche_infos('Impossible de supprimer un mot-clé obligatoire ')
	  print "Impossible de supprimer un mot-clé obligatoire"
          return 0
      else :
          self.object.suppentite(item.object)
          message = "Mot-clé " + item.object.nom + " supprimé"
          self.appli.affiche_infos(message)
          return 1

  def GetText(self):
      try:
          return self.object.get_sdname()
      except:
          return ''

  def keys(self):
      keys=self.object.mc_dict.keys()
      return keys

  def GetSubList(self):
      sublist=[]
      for obj in self.object.mc_liste:
        def setfunction(value, object=obj):
          object.setval(value)
        item = self.make_objecttreeitem(self.appli, obj.nom + " : ", obj, setfunction)
        sublist.append(item)
      return sublist

  def isvalid(self):
      return self.object.isvalid()

  def iscopiable(self):
      """
      Retourne 1 si l'objet est copiable, 0 sinon
      """
      return 1

  def isCommande(self):
      """
      Retourne 1 si l'objet pointé par self est une Commande, 0 sinon
      """
      return 1
      
  def verif_condition_bloc(self):
      return self.object.verif_condition_bloc()

  def get_noms_sd_oper_reentrant(self):
      return self.object.get_noms_sd_oper_reentrant()

import Accas
treeitem=MACROTreeItem
objet=Accas.MACRO_ETAPE
    
class MacroDisplay:
  def __init__(self,appli,jdc,nom_jdc):
    self.fenetre = Tkinter.Toplevel()
    self.fenetre.configure(width = 800,height=500)
    self.fenetre.protocol("WM_DELETE_WINDOW", self.quit)
    self.fenetre.title("Visualisation Macro_Etape")
    self.jdc=jdc
    self.nom_jdc=nom_jdc
    self.appli=appli
    self.mainPart=Pmw.ScrolledCanvas(self.fenetre,
                                     hull_width=600,
                                     hull_height=500,
                                     borderframe=1)
    self.canvas=self.mainPart.component('canvas')
    Pmw.Color.changecolor(self.canvas,background='gray95')
    self.mainPart.pack(padx=10,pady=10,fill = 'both', expand = 1)
    self.item=MACRO2TreeItem(self.appli,nom_jdc,jdc)
    import treewidget
    self.tree = treewidget.Tree(self.appli,self.item,self.mainPart,command=None)
    self.tree.draw()
    
  def quit(self):
    self.fenetre.destroy()

