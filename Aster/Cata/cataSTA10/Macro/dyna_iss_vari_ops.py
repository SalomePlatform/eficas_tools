#@ MODIF dyna_iss_vari_ops Macro  DATE 08/12/2010   AUTEUR ZENTNER I.ZENTNER 
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

# RESPONSABLE ZENTNER I.ZENTNER
import os


def dyna_iss_vari_ops(self, NOM_CMP, PRECISION, INTERF,MATR_COHE, UNITE_RESU_FORC, 
                                 UNITE_RESU_IMPE, TYPE, MATR_GENE ,INFO, 
#                      NB_FREQ, FREQ_INIT, FREQ_PAS,  FREQ_MAX, OPTION,
                         **args):
   """
      Macro DYNA_ISS_VARI
   """
   ier=0
   import numpy as NP
   from numpy import linalg
   from math import pi, ceil, sqrt, floor, log, tanh
   import aster   
   from Accas import _F
   from Utilitai.Table import Table
   from Utilitai.Utmess import  UTMESS
   
  #--------------------------------------------------------------------------------  
   def get_group_coord(group):
      """Retourne les coordonnees des noeuds du groupe 'group'
      """
      l_ind = NP.array(coll_grno.get('%-8s' % group, [])) - 1
      return NP.take(t_coordo, l_ind, axis=0)

 #-------------------------------------------------------------------------------- 
 # On importe les definitions des commandes a utiliser dans la macro
 # 
   COMB_MATR_ASSE = self.get_cmd('COMB_MATR_ASSE')
   LIRE_IMPE_MISS = self.get_cmd('LIRE_IMPE_MISS')
   LIRE_FORC_MISS = self.get_cmd('LIRE_FORC_MISS')
   COMB_MATR_ASSE = self.get_cmd('COMB_MATR_ASSE')   
   CREA_CHAMP = self.get_cmd('CREA_CHAMP')   
   DYNA_LINE_HARM = self.get_cmd('DYNA_LINE_HARM')   
   DETRUIRE= self.get_cmd('DETRUIRE')   
   
 
   DEFI_FONCTION  = self.get_cmd('DEFI_FONCTION')
   CALC_FONCTION  = self.get_cmd('CALC_FONCTION')      
   CREA_TABLE     = self.get_cmd('CREA_TABLE')
   REST_SPEC_TEMP     = self.get_cmd('REST_SPEC_TEMP')
   DEFI_LIST_REEL=self.get_cmd('DEFI_LIST_REEL')
  
   # Comptage commandes + declaration concept sortant
   self.set_icmd(1)
   macro='DYNA_ISS_VARI'   
   # Type de r�sultat
   fonc_acce  =  args['FONC_SIGNAL'] 
   if fonc_acce !=None:
      TYPE_RESU='TRANS'
      self.DeclareOut('dyha', self.sd)
   else:
      TYPE_RESU='SPEC'   
      self.DeclareOut('tab_out', self.sd)
   
#--------------------------------------------------------------------------------
 # -------- DISCRETISATION frequentielle ou temporelle -------- 

   if TYPE_RESU=='SPEC':
         FREQ_INIT=  args['FREQ_INIT']
         NB_FREQ =  args['NB_FREQ'] 
         PAS=  args['FREQ_PAS']  
         OPTION=args['OPTION']  
     
   if TYPE_RESU=='TRANS':         
         tt, vale_s=fonc_acce.Valeurs()  
         DT=tt[1]-tt[0]            

         __foint=CALC_FONCTION(                            
#          __foncaf=CALC_FONCTION(
                             FFT=_F( FONCTION =fonc_acce , 
#                             METHODE='COMPLET',
                               METHODE='PROL_ZERO', 
                     ),  );    
                            
         vale_fre, vale_re, vale_im =__foint.Valeurs()            
         NB_FREQ2= len(vale_fre)
         PAS=1./(NB_FREQ2*DT)
         NB_FREQ= int(floor(len(vale_fre)/2)) #signal nombre impair (floor(N/2)) ou signal nombre pair avec REST_SPEC_TEMP (prend N/2 pour N pair)
