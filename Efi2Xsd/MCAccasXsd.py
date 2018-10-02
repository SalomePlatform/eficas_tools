#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import traceback
#import raw.efficas as efficas
import types

sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))

try :
  import pyxb
  import pyxb.binding
  import pyxb.binding.basis
except : 
  pass
#import pyxb.utils.utility
#import pyxb.utils.domutils

class X_OBJECT:
# -------------

  def deletePyxbObject(self):
      if not self.cata or  not self.cata.modeleMetier : return
      print ('----------- deletePyxbObject', self.nom)  
      indice = 0
      trouve = False
      for i in self.perePyxb.objPyxb.orderedContent(): 
            if id(self.objPyxb) == id(i._Content__value) : trouve = True ;break
            indice = indice + 1
      if not trouve : print ('objet pas trouve')
      print (self.perePyxb.objPyxb.description)
      del self.perePyxb.objPyxb.__dict__[self.nom]
      print (self.perePyxb.objPyxb.__delattr__)
      #delattr(self.perePyxb.objPyxb,self.nom)
      # PNPN
      
      print ('delattr', self.perePyxb.objPyxb,self.nom)
      del self.perePyxb.objPyxb.orderedContent()[indice]


class X_MCSIMP(X_OBJECT):
# -----------------------
      
   def buildObjPyxb(self) :
      # self.valeur tient compte de la valeur par defaut
      # utiliser getValeur ? expression numpy
      if not self.cata or  not self.cata.modeleMetier : return
      #print ('X_MCSIMP buildObjPyxb', self.nom, self,self.valeur)
      #if self.nom == 'diameter' : 
      #    traceback.print_stack()
      #    print ('****************************************************')
      # print ('objPyxbDeConstruction', self.objPyxbDeConstruction)
      #if self.objPyxbDeConstruction == None : print (self.nom, ' pas de pyxb')
      if self.objPyxbDeConstruction != None :
        self.objPyxb = self.objPyxbDeConstruction
        self.maClasseModeleMetier =type(self.objPyxb)
        #print (self.maClasseModeleMetier)
        self.objPyxbDeConstruction = None
      else :
        self.monNomClasseModeleMetier='T_'+self.nom
        self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)
        #print (self.maClasseModeleMetier)
        #print (self.valeur)
        #print (type(self.valeur))
        if self.valeur != None : self.objPyxb=self.maClasseModeleMetier(self.valeur)
        elif self.definition.into != None and 'TXM' in self.definition.type  : self.objPyxb = None
        else                   : self.objPyxb=self.maClasseModeleMetier(); 
      self.filsPyxb=None
      #print ('X_MCSIMP', self.nom, self.objPyxb)
      #print ('fin X_MCSIMP', self.objPyxb, self.nom,self)


   def setValeurObjPyxb(self,newVal):
       if not self.cata or  not self.cata.modeleMetier : return
       print ('dans setValeurObjPyxb MCSIMP')
       #  print (self.nom , ' a pour pere', self.perePyxb, self.perePyxb.nom, self.perePyxb.objPyxb)
       if newVal != None : nvlObj=self.maClasseModeleMetier(newVal)
       else              : nvlObj=self.maClasseModeleMetier()
       self.val=newVal
       setattr(self.perePyxb.objPyxb,self.nom,nvlObj)
       print ('setattr', self.perePyxb.objPyxb,self.nom)
       trouve=False
       indice=0
       for i in self.perePyxb.objPyxb.orderedContent(): 
           if isinstance(i._Content__value, self.maClasseModeleMetier) : 
              self.perePyxb.objPyxb.orderedContent()[indice]=self.perePyxb.objPyxb.orderedContent()[-1]
              del(self.perePyxb.objPyxb.orderedContent()[-1])
              trouve=True
              break
           indice+=1
       if not trouve : print ('Attention souci au changement de valeur de ', self.nom)
       self.objPyxb=nvlObj
       print ('iiiiiiiiiiiiiiiiiiiiiiiiiiiiii', nvlObj, id(nvlObj))
       #for i in self.perePyxb.objPyxb.orderedContent(): 
       #    print ('ds le for pour i')
       #    print (i._Content__value)
       #    print (id(i._Content__value))
       #    print (type((i._Content__value)))
       #    if id(i._Content__value) == id(self.objPyxb) : break
       #    indexOC +=1

       #maValeur = getattr(self.perePyxb.objPyxb, self.nom)
       #print ('je change', indexOC)
       #if isinstance(maValeur, pyxb.binding.basis.simpleTypeDefinition):
       #if 1 :
       #   print ('jkjkljkljklj')
       #   setattr(self.perePyxb.objPyxb,self.nom,nvlObj)
       #   self.perePyxb.objPyxb.orderedContent()[indexOC]=self.perePyxb.objPyxb.orderedContent()[-1]
       #   del(self.perePyxb.objPyxb.orderedContent()[-1])
       #print ('apres',self.nom, self.perePyxb.objPyxb.orderedContent())
       #else :
       #   index=0
       #   trouve=False
       #   try :
       #     for i in maValeur: 
       #       if id(i) == id(self.objPyxb) :trouve = True ; break
       #       index=index+1
       #     maValeur[index]=nvlObj
       #     self.perePyxb.objPyxb.orderedContent()[indexOC]._Content__value=nvlObj
       #   except : pass
       #   if not trouve : print (self.nom , 'pas trouve')

       #print ('arret programme'); exit()

       #print ('id objPyxb',id(self.objPyxb))
       #print ('id objPyxb[0]',id(self.objPyxb[0]))
       #print ('id elt ', id(self.objPyxb._element), self.objPyxb._element, type(self.objPyxb._element), type(self.objPyxb._element()))
       #print ('        perePyxb _ElementMap')
       #print (self.perePyxb.objPyxb._ElementMap)
       #index=0
       #for i in self.perePyxb.objPyxb._ElementMap.keys() : 
       #    print (id(i), ' ',  id(self.perePyxb.objPyxb._ElementMap[i]))
           #print (dir(self.perePyxb.objPyxb._ElementMap[i]))
       #    print (id(self.perePyxb.objPyxb._ElementMap[i]))
