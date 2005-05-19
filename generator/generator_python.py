# -*- coding: utf-8 -*-
#            CONFIGURATION MANAGEMENT OF EDF VERSION
# ======================================================================
# COPYRIGHT (C) 1991 - 2002  EDF R&D                  WWW.CODE-ASTER.ORG
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
#
#
# ======================================================================
"""
    Ce module contient le plugin generateur de fichier au format 
    python pour EFICAS.

"""
import traceback
import types,string,re

from Noyau import N_CR
from Noyau.N_utils import repr_float
import Accas
from Extensions.parametre import ITEM_PARAMETRE
from Formatage import Formatage

def entryPoint():
   """
       Retourne les informations n�cessaires pour le chargeur de plugins

       Ces informations sont retourn�es dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'python',
        # La factory pour cr�er une instance du plugin
          'factory' : PythonGenerator,
          }


class PythonGenerator:
   """
       Ce generateur parcourt un objet de type JDC et produit
       un fichier au format python 

       L'acquisition et le parcours sont r�alis�s par la m�thode
       generator.gener(objet_jdc,format)

       L'�criture du fichier au format ini par appel de la m�thode
       generator.writefile(nom_fichier)

       Ses caract�ristiques principales sont expos�es dans des attributs 
       de classe :
         - extensions : qui donne une liste d'extensions de fichier pr�conis�es

   """
   # Les extensions de fichier pr�conis�es
   extensions=('.comm',)

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR generateur format python pour python',
                         fin='fin CR format python pour python')
      # Le texte au format python est stock� dans l'attribut text
      self.text=''
      self.appli=None

   def writefile(self,filename):
      fp=open(filename,'w')
      fp.write(self.text)
      fp.close()

   def gener(self,obj,format='brut'):
      """
          Retourne une repr�sentation du JDC obj sous une
          forme qui est param�tr�e par format.
          Si format vaut 'brut', retourne une liste de listes de ...
          Si format vaut 'standard', retourne un texte obtenu par concat�nation de la liste
          Si format vaut 'beautifie', retourne le meme texte beautifi�
      """
      self.appli=obj.get_jdc_root().appli
      #self.appli=obj.appli
      liste= self.generator(obj)
      if format == 'brut':
         self.text=liste
      elif format == 'standard':
         self.text=string.join(liste)
      elif format == 'beautifie':
         jdc_formate = Formatage(liste,mode='.py')
         self.text=jdc_formate.formate_jdc()
      else:
         raise "Format pas impl�ment� : "+format
      return self.text

   def generator(self,obj):
      """
         Cette methode joue un role d'aiguillage en fonction du type de obj
         On pourrait utiliser les m�thodes accept et visitxxx � la 
         place (d�pend des gouts !!!)
      """
      # ATTENTION a l'ordre des tests : il peut avoir de l'importance (h�ritage)
      if isinstance(obj,Accas.PROC_ETAPE):
         return self.generPROC_ETAPE(obj)
      # Attention doit etre plac� avant MACRO (raison : h�ritage)
      elif isinstance(obj,Accas.FORM_ETAPE):
         return self.generFORM_ETAPE(obj)
      elif isinstance(obj,Accas.MACRO_ETAPE):
         return self.generMACRO_ETAPE(obj)
      elif isinstance(obj,Accas.ETAPE):
         return self.generETAPE(obj)
      elif isinstance(obj,Accas.MCFACT):
         return self.generMCFACT(obj)
      elif isinstance(obj,Accas.MCList):
         return self.generMCList(obj)
      elif isinstance(obj,Accas.MCBLOC):
         return self.generMCBLOC(obj)
      elif isinstance(obj,Accas.MCSIMP):
         return self.generMCSIMP(obj)
      elif isinstance(obj,Accas.ASSD):
         return self.generASSD(obj)
      elif isinstance(obj,Accas.ETAPE_NIVEAU):
         return self.generETAPE_NIVEAU(obj)
      elif isinstance(obj,Accas.COMMENTAIRE):
         return self.generCOMMENTAIRE(obj)
      # Attention doit etre plac� avant PARAMETRE (raison : h�ritage)
      elif isinstance(obj,Accas.PARAMETRE_EVAL):
         return self.generPARAMETRE_EVAL(obj)
      elif isinstance(obj,Accas.PARAMETRE):
         return self.generPARAMETRE(obj)
      elif isinstance(obj,Accas.EVAL):
         return self.generEVAL(obj)
      elif isinstance(obj,Accas.COMMANDE_COMM):
         return self.generCOMMANDE_COMM(obj)
      elif isinstance(obj,Accas.JDC):
         return self.generJDC(obj)
      elif isinstance(obj,Accas.MCNUPLET):
         return self.generMCNUPLET(obj)
      elif isinstance(obj,ITEM_PARAMETRE):
         return self.generITEM_PARAMETRE(obj)
      else:
         raise "Type d'objet non pr�vu",obj

   def generJDC(self,obj):
      """
         Cette m�thode convertit un objet JDC en une liste de chaines de
         caract�res � la syntaxe python
      """
      l=[]
      if obj.definition.l_niveaux == ():
         # Il n'y a pas de niveaux
         for etape in obj.etapes:
            l.append(self.generator(etape))
      else:
         # Il y a des niveaux
         for etape_niveau in obj.etapes_niveaux:
            l.extend(self.generator(etape_niveau))
      if l != [] :
         # Si au moins une �tape, on ajoute le retour chariot sur la derni�re �tape
         if type(l[-1])==types.ListType:
            l[-1][-1] = l[-1][-1]+'\n'
         elif type(l[-1])==types.StringType:
            l[-1] = l[-1]+'\n'
      return l

   def generMCNUPLET(self,obj):
      """ 
          M�thode g�n�rant une repr�sentation de self permettant son ecriture
          dans le format python
      """
      l=[]
      l.append('(')
      for v in obj.mc_liste:
        text = re.sub(".*=","",self.generator(v))
        l.append(text)
      l.append('),')
      return l

   def generCOMMANDE_COMM(self,obj):
      """
         Cette m�thode convertit un COMMANDE_COMM
         en une liste de chaines de caract�res � la syntaxe python
      """
      l_lignes = string.split(obj.valeur,'\n')
      txt=''
      for ligne in l_lignes:
          txt = txt + '##'+ligne+'\n'
      return txt

   def generEVAL(self,obj):
      """
         Cette m�thode convertit un EVAL
         en une liste de chaines de caract�res � la syntaxe python
      """
      return 'EVAL("""'+ obj.valeur +'""")'

   def generCOMMENTAIRE(self,obj):
      """
         Cette m�thode convertit un COMMENTAIRE
         en une liste de chaines de caract�res � la syntaxe python
      """
      # modification pour r�pondre � la demande de C. Durand, d'�viter
      # l'ajout syst�matique d'un di�se, � la suite du commentaire
      # Dans la chaine de caracteres obj.valeur, on supprime le dernier
      # saut de ligne
      sans_saut = re.sub("\n$","",obj.valeur)
      l_lignes = string.split(sans_saut,'\n')
      txt=''
      for ligne in l_lignes:
        txt = txt + '#'+ligne+'\n'

      # suppression du dernier saut de ligne
      txt = re.sub("\n$","",txt)
      return txt

   def generPARAMETRE_EVAL(self,obj):
      """
         Cette m�thode convertit un PARAMETRE_EVAL
         en une liste de chaines de caract�res � la syntaxe python
      """
      if obj.valeur == None:
         return obj.nom + ' = None ;\n'
      else:
         return obj.nom + ' = '+ self.generator(obj.valeur) +';\n'

   def generITEM_PARAMETRE(self,obj):
       return repr(obj) 

   def generPARAMETRE(self,obj):
      """
         Cette m�thode convertit un PARAMETRE
         en une liste de chaines de caract�res � la syntaxe python
      """
      if type(obj.valeur) == types.StringType:
        # PN pour corriger le bug a='3+4' au lieu de a= 3+4
        #return obj.nom + " = '" + obj.valeur + "';\n"
        return obj.nom + " = " + obj.valeur + ";\n"
      else:
        return obj.nom + ' = ' + str(obj.valeur) + ';\n'

   def generETAPE_NIVEAU(self,obj):
      """
         Cette m�thode convertit une �tape niveau
         en une liste de chaines de caract�res � la syntaxe python
      """
      l=[]
      if obj.etapes_niveaux == []:
        for etape in obj.etapes:
          l.append(self.generator(etape))
      else:
        for etape_niveau in obj.etapes_niveaux:
          l.extend(self.generator(etape_niveau))
      return l

   def generETAPE(self,obj):
      """
         Cette m�thode convertit une �tape
         en une liste de chaines de caract�res � la syntaxe python
      """
      try:
        sdname= self.generator(obj.sd)
      except:
        sdname='sansnom'
      l=[]
      label=sdname + '='+obj.definition.nom+'('
      l.append(label)
      if obj.reuse != None :
        str = 'reuse ='+ self.generator(obj.reuse) + ','
        l.append(str)
      for v in obj.mc_liste:
        if isinstance(v,Accas.MCBLOC) :
          liste=self.generator(v)
          for mocle in liste :
            l.append(mocle)
        elif isinstance(v,Accas.MCSIMP) :
          text=self.generator(v)
          l.append(v.nom+'='+text)
        else:
          # MCFACT ou MCList
          liste=self.generator(v)
          liste[0]=v.nom+'='+liste[0]
          l.append(liste)
      if len(l) == 1:
        l[0]=label+');'
      else :
        l.append(');')
      return l

   def generFORM_ETAPE(self,obj):
        """
            M�thode particuli�re pour les objets de type FORMULE
        """
        l=[]
        nom = obj.get_nom()
        if nom == '' : nom = 'sansnom'
        l.append(nom + ' = FORMULE(')
        for v in obj.mc_liste:
	    text=self.generator(v)
	    l.append(v.nom+'='+text)
        l.append(');')
        return l

   def generMACRO_ETAPE(self,obj):
      """
         Cette m�thode convertit une macro-�tape
         en une liste de chaines de caract�res � la syntaxe python
      """
      try:
        if obj.sd == None:
          sdname=''
        else:
          sdname= self.generator(obj.sd)+'='
      except:
        sdname='sansnom='
      l=[]
      label = sdname + obj.definition.nom+'('
      l.append(label)
      if obj.reuse != None:
         # XXX faut il la virgule ou pas ????
         str = "reuse =" + self.generator(obj.reuse) + ','
         l.append(str)
      for v in obj.mc_liste:
        if isinstance(v,Accas.MCBLOC) :
          liste=self.generator(v)
          for mocle in liste :
            l.append(mocle)
        elif isinstance(v,Accas.MCSIMP) :
          text=self.generator(v)
          l.append(v.nom+'='+text)
        else:
          # MCFACT ou MCList
          liste=self.generator(v)
          liste[0]=v.nom+'='+liste[0]
          l.append(liste)

      if len(l) == 1:
        l[0]=label+');'
      else :
        l.append(');')
      return l

   def generPROC_ETAPE(self,obj):
      """
         Cette m�thode convertit une PROC �tape
         en une liste de chaines de caract�res � la syntaxe python
      """
      l=[]
      label=obj.definition.nom+'('
      l.append(label)
      for v in obj.mc_liste:
        if isinstance(v,Accas.MCBLOC) :
          liste=self.generator(v)
          for mocle in liste :
            l.append(mocle)
        elif isinstance(v,Accas.MCSIMP) :
          text=self.generator(v)
          l.append(v.nom+'='+text)
        else:
          # MCFACT ou MCList
          liste=self.generator(v)
          liste[0]=v.nom+'='+liste[0]
          l.append(liste)

      if len(l) == 1:
        l[0]=label+');'
      else :
        l.append(');')
      return l

   def generASSD(self,obj):
      """
          Convertit un objet d�riv� d'ASSD en une chaine de caract�res � la
          syntaxe python
      """
      return obj.get_name()

   def generMCFACT(self,obj):
      """
          Convertit un objet MCFACT en une liste de chaines de caract�res � la
          syntaxe python
      """
      l=[]
      l.append('_F(')
      for v in obj.mc_liste:
         if not isinstance(v,Accas.MCSIMP) and not isinstance (v,Accas.MCBLOC) :
           # on est en pr�sence d'une entite compos�e : on r�cup�re une liste
           liste=self.generator(v)
           liste[0]=v.nom+'='+liste[0]
           l.append(liste)
         elif isinstance(v,Accas.MCBLOC):
           liste=self.generator(v)
           for arg in liste :
             l.append(arg)
         else:
           # on est en pr�sence d'un MCSIMP : on r�cup�re une string
           text =self.generator(v)
           l.append(v.nom+'='+text)
      # il faut �tre plus subtil dans l'ajout de la virgule en diff�renciant 
      # le cas o� elle est obligatoire (si self a des fr�res cadets 
      # dans self.parent) ou non
      # (cas o� self est seul ou le benjamin de self.parent)
      l.append('),')
      return l

   def generMCList(self,obj):
      """
          Convertit un objet MCList en une liste de chaines de caract�res � la
          syntaxe python
      """
      if len(obj.data) > 1:
         l=['(']
         for mcfact in obj.data: l.append(self.generator(mcfact))
         l.append('),')
      else:
         l= self.generator(obj.data[0])
      return l

   def generMCBLOC(self,obj):
      """
          Convertit un objet MCBLOC en une liste de chaines de caract�res � la
          syntaxe python
      """
      l=[]
      for v in obj.mc_liste:
        if isinstance(v,Accas.MCBLOC) :
          liste=self.generator(v)
          for mocle in liste :
            l.append(mocle)
        elif isinstance(v,Accas.MCList):
          liste=self.generator(v)
          liste[0]=v.nom+'='+liste[0]
          for mocle in liste :
            l.append(mocle)
        else:
          data=self.generator(v)
          if type(data) == types.ListType:
            data[0]=v.nom+'='+data[0]
          else:
            data=v.nom+'='+data
          l.append(data)
      return l

   def generMCSIMP(self,obj) :
      """
          Convertit un objet MCSIMP en une liste de chaines de caract�res � la
          syntaxe python
      """
      if type(obj.valeur) in (types.TupleType,types.ListType) :
         s = ''
         for val in obj.valeur :
            if type(val) == types.InstanceType :
               if hasattr(obj.etape,'sdprods') and val in obj.etape.sdprods :
                  s = s + "CO('"+ self.generator(val) +"')"
               elif val.__class__.__name__ == 'CO':
                  s = s + "CO('"+ self.generator(val) +"')"
               elif isinstance(val,Accas.PARAMETRE):
                  # il ne faut pas prendre la string que retourne gener
                  # mais seulement le nom dans le cas d'un param�tre
                  s = s + val.nom
               else:
                  s = s + self.generator(val)
            elif type(val) == types.FloatType :
               # Pour un flottant on utilise str qui a une precision de
               # "seulement" 12 chiffres : evite les flottants du genre 0.599999999999998
               s2=str(val)
               try :
                 clefobj=obj.GetNomConcept()
                 if self.appli.dict_reels.has_key(clefobj):
                    if self.appli.dict_reels[clefobj].has_key(val):
                       s2=self.appli.dict_reels[clefobj][val]
               except:
                  pass
               s = s + s2
            else :
               # Pour les autres types on utilise repr
               s = s + `val`
            s = s + ','
         if len(obj.valeur) > 1:
            s = '(' + s + '),'
      else :
         val=obj.valeur
         if type(val) == types.InstanceType :
            if hasattr(obj.etape,'sdprods') and val in obj.etape.sdprods :
               s = "CO('"+ self.generator(val) +"')"
            elif val.__class__.__name__ == 'CO':
                s = "CO('"+ self.generator(val) +"')"
            elif isinstance(val,Accas.PARAMETRE):
                # il ne faut pas prendre la string que retourne gener
                # mais seulement le nom dans le cas d'un param�tre
                s = val.nom
            else:
                s = self.generator(val)
         elif type(val) == types.FloatType :
            # Pour un flottant on utilise str 
            # ou la notation scientifique
            s = str(val)
            try :
              clefobj=obj.GetNomConcept()
              if self.appli.dict_reels.has_key(clefobj):
                 if self.appli.dict_reels[clefobj].has_key(val):
                    s=self.appli.dict_reels[clefobj][val]
            except:
              pass
         else :
            # Pour les autres types on utilise repr
            s = `val`
         s= s + ','
      return s


