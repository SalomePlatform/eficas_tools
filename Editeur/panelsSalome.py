# -*- coding: utf-8 -*-
print "Import de panelsSalome"

from Tkinter import *
from widgets import ListeChoix
from widgets import showerror

from fonctionpanel      import FONCTION_Panel
from shellpanel         import SHELLPanel
from plusieursintopanel import PLUSIEURS_INTO_Panel
from plusieursassdpanel import PLUSIEURS_ASSD_Panel
from plusieursbasepanel import PLUSIEURS_BASE_Panel
from uniquesdcopanel    import UNIQUE_SDCO_Panel
from uniqueassdpanel    import UNIQUE_ASSD_Panel
from uniqueintopanel    import UNIQUE_INTO_Panel
from uniquecomppanel    import UNIQUE_COMP_Panel
from uniquebasepanel    import UNIQUE_BASE_Panel
from uniqueassdpanel    import UNIQUE_ASSD_Panel_Reel

from Noyau.N_CR import justify_text

import traceback
import SalomePyQt
import salome
import images
import SMESH_utils
sgQt=SalomePyQt.SalomePyQt()



# 2 types de commandes vont etre particularisees dans Salome
#
# - un cas general : 
# Toutes les commandes possedant GROUP_NO ou GROUP_MA
# seront surchargees d office
# pour cela on va utiliser le dictionnaire dict_classes_salome
# qui va permettre de changer la classe de la commande
# ainsi si un panel en dehors de salome a pour classe PLUSIEURS_BASE_Panel
# la classe de ce panel devient alors SALOME_PLUSIEURS_BASE_Panel
# (pour cela voir composimp)

# des commandes "autres" ne pouvant pas etre identifiées par leur nom 
# il suffit de creer dans la classe SALOME de la commande
# une fonction portant son nom 
# Exemple de particularisation d un panel :
# Supposons que l on veuille particulariser la commande
#	- LIRE_MAILLAGE_UNITE 
# le panel initial a pour classe UNIQUE_BASE_Panel
# il suffit d'ajouter dans la classe derivée SALOME_UNIQUE_BASE_Panel
# une fonction  SALOME_LIRE_MAILLAGE_UNITE
# la classe de ce panel devient alors SALOME_UNIQUE_BASE_Panel
# on peut surcharger les methodes nécessaires (affichage par exemple)  


class SALOME_SHELLPanel (SHELLPanel):
	""

class SALOME_FONCTION_Panel (FONCTION_Panel):
	""

class SALOME_PLUSIEURS_INTO_Panel (PLUSIEURS_INTO_Panel):
	""

class SALOME_PLUSIEURS_ASSD_Panel (PLUSIEURS_ASSD_Panel):
	""

class SALOME_UNIQUE_INTO_Panel (UNIQUE_INTO_Panel):
	""

class SALOME_UNIQUE_SDCO_Panel (UNIQUE_SDCO_Panel):
	""

class SALOME_UNIQUE_ASSD_Panel (UNIQUE_ASSD_Panel):
	""

class SALOME_UNIQUE_COMP_Panel (UNIQUE_COMP_Panel):
	""

class SALOME_UNIQUE_ASSD_Panel_Reel (UNIQUE_ASSD_Panel_Reel):
	""

# ------------------------------------------------------------------------------#
# classe SALOME_PLUSIEURS_BASE_Panel
#
# Commandes modifiées  :  
#	- AFFE_CHAR_MECA_DDL_IMPO_GROUP_NO
# Methodes surchargées :  
#	- makeValeurPage(self,page)
#
# ------------------------------------------------------------------------------#

