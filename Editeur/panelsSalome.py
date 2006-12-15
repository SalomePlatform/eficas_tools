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
from plusieursbasepanel import PLUSIEURS_BASE_OR_UNELISTE_Panel
from uniquesdcopanel    import UNIQUE_SDCO_Panel
from uniqueassdpanel    import UNIQUE_ASSD_Panel
from uniqueintopanel    import UNIQUE_INTO_Panel
from uniquecomppanel    import UNIQUE_COMP_Panel
from uniquebasepanel    import UNIQUE_BASE_Panel
from uniqueassdpanel    import UNIQUE_ASSD_Panel_Reel

from Noyau.N_CR import justify_text

import traceback
import salome           # CS_pbruno à poubelliser
import images



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
#        - LIRE_MAILLAGE_UNITE 
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
#        - AFFE_CHAR_MECA_DDL_IMPO_GROUP_NO
# Methodes surchargées :  
#        - makeValeurPage(self,page)
#
# ------------------------------------------------------------------------------#

class SALOME_PLUSIEURS_BASE_OR_UNELISTE_Panel(PLUSIEURS_BASE_OR_UNELISTE_Panel):
      ""        

class SALOME_PLUSIEURS_BASE_Panel(PLUSIEURS_BASE_Panel):

  def __init__(self,parent,panneau,node):
      PLUSIEURS_BASE_Panel.__init__( self, parent, panneau, node )
      #self.selected_valeur = None
      
  def add_valeur_plusieurs_base(self,name=None):
      try: 
        valeur,validite,commentaire=self.get_valeur()
        if not valeur: # sélection dans salome        
            strSelection = ''
            
            genea=self.node.item.get_genealogie()
            kwType = None
            for e in genea:
                if "GROUP_NO" in e:
                    kwType = "GROUP_NO"
                if "GROUP_MA" in e:
                    kwType = "GROUP_MA"            
                
            selection, msg = self.parent.appli.selectGroupFromSalome(kwType)
            if selection:
                for oneSelection in selection:
                    strSelection +=str( oneSelection )
                    strSelection +=','
                            
                strSelection = strSelection.rstrip(',')
                self.display_valeur( strSelection )                
                    
        PLUSIEURS_BASE_Panel.add_valeur_plusieurs_base( self, name )
        if msg:
            self.parent.appli.affiche_infos(msg)
        self.erase_valeur()
      except:
        print ' erreur  add_valeur_plusieurs_base' #CS_pbruno : afficher boite de dialogue ici ?          
        
  def makeValeurPage(self,page):
      """
      Crée la page de saisie d'une liste de valeurs à priori quelconques,
      cad qui ne sont  pas à choisir dans une liste prédéfinie
      """      
      PLUSIEURS_BASE_Panel.makeValeurPage(self,page)
      self.c = Button( self.frame_choix, text='Visualiser',command=self.displayInSalomeGeom )      
      self.c.place( relx=0.3, rely=0.0,relwidth=0.55)
      
      
  def displayInSalomeGeom( self ):
      if self.selected_valeur:        
        ok, msgError = self.parent.appli.displayShape( self.selected_valeur )
        if not ok:
            self.parent.appli.affiche_infos(msgError)
      
      


# ------------------------------------------------------------------------------#
# classe SALOME_UNIQUE_BASE_Panel
#
# Commandes modifiées  :  
#        - LIRE_MAILLAGE_UNITE 
# Methodes surchargées :  
#        - makeValeurPage(self,page)
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
              self.entry.delete(0,END)
              self.entry2.delete(0,END)
              self.entry.insert(0,FileName)
              self.entry2.insert(0,FileName)
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
          self.entry.delete(0,END)
          self.entry2.delete(0,END)
          self.entry.insert(0,EntryName)
          self.entry2.insert(0,EntryName)
          self.valid_valeur()

  def SALOME_DONNEES_HOMARD_FICHIER_MED_MAILLAGE_NP1(self):
      self.SALOME_DONNEES_HOMARD_FICHIER_MED_MAILLAGE_N()

  def SALOME_DEFI_GROUP_CREA_GROUP_MA_GROUP_MA(self):
      #try: 
      if ( 1 == 1 ) :
        selection, msg = self.parent.appli.selectGroupFromSalome()
        if selection:
           strSelection =str( selection )
           UNIQUE_BASE_Panel.valid_valeur(self,strSelection)
        if msg:
            self.parent.appli.affiche_infos(msg)
        self.erase_valeur()
      #except:
      else :
        print ' erreur  '
        

  def redistribue_selon_simp(self):
      genea = self.node.item.get_genealogie()
      commande="SALOME"
      for i in range(0,len( genea )) :
        commande=commande+"_"+ genea[i]
      # --------------------------------------------------------------
      # on verifie que la methode n est pas particularise
      # sinon on appelle SALOME_DEFI_GROUP_CREA_GROUP_MA_GROUP_MA qui
      # sert comme methode par defaut 
      # --------------------------------------------------------------
      try :
        SALOME_UNIQUE_BASE_Panel.__dict__[commande](self)
      except :
         SALOME_UNIQUE_BASE_Panel.SALOME_DEFI_GROUP_CREA_GROUP_MA_GROUP_MA(self)



  def makeValeurPage(self,page):
      """
      Crée la page de saisie d'une valeur à priori quelconque,
      cad qui ne sont  pas à choisir dans une liste prédéfinie
      Ajout d'un bouton pour selectionner  à partir de Salome  
      """      
      UNIQUE_BASE_Panel.makeValeurPage(self,page)
      self.b = Button(self.frame_valeur,text='Relier selection',command=self.redistribue_selon_simp)
      self.b.place(relx=0.28,rely=0.4,relwidth=0.4)

#---------------------------------------------------------------------------------------
# Correspondances entre les classes eficas et les classes salome_eficas 
#______________________________________________________________________________________
dict_classes_salome = { SHELLPanel : SALOME_SHELLPanel, 
                          FONCTION_Panel       : SALOME_FONCTION_Panel,
                          PLUSIEURS_INTO_Panel : SALOME_PLUSIEURS_INTO_Panel,
                          PLUSIEURS_ASSD_Panel : SALOME_PLUSIEURS_ASSD_Panel,
                          PLUSIEURS_BASE_Panel : SALOME_PLUSIEURS_BASE_Panel,
                          PLUSIEURS_BASE_OR_UNELISTE_Panel : SALOME_PLUSIEURS_BASE_OR_UNELISTE_Panel,
                          UNIQUE_INTO_Panel :  SALOME_UNIQUE_INTO_Panel,
                          UNIQUE_SDCO_Panel : SALOME_UNIQUE_SDCO_Panel,
                          UNIQUE_ASSD_Panel : SALOME_UNIQUE_ASSD_Panel,
                          UNIQUE_ASSD_Panel_Reel : SALOME_UNIQUE_ASSD_Panel_Reel,
                          UNIQUE_COMP_Panel : SALOME_UNIQUE_COMP_Panel,
                          UNIQUE_BASE_Panel : SALOME_UNIQUE_BASE_Panel}

dict_geom_numgroupe = { }
dict_geom_numface = { }
