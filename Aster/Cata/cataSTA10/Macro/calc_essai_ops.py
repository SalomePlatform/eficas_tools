#@ MODIF calc_essai_ops Macro  DATE 28/01/2010   AUTEUR BODEL C.BODEL 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2008  EDF R&D                  WWW.CODE-ASTER.ORG
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
# ======================================================================

## \package calc_essai_ops Impl�mentation de la macro CALC_ESSAI
#
# Ce module contient la partie controle de la macro CALC_ESSAI
# l'impl�metation de cette macro se trouve dans les modules
# meidee_help, meidee_mac, meidee_massamor, meidee_turbulent
# on utilise aussi une librairie de support
# pour la gestion de l'interface graphique dans meidee_iface


def calc_essai_ops( self,
                    INTERACTIF          = None,
                    #UNITE_FIMEN         = None,
                    UNITE_RESU          = None,
                    EXPANSION           = None,
                    #MEIDEE_FLUDELA      = None,
                    #MEIDEE_TURBULENT    = None,
                    IDENTIFICATION      = None,
                    MODIFSTRUCT         = None,
                    TRAITEMENTSIG       = None,
                    GROUP_NO_CAPTEURS   = None,
                    GROUP_NO_EXTERIEUR  = None,
                    #RESU_FLUDELA        = None,
                    #RESU_TURBULENT      = None,
                    RESU_IDENTIFICATION = None,
                    RESU_MODIFSTRU      = None,
                    **args):
    import aster
    from Meidee.meidee_cata import MeideeObjects
    ier = 0
    
    # La macro compte pour 1 dans la numerotation des commandes
    self.set_icmd(1)

    prev = aster.onFatalError()
    
    # gestion des concepts sortants de la macro, declares a priori
    table = []
    table_fonction = []
    mode_mec = []


    if not RESU_MODIFSTRU:
        out_modifstru = {}
    else:
        out_modifstru = RESU_MODIFSTRU[0] # max=1 dans le capy


    if not RESU_IDENTIFICATION:
        RESU_IDENTIFICATION = []
    else:
        for res in RESU_IDENTIFICATION:
            table_fonction.append(res['TABLE'])
    out_identification = {"DeclareOut" : self.DeclareOut,
                          "TypeTables" : 'TABLE_FONCTION',
                          "ComptTable" : 0,
                          "TablesOut"  : table_fonction}

## SUPRESSION (PROVISOIRE ?) DES ONGLETS IFS
##    if not RESU_FLUDELA:
##        RESU_FLUDELA = []
##    else:
##        for res in RESU_FLUDELA:
##            table.append(res['TABLE'])
##    out_fludela = {"DeclareOut" : self.DeclareOut,
##                   "TypeTables" : 'TABLE',
##                   "ComptTable" : 0,
##                   "TablesOut" : table}
##
##    if not RESU_TURBULENT:
##        RESU_TURBULENT = []
##    else:
##        for res in RESU_TURBULENT:
##            table_fonction.append(res['FONCTION'])
##    out_meideeturb = {"DeclareOut" : self.DeclareOut,
##                      "FoncOut" : table_fonction}
    
    # Mode interactif : ouverture d'une fenetre Tk
    if INTERACTIF == "OUI":
        aster.onFatalError('EXCEPTION')

        create_interactive_window(self,
                                  #UNITE_FIMEN,
                                  #out_fludela,
                                  #out_meideeturb,
                                  out_identification,
                                  out_modifstru,
                                  )
    else:
        from Meidee.meidee_calcul import MessageBox
        from Meidee.meidee_test import TestMeidee
        mess = MessageBox(UNITE_RESU)
        mess.disp_mess("Mode non int�ractif")
        
        objects = MeideeObjects(self, mess)

        # importation des concepts aster existants de la memoire jeveux
        TestMeidee(self,
                   mess,
                   #out_fludela,
                   #out_meideeturb,
                   out_identification,
                   out_modifstru,
                   objects,
                   EXPANSION,
                   #MEIDEE_FLUDELA,
                   #MEIDEE_TURBULENT,
                   IDENTIFICATION,
                   MODIFSTRUCT,
                   GROUP_NO_CAPTEURS,
                   GROUP_NO_EXTERIEUR              
                   )

        mess.close_file()
    aster.onFatalError(prev)
    return ier