class SALOME_PLUSIEURS_BASE_Panel(PLUSIEURS_BASE_Panel):


  def convertit_group_no_from_salome(self,liste_in):
      newr=[]
      #try:
      if ( 1 == 1 ) :
	  for entree in liste_in :
	       travail=[]
	       travail.append(entree)
	       entryname_list=SMESH_utils.entryToName(salome.myStudy,travail)
               entreeName=entryname_list[0]
	       if dict_geom_numgroupe.has_key(entreeName):
		   r=dict_geom_numgroupe[entreeName]
	       else:
                   r=SMESH_utils.getAsterGroupNo(salome.myStudy,travail)
		   dict_geom_numgroupe[entreeName]=r
               for i in r :
                   newr.append(i)
      #except:
      else :
	   print "pas de groupe de noeuds associé"
	   showerror("Pas de groupe associé","Cet Objet ne peut pas être défini comme un ensemble de groupe de noeuds")
      return newr

  def convertit_group_maille_from_salome(self,liste_in):
      newr=[]
      #try:
      if [ 1 == 1 ]:
          print liste_in
	  for entree in liste_in :
	       travail=[]
	       travail.append(entree)
	       entryname_list=SMESH_utils.entryToName(salome.myStudy,travail)
               entreeName=entryname_list[0]
	       if dict_geom_numgroupe.has_key(entreeName):
		   r=dict_geom_numgroupe[entreeName]
	       else:
                   r=SMESH_utils.getAsterGroupMa(salome.myStudy,travail)
		   dict_geom_numgroupe[entreeName]=r
	       if r != None :
                   for i in r :
                      newr.append(i)
      #except:
      else :
	   print "pas de groupe de maille associé"
	   showerror("Pas de groupe associé","Cet Objet ne peut pas être défini comme un ensemble de groupe de maille")
      return newr

  def convertit_entrees_en_valeurs(self,entrychaine):
      if SALOME_PLUSIEURS_BASE_Panel.__dict__.has_key(self.clef_fonction):
           valeur=apply(SALOME_PLUSIEURS_BASE_Panel.__dict__[self.clef_fonction],(self,entrychaine))
      else :
           if (self.clef_fonction.find("GROUP_NO") != -1) and (self.clef_fonction.find("GROUP_MA") != -1) :
              if (self.clef_fonction.find("GROUP_NO") < self.clef_fonction.find("GROUP_MA")) :
		valeur=self.convertit_group_maille_from_salome(entrychaine)
	      else :
		valeur=self.convertit_group_no_from_salome(entrychaine)  
	   elif self.clef_fonction.find("GROUP_NO") != -1 :
	       valeur=self.convertit_group_no_from_salome(entrychaine)
	   else :
	       if self.clef_fonction.find("GROUP_MA") != -1 :
		   valeur=self.convertit_group_maille_from_salome(entrychaine)
	       else :
		    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		    print "Pb pas de fonction de conversion de la valeur Salome en valeur Aster"
		    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                    valeur=[]
      print "VALEUR", valeur
      return valeur

  def sup_valeur_from_salome(self,name=None):
      """
      Méthode qui sert à retirer de la liste des valeurs la valeur sélectionnée
      """
      liste_valeurs = self.Liste_valeurs.get_liste()
      liste_valeurs_salome=self.Liste_valeurs_salome.get_liste()
      entrychaine=salome.sg.getAllSelected()

      try:
          valeur = self.convertit_entrees_en_valeurs(entrychaine)
          for i in valeur :
            if i in liste_valeurs :
          	liste_valeurs.remove(i)
                print "enleve" , i
      except:
          # la valeur sélectionnée n'est pas dans la liste
          pass

      entryname_list=SMESH_utils.entryToName(salome.myStudy,entrychaine)
      self.entrygroupe.delete(0,END)
      self.sortie.delete(0,END)
      for entryname in entryname_list:
          try:
	     liste_valeurs_salome.remove(entryname)
	  except:
	     print "la valeur ", entryname, "n est pas dans la liste"
	  entryname=entryname + " "
          self.sortie.insert(0,entryname)
      self.selected_valeur = None
      self.Liste_valeurs.put_liste(liste_valeurs)
      self.Liste_valeurs_salome.put_liste(liste_valeurs_salome)
      self.recalcule()

  def visu_in_salome(self):
      liste_valeurs = self.Liste_valeurs.get_liste()
      entryname_list=SMESH_utils.VisuGroupe(salome.myStudy,liste_valeurs)

  def visu3D_in_salome(self):
      liste_valeurs = self.Liste_valeurs.get_liste()
      entryname_list=SMESH_utils.VisuGroupe(salome.myStudy,liste_valeurs)

  def recalcule(self):
      liste_valeurs_salome=self.Liste_valeurs_salome.get_liste()
      groups={}
      liste_valeurs = self.Liste_valeurs.get_liste()
      for valeur in liste_valeurs_salome:
	  r=dict_geom_numgroupe[valeur]
          for i in r :
              if i not in liste_valeurs :
          	  liste_valeurs.append(i)
      self.Liste_valeurs.put_liste(liste_valeurs)

  def add_valeur_from_salome(self,name=None):
       entrychaine=salome.sg.getAllSelected()
       self.sortie.delete(0,END)
       self.entrygroupe.delete(0,END)
       if entrychaine != '':
          entryname_list=SMESH_utils.entryToName(salome.myStudy,entrychaine)
          touteslesvaleurs = self.convertit_entrees_en_valeurs(entrychaine)
         
          valeur=[]
          liste_valeurs  = self.Liste_valeurs.get_liste()
          for i in touteslesvaleurs:
              if i not in liste_valeurs:
	         valeur.append(i)
	      
          if valeur==[]:
	     entryname_list=[]

          liste_valeurs_salome = self.Liste_valeurs_salome.get_liste()
	  for entryname in entryname_list:
	      if entryname not in liste_valeurs_salome: 
                 liste_valeurs_salome.append(entryname)
	      entryname=entryname + " "
              self.entrygroupe.insert(0,entryname)
          self.Liste_valeurs_salome.put_liste(liste_valeurs_salome)

          if self.node.item.wait_reel():
             print "wait_reel()"
             valeur = self.traite_reel(valeur)
          if self.node.item.wait_geom():
             print "wait_geom()"
             val,test1 = valeur,1
          else:
             print "else wait"
             val,test1 = self.node.item.object.eval_valeur(valeur)

          if test1 :
             test2 = self.node.item.object.verif_type(val)
             if test2 :
                 liste_valeurs = self.Liste_valeurs.get_liste()
                 if len(liste_valeurs) >= max :
                     self.parent.appli.affiche_infos("La liste a déjà atteint le nombre maximum d'éléments, ajout refusé")
                     self.erase_valeur()
                     return
                 if type(val) == type([]):
                   for groupe in val:
                     liste_valeurs.append(groupe)
                 else:
                   liste_valeurs.append(val)
                 self.Liste_valeurs.put_liste(liste_valeurs)
                 self.parent.appli.affiche_infos("Nouvelle valeur acceptée")
             else:
                 self.parent.appli.affiche_infos("Valeur incorrecte : ajout à la liste refusé")
          else:
             print "impossible d'évaluer %s" %val
             self.parent.appli.affiche_infos("Valeur incorrecte : ajout à la liste refusé")

   
  def makeValeurPage(self,page):
      """
      Crée la page de saisie d'une liste de valeurs à priori quelconques,
      cad qui ne sont  pas à choisir dans une liste prédéfinie
      """
      # On récupère la bulle d'aide du panneau, l'objet, l'aide,min et max (cardinalité de la liste),
      # et la liste des valeurs déjà affectées à l'objet courant
      bulle_aide=self.get_bulle_aide()
      objet_mc = self.node.item.get_definition()
      aide = self.get_aide()
      aide = justify_text(texte=aide)
      min,max = self.node.item.GetMinMax()
      self.clef_fonction=  self.node.item.clef_fonction
      l_valeurs = self.node.item.GetListeValeurs()

      self.frame1 = Frame(page,relief='groove',bd=2)
      self.frame2 = Frame(page)
      self.frame1.place(relx=0.,rely=0.,relwidth=1.,relheight=0.85)
      self.frame2.place(relx=0.,rely=0.85,relwidth=1,relheight=0.15)
      self.frame_right = Frame(self.frame1)
      self.frame_right.place(relx=0.35,rely=0.,relwidth=0.65,relheight=1.)

      # création des frames internes
      self.frame_valeurs = Frame(self.frame1)
      self.frame_valeurs.place(relx=0.0,rely=0.0,relwidth=0.35,relheight=0.95)

      self.frame_choix = Frame(self.frame_right)
      self.frame_choix.place(relx=0.0,rely=0.0,relwidth=1,relheight=0.9)
      self.frame_valeurs_salome = Frame(self.frame_right)
      self.frame_valeurs_salome.place(relx=0.02,rely=0.7,relwidth=0.9,relheight=0.3)

      self.frame_boutons = Frame(self.frame2)
      self.frame_boutons.place(relx=0.1,rely=0.,relwidth=0.5,relheight=1.)
      self.frame_aide = Frame(self.frame2)
      self.frame_aide.place(relx=0.6,rely=0.,relwidth=0.5,relheight=1)

      for fram in (self.frame1,self.frame2,self.frame_right,self.frame_valeurs,
                 self.frame_choix,self.frame_aide,self.frame_boutons):
            fram.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
            fram.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)

      # création des objets dans les frames
      liste_commandes_valeurs = (("<Button-1>",self.selectValeur),
                                 ("<Button-3>",self.deselectValeur),
                                 ("<Double-Button-1>",self.sup_valeur_sans_into))
      self.Liste_valeurs = ListeChoix(self,self.frame_valeurs,l_valeurs,
			              liste_commandes = liste_commandes_valeurs,
                                      titre="Valeur(s) actuelle(s)")

    # PN : pour ajouter les validators
      self.make_entry(frame = self.frame_choix,command = self.add_valeur_plusieurs_base,y=0.55)

      bouton_valeurs_fichier = Button(self.frame_choix,
                                      text="Importer ...",
                                      command=self.select_in_file)
      bouton_valeurs_fichier.place(relx=0.28,rely=0.65,relwidth=0.6)

      self.ajout_valeurs = None
      self.b = Button(self.frame_choix,text='ajout select.',command=self.add_valeur_from_salome)

      self.b.place(relx=0.03,rely=0.05,relwidth=0.35)
      self.entrygroupe = Entry(self.frame_choix,relief='sunken')
      self.entrygroupe.place(relx=0.4,rely=0.05,relwidth=0.6)

      self.a = Button(self.frame_choix,text='enlev. select.',command=self.sup_valeur_from_salome)
      self.a.place(relx=0.03,rely=0.2,relwidth=0.35)
      self.sortie = Entry(self.frame_choix,relief='sunken')
      self.sortie.place(relx=0.4,rely=0.2,relwidth=0.6)
      self.c = Button(self.frame_choix,text='Visualiser',command=self.visu_in_salome)
      self.c.place(relx=0.03,rely=0.35,relwidth=0.35)

      self.genea =self.node.item.get_genealogie()
      print self.genea
      if "AFFE_CARA_ELEM" in self.genea :
         self.d=Button(self.frame_choix,text='Visu 3D',command=self.visu3D_in_salome)
         self.d.place(relx=0.47,rely=0.35,relwidth=0.35)

      l_salome_valeurs=self.node.item.get_salome_valeurs()
      self.Liste_valeurs_salome=ListeChoix(self,self.frame_valeurs_salome,l_salome_valeurs,
					liste_commandes = liste_commandes_valeurs,
                                     	titre="Valeur(s) Salome actuelle(s) ")
      self.Liste_valeurs_salome.affiche_liste()


      # boutons Ajouter et Supprimer
      bouton_add = Button(self.frame_choix,
                          image = images.get_image('arrow_left'),
                          command = self.add_valeur_plusieurs_base)
      bouton_sup = Button(self.frame_choix,
                          image = images.get_image('arrow_right'),
                          command = self.sup_valeur_sans_into)
      bouton_add.place(relx=0.08,rely=0.55)
      bouton_sup.place(relx=0.08,rely=0.65)

      # affichage de l'aide
      self.frame_aide.update()
      self.aide = Label(self.frame_aide, text = aide,
                        justify='center', anchor='center',
                        wraplength=int(self.frame_aide.winfo_width()*0.8))
      self.aide.place(relx=0.5,rely=0.5,anchor='center',relwidth=1)
      self.Liste_valeurs.affiche_liste()

      # boutons Accepter et Annuler
      bouton_accepter = Button(self.frame_boutons,
                               text='Valider',
                               command = lambda s=self,m=min,M=max : s.accepte_modifs_valeur(m,M))
      bouton_annuler = Button(self.frame_boutons,
                              text = 'Annuler',
                              command = self.annule_modifs_valeur)
      for but in (bouton_accepter,bouton_annuler):
          but.pack(side='left',padx=5)