#         NB_FREQ= int(floor(len(vale_fre)/2)+1)  # signal nombre pair: N/2+1
         OMF =1./(2.*DT)            
         FREQ_INIT=0.0
                  
        # liste des frequences complete 
         l_freq_sig=[]   
         for k in range(NB_FREQ):
            freqk=FREQ_INIT+PAS*k
            l_freq_sig.append(freqk)
            

         FREQ_FIN  =  args['FREQ_MAX']                
         if  FREQ_FIN  !=None :  
            assert (FREQ_FIN > (NB_FREQ-1)*PAS),  'FREQ_FIN = ' + str(FREQ_FIN)  +'  < frequence de coupure: augmenter FREQ_FIN'
            PAS  =  args['FREQ_PAS'] 
            NB_FREQ = int(ceil(FREQ_FIN/ PAS))+1
            FREQ_INIT =0.0
            
#          NB_FREQ=NB_FREQ2
         print '', NB_FREQ, PAS, FREQ_INIT,  (NB_FREQ-1)*PAS        
 #        if INFO==2:
 #            aster.affiche('MESSAGE','DISCRETISATION UTILISATEUR :  NB_FREQ, PAS, FREQ_FIN'+str(NB_FREQ)+' ,'+str(PAS)+' ,'+ str(NB_FREQ-1)*PAS))
#---------------------------------------------------------------------------------------           
# --------------------------------------------------------------------------------------
   dgene = MATR_GENE[0].cree_dict_valeurs(MATR_GENE[0].mc_liste)
   if dgene['MATR_AMOR'] != None:
     aster.affiche('MESSAGE',' MATR_AMOR existe')
     __ma_amort = MATR_GENE['MATR_AMOR']
   else:         
     __ma_amort=COMB_MATR_ASSE(CALC_AMOR_GENE=_F(MASS_GENE = MATR_GENE['MATR_MASS'] ,
                                        RIGI_GENE = MATR_GENE['MATR_RIGI'] ,                                       
                                        AMOR_REDUIT= (  0.0,),
                                         ),                               
                                  );
     aster.affiche('MESSAGE',' MATR_AMOR pas donnee, on prend AMOR_REDUIT=0.0,')
  
   from SD.sd_maillage      import sd_maillage
   from SD.sd_nume_ddl_gd   import sd_nume_ddl_gd    
   from SD.sd_nume_ddl_gene import sd_nume_ddl_gene    
   from SD.sd_mode_meca import sd_mode_meca 
   from SD.sd_resultat import sd_resultat
   from SD.sd_cham_gene import sd_cham_gene

   v_refa_rigi = MATR_GENE['MATR_RIGI'].REFA.get()
   v_refa_mass = MATR_GENE['MATR_MASS'].REFA.get()
   # MAILLAGE
   nom_bamo = v_refa_rigi[0]
   nume_ddl = aster.getvectjev(nom_bamo[0:8] + '           .REFD        ' )[3]
   nom_mail = aster.getvectjev( nume_ddl[0:14] + '.NUME.REFN        ' )[0] 
   maillage = sd_maillage(nom_mail)
   # MODELE, DDLGENE
   nom_ddlgene = v_refa_rigi[1]  
   nom_modele = aster.getvectjev( nume_ddl[0:14] + '.NUME.LILI        ' )[1]   
   resultat = self.get_concept(nom_bamo)
   nume_ddlgene = self.get_concept(nom_ddlgene)
   modele = self.get_concept(nom_modele[0:8])

   #TEST base modale
   nom_bamo2 = v_refa_mass[0]
   if nom_bamo.strip() != nom_bamo2.strip():
      UTMESS('F','ALGORITH5_42')
   
   nbnot, nbl, nbma, nbsm, nbsmx, dime = maillage.DIME.get()

   # coordonnees des noeuds
   l_coordo = maillage.COORDO.VALE.get()
   t_coordo = NP.array(l_coordo)
   t_coordo.shape = nbnot, 3
   # groupes de noeuds
   coll_grno = maillage.GROUPENO.get()
   GROUP_NO_INTER=INTERF['GROUP_NO_INTERF']
   noe_interf = get_group_coord(GROUP_NO_INTER)
   nbno, nbval = noe_interf.shape
   
   del nume_ddl, nom_mail, nom_modele
   if INFO==2:
      aster.affiche('MESSAGE','NBNO INTERFACE : '+str(nbno))

  # MODES
   nbmodt2 = MATR_GENE['MATR_RIGI'].DESC.get()[1]
   iret,nbmodd,kbid=aster.dismoi('F','NB_MODES_DYN', nom_bamo,'RESULTAT')
   iret,nbmods,kbid=aster.dismoi('F','NB_MODES_STA', nom_bamo,'RESULTAT')
   iret,nbmodt,kbid=aster.dismoi('F','NB_MODES_TOT',nom_bamo,'RESULTAT')  
   if nbmodt2 != nbmodt:
       UTMESS('F','ALGORITH5_42')

   if INFO==2:
      texte = 'NOMBRE DE MODES: '+str(nbmodt)+'   MODES DYNAMIQUES: '+str(nbmodd)+'   MODES STATIQUES: '+str(nbmods)
      aster.affiche('MESSAGE',texte)
      aster.affiche('MESSAGE','COMPOSANTE '+NOM_CMP)


   if TYPE_RESU=="SPEC":
      SPEC = NP.zeros((NB_FREQ,nbmodt,nbmodt))+1j
   if TYPE_RESU=="TRANS":      
      VEC = NP.zeros((NB_FREQ,nbmodt))+1j 
   abscisse = [None]*NB_FREQ     
   
  # PARAMETRES fonction de coh�rence
   VITE_ONDE = MATR_COHE['VITE_ONDE']
   alpha = MATR_COHE['PARA_ALPHA']
   
