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
__Id__="$Id: compomacro.py,v 1.17 2005/04/18 10:20:36 eficas Exp $"
#

class MACROPanel(panels.OngletPanel):
  def init(self):
    nb = Pmw.NoteBook(self,raisecommand=self.raisecmd)
    nb.pack(fill = 'both', expand = 1)
    self.nb=nb
    nb.add('Mocles', tab_text='Ajouter mots-cl�s')
    typsd=self.node.item.object.get_type_produit()
    ficini = self.node.item.wait_fichier_init()
    if typsd != None:
      nb.add('Concept', tab_text='Nommer concept')
    if ficini == 1:
      nb.add('Fichierinit',tab_text = 'Fichier %s' %self.node.item.get_nom())
    nb.add('Commande', tab_text='Nouvelle Commande')
    nb.add('Commentaire',tab_text='Param�tre/Commentaire')
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
    titre.place(relx=0.5,rely=0.3,anchor='center')
    Tkinter.Label(page,text="Fichier :").place(relx=0.1,rely=0.5,relwidth=0.2)
    self.entry = Tkinter.Entry(page,relief='sunken',bg='white')
    self.entry.place(relx=0.35,rely=0.5,relwidth=0.55)
    Tkinter.Button(page,text='Valider',command = self.change_fichier_init).place(relx=0.3,rely=0.8)
    Tkinter.Button(page,text='Browse',command = self.browse_fichier_init).place(relx=0.5,rely=0.8)
    Tkinter.Button(page,text='Annuler',command = self.annule_fichier_init).place(relx=0.7,rely=0.8)
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
            self.parent.appli.affiche_infos("Erreur � la conversion")
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
    if not hasattr(self.node.item.object,'fichier_ini'):
       self.node.item.object.fichier_ini=None
       self.node.item.object.fichier_text=None
       self.node.item.object.fichier_err="Le fichier n'est pas defini"
       self.node.item.object.contexte_fichier_init={}
       self.node.item.object.recorded_units={}
       self.node.item.object.fichier_unite="PasDefini"
       import Extensions.jdc_include
       self.node.item.object.JdC_aux=Extensions.jdc_include.JdC_include

    old_fic = self.node.item.object.fichier_ini
    old_text = self.node.item.object.fichier_text
    old_err = self.node.item.object.fichier_err
    old_context=self.node.item.object.contexte_fichier_init
    old_units=self.node.item.object.recorded_units
    old_etapes=self.node.item.object.etapes

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
    #self.node.item.object.recorded_units={}

    try:
      self.node.item.object.make_contexte_include(new_fic,text)
    except:
      # Erreurs lors de l'evaluation de text dans un JDC auxiliaire
      self.parent.appli.affiche_infos("Fichier invalide")
      l=traceback.format_exception_only("Fichier invalide",sys.exc_info()[1])
      f=FenetreYesNo(self.parent.appli,titre="Fichier invalide : voulez vous retablir l ancien fichier ?",
                             texte="Erreur dans l'interpr�tation du nouveau fichier ...\n\n"+string.join(l),
                             yes="Retablir",no="Changer")
      f.wait()
      reponse=f.result
      if reponse:
         # On retablit l'ancien fichier
         self.entry.delete(0,Tkinter.END)
         self.node.item.object.fichier_ini=old_fic
         self.node.item.object.fichier_text=old_text
         self.node.item.object.fichier_err=old_err
         self.node.item.object.contexte_fichier_init=old_context
         self.node.item.object.recorded_units=old_units
         self.node.item.object.etapes=old_etapes
         self.parent.appli.affiche_infos("Fichier invalide ... Ancien fichier restaur�")
         if old_fic:
             self.entry.insert(0,self.node.item.object.fichier_ini)
      else:
         # On conserve la memoire du nouveau fichier
         # mais on n'utilise pas les concepts crees par ce fichier
         # on met l'etape en erreur : fichier_err=string.join(l)
         self.node.item.object.init_modif()
         self.node.item.object.fichier_ini=new_fic
         self.node.item.object.fichier_text=text
         self.node.item.object.fichier_err=string.join(l)
         # On enregistre la modification de fichier
         self.node.item.object.record_unite()  
         #self.node.item.object.etapes=[]
         self.node.item.object.g_context={}
         # Le contexte du parent doit etre reinitialise car les concepts produits ont chang�
         self.node.item.object.parent.reset_context()

         self.node.item.object.old_contexte_fichier_init=old_context
         self.node.item.object.contexte_fichier_init={}
         self.node.item.object.reevalue_sd_jdc()

         self.node.item.object.fin_modif()
         self.parent.appli.affiche_infos("Fichier invalide ... Nouveau fichier m�moris�")
         self.node.update()
      return

    # L'evaluation de text dans un JDC auxiliaire s'est bien pass�
    # on peut poursuivre le traitement
    self.node.item.object.init_modif() 
    self.node.item.object.state="undetermined"
    self.node.item.object.fichier_ini = new_fic
    self.node.item.object.fichier_text=text
    self.node.item.object.fichier_err=None
    # On enregistre la modification de fichier
    self.node.item.object.record_unite()  
    # Le contexte du parent doit etre reinitialise car les concepts produits ont chang�
    self.node.item.object.parent.reset_context()

    # Si des concepts ont disparu lors du changement de fichier, on demande leur suppression
    self.node.item.object.old_contexte_fichier_init=old_context
    self.node.item.object.reevalue_sd_jdc()

    self.node.item.object.fin_modif()
    self.parent.appli.affiche_infos("Fichier %s modifi�" %self.node.item.get_nom())
    self.node.update()

  def annule_fichier_init(self,event=None):
    """ Restaure dans self.entry le nom de fichier_init"""
    self.entry.delete(0,Tkinter.END)
    self.entry.insert(0,self.node.item.object.fichier_ini)

  def browse_fichier_init(self,event=None):
    """ 
         Propose � l'utilisateur une Bsf et retourne le fichier 
         s�lectionn� dans self.entry 
    """
    file = askopenfilename(title="Choix du fichier %s" %self.node.item.get_nom())
    if file :
      self.entry.delete(0,Tkinter.END)
      self.entry.insert(0,file)
    
    
