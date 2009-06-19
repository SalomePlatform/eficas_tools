#@ AJOUT OpenturnsSolver Macro
# -*- coding: iso-8859-1 -*-
# RESPONSABLE

"""
Ce module contient le generateur XML pour Openturns
"""
import sys
print sys.path
import openturns

# Dictionnaires de conversion des valeurs lues dans EFICAS
# en valeurs reconnues par Open TURNS
# Les clefs 'None' sont les valeurs par defaut

VariableTypeByName = {
  "in"  : openturns.WrapperDataVariableType.IN,
  "out" : openturns.WrapperDataVariableType.OUT,
  None  :  openturns.WrapperDataVariableType.IN,
  }

FileTypeByName = {
  "in"  : openturns.WrapperDataFileType.IN,
  "out" : openturns.WrapperDataFileType.OUT,
  None  : openturns.WrapperDataFileType.IN,
  }

SymbolProvidedByName = {
  "no"  : openturns.WrapperSymbolProvided.NO,
  "yes" : openturns.WrapperSymbolProvided.YES,
  None  : openturns.WrapperSymbolProvided.NO,
  }

WrapperStateByName = {
  "shared"   : openturns.WrapperState.SHARED,
  "specific" : openturns.WrapperState.SPECIFIC,
  None       : openturns.WrapperState.SPECIFIC,
  }

WrapperModeByName = {
  "static-link"  : openturns.WrapperMode.STATICLINK,
  "dynamic-link" : openturns.WrapperMode.DYNAMICLINK,
  "fork"         : openturns.WrapperMode.FORK,
  None           : openturns.WrapperMode.FORK,
  }

WrapperDataTransferByName = {
  "files"     : openturns.WrapperDataTransfer.FILES,
  "pipe"      : openturns.WrapperDataTransfer.PIPE,
  "arguments" : openturns.WrapperDataTransfer.ARGUMENTS,
  "socket"    : openturns.WrapperDataTransfer.SOCKET,
  "corba"     : openturns.WrapperDataTransfer.CORBA,
  None        : openturns.WrapperDataTransfer.FILES,
  }

#==========================
# La classe de creation XML 
#==========================