#   # PARAMETRE nom_champ   
#    cham_calc=NOM_CHAM
#    print 'NOM_CHAMP   ',cham_calc 
#    if cham_calc=='DEPL':
#       ii_cham=1
#    elif   cham_calc=='VITE': 
#       ii_cham=2     
#    elif   cham_calc=='ACCE': 
#       ii_cham=3   

 #   POUR TRANS, on sort le champ en d�palcement: c'est �quivalen du champ en deplacement si on applique un signal en ACCE
   cham_calc='DEPL'     
   ii_cham=1      


#---------------------------------------------------------------------
#---------------------------------------------------------------------
  # BOUCLE SUR LES FREQUENCES
   for k in range(NB_FREQ):
      freqk=FREQ_INIT+PAS*k   
      if INFO==2:
         aster.affiche('MESSAGE','FREQUENCE DE CALCUL: '+str(freqk))      
      
# #---------------------------------------------------------           
#       # Matrice de coherence                  
      XX=noe_interf[:,0]
      YY=noe_interf[:,1]
#       
# # ----MITA & LUCO
      XN=NP.repeat(XX,nbno)
      YN=NP.repeat(YY,nbno)
      XR=NP.reshape(XN,(nbno,nbno))
      YR=NP.reshape(YN,(nbno,nbno))
      XRT=NP.transpose(XR)
      YRT=NP.transpose(YR)
      DX=XR-XRT
      DY=YR-YRT
      DIST=DX**2+DY**2
      
      COHE=NP.exp(-(DIST*(alpha*freqk/VITE_ONDE)**2.))

