#@ MODIF macr_aspic_mail_ops Macro  DATE 19/01/2004   AUTEUR DURAND C.DURAND 
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2004  EDF R&D                  WWW.CODE-ASTER.ORG
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

# Ecriture du fichier GIBI principal (dgib) - ASPID0
def write_file_dgib_ASPID0(nomFichierDATG,UNITD, EPT1, DET1, D1, D2, EPT2, DET2, ZMAX, H,
                           ALPHA, JEU, EPC, DEC, XMAX, TYPMAI, THETA, TYPELE,
                           ITYPSO, DPENE, NIVMAG, loc_datg) :

# Ouverture du fichier d'entrée de commandes
  fdgib=open(nomFichierDATG,'w')
  POIVIR = ' ;                                         \n'
  texte='****************************************************************\n'
  texte=texte+'opti echo 0 ;                                                   \n'
  texte=texte+'epT1   = '+str(EPT1)         +POIVIR
  texte=texte+'DeT1   = '+str(DET1)         +POIVIR
  texte=texte+'d1     = '+str(D1)           +POIVIR
  texte=texte+'d2     = '+str(D2)           +POIVIR
  texte=texte+'epT2   = '+str(EPT2)         +POIVIR
  texte=texte+'DeT2   = '+str(DET2)         +POIVIR
  texte=texte+'Zmax   = '+str(ZMAX)         +POIVIR
  texte=texte+'type_s = '+str(ITYPSO)       +POIVIR
  texte=texte+'d_pene = '+str(DPENE)        +POIVIR
  texte=texte+'h      = '+str(H)            +POIVIR
  texte=texte+'angl_s = '+str(ALPHA)        +POIVIR
  texte=texte+'jeu    = '+str(JEU)          +POIVIR
  texte=texte+'epC    = '+str(EPC)          +POIVIR
  texte=texte+'DeC    = '+str(DEC)          +POIVIR
  texte=texte+'Xmax   = '+str(XMAX)         +POIVIR
  texte=texte+'typmai =  MOT '+TYPMAI       +POIVIR
  texte=texte+'theta  = '+str(THETA)        +POIVIR
  texte=texte+'typele =  MOT '+TYPELE       +POIVIR
  texte=texte+'typ_eque = MOT '+'SAINE'     +POIVIR
  texte=texte+'nivmag = '+str(NIVMAG)       +POIVIR
  texte=texte+'*                                                               \n'
  texte=texte+'opti donn '
  texte=texte+"'"+loc_datg+'aspic.datg'+"';\n"
  print texte
  fdgib.write(texte)
  fdgib.close()

# Ecriture du fichier GIBI principal (dgib) - ASPID1
def write_file_dgib_ASPID1(nomFichierDATG,UNITD, EPT1, DET1, D1, D2, EPT2, DET2, ZMAX, H,
                           ALPHA, JEU, EPC, DEC, XMAX, TYPMAI,THETA,
                           A,C,EPS, RC0, NS,NC,NT,POSI, NDT,FETIRF,FETIRP,
                           TFISS,ZETA,ITYPSO,DPENE, NIVMAG, loc_datg) :