#	   index=index+1
       #print ('        objPyxb monBinding id')
       #monBinding = getattr(self.perePyxb.objPyxb, self.nom)
       #for i in monBinding : print id(i)
       #print ('        perePyxb orderedContent')
       #for i in self.perePyxb.objPyxb.orderedContent(): 
       #    print id(i._Content__value)
       #    print (i._Content__value, type(i._Content__value))
       #print ('        perePyxb orderedContent')
       #for i in self.perePyxb.objPyxb.content(): print id(i)
       
       #print (self.perePyxb.objPyxb.orderedContent())
       #print (monBinding)
        
      
   def addPyxbObject(self, indiceDsLeContenu):
      if not self.cata or  not self.cata.modeleMetier : return

      # adherence Accas sur le parent
      parent=self.parent
      while (parent.isBLOC() ): parent=parent.parent
      self.perePyxb=parent

      self.monNomClasseModeleMetier='T_'+self.nom
      self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)
      nvlObj=self.maClasseModeleMetier() 
      print ('setattr', self.perePyxb.objPyxb,self.nom)
      setattr(self.perePyxb.objPyxb,self.nom,nvlObj)
      tampon=self.perePyxb.objPyxb.orderedContent()[-1]
      self.objPyxb  = nvlObj
      indexOC=-1
      longueur=len(self.perePyxb.objPyxb.orderedContent())
      for i in reversed(range(longueur)):
          self.perePyxb.objPyxb.orderedContent()[i]=self.perePyxb.objPyxb.orderedContent()[i-1]
          if i == indiceDsLeContenu + 1 : break
      self.perePyxb.objPyxb.orderedContent()[indiceDsLeContenu]=tampon


      #for i in self.perePyxb.objPyxb.orderedContent() :
      #    print (i._Content__value, type(i._Content__value))
      #print ('----------------')

      #print self.perePyxb.objPyxb.orderedContent()
      #for i in  self.perePyxb.objPyxb.orderedContent():
      #     print ('valeur de ', i)
      #     print (i._Content__value)
      #     print (type(i._Content__value))
      #     if isinstance(i._Content__value, self.maClasseModeleMetier) : 
      #        print dir(i._Content__value)
      #        self.objPyxb = i._Content__value 
      #        setattr(self.perePyxb.objPyxb, self.nom, nvlObj)
      #        self.perePyxb.objPyxb.orderedContent()[indexOC]=self.perePyxb.objPyxb.orderedContent()[-1]
      #        del(self.perePyxb.objPyxb.orderedContent()[-1])
      #     indexOC+=1
      #PNPNPNPNPNPNPNPNP