# #----ABRAHAMSON (EPRI)
#       p_a1=1.647
#       p_a2=1.01
#       p_a3=0.4
#       p_n1=7.02
#    #    p_n2=1.685
#       COHE=NP.zeros((nbno,nbno))
#       for no1 in range(nbno):
#          for no2 in range(nbno):
#             dist_xi=sqrt((XX[no1]-XX[no2])**2+(YY[no1]-YY[no2])**2)
#             p_n2=5.1-0.51*log(dist_xi+10.)
#             pfc=-1.886+2.221*log(4000./(dist_xi+1.)+1.5)
#             term1=1.+(freqk*tanh(p_a3*dist_xi)/(p_a1*pfc))**p_n1
#             term2=1.+(freqk*tanh(p_a3*dist_xi)/(p_a2*pfc))**p_n2
#             COHE[no1,no2]=1./sqrt(term1* term2)
#             
  #---------------------------------------------------------          
      # On desactive temporairement les FPE qui pourraient etre generees (a tord!) par blas
      aster.matfpe(-1)
      eig, vec =linalg.eig(COHE)
      vec = NP.transpose(vec)   # les vecteurs sont en colonne dans numpy
      aster.matfpe(1)
      eig=eig.real
      vec=vec.real
      # on rearrange selon un ordre decroissant
      eig = NP.where(eig < 1.E-10, 0.0, eig)
      order = (NP.argsort(eig)[::-1])
      eig = NP.take(eig, order)
      vec = NP.take(vec, order, 0)
      
      #-----------------------
      # Nombre de modes POD a retenir
      
      etot=NP.sum(eig**2)
      ener=0.0
      nbme=0
      while nbme < nbno:
         ener= eig[nbme]**2+ener
         prec=ener/etot
         nbme=nbme+1
         if INFO==2:
            aster.affiche('MESSAGE','VALEUR PROPRE  '+str(nbme)+' : '+str(eig[nbme-1]))
         if prec > PRECISION :
            break

      if INFO==2:      
         aster.affiche('MESSAGE','NOMBRE DE MODES POD RETENUS : '+str(nbme))
         aster.affiche('MESSAGE','PRECISION (ENERGIE RETENUE) : '+str(prec))      

      PVEC=NP.zeros((nbme,nbno))
      for k1 in range(0,nbme):
         PVEC[k1, 0:nbno]=NP.sqrt(eig[k1])*vec[k1] 
      # CALCUL DE FS variable-------------------------------
      XO=NP.zeros((nbme,nbmods))
      if NOM_CMP=='DX':
         COMP = 1
      elif NOM_CMP=='DY':
         COMP = 2
      elif NOM_CMP=='DZ': 
         COMP = 3  
   #---------MODES interface
      # ----- boucle sur les modes statiques
      for mods in range(0,nbmods):
         nmo = nbmodd+mods+1
         __CHAM=CREA_CHAMP( TYPE_CHAM='NOEU_DEPL_R',
                OPERATION='EXTR',                  
                NUME_ORDRE=nmo,
                RESULTAT = resultat  ,
                NOM_CHAM = 'DEPL'
                      );
         MCMP =__CHAM.EXTR_COMP(NOM_CMP,[GROUP_NO_INTER]).valeurs

         NNO =__CHAM.EXTR_COMP(NOM_CMP,[GROUP_NO_INTER], topo=1).noeud


         som=NP.sum(MCMP)
         max1=NP.max(MCMP)
         min1=NP.min(MCMP)
         maxm=NP.max([abs(max1),abs(min1)])

      #-------------CALCUL DE XO -------------