# Ouverture du fichier d'entrée de commandes
  fdgib=open(nomFichierDATG,'w')
  POIVIR = ' ;                                         \n'
  texte='****************************************************************\n'
  texte=texte+'opti echo 0 ;                                                   \n'
  texte=texte+'epT1   = '+str(EPT1)         +POIVIR
  texte=texte+'DeT1   = '+str(DET1)         +POIVIR
  texte=texte+'d1     = '+str(D1)           +POIVIR
  texte=texte+'d2     = '+str(D2)           +POIVIR
  texte=texte+'epT2   = '+str(EPT2)         +POIVIR
  texte=texte+'DeT2   = '+str(DET2)         +POIVIR
  texte=texte+'Zmax   = '+str(ZMAX)         +POIVIR
  texte=texte+'type_s = '+str(ITYPSO)       +POIVIR
  texte=texte+'d_pene = '+str(DPENE)        +POIVIR
  texte=texte+'h      = '+str(H)            +POIVIR
  texte=texte+'angl_s = '+str(ALPHA)        +POIVIR
  texte=texte+'jeu    = '+str(JEU)          +POIVIR
  texte=texte+'epC    = '+str(EPC)          +POIVIR
  texte=texte+'DeC    = '+str(DEC)          +POIVIR
  texte=texte+'Xmax   = '+str(XMAX)         +POIVIR
  texte=texte+'typmai =  MOT '+TYPMAI       +POIVIR
  texte=texte+'theta  = '+str(THETA)        +POIVIR
  texte=texte+'a      = '+str(A)            +POIVIR
  texte=texte+'c      = '+str(C)            +POIVIR
  texte=texte+'zeta   = '+str(ZETA)         +POIVIR
  texte=texte+'eps    = '+str(EPS)          +POIVIR
  texte=texte+'rc0    = '+str(RC0)          +POIVIR
  texte=texte+'ns     = '+str(NS)           +POIVIR
  texte=texte+'nc     = '+str(NC)           +POIVIR
  texte=texte+'nt     = '+str(NT)           +POIVIR
  texte=texte+'dir_fiss = MOT '+POSI        +POIVIR
  texte=texte+'pos_fiss = MOT '+TFISS       +POIVIR
  texte=texte+'ndt    = '+str(NDT)          +POIVIR
  texte=texte+'f_etir_f = '+str(FETIRF)     +POIVIR
  texte=texte+'f_etir_p = '+str(FETIRP)     +POIVIR
  texte=texte+'typ_eque = MOT '+'FISS_LON'  +POIVIR
  texte=texte+'nivmag = '+str(NIVMAG)       +POIVIR
  texte=texte+'*                                                               \n'
  texte=texte+'opti donn '
  texte=texte+"'"+loc_datg+'aspic_v2.datg'+"';\n"
  print texte
  fdgib.write(texte)
  fdgib.close()

# Ecriture du fichier GIBI principal (dgib) - ASPID2
def write_file_dgib_ASPID2(nomFichierDATG,UNITD, EPT1, DET1, D1, D2, EPT2, DET2, ZMAX,
                           H, ALPHA, JEU, EPC, DEC, XMAX, TYPMAI,
                           THETA, A, C, EPS, RC0, RC1, RC2, RC3,
                           ALP,BETA, NS, NC, NT, POSI ,NDT,NSDT,TFISS,
                           ZETA,ITYPSO,DPENE, NIVMAG, loc_datg) :

# Ouverture du fichier d'entrée de commandes
  fdgib=open(nomFichierDATG,'w')
  POIVIR = ' ;                                         \n'
  texte='****************************************************************\n'
  texte=texte+'opti echo 0 ;                                                   \n'
  texte=texte+'epT1   = '+str(EPT1)         +POIVIR
  texte=texte+'DeT1   = '+str(DET1)         +POIVIR
  texte=texte+'d1     = '+str(D1)           +POIVIR
  texte=texte+'d2     = '+str(D2)           +POIVIR
  texte=texte+'epT2   = '+str(EPT2)         +POIVIR
  texte=texte+'DeT2   = '+str(DET2)         +POIVIR
  texte=texte+'Zmax   = '+str(ZMAX)         +POIVIR
  texte=texte+'type_s = '+str(ITYPSO)       +POIVIR
  texte=texte+'d_pene = '+str(DPENE)        +POIVIR
  texte=texte+'h      = '+str(H)            +POIVIR
  texte=texte+'angl_s = '+str(ALPHA)        +POIVIR
  texte=texte+'jeu    = '+str(JEU)          +POIVIR
  texte=texte+'epC    = '+str(EPC)          +POIVIR
  texte=texte+'DeC    = '+str(DEC)          +POIVIR
  texte=texte+'Xmax   = '+str(XMAX)         +POIVIR
  texte=texte+'typmai =  MOT '+TYPMAI       +POIVIR
  texte=texte+'theta  = '+str(THETA)        +POIVIR
  texte=texte+'a      = '+str(A)            +POIVIR
  texte=texte+'c      = '+str(C)            +POIVIR
  texte=texte+'zeta   = '+str(ZETA)         +POIVIR
  texte=texte+'eps    = '+str(EPS)          +POIVIR
  texte=texte+'rc0    = '+str(RC0)          +POIVIR
  texte=texte+'rc1    = '+str(RC1)          +POIVIR
  texte=texte+'rc2    = '+str(RC2)          +POIVIR
  texte=texte+'rc3    = '+str(RC3)          +POIVIR
  texte=texte+'alpha  = '+str(ALP)          +POIVIR
  texte=texte+'beta   = '+str(BETA)         +POIVIR
  texte=texte+'ns     = '+str(NS)           +POIVIR
  texte=texte+'nc     = '+str(NC)           +POIVIR
  texte=texte+'nt     = '+str(NT)           +POIVIR
  texte=texte+'dir_fiss = MOT '+POSI        +POIVIR
  texte=texte+'pos_fiss = MOT '+TFISS       +POIVIR
  texte=texte+'ndt    = '+str(NDT)          +POIVIR
  texte=texte+'nsdt   = '+str(NSDT)         +POIVIR
  texte=texte+'typ_eque = MOT '+'FISS_COU'  +POIVIR
  texte=texte+'nivmag = '+str(NIVMAG)       +POIVIR
  texte=texte+'*                                                               \n'
  texte=texte+'list epc ;\n'
  texte=texte+'opti donn '
  texte=texte+"'"+loc_datg+'aspic.datg'+"';\n"
  print texte
  fdgib.write(texte)
  fdgib.close()

