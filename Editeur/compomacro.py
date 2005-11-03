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
# Modules Python
import os,sys,string
import types
import Tkinter
import Pmw
import traceback

# Modules Eficas
import Objecttreeitem
import panels
import fontes
import compooper
import convert
from widgets import askopenfilename
from widgets import Fenetre,FenetreYesNo
from widgets import showinfo,showerror

#
__version__="$Name:  $"
__Id__="$Id: compomacro.py,v 1.23 2005/06/16 09:27:25 eficas Exp $"
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
    nb.add('Commande', tab_text='Nouvelle Commande')
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
    self.affiche()

  def makeFichierPage(self,page):
    """
    Affiche la page d'onglet correspondant au changement du fichier
    dont a besoin la macro
    """
    titre = Tkinter.Label(page,text="La commande %s requiert un fichier " %self.node.item.get_nom())
    titre.place(relx=0.5,rely=0.2,anchor='center')
    frameMain=Tkinter.Frame(page)
    frameMain.place(relx=0.5,rely=0.4,anchor='center',relwidth=1.)
    Tkinter.Label(frameMain,text="Fichier :").pack(side='left',padx=5)
    self.entry = Tkinter.Entry(frameMain,relief='sunken',bg='white')
    self.entry.pack(side='left',padx=5,fill='x',expand=1)
    frameButtons=Tkinter.Frame(page)
    but1=Tkinter.Button(frameButtons,text='Valider',command = self.change_fichier_init)
    but2=Tkinter.Button(frameButtons,text='Browse',command = self.browse_fichier_init)
    but3=Tkinter.Button(frameButtons,text='Annuler',command = self.annule_fichier_init)
    but1.grid(row=0,column=0,padx=5,pady=5)
    but2.grid(row=0,column=1,padx=5,pady=5)
    but3.grid(row=0,column=2,padx=5,pady=5)
    frameButtons.place(relx=0.5,rely=0.6,anchor='center')

    if hasattr(self.node.item.object,'fichier_ini'):
      if self.node.item.object.fichier_ini :
        self.entry.insert(0,self.node.item.object.fichier_ini)
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
    new_fic = self.entry.get()
    if not os.path.isfile(new_fic) :
      showinfo("Fichier introuvable","Le fichier que vous avez saisi\n"+
               "n'est pas un nom de fichier valide !")
      self.parent.appli.affiche_infos("Fichier introuvable")
      return
    # On convertit le fichier
    text=self.convert_file(new_fic)
    # Si probleme a la lecture-conversion on arrete le traitement
    if not text:
       return

    try:
      self.node.item.object.change_fichier_init(new_fic,text)
      self.parent.appli.affiche_infos("Fichier %s modifié" %self.node.item.get_nom())
    except:
      # Erreurs lors de l'evaluation de text dans un JDC auxiliaire
      self.parent.appli.affiche_infos("Fichier invalide")
      l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
      f=FenetreYesNo(self.parent.appli,titre="Fichier invalide : voulez vous retablir l ancien fichier ?",
                             texte="Erreur dans l'interprétation du nouveau fichier ...\n\n"+string.join(l),
                             yes="Retablir",no="Changer")
      f.wait()
      reponse=f.result
      if reponse:
         # On retablit l'ancien fichier
         self.entry.delete(0,Tkinter.END)
         self.node.item.object.restore_fichier_init()
         self.parent.appli.affiche_infos("Fichier invalide ... Ancien fichier restauré")
         fic=self.node.item.object.fichier_ini
         if fic:
             self.entry.insert(0,fic)
      else:
         self.node.item.object.force_fichier_init()
         self.parent.appli.affiche_infos("Fichier invalide ... Nouveau fichier mémorisé")

  def annule_fichier_init(self,event=None):
    """ Restaure dans self.entry le nom de fichier_init"""
    self.entry.delete(0,Tkinter.END)
    if self.node.item.object.fichier_ini:
       self.entry.insert(0,self.node.item.object.fichier_ini)

  def browse_fichier_init(self,event=None):
    """ 
         Propose à l'utilisateur une Bsf et retourne le fichier 
         sélectionné dans self.entry 
    """
    file = askopenfilename(title="Choix du fichier %s" %self.node.item.get_nom())
    if file :
      self.entry.delete(0,Tkinter.END)
      self.entry.insert(0,file)
    
  def update_panel(self):
    if hasattr(self,"entry"):
       self.annule_fichier_init()
    