#  on recupere la composante COMP (dx,dy,dz) des modes et on projete
         #  CAS 1: MODES DE CORPS RIGIDE
         if INTERF['MODE_INTERF'] =='CORP_RIGI':
            for modp in range(0,nbme):
               #modes de translation
               if mods+1 <=3:
                  if abs(som)<10.E-6:
                     XO[modp,mods]=0.0
                  else :
                     fact=1./som               
                     XO[modp,mods]=fact*abs(NP.inner(MCMP,PVEC[modp]))
               #modes de rotation
               else:
                  if maxm<10.E-6:
                     if som<10.E-6:
                        XO[modp,mods]=0.0 
                     else :
                        UTMESS('F','ALGORITH6_86')
                  else :  
                     fact = 1./(nbno)                   
                     XO[modp,mods]=1./(maxm**2.)*fact*NP.inner(MCMP,PVEC[modp])

         # CAS 2: MODES EF
         if INTERF['MODE_INTERF'] =='TOUT':
            for modp in range(0,nbme):
               if abs(som)<10.E-6:
                  if maxm<10.E-6:
                     XO[modp,mods]=0.0 
                  else:
                     UTMESS('F','UTILITAI5_89')                     
               else:
                  fact=1./som                  
                  XO[modp,mods]=fact*abs(NP.inner(MCMP,PVEC[modp]))

         DETRUIRE(CONCEPT=_F(NOM=(__CHAM)),INFO=1)

   #----Impedances + force sismique.----------------------------------------------------------------- 
      if k>0:
         DETRUIRE(CONCEPT=_F(NOM=(__impe,__fosi,__rito)),INFO=1) 

      __impe = LIRE_IMPE_MISS(BASE=resultat,  
                           TYPE=TYPE,
                           NUME_DDL_GENE=nume_ddlgene,               
                           UNITE_RESU_IMPE= UNITE_RESU_IMPE, 
                           FREQ_EXTR=freqk, 
                           );
      __rito=COMB_MATR_ASSE(COMB_C=(
                                _F(MATR_ASSE=__impe,
                                 COEF_C=1.0+0.j,),
                                _F(MATR_ASSE=MATR_GENE['MATR_RIGI'],
                                 COEF_C=1.0+0.j,),
                                 ),
                                 SANS_CMP='LAGR',
                                 );        

      #    on cree __fosi  pour  RECU_VECT_GENE_C   plus loin                                                                                                             

      __fosi = LIRE_FORC_MISS(BASE=resultat,  
                           NUME_DDL_GENE=nume_ddlgene,
                           NOM_CMP=NOM_CMP,
                            NOM_CHAM='DEPL',                                       
                           UNITE_RESU_FORC = UNITE_RESU_FORC, 
                           FREQ_EXTR=freqk,); 


      # impedance
      MIMPE=__impe.EXTR_MATR_GENE() 
      #  extraction de la partie modes interface 
      KRS = MIMPE[nbmodd:nbmodt,nbmodd:nbmodt]
      
 
      if TYPE_RESU=="TRANS":        
           #   force sismique resultante: somme des mode POD 
         XO_s=NP.sum(XO,0)          
         FS = NP.dot(KRS,XO_s) 
         Fzero=NP.zeros((1,nbmodd)) 
         FS2=NP.concatenate((Fzero,NP.reshape(FS,(1,nbmods))),1)
       
        #  Calcul harmonique
         __fosi.RECU_VECT_GENE_C(FS2[0])       
         __dyge = DYNA_LINE_HARM(
                          MODELE=modele,
                          MATR_MASS = MATR_GENE['MATR_MASS'],
                          MATR_RIGI = __rito, 
                          FREQ = freqk,
                          MATR_AMOR = __ma_amort,                          
                          EXCIT =_F ( VECT_ASSE = __fosi,
                                      COEF_MULT= 1.0,
                                  ),
                        );                                        
         #  recuperer le vecteur modal depl calcule par dyge                                                      
         desc = __dyge.DESC.get()
         assert desc[ii_cham-1].strip() ==cham_calc , 'Champ'+cham_calc+ 'non trouv�'
            
         nomcham = __dyge.TACH.get()[ii_cham][0].strip()
         cham = sd_cham_gene(nomcham)
         RS = NP.array(cham.VALE.get())                
         DETRUIRE(CONCEPT=_F(NOM=(__dyge)),INFO=1) 
         
         
      if  TYPE_RESU=="SPEC":               
         SP=NP.zeros((nbmodt,nbmodt))
         for k1 in range(0,nbme):
         #  calcul de la force sismique mode POD par mode POD
            FS = NP.dot(KRS,XO[k1]) 
            Fzero=NP.zeros((1,nbmodd)) 
            FS2=NP.concatenate((Fzero,NP.reshape(FS,(1,nbmods))),1)       
        #  Calcul harmonique
            __fosi.RECU_VECT_GENE_C(FS2[0])       
            __dyge = DYNA_LINE_HARM(
                          MODELE=modele,
                          MATR_MASS = MATR_GENE['MATR_MASS'],
                          MATR_RIGI = __rito, 
                          FREQ = freqk,
                          MATR_AMOR = __ma_amort,                          
                          EXCIT =_F ( VECT_ASSE = __fosi,
                                      COEF_MULT= 1.0,
                                  ),
                        );                                        
         #  recuperer le vecteur modal depl calcule par dyge                                                      
            desc = __dyge.DESC.get()
            assert desc[ii_cham-1].strip() ==cham_calc , 'Champ'+cham_calc+ 'non trouv�'
            
            nomcham = __dyge.TACH.get()[ii_cham][0].strip()
            cham = sd_cham_gene(nomcham)
            RS = NP.array(cham.VALE.get())                
            DETRUIRE(CONCEPT=_F(NOM=(__dyge)),INFO=1) 
             # stockage des matrices r�sultats: sum(s_q s_q* ) 
            SP=SP+RS*NP.conj(RS[:,NP.newaxis])   

          
            
