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
import os,string
import traceback
import Pmw
from tkFileDialog import askopenfilename,asksaveasfilename
from tkMessageBox import showinfo,askyesno,showerror

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

class BUREAU:
   menu_defs=[
              ('Fichier',[
                           ('Nouveau','newJDC'),
                           ('Ouvrir','openJDC'),
                           ('Enregistrer','saveJDC'),
                           ('Enregistrer sous','saveasJDC'),
                           None,
                           ('Fermer','closeJDC'),
                           ('Quitter','exitEFICAS'),
                         ]
              ),
              ('Edition',[
                           ('Copier','copy'),
                           ('Couper','cut'),
                           ('Coller','paste'),
                         ]
              ),
              ('Jeu de commandes',[
                                   ('Rapport de validation','visuCRJDC'),
                                   ('Fichier � plat','visu_a_plat'),
                                   ('Fichier .py','visuJDC_py'),
                                   ('Fichier source','visu_txt_brut_JDC'),
                                   ('Param�tres Eficas','affichage_fichier_ini'),
                                   ('Mots-cl�s inconnus','mc_inconnus'),
                                  ]
              ),
             ]

   button_defs  =      (('New24',"newJDC","Cr�ation d'un nouveau fichier",'always'),
                        ('Open24',"openJDC","Ouverture d'un fichier existant",'always'),
                        ('Save24',"saveJDC","Sauvegarde du fichier courant",'always'),
                        ('Zoom24',"visuJDC","Visualisation du fichier de commandes",'always'),
                        None,
                        ('Copy24',"copy","Copie l'objet courant",'jdc'),
                        ('Cut24',"cut","Coupe l'objet courant",'jdc'),
                        ('Paste24',"paste","Colle l'objet copi� apr�s l'objet courant",'jdc'),
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
      splash._splash.configure(text = "Cr�ation du bureau")
      self.nb = Pmw.NoteBook(self.parent,raisecommand=self.selectJDC)
      self.nb.pack(fill='both',expand=1)
      self.JDCDisplay_courant=None
      self.fileName=None
      self.liste_JDCDisplay=[]
      self.cree_cataitem()

   def cree_cataitem(self):
      """
          On r�cup�re dans l'appli_composant readercata les variables 
          qui servent par la suite pour la cr�ation des JDC
      """
      self.cataitem=self.appli.readercata.cataitem
      self.cata=self.appli.readercata.cata
      self.cata_ordonne_dico=self.appli.readercata.cata_ordonne_dico
      self.code=self.appli.readercata.code
      self.version_code=self.appli.readercata.version_code
      self.fic_cata=self.appli.readercata.fic_cata

   def selectJDC(self,event=None):
      """
          Cette m�thode est appel�e chaque fois que l'on s�lectionne 
          l'onglet d'un JDC dans le NoteBook des JDC.
          Elle permet de stocker dans les variable self.JDC et 
          self.JDCDisplay_courant les valeurs concernant le JDC courant
      """
      if len(self.liste_JDCDisplay) == 0 : return
      #if self.JDCDisplay_courant : self.JDCDisplay_courant.jdc.unset_context()
      numero_jdc = self.nb.index(self.nb.getcurselection())
      self.JDCDisplay_courant = self.liste_JDCDisplay[numero_jdc]
      self.JDC = self.JDCDisplay_courant.jdc
      #self.JDC.set_context()
      self.JDCName = self.JDC.nom

   def newJDC(self):
      """
          Initialise un nouveau JDC vierge
      """
      self.appli.statusbar.reset_affichage_infos()

      CONTEXT.unset_current_step()
      J=self.cata[0].JdC(cata=self.cata,
                         cata_ord_dico=self.cata_ordonne_dico,
                         appli=self.appli)
      self.JDCName=J.nom
      self.fileName=None
      self.ShowJDC(J,self.JDCName)
      self.appli.toolbar.active_boutons()

   def ShowJDC(self,JDC,nom,label_onglet=None):
      """
          Lance l'affichage du JDC cad cr�ation du JDCDisplay
          Rajoute le JDCDisplay � la liste des JDCDisplay si label_onglet == None cad si on cr�e
          bien un nouveau JDCDisplay et non si on remplace (renommage de l'onglet)
      """
      self.JDC=JDC
      self.JDCName = self.JDC.nom = nom
      #XXX CCAR: pour le moment mis en commentaire
      #self.JDC.set_context()
      if label_onglet == None :
          label_onglet = self.GetLabelJDC()
          self.nb.add(label_onglet,tab_text = nom,tab_width=20)
          new = 'oui'
      else :
          new = 'non'
      self.JDCDisplay_courant=JDCDISPLAY(self.JDC,nom,appli=self.appli,parent=self.nb.page(label_onglet))
      if new == 'oui':
          self.liste_JDCDisplay.append(self.JDCDisplay_courant)
      self.JDCDisplay_courant.modified='n'
      self.JDCDisplay_courant.fichier=self.fileName
      self.nb.selectpage(label_onglet)
      self.nb.setnaturalsize()
      texte = "Jeu de commandes :" + self.JDCName+" ouvert"
      self.appli.affiche_infos(texte)

   def closeJDC (self) :
      """
      Ferme le JDC courant et d�truit l'onglet associ� dans le notebook self.nb
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
      self.JDCDisplay_courant.jdc.supprime()
      self.liste_JDCDisplay.remove(self.JDCDisplay_courant)
      self.nb.delete(self.nb.getcurselection())
      #XXX CCAR: pour le moment mis en commentaire
      #self.JDC.unset_context()
      self.JDC = None
      try:
          index = self.nb.index(self.nb.getcurselection())
          self.JDCDisplay_courant = self.liste_JDCDisplay[index]
          self.JDC = self.JDCDisplay_courant.jdc
      except:
          self.JDCDisplay_courant = None
          self.appli.toolbar.inactive_boutons()

   def visuCRJDC(self):
      return self.visuCR(mode='JDC')

   def visuCR(self,mode):
      """
      M�thode permettant l'affichage du rapport de validation
      """
      if mode == 'JDC':
          if not hasattr(self,'JDC') : return
          titre="rapport de validation du jeu de commandes courant"
          cr = self.JDC.report()
      elif mode == 'CATA':
          from Noyau.N_CR import CR
          cr = CR()
          cr.debut = "D�but rapport de validation du catalogue"
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

   def openJDC(self,file=None):
      """
          Demande � l'utilisateur quel JDC existant il veut ouvrir
      """
      if self.code == 'ASTER':
          filetypes = ( ("format "+self.appli.format_fichier.get(), ".comm"),("Tous",'*'))
      else:
          filetypes = ( ("format "+self.appli.format_fichier.get(), ".py"),)
      if not hasattr(self,'initialdir'):
         #self.initialdir = self.appli.CONFIGURATION.rep_user
         self.initialdir = self.appli.CONFIGURATION.initialdir
      if not file :
          file = askopenfilename(title="Ouverture d'un fichier de commandes Aster",
                                 defaultextension=".comm",
                                 filetypes = filetypes,
                                 initialdir = self.initialdir)
      if file != '':
          self.fileName = file
          e=extension_fichier(file)
          self.JDCName=stripPath(file)
          self.initialdir = os.path.dirname(file)
      else :
          return
      #XXX CCAR: pour le moment mis en commentaire
      #if self.JDCDisplay_courant:self.JDCDisplay_courant.jdc.unset_context()

      format=self.appli.format_fichier.get()
      # Il faut convertir le contenu du fichier en fonction du format
      if convert.plugins.has_key(format):
         # Le convertisseur existe on l'utilise
         p=convert.plugins[format]()
         p.readfile(file)
         text=p.convert('exec')
         if not p.cr.estvide(): 
            self.appli.affiche_infos("Erreur � la conversion")
            Fenetre(self.appli,
                    titre="compte-rendu d'erreurs, EFICAS ne sait pas convertir ce fichier",
                    texte = str(p.cr)).wait()
            return
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
                         nom = self.JDCName)
      J.analyse()
      txt_exception = J.cr.get_mess_exception()
      if txt_exception :
          # des exceptions ont �t� lev�es � la cr�ation du JDC 
          # --> on affiche les erreurs mais pas le JDC
          self.appli.affiche_infos("Erreur fatale au chargement de %s" %file)
          showerror("Erreur fatale au chargement d'un fichier",txt_exception)
      else:
          self.ShowJDC(J,self.JDCName)
          self.appli.toolbar.active_boutons()
	  # si le JDC ne contient rien (vide), on retourne ici
	  if len(self.JDC.etapes) == 0 : return
	  # dans le cas o� le JDC est invalide, on affiche son CR
	  cr = self.JDC.report()
	  if not cr.estvide() : 
	     self.appli.top.update()
	     self.visuCR(mode='JDC')


   def GetLabelJDC(self,nb_jdc = 'absent'):
      """
      Retourne le label de l'onglet du NoteBook associ� au JDC � afficher
      """
      if nb_jdc == 'absent':
          nb_jdc = len(self.nb.pagenames())
      nb_jdc = nb_jdc+1
      label_onglet = 'JDC'+`nb_jdc`
      if label_onglet not in self.nb.pagenames() :
          return label_onglet
      else :
          return self.GetLabelJDC(nb_jdc)

   def saveasJDC(self):
      """ 
           Sauvegarde le JDC courant en demandant imp�rativement � l'utilisateur de
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
      if not hasattr(self,'JDC') : return 0
      format=self.appli.format_fichier.get()
      if generator.plugins.has_key(format):
         # Le generateur existe on l'utilise
         g=generator.plugins[format]()
         jdc_formate=g.gener(self.JDC,format='beautifie')
         if not g.cr.estvide():
            print g.cr
            self.appli.affiche_infos("Erreur � la generation")
            showerror("Erreur � la generation","EFICAS ne sait pas convertir ce JDC")
            return
      else:
         # Il n'existe pas c'est une erreur
         self.appli.affiche_infos("Format %s non reconnu" % format)
         showerror("Format %s non reconnu" % format,"EFICAS ne sait pas convertir le JDC")
         return
      self.jdc_fini = string.replace(jdc_formate,'\r\n','\n')

      if echo =='oui' or self.JDCDisplay_courant.fichier == None:
          return self.asknomsauvegardeJDC()
      elif self.JDCDisplay_courant.fichier != None :
          # le JDC a d�j� un nom : on sauvegarde directement sans demander
          # un autre nom au d�veloppeur
          if not save_in_file(self.JDCDisplay_courant.fichier,self.jdc_fini) :
              showinfo("Erreur","Probl�me � la sauvegarde du fichier :" + `self.JDCDisplay_courant.fichier`)
              return 0
          else :
              self.JDCDisplay_courant.stop_modif()
              self.appli.affiche_infos("sauvegarde de "+`self.JDCDisplay_courant.fichier`+" effectu�e")
              return 1

   def asknomsauvegardeJDC(self):
      """ Demande � l'utilsateur le nom sous lequel il veut sauvegarder le JDC courant """
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
                                     initialdir = self.appli.CONFIGURATION.initialdir)
                                     #initialdir = self.appli.CONFIGURATION.rep_user)
      if sauvegarde != '':
          if not save_in_file(sauvegarde,self.jdc_fini) :
              showinfo("Erreur","Probl�me � la sauvegarde du fichier "+`sauvegarde`)
              return 0
          else :
              self.JDCDisplay_courant.stop_modif()
              self.appli.affiche_infos("Sauvegarde effectu�e")
              if sauvegarde != self.JDCDisplay_courant.fichier :
                  # l'utilisateur a sauvegard� le JDC sous un autre nom
                  self.JDCDisplay_courant.fichier = sauvegarde
                  self.JDCName = self.JDC.nom = stripPath(sauvegarde)
                  self.changeNomPage()
              return 1
      else :
          return 0

   def changeNomPage(self):
      """ Change le nom de l'onglet contenant le JDC courant : en fait d�truit l'actuel
          et recr�e un autre onglet � la m�me place avec le bon nom 
      """
      nom = self.JDCName
      self.JDCDisplay_courant.jdc.nom = nom
      nom_page = self.nb.getcurselection()
      num_page = self.nb.index(nom_page)
      tab = self.nb.tab(num_page)
      tab.configure(text = nom)

   def exitEFICAS(self):
      """
          Permet de sortir d'EFICAS en demandant � l'utilisateur
          s'il veut sauvegarder les modifications en cours
      """
      liste = self.GetListeJDCaSauvegarder()
      if liste != [] :
          # Certains fichiers n'ont pas �t� sauvegard�s ...
          if askyesno("Enregistrer modifications","Enregister les modifications ?") :
              test = self.saveall(liste)
              if test != 1 :
                  return
      if askyesno ("Quitter","Voulez-vous vraiment quitter l'application ?") :
          for JDCDisplay in self.liste_JDCDisplay:
              JDCDisplay.jdc.supprime()
          self.appli.quit()
          return

   def GetListeJDCaSauvegarder(self) :
      """ Retourne parmi la liste de tous les JDC ouverts la liste de ceux qui ont �t� modifi�s """
      if not self.JDCDisplay_courant : return []
      if len(self.liste_JDCDisplay) == 0 : return l
      l = []
      for JDCDisplay in self.liste_JDCDisplay:
          if JDCDisplay.modified == 'o' :
              l.append(JDCDisplay)
      return l

   def copy(self):
      """
          Lance la copie sur le JDC courant
      """
      if self.JDCDisplay_courant : self.JDCDisplay_courant.doCopy()

   def paste(self):
      """
           Lance le collage sur le JDC courant
      """
      if self.JDCDisplay_courant : self.JDCDisplay_courant.doPaste()

   def cut(self):
      """
         Lance le cut sur le JDC courant
      """
      if self.JDCDisplay_courant: self.JDCDisplay_courant.doCut()

   def delete(self):
      """
          Lance la suppression du noeud courant
      """
      if not self.JDCDisplay_courant : return
      try:
          if self.JDCDisplay_courant.modified == 'n' : 
             self.JDCDisplay_courant.init_modif()
          pere = self.JDCDisplay_courant.node_selected.parent
          self.JDCDisplay_courant.node_selected.delete()
          pere.select()
      except AttributeError:
          pass

   def visuJDC_py(self):
      """ 
          M�thode permettant d'afficher dans une fen�tre � part l'�cho au 
            format python du jdc courant 
      """
      if not hasattr(self,'JDC') : return
      jdc_fini = self.get_text_JDC('python')
      if jdc_fini == None : return
      Fenetre(self.appli,
              titre = 'fichier '+ self.JDCName + ' � la syntaxe Python',
              texte = jdc_fini)

   def visuJDC(self):
      """ 
          M�thode permettant d'afficher dans une fen�tre � part l'�cho au 
            format .comm ou .py du jdc courant 
      """
      if not hasattr(self,'JDC') : return
      titre = 'fichier '+ self.JDCName + ' � la syntaxe '+ self.code
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
            print g.cr
            self.appli.affiche_infos("Erreur � la generation")
            showerror("Erreur � la generation","EFICAS ne sait pas convertir ce JDC")
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
          - Ne fonctionne pas sous UNIX (chemin d'acc�s Acrobat Reader)
          - indication du chemin d'acc�s aux fichiers pdf � revoir : trop statique
      """
      if not self.JDCDisplay_courant : return
      try:
          cle_doc = self.JDCDisplay_courant.node_selected.item.get_docu()
          if cle_doc == None : return
          cle_doc = string.replace(cle_doc,'.','')
          cle_doc = string.replace(cle_doc,'-','')
          commande = self.appli.CONFIGURATION.exec_acrobat
          nom_fichier = cle_doc+".pdf"
          rep_fichier = cle_doc[0:2]
          fichier = os.path.abspath(os.path.join(self.appli.CONFIGURATION.path_doc,rep_fichier,nom_fichier))
          if os.name == 'nt':
              os.spawnv(os.P_NOWAIT,commande,(commande,fichier,))
          elif os.name == 'posix':
              script ="#!/usr/bin/sh \n%s %s&" %(commande,fichier)
              pid = os.system(script)
      except AttributeError:
          traceback.print_exc()
          pass

   def visu_a_plat(self):
      """ 
          M�thode permettant d'afficher dans une fen�tre � part l'�cho '� plat' du jdc courant 
      """
      if not hasattr(self,'JDC') : return
      titre = 'fichier '+ self.JDCName + ' � plat '
      self.jdc_fini = self.get_text_JDC('aplat')
      if self.jdc_fini == None : return
      self.visu_fichier_cmd = Fenetre(self.appli,titre=titre,texte = self.jdc_fini)

   def visu_txt_brut_JDC(self):
      """
           M�thode permettant d'afficher le jeu de commandes tel qu'il a �t� pass� au JDC
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
           Affichage des valeurs des param�tres relus par Eficas
      """
      self.appli.CONFIGURATION.affichage_fichier_ini()

   def saveall(self,liste):
      """ 
           Sauvegarde tous les JDC contenus dans liste 
      """
      test = 1
      for JDCDisplay in liste :
          self.JDC = JDCDisplay.jdc
          test = test * self.saveJDC(echo = 'non')
      return test


# ---------------------------------------------------------------------------
#     			M�thodes li�es aux mots-cl�s inconnus
# ---------------------------------------------------------------------------

   def mc_inconnus(self):
      l_mc = self.JDCDisplay_courant.jdc.get_liste_mc_inconnus()
      o = fenetre_mc_inconnus(l_mc)
      l = o.wait_new_list()
      #print "mc_inconnus_new_list: ",l
      #CCAR: Il n' y a pas de retour vers le JDC

   def aideEFICAS(self):
      AIDE.go(master=self.parent)
