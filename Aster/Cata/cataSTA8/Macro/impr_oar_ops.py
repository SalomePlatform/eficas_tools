#@ MODIF impr_oar_ops Macro  DATE 21/11/2007   AUTEUR MACOCCO K.MACOCCO 
# -*- coding: iso-8859-1 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2006  EDF R&D                  WWW.CODE-ASTER.ORG
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

# protection pour eficas
try:
   import aster
   from Utilitai.Utmess import UTMESS
   from Utilitai.Table import Table
   from Utilitai.partition import MAIL_PY
except:
   pass
   
def buildTabString(tabLevel):
   """
      Construit une chaine de tabulation
   """
   chaine = ''
   for i in range(0, tabLevel) :
      chaine += '\t'
      
   return chaine
   
def getBornes(listIn, valTest) :
   """
      Retourne un doublet de valeurs qui correspond aux valeurs de la liste qui encadrent la valeur (valTest)
      Si val n'est pas encadr�e par des valeurs de la liste, une des valeurs du doublet est None
   """
   v1 = None
   v2 = None   
   for val in listIn :
      if valTest > val : v1 = val
      if valTest < val : v2 = val
      
   # traitement des cas limites
   if valTest == listIn[0] : v1 = listIn[0]
   if valTest == listIn[len(listIn)-1] : v2 = listIn[len(listIn)-1]
   
   return (v1, v2) 

def interpoleLin(listDoublet, X) :
   """
      Interpole lin�airement entre deux bornes d�finies par listDoublets[(X0, Y0), (X1, Y1)] la valeur Y en X
   """
   X0 = listDoublet[0][0]
   Y0 = listDoublet[0][1]
   X1 = listDoublet[1][0]
   Y1 = listDoublet[1][1]
   
   return Y0 + (X - X0) * (Y1 - Y0) / (X1 - X0)

class interpolationError(Exception) :
   def __init__(self) :
      self.mess = 'Interpolation sur une valeur hors bornes'
      self.otherExcept = Exception()
        
   def getMess(self) :
      """ 
         retourne le message associ� � l'erreur
      """
      # Analyse les diff�rents cas d'erreurs
      if self.otherExcept == IOError :
         self.mess += "\nProbl�me � l'ouverture du fichier\n"

      return self.mess
 
class XMLNode :
    """
        Classe g�rant un noeud de l'arborescence XML
        Un noeud poss�de :
            - un nom de balise
            - un commentaire (optionnel)
            - un ensemble de "param�tres" (optionnels)
            - une liste d'�l�ment ou d'autres noeuds (optionnels/possibilit� de balises vides) :

        La classe propose : 
            - une m�thode "buildTree" qui parcoure le liste de mani�re r�cursive pour
              produire l'arborescence XML en vu de son enregistrement ou son impression
            - (TO DO) une methode statique "loadTree" qui produit un arbre XML � partir d'un fichier
    """
    def __init__(self, nomBalise, valeur = None, commentaire = None, **listOpt) :
        self.nomBalise = nomBalise
        self.commentaire = commentaire
        self.param = listOpt
        self.arbre=list()
        if valeur != None : self.addValue(valeur) # None n'est pas 0 !

    def getCommentaire(self) : return self.commentaire

    def setCommentaire(sel, commentaire) : self.commentaire = commentaire

    def getParametres(self) : return  self.param

    def setParametres(self, parametres) : self.param = parametres    

    def append(self, nodeName, valeur=None, commentaire = None, **listOpt) :
        """
            Ajoute un noeud � l'arborescence et retourne une r�f�rence sur ce noeud
            On peut ajouter directement la valeur, si simple, associ�e � la balise
        """
        node = XMLNode(nodeName, valeur, commentaire)

        self.arbre.append(node)

        return self.arbre[len(self.arbre)-1]

    def addValue(self, valeur):
        """
            Ajoute un �l�ment "simple" (nombre, texte) � l'arborescence
        """
        self.arbre.append(valeur)
            
    def buildTree(self, tabLevel=0) :
        """
            Construit l'arborescence XML en parcourant r�cursivement la structure de donn�e
            et la retourne sous la forme d'une chaine de caract�res

            tabLevel permet de g�rer l'indentation
        """
        # Construction de la chaine de tabulations n�cessaire � une bonne lecture du fichier XML
        tabString = buildTabString(tabLevel) 

        XMLString = ''
        
        try :
            # listOpt contient les param�tres optionnels de la balise
            chaine = ''
            for v in self.param.keys() :
                chaine = chaine + ' ' +  v  + '=' + self.param[v] 
        except : pass
        
        baliseOuverture=tabString + "<" + self.nomBalise + chaine +">\n"
        XMLString += baliseOuverture

        if self.commentaire :
            XMLString = XMLString + tabString + "\t<!--"+self.commentaire+"-->\n"

        for elem in self.arbre :
            try :
                XMLString += elem.buildTree(tabLevel+1)
            except : # l'�l�ment n'est pas un noeud
                XMLString = XMLString + tabString + '\t' + str(elem) + '\n'

        XMLString = XMLString + tabString + "</"+self.nomBalise+">\n"

        return XMLString

    def save(self, fileObj) :
        """ 
         Construit le l'arborescence XML et l'�crit dans un fichier 
         point� par le handler pass� en param�tres
        """ 
        try :
            fileObj.write(self.buildTree())
        except : pass

