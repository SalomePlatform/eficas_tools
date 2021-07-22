#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2007-2021   EDF R&D
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

import sys,os
import inspect
import traceback
def trace():
    traceback.print_stack()
#import raw.efficas as efficas
import types

sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),'..')))

try :
    import pyxb
    import pyxb.binding
    import pyxb.binding.basis
    #import pyxb.utils.utility
    #import pyxb.utils.domutils
except : pass

from Accas import A_ASSD

class X_OBJECT:
# -------------

    def delObjPyxb(self, debug=False):
        if not self.cata or not self.cata.modeleMetier : return
        if self.nom == 'Consigne' : return None
        trouve = False

        if debug : print ('--------------- in delObjPyxb pour ' , self.nom)
        if debug : print (self.perePyxb.objPyxb.orderedContent())
        if debug : print (list(map(lambda o:o.value, self.perePyxb.objPyxb.orderedContent())))

        elt=pyxb.binding.basis.ElementContent(self.objPyxb, instance=self.perePyxb.objPyxb, tag=pyxb.namespace.ExpandedName(self.cata.modeleMetier.Namespace, self.nom))
        if debug : print ('element moi = ', elt, 'id de moi = ', id(self.objPyxb), self.objPyxb)
        if (elt.elementDeclaration.isPlural()):
            if debug : print ('je suis Plural')
        #   monIndexInOrderedContent=0
        #   for c in self.perePyxb.objPyxb.orderedContent():
        #     if isinstance(c._Content__value,list) and  isinstance(c._Content__value[0], type(self.objPyxb)): monIndexInOrderedContent += 1
        #   listeObjetsAccas=self.parent.getChild(self.nom,restreint='oui')
        #   if len(listeObjetsAccas) == 1 : monIndex=0
        #   else : monIndex=listeObjetsAccas.index(self)
        #   listeObjetsPyxb=getattr(self.perePyxb.objPyxb,elt.elementDeclaration._ElementDeclaration__key)
        #   listeObjetsPyxb.pop(monIndex)
        #   self.perePyxb.objPyxb.orderedContent().pop(monIndexInOrderedContent)
            for c in self.perePyxb.objPyxb.orderedContent():
                trouve=False
                if isinstance(c._Content__value,list) and  isinstance(c._Content__value[0],type(self.objPyxb)):
                    monIndex=c.value.index(self.objPyxb)
                    trouve = True
                if trouve : break
            if not trouve : print ("************ pas trouve au delete"); return
            listeObjetsPyxb=getattr(self.perePyxb.objPyxb,elt.elementDeclaration._ElementDeclaration__key)
            listeObjetsPyxb.pop(monIndex)
            # si dernier ?
        else :
            newOrderedContent = []
            for i in self.perePyxb.objPyxb.orderedContent():
                if id(self.objPyxb) == id(i._Content__value) : trouve = True ;continue
                newOrderedContent.append(i)
            if not trouve : print ('elt a supprimer ', self.nom, 'non trouve')
            for i in range(len(newOrderedContent)):
                self.perePyxb.objPyxb.orderedContent()[i]=newOrderedContent[i]
            self.perePyxb.objPyxb.orderedContent().pop(len(newOrderedContent))

            setattr(self.perePyxb.objPyxb,elt.elementDeclaration._ElementDeclaration__key,None)
            if debug : print (list(map(lambda o:o.value, self.perePyxb.objPyxb.orderedContent())))



    def addObjPyxb(self,indiceDsLeContenu,debug=False):
        if not self.cata or not self.cata.modeleMetier : return
        if debug :print ('_____________ addObjPyxb ds X_OBJECT', self.nom, indiceDsLeContenu)
        # adherence Accas sur le parent
        parent=self.parent
        while (parent.isBLOC()):
            if parent != self.parent : indiceDsLeContenu += parent.rangDsPyxb()
            parent=parent.parent
        self.perePyxb=parent

        if debug :print ('indiceDsLeContenu',indiceDsLeContenu)
        if debug :print (pyxb.namespace.ExpandedName(self.cata.modeleMetier.Namespace, self.nom))

        #if self.objPyxb ! = None : self.objPyxb.objAccas=self
        elt=pyxb.binding.basis.ElementContent(self.objPyxb, instance=self.perePyxb.objPyxb, tag=pyxb.namespace.ExpandedName(self.cata.modeleMetier.Namespace, self.nom))
        self.perePyxb.objPyxb.orderedContent().insert(indiceDsLeContenu,elt)
        if (elt.elementDeclaration.isPlural()):
        # je suis donc un MCList
            listeObjetsAccas=self.parent.getChild(self.nom,restreint='oui')
            if len(listeObjetsAccas) == 1 : monIndex=1
            else : monIndex=listeObjetsAccas.index(self)
            listeObjetsPyxb=getattr(self.perePyxb.objPyxb,elt.elementDeclaration._ElementDeclaration__key)
            listeObjetsPyxb.insert(monIndex,self.objPyxb)
        else :
            setattr(self.perePyxb.objPyxb,elt.elementDeclaration._ElementDeclaration__key,self.objPyxb)
        if debug : print (list(map(lambda o:o.value, self.perePyxb.objPyxb.orderedContent())))
        if debug : print ('fin _____________ addObjPyxb ds X_OBJECT', self.nom, indiceDsLeContenu)


    def rangDsPyxb(self):
        monRangEnAccas=self.parent.mcListe.index(self)
        rangEnPyxb=0
        for frere in self.parent.mcListe[0: monRangEnAccas] :
            rangEnPyxb += frere.longueurDsArbre()
        return rangEnPyxb