class MACROTreeItem(compooper.EtapeTreeItem):
  """ Cette classe hérite d'une grande partie des comportements
      de la classe compooper.EtapeTreeItem
  """
  panel=MACROPanel

class INCLUDETreeItemBase(MACROTreeItem):
  rmenu_specs=[("View","makeView"),
               ("Edit","makeEdit"),
              ]

  def __init__(self,appli, labeltext, object, setfunction):
    MACROTreeItem.__init__(self,appli, labeltext, object, setfunction)

  def iscopiable(self):
      """
      Retourne 1 si l'objet est copiable, 0 sinon
      """
      return 0

  def makeEdit(self,appli,node):
    #print "makeEdit",self.object,self.object.nom
    #print "makeEdit",self.object.jdc_aux,self.object.jdc_aux.nom
    #print "makeEdit",self.object.jdc_aux.context_ini
    if not hasattr(self.object,"jdc_aux") or self.object.jdc_aux is None:
       #L'include n'est pas initialise
       self.object.build_include(None,"")
    # On cree un nouvel onglet dans le bureau
    appli.bureau.ShowJDC(self.object.jdc_aux,self.object.jdc_aux.nom,
                             label_onglet=None,
                             JDCDISPLAY=macrodisplay.MACRODISPLAY)

  def makeView(self,appli,node):
    if not hasattr(self.object,"jdc_aux") or self.object.jdc_aux is None:
         showerror("Include vide","L'include doit etre correctement initialisé pour etre visualisé")
         return
    nom=self.object.nom
    if hasattr(self.object,'fichier_ini'):
       if self.object.fichier_ini is None:
          nom=nom+' '+"Fichier non défini"
       else:
          nom=nom+' '+self.object.fichier_ini
    macdisp=macrodisplay.makeMacroDisplay(appli,self,nom)

class INCLUDEPanel(MACROPanel):
  def makeFichierPage(self,page):
    """
    Affiche la page d'onglet correspondant au changement du fichier INCLUDE
    """
    if not hasattr(self.node.item.object,'fichier_ini'):
       titre = Tkinter.Label(page,text="L'INCLUDE n'a pas de fichier associé\nIl faut d'abord choisir un numero d'unité " )
       titre.place(relx=0.5,rely=0.5,anchor='center')
    else:
       MACROPanel.makeFichierPage(self,page)

class INCLUDETreeItem(INCLUDETreeItemBase):
   panel=INCLUDEPanel

class POURSUITETreeItem(INCLUDETreeItemBase): 
  def makeEdit(self,appli,node):
    if not hasattr(self.object,"jdc_aux") or self.object.jdc_aux is None:
       #La poursuite n'est pas initialisee
       text="""DEBUT()
FIN()"""
       self.object.build_poursuite(None,text)
    # On cree un nouvel onglet dans le bureau
    appli.bureau.ShowJDC(self.object.jdc_aux,self.object.jdc_aux.nom,
                             label_onglet=None,
                             JDCDISPLAY=macrodisplay.MACRODISPLAY)

  def makeView(self,appli,node):
    if not hasattr(self.object,"jdc_aux") or self.object.jdc_aux is None:
         showerror("Poursuite vide","Une POURSUITE doit etre correctement initialisée pour etre visualisée")
         return
    nom=self.object.nom
    if hasattr(self.object,'fichier_ini'):
       if self.object.fichier_ini is None:
          nom=nom+' '+"Fichier non défini"
       else:
          nom=nom+' '+self.object.fichier_ini
    macdisp=macrodisplay.makeMacroDisplay(appli,self,nom)

class INCLUDE_MATERIAUTreeItem(INCLUDETreeItemBase):
  rmenu_specs=[("View","makeView"),
              ]
  def iscopiable(self):
      """
      Retourne 1 si l'objet est copiable, 0 sinon
      """
      return 1


def treeitem(appli, labeltext, object, setfunction=None):
   """ Factory qui retourne l'item adapté au type de macro : 
       INCLUDE, POURSUITE, MACRO
   """
   if object.nom == "INCLUDE_MATERIAU":
      return INCLUDE_MATERIAUTreeItem(appli, labeltext, object, setfunction)
   elif object.nom == "INCLUDE":
      return INCLUDETreeItem(appli, labeltext, object, setfunction)
   elif object.nom == "POURSUITE":
      return POURSUITETreeItem(appli, labeltext, object, setfunction)
   else:
      return MACROTreeItem(appli, labeltext, object, setfunction)

import Accas
objet=Accas.MACRO_ETAPE
    
import macrodisplay