def macr_aspic_mail_ops(self,EXEC_MAILLAGE,TYPE_ELEM,RAFF_MAIL,TUBULURE,
                             SOUDURE,CORPS,FISS_SOUDURE,IMPRESSION,INFO,
                        **args):
  """
     Ecriture de la macro MACR_ASPIC_MAIL
  """
  from Accas import _F
  import types
  import aster 
  from math import sqrt,cos,sin,pi
  ier=0
  
# On importe les definitions des commandes a utiliser dans la macro
  EXEC_LOGICIEL =self.get_cmd('EXEC_LOGICIEL')
  PRE_GIBI      =self.get_cmd('PRE_GIBI')
  LIRE_MAILLAGE =self.get_cmd('LIRE_MAILLAGE')
  DEFI_GROUP    =self.get_cmd('DEFI_GROUP')
  MODI_MAILLAGE =self.get_cmd('MODI_MAILLAGE')
  AFFE_MODELE   =self.get_cmd('AFFE_MODELE')
  CREA_MAILLAGE =self.get_cmd('CREA_MAILLAGE')
  DEFI_FICHIER  =self.get_cmd('DEFI_FICHIER')
  IMPR_RESU     =self.get_cmd('IMPR_RESU')

# La macro compte pour 1 dans la numerotation des commandes
  self.set_icmd(1)

  TYPELE = TYPE_ELEM
  NIVMAG = EXEC_MAILLAGE['NIVE_GIBI']
#
#     --- raffinement maillage ---
#
  TYPMAI = RAFF_MAIL
  GROS   = (TYPMAI=='GROS')
  if GROS : NBAZIT = 40
  else    : NBAZIT = 48
#
#     --- caracteristiques de la tubulure ---
#
  EPT1  = TUBULURE['E_BASE'   ]
  DET1  = TUBULURE['DEXT_BASE']
  D1    = TUBULURE['L_BASE'   ]
  D2    = TUBULURE['L_CHANF'  ]
  EPT2  = TUBULURE['E_TUBU'   ]
  DET2  = TUBULURE['DEXT_TUBU']
  ZMAX  = TUBULURE['Z_MAX'    ]
  TYPSOU= TUBULURE['TYPE'     ]
  DPENE = TUBULURE['L_PENETR' ]
  if TYPSOU=='TYPE_2' and DPENE>0.0 : 
    self.cr.fatal("<F> <MACR_ASPIC_MAIL> les piquages penetrants sont autorises uniquement avec les soudures de type 1")
    ier = ier+1
    return ier
  if TYPSOU=='TYPE_2' :
     ITYPSO = 2
  else :
     ITYPSO = 1
