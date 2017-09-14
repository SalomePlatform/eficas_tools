# -*- coding: utf-8 -*-
# Copyright (C) 2007-2017   EDF R&D
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
from __future__ import absolute_import
import six
_no=0

import Accas
def number_entite(entite):
   """
      Fonction qui attribue un numero unique a tous les objets du catalogue
      Ce numero permet de conserver l'ordre des objets
   """
   global _no
   _no=_no+1
   entite._no=_no

class ENTITE:
  def __init__(self):
     number_entite(self)
    
  def get_docu(self):
    if hasattr(self,'docu') :
      if self.docu != "" : return self.docu
      else:
        if hasattr(self,'pere'):
          return self.pere.get_docu()
        else:
          return None
    else:
      return None

  def get_sug(self):
    if hasattr(self,'sug') :
      if self.sug != "" : return self.sug
    return None

  def check_definition(self, parent):
      """Verifie la definition d'un objet composite (commande, fact, bloc)."""
      args = self.entites.copy()
      mcs = set()
      for nom, val in args.items():
         if val.label == 'SIMP':
            mcs.add(nom)
            #XXX
            #if val.max != 1 and val.type == 'TXM':
                #print "#CMD", parent, nom
         elif val.label == 'FACT':
            val.check_definition(parent)
            #PNPNPN surcharge
            # CALC_SPEC !
            #assert self.label != 'FACT', \
            #   'Commande %s : Mot-clef facteur present sous un mot-clef facteur : interdit !' \
            #   % parent
         else:
            continue
         del args[nom]
      # seuls les blocs peuvent entrer en conflit avec les mcs du plus haut niveau
      for nom, val in args.items():
         if val.label == 'BLOC':
            mcbloc = val.check_definition(parent)
            #XXX
            #print "#BLOC", parent, re.sub('\s+', ' ', val.condition)
            #assert mcs.isdisjoint(mcbloc), "Commande %s : Mot(s)-clef(s) vu(s) plusieurs fois : %s" \
            #   % (parent, tuple(mcs.intersection(mcbloc)))
      return mcs

  def enregistreXML(self,root,catalogueXml):
      import xml.etree.ElementTree as ET
      import types
      moi=ET.SubElement(root,str(self.__class__))
      nom=ET.SubElement(moi,'nom')
      nom.text=self.nom

      if hasattr(self,'validators') and (self.validators != () and self.validators != None):
         valid=ET.SubElement(moi,'validators')
         valid.text= str(self.validators.__class__)
         catalogueXml.validatorsUtilises.append(self.validators)

      if hasattr(self,'regles') and (self.regles !=() and self.regles != None):
         for regle in self.regles:
             regle.enregistreXML(moi,catalogueXml)
         catalogueXml.reglesUtilisees.append(self.regles)

      if ((self.get_docu() !="" and self.get_docu() !=None) or  \
          (self.fr != "" and self.fr != None) or \
          (self.ang != "" and self.ang != None) ):
                dico={}
                if self.get_docu() !=None : dico["docu"]=self.get_docu()
                if self.fr != None        : dico["fr"]=six.text_type(self.fr,"iso-8859-1")
                if self.ang != None       : dico["ang"]=self.ang
                doc=ET.SubElement(moi,'doc')
                doc.attrib=dico

      if ((self.get_sug() !=None) or  \
          (hasattr(self,'defaut') and (self.defaut != None) and (self.defaut != 'None'))) :
                # il faut ajouter des sug dans le catalogue
                # les attributs sont  toujours du texte 
                dico={}
                if (self.defaut != None) and (self.defaut != 'None') :
                    if isinstance(self.defaut,str ) : dico["defaut"]=six.text_type(self.defaut,"iso-8859-1")
                    else :dico["defaut"]=str(self.defaut)
                if self.get_sug() !=None:
                    if isinstance(self.get_sug(),str ) : dico["sug"]=six.text_type(self.get_sug(),"iso-8859-1")
                    else :dico["sug"]=str(self.get_sug())
                
                doc=ET.SubElement(moi,'ValeurDef')
                doc.attrib=dico

      dico={}
      if hasattr(self,'into') and self.into!=None: dico['into']=str(self.into)
      if hasattr(self,'val_max') and self.val_max != "**" : dico['max']=str(self.val_max)
      if hasattr(self,'val_min') and self.val_min != "**" : dico['min']=str(self.val_min)
      if dico != {} :
           PV=ET.SubElement(moi,'PlageValeur')
           PV.attrib=dico

      dico={}
      if hasattr(self,'max')  and self.max != 1 : dico['max']=str(self.max)
      if hasattr(self,'min')  and self.min != 1 : dico['max']=str(self.min)
      if dico != {} :
           Card=ET.SubElement(moi,'Cardinalite')
           Card.attrib=dico

      dico={}
      if hasattr(self,'reentrant') and self.reentrant not in ('f','n') : dico['reentrant']=str(self.reentrant)
      if hasattr(self,'position') and self.position != "local": dico['position']=str(self.position)
      if hasattr(self,'homo') and self.homo != 1 : dico['homogene']=str(self.homo)
      if hasattr(self,'statut') : dico['statut']=str(self.statut)
      if hasattr(self,'repetable') : dico['repetable']=str(self.repetable)
      if dico != {} :
           pos=ET.SubElement(moi,'situation')
           pos.attrib=dico

      if hasattr(self,'type') and self.type != ():
         typeAttendu=ET.SubElement(moi,'typeAttendu')
         l=[]
         for t in self.type:
             if type(t) == type : l.append(t.__name__)
             else : l.append(t)
         typeAttendu.text=str(l)

      if hasattr(self,'sd_prod') and self.sd_prod != () and self.sd_prod !=None:
         typeCree=ET.SubElement(moi,'typeCree')
         typeCree.text=str(self.sd_prod.__name__) 
 
      if hasattr(self,'op') and self.op !=None  : 
         subRoutine=ET.SubElement(moi,'subRoutine')
         subRoutine.text=str(self.op)

      if hasattr(self,'proc') and self.proc != None : 
         construction=ET.SubElement(moi,'Construction')
         construction.text=self.proc.uri

      for nomFils, fils in self.entites.items() :
          fils.enregistreXML(moi,catalogueXml)
      
  def enregistreXMLStructure(self,root,catalogueXml):
      import xml.etree.ElementTree as ET
      import types
      moi=ET.SubElement(root,str(self.__class__))

      if hasattr(self,'into') and self.into!=None: 
          INTO=ET.SubElement(moi,'into')
          INTO.text='into'

      dico={}
      if hasattr(self,'val_max') and self.val_max != "**" : dico['max']=str(self.val_max)
      if hasattr(self,'val_min') and self.val_min != "**" : dico['min']=str(self.val_min)
      if dico != {} :
           PV=ET.SubElement(moi,'maxOrMin')
           PV.text='maxOrMin'

      dico={}
      if hasattr(self,'max')  and self.max != 1 : dico['max']=str(self.max)
      if hasattr(self,'min')  and self.min != 1 : dico['max']=str(self.min)
      if dico != {} :
           Card=ET.SubElement(moi,'liste')
           Card.text="liste"

      dico={}
      if hasattr(self,'statut') and self.statut=="f" :
         statut=ET.SubElement(moi,'facultatif')
         statut.text='facultatif'
      if hasattr(self,'statut') and self.statut !="f" :
         statut=ET.SubElement(moi,'obligatoire')
         statut.text='obligatoire'

      if hasattr(self,'type') and self.type != ():
        try :
           if 'Fichier' in self.type : ty=ET.SubElement(moi,'Fichier')
           ty.text='type'
        except :
           try :
             if 'Repertoire' in self.type : ty=ET.SubElement(moi,'Repertoire')
             ty.text='type'
           except :
              for t in self.type:
                if t == "I" : ty=ET.SubElement(moi,'typeEntier')
                elif t == "R" : ty=ET.SubElement(moi,'typeReel')
                elif t == "TXM" : ty=ET.SubElement(moi,'typeTXM')
                else :
                  try :
                    ty=ET.SubElement(moi,t.__name__) 
                  except :
                    ty=ET.SubElement(moi,'autre') 
                ty.text='type'

      if hasattr(self,'sd_prod') and self.sd_prod != () and self.sd_prod !=None:
         typeCree=ET.SubElement(moi,'typeCree')
         typeCree.text='sd_prod'
 
      if hasattr(self,'op') and self.op !=None  : 
         subRoutine=ET.SubElement(moi,'subRoutine')
         subRoutine.text='op'

      if hasattr(self,'proc') and self.proc != None : 
         construction=ET.SubElement(moi,'Construction')
         construction.text='proc'

      for nomFils, fils in self.entites.items() :
          fils.enregistreXMLStructure(moi,catalogueXml)
      