# ------------------------------------------------------------------------------#
# classe SALOME_UNIQUE_BASE_Panel
#
# Commandes modifiées  :  
#	- LIRE_MAILLAGE_UNITE 
# Methodes surchargées :  
#	- makeValeurPage(self,page)
#
# ------------------------------------------------------------------------------#

class SALOME_UNIQUE_BASE_Panel(UNIQUE_BASE_Panel):

# ce dictionnaire va servir lors de la sortie d efficas
# a creer le fichier qui sera integre au config.txt
# pour relier une unite logique et un nom de fichier

  dict_fichier_unite={}


  def SALOME_DONNEES_HOMARD_FICHIER_MED_MAILLAGE_N(self):
      entrychaine=salome.sg.getAllSelected()
      if entrychaine != '':
          self.entry2.delete(0,END)
          try:
              SO = salome.myStudy.FindObjectID(entrychaine[0])
          except:
              boo = 0
              SO = None

          FileName=''
          if SO != None:
              myBuilder = salome.myStudy.NewBuilder()
              boo,FileAttr = myBuilder.FindAttribute(SO,"AttributeFileType")
              if boo:
                 val=FileAttr.Value()
                 if (val !="FICHIERMED" and val != "FICHIER_RESU_MED"):
                     boo=0
                     showerror("Pas de Fichier MED","Cet Objet n a pas de fichier MED Associ\xe9")
                 else:
                     boo,FileAttr = myBuilder.FindAttribute(SO,"AttributeExternalFileDef")
              if boo :
                FileName=FileAttr.Value()
              else:
                 showerror("Pas de Fichier MED","Cet Objet n a pas de fichier MED Associ\xe9")
          if FileName != '' :
              self.entry2.insert(0,FileName)
              self.entry.delete(0,END)
              self.entry.insert(0,FileName)
              self.valid_valeur()


  def SALOME_DONNEES_HOMARD_TRAITEMENT_NOM_MED_MAILLAGE_N(self):
      EntryName=''
      entrychaine=salome.sg.getAllSelected()
      if entrychaine != '':
          self.entry2.delete(0,END)
          try:
              SO = salome.myStudy.FindObjectID(entrychaine[0])
          except:
              boo = 0
              SO = None

          if SO is not None:
	     myBuilder = salome.myStudy.NewBuilder()
             ok, AtName = myBuilder.FindAttribute(SO,"AttributeName")
	     if ok:
		EntryName=AtName.Value()

      if EntryName != '':
          self.entry2.insert(0,EntryName)
          self.entry.delete(0,END)
          self.entry.insert(0,EntryName)
          self.valid_valeur()

  def SALOME_DONNEES_HOMARD_FICHIER_MED_MAILLAGE_NP1(self):
      self.SALOME_DONNEES_HOMARD_FICHIER_MED_MAILLAGE_N()


