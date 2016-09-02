
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2007-2013   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

print "version en dur"
from ExtractGeneratorLoadLineandTransfoDico import *
#from ExtractGeneratorLoadLineandTransfoDico import ExtractGeneratorLoadLineandTransfoDico2

#import Storage

def INCLUDE(self,PSSE_path,**args):
   """
       Fonction sd_prod pour la macro INCLUDE
   """
   CaseFolder = args['output_folder']
   #Storage.MaximumDepth = args['MaxDepth']
   #print('casefolder loaded')
   if CaseFolder==None: return

   reevalue=0
   if hasattr(self,'fichier_ini'):
       reevalue=1
       if self.fichier_ini == CaseFolder : return
       if hasattr(self,'old_context_fichier_init' ):
         for concept in self.old_context_fichier_init.values():
             self.jdc.delete_concept(concept)
         self.jdc_aux=None
         self.contexte_fichier_init={}
         self.reevalue_sd_jdc()
         self.jdc.reset_context()

   self.fichier_ini=CaseFolder
   self.contexte_fichier_init = {}
   self.fichier_unite = 999
   self.fichier_err = None
   self.fichier_text=""

   unite = 999

   CaseFile = ''
   FolderList = os.listdir(CaseFolder)
   for folder in FolderList:
      if folder[0:7] == 'package':
         # Get BaseCase.sav inside the first package folder we find
         FolderContents = os.listdir(os.path.join(CaseFolder, folder))
         for file in FolderContents:
            if file == 'BaseCase.sav':
               CaseFile = os.path.join(os.path.join(CaseFolder, folder), file)
               break
         break
   print "ops before try"

           
   try:
      #MachineDico,LoadDico,LineDico,TransfoDico,MotorDico,BusDico,BranchesDico,BusNominal = ExtractGeneratorLoadLineandTransfoDico(CaseFile, PSSE_path)
      # BusList = getBusNominalkV(CaseFile)
      BusList, LinesList, TransfosList = getNominalkV(CaseFile)
      #getTrueLines(CaseFile)
   except Exception, e:
      exc_type, exc_obj, exc_tb = sys.exec_info()
      print(e)
      print(exc_type, exc_tb.tb_lineno)
   
   for e in self.jdc.etapes:
       if e.nom == 'CASE_SELECTION' : 
          etape=e
          break
   self.jdc.appli.changeIntoMC(e, 'BusesList', BusList)
   self.jdc.appli.changeIntoMC(e, 'LinesList', LinesList)
   self.jdc.appli.changeIntoMC(e, 'TransformersList', TransfosList)

   self.jdc.appli.changeIntoDefMC('CONTINGENCY_SELECTION', ('Automatic_N_2_Selection', 'BusesList'), BusList)
   self.jdc.appli.changeIntoDefMC('CONTINGENCY_SELECTION', ('Automatic_N_2_Selection', 'LinesList'), LinesList)
   self.jdc.appli.changeIntoDefMC('CONTINGENCY_SELECTION', ('Automatic_N_2_Selection', 'TransformersList'), TransfosList)
   

   try:
       #updateConts()
       #self.jdc.appli.changeIntoDefMC('CONTINGENCY_SELECTION', ('MultipleContingencyList', 'ComponentList'), Storage.ContFullList)
       ContFullList=('AAAA','ZER','t__uuu','nkop','iop')
       self.jdc.appli.changeIntoDefMC('CONTINGENCY_SELECTION', ('MultipleContingencyList', 'ComponentList'), ContFullList)
   except Exception, e:
      exc_type, exc_obj, exc_tb = sys.exec_info()
      print(e)
      print(exc_type, exc_tb.tb_lineno)


   #self.jdc.ajoutMC(e,'TransfosList',listeTuple)



def INCLUDE_context(self,d):
   """
       Fonction op_init pour macro INCLUDE
   """
   for k,v in self.g_context.items():
      d[k]=v

def getXLS(fileName) :
    dico={}
    dico['onglet1']=(('bus1','bus2','bus3'),('contin1','contin2','contin3'))
    dico['onglet2']=(('bus4','bus5'),('contin4','contin5','contin6'))
    dico['onglet3']=(('bus6','bus7'),('contin8',))
    print dico
    return dico


def PROCESS_context(self,d):
    print "dans le init du Process"