#
#     --- caracteristiques de la soudure ---
#
  H     = SOUDURE['H_SOUD'   ]
  ALPHA = SOUDURE['ANGL_SOUD']
  JEU   = SOUDURE['JEU_SOUD' ]
#
#     --- caracteristiques du corps ---
#
  EPC   = CORPS  ['E_CORP'   ]
  DEC   = CORPS  ['DEXT_CORP']
  XMAX  = CORPS  ['X_MAX'    ]
  EPSI  = 1.E-03
  RMB   = ( DET1 - EPT1 ) / 2.0
  VAL1  = 1.5 * sqrt( RMB**3 / EPT1 )
  VAL3  = 3.0 * sqrt( RMB    * EPT1 )
  RMT   = ( DET2 - EPT2 ) / 2.0
  VAL2  = 1.5 * sqrt( RMT**3 / EPT2 )
  VAL4  = 3.0 * sqrt( RMT    * EPT2 )
  LZMAX = max ( VAL1 , VAL2, VAL3, VAL4 )
  ZMAXC = LZMAX + ( DEC/2.0 ) + D1 + D2
  LOK = ( abs(ZMAX-ZMAXC) <= EPSI * abs(ZMAXC) )
  if not LOK :
    print ' <MACR_ASPIC_MAIL> erreur donnees'
    print ' <MACR_ASPIC_MAIL> Z_MAX FOURNIE   : ', ZMAX
    print ' <MACR_ASPIC_MAIL> Z_MAX CALCULEE  : ', ZMAXC
    self.cr.fatal("<F> <MACR_ASPIC_MAIL> erreur donnees ")
    ier = ier+1
    return ier
  RMC   = ( DEC - EPC ) / 2.0
  VAL1  = 1.5 * sqrt( RMC**3 / EPC )
  VAL2  = 3.0 * sqrt( RMC    * EPC )
  LXMAX = max( VAL1 , VAL2 )
  XMAXC = LXMAX + ( DET1 / 2.0 )
  LOK = ( abs(XMAX-XMAXC) <= EPSI * abs(XMAXC) )
  if not LOK :
    print ' <MACR_ASPIC_MAIL> erreur donnees'
    print ' <MACR_ASPIC_MAIL> Z_MAX FOURNIE   : ', ZMAX
    print ' <MACR_ASPIC_MAIL> Z_MAX CALCULEE  : ', ZMAXC
    self.cr.fatal("<F> <MACR_ASPIC_MAIL> erreur donnees ")
    ier = ier+1
    return ier
  print ' MACR_ASPIC_MAIL / X_MAX CALCULEE : ',XMAX
  print ' MACR_ASPIC_MAIL / Z_MAX CALCULEE : ',XMAXC