#--------------------------------------------
# stockage de r�sultats pour toutes les fr�quences calcul�es

      if  TYPE_RESU=="SPEC":      #SPEC = (NB_FREQ,nbmodt,nbmodt)
         SPEC[k]=SP
      if TYPE_RESU=="TRANS":      #VEC (NB_FREQ,nbmodt) 
         VEC[k]=RS
 
      abscisse[k]= freqk

#   DETRUIRE(CONCEPT=_F(NOM=(__impe,__fosi,__rito)),INFO=1) 

##-------------------------------------------------------------------------------------------------------------------------       
##--------------------------------------------------------------------------------------------------------------------------
#  Creation des sorties : table_fonction pour SPEC ou dyna_trans pour TRANS
#-------------------------------------------------------------------------------------------------------------------------- 
#-
   aster.affiche('MESSAGE','TYPE_RESU : '+TYPE_RESU) 
##---------------------------------------------------------------------
#  Si SPEC: Ecriture des tables
#--------------------------------------------------------------------- 
   if TYPE_RESU=='SPEC':
       
#   ------ CREATION DE L OBJET TABLE 
      tab = Table()
      tab.append({'NOM_CHAM' : 'DSP', 'OPTION' : 'TOUT',  'DIMENSION' : nbmodt})
      for k2 in range(nbmodt):
         if OPTION =='DIAG' : # on ecrit uniquement les termes diagonaux (autospectres) de la matrice
            foncc=[]
            for k in range(NB_FREQ) :
                 foncc.append(abscisse[k])
                 foncc.append(SPEC[k][k2,k2].real)
                 foncc.append(SPEC[k][k2,k2].imag)      
            _f = DEFI_FONCTION(NOM_PARA='FREQ',
                      NOM_RESU='SPEC',
                      VALE_C  = foncc )      
         # Ajout d'une ligne dans la Table
            tab.append({'NUME_ORDRE_I' : k2+1, 'NUME_ORDRE_J' : k2+1, 'FONCTION_C' : _f.nom})

         else: # on ecrit tout
            for k1 in range(k2+1):
               foncc=[]
               for k in range(NB_FREQ) :
                  foncc.append(abscisse[k])
                  foncc.append(SPEC[k][k1,k2].real)
                  foncc.append(SPEC[k][k1,k2].imag)      
               _f = DEFI_FONCTION(NOM_PARA='FREQ',
                      NOM_RESU='SPEC',
                      VALE_C  = foncc )
            # Ajout d'une ligne dans la Table
               tab.append({'NUME_ORDRE_I' : k1+1, 'NUME_ORDRE_J' : k2+1, 'FONCTION_C' : _f.nom})

   # Creation du concept en sortie
      dict_keywords = tab.dict_CREA_TABLE()
      tab_out = CREA_TABLE(TYPE_TABLE='TABLE_FONCTION',
                        **dict_keywords)                       