class X_MCCOMPO(X_OBJECT) :
# -------------------------
# 
   def buildObjPyxb(self,mc_list) :
      #print ('________________________________________________')
      #print ('X_MCCOMPO buildObjPyxb', self.nom, self, mc_list)
      if not self.cata or  not self.cata.modeleMetier : return

      self.listArg=[]
      for objAccas in mc_list :
        if objAccas.nature == 'MCBLOC' :
           self.exploreBLOC(objAccas)
        elif objAccas.nature == 'MCList' :
           for fils in objAccas : 
               fils.perePyxb=self
               self.listArg.append(fils.objPyxb)
        else :
           self.listArg.append(objAccas.objPyxb)
           objAccas.perePyxb=self
           print (objAccas.nom ,' a pour pere Pyxb', self, self.nom)

      self.monNomClasseModeleMetier='T_'+self.nom
      self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)
      if self.objPyxbDeConstruction != None :
        self.objPyxb = self.objPyxbDeConstruction
        self.objPyxbDeConstruction = None
        #print ('je passe dans le if pour ', self.nom, self.objPyxb, self)
      else :
        self.objPyxb=self.maClasseModeleMetier(*self.listArg)
      #print ('Fin __________ ', self.nom, self.objPyxb)
      #print ('X_MCCOMPO', self.nom, self.objPyxb)
      #print ('_______________________________________')

   def deletePyxbObject(self):
      if not self.cata or  not self.cata.modeleMetier : return
      print ('******************************************')
      print ('je passe ds deletePyxbObject pour ', self, self.nom)
      print (self.perePyxb)
      print (dir(self)) 
      print ('******************************************')

   def exploreBLOC(self,objAccas):
      if not self.cata or  not self.cata.modeleMetier : return
      laListeSsLesBlocs=[]
      for fils in objAccas.mcListe:
        if fils.nature == 'MCBLOC' :
           self.exploreBLOC(fils)
        elif fils.nature == 'MCList' :
           for objFils in fils : 
               fils.perePyxb=self
               self.listArg.append(fils.objPyxb)
               #print (fils.nom ,' a pour pere Pyxb', self, self.nom)
        else :
           self.listArg.append(fils.objPyxb)
           fils.perePyxb=self
           #print (fils.nom ,' a pour pere Pyxb', self, self.nom)
          
   

  
class X_MCBLOC (X_MCCOMPO):
# --------------------------
   def buildObjPyxb(self,mc_list):
      if not self.cata or  not self.cata.modeleMetier : return
      # mise a none ? le bloc n a pas d existence en pyxb
      self.perePyxb=None
      #print ('_______________________________________')
      #print ('X_MCBLOC buildObjPyxb', self.nom, self, mc_list)
      # on rattache ses fils au bloc mais leur pere sera ensuite le MCCOMPO qui contient le bloc 
      # Pas sur d en avoir besoin du filsPyxb
      self.filsPyxb=[]
      self.objPyxb=None
      for objAccas in mc_list :
         self.filsPyxb.append(objAccas.objPyxb)
      #print (self.filsPyxb)
      #print ('Fin ', self.nom, self.objPyxb)
      #print ('_______________________________________')

        
       

class X_MCLIST (X_MCCOMPO):
# --------------------------
 
   def buildObjPyxb(self,mc_list):
      #print ('__________________________________________________________________')
      #print ('X_MCLIST buildObjPyxb traite ds X_MCLIST', self.nom, self)
      #print ('on ne fait rien pour les MCLISTs, cela sera fait dans chaque MCFACT')
      #print ('__________________________________________________________________')
      pass


class X_MCFACT (X_MCCOMPO):
# -------------------------
# on gere  au niveau du MCCOMPO
      pass


