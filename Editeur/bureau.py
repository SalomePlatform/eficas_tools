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
   Ce module contient la classe BUREAU qui gere les JDC ouverts
"""
# Modules Python
import os,string,sys
import traceback
import Pmw
from widgets import askopenfilename,asksaveasfilename
from widgets import showinfo,askyesno,showerror

# Modules Eficas
import splash
import prefs
import convert
import generator
import AIDE
from jdcdisplay import JDCDISPLAY
from utils import extension_fichier,stripPath,save_in_file
from widgets import Fenetre,Ask_Format_Fichier
from fenetre_mc_inconnus import fenetre_mc_inconnus
from Ihm import CONNECTOR

import comploader

class BUREAU:
   menu_defs=[
              ('Fichier',[
                           ('Nouveau','newJDC','<Control-n>'),
                           ('Ouvrir','openJDC','<Control-o>'),
                           ('Enregistrer','saveJDC','<Control-e>'),
                           ('Enregistrer sous','saveasJDC','<Control-s>'),
                           None,
                           ('Fermer','closeJDC','<Control-f>'),
                           ('Quitter','exitEFICAS','<Control-q>'),
                         ]
              ),
              ('Edition',[
                           ('Copier','copy','<Control-c>'),
                           ('Couper','cut','<Control-x>'),
                           ('Coller','paste','<Control-v>'),
                         ]
              ),
              ('Jeu de commandes',[
                                   ('Rapport de validation','visuCRJDC','<Control-r>'),
                                   ('Fichier à plat','visu_a_plat','<Control-p>'),
                                   ('Fichier .py','visuJDC_py'),
                                   ('Fichier source','visu_txt_brut_JDC','<Control-b>'),
                                   ('Paramètres Eficas','affichage_fichier_ini'),
                                   ('Mots-clés inconnus','mc_inconnus'),
                                  ]
              ),
              ('Aide',[
                        ('Aide EFICAS','aideEFICAS'),
                      ]
              ),
             ]

   button_defs  =      (('New24',"newJDC","Création d'un nouveau fichier",'always'),
                        ('Open24',"openJDC","Ouverture d'un fichier existant",'always'),
                        ('Save24',"saveJDC","Sauvegarde du fichier courant",'always'),
			('Fermer24',"closeJDC","Fermeture du fichier courant",'always'),
                        ('Zoom24',"visuJDC","Visualisation du fichier de commandes",'always'),
                        None,
                        ('Copy24',"copy","Copie l'objet courant",'jdc'),
                        ('Cut24',"cut","Coupe l'objet courant",'jdc'),
                        ('Paste24',"paste","Colle l'objet copié après l'objet courant",'jdc'),
                        None,
                        ('Delete24',"delete","Supprime l'objet courant",'jdc'),
                        ('Help24',"view_doc","Documentation de l'objet courant",'jdc')
                       )
   try:
      menu_defs=prefs.menu_defs['bureau']
   except:
      pass
   try:
      button_defs=prefs.button_defs['bureau']
   except:
      pass

   def __init__(self,appli,parent):
      self.parent=parent
      self.appli=appli
      if self.appli.test == 0 :
         splash._splash.configure(text = "Création du bureau")
      self.nb = Pmw.NoteBook(self.parent,raisecommand=self.selectJDC)
      self.nb.pack(fill='both',expand=1)
      self.JDCDisplay_courant=None
      self.fileName=None
      self.liste_JDCDisplay=[]
      comploader.charger_composants()
      self.cree_cataitem()
      self.text_reel=""
      self.initialdir = self.appli.CONFIGURATION.initialdir

   def cree_cataitem(self):
      """
          On récupère dans l'appli_composant readercata les variables 
          qui servent par la suite pour la création des JDC
      """
      self.cataitem=self.appli.readercata.cataitem
      self.cata=self.appli.readercata.cata
      self.cata_ordonne_dico=self.appli.readercata.cata_ordonne_dico
      self.code=self.appli.readercata.code
      self.version_code=self.appli.readercata.version_code
      self.fic_cata=self.appli.readercata.fic_cata

   def selectJDC(self,event=None):
      """
          Cette méthode est appelée chaque fois que l'on sélectionne 
          l'onglet d'un JDC dans le NoteBook des JDC.
          Elle permet de stocker dans les variable self.JDC et 
          self.JDCDisplay_courant les valeurs concernant le JDC courant
      """
      if len(self.liste_JDCDisplay) == 0 : return
      #if self.JDCDisplay_courant : self.JDCDisplay_courant.jdc.unset_context()
      numero_jdc = self.nb.index(self.nb.getcurselection())
      self.JDCDisplay_courant.unselect()
      self.JDCDisplay_courant = self.liste_JDCDisplay[numero_jdc]
      self.JDC = self.JDCDisplay_courant.jdc
      self.JDCName = self.JDC.nom
      self.JDCDisplay_courant.select()
      #print "selectJDC",numero_jdc,self.JDCDisplay_courant,self.JDCName


   def newJDC_include(self,event=None):
      """
          Initialise un nouveau JDC vierge
      """
      import Extensions.jdc_include
      JdC_aux=Extensions.jdc_include.JdC_include

      self.appli.statusbar.reset_affichage_infos()

      CONTEXT.unset_current_step()
      jaux=self.cata[0].JdC(procedure="",appli=self.appli,
                         cata=self.cata,cata_ord_dico=self.cata_ordonne_dico,
                         rep_mat=self.appli.CONFIGURATION.rep_mat,
                         )
      jaux.analyse()

      J=JdC_aux(procedure="",appli=self.appli,
                         cata=self.cata,cata_ord_dico=self.cata_ordonne_dico,
                         jdc_pere=jaux,
                         rep_mat=self.appli.CONFIGURATION.rep_mat,
                         )
      J.analyse()
      self.JDCName=J.nom
      self.fileName=None
      self.ShowJDC(J,self.JDCName)
      self.appli.toolbar.active_boutons()

   def newJDC(self,event=None):
      """
          Initialise un nouveau JDC include vierge
      """
      self.appli.statusbar.reset_affichage_infos()

      CONTEXT.unset_current_step()
      J=self.cata[0].JdC(procedure="",appli=self.appli,
                         cata=self.cata,cata_ord_dico=self.cata_ordonne_dico,
                         rep_mat=self.appli.CONFIGURATION.rep_mat,
                         )
      J.analyse()
      self.JDCName=J.nom
      self.fileName=None
      self.ShowJDC(J,self.JDCName)
      self.appli.toolbar.active_boutons()

   def ShowJDC(self,JDC,nom,label_onglet=None,JDCDISPLAY=JDCDISPLAY,enregistre="non"):
      """
          Lance l'affichage du JDC cad création du JDCDisplay
          Rajoute le JDCDisplay à la liste des JDCDisplay si label_onglet == None cad si on crée
          bien un nouveau JDCDisplay et non si on remplace (renommage de l'onglet)
      """
      self.JDC=JDC
      self.JDCName = self.JDC.nom = nom
      if label_onglet == None :
          # On veut un nouvel onglet
          label_onglet = self.GetLabelJDC()
          self.nb.add(label_onglet,tab_text = nom,tab_width=20)
          new = 'oui'
      else :
          new = 'non'
      self.JDCDisplay_courant=JDCDISPLAY(self.JDC,nom,appli=self.appli,parent=self.nb.page(label_onglet))
      if new == 'oui':
          self.liste_JDCDisplay.append(self.JDCDisplay_courant)
      self.JDCDisplay_courant.modified='n'
      if enregistre != "non" :
         self.JDCDisplay_courant.fichier=self.fileName
      else :
         self.initialdir = self.appli.CONFIGURATION.rep_user
      self.nb.selectpage(label_onglet)
      self.nb.setnaturalsize()
      self.nb.bind_all("<Key-Next>",lambda e,s=self:s.selectArbreDown())
      self.nb.bind_all("<Key-Prior>",lambda e,s=self:s.selectArbreUp())
      self.nb.bind_all("<Insert>",lambda e,s=self:s.deplieReplieNode())
      texte = "Jeu de commandes :" + self.JDCName+" ouvert"
      CONNECTOR.Connect(JDC,"close",self.onClose,(self.JDCDisplay_courant,))
      self.appli.affiche_infos(texte)

   def onClose(self,jdcdisplay):
      #print "onClose",jdcdisplay
      self.closeJDCDISPLAY(jdcdisplay)

   def closeJDCDISPLAY(self,jdc):
      """
        Ferme le jdcdisplay spécifié par l'argument jdc
      """
      if jdc is self.JDCDisplay_courant:
         # on ferme le jdcdisplay courant
         self.closeSelectedJDC()
      else:
         # on ferme un autre jdcdisplay que le courant
         old_JDCDisplay=self.JDCDisplay_courant
         old_page=self.nb.getcurselection()

         self.JDCDisplay_courant=jdc
         self.JDC=jdc.jdc
         numero_jdc=self.liste_JDCDisplay.index(jdc)
         self.nb.selectpage(numero_jdc)
         #print numero_jdc
      
         self.closeSelectedJDC()
         self.JDCDisplay_courant=old_JDCDisplay
         self.JDC=old_JDCDisplay.jdc
         self.nb.selectpage(old_page)

   def closeJDC (self,event=None) :
      """
          Ferme le JDC associé au JDCDISPLAY selectionné
      """
      if self.JDCDisplay_courant :
         self.JDCDisplay_courant.jdc.close()

   def closeSelectedJDC (self) :
      """
      Ferme le JDC courant et détruit l'onglet associé dans le notebook self.nb
      """
      if self.JDCDisplay_courant.modified == 'o' :
          message = "Voulez-vous sauvegarder le jeu de commandes "+self.JDC.nom+" courant ?"
          reponse = askyesno(title="Sauvegarde du jdc courant",
                             message=message)
          if reponse :
              test = self.saveJDC()
              if test == 0 :
                  self.appli.affiche_infos("Sauvegarde impossible")
                  return

      CONNECTOR.Disconnect(self.JDCDisplay_courant.jdc,"close",self.onClose,(self.JDCDisplay_courant,))
      self.JDCDisplay_courant.supprime()
      self.JDCDisplay_courant.jdc.supprime()
      self.liste_JDCDisplay.remove(self.JDCDisplay_courant)
      # Active le mecanisme de selection du notebook (selectJDC)
      self.nb.delete(self.nb.getcurselection())

      try:
          index = self.nb.index(self.nb.getcurselection())
          self.JDCDisplay_courant = self.liste_JDCDisplay[index]
          self.JDC = self.JDCDisplay_courant.jdc
      except:
          self.JDC = None
          self.JDCDisplay_courant = None
          self.appli.toolbar.inactive_boutons()

   def visuCRJDC(self,event=None):
      return self.visuCR(mode='JDC')

   def visuCR(self,mode):
      """
      Méthode permettant l'affichage du rapport de validation
      """
      if mode == 'JDC':
          if not hasattr(self,'JDC') : return
          titre="rapport de validation du jeu de commandes courant"
          cr = self.JDC.report()
          #self.update_jdc_courant()
      elif mode == 'CATA':
          from Noyau.N_CR import CR
          cr = CR()
          cr.debut = "Début rapport de validation du catalogue"
          cr.fin = "Fin rapport de validation du catalogue"
          titre="rapport de validation du catalogue"
          if hasattr(self,'cata_ordonne_cr') :
              cr.add(self.cata_ordonne_cr)
          if hasattr(self,'cata_dev_ordonne_cr') :
              cr.add(self.cata_dev_ordonne_cr)
          for cata in self.cata:
              if hasattr(cata,'JdC'):
                  cr.add(cata.JdC.report())
      texte_cr = str(cr)
      self.visu_texte_cr = Fenetre(self.appli,titre=titre,texte=texte_cr)

   def openJDC(self,event=None,file=None,units=None,enregistre="oui"):
      """
          Demande à l'utilisateur quel JDC existant il veut ouvrir
      """
      if self.code == 'ASTER':
          filetypes = ( ("format "+self.appli.format_fichier.get(), ".com*"),("Tous",'*'))
      elif self.code == 'HOMARD' :
          filetypes = ( ("format "+self.appli.format_fichier.get(), ".py"),("Tous",'*'))
      else:
          filetypes = ( ("format "+self.appli.format_fichier.get(), ".py"),)
      if not hasattr(self,'initialdir'):
         self.initialdir = self.appli.CONFIGURATION.initialdir

      if not file :
          file = askopenfilename(title="Ouverture d'un fichier de commandes Aster",
                                 defaultextension=".comm",
                                 filetypes = filetypes,
                                 initialdir = self.initialdir)
      if file :
          self.fileName = file
          e=extension_fichier(file)
          self.JDCName=stripPath(file)
          self.initialdir = os.path.dirname(os.path.abspath(file))
      else :
          return

      format=self.appli.format_fichier.get()
      # Il faut convertir le contenu du fichier en fonction du format
      if convert.plugins.has_key(format):
         # Le convertisseur existe on l'utilise
         p=convert.plugins[format]()
         p.readfile(file)
         text=p.convert('exec',self.appli)
         if not p.cr.estvide(): 
            self.appli.affiche_infos("Erreur à la conversion")
            Fenetre(self.appli,
                    titre="compte-rendu d'erreurs, EFICAS ne sait pas convertir ce fichier",
                    texte = str(p.cr)).wait()
            return
	 if enregistre == "oui" :
	    self.appli.listeFichiers.aOuvert(file)
      else:
         # Il n'existe pas c'est une erreur
         self.appli.affiche_infos("Type de fichier non reconnu")
         showerror("Type de fichier non reconnu","EFICAS ne sait pas ouvrir ce type de fichier")
         return

      # On se met dans le repertoire ou se trouve le fichier de commandes
      # pour trouver les eventuels fichiers include ou autres
      # localises a cote du fichier de commandes
      os.chdir(self.initialdir)
      CONTEXT.unset_current_step()
      J=self.cata[0].JdC(procedure=text,appli=self.appli,
                         cata=self.cata,cata_ord_dico=self.cata_ordonne_dico,
                         nom = self.JDCName,
                         rep_mat=self.appli.CONFIGURATION.rep_mat,
                         )
      if units is not None:
         J.recorded_units=units
         J.old_recorded_units=units

      J.analyse()
      txt_exception = J.cr.get_mess_exception()
      if txt_exception :
          # des exceptions ont été levées à la création du JDC 
          # --> on affiche les erreurs mais pas le JDC
          self.JDC=J
          self.appli.affiche_infos("Erreur fatale au chargement de %s" %file)
          if self.appli.test == 0 :
             showerror("Erreur fatale au chargement d'un fichier",txt_exception)
      else:
          self.ShowJDC(J,self.JDCName,enregistre=enregistre)
          self.appli.toolbar.active_boutons()
	  # si le JDC ne contient rien (vide), on retourne ici
	  if len(self.JDC.etapes) == 0 : return
	  # dans le cas où le JDC est invalide, on affiche son CR
          if not self.JDC.isvalid():
	     self.appli.top.update()
	     self.visuCR(mode='JDC')

   def deplieReplieNode(self):
       self.JDCDisplay_courant.tree.tree.deplieReplieNode()

   def selectArbreDown(self):
       self.JDCDisplay_courant.tree.tree.canvas.focus_set()
       self.JDCDisplay_courant.tree.tree.mot_down_force()

   def selectArbreUp(self):
       self.JDCDisplay_courant.tree.tree.canvas.focus_set()
       self.JDCDisplay_courant.tree.tree.mot_up_force()

   def GetLabelJDC(self,nb_jdc = 'absent'):
      """
      Retourne le label de l'onglet du NoteBook associé au JDC à afficher
      """
      if nb_jdc == 'absent':
          nb_jdc = len(self.nb.pagenames())
      nb_jdc = nb_jdc+1
      label_onglet = 'JDC'+`nb_jdc`
      if label_onglet not in self.nb.pagenames() :
          return label_onglet
      else :
          return self.GetLabelJDC(nb_jdc)

   def saveasJDC(self,event=None):
      """ 
           Sauvegarde le JDC courant en demandant impérativement à l'utilisateur de
           donner le nom du fichier de sauvegarde 
      """
      self.saveJDC(echo='oui')

   def saveJDC(self,echo='non'):
      """ 
          Sauvegarde le JDC courant.
          Retourne 1 si la sauvegarde s'est bien faite, 0 sinon.
          Si echo = 'oui' : interactif (l'utilisateur donne le nom sous lequel il 
                            veut sauver le JDC
          Si echo = 'non' : muet (sauvegarde le JDC dans JDC.procedure)
      """
      ok = 0
      if not hasattr(self,'JDC') : return 0
      format=self.appli.format_fichier.get()
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         g=generator.plugins[format]()
         jdc_formate=g.gener(self.JDC,format='beautifie')
         if format == 'homard':
            self.jdc_homard=g.get_homard()
         if not g.cr.estvide():
            self.appli.affiche_infos("Erreur à la generation")
            showerror("Erreur à la generation","EFICAS ne sait pas convertir ce JDC")
            return
      else:
         # Il n'existe pas c'est une erreur
         self.appli.affiche_infos("Format %s non reconnu" % format)
         showerror("Format %s non reconnu" % format,"EFICAS ne sait pas convertir le JDC")
         return
      self.jdc_fini = string.replace(jdc_formate,'\r\n','\n')

      if echo =='oui' or self.JDCDisplay_courant.fichier == None:
	 ok = self.asknomsauvegardeJDC()
      elif self.JDCDisplay_courant.fichier != None :
         # le JDC a déjà un nom : on sauvegarde directement sans demander
         # un autre nom au développeur
         if not save_in_file(self.JDCDisplay_courant.fichier,self.jdc_fini,self.appli.dir) :
              showinfo("Erreur","Problème à la sauvegarde du fichier :" + `self.JDCDisplay_courant.fichier`)
              #return 0
	      ok = 0
         else :
              if self.appli.format_fichier.get() == 'homard':
                  self.save_homard(self.JDCDisplay_courant.fichier,self.jdc_homard)
              self.JDCDisplay_courant.stop_modif()
              self.appli.affiche_infos("sauvegarde de "+`self.JDCDisplay_courant.fichier`+" effectuée")
              ok = 1

      if ok and hasattr( self.appli, 'salome'):
         # eficas a été lancé à partir deSalome
         #1)ajout dans l'arbre d'étude du nom du jdc
	 ok, msg = self.appli.addJdcInSalome( self.JDCDisplay_courant.fichier )

         #2)CS_pbruno ??
	 from panelsSalome import SALOME_UNIQUE_BASE_Panel
	 if len(SALOME_UNIQUE_BASE_Panel.dict_fichier_unite) > 0 :
	    print 'CS_pbruno if len(SALOMchier_unite) > 0 :???????'
	    self.appli.creeConfigTxt( self.appli.CONFIGURATION.initialdir, SALOME_UNIQUE_BASE_Panel.dict_fichier_unite )

	 #3)création/mise à jours d'un maillage dans Salome
	 self.appli.createOrUpdateMesh()
      return ok

   def asknomsauvegardeJDC(self):
      """ Demande à l'utilsateur le nom sous lequel il veut sauvegarder le JDC courant """
      titre = "Sauvegarde d'un fichier de commandes "+self.code
      if self.code == 'ASTER':
          defext = ".comm"
          filtyp = ( ("ASTER", ".comm"),)
      else :
          defext = ".py"
          filtyp = ( (self.code, ".py"),)
      sauvegarde = asksaveasfilename(title=titre,
                                     defaultextension=defext,
                                     filetypes = filtyp,
                                     initialdir = self.initialdir)
                            #initialdir = self.appli.CONFIGURATION.initialdir)
                            #initialdir = self.appli.CONFIGURATION.rep_user)
      if sauvegarde :
          if not save_in_file(sauvegarde,self.jdc_fini,None) :
              showinfo("Erreur","Problème à la sauvegarde du fichier "+`sauvegarde`)
              return 0
          else :
              if self.appli.format_fichier.get() == 'homard':
                  self.save_homard(sauvegarde,self.jdc_homard)
              self.JDCDisplay_courant.stop_modif()
              self.appli.affiche_infos("Sauvegarde effectuée")
              if sauvegarde != self.JDCDisplay_courant.fichier :
                  # l'utilisateur a sauvegardé le JDC sous un autre nom
                  self.JDCDisplay_courant.fichier = sauvegarde
                  self.JDCName = self.JDC.nom = stripPath(sauvegarde)
                  self.JDC.changefichier(sauvegarde)
                  self.changeNomPage()
              return 1
      else :
          return 0

   def changeNomPage(self):
      """ Change le nom de l'onglet contenant le JDC courant : en fait détruit l'actuel
          et recrée un autre onglet à la même place avec le bon nom 
      """
      nom = self.JDCName
      self.JDCDisplay_courant.jdc.nom = nom
      nom_page = self.nb.getcurselection()
      num_page = self.nb.index(nom_page)
      tab = self.nb.tab(num_page)
      tab.configure(text = nom)

   def exitEFICAS(self,event=None):
      """
          Permet de sortir d'EFICAS en demandant à l'utilisateur
          s'il veut sauvegarder les modifications en cours
      """
      liste = self.GetListeJDCaSauvegarder()
      if liste != [] :
          # Certains fichiers n'ont pas été sauvegardés ...
          if askyesno("Enregistrer modifications","Enregistrer les modifications ?") :
              test = self.saveall(liste)
              if test != 1 :
                  return
      if askyesno ("Quitter","Voulez-vous vraiment quitter l'application ?") :
          for JDCDisplay in self.liste_JDCDisplay:
              JDCDisplay.jdc.supprime()
          self.appli.quit()
          return

   def GetListeJDCaSauvegarder(self) :
      """ Retourne parmi la liste de tous les JDC ouverts la liste de ceux qui ont été modifiés """
      if not self.JDCDisplay_courant : return []
      if len(self.liste_JDCDisplay) == 0 : return l
      l = []
      for JDCDisplay in self.liste_JDCDisplay:
          if JDCDisplay.modified == 'o' :
              l.append(JDCDisplay)
      return l

   def copy(self,event=None):
      """
          Lance la copie sur le JDC courant
      """
      if self.JDCDisplay_courant : self.JDCDisplay_courant.doCopy()

   def paste(self,event=None):
      """
           Lance le collage sur le JDC courant
      """
      if self.JDCDisplay_courant : self.JDCDisplay_courant.doPaste()

   def cut(self,event=None):
      """
         Lance le cut sur le JDC courant
      """
      if self.JDCDisplay_courant: self.JDCDisplay_courant.doCut()

   def delete(self):
      """
          Lance la suppression du noeud courant
      """
      if not self.JDCDisplay_courant : return
      self.JDCDisplay_courant.init_modif()
      self.JDCDisplay_courant.node_selected.delete()

   def visuJDC_py(self,event=None):
      """ 
          Méthode permettant d'afficher dans une fenêtre à part l'écho au 
            format python du jdc courant 
      """
      if not hasattr(self,'JDC') : return
      jdc_fini = self.get_text_JDC('python')
      if jdc_fini == None : return
      Fenetre(self.appli,
              titre = 'fichier '+ self.JDCName + ' à la syntaxe Python',
              texte = jdc_fini)

   def visuJDC(self):
      """ 
          Méthode permettant d'afficher dans une fenêtre à part l'écho au 
            format .comm ou .py du jdc courant 
      """
      if not hasattr(self,'JDC') : return
      titre = 'fichier '+ self.JDCName + ' à la syntaxe '+ self.code
      format=self.appli.format_fichier.get()
      self.jdc_fini = self.get_text_JDC(format)
      if self.jdc_fini == None : return
      self.visu_fichier_cmd = Fenetre(self.appli,titre=titre,texte = self.jdc_fini)

   def get_text_JDC(self,format):
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         g=generator.plugins[format]()
         jdc_formate=g.gener(self.JDC,format='beautifie')
         if not g.cr.estvide():
            self.appli.affiche_infos("Erreur à la generation")
            showerror("Erreur à la generation","EFICAS ne sait pas convertir ce JDC")
            return
         else:
            return jdc_formate
      else:
         # Il n'existe pas c'est une erreur
         self.appli.affiche_infos("Format %s non reconnu" % format)
         showerror("Format %s non reconnu" % format,"EFICAS ne sait pas convertir le JDC en format %s "% format)
         return

   def view_doc(self):
      """
          Permet d'ouvrir le fichier doc U de la commande au format pdf avec Acrobat Reader
          - Ne fonctionne pas sous UNIX (chemin d'accès Acrobat Reader)
          - indication du chemin d'accès aux fichiers pdf à revoir : trop statique
      """
      if not self.JDCDisplay_courant : return
      try:
          cle_doc = self.JDCDisplay_courant.node_selected.item.get_docu()
          if cle_doc == None : return
          cle_doc = string.replace(cle_doc,'.','')
          cle_doc = string.replace(cle_doc,'-','')
          commande = self.appli.CONFIGURATION.exec_acrobat
          nom_fichier = cle_doc+".pdf"
          fichier = os.path.abspath(os.path.join(self.appli.CONFIGURATION.path_doc,nom_fichier))
          if os.name == 'nt':
              os.spawnv(os.P_NOWAIT,commande,(commande,fichier,))
          elif os.name == 'posix':
              script ="#!/usr/bin/sh \n%s %s&" %(commande,fichier)
              pid = os.system(script)
      except AttributeError:
          traceback.print_exc()
          pass

   def visu_a_plat(self,event=None):
      """ 
          Méthode permettant d'afficher dans une fenêtre à part l'écho 'à plat' du jdc courant 
      """
      if not hasattr(self,'JDC') : return
      titre = 'fichier '+ self.JDCName + ' à plat '
      self.jdc_fini = self.get_text_JDC('aplat')
      if self.jdc_fini == None : return
      self.visu_fichier_cmd = Fenetre(self.appli,titre=titre,texte = self.jdc_fini)

   def visu_txt_brut_JDC(self,event=None):
      """
           Méthode permettant d'afficher le jeu de commandes tel qu'il a été passé au JDC
      """
      if not hasattr(self,'JDC') : return
      titre = "fichier de commandes utilisateur"
      #texte = self.JDC.procedure
      #if texte == None:
      if self.JDCDisplay_courant.fichier == None:
            self.appli.affiche_infos("Pas de fichier initial")
            showerror("Impossible de visualiser le fichier initial",
                      "EFICAS ne peut visualiser le fichier initial.\nIl s'agit d'un nouveau JDC")
            return
      f=open(self.JDCDisplay_courant.fichier,'r')
      texte=f.read()
      f.close()
      self.visu_texte_JDC = Fenetre(self.appli,titre=titre,texte=texte)

   def affichage_fichier_ini(self):
      """
           Affichage des valeurs des paramètres relus par Eficas
      """
      self.appli.CONFIGURATION.affichage_fichier_ini()

   def saveall(self,liste):
      """ 
           Sauvegarde tous les JDC contenus dans liste 
      """
      test = 1
      for JDCDisplay in liste :
          self.JDCDisplay_courant=JDCDisplay
          self.JDC = JDCDisplay.jdc
          test = test * self.saveJDC(echo = 'non')
      return test

   def save_homard(self,nom,texte):
       file_homard=nom+'.conf_homard'
       try:
           f=open(file_homard,'w')
           for ligne in texte:
               f.write(ligne)
               f.write('\n')
           f.close()
       except:
           print "Pb a la sauvegarde sous le format homard"
       if hasattr( self.appli, 'salome'):
           import eficasEtude
           self.appli.salome.rangeInStudy(file_homard,"_CONF")

# ---------------------------------------------------------------------------
#     			Méthodes liées aux mots-clés inconnus
# ---------------------------------------------------------------------------

   def mc_inconnus(self):
      l_mc = self.JDCDisplay_courant.jdc.get_liste_mc_inconnus()
      o = fenetre_mc_inconnus(l_mc)
      l = o.wait_new_list()
      #print "mc_inconnus_new_list: ",l
      #CCAR: Il n' y a pas de retour vers le JDC

   def aideEFICAS(self,event=None):
      AIDE.go(master=self.parent)

   def update_jdc_courant(self):
      self.JDCDisplay_courant.update()