#  def SALOME_LIRE_MAILLAGE_UNITE(self):

#      unite=self.node.item.get_valeur()
#      entrychaine=salome.sg.getAllSelected()
#      if entrychaine != '':
#	  self.entry2.delete(0,END)

#          try:
#              SO = salome.myStudy.FindObjectID(entrychaine[0])
#          except:
#              boo = 0
#              SO = None

#          if SO != None:
#	      myBuilder = salome.myStudy.NewBuilder()
#              boo,FileAttr = myBuilder.FindAttribute(SO,"AttributeComment")
#
#          FileName=''
#          if SO != None:
#              myBuilder = salome.myStudy.NewBuilder()
#              boo,FileAttr = myBuilder.FindAttribute(SO,"AttributeFileType")
#              if boo:
#                 boo=0
#                 val=FileAttr.Value()
#                 if (val !="FICHIERMED"):
#                     showerror("Pas de Fichier MED","Cet Objet n a pas de fichier MED Associ\xe9")
#                 else:
#                     boo,FileAttr = myBuilder.FindAttribute(SO,"AttributeExternalFileDef")
#          if boo :
#              FileName=FileAttr.Value()
#          else:
#              showerror("Pas de Fichier MED","Cet Objet n a pas de fichier MED Associ\xe9")

#          print "FileName = " , FileName
#          if FileName != '' :
#              self.entry2.insert(0,FileName)
#              typefic='D'
#              SALOME_UNIQUE_BASE_Panel.dict_fichier_unite[unite]=typefic+FileName
#          else :
#              print "il faut afficher une Fenetre d impossibilit\xe9"
#              showerror("Pas de Fichier MED","Cet Objet n a pas de fichier MED Associ\xe9")

  def redistribue_selon_simp(self):
      genea = self.node.item.get_genealogie()
      commande="SALOME"
      for i in range(0,len( genea )) :
        commande=commande+"_"+ genea[i]
      (SALOME_UNIQUE_BASE_Panel.__dict__[commande])(self)


  def makeValeurPage(self,page):
      """
      Génère la page de saisie de la valeur du mot-clé simple courant qui doit être de type
      de base cad entier, réel, string ou complexe
      """
      # Récupération de l'aide associée au panneau, de l'aide destinée à l'utilisateur,
      # et de la liste des SD du bon type (constituant la liste des choix)
      bulle_aide=self.get_bulle_aide()
      aide=self.get_aide()
      aide= justify_text(texte=aide)
      liste_noms_sd = self.node.item.get_sd_avant_du_bon_type()
      # Remplissage du panneau
      self.frame_valeur = Frame(page)
      self.frame_valeur.pack(fill='both',expand=1)
      self.frame_valeur.bind("<Button-3>",lambda e,s=self,a=bulle_aide : s.parent.appli.affiche_aide(e,a))
      self.frame_valeur.bind("<ButtonRelease-3>",self.parent.appli.efface_aide)
      self.label = Label(self.frame_valeur,text='Valeur :')
      self.label.place(relx=0.1,rely=0.5)
      self.entry = Entry(self.frame_valeur,relief='sunken')
      self.entry.place(relx=0.28,rely=0.5,relwidth=0.6)
      self.entry.bind("<Return>",lambda e,c=self.valid_valeur:c())
      self.entry.bind("<KP_Enter>",lambda e,c=self.valid_valeur:c())

      # PN : Ajout d'un bouton pour selectionner  à partir de Salome  
      self.b = Button(self.frame_valeur,text='Relier selection',command=self.redistribue_selon_simp)
      self.b.place(relx=0.05,rely=0.1)
      unite=self.node.item.get_valeur()
      self.entry2 = Entry(self.frame_valeur,relief='sunken')
      self.entry2.place(relx=0.3,rely=0.1)
      self.entry2.configure(width = 250)

      if SALOME_UNIQUE_BASE_Panel.dict_fichier_unite.has_key(unite):
         associe=SALOME_UNIQUE_BASE_Panel.dict_fichier_unite[unite][1:]
	 self.entry2.delete(0,END)
	 if associe != "" :
             self.entry2.insert(0,associe)
      else:
	 self.entry2.delete(0,END)

      # aide associée au panneau
      self.frame_valeur.update()
      self.aide = Label(self.frame_valeur,
                        text = aide,
                        wraplength=int(self.frame_valeur.winfo_width()*0.8),
                        justify='center')
      self.aide.place(relx=0.5,rely=0.7,anchor='n')
      # affichage de la valeur du MCS
      self.display_valeur()