class MACROTreeItem(compooper.EtapeTreeItem):
  """ Cette classe h�rite d'une grande partie des comportements
      de la classe compooper.EtapeTreeItem
  """
  panel=MACROPanel

class INCLUDETreeItem(MACROTreeItem):
  rmenu_specs=[("View","makeView"),
               ("Edit","makeEdit"),
              ]

  def __init__(self,appli, labeltext, object, setfunction):
    MACROTreeItem.__init__(self,appli, labeltext, object, setfunction)
    self.views=[]

  def makeEdit(self,appli,node):
    print "makeEdit",self.object,self.object.nom
    print "makeEdit",self.object.jdc_aux,self.object.jdc_aux.nom
    self.parent_node=node
    # On cree un nouvel onglet dans le bureau
    appli.bureau.ShowJDC(self.object.jdc_aux,self.object.jdc_aux.nom,
                             label_onglet=None,
                             JDCDISPLAY=macrodisplay.MACRODISPLAY)
    self.myjdc=appli.bureau.JDCDisplay_courant
    self.object.jdc_aux.subscribe(self)

  def notify(self,obj):
    print "notify",self,obj
    self.parent_node.update_valid()
    # Il faudrait redessiner l'arbre de maniere optimale
    # et pas seulement l'updater
    for display in self.views:
       display.tree.update()

  def makeView(self,appli,node):
    nom=self.object.nom
    if hasattr(self.object,'fichier_ini'):
       if self.object.fichier_ini is None:
          nom=nom+' '+"Fichier non d�fini"
       else:
          nom=nom+' '+self.object.fichier_ini
    macdisp=macrodisplay.makeMacroDisplay(appli,self,nom)
    self.views.append(macdisp)

class INCLUDE_MATERIAUTreeItem(INCLUDETreeItem): pass
class POURSUITETreeItem(INCLUDETreeItem): pass

def treeitem(appli, labeltext, object, setfunction=None):
   """ Factory qui retourne l'item adapt� au type de macro : 
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
