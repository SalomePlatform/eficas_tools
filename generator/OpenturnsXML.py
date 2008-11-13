#@ AJOUT OpenturnsSolver Macro
# -*- coding: iso-8859-1 -*-
# RESPONSABLE

"""
Ce module contient le generateur XML pour Openturns
"""

#  Les variables
#---------------------

# OrdreVariable contient l'ordre des MC pour definir une variable en XML
# dictMCXML a pour cle le nom du MC dans la commande,
# Il contient aussi une liste donnant les informations suivantes
# 	0 : debut de ligne
#	1 : fin de ligne
#	2 : code : 0 : facultatif, 1 : obligatoire 
# Type est sur la meme ligne que Name

OrdreVariable = ( 'Name', 'Type', 'Comment', 'Unit', 'Regexp', 'Format' )
dictMCXML = { "Name"    : ( '        <variable id="',  '" ',           1 ), 
              "Type"    : ( 'type ="'               ,  '">\n',         1 ),
              "Comment"	: ( '          <comment>'   ,  '</comment>\n', 0 ),
              "Unit"	: ( '          <unit>'      ,  '</unit>\n',    0 ),
              "Regexp"	: ( '          <regexp>'    ,  '</regexp>\n',  0 ),
              "Format"	: ( '          <format>'    ,  '</format>\n',  0 ),
              }


#  Les fonctions du wrapper
#--------------------------------
# OrdreLibrary contient l'ordre des MC pour definir la partie library en XML
# dictLibXML a pour cle le nom du MC dans la commande,
# Il contient aussi une liste donnant les informations suivantes :
# 	0 : debut de ligne
#	1 : milieu de ligne si le MC est present
#	2 : milieu de ligne si le MC n est pas present
#	3 : fin de ligne
#   4 : code :  0 : facultatif, 1 : obligatoire sans defaut

OrdreLibrary = ( 'FunctionName', 'GradientName', 'HessianName' )
dictLibXML = { "FunctionName" : ( '\n\n      <!-- The function that we try to execute through the wrapper -->',
                                  '\n      <function provided="yes">',
                                  '\n      <function provided="no">',
                                    '</function>',
                                  1,
                                  ),
               "GradientName" : ( '\n\n      <!-- The gradient of the function -->',
                                  '\n      <gradient provided="yes">',
                                  '\n      <gradient provided="no">',
                                  '</gradient>',
                                  0,
                                  ),
               "HessianName"  : ( '\n\n      <!-- The hessian of the function wrapper -->',
                                  '\n      <hessian provided="yes">',
                                  '\n      <hessian provided="no">' ,
                                  '</hessian>\n\n',
                                  0,
                                  ),
               }

#  Les communications du wrapper
#--------------------------------
# OrdreWrapMode contient l'ordre des MC pour definir la partie WrapMode en XML
# dictWrMXML a pour cle le nom du MC dans la commande,
# Il contient aussi une liste donnant les informations suivantes
# 	0 : debut de ligne
#	1 : fin de ligne
#	2 : code : 0 : facultatif, 1 : obligatoire sans defaut, 2 : obligatoire avec defaut
#	3 : valeur par defaut eventuelle
OrdreWrapMode = ( 'WrapCouplingMode', 'State', 'InDataTransfer', 'OutDataTransfer' )
dictWrMXML = { "WrapCouplingMode" : ( '\n    <wrap-mode type="'        , '"'     ,  1 ),
               "State"            : ( ' state="'                       , '">\n'  ,  2,  'shared">\n' ),
	       "InDataTransfer"   : ( '      <in-data-transfer mode="' , '" />\n',  0 ),
	       "OutDataTransfer"  : ( '      <out-data-transfer mode="', '" />\n',  0 ),
               }

# Les fichiers d'echange du wrapper
#-----------------------------------------
# OrdreExchangeFile contient l'ordre des MC pour definir la partie OrdreExchangeFile en XML
# dictFilXML a pour cle le nom du MC dans la commande,
# Il contient aussi une liste donnant les informations suivantes
# 	0 : debut de ligne
#	1 : fin de ligne
#	2 : code : 0 : facultatif, 1 : obligatoire sans defaut
OrdreExchangeFile = ( 'Id', 'Type', 'Name', 'Path', 'Subst' )
dictFilXML = { "Id"    : ( '\n      <file id="', '">'       ),
	       "Type"  : ( ' type="'           , '">'       ),
	       "Name"  : ( '\n        <name>'  , '</name>'  ),
	       "Path"  : ( '\n        <path>'  , '</path>'  ),
	       "Subst" : ( '\n        <subst>' , '</subst>' ),
               }


#==========================
# La classe de creation XML 
#==========================