#
#     --- caracteristiques de la fissure ---
#
  SAIN   = 0
  FISLON = 0
  FISCOU = 0
  THETA  = 0.0
  TFISS  = None
  if FISS_SOUDURE==None :
     SAIN = 1
  else :
     if   FISS_SOUDURE['TYPE']=='LONGUE' : FISLON = 1
     elif FISS_SOUDURE['TYPE']=='COURTE' : FISCOU = 1
     THETA = FISS_SOUDURE['AZIMUT'        ]
     EPS   = FISS_SOUDURE['ANGL_OUVERTURE']
     AXIS  = FISS_SOUDURE['AXIS'          ]
     POSI  = FISS_SOUDURE['POSITION'      ]
     TFISS = FISS_SOUDURE['FISSURE'       ]
     A     = FISS_SOUDURE['PROFONDEUR'    ]
     if      FISS_SOUDURE['LONGUEUR'      ]!=None :
        C  = FISS_SOUDURE['LONGUEUR'      ]
        N1 = 1
     else : N1 = 0
     if (TFISS=='DEB_INT') and (POSI=='INCLINE') and (DPENE>0.0) and (JEU>0.0) : 
       print ' <MACR_ASPIC_MAIL> erreur donnees'
       print ' <MACR_ASPIC_MAIL> dans le cas de fissures'
       print ' <MACR_ASPIC_MAIL> inclinees debouchant en peau interne avec'
       print ' <MACR_ASPIC_MAIL> piquage penetrant le jeu doit etre nul'
       self.cr.fatal("<F> <MACR_ASPIC_MAIL> erreur donnees ")
       ier = ier+1
       return ier
     ZETA = 0.5
     if TFISS not in ('DEB_INT','DEB_EXT') :
        if FISS_SOUDURE['LIGA_INT']==None : 
           print ' <MACR_ASPIC_MAIL> erreur donnees'
           print ' <MACR_ASPIC_MAIL> dans le cas de fissures internes'
           print ' <MACR_ASPIC_MAIL> (NON_DEB) le ligament inferieur est obligatoire'
           self.cr.fatal("<F> <MACR_ASPIC_MAIL> erreur donnees ")
           ier = ier+1
           return ier
        LIGA  = FISS_SOUDURE['LIGA_INT']
        if POSI=='DROIT' :
           if ITYPSO==1 : ZETA = (A+LIGA)/(EPC+H)
           else         : ZETA = (A+LIGA)/(EPT1+H)
        else :
           if ITYPSO==1 : ZETA = (A+LIGA)*cos(ALPHA*pi/180.0)/EPC
           else         : ZETA = (A+LIGA)*cos(ALPHA*pi/180.0)/EPT1
        if ZETA < 0.1   :
           self.cr.fatal("<F> <MACR_ASPIC_MAIL> dans le cas de fissures internes (NON_DEB) le ligament est trop petit ")
           ier = ier+1
           return ier
        if ZETA > 0.9   :
           self.cr.fatal("<F> <MACR_ASPIC_MAIL> dans le cas de fissures internes (NON_DEB) le ligament est trop grand ")
           ier = ier+1
           return ier
        if LIGA < 0.1*EPC :
           self.cr.fatal("<F> <MACR_ASPIC_MAIL> dans le cas de fissures internes (NON_DEB) le ligament est trop petit ")
           ier = ier+1
           return ier
        if (LIGA + 2.0*A) > 0.9*EPC :
           self.cr.fatal("<F> <MACR_ASPIC_MAIL> dans le cas de fissures internes (NON_DEB) le ligament est trop grand ")
           ier = ier+1
           return ier
     if N1==0 :
        if FISCOU      :
           self.cr.fatal("<F> <MACR_ASPIC_MAIL> dans le cas de fissures courte il faut preciser la longueur ")
           ier = ier+1
           return ier
        if AXIS=='NON' :
           self.cr.fatal("<F> <MACR_ASPIC_MAIL> dans le cas de la fissure longue il faut preciser la longueur ou axis=oui ")
           ier = ier+1
           return ier
        C = 0.0
     else :
        if AXIS=='OUI' : print '<A> <MACR_ASPIC_MAIL> fissure axisymetrique : le mot clef <LONGUEUR> ne doit pas etre renseigne'
     C = 0.5 * C
     LEQU=2.*(pi*(DEC-EPC)-DET1+2.*EPT1)
#
# LPIQ est une valeur qui depend theoriquement de la fissure. la valeur
# ci-dessous est approchee car elle ne sert qu'a calculer les facteurs d'etirement
#
     LPIQ=pi*(DET1)
     if AXIS=='OUI' : C=100.0*LPIQ
     RAPL=LEQU/LPIQ
     if FISCOU :
        RAP=A/C
        CAS1=RAP<0.3499
        CAS3=RAP>0.4999
        CAS2= not (CAS1 or CAS3)
        if CAS1 : ALP=0.8
        if CAS2 : ALP=0.4
        if CAS3 : ALP=0.0
        BETA=1.0
        if GROS and not CAS1 :
          NDT=1
          NSDT=2
        else :
          NDT=2
          NSDT=4
#
     if FISLON :
       if GROS :
         NDT=2
         FETIRF=30.*RAPL
         FETIRP=60.*RAPL
       else :
         NDT=3
         FETIRF=15.*RAPL
         FETIRP=30.*RAPL
#
     RC0 = FISS_SOUDURE['RAYON_TORE']
     if (FISCOU and RC0==None) :
       if GROS : RC0=0.12
       else    : RC0=0.10
       if CAS1 : RC0=0.08
       RC0=RC0*A
     if (FISLON and RC0==None) : RC0=A/(NDT+1)