#-
##---------------------------------------------------------------------
#  Si TRANS: Ecriture de  tran_gene
#--------------------------------------------------------------------- 
# 1) on cree un concept harm_gene (factice) et le remplit a l'aide de putvectjev avec les bonnes valeurs, 
# 2) On interpole les valeurs non calcul�s (l_freq_sig)
# 3) puis on fait la FFT pour obtenir le signal temporel
         
   elif TYPE_RESU=='TRANS':  
               
      __lfre = DEFI_LIST_REEL(  VALE = list(l_freq_sig), ) ;
#      print ' creation SD DYNA_LINE_HARM'
        # on cree la SD resultat - factice (le champ ACCE sera remplace dans la suit par celui calcule)
      __dyge0 = DYNA_LINE_HARM(
                          MODELE=modele,
                          MATR_MASS = MATR_GENE['MATR_MASS'],
                          MATR_RIGI = __rito,                
                          LIST_FREQ= __lfre,              #tuple(l_freq_sig),
                          MATR_AMOR = __ma_amort,                          
                          EXCIT =_F ( VECT_ASSE = __fosi,
                                      COEF_MULT_C=1.,
                                  ),
                        );               

#   ATTENTION:  on sort le champ en d�palcement: c'est �quivalent au champ en acceleration car on a applique un signal en ACCE pour fosi en acce    
      #   #         cela evite de diviser pr w2 pour int�grer l'acceleration (erreurs numeriques au point 0)
      #   #         on remplace donc le champ en acceleration      
      cham_calc='ACCE'     
      ii_cham=3      

#       print ' putvectjev'                          
#      si tous les point on �t� calcul�s: pas d'interpolation
      if  FREQ_FIN ==None :  
         for  k,freqk in enumerate(l_freq_sig):       
            coef_a=(vale_re[k]+vale_im[k]*1.j)                   
            VEC_comp=VEC[k]*coef_a            
            nomcham = __dyge0.TACH.get()[ii_cham][k].strip()
            tup_re=tuple(VEC_comp.real)
            tup_im=tuple(VEC_comp.imag)
            aster.putvectjev( nomcham + '.VALE        ', nbmodt,tuple(range(1,nbmodt+1)),tup_re,tup_im,1 ) 

      else:

         for  k,freqk in enumerate(l_freq_sig):
            coef_a=(vale_re[k]+vale_im[k]*1.j)                              
  #  ------------ interpolation du vecteur POD  VEC (NB_FREQ, nbmodt)       
            vale_i=NP.searchsorted(abscisse, freqk)
#         print  freqk, vale_i,  abscisse[vale_i-1], abscisse[vale_i]
            if vale_i ==0:
               VEC_comp=VEC[0]*coef_a
               VEC_real=VEC_comp.real
               VEC_imag=VEC_comp.imag
            else:
               dfp=(freqk-abscisse[vale_i-1])/(abscisse[vale_i]-abscisse[vale_i-1])
               VEC_comp=(VEC[vale_i-1]+dfp*(VEC[vale_i]-VEC[vale_i-1]))*coef_a
               VEC_real=VEC_comp.real
               VEC_imag=VEC_comp.imag                               
            nomcham = __dyge0.TACH.get()[ii_cham][k].strip()
            tup_re=tuple(VEC_real)
            tup_im=tuple(VEC_imag)
            aster.putvectjev( nomcham + '.VALE        ', nbmodt,tuple(range(1,nbmodt+1)),tup_re,tup_im,1 ) 
      

      print 'REST_SPEC_TEMP'         
      
      dyha= REST_SPEC_TEMP( RESU_GENE = __dyge0 , 
#                        METHODE = 'PROL_ZERO' ,
                          SYMETRIE = 'NON' ,        # signal non symm�trique: a completer
#                        SYMETRIE = 'OUI' ,           # pas de prolongation                    
                          NOM_CHAM = 'ACCE' );
     
      
                    
   return ier