class OAR_element :
   """
      Classe de base des �l�ments manipul�s par IMPR_OAR
   """
   def __init__(self) :
      self.nodeComp = None
      
   def buildTree(self) : pass

   def getNode(self) :
      """
         Renvoie le noeud XML construit par buildTree
      """
      return self.nodeComp
   

class composant(OAR_element) :
   """
      Classe permettant de traiter les composants
      
      NB :
      1. L utilisateur est suppose faire la meme coupe pour le calcul mecanique et le calcul thermo-mecanique 
      2. Dans le cas d'un revetement, l'utilisateur est suppos� d�finir son plan de coupe de telle sorte 
         que la coupe de la structure et la coupe du revetement se raccordent
   """
   def __init__(self, **args) :
      self.nodeComp = XMLNode("COMPOSANT") # Racine de l'arborescence composant
      
      self.diametre = args['DIAMETRE']
      self.origine  = args['ORIGINE']
      self.coef_u   = args['COEF_U']
      self.angle_c  = args['ANGLE_C']
      self.revet    = args['REVET']
      
      self.lastAbscisse = None # Permet de gerer le recouvrement des points de coupe entre revetement et structure
      self.num_char = -1
      self.type_char = ''
      self.tabAbscisses = list()
      self.tabAbscisses_S = None
      self.dictMeca = dict()
      self.dictMeca_S = None # Pas cr�� car optionnel
      self.epaisseur = 0.0
      self.epaisseur_R = 0.0

      # dictionnaire g�rant le r�sultat contraintes en fonction des instants et des abscisses
      self.dictInstAbscSig = dict()
      self.dictInstAbscSig_S = None # Cr�ation si n�cessaire
      # dictionnaire g�rant le r�sultat temp�rature en fonction des instants et des abscisses
      self.dictInstAbscTemp = dict()
      self.dictInstAbscTemp_S = None # facultatif 
      self.list_inst = None
      self.num_tran = None    

      self.noResuMeca = False
      self.noResuTher = False
      
      # 1. resultat mecanique
      try : 
         # On ne construit qu'une table des abscisses et une table des contraintes.
         # Le revetement est obligatoirement en interne on commence par lui
         para_resu_meca = args['RESU_MECA']
         self.num_char = para_resu_meca['NUM_CHAR']
         self.type_char = para_resu_meca['TYPE']

         if self.revet == 'OUI' :
            # Construction de la table complementaire si revetement
            self.dictMeca_S = dict()
            self.tabAbscisses_S = list()
            self.buildTablesMeca('TABLE_S', para_resu_meca, self.tabAbscisses_S, self.dictMeca_S)
            self.epaisseur_R = abs(self.tabAbscisses_S[len(self.tabAbscisses_S)-1] - self.tabAbscisses_S[0])
         
         self.buildTablesMeca('TABLE', para_resu_meca, self.tabAbscisses, self.dictMeca, offset=self.epaisseur_R)
        
         if self.revet == 'OUI' :
            self.mergeDictMeca() # merge les tableaux resultats du revetement et de la structure

         # Calcul de l'�paisseur de la coupe.
         self.epaisseur = abs(self.tabAbscisses[len(self.tabAbscisses)-1] - self.tabAbscisses[0])
 
      except : 
         self.noResuMeca = True
      
      # 2. R�sultat thermique
      try :
         para_resu_ther = RESU_THER
         self.num_tran = para_resu_ther['NUM_TRAN']
         self.tabAbscisses = list()
         self.tabAbscisses_S = None
         
         listInst = list()
         if self.revet == 'OUI' :
            # Le revetement est obligatoirement en interne on commence par lui
            # 1. Construction champ temperature
            self.dictInstAbscTemp_S = dict()
            self.buildTemp('TABLE_ST', para_resu_ther, self.dictInstAbscTemp_S)
         
            # 2. Construction de la "table" des contraintes
            self.dictInstAbscSig_S = dict()
            self.tabAbscisses_S = list()
            self.buildTablesTher('TABLE_S', para_resu_ther, self.tabAbscisses_S, self.dictInstAbscSig_S)
               
            # 3. calcul de l'�paisseur
            self.epaisseur_R = abs(self.tabAbscisses_S[len(self.tabAbscisses_S)-1] - self.tabAbscisses_S[0])
         
         # Pour la structure
         # 1. Construction champ temp�rature
         self.buildTemp('TABLE_TEMP', para_resu_ther, self.dictInstAbscTemp, self.epaisseur_R)

         # 2. Construction de la table des contraintes
         self.buildTablesTher('TABLE_T', para_resu_ther, self.tabAbscisses, self.dictInstAbscSig, offset=self.epaisseur_R)
        
         if self.revet == 'OUI' :
            self.mergeDictTher() # merge les tableaux resultats du revetement et de la structure
            
         if  not(self.compareListAbscTher()) :
            UTMESS('F', 'IMPR_OAR', 'LES COUPES MECANIQUES ET THERMIQUE DOIVENT PARTAGER LES MEMES ABSCISSES')
            
         try :
            self.interpoleInstants() # Interpolation des instants de la table des temp�rature sur celle de la table m�canique
         except interpolationError, err:
            UTMESS('F', 'IMPR_OAR', err.getMess())

         # 3. Calcul de l'�paisseur de la coupe.
         self.epaisseur = abs(self.tabAbscisses[len(self.tabAbscisses)-1] - self.tabAbscisses[0])

      except :
         self.noResuTher = True
      
      # Construction de l arborescence
      self.buildTree() 
           
                
   def getAbscisses(self, dicoTable, tableAbsc, offset=0.0) :
      """
         R�cup�re la liste des abscisses
      """
      # r�cup�ration des abscisses
      ABSCISSES = dicoTable['ABSC_CURV']
     
      valeurAbsc = 0.0
      for val in ABSCISSES :
         valeurAbsc = val + offset
         tableAbsc.append(valeurAbsc)
         
   def buildTablesMeca(self, label, para_resu, tableAbsc, dictMeca, offset=0.0) :
      """
         Construction des tableaux m�canique 
      """ 
      sigma_xml   = ( 'S_RR', 'S_TT', 'S_ZZ', 'S_RT', 'S_TZ', 'S_ZR' )
      
      table_meca = para_resu[label].EXTR_TABLE() 
      
      # Utilisation des m�thodes de la classe table
      dictTable = table_meca.values()

      # r�cup�ration des abscisses
      self.getAbscisses(dictTable, tableAbsc, offset)
      
      # Construction de la table m�canique principale
      for val in sigma_xml :
         dictMeca[val] = list()

      S_XX = dictTable['SIXX']
      S_YY = dictTable['SIYY']
      S_ZZ = dictTable['SIZZ']
      S_XY = dictTable['SIXY']
      S_YZ = dictTable['SIYZ']
      S_XZ = dictTable['SIXZ']
      for v1, v2, v3, v4, v5, v6 in zip(S_XX, S_YY, S_ZZ, S_XY, S_YZ, S_XZ) :
         dictMeca['S_RR'].append(v1)
         dictMeca['S_TT'].append(v2)
         dictMeca['S_ZZ'].append(v3)
         dictMeca['S_RT'].append(v4)
         dictMeca['S_TZ'].append(v5)
         dictMeca['S_ZR'].append(v6)
    
   def mergeDictMeca(self) :
      """
      Merge des r�sultats m�caniques issus de la structure et du revetement
      """
      # Merge des listes d'abscisses
      # Le revetement est interieur la derniere abscisse du revetement doit etre egal a la premiere de la structure
      if self.tabAbscisses_S[len(self.tabAbscisses_S)-1] != self.tabAbscisses[0] :
         UTMESS('F', 'IMPR_OAR', 'LES COUPES DU REVETEMENT ET DE LA STRUCTURE DOIVENT PARTAGER UNE ABSCISSE COMMUNE')
         
      # On construit une table des abscisses tempopraire
      tableAbscTemp = self.tabAbscisses_S
      
      # On recopie la table des abscisses en sautant le premier
      debut = True
      for val in self.tabAbscisses :
         if debut :
            debut = False
            continue
         tableAbscTemp.append(val)
         
      self.tabAbscisses = tableAbscTemp
      
      # On construit des listes de travail interm�diaires que l'on commence par remplir avec les tables "suppl�mentaires"
      dictMecaBis = self.dictMeca_S
      
      # On recopie les �l�ments de la structure dans le tableau
      debut = True
      for v1, v2, v3, v4, v5, v6 in zip(self.dictMeca['S_RR'], self.dictMeca['S_TT'], self.dictMeca['S_ZZ'], self.dictMeca['S_RT'], self.dictMeca['S_TZ'], self.dictMeca['S_ZR']) :
         if debut :
            debut = False
            continue
         dictMecaBis['S_RR'].append(v1)
         dictMecaBis['S_TT'].append(v2)
         dictMecaBis['S_ZZ'].append(v3)
         dictMecaBis['S_RT'].append(v4)
         dictMecaBis['S_TZ'].append(v5)
         dictMecaBis['S_ZR'].append(v6)
         
      # On restitue ensuite la liste globale dans self.dictMeca
      self.dictMeca = dictMecaBis

  
   def buildTemp(self, label, para_resu, dictInstAbscTemp, offset=0.0):
      """
         R�cup�ration du champ temp�rature aux noeuds avec interpolation sur les "instants" du calcul m�canique
      """
      table_temp = para_resu[label].EXTR_TABLE()

      # Utilisation des m�thodes de la classe table
      dictTable = table_temp.values()
      
      # On construit un dictionnaire associant un "instant" avec un couple ("abscisse", "temp�rature")

      # 1. R�cup�ration de la liste des instants
      INSTANTS = dictTable['INST']
      for val in INSTANTS :
         dictInstAbscTemp[val] = 0 # On cr�e juste les cl�s du dictionnaire
         
      listTables = list() # liste de tables contenant une table pas instant
      for inst in dictInstAbscTemp.keys():
         listTables.append(table_temp.INST == inst)
         
      # 2. R�cup�ration des abscisses
      tableAbsc = list()
      self.getAbscisses(listTables[0].values(), tableAbsc, offset)
      
      # 3. R�cup�ration des temp�ratures
      tableTemp = list() # liste de liste de temp�rature (1 par instant)
      for tb in listTables :
         TEMPERATURE = tb.values()['TEMP']
         tableTemp.append(TEMPERATURE)
         
      # 4. Construction de dictInstAbscTemp
      for i in range(0, len(dictInstAbscTemp.keys())):
         listDoublets = list()
         for absc, temp in zip(tableAbsc, tableTemp[i]) :
            listDoublets.append((absc,temp))
            
         inst = dictInstAbscTemp.keys()[i]
         dictInstAbscTemp[inst] = listDoublets
         
   def buildTablesTher(self, label, para_resu, tabAbscisses, dictInstAbscSig, offset=0.0) :
      """
         Construction des tableaux thermo-m�canique
         listDictTher contient un dictionnaire par num�ro d'ordre 
      """
      table_temp = para_resu[label].EXTR_TABLE()   

      # On construit un dictionnaire associant un "instant" avec une liste de couples ("abscisse", liste de "sigma")

      # Utilisation des m�thodes de la classe table
      dictTable = table_temp.values()
      
      # On construit un dictionnaire associant un "instant" avec un couple ("abscisse", "temp�rature")

      # 1. R�cup�ration de la liste des instants
      INSTANTS = dictTable['INST']
      for val in INSTANTS :
         dictInstAbscSig[val] = 0 # On cr�e juste les cl�s du dictionnaire
         
      listTables = list() # liste de tables contenant une table pas instant
      for inst in dictInstAbscSig.keys():
         listTables.append(table_temp.INST == inst)
         
      # 2. R�cup�ration des abscisses
      self.getAbscisses(listTables[0].values(), tabAbscisses, offset)
         
      # 3. R�cup�ration des listes de sigma
      listListListSigAbscInst = list() # liste des sigma par abscisse par instant
      for tbl in listTables:
         listListSigAbscInst = list()
         
         # On cr�e une table pour chaque instant
         S_XX = tbl.values()['SIXX']
         S_YY = tbl.values()['SIYY']
         S_ZZ = tbl.values()['SIZZ']
         S_XY = tbl.values()['SIXY']
         S_YZ = tbl.values()['SIYZ']
         S_XZ = tbl.values()['SIXZ']
         for v1, v2, v3, v4, v5, v6 in zip(S_XX, S_YY, S_ZZ, S_XY, S_YZ, S_XZ) :
            listSigAbsc = list() # Liste des sigmas pour une abscisse
            listSigAbsc.append(v1)
            listSigAbsc.append(v2)
            listSigAbsc.append(v3)
            listSigAbsc.append(v4)
            listSigAbsc.append(v5)
            listSigAbsc.append(v6)
            
            listListSigAbscInst.append(listSigAbsc)
            
         listListListSigAbscInst.append(listListSigAbscInst)
         
      # 4. Assemblage du dictionnaire
      for i in range(0, len(dictInstAbscSig.keys())) :
         listDoublet = list()
         for j in range(0, len(tabAbscisses)) :
           listDoublet.append((tabAbscisses[j], listListListSigAbscInst[i][j]))
               
         dictInstAbscSig[dictInstAbscSig.keys()[i]] = listDoublet 

   def mergeDictTher(self) : 
      """
         Merge les resultats issus de la coupe du revetement avec ceux issus de la coupe de la structure
      """
      # Merge des listes d'abscisses
      # Le revetement est interieur la derniere abscisse du revetement doit etre egal a la premiere de la structure
      if self.tabAbscisses_S[len(self.tabAbscisses_S)-1] != self.tabAbscisses[0] :
         UTMESS('F', 'IMPR_OAR', 'LES COUPES DU REVETEMENT ET DE LA STRUCTURE DOIVENT PARTAGER UNE ABSCISSE COMMUNE')
         
      # On construit une table des abscisses tempopraire
      tableAbscTemp = self.tabAbscisses_S
      
      # On recopie la table des abscisses en sautant le premier
      debut = True
      for val in self.tabAbscisses :
         if debut :
            debut = False
            continue
         tableAbscTemp.append(val)
         
      self.tabAbscisses = tableAbscTemp
       
      # On construit des listes de travail interm�diaires que l'on commence par remplir avec les tables "suppl�mentaires"
      dictInstAbscSigBis = self.dictInstAbscSig_S
      dictInstAbscTempBis = self.dictInstAbscTemp_S
      
      # On recopie les �l�ment thermiques de la structure principale en sautant la premi�re abscisse de la structure
      for key in dictInstAbscTempBis.keys() : # Les dictionnaires partagent les memes instants
         debut = True
         for valTher in self.dictInstAbscTemp[key] :
            if debut :
               debut = False
               continue
            dictInstAbscTempBis[key].append(valTher)
            
      # On recopie les �l�ment m�caniques de la structure principale en sautant la premi�re abscisse de la structure
      for key in dictInstAbscSigBis.keys() : # Les dictionnaires partagent les memes instants
         debut = True
         for valSig in self.dictInstAbscSig[key] :
            if debut :
               debut = False
               continue
            dictInstAbscSigBis[key].append(valSig)

      # On restitue ensuite la liste globale dans self.dictInstAbscSig
      self.dictInstAbscSig = dictInstAbscSigBis
      self.dictInstAbscTemp = dictInstAbscTempBis

   def compareListAbscTher(self) :
      """
         V�rifie que la coupe du champ thermique et la coupe m�canique partagent les memes abscisses
      """
      # 1. R�cup�ration des abscisses associ�es aux temp�ratures
      listAbsc = list()
      lstDoublet = self.dictInstAbscTemp[self.dictInstAbscTemp.keys()[0]]
      for val in lstDoublet :
         listAbsc.append(val[0])
         
      # 2. Comparaison des deux listes 
      for A1, A2 in zip(self.tabAbscisses, listAbsc) :
         if A1 != A2 : return False
      
      return True
      
   def interpoleInstants(self) :
      """
         Interpole les r�sultats thermique sur les instants des r�sultats m�caniques
      """
      # 1. r�cup�ration des instants des deux tables
      listInstTher = self.dictInstAbscTemp.keys()
      listInstMeca = self.dictInstAbscSig.keys()
      
      # 2. calcul de la liste des bornes de la table thermique qui encadrent les r�sultats m�caniques
      dictInstAbscTemp = dict()
      listAbscTemp = list()
      listBornes = list()
      for inst in listInstMeca :
         bornes = getBornes(listInstTher, inst)
         # Si une des bornes n'est pas d�finie, on lance une exception
         if not(bornes[0]) or not(bornes[1]) : raise interpolationError
          
         abscTempInf = self.dictInstAbscTemp[bornes[0]] # Liste de doublet (abscisse, temperature) pour la borne inf�rieure
         abscTempSup = self.dictInstAbscTemp[bornes[1]] # Liste de doublet (abscisse, temperature) pour la borne sup�rieure
         
         listAbscTemp = list() # liste de couples abscisses/Temp�rature
         for A1, A2 in zip(abscTempInf, abscTempSup) : # A1 et A2 sont des doublets abscisse/Temperature
            temperature = interpoleLin( ((bornes[0], A1[1]), (bornes[1], A2[1])), inst)   
            listAbscTemp.append((A1[0], temperature)) # on aurait pu tout aussi bien prendre A2[0] (c est pareil ...)
            
         dictInstAbscTemp[inst] = listAbscTemp
         
      # remplacement de l'ancienne table par la nouvelle
      self.dictInstAbscTemp = dictInstAbscTemp

   def buildTree(self) :
      """
         Construction (en m�moire) de l'arborescence du document XML
      """
      sigma_xml   = ( 'S_RR', 'S_TT', 'S_ZZ', 'S_RT', 'S_TZ', 'S_ZR' )

      # Cr�ation de l'arborescence "g�om�trie"
      nodeGeomComp = self.nodeComp.append("GEOM_COMPO")
      nodeGeomComp.append("REVETEMENT", valeur=self.revet)
      if self.revet == 'OUI' :
         nodeGeomComp.append("EP_REVET", valeur=self.epaisseur_R)
      nodeLigneCoupe = nodeGeomComp.append("LIGNE_COUPE")
      nodeLigneCoupe.append("EPAISSEUR_EF", valeur=self.epaisseur)
      nodeLigneCoupe.append("DIAM_EXT_EF", valeur=self.diametre)
      nodeLigneCoupe.append("ORI_ABSC", valeur=self.origine)
      
      if self.noResuMeca == False :
         # Cr�ation des abscisses
         for val in self.tabAbscisses :
            nodeLigneCoupe.append("ABSCISSE", val)
      
         nodeLigneCoupe.append('PSI', self.angle_c)
      
         # Cr�ation des r�sultats m�caniques
         nodeSigma_u = self.nodeComp.append("SIGMA_UNITE")
         nodeSigma_u.append("NUM_MECA", valeur=self.num_char)
         nodeSigma_u.append("NOM_MECA", valeur=self.type_char)
         nodeSigma_meca = nodeSigma_u.append("SIGMA_MECA")
         
         for i in range(0, len(self.tabAbscisses)) :
            for val in self.dictMeca.keys() :
               nodeSigma_meca.append(val, valeur = self.dictMeca[val][i])
     
      # Cr�ation de l'arborescence "r�sultat thermo_m�canique"
      if self.noResuTher == False :
         # Cr�ation des abscisses
         listDoublet = self.dictInstAbscTemp[self.dictInstAbscTemp.keys()[0]]
         for val in listDoublet :
            nodeLigneCoupe.append("ABSCISSE", val[0])
            
         nodeLigneCoupe.append('PSI', self.angle_c)
            
         # Cr�ation des r�sultats m�caniques
         nodeSigma_ther_c = self.nodeComp.append("SIGMA_THER_C")
         nodeSigma_ther_c.append("NUM_TRANSI_THER", valeur=self.num_tran)
         
         for inst in self.dictInstAbscTemp.keys() : # boucle sur les instants
            nodeSigma_ther = nodeSigma_ther_c.append("SIGMA_THER")
            nodeSigma_ther.append("INSTANT", valeur=inst)
            
            # boucle sur les abscisses
            for doubletAbscSig, doubletAbscTemp in zip(self.dictInstAbscSig[inst], self.dictInstAbscTemp[inst]) : 
               nodeSigma_point = nodeSigma_ther.append("SIGMA_POINT")
               for val, label in zip(doubletAbscSig[1], sigma_xml) :
                  nodeSigma_point.append(label, valeur = val)
               
               nodeSigma_point.append("TEMPERATURE", doubletAbscTemp[1]) 