#
     RC1 = FISS_SOUDURE['COEF_MULT_RC1']
     if (FISCOU and RC1==None) :
       if GROS : RC1=1.2
       else    : RC1=1.0
#
     RC2 = FISS_SOUDURE['COEF_MULT_RC2']
     if (FISCOU and RC2==None) :
       if GROS : RC2=1.4
       else    : RC2=1.2
#
     RC3 = FISS_SOUDURE['COEF_MULT_RC3']
     if (FISCOU and RC3==None) :
       if GROS :
          if CAS1 : RC3=2.5
          else    : RC3=1.0  # valeur non utilisee
       else : 
          if CAS3 : RC3=2.2
          else    : RC3=2.0
#
     NT = FISS_SOUDURE['NB_TRANCHE']
     if (FISCOU and NT==None) :
       if GROS : NT = 8
       else    : NT = 16
       if CAS1 : NT = NT*2
     if (FISLON and NT==None) : NT=0
#
     NS = FISS_SOUDURE['NB_SECTEUR']
     if (FISCOU and NS==None) :
       if GROS : NS = 2
       else    : NS = 4
     if (FISLON and NS==None) :
       if GROS : NS = 2
       else    : NS = 4
#
     NC = FISS_SOUDURE['NB_COURONNE']
     if (FISCOU and NC==None) :
       if GROS : NC = 3
       else    : NC = 4
     if (FISLON and NC==None) :
       if GROS : NC = 3
       else    : NC = 4
#
  loc_gibi=aster.repout()
  logiel = EXEC_MAILLAGE['LOGICIEL'  ]
  UNITD  = EXEC_MAILLAGE['UNITE_DATG']
  UNITS  = EXEC_MAILLAGE['UNITE_MGIB']
  if   logiel=='GIBI98'  : logiel = loc_gibi+'gibi98'
  elif logiel=='GIBI2000': logiel = loc_gibi+'gibi2000'
  else                   :
       self.cr.fatal("<F> <MACR_ASPIC_MAIL> seuls gibi98 et gibi2000 sont appelableS")
       ier = ier+1
       return ier
#
#     --- ecriture sur le fichier .datg  de la procedure ---
#
# Nom du fichier de commandes pour GIBI
  nomFichierDATG = 'fort.'+str(UNITD)
# Nom du fichier de maillage GIBI
  nomFichierGIBI = 'fort.'+str(UNITS)
  loc_datg = aster.repdex()
  if SAIN   : write_file_dgib_ASPID0(nomFichierDATG,UNITD, EPT1, DET1, D1, D2, EPT2, DET2, ZMAX, H,
                                     ALPHA, JEU, EPC, DEC, XMAX, TYPMAI, THETA, TYPELE,
                                     ITYPSO, DPENE, NIVMAG,loc_datg)
  if FISLON : write_file_dgib_ASPID1(nomFichierDATG,UNITD, EPT1, DET1, D1, D2, EPT2, DET2, ZMAX, H,
                                     ALPHA, JEU, EPC, DEC, XMAX, TYPMAI,THETA,
                                     A,C,EPS, RC0,NS,NC,NT,POSI, NDT,FETIRF,FETIRP,
                                     TFISS,ZETA,ITYPSO,DPENE, NIVMAG,loc_datg)
  if FISCOU : write_file_dgib_ASPID2(nomFichierDATG,UNITD, EPT1, DET1, D1, D2, EPT2, DET2, ZMAX,
                                     H, ALPHA, JEU, EPC, DEC, XMAX, TYPMAI,
                                     THETA, A, C, EPS, RC0, RC1, RC2, RC3,
                                     ALP,BETA, NS, NC, NT, POSI ,NDT,NSDT,TFISS,
                                     ZETA,ITYPSO,DPENE, NIVMAG,loc_datg)
#
  EXEC_LOGICIEL( LOGICIEL = logiel ,
                 ARGUMENT = ( _F(NOM_PARA=nomFichierDATG),
                              _F(NOM_PARA=nomFichierGIBI), ), )
#
  PRE_GIBI()
#
  __MAPROV=LIRE_MAILLAGE(INFO=INFO)