class X_MCSIMP(X_OBJECT):
# -----------------------

    def buildObjPyxb(self, debug=True) :
        if not self.cata or not self.cata.modeleMetier : return
        if self.nom == 'Consigne' : return None
        if debug : print (self.definition.nomComplet())
        if debug : print ('_______________ X_MCSIMP buildObjPyxb', self.nom, self,self.valeur)
        if debug and self.objPyxbDeConstruction == None : print (self.nom, ' pas de pyxb')
        elif debug : print ('objPyxbDeConstruction', self.objPyxbDeConstruction)

        if self.objPyxbDeConstruction != None :
            self.objPyxb = self.objPyxbDeConstruction
            self.maClasseModeleMetier =type(self.objPyxb)
            self.objPyxbDeConstruction = None
            if issubclass(self.maClasseModeleMetier, self.cata.modeleMetier.pyxb.binding.basis.STD_union):
                self.needFactory=True
                self.maClasseModeleMetierFactory=getattr(self.maClasseModeleMetier,'Factory')
            else : self.needFactory=False
        else :
            self.monNomClasseModeleMetier ='T_'+self.nom
            if hasattr(self.definition,'nomXML') and self.definition.nomXML != None : self.monNomClasseModeleMetier='T_'+self.definition.nomXML
            if self.monNomClasseModeleMetier in list(self.cata.DicoNomTypeDifferentNomElt.keys()) :
                nomComplet=self.definition.nomComplet()
                if nomComplet in list(self.cata.DicoNomTypeDifferentNomElt[self.monNomClasseModeleMetier].keys()):
                    self.monNomClasseModeleMetier=self.cata.DicoNomTypeDifferentNomElt[self.monNomClasseModeleMetier][nomComplet]
            if debug : print ('Pour', self.nom, ' le type est ', self.monNomClasseModeleMetier)
            self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)

            if self.waitMatrice() :
               #PNPN : Attention rien ne relie les objets listeObjPyxb a un objAccas
               # 27/04 je ne sais pas si cela posera pb
               self.listeLines = []
               self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)
               self.maClasseModeleMetier_line=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier+'_line')
               if debug : print ('Matrice  de type ', self.maClasseModeleMetier)
               for v in self.valeur: 
                   l=self.maClasseModeleMetier_line(v)
                   self.listeLines.append(l)
               self.objPyxb=self.maClasseModeleMetier(*self.listeLines)
               #if self.objPyxb !=None : self.objPyxb.objAccas=self
               if debug : print ('Matrice ', self.nom, self.objPyxb)
               return
            if self.waitTuple() :
               self.objPyxb = []
               self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)
               # if faut traiter l autre cas
               # et optimiser
               if self.definition.max !=1 :
                  for v in self.valeur :
                    if debug : print ('je traite ', v)
                    listeConstruction=[]
                    for i in range(self.combienEltDsTuple()):
                        num=i+1
                        maClasseElt=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier+'_n'+str(num))
                        listeConstruction.append(maClasseElt(v[i]))
                    self.objPyxb.append(self.maClasseModeleMetier(*listeConstruction))
                    if debug  : print (self.objPyxb)
                  return
            if self.waitChaineAvecBlancs() and self.definition.max > 1:
               self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)
               if debug : print (self.valeur)
               if self.valeur != None and self.valeur != [] : self.objPyxb = self.maClasseModeleMetier(*self.valeur)
               else :self.objPyxb = self.maClasseModeleMetier()
               if debug : print ('X_MCSIMP', self.nom, self.objPyxb, )
               if debug : print ('__________ fin X_MCSIMP', self.objPyxb, self.nom, self, self.maClasseModeleMetier,self.valeur)
               return

                        
            if issubclass(self.maClasseModeleMetier, self.cata.modeleMetier.pyxb.binding.basis.STD_union):
                if debug : print ('needFactory')
                self.needFactory=True
                self.maClasseModeleMetierFactory=getattr(self.maClasseModeleMetier,'Factory')
            else : self.needFactory=False

            if self.valeur != None :
                if self.needFactory :
                    if self.definition.max > 1 :
                       # PNPN A corriger 
                       # self.objPyxb=self.maClasseModeleMetier(self.valeur)
                            self.objPyxb=self.maClasseModeleMetierFactory(self.valeur)
                    else :  self.objPyxb=self.maClasseModeleMetierFactory(self.valeur)
                else                :  self.objPyxb=self.maClasseModeleMetier(self.valeur)
            else                   :
                if self.needFactory : self.objPyxb=None
                else                : self.objPyxb=self.maClasseModeleMetier(_validate_constraints=False)


            #if self.objPyxb !=None : self.objPyxb.objAccas=self
        if debug : print ('X_MCSIMP', self.nom, self.objPyxb, )
        if debug : print ('__________ fin X_MCSIMP', self.objPyxb, self.nom, self, self.maClasseModeleMetier,self.valeur)


    def setValeurObjPyxb(self,newVal, debug=True):
        if not self.cata or not self.cata.modeleMetier : return
        if debug : print (' ___________________________ dans setValeurObjPyxb MCSIMP ', self.nom, newVal)
        if debug : print (' self.perePyxb = ', self.perePyxb.nom)
        if debug : print (self.nom , ' a pour pere', self.perePyxb, self.perePyxb.nom, self.perePyxb.objPyxb)
        if debug : print ('debut du setValeurObjPyxb pour ', self.nom, self.perePyxb.objPyxb.orderedContent())

        #if newVal != None : nvlObj=self.maClasseModeleMetier(newVal)
        if newVal != None :
            if self.needFactory : nvlObj=self.maClasseModeleMetierFactory(newVal)
            else                : nvlObj=self.maClasseModeleMetier(newVal)
        else                   :
            if self.needFactory : nvlObj =None
            else                : nvlObj=self.maClasseModeleMetier(_validate_constraints=False)
        self.val=newVal
        if debug : print ('fin du setValeurObjPyxb pour ', self.nom, self.perePyxb.objPyxb.orderedContent())

        if inspect.isclass(newVal) and issubclass(newVal,A_ASSD)  :
            newVal = newVal.nom
        setattr(self.perePyxb.objPyxb,self.nom,nvlObj)
        trouve=False
        indice=0
        for i in self.perePyxb.objPyxb.orderedContent():
            if i.elementDeclaration.id() == self.nom:
            #if isinstance(i._Content__value, self.maClasseModeleMetier) :
                self.perePyxb.objPyxb.orderedContent()[indice]=self.perePyxb.objPyxb.orderedContent()[-1]
                del(self.perePyxb.objPyxb.orderedContent()[-1])
                trouve=True
                break
            indice+=1
        if not trouve : print ('Attention souci au changement de valeur de ', self.nom)
        self.objPyxb=nvlObj
        #self.objPyxb.objAccas=self
        if debug : print ('fin du setValeurObjPyxb pour ', self.nom, self.perePyxb.objPyxb.orderedContent())




