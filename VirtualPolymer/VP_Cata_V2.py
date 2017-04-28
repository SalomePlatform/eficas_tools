# coding: utf-8
import types
from Accas import *

import lienDB
import listesDB

monDico= { 'Equation_Liste' : ('initiation', 'propagation', 'termination', 'stabilization'),
           'Modele_TechnicalUse' : ('cable', 'coating', 'pipes'),
         }

monModele=listesDB.sModele().monModele

JdC = JDC_CATA(code='VP',
               execmodul=None,
                )

  
#---------------------------------
Equation = PROC (nom="Equation",
      op=None,
#---------------------------------
      Equation_DB=SIMP(statut= 'o',typ= 'TXM', into=("Approved data base", "My data base") ),
      Equation_Type = SIMP(statut= 'o',typ= 'TXM', into=("Show equation database", "Equation creation"),),
      
#     ---------------------------------------------------------------------------
       b_type_show = BLOC(condition = " Equation_Type == 'Show equation database'",
#      ---------------------------------------------------------------------------
        Equation_Liste=SIMP(statut= 'o',typ= 'TXM', into=('reaction_type','aging_type')),

         b_reaction_type =  BLOC(condition = " Equation_Liste  == 'reaction_type'",
           Equation_reaction=SIMP(statut= 'o',typ= 'TXM', into=monDico['Equation_Liste'],siValide=lienDB.recupereDicoEquation),
         ), # Fin b_reaction_type

         b_aging_type =  BLOC(condition = " Equation_Liste  == 'aging_type'",
              Equation_reaction=SIMP(statut= 'o',typ= 'TXM', into=('All', 'thermo', 'radio'),siValide=lienDB.recupereDicoEquation),
         ), # Fin b_reaction_type

         ListeEquation = SIMP(statut='o', typ='TXM',  homo='SansOrdreNiDoublon',siValide=lienDB.afficheValeurEquation),
         b_modification = BLOC(condition = " ListeEquation != None ",
           modification = SIMP(typ = bool, statut = 'o',defaut = False, fr='toto', ang='toto en anglais', siValide=lienDB.instancieChemicalFormulation),
           
           b_modif = BLOC(condition = "modification == True",
            Reaction_Type=SIMP(statut= 'o',typ= 'TXM', min=1,into=monDico['Equation_Liste'],),
            Aging_Type=SIMP(statut= 'o',typ= 'TXM', min=1,max='**', homo='SansOrdreNiDoublon', into=('All', 'thermo', 'radio'),),
            ChemicalFormulation = SIMP(statut='o', typ='TXM', defaut = 'POOH -> 2P'),

            OptionnelConstituant =  FACT ( statut = 'f',max = '**',
                Constituant = SIMP (statut = 'o', typ = 'TXM'),
                Differential_Equation =  SIMP(statut= 'o',typ= 'TXM'),
               ), # fin Const_Equa
            OptionnelleConstante  = FACT (statut = 'f', max = '**',
                  ConstanteName= SIMP (statut = 'o', typ = 'TXM',),
                  ConstanteType =  SIMP(statut= 'o',typ= 'TXM', min=1,into=('Arrhenius type','non Arrhenius type'),defaut='Arrhenius type'),
                  ),# fin ConstanteOptionnelle
            Commentaire =  SIMP (statut = 'f', typ = 'TXM', defaut = ' '),

           ),# fin b_modif
         
         ), # fin b_modification
       ), # Fin b_type_show


#     ---------------------------------------------------------------------------
      b_type_creation = BLOC(condition = " Equation_Type == 'Equation creation'",
#         ---------------------------------------------------------------------------
         Equation_Modification = FACT ( statut = 'o',
 
            ChemicalFormulation = SIMP(statut='o', typ='TXM', defaut = 'POOH -> 2P'),

            Reaction_Type=SIMP(statut= 'o',typ= 'TXM', min=1,into=monDico['Equation_Liste'],),
            Aging_Type=SIMP(statut= 'o',typ= 'TXM', min=1,max='**', homo='SansOrdreNiDoublon', into=('All', 'thermo', 'radio'),),

            Constituants = FACT ( statut = 'o',
               ConstituantPOOH = SIMP (statut = 'f', typ = 'TXM', into = ('POOH',)),
               b_pooh =  BLOC(condition = " ConstituantPOOH == 'POOH'" ,
                  Differential_Equation_POOH =  SIMP(statut= 'o',typ= 'TXM', defaut = '-ku1*POOH'),
               ), # Fin b_pooh
               #ConstituantP = SIMP (statut = 'f', typ = 'TXM', into = ('P',)),
               #b_p =  BLOC(condition = " ConstituantP == 'P'" ,
               #  Differential_Equation_P =  SIMP(statut= 'o',typ= 'TXM', defaut = '2*ku1*POOH'),
               #), # Fin b_p
               ConstituantP = FACT ( statut = 'f',
                  ConstituantP = SIMP (statut = 'f', typ = 'TXM', into = ('P',)),
                  Differential_Equation_P =  SIMP(statut= 'o',typ= 'TXM', defaut = '2*ku1*POOH'),
               ), # Fin ConstituantP

            OptionnelConstituant =  FACT ( statut = 'f',max = '**',
                Constituant = SIMP (statut = 'o', typ = 'TXM'),
                Differential_Equation =  SIMP(statut= 'o',typ= 'TXM'),
               ), # fin Const_Equa
            ),# Fin Constituants

            Constante = FACT ( statut = 'o',
               Constanteku1 = SIMP (statut = 'f', typ = 'TXM', into = ('ku1',), defaut= 'ku1'),
               b_cku1 =  BLOC(condition = "Constanteku1 == 'ku1'" ,
                  ConstanteType =  SIMP(statut= 'o',typ= 'TXM', into=('Arrhenius type','non Arrhenius type'),defaut='Arrhenius type'),
                  ),
               OptionnelleConstante  = FACT (statut = 'f', max = '**',
                  ConstanteName= SIMP (statut = 'o', typ = 'TXM',),
                  ConstanteType =  SIMP(statut= 'o',typ= 'TXM', min=1,into=('Arrhenius type','non Arrhenius type'),defaut='Arrhenius type'),
                  ),# fin ConstanteOptionnelle
            ), # fin constante
            Commentaire =  SIMP (statut = 'f', typ = 'TXM', defaut = ' '),
                  
         ), # Fin Equation_Modification
        ),  # fin b_type_creation
                 
      
) # Fin Equation