#
  motscles={}
  motscles['CREA_GROUP_MA']=[]
  l_CREA_GROUP_NO=[]
  if SAIN :
     l_CREA_GROUP_NO.append('S_LAT1')
     l_CREA_GROUP_NO.append('S_LAT2')
  else :
     l_CREA_GROUP_NO.append('S_LAT1_C')
     l_CREA_GROUP_NO.append('S_LAT2_C')
     l_CREA_GROUP_NO.append('S_LAT1_T')
     l_CREA_GROUP_NO.append('S_LAT2_T')
     if (TFISS=='NON_DEB') and (FISS_SOUDURE['TYPE']=='LONGUE') :
        l_CREA_GROUP_NO.append('PFONDINF')
        l_CREA_GROUP_NO.append('PFONDSUP')
     else :
        l_CREA_GROUP_NO.append('PFONDFIS')
     if (TFISS=='NON_DEB') and (FISS_SOUDURE['TYPE']=='COURTE') :
        motscles['CREA_GROUP_MA'].append(_F(GROUP_MA = 'FONDFISS',
                                            NOM      = 'MAIL_ORI',
                                            POSITION = 'INIT'     ))
     if (TFISS[:4]=='DEB_') and (AXIS=='OUI') :
        motscles['CREA_GROUP_MA'].append(_F(GROUP_MA = 'FONDFISS',
                                            NOM      = 'MAIL_ORI',
                                            POSITION = 'INIT'     ))
     if (TFISS=='NON_DEB') and (FISS_SOUDURE['TYPE']=='LONGUE') :
        motscles['CREA_GROUP_MA'].append(_F(GROUP_MA = 'FOND_SUP',
                                            NOM      = 'MA_ORI_S',
                                            POSITION = 'INIT'     ))
        motscles['CREA_GROUP_MA'].append(_F(GROUP_MA = 'FOND_INF',
                                            NOM      = 'MA_ORI_I',
                                            POSITION = 'INIT'     ))
  l_CREA_GROUP_NO.append('S_FOND1')
  l_CREA_GROUP_NO.append('S_FOND2')
  l_CREA_GROUP_NO.append('EQUERRE')
  motscles['CREA_GROUP_NO']=_F(GROUP_MA=l_CREA_GROUP_NO)
#
  __MAPROV=DEFI_GROUP(reuse   =__MAPROV,
                      MAILLAGE=__MAPROV,
                      **motscles )
#
  __MAPROV=MODI_MAILLAGE(reuse   =__MAPROV,
                         MAILLAGE=__MAPROV,
                         EQUE_PIQUA=_F( GROUP_NO  = 'EQUERRE' ,
                                        E_BASE    = EPT1  ,
                                        DEXT_BASE = DET1  ,
                                        L_BASE    = D1    ,
                                        L_CHANF   = D2    ,
                                        TYPE      = TYPSOU,
                                        H_SOUD    = H     , 
                                        ANGL_SOUD = ALPHA ,
                                        JEU_SOUD  = JEU   ,
                                        E_CORP    = EPC   , 
                                        DEXT_CORP = DEC   ,
                                        AZIMUT    = THETA ,
                                        RAFF_MAIL = TYPMAI,
                                        X_MAX     = XMAX  , )
                         )
#
  __MODELE=AFFE_MODELE( MAILLAGE=__MAPROV,
                        AFFE=_F( GROUP_MA     = ('EQUERRE','PEAUINT','EXCORP1','EXCORP2','EXTUBU'),
                                 PHENOMENE    = 'MECANIQUE'  ,
                                 MODELISATION = '3D'         , )
                         )
#
  motscles={}
  if TFISS=='DEB_INT' :
     motscles['ORIE_PEAU_3D']=_F(GROUP_MA=('PEAUINT','EXCORP1','EXCORP2','EXTUBU','LEVRTUBU','LEVRCORP'),)
  else :
     motscles['ORIE_PEAU_3D']=_F(GROUP_MA=('PEAUINT','EXCORP1','EXCORP2','EXTUBU',),)
  __MAPROV=MODI_MAILLAGE(reuse   =__MAPROV,
                         MAILLAGE=__MAPROV,
                         MODELE  =__MODELE,
                         **motscles
                         )