class X_MCCOMPO(X_OBJECT) :
# -------------------------
#
    def buildObjPyxb(self,mc_list, debug=False) :
        if not self.cata or not self.cata.modeleMetier : return

        #if self.nom == 'Scenario_data' : debug=1
        if debug : print ('X_MCCOMPO', self.nom)
        deepDebug=False
        self.listArg=[]
        self.dicoArg={}
        for objAccas in mc_list :
            if objAccas.nature == 'MCBLOC' :
                self.exploreBLOC(objAccas)
            elif objAccas.nature == 'MCList' :
                if objAccas[0].definition.max > 1 :
                    self.listArg.append(objAccas) # les MCList n ont pas objPyxb
                    self.dicoArg[objAccas.nom]=[]
                    for fils in objAccas :
                        fils.perePyxb=self
                        self.dicoArg[objAccas.nom].append(fils.objPyxb)
                else :
                    objAccas[0].perePyxb=self
                    self.dicoArg[objAccas.nom]=objAccas[0].objPyxb
                    self.listArg.append(objAccas[0].objPyxb)
            else :
                if objAccas.nom == 'Consigne'     : continue
                print ('______________', objAccas.nom, objAccas.objPyxb)
                self.listArg.append(objAccas.objPyxb)
                self.dicoArg[objAccas.nom]=objAccas.objPyxb
                objAccas.perePyxb=self

        if debug : print('X_MCCOMPO -- listArg ---',self.nom,self.listArg)
        if debug : print('X_MCCOMPO -- dicoArg ---',self.nom,self.dicoArg)


        self.monNomClasseModeleMetier='T_'+self.nom
        if self.monNomClasseModeleMetier in list(self.cata.DicoNomTypeDifferentNomElt.keys()) :
            self.nomComplet=self.definition.nomComplet()
            self.monNomClasseModeleMetier=self.cata.DicoNomTypeDifferentNomElt[self.monNomClasseModeleMetier][self.nomComplet]
        self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)

        # PN : Ne doit-on pas tester avant
        if self.objPyxbDeConstruction != None :
            self.objPyxb = self.objPyxbDeConstruction
            self.objPyxbDeConstruction = None
            if debug : print ('je passe dans le if pour ', self.nom, self.objPyxb, self)
            if debug : print ('X_MCCOMPO', self, self.nom, self.objPyxb,self.listArg,self.objPyxb.orderedContent())
        else :
            if debug : print (self.listArg)
            if debug : print (self.maClasseModeleMetier)
            # self.objPyxb=self.maClasseModeleMetier(*self.listArg)
            self.objPyxb=self.maClasseModeleMetier(**self.dicoArg)
            if deepDebug :
                print ('debut de __________ new ordered content')
                for o in self.objPyxb.orderedContent():
                    print ('o', o)
                    print ('value', o.value)
                    print ('type', type(o.value))
                    print ('id', id(o.value))
                print ('fin __________ new ordered content')
                print ('debut de  __________ listArg')
                for obj in self.listArg:
                    print ('obj',obj)
                    print ('type obj', type(obj))
                    print ('id(obj)', id(obj))
                print ('fin __________  listArg')

            newOrderedContent=[]
            if debug  : print ('list Arg')
            for obj in self.listArg:
                if debug :
                    print ('obj',obj)
                    print ('type obj', type(obj))
                    print ('id(obj)', id(obj))

                # on teste le caractere pluriel
                if  isinstance(obj, list):
                    for c in self.objPyxb.orderedContent() :
                        if hasattr (c,'value') and c.value == obj :
                           newOrderedContent.append(c)
                    continue
                if (hasattr(obj, 'nature')) : # attention on a un object Accas et non un pyxb car les MCList n ont pas de objPyxb
                    max=obj[0].definition.max
                else : max = 1
                if  max == 1 :
                    #if not(issubclass(type(obj), pyxb.binding.basis.enumeration_mixin) ):
                    #   newOrderedContent.append(self.objPyxb.orderedContent()[list(map(lambda o:id(o.value), self.objPyxb.orderedContent())).index(id(obj))] )
                    #else :
                    #   newOrderedContent.append(self.objPyxb.orderedContent()[list(map(lambda o:type(o.value), self.objPyxb.orderedContent())).index(type(obj))] )
                    # PN 22 sept 2020 . pourquoi pas toujours l id. le tyoe ne convient pas en cas d union d enum
                    newOrderedContent.append(self.objPyxb.orderedContent()[list(map(lambda o:id(o.value), self.objPyxb.orderedContent())).index(id(obj))] )
                else  : # element Pural
                    for c in self.objPyxb.orderedContent() :
                        if isinstance(c._Content__value,list) and  isinstance(c._Content__value[0], type(obj[0].objPyxb)): newOrderedContent.append(c)

            for i in range(len(self.listArg)):
                self.objPyxb.orderedContent()[i]=newOrderedContent[i]
            debug=True
            if debug : print ('X_MCCOMPO', self, self.nom, self.objPyxb)
            if debug : print ('X_MCCOMPO', self.listArg)
            if debug : print ('X_MCCOMPO', newOrderedContent)
            if debug : print ( 'X_MCCOMPO',self.objPyxb.orderedContent())
        if debug : print ('fin buildObjetPyxb _______________________________________')
        # assert(self.objPyxb.validateBinding())


    def exploreBLOC(self,objAccas,debug=False):
        if debug : print (' ds exploreBLOC', objAccas.nom)
        laListeSsLesBlocs=[]
        for fils in objAccas.mcListe:
            if fils.nature == 'MCBLOC' :
                self.exploreBLOC(fils)
            elif fils.nature == 'MCList' :
                #print ('exploreBLOC des MCList', fils.nom)
                self.dicoArg[fils.nom]=[]
                if fils[0].definition.max > 1 :
                    #print ('ajout de ', fils)
                    self.listArg.append(fils) # les MCList n ont pas objPyxb
                    for objFils in fils :
                        objFils.perePyxb=self
                        self.dicoArg[fils.nom].append(objFils.objPyxb)
                else:
                    fils[0].perePyxb=self
                    self.dicoArg[fils.nom]=fils[0].objPyxb
                    self.listArg.append(fils[0].objPyxb)
            else :
                if fils.nom == "Consigne" : continue
                self.listArg.append(fils.objPyxb)
                self.dicoArg[fils.nom]=fils.objPyxb
                fils.perePyxb=self
                if debug : print (fils.nom ,' est un SIMP a pour pere Pyxb', self, self.nom)
        if debug : print ('fin  ds exploreBLOC', objAccas .nom)