#---------------------------------------------------------------------------------------
# Correspondances entre les classes eficas et les classes salome_eficas 
#______________________________________________________________________________________
dict_classes_salome = { SHELLPanel : SALOME_SHELLPanel, 
                          FONCTION_Panel       : SALOME_FONCTION_Panel,
			  PLUSIEURS_INTO_Panel : SALOME_PLUSIEURS_INTO_Panel,
			  PLUSIEURS_ASSD_Panel : SALOME_PLUSIEURS_ASSD_Panel,
			  PLUSIEURS_BASE_Panel : SALOME_PLUSIEURS_BASE_Panel,
			  UNIQUE_INTO_Panel :  SALOME_UNIQUE_INTO_Panel,
			  UNIQUE_SDCO_Panel : SALOME_UNIQUE_SDCO_Panel,
			  UNIQUE_ASSD_Panel : SALOME_UNIQUE_ASSD_Panel,
			  UNIQUE_ASSD_Panel_Reel : SALOME_UNIQUE_ASSD_Panel_Reel,
			  UNIQUE_COMP_Panel : SALOME_UNIQUE_COMP_Panel,
			  UNIQUE_BASE_Panel : SALOME_UNIQUE_BASE_Panel}

dict_geom_numgroupe = { }
dict_geom_numface = { }