#---------------------------------
Modele = PROC (nom="Modele",
      op=None,
      Modele_DB=SIMP(statut= 'o',typ= 'TXM', into=("Approved data base", "My data base"),siValide=lienDB.recupereDicoModele ),
      Modele_Type = SIMP(statut= 'o',typ= 'TXM', into=("Show modele database", "Modele creation"),siValide=lienDB.creeListeEquation),
#     ---------------------------------------------------------------------------
      b_type_creation = BLOC(condition = " Modele_Type == 'Modele creation'",
#         ---------------------------------------------------------------------------
        technicalUse= SIMP(statut= 'o',typ= 'TXM',into=monDico['Modele_TechnicalUse'],defaut=monModele.technical_use ),
        modeleName=SIMP(statut='o',typ='TXM',defaut=monModele.nom,),
        material=SIMP(statut='o',typ='TXM',defaut=monModele.materiaux[0],),
        stabilizer = SIMP(typ = bool, statut = 'o',defaut = monModele.stabilise),
        model_developed_by_for_EDF = SIMP(typ = bool, statut = 'o',defaut = monModele.dvt_EDF[0]),
        documentation=SIMP(statut='o',typ='TXM',defaut=monModele.reference,),
        
       # ajouter la liste des equations et le remove (il faut garder ceux qu on a enlever)
      

       AjoutEquation=SIMP(statut= 'o',typ= bool, defaut=False, siValide=lienDB.recupereModeleEquation),
       b_ajout_equation = BLOC(condition = " AjoutEquation == True",
          listeEquation_initiation=SIMP(statut='o', typ='TXM',homo='SansOrdreNiDoublon', max='**', min=0, defaut=[] ),
          listeEquation_propagation=SIMP(statut='o', typ='TXM',homo='SansOrdreNiDoublon', max='**', min=0, defaut=[] ),
          listeEquation_termination=SIMP(statut='o', typ='TXM',homo='SansOrdreNiDoublon', max='**', min=0, defaut=[] ),
          listeEquation_stabilization=SIMP(statut='o',typ='TXM', homo='SansOrdreNiDoublon', max='**', min=0, defaut=[] ),
       ),# fin b_ajout_equation
       
        # coefficients monModele.coef = liste de dictionnaire mais il faut prendre que le 0
        # on enleve ceux qui commence par D, S et B(casse imprtante)
        # la clef est le coef, puis les valeurs

        Aging_Type=SIMP(statut= 'o',typ='TXM', min=1,max='**', homo='SansOrdreNiDoublon', into=('All', 'thermo', 'radio'), defaut=monModele.type_vieil),
        Diffusion = SIMP(typ = bool, statut = 'o',defaut = monModele.diffusion,siValide = lienDB.prepareDiffusion),

        b_diffusion = BLOC(condition = " Diffusion == True",
         #coefficients monModele.coef = liste de dictionnaire mais il faut prendre que le 0
        # on met ceux qui commence par D, S et pas les B ni les aitres( casse imprtante)
           listeProduitPourLaDiffusion=SIMP(statut='o', typ='TXM', max='**', min=1,homo='SansOrdreNiDoublon', into = monModele.param_ini.keys(),siValide=lienDB.ajouteDiffusion), 
       ),  # fin b_diffusion
 
       ),  # fin b_type_creation


       #AjoutEquation=Fact(statut='f',
       #     Reaction_Type=SIMP(statut= 'o',typ= 'TXM', min=1,into=monDico['Equation_Liste'],siValide=lienDB.recupereModeleEquation),
       #), # fin AjoutEquation

      Commentaire =  SIMP (statut = 'f', typ = 'TXM'),
) # Fin Modele