class X_MCBLOC (X_MCCOMPO):
# --------------------------
    def buildObjPyxb(self,mc_list,debug=False):
        if not self.cata or not self.cata.modeleMetier : return
        if debug : print ('X_MCBLOC buildObjPyxb', self.nom, self, mc_list, 'ne fait rien')
        self.perePyxb=None
        self.objPyxb=None

    def addObjPyxb(self, indiceDsLeContenu, debug=False):
        if not self.cata or not self.cata.modeleMetier : return
        if debug : print ('X_MCBLOC addObjPyxb', self.nom, self, self.mcListe, indiceDsLeContenu)
        rangDeLObjet=indiceDsLeContenu
        for obj in self.mcListe:
            obj.addObjPyxb( rangDeLObjet)
            rangDeLObjet=rangDeLObjet+obj.longueurDsArbre()

    def delObjPyxb(self, debug=False):
        if not self.cata or not self.cata.modeleMetier : return
        if debug : print ('X_MCBLOC delObjPyxb', self.nom, ' --------------------------')
        for obj in self.mcListe:
            obj.delObjPyxb()
        if debug : print ('fin X_MCBLOC delObjPyxb --------------------------')

class X_MCLIST (X_MCCOMPO):
# --------------------------

    def buildObjPyxb(self,mc_list, debug=False):
        if debug : print ('X_MCLIST buildObjPyxb ne fait rien', self.nom, self, mc_list)
        pass

    def addObjPyxb(self,indiceDsLeContenu, debug=False):
        if debug : print ('X_MCLIST addObjPyxb', self.nom, indiceDsLeContenu)
        rangDeLObjet=indiceDsLeContenu
        for objFils in self :
            objFils.addObjPyxb(rangDeLObjet)
            rangDeLObjet= rangDeLObjet + 1

    def delObjPyxb(self, debug=False):
        if not self.cata or not self.cata.modeleMetier : return
        if debug : print ('X_MCLIST delObjPyxb', self.nom, ' --------------------------')
        for obj in self:
            obj.delObjPyxb()
        if debug : print ('fin X_MCLIST delObjPyxb --------------------------')