class tuyauterie(OAR_element) :
   """
      Classe permettant de traiter les tuyauteries
   """
   def __init__(self, **args) :
      self.nodeComp = XMLNode("TUYAUTERIE")
      try :
         self.para_resu_meca = args['RESU_MECA']
         self.num_char = self.para_resu_meca['NUM_CHAR']
      
         #Gestion du maillage
         self.maillage = self.para_resu_meca['MAILLAGE']
         mapy = MAIL_PY()
         mapy.FromAster(self.maillage)
      
         self.ma = [val.rstrip() for val in mapy.correspondance_mailles]
         self.no = [val.rstrip() for val in mapy.correspondance_noeuds]
      
         self.dictMailleNoeuds = dict()
         for val in self.ma :
            self.dictMailleNoeuds[val] = list()
      
         for i in range(0, len(mapy.co)) :
            self.dictMailleNoeuds[self.ma[i]].append(self.no[mapy.co[i][0]])
            self.dictMailleNoeuds[self.ma[i]].append(self.no[mapy.co[i][1]])
      
         self.dictNoeudValTorseur = dict()
         self.buildTableTorseur()
      
      except :
         UTMESS('F', 'IMPR_OAR', "ERREUR D'ACCES AUX DONNEES")

      # Construction de l arborescence
      self.buildTree() 
       

   def buildTableTorseur(self) :
      """
         Construit un dictionnaire associant un noeud � un torseur exprim� sous la forme d'une liste de valeurs
      """
      table_temp = self.para_resu_meca['TABLE'].EXTR_TABLE()   

      # Utilisation des m�thodes de la classe table
      dictTable = table_temp.values()
      
      # 1. R�cup�ration de la liste des noeuds
      NOEUDS = dictTable['NOEUD']
      for val in NOEUDS :
         self.dictNoeudValTorseur[val.rstrip()] = list() # On cr�e juste les cl�s du dictionnaire
         
      N   = dictTable['N']
      VY  = dictTable['VY']
      VZ  = dictTable['VZ']
      MT  = dictTable['MT']
      MFY = dictTable['MFY']
      MFZ = dictTable['MFZ']
      
      for no, n, vy, vz, mt, mfy, mfz in zip(NOEUDS, N, VY, VZ, MT, MFY, MFZ):
         no = no.rstrip()
         self.dictNoeudValTorseur[no].append(n)
         self.dictNoeudValTorseur[no].append(vy)
         self.dictNoeudValTorseur[no].append(vz)
         self.dictNoeudValTorseur[no].append(mt)
         self.dictNoeudValTorseur[no].append(mfy)
         self.dictNoeudValTorseur[no].append(mfz)
         
         
   def buildTree(self) :
      """
         Construction (en m�moire) de l'arborescence du document XML
      """
      torseur_XML   = ( 'FX', 'FY', 'FZ', 'MX', 'MY', 'MZ' )

      # Cr�ation de l'arborescence "torseur"
      nodeTMG = self.nodeComp.append("TORSEUR_MECA-GRP")
      nodeTM = nodeTMG.append("TORSEUR_MECA")
      nodeTM.append("oar:CHAR-REF", self.num_char)
      nodeMTG = nodeTM.append("MAILLE_TORSEUR-GRP")
      nodeMT = nodeMTG.append("MAILLE_TORSEUR")
      for MA in self.dictMailleNoeuds.keys() : # Boucle sur les mailles
         nodeMT.append("oar:MAILLE-REF", MA)
         for NO in self.dictMailleNoeuds[MA] : # 2 noeuds
            nodeTorseur = nodeMT.append("oar:TORSEUR")
            for val, cle in zip(self.dictNoeudValTorseur[NO], torseur_XML) : # 6 valeurs
               nodeTorseur.append(cle, val)
      
      