class XMLGenerateur :

  '''
  Generation du fichier XML
  '''
  def __init__ (self, DictMCVal, ListeVariables, DictLois ) :
  #---------------------------------------------------------#
    self.ListeFiles = []
    self.DictMCVal = DictMCVal
    self.ListeVariables = ListeVariables
    self.DictLois = DictLois 

  def CreeXML (self) :
  #------------------#
    '''
    Pilotage general de la creation du fichier XML
    '''
    self.texte  = self.CreeEntete()
    self.texte += self.CreeWrapperAndPath()
    self.texte += self.CreeVariables()
    self.texte += self.CreeLibrary()
    self.texte += self.CreeFile()
    self.texte += self.CreeWrapMode()
    self.texte += self.CreeCommande()
    return self.texte


  def CreeEntete (self) :
  #---------------------#
    '''
    La variable DTDDirectory doit etre dans DictMCVal
    '''
    #PN a faire : recuperer DTDDirectory dans editeur.ini
    texte = "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n"
    if self.DictMCVal.has_key("DTDDirectory")  :
      aux = os.path.join(self.DictMCVal["DTDDirectory"], "wrapper.dtd")
      texte += "<!DOCTYPE wrapper SYSTEM \"" + aux + "\">\n"
    texte += '\n<wrapper>\n'
    texte += '\n  <library>\n\n'
    return texte


  def CreeWrapperAndPath (self) :
  #-----------------------------#
    texte  = '    <!-- The path of the shared object -->\n'
    texte += '    <path>'
    if self.DictMCVal.has_key("WrapperPath") :
      texte += self.DictMCVal["WrapperPath"]
    else :
      print "*********************************************"
      print "*          ERREUR GENERATION XML            *"
      print "*       champ WrapperPath non rempli        *"
      print "*********************************************"
    texte += '</path>\n\n\n'

    return texte


  def CreeVariables (self) :
  #------------------------#
    texte  ='    <!-- This section describes all exchanges data between the wrapper and the platform -->\n'
    texte +='    <description>\n\n'
    texte +='      <!-- Those variables are substituted in the files above -->\n'
    texte +='      <!-- The order of variables is the order of the arguments of the function -->\n\n'
    texte += '      <variable-list>'

    numvar = 0
    for DictVariable in self.ListeVariables :
      texte += "\n        <!-- The definition of variable # "+  str(numvar) + " -->\n"
      for MC in OrdreVariable :
        if DictVariable.has_key(MC) :
          texte += dictMCXML[MC][0] + DictVariable[MC] + dictMCXML[MC][1]
        else :
          if dictMCXML[MC][2] :
            print "**************************************************"
            print "*            ERREUR GENERATION XML               *"
            print "*  champ obligatoire non rempli pour variable    *"
            print "**************************************************"
      texte += '        </variable>\n'
      numvar += 1
    texte += '\n      </variable-list>\n'
    texte += '      <!-- End of variable description -->\n'
    return texte

  def CreeLibrary (self) :
  #----------------------#
    '''
    Librairies
    '''
    texte = ""
    for MC in OrdreLibrary :
      texte += dictLibXML[MC][0]
      if self.DictMCVal.has_key(MC) :
        texte += dictLibXML[MC][1] + self.DictMCVal[MC] + dictLibXML[MC][3]
      else :
        texte += dictLibXML[MC][2] + dictLibXML[MC][3]
        if dictLibXML[MC][4] :
          print "**************************************************"
          print "*            ERREUR GENERATION XML               *"
          print "*  champ obligatoire non rempli pour wrapper     *"
          print "**************************************************"
    texte += '    </description>\n\n'
    texte += '  </library>\n'
    return texte

  def CreeFile (self) :
  #-------------------#
    '''
    Fichiers
    '''
    texte  = '\n  <external-code>\n'
    texte += '\n    <!-- Those data are external to the platform (input files, etc.)-->\n'
    texte += '    <data>\n'

    if self.DictMCVal.has_key("exchange_file") :
       for dico in self.DictMCVal["exchange_file"] :
          texte += "\n      <!-- The definition of file  -->"
          for MC in OrdreExchangeFile :
              if dico.has_key(MC) :
                 texte += dictFilXML[MC][0] + dico[MC] + dictFilXML[MC][1]
          texte += "\n      </file>\n"
    texte += '\n    </data>\n'
    return texte

  def CreeWrapMode (self) :
  #-----------------------#
    '''
    WrapMode
    '''
    texte = '\n    <!-- Transfert data mode through Wrapper -->'

    for MC in OrdreWrapMode :
      if self.DictMCVal.has_key(MC) :
        texte += dictWrMXML[MC][0] + self.DictMCVal[MC] + dictWrMXML[MC][1]
      else :
        if dictWrMXML[MC][2] == 2 :
          texte += dictWrMXML[MC][0] + dictWrMXML[MC][3]
        elif dictWrMXML[MC][2] == 1 :
          print "**************************************************"
          print "*            ERREUR GENERATION XML               *"
          print "*  champ obligatoire non rempli pour external    *"
          print "**************************************************"
    texte += '    </wrap-mode>\n\n'
    return texte

  def CreeCommande (self) :
  #-----------------------#
    '''
    La commande
    On lui passera en argument les options supplementaires eventuelles
    '''
    texte  = '    <!-- Command -->\n'
    texte += '    <command>'
    if self.DictMCVal.has_key("Command") :
      texte += self.DictMCVal["Command"]
      if self.DictMCVal.has_key("ArguCommande") :
         for argument in self.DictMCVal[ArguCommande] :
             texte += " " + argument
	 texte += "\n"
    else :
      texte += '# no command'
    texte +='</command>\n'
    texte +='\n  </external-code>\n'
    texte +='\n</wrapper>\n'
    return texte