class X_JDC (X_MCCOMPO):
# ---------------------
 
   def  __init__(self):
      #print ('_______________________________________')
      #print ('X_JDC buildObjPyxb',  self)
      if not self.cata or  not self.cata.modeleMetier : return
      self.monNomClasseModeleMetier=self.code
      self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)
      self.objPyxb=self.maClasseModeleMetier()
      pyxb.GlobalValidationConfig._setContentInfluencesGeneration(pyxb.GlobalValidationConfig.ALWAYS)
      pyxb.GlobalValidationConfig._setInvalidElementInContent(pyxb.GlobalValidationConfig.RAISE_EXCEPTION)
      pyxb.GlobalValidationConfig._setOrphanElementInContent(pyxb.GlobalValidationConfig.RAISE_EXCEPTION)
      #print ('fin buildObjPyxb _______________________________________')

   def enregistreEtapePyxb(self,etape):
     # OK seulement si sequence (choice ? ...)
      if not self.cata or  not self.cata.modeleMetier : return
      print ('enregistreEtapePyxb' , etape)
      self.objPyxb.append(etape.objPyxb)
      etape.perePyxb = self
      #self.toXml()

   def toXml(self):
      if not self.cata or  not self.cata.modeleMetier : return
      print ('***************',self.objPyxb,'***************',)
      print ('***************',self.objPyxb.orderedContent(),'***************',)
      print(self.objPyxb.toDOM().toprettyxml())
      print(self.objPyxb.toxml())
      return (self.objPyxb.toDOM().toprettyxml())
        

   def analyseFromXML(self):
      print ("je suis ds analyseFromXML -- > appel ds analyse de I_JDC.py")
      if not self.cata or  not self.cata.modeleMetier : return
      if self.procedure == "" : return
      self.objPyxb=self.cata.modeleMetier.CreateFromDocument(self.procedure)
      for objEtape in self.objPyxb.content():
          objEtape.dictArgs= (self.pyxbToDict(objEtape))
          objEtape.monNomClasseAccas=objEtape._ExpandedName.localName()
          objEtape.monNomClasseAccas=objEtape.monNomClasseAccas[2:]
          objEtape.dictPyxb['objEnPyxb']=objEtape
          objEtape.dictArgs['dicoPyxbDeConstruction']=objEtape.dictPyxb
          maClasseAccas=getattr(self.cata,objEtape.monNomClasseAccas)
          objAccasEtape=maClasseAccas(**(objEtape.dictArgs))
          # attention objAccasEtape = None normal (cf buildSd)
 
          #print ( 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
          #print (objEtape , type(objEtape))
          #print (objEtape.dictPyxb)
          #print (maClasseAccas)
          #print (objAccasEtape)
 
          #print (objEtape.monNomClasseAccas, type(objEtape.monNomClasseAccas))
          #print (objEtape._ExpandedName, type(objEtape._ExpandedName))
          #print (objEtape.dictPyxb[u'experience'])
          #print (objEtape.dictArgs)
          #print (objEtape.dictPyxb)
          #print ( 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
          #exit()
      

   def pyxbToDict(self,objAAnalyser):
    # la transformation de l objAAnalyser en type lu par eficas ne fonctionne pas pour tout
    # faudrait - il travailler sur les types des objets ?
    # c est a revoir -> fonction cast a prevoir ds les 2 sens
    if not self.cata or  not self.cata.modeleMetier : return
    if objAAnalyser is None: return
    #print ('debut pour ',objAAnalyser)
    dictArgs = {}
    if isinstance(objAAnalyser, pyxb.binding.basis.simpleTypeDefinition): 
       objAAnalyser.dictPyxb=objAAnalyser
       #print (objAAnalyser.dictPyxb , type(objAAnalyser.dictPyxb))
       if isinstance(objAAnalyser, pyxb.binding.basis.enumeration_mixin):    return str(objAAnalyser)
       if isinstance(objAAnalyser, types.StringTypes):  return str(objAAnalyser)
       if isinstance(objAAnalyser, types.FloatType):  return float(objAAnalyser)
       if isinstance(objAAnalyser, (types.IntType, types.LongType)):  return int(objAAnalyser)
       #if isinstance(objAAnalyser, (types.NoneType, types.BooleanType, types.FloatType, types.IntType, types.LongType)):
       return repr(objAAnalyser)
       # ou ? return objAAnalyser
       #if isinstance(objAAnalyser, types.StringTypes): return pyxb.utils.utility.QuotedEscaped(objAAnalyser,)
       #pour une enum getattr(value dans le type)
       # return pythonLiteral(ReferenceFacet(facet=value, **kw))
    objAAnalyser.dictPyxb = {} 
    for expandedName, elementDeclaration in objAAnalyser._ElementMap.items():
        objPyxbName  = expandedName.localName()
        objPyxbValue = getattr(objAAnalyser, objPyxbName)
        if objPyxbValue == None or objPyxbValue == [] : continue
        if elementDeclaration.isPlural():
            dictArgs[objPyxbName] = []
            #objAAnalyser.dictPyxb[objPyxbName]={} 
            objAAnalyser.dictPyxb[objPyxbName]=[] 
            #objAAnalyser.dictPyxb['objEnPyxb']=objAAnalyser
            for objPyxb in objPyxbValue : 
                #print ('-------------',objPyxb)
                dictArgs[objPyxbName].append(self.pyxbToDict(objPyxb))
                objPyxb.dictPyxb['objEnPyxb'] = objPyxb
                objAAnalyser.dictPyxb[objPyxbName].append(objPyxb.dictPyxb)
        else:
            dictArgs[objPyxbName] = self.pyxbToDict(getattr(objAAnalyser, objPyxbName))
            #print ('ajout ds dico de ', objAAnalyser , 'de',  objPyxbName, objPyxbValue)
            objAAnalyser.dictPyxb[objPyxbName] = objPyxbValue.dictPyxb
            #print ('ajout ds dico de ', objPyxbValue.dictPyxb, 'de',  objPyxbName)
            objAAnalyser.dictPyxb['objEnPyxb']=objAAnalyser
    #print ("***********************************")
    #print ('pyxbToDict  fin pour ********** ', objAAnalyser)
    #print ('pyxbToDict ', objAAnalyser, objAAnalyser.dictPyxb)
    #print ('pyxbToDict  fin pour ********** ', objAAnalyser)
    #print ("***********************************")
    #print (dictArgs)
    #print (dictPyxb)
    #for i in dictArgs.keys(): print (i, " ", dictArgs[i], " ", type(dictArgs[i]))
    #print ('fin pour ',objAAnalyser)
    return dictArgs

   
  

if __name__ == "__main__":
   print ('a faire')