class XMLGenerateur :

  '''
  Generation du fichier XML
  '''
  def __init__ (self, appli, DictMCVal, DictVariables ) :
    self.DictMCVal = DictMCVal
    self.DictVariables = DictVariables
    self.appli = appli

  def CreeXML (self) :
    '''
    Pilotage general de la creation du fichier XML
    '''
    data = openturns.WrapperData()
    data.setLibraryPath( self.GetMCVal('WrapperPath','') )
    data.setVariableList( self.VariableList() )
    data.setFunctionDescription( self.FunctionDefinition() )
    data.setGradientDescription( self.GradientDefinition() )
    data.setHessianDescription(  self.HessianDefinition()  )
    data.setFileList( self.FileList() )
    data.setParameters( self.Parameters() )
    data.setFrameworkData( self.FrameworkData() )
    
    wrapper=openturns.WrapperFile()
    wrapper.setWrapperData( data )
    
    return wrapper


  class __variable_ordering:
    def __init__ (self, dictVar) :
      self.dictVar = dictVar
      
    def __call__(self, a, b):
      return self.dictVar[a]['numOrdre'] - self.dictVar[b]['numOrdre']
  
  def VariableList (self) :
    '''
    Ecrit la liste des variables
    '''
    varList = openturns.WrapperDataVariableList()
    for var in sorted( self.DictVariables.keys(), self.__variable_ordering( self.DictVariables ) ) :
      varList.add( self.Variable( var, self.DictVariables[var] ) )
    return varList

  def Variable (self, var, dictVar) :
    '''
    Ecrit le parametrage d une variable
    '''
    variable = openturns.WrapperDataVariable()
    variable.id_ = var
    if dictVar[ 'Type' ] in VariableTypeByName.keys() :
      variable.type_ = VariableTypeByName[ dictVar[ 'Type' ] ]
    if dictVar.has_key('Comment')   : variable.comment_ = dictVar[ 'Comment' ]
    if dictVar.has_key('Unit')      : variable.unit_    = dictVar[ 'Unit'    ]
    if dictVar.has_key('Regexp')    : variable.regexp_  = dictVar[ 'Regexp'  ]
    if dictVar.has_key('Format')    : variable.format_  = dictVar[ 'Format'  ]
    return variable

  def FunctionDefinition (self) :
    '''
    Ecrit la description de la Fonction
    '''
    func = openturns.WrapperFunctionDescription()
    func.name_ = self.GetMCVal( 'FunctionName', '' )
    if (len(func.name_) != 0) : func.provided_ = SymbolProvidedByName[ 'yes' ]
    return func
  
  def GradientDefinition (self) :
    '''
    Ecrit la description du Gradient
    '''
    grad = openturns.WrapperFunctionDescription()
    grad.name_ = self.GetMCVal( 'GradientName', '' )
    if (len(grad.name_) != 0) : grad.provided_ = SymbolProvidedByName[ 'yes' ]
    return grad
  
  def HessianDefinition (self) :
    '''
    Ecrit la description de la Hessienne
    '''
    hess = openturns.WrapperFunctionDescription()
    hess.name_ = self.GetMCVal( 'HessianName', '' )
    if (len(hess.name_) != 0) : hess.provided_ = SymbolProvidedByName[ 'yes' ]
    return hess
  


  def FileList (self) :
    '''
    Ecrit la liste des fichiers
    '''
    fileList = openturns.WrapperDataFileList()
    for dictFile in self.GetMCVal('Files', []) :
      fileList.add( self.File( dictFile ) )
    return fileList

  def File (self, dictFile ) :
    '''
    Ecrit le parametrage d un fichier
    '''
    fich = openturns.WrapperDataFile()
    fich.id_ = dictFile[ 'Id' ]
    if dictFile[ 'Type' ] in FileTypeByName.keys() :
      fich.type_ = FileTypeByName[ dictFile[ 'Type' ] ]
    if dictFile.has_key('Name')   : fich.name_  = dictFile[ 'Name' ]
    if dictFile.has_key('Path')   : fich.path_  = dictFile[ 'Path' ]
    if dictFile.has_key('Subst')  :
      import string
      fich.subst_ = string.join( dictFile[ 'Subst' ], ',' )
    return fich

  def Parameters (self) :
    '''
    Ecrit les parametres de couplage au code externe
    '''
    parameters = openturns.WrapperParameter()
    parameters.mode_  = WrapperModeByName[ self.GetMCVal('WrapCouplingMode') ]
    parameters.state_ = WrapperStateByName[ self.GetMCVal('State') ]
    parameters.in_    = WrapperDataTransferByName[ self.GetMCVal('InDataTransfer') ]
    parameters.out_   = WrapperDataTransferByName[ self.GetMCVal('OutDataTransfer') ]
    return parameters
  
  def FrameworkData (self) :
    '''
    Ecrit les donnees liees a l utilisation d un framework englobant
    '''
    framework = openturns.WrapperFrameworkData()
    #framework.studycase_ = "12:23:34"
    framework.componentname_ = self.GetMCVal('SolverComponentName')
    return framework


  # ---------------------------------------------------------------------------------


  def GetTag (self, tag) :
    '''
    Recupere la chaine associee au tag dans la table dictTagsXML.
    Leve une exception si le tag n est pas trouve
    '''
    if ( dictTagsXML.has_key(tag) ) :
      return dictTagsXML[tag]
    else :
      raise KeyError, "Tag '%s' is undefined. This is an internal bug. Report bug to developers" % tag 
    pass
  
  def GetMCVal (self, MC, default = None, mandatory = False) :
    '''
    Recupere la chaine associee au MC dans la table DictMCVal.
    Leve une exception si le MC n est pas trouve et mandatory vaut True
    '''
    if ( self.DictMCVal.has_key(MC) and self.DictMCVal[MC] != None ) :
      return self.DictMCVal[MC]
    else :
      if ( mandatory ) :
        raise KeyError, "Keyword '%s' is mandatory" % MC
      else :
        return default
    pass