def PROCESS(self,XLS_file,**args):



    print "dans PROCESS"
    if XLS_file == "" or XLS_file == None: return
    #Storage.csvFileName = XLS_file
    # c est la premier fois
    
    if not (hasattr(self,'sheets')) :
       print "dans if" 
       #from Processor_Storage import *
       #print getSheets
       #getSheets()
       #ComponentList, ContingencyList = getComponentandContingencyList(Storage.sheets[0])
       #print ComponentList
       #print ContingencyList
       #Storage.selectedDoubleRow[Storage.sheets[0]]=['PV MATIMBA']
       #Storage.selectedDoubleCol[Storage.sheets[0]]=['MAZENOD_MHDAM_LI1_']
       #self.jdc.appli.changeIntoMC(self,'TabList',Storage.sheets)
       #self.sheets=Storage.sheets
       #self.OngletsValeurs=[]
       self.sheets=getXLS(XLS_file)
       self.jdc.appli.changeIntoMC(self,'TabList',self.sheets.keys())
      
       for k in self.sheets.keys():
           nom='Component_List_For_'+k
           monInto=self.sheets[k][0]
           self.jdc.appli.ajoutDefinitionMC('CONTINGENCY_PROCESSING',nom,'TXM',min=0, max='**', into=monInto, homo= 'SansOrdreNiDoublon')
           nom='Contingency_List_For_'+k
           monInto=self.sheets[k][1]
           self.jdc.appli.ajoutDefinitionMC('CONTINGENCY_PROCESSING',nom,'TXM',min=0, max='**', into=monInto, homo= 'SansOrdreNiDoublon')

       self.MCAjoutes=[]
       self.OngletsSelectionnes=[]
       
    else :
       # On a selectionne un onglet 
       # On teste si on a modifie la liste des onglets

       nouveauxOngletsSelectionnes= self.get_child('TabList').getval()
       if  nouveauxOngletsSelectionnes==self.OngletsSelectionnes : return
       if nouveauxOngletsSelectionnes==() or nouveauxOngletsSelectionnes == [] :
          for MC in self.MCAjoutes :
              self.jdc.appli.deleteMC(self,MC)
          self.MCAjoutes=[]
          self.OngletsSelectionnes=[]
          return
          
       for Onglet in nouveauxOngletsSelectionnes:
           if Onglet in self.OngletsSelectionnes : continue

           MCFils='Contingency_List_For_'+Onglet
           self.jdc.appli.ajoutMC(self,MCFils,[])
           self.MCAjoutes.append(MCFils)
           MCFils='Component_List_For_'+Onglet
           self.jdc.appli.ajoutMC(self,MCFils,[])
           self.MCAjoutes.append(MCFils)


       for Onglet in self.OngletsSelectionnes:
           if Onglet in nouveauxOngletsSelectionnes : continue

           MCFils='Contingency_List_For_'+Onglet
           self.jdc.appli.deleteMC(self,MCFils)
           self.MCAjoutes.remove(MCFils)

           MCFils='Component_List_For_'+Onglet
           self.jdc.appli.deleteMC(self,MCFils)
           self.MCAjoutes.remove(MCFils)

       self.OngletsSelectionnes=nouveauxOngletsSelectionnes
     


      # OldBusValeurs= self.get_child('BusList').getval()
#       OldContValeurs= self.get_child('ContList').getval()
#       if OldBusValeurs ==  None : OldBusValeurs=[]
#       if OldContValeurs ==  None : OldContValeurs=[]
#
#       listeBus=[]
#       listeCont=[]
#       listeBusCoches=[]
#       listeContCoches=[]
#       for o in OngletsValeurs :
#           for b in self.dico[o][0]:
#               texte=b+" ("+ str(o) +" )"
#               listeBus.append(str(texte))
#               if texte in OldBusValeurs : listeBusCoches.append(str(texte))
#           for c in self.dico[o][1]:
#               texte=c+" ("+ str(o) +" )"
#               listeCont.append(str(texte))
#               if texte in OldContValeurs : listeContCoches.append(str(texte))
#           
#       self.jdc.appli.changeIntoMCandSet(self,'BusList',listeBus,listeBusCoches)
#       self.jdc.appli.changeIntoMCandSet(self,'ContList',listeCont,listeContCoches)