def impr_oar_ops(self, TYPE_CALC, **args) :
   """
   Macro IMPR_OAR
   Ecrit des fichiers au format XML selon la DTD OAR Fichier
   
   IMPR_OAR va etre utilise en deux fois d abord calcul mecanique, 
   ensuite calcul thermique ce qui implique qu il ne peut y avoir qu'une seule des deux options a la fois
   """
   # La macro compte pour 1 dans la num�rotation des commandes
   self.set_icmd(1)
   
   obj = None
   
   if TYPE_CALC=='COMPOSANT' :
      obj = composant(**args)
   elif TYPE_CALC=='MEF' : 
      UTMESS('F', 'IMPR_OAR', 'FONCTION NON IMPLANTEE') 
   elif TYPE_CALC=='TUYAUTERIE' :
      obj = tuyauterie(**args) 
   else :
      UTMESS('F', 'IMPR_OAR', 'Mot cl� facteur inconnu')

   # Ecriture dans le fichier
   # R�cup�ration de la LU du fichier de sortie
   try :
      unite = args['UNITE']
   except :
      unite = 38
      
   try :
      ajout=args['AJOUT']
   except :
      ajout='NON'
         
   name = 'fort.'+str(unite)
   try :
      if ajout=='NON' :  # nouveau fichier
         fileObj = open(name, 'wt')
      else :            # extension du fichier existant
         fileObj = open(name, 'a+t')
   except IOError :
      UTMESS('F', 'IMPR_OAR', "Erreur � l'ouverture du fichier") 
   else :
      obj.getNode().save(fileObj)
      fileObj.close()