def create_tab_mess_widgets(tk):
    """Construits les objects table et bo�te � messages."""
    try:
        from Pmw import PanedWidget
    except ImportError:
        PanedWidget = None
    
    from Meidee.meidee_iface import MessageBoxInteractif, TabbedWindow
    
    tabsw = tk
    msgw = tk
    tk.rowconfigure(0, weight=2)
    tk.rowconfigure(1, weight=1)

    tabs = TabbedWindow(tabsw, ["Expansion de modeles",
                                "Modification structurale",
                                #"MEIDEE mono-modal fludela",
                                #"MEIDEE mono-modal turbulent",
                                "Identification de chargement",
                                "Traitement du signal",
                                "Parametres de visualisation",
                               ])

    tabs.grid(row=0, column=0, sticky='nsew')
    # pack(side='top',expand=1,fill='both')
    
    # ecriture des message dans un fichier message
    mess = MessageBoxInteractif(msgw)
    mess.grid(row=1, column=0, sticky='nsew')
    
    return tabs, mess

## SUPRESSION (PROVISOIRE ?) DES ONGLETS IFS
##def get_fimen_files(UNITE_FIMEN, FIMEN=None):
##    """Fichiers fimen �ventuels associ�s aux unit�s logiques en entr�e"""
##    # XXX FIMEN is not defined (should it be included in the macro)
##    from Utilitai.UniteAster import UniteAster
##    fichiers_fimen = []
##    print "FIMEN:", UNITE_FIMEN
##
##    if UNITE_FIMEN:
##        if type(FIMEN)==int:
##            UNITE_FIMEN= [ UNITE_FIMEN ]
##        for unit in UNITE_FIMEN:
##            UL = UniteAster()
##            fichiers_fimen.append( (unit, UL.Nom(unit)) )
##
##    return fichiers_fimen


class FermetureCallback:
    """Op�rations � appliquer lors de la fermeture de la
    fen�tre Tk.
    """

    def __init__(self, main_tk, turbulent):
        self.main_tk = main_tk
        self.turbulent = turbulent

    def apply(self):
        """Enl�ve les fichiers temporaires de Xmgrace"""
        if self.turbulent.param_visu.logiciel_courbes is not None:
            self.turbulent.param_visu.logiciel_courbes.fermer()
        self.main_tk.quit()


def create_interactive_window(macro,
                              #UNITE_FIMEN,
                              #out_fludela,
                              #out_meideeturb,
                              out_identification,
                              out_modifstru,
                              ):
    """Construit la fen�tre interactive comprenant une table pour 
    les 4 domaines de Meidee."""
    from Tkinter import Tk
    
    from Meidee.meidee_cata import MeideeObjects
    from Meidee.meidee_correlation import InterfaceCorrelation
    from Meidee.meidee_modifstruct import InterfaceModifStruct
    from Meidee.meidee_turbulent import InterfaceTurbulent
    from Meidee.meidee_parametres import InterfaceParametres
    from Meidee.meidee_calc_spec import InterfaceCalcSpec
## SUPRESSION (PROVISOIRE ?) DES ONGLETS IFS
##    from Meidee.meidee_fludela import InterfaceFludela, InterfaceTurbMonomod
    
    # fenetre principale
    tk = Tk()
    tk.rowconfigure(0, weight=1)
    tk.columnconfigure(0,weight=1)
    tk.title("CALC_ESSAI")

    tabs, mess = create_tab_mess_widgets(tk)
    main = tabs.root()
    
    # importation des concepts aster de la memoire jeveux    
    objects = MeideeObjects(macro, mess)
    tabs.set_objects(objects)
    
    param_visu = InterfaceParametres(main, mess)
    
    iface = InterfaceCorrelation(main, objects, macro, mess,
                                 param_visu)
    imodifstruct = InterfaceModifStruct(main, objects, macro,
                                        mess, out_modifstru, param_visu)
    identification = InterfaceTurbulent(main, objects, mess, out_identification, param_visu)
    
    calc_spec= InterfaceCalcSpec(main,objects,mess,param_visu)
## SUPRESSION (PROVISOIRE ?) DES ONGLETS IFS
##    fludelamonomod = InterfaceFludela(main, objects,
##                                      get_fimen_files(UNITE_FIMEN), mess, out_fludela, param_visu)
##    turbmonomod = InterfaceTurbMonomod(main, objects,get_fimen_files(UNITE_FIMEN) ,mess, out_meideeturb, param_visu)


    tabs.set_tab("Expansion de modeles", iface.main)
    tabs.set_tab("Modification structurale", imodifstruct.main)
    tabs.set_tab("Identification de chargement", identification)
    tabs.set_tab("Traitement du signal", calc_spec)
    tabs.set_tab("Parametres de visualisation", param_visu)
## SUPRESSION (PROVISOIRE ?) DES ONGLETS IFS
##    tabs.set_tab("MEIDEE mono-modal fludela", fludelamonomod )
##    tabs.set_tab("MEIDEE mono-modal turbulent", turbmonomod )
    
    
    tabs.set_current_tab("Expansion de modeles")

    tk.protocol("WM_DELETE_WINDOW", FermetureCallback(tk, identification).apply)
    
    try:
        tk.mainloop()
    except :
        print "MEIDEE : *ERREUR*"

    