#
  if SAIN :
     __MAPROV=DEFI_GROUP(reuse         = __MAPROV,
                         MAILLAGE      = __MAPROV,
                         CREA_GROUP_NO = _F(GROUP_MA=('NIDXT','NEDXT','NIIXT','NEIXT')) )
#
     for i in range(1,NBAZIT+1):
       prec = EPC / 5.0
       __MAPROV=DEFI_GROUP(reuse         = __MAPROV,
                           MAILLAGE      = __MAPROV,
                         CREA_GROUP_NO = ( _F( NOM       = 'NID'+str(i) ,
                                               GROUP_NO  = 'NIDXT'      ,
                                               NUME_INIT = i            ,
                                               NUME_FIN  = i            ,),
                                           _F( NOM       = 'NED'+str(i) ,
                                               GROUP_NO  = 'NEDXT'      ,
                                               NUME_INIT = i            ,
                                               NUME_FIN  = i            ,),
                                           _F( NOM       = 'NII'+str(i) ,
                                               GROUP_NO  = 'NIIXT'      ,
                                               NUME_INIT = i            ,
                                               NUME_FIN  = i            ,),
                                           _F( NOM       = 'NEI'+str(i) ,
                                               GROUP_NO  = 'NEIXT'      ,
                                               NUME_INIT = i            ,
                                               NUME_FIN  = i            ,),
                                           _F( NOM       = 'LDN'+str(i) ,
                                               GROUP_MA  = 'LD' +str(i) ,),
                                           _F( NOM       = 'LD' +str(i) ,
                                               GROUP_NO  = 'LDN'+str(i) ,
                                               OPTION    = 'SEGM_DROI_ORDO',
                                               PRECISION =  prec        ,
                                               CRITERE   = 'ABSOLU'     ,
                                               GROUP_NO_ORIG   = 'NID'+str(i),
                                               GROUP_NO_EXTR   = 'NED'+str(i),),
                                           _F( NOM       = 'LIN'+str(i) ,
                                               GROUP_MA  = 'LI' +str(i) ,),
                                           _F( NOM       = 'LI' +str(i) ,
                                               GROUP_NO  = 'LIN'+str(i) ,
                                               OPTION    = 'SEGM_DROI_ORDO',
                                               PRECISION =  prec        ,
                                               CRITERE   = 'ABSOLU'     ,
                                               GROUP_NO_ORIG   = 'NII'+str(i),
                                               GROUP_NO_EXTR   = 'NEI'+str(i),),))
#
#
#     --- commande CREA_MAILLAGE ---
#
  self.DeclareOut('nomres',self.sd)
  nomres=CREA_MAILLAGE( MAILLAGE=__MAPROV,
                        CREA_POI1 = ( _F( NOM_GROUP_MA = 'P1_CORP ' ,
                                          GROUP_NO     = 'P1_CORP ' , ),
                                      _F( NOM_GROUP_MA = 'P2_CORP ' ,
                                          GROUP_NO     = 'P2_CORP ' , ),
                                      _F( NOM_GROUP_MA = 'P_TUBU ' ,
                                          GROUP_NO     = 'P_TUBU ' ,  ),)
                         )
#
  if IMPRESSION!=None:
     if IMPRESSION.__class__.__name__  !='MCList' : IMPRESSION  =[IMPRESSION,]
     for impr in IMPRESSION :
#
         if impr['FICHIER']!=None:
            DEFI_FICHIER(FICHIER = impr['FICHIER'],
                         UNITE   = impr['UNITE'  ] )
#
         motscles={}
         if impr['FORMAT']=='IDEAS'  : motscles['VERSION']  =impr['VERSION']
         if impr['FORMAT']=='CASTEM' : motscles['NIVE_GIBI']=impr['NIVE_GIBI']
         if impr['FICHIER']!=None    : motscles['FICHIER']  =impr['FICHIER']
         impr_resu = _F( MAILLAGE = nomres,
                         FORMAT   = impr['FORMAT'],
                         **motscles)
         IMPR_RESU( RESU = impr_resu )
#
  return ier