class X_MCFACT (X_MCCOMPO):
# -------------------------
    pass

class X_ETAPE(X_MCCOMPO) :
# -------------------------

    def metAJourNomASSD(self, nom,debug=False):
        if not self.cata or not self.cata.modeleMetier : return
        if debug : print ('X_ETAPE metAJourLesAttributs', self.nom, nom,' --------------------------')
        self.objPyxb.sdName=nom

class X_JDC (X_MCCOMPO):
# ---------------------

    def  __init__(self):
        self.perePyxb=None
        if not self.cata or not self.cata.modeleMetier : return
        #if hasattr(self.cata,'DicoNomTypeDifferentNomElt') : print ('jkllllllllllllllll')
        if not(hasattr(self.cata,'DicoNomTypeDifferentNomElt')) : self.cata.DicoNomTypeDifferentNomElt={}
        self.monNomClasseModeleMetier=self.code
        self.maClasseModeleMetier=getattr(self.cata.modeleMetier,self.monNomClasseModeleMetier)
        self.objPyxb=self.maClasseModeleMetier()
        #self.objPyxb.objAccas=self
        pyxb.GlobalValidationConfig._setContentInfluencesGeneration(pyxb.GlobalValidationConfig.NEVER)
        pyxb.GlobalValidationConfig._setInvalidElementInContent(pyxb.GlobalValidationConfig.RAISE_EXCEPTION)
        pyxb.GlobalValidationConfig._setOrphanElementInContent(pyxb.GlobalValidationConfig.RAISE_EXCEPTION)



    def enregistreEtapePyxb(self,etape,indice=0):
      # ne fonctionne pas : a reecrire avec les fonctions addObjPyxb et ReconstruitPerePyxb
      # ne contient pas indice pour l insant
      # print ( 'hhhhhhhhhhhhhhh enregistreEtapePyxb hhhhhhhhhhhhhhhhhhhhhhhhh')
      # print ('enregistre ds ',self, etape.nom, 'indice = ', indice)
        if not self.cata.modeleMetier : return
        self.objPyxb.append(etape.objPyxb)
        etape.perePyxb = self

        #print (self.objPyxb.orderedContent())
        #if indice   != (len(self.objPyxb.orderedContent()) ) :
        #  tampon=self.objPyxb.orderedContent()[-1]
        #  for i in reversed(range(len(self.objPyxb.orderedContent()))):
        #    self.objPyxb.orderedContent()[i]=self.objPyxb.orderedContent()[i-1]
        #    if i == indice + 1 : break
        #  self.objPyxb.orderedContent()[indice]=tampon

        #print (self.objPyxb.orderedContent())
        #try:
        #   self.objPyxb.validateBinding()
        #except pyxb.ValidationError as e:
        #   print(e.details())

    def toXml(self,fichier=None, debug=False):
        if debug : print ('ds to XML')
        if not self.cata or not self.cata.modeleMetier : return
        if debug : print (' to xml ***************',self.objPyxb,'***************',)
        if debug : print (' to xml ***************',self,'***************',)
        if debug : print (' to xml ***************',self.objPyxb.orderedContent(),'***************',)
        if debug : print(self.objPyxb.toDOM().toprettyxml())
        if debug : print(self.objPyxb.toxml())
        return (self.objPyxb.toDOM().toprettyxml())


    def analyseFromXML(self,debug=False):
        print ("je suis ds analyseFromXML -- > appel ds analyseXML de I_JDC.py")
        if self.procedure == "" : return
        self.objPyxb=self.cata.modeleMetier.CreateFromDocument(self.procedure)
        if not hasattr(self.cata.modeleMetier,'AccasUserAssd'):
            from Accas import UserASSD
            self.cata.modeleMetier.AccasUserAssd=UserASSD
        for contentObjEtape in self.objPyxb.orderedContent():
            objEtape=contentObjEtape.value
            objEtape.dictArgs=(self.pyxbToDict(objEtape))
            objEtape.monNomClasseAccas=objEtape._ExpandedName.localName()
            objEtape.monNomClasseAccas=objEtape.monNomClasseAccas[2:]
            # doute sur les 2 lignes suivantes : objEtape peut etre contentObjEtape 2juin20
            objEtape.dictPyxb['objEnPyxb']=objEtape
            objEtape.dictArgs['dicoPyxbDeConstruction']=objEtape.dictPyxb
            if debug : print ('dicoPyxbDeConstruction', objEtape.dictArgs['dicoPyxbDeConstruction'])
            maClasseAccas=getattr(self.cata,objEtape.monNomClasseAccas)
            if debug : print ( 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
            if debug : print ('maClasseAccas ', maClasseAccas)
            if debug : print ('objEtape ', objEtape , type(objEtape))
            if debug : print ('nomClasseAccas ',objEtape.monNomClasseAccas, type(objEtape.monNomClasseAccas))
            if debug : print ('_ExpandedName ', objEtape._ExpandedName, type(objEtape._ExpandedName))
            if debug : print ('dictArgs ',objEtape.dictArgs)
            if debug : print ('dictPyxb ',objEtape.dictPyxb)
            # attention au call d Oper qui renomme l objet pyxb
            if hasattr(objEtape,'sdName') :
                if debug and hasattr(objEtape,'sdName') :print ('sdName',objEtape.sdName)
                objAccasEtape=maClasseAccas(nomXML=objEtape.sdName, **(objEtape.dictArgs))
            else : objAccasEtape=maClasseAccas(**(objEtape.dictArgs))
            if debug : print ( 'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')


    def pyxbToDict(self,objAAnalyser, debug=True):
        # la transformation de l objAAnalyser en type lu par eficas ne fonctionne pas pour tout
        if objAAnalyser is None: return
        if debug : print ('debut pour_____________________________ ',objAAnalyser)
        dictArgs = {}
        # traitement SIMP
        # ---------------
        # a revoir pour les matrices
        # et les tuples
        debug = 1
        if isinstance(objAAnalyser, pyxb.binding.basis.simpleTypeDefinition):
            if debug : print ('je suis un MCSimple', objAAnalyser)
            # traitement scalaire
            objAAnalyser.dictPyxb=objAAnalyser
            if not (isinstance(objAAnalyser,pyxb.binding.basis.STD_list)):
                if debug :  print ('je suis un scalaire')
                if isinstance(objAAnalyser,self.cata.modeleMetier.AccasUserAssd) or isinstance(objAAnalyser,self.cata.modeleMetier.AccasUserAssdMultiple):
                    if debug : print ('je suis un UserASSD')
                    laClassePyxbUserAssd=type(objAAnalyser)
                    return self.creeUserAssd(objAAnalyser,laClassePyxbUserAssd)
                if isinstance(objAAnalyser, pyxb.binding.datatypes.boolean) : return bool(objAAnalyser)
                if isinstance(objAAnalyser, str)  : return str(objAAnalyser)
                if isinstance(objAAnalyser, int)  : return int(objAAnalyser)
                if isinstance(objAAnalyser, float): return float(objAAnalyser)
                if isinstance(objAAnalyser, pyxb.binding.basis.enumeration_mixin):    return str(objAAnalyser)
                return objAAnalyser
            else :
                if debug : print ('je suis une liste')
                laListe=[]
                # liste homogene
                if len(objAAnalyser)>0:
                    if issubclass(objAAnalyser[0].__class__,self.cata.modeleMetier.AccasUserAssd) or issubclass(objAAnalyser[0].__class__,self.cata.modeleMetier.AccasUserAssdMultiple): estUnUserASSDorUserASSDMultiple = True
                    else : estUnUserASSDorUserASSDMultiple=False
                else : estUnUserASSDorUserASSDMultiple=False
                if debug : print ('estUnUserASSDorUserASSDMultiple', estUnUserASSDorUserASSDMultiple)
                for obj in objAAnalyser :
                    if estUnUserASSDorUserASSDMultiple:
                       laClassePyxbUserAssd=obj.__class__
                       laListe.append(self.creeUserAssd(obj,laClassePyxbUserAssd))
                    elif isinstance(obj, str): laListe.append (str(obj))
                    elif isinstance(obj, int): laListe.append (int(obj))
                    elif isinstance(obj, float): laListe.append (float(obj))
                    elif isinstance(obj, pyxb.binding.basis.enumeration_mixin): laListe.append(str(obj))
                    else :  laListe.append(obj)
                return (laListe)
            #  if debug : print ('je suis Plural')
            # ou ? return objAAnalyser
            #if isinstance(objAAnalyser, types.StringTypes): return pyxb.utils.utility.QuotedEscaped(objAAnalyser,)
            #pour une enum getattr(value dans le type)
            # return pythonLiteral(ReferenceFacet(facet=value, **kw))
        #print ('je suis un mot complexe')
        # traitement FACT ou BLOC
        # ------------------------
        # il faut traiter les fact multiples
        objAAnalyser.dictPyxb = {}
        objAAnalyser.dictPyxb['objEnPyxb']=objAAnalyser
        #for expandedName, elementDeclaration in objAAnalyser._ElementMap.items():
        #    objPyxbName  = expandedName.localName()
        #    objPyxbValue = getattr(objAAnalyser, objPyxbName)
        for objEltContentFils in objAAnalyser.orderedContent():
            objPyxbValue = objEltContentFils.value
            objPyxbName  = objEltContentFils.elementDeclaration.id()
            elementDeclaration = objEltContentFils.elementDeclaration
            #if objPyxbValue == None or objPyxbValue == [] : continue
            if elementDeclaration.isPlural():
                if objPyxbName not in list(dictArgs.keys()) : dictArgs[objPyxbName]=[]
                if objPyxbName not in list(objAAnalyser.dictPyxb.keys()) : objAAnalyser.dictPyxb[objPyxbName]=[]
                dictArgs[objPyxbName].append(self.pyxbToDict(objPyxbValue))
                objAAnalyser.dictPyxb[objPyxbName].append(objPyxbValue.dictPyxb)
            else:
                dictArgs[objPyxbName] = self.pyxbToDict(getattr(objAAnalyser, objPyxbName))
                objAAnalyser.dictPyxb[objPyxbName] = objPyxbValue.dictPyxb
                # print ('ajout dans dictPyxb', objPyxbName, objPyxbValue.dictPyxb)
                #print ('avec la valeur', 'de',  objAAnalyser.dictPyxb[objPyxbName])

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

    def creeUserAssd(self,objAAnalyser,laClassePyxbUserAssd,debug=True):

        enCreation=False
        if debug : print ('creeUserAssd ', objAAnalyser, ' ',laClassePyxbUserAssd)
        leTypeIntermediaire=laClassePyxbUserAssd.XsdSuperType()  
        if debug : print ('leTypeIntermediaire ', leTypeIntermediaire)
        if debug : print ('leTypeIntermediaire ', leTypeIntermediaire.XsdSuperType())
        if leTypeIntermediaire.__name__[-2:]== '_C' : enCreation = True
        elif leTypeIntermediaire.__name__[-2:] != '_U' : print ('pb avec', laClassePyxbUserAssd); return None #exit() 
        nomClasseAccasUserAssd=leTypeIntermediaire.XsdSuperType().__name__
        if debug : print ('nomClasseAccasUserAssd', nomClasseAccasUserAssd)
        laClasseAccas=getattr(self.cata,nomClasseAccasUserAssd)
        print (laClasseAccas)
        if not(enCreation):
            if str(objAAnalyser) in self.g_context.keys():return self.g_context[str(objAAnalyser)]
            else :
                obj=laClasseAccas()
                self.g_context[str(objAAnalyser)]=obj
                return obj
        if str(objAAnalyser) in self.g_context.keys():
            if isinstance(self.g_context[str(objAAnalyser)],laClasseAccas):
                return self.g_context[str(objAAnalyser)]
            else :
                nvlObj=laClasseAccas()
                oldObj=self.g_context[str(objAAnalyser)]
                nvlObj.transfere(oldObj)
                self.g_context[str(objAAnalyser)]=nvlObj
                return nvlObj
        else :
            obj=laClasseAccas()
            self.g_context[str(objAAnalyser)]=obj
            return obj

#   def analyseContent(self,objAAnalyser):
#       objAAnalyser.dictArgs={}
#       for objContenu in objAAnalyser.content():
#          #print ('j analyse ', objContenu)
#          objContenu.monNomClasseModeleMetier=str(objContenu.__class__).split('.')[-1]
#          objContenu.monNomClasseAccas=objContenu.monNomClasseModeleMetier[2:-2]
#          #maClasseAccas=classeAccasPere.entites[objContenu.monNomClasseAccas]
#          if objContenu._IsSimpleTypeContent():
#             print (objContenu.monNomClasseAccas,objContenu.pythonLiteral())
#             print (objContenu.monNomClasseAccas,objContenu.xsdLiteral())
#             #chaine=objContenu.pythonLiteral().split('(')[1].split(')')[0]
#             print (dir(objContenu))
#             objAAnalyser.dictArgs[objContenu.monNomClasseAccas]=None
#             #objAAnalyser.dictArgs[objContenu.monNomClasseAccas]=objContenu.pythonLiteral()
#          else :
#             self.analyseContent(objContenu)
#             objAAnalyser.dictArgs[objContenu.monNomClasseAccas]=objContenu.dictArgs
            #print ( '________________')
            #print (objAAnalyser.monNomClasseAccas)
            #for i in objAAnalyser.dictArgs : print (i, objAAnalyser.dictArgs[i])
            #print ( '________________')



if __name__ == "__main__":
    print ('a faire')
