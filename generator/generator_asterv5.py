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
    Ce module contient le plugin generateur de fichier au format asterv5 pour EFICAS.


"""
import traceback
import types,string

from Noyau import N_CR
from Accas import ETAPE,PROC_ETAPE,MACRO_ETAPE,ETAPE_NIVEAU,JDC,FORM_ETAPE
from Accas import MCSIMP,MCFACT,MCBLOC,MCList,EVAL
from Accas import GEOM,ASSD
from Accas import COMMENTAIRE,PARAMETRE, PARAMETRE_EVAL,COMMANDE_COMM
from Formatage import Formatage

def entryPoint():
   """
       Retourne les informations nécessaires pour le chargeur de plugins

       Ces informations sont retournées dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'asterv5',
        # La factory pour créer une instance du plugin
          'factory' : AsterGenerator,
          }


class AsterGenerator:
   """
       Ce generateur parcourt un objet de type JDC et produit
       un fichier au format asterv5

       L'acquisition et le parcours sont réalisés par la méthode
       generator.gener(objet_jdc,format)

       L'écriture du fichier au format asterv5 est réalisée par appel de la méthode
       generator.writefile(nom_fichier)

       Ses caractéristiques principales sont exposées dans des attributs 
       de classe :
         - extensions : qui donne une liste d'extensions de fichier préconisées

   """
   # Les extensions de fichier préconisées
   extensions=('.comm',)

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR generateur format asterv5',
                         fin='fin CR format asterv5')
      # Le texte au format asterv5 est stocké dans l'attribut text
      self.text=''

   def writefile(self,filename):
      fp=open(filename,'w')
      fp.write(self.text)
      fp.close()

   def gener(self,obj,format='brut'):
      """
          Retourne une représentation du JDC obj sous une
          forme qui est paramétrée par format.
          Si format vaut 'brut',      retourne une liste de listes de ...
          Si format vaut 'standard',  retourne un texte obtenu par concaténation de la liste
          Si format vaut 'beautifie', retourne le meme texte beautifié
      """
      liste= self.generator(obj)
      if format == 'brut':
         self.text=liste
      elif format == 'standard':
         self.text=string.join(liste)
      elif format == 'beautifie':
         jdc_formate = Formatage(liste,sep=':',l_max=72)
         self.text=jdc_formate.formate_jdc()
      else:
         raise "Format pas implémenté : "+format
      return self.text

   def generator(self,obj):
      """
         Cette methode joue un role d'aiguillage en fonction du type de obj
         On pourrait utiliser les méthodes accept et visitxxx à la
         place (dépend des gouts !!!)
      """
      # ATTENTION a l'ordre des tests : il peut avoir de l'importance (héritage)
      if isinstance(obj,PROC_ETAPE):
         return self.generPROC_ETAPE(obj)
      elif isinstance(obj,MACRO_ETAPE):
         return self.generMACRO_ETAPE(obj)
      elif isinstance(obj,FORM_ETAPE):
         return self.generFORM_ETAPE(obj)
      elif isinstance(obj,ETAPE):
         return self.generETAPE(obj)
      elif isinstance(obj,MCFACT):
         return self.generMCFACT(obj)
      elif isinstance(obj,MCList):
         return self.generMCList(obj)
      elif isinstance(obj,MCBLOC):
         return self.generMCBLOC(obj)
      elif isinstance(obj,MCSIMP):
         return self.generMCSIMP(obj)
      elif isinstance(obj,ASSD):
         return self.generASSD(obj)
      elif isinstance(obj,ETAPE_NIVEAU):
         return self.generETAPE_NIVEAU(obj)
      elif isinstance(obj,COMMENTAIRE):
         return self.generCOMMENTAIRE(obj)
      # Attention doit etre placé avant PARAMETRE (raison : héritage)
      elif isinstance(obj,PARAMETRE_EVAL):
         return self.generPARAMETRE_EVAL(obj)
      elif isinstance(obj,PARAMETRE):
         return self.generPARAMETRE(obj)
      elif isinstance(obj,EVAL):
         return self.generEVAL(obj)
      elif isinstance(obj,COMMANDE_COMM):
         return self.generCOMMANDE_COMM(obj)
      elif isinstance(obj,JDC):
         return self.generJDC(obj)
      else:
         raise "Type d'objet non prévu",obj

   def generJDC(self,obj):
      """
         Cette méthode convertit un objet JDC en une liste de chaines de 
         caractères à la syntaxe asterv5
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
         # Si au moins une étape, on ajoute le retour chariot sur la dernière étape
         if type(l[-1])==types.ListType:
            l[-1][-1] = l[-1][-1]+'\n'
         elif type(l[-1])==types.StringType:
            l[-1] = l[-1]+'\n' 
      return l

   def generCOMMANDE_COMM(self,obj):
      """
         Cette méthode convertit un COMMANDE_COMM
         en une liste de chaines de caractères à la syntaxe asterv5
      """
      l_lignes = string.split(obj.valeur,'\n')
      txt=''
      for ligne in l_lignes:
          txt = txt + '%%'+ligne+'\n'
      return txt

   def generEVAL(self,obj):
      """
         Cette méthode convertit un EVAL
         en une liste de chaines de caractères à la syntaxe asterv5
      """
      return 'EVAL("'+ obj.valeur +'")'

   def generCOMMENTAIRE(self,obj):
      """
         Cette méthode convertit un COMMENTAIRE
         en une liste de chaines de caractères à la syntaxe asterv5
      """
      l_lignes = string.split(obj.valeur,'\n')
      txt=''
      for ligne in l_lignes:
        txt = txt + '%'+ligne+'\n'
      return txt

   def generPARAMETRE_EVAL(self,obj):
      """
         Cette méthode convertit un PARAMETRE_EVAL
         en une liste de chaines de caractères à la syntaxe asterv5
      """
      if obj.valeur == None:
         return obj.nom + ' = None ;\n'
      else:
         return obj.nom + ' = '+ self.generator(obj.valeur) +';\n'

   def generPARAMETRE(self,obj):
      """
         Cette méthode convertit un PARAMETRE
         en une liste de chaines de caractères à la syntaxe asterv5
      """
      if type(obj.valeur) == types.StringType:
        return obj.nom + " = '" + obj.valeur + "';\n"
      else:
        return obj.nom + ' = ' + str(obj.valeur) + ';\n'

   def generETAPE_NIVEAU(self,obj):
      """
         Cette méthode convertit une étape niveau
         en une liste de chaines de caractères à la syntaxe asterv5
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
         Cette méthode convertit une étape
         en une liste de chaines de caractères à la syntaxe asterv5
      """
      try:
        if obj.reuse != None:
          sdname= "&" + self.generator(obj.reuse)
        else:
          sdname= self.generator(obj.sd)
      except:
        sdname='sansnom'
      l=[]
      label=sdname + '='+obj.definition.nom+'('
      l.append(label)
      for v in obj.mc_liste:
        if isinstance(v,MCBLOC) or isinstance(v,MCList):
          liste=self.generator(v)
          for mocle in liste :
            l.append(mocle)
        else:
          l.append(self.generator(v))
      if len(l) == 1:
        l[0]=label+');'
      else :
        l.append(');')
      return l

   def generFORM_ETAPE(self,obj):
        """
            Méthode particulière pour les objets de type FORMULE
        """
        l=[]
        nom = obj.get_nom()
        if nom == '' : nom = 'sansnom'
        if len(obj.mc_liste)>0:
            l.append(nom + ' = FORMULE(')
            s=obj.type_retourne + ' = ' + "'''" + obj.arguments + ' = ' + obj.corps+"'''"
            l.append(s)
            l.append(');')
        else:
            l.append(nom+' = FORMULE();')
        return l

   def generMACRO_ETAPE(self,obj):
      """
         Cette méthode convertit une macro-étape
         en une liste de chaines de caractères à la syntaxe asterv5
      """
      if obj.definition.nom == 'FORMULE' : return self.gen_ast_formule(obj)
      try:
        if obj.reuse != None:
          sdname= "&" + self.generator(obj.reuse)+'='
        elif obj.sd == None:
          sdname=''
        else:
          sdname= self.generator(obj.sd)+'='
      except:
        sdname='sansnom='
      l=[]
      label = sdname + obj.definition.nom+'('
      l.append(label)
      for v in obj.mc_liste:
        if isinstance(v,MCBLOC) or isinstance(v,MCList):
          liste=self.generator(v)
          for mocle in liste :
            l.append(mocle)
        else:
          # MCFACT ou MCSIMP
          l.append(self.generator(v))
      if len(l) == 1:
        l[0]=label+');'
      else :
        l.append(');')
      return l

   def gen_ast_formule(self,obj):
      """ 
           Méthode gen_ast particuliere aux objets de type FORMULE 
      """
      label='!FORMULE('
      try:
        sdname= self.generator(obj.sd)
      except:
        sdname='sansnom'
      l=[]
      l.append(label)
      for v in obj.mc_liste:
        s=''
        s= v.nom+':'+sdname+'('+v.valeur+')'
        l.append(s)
      if len(l) == 1:
        l[0]=label+');'
      else :
        l.append(');')
      return l

   def generPROC_ETAPE(self,obj):
      """
         Cette méthode convertit une étape
         en une liste de chaines de caractères à la syntaxe asterv5
      """
      l=[]
      label=obj.definition.nom+'('
      l.append(label)
      for v in obj.mc_liste:
        if isinstance(v,MCBLOC) or isinstance(v,MCList):
          liste=self.generator(v)
          for mocle in liste :
            l.append(mocle)
        else:
          l.append(self.generator(v))
      if len(l) == 1:
        l[0]=label+');'
      else :
        l.append(');')
      return l

   def generMCSIMP(self,obj) :
      """
          Convertit un objet MCSIMP en une liste de chaines de caractères à la
          syntaxe asterv5
      """
      if type(obj.valeur) == types.TupleType :
        s = '('
        for val in obj.valeur :
          if s != '(': s = s + ','
          if type(val) == types.InstanceType :
            if isinstance(val,PARAMETRE):
              # il ne faut pas prendre la string que retourne gen_ast
              # mais seulement le nom dans le cas d'un paramètre
              s = s + val.nom
            else:
              s = s + self.generator(val)
          elif self.wait_geom(obj):
            s = s + val
          elif type(val) == types.FloatType :
            #s = s + self.repr_float(val)
            s = s + str(val)
          else :
            s = s + `val`
        s = s + ')'
        s=obj.nom+':'+s+' '
        return s
      else :
        if type(obj.valeur) == types.InstanceType :
          if isinstance(obj.valeur,PARAMETRE):
            # il ne faut pas prendre la string que retourne gen_ast
            # mais seulement str dans le cas d'un paramètre
            s = obj.valeur.nom
          else:
            s =  self.generator(obj.valeur)
        elif self.wait_geom(obj):
            s = obj.valeur
        elif type(obj.valeur) == types.FloatType :
            #s = self.repr_float(obj.valeur)
            s = str(obj.valeur)
        else :
          s = `obj.valeur`
        s=obj.nom+':'+s+' '
        return s

   def wait_geom(self,obj):
      for typ in obj.definition.type:
        if type(typ) == types.ClassType :
          if issubclass(typ,GEOM) : return 1
      return 0

   def repr_float(self,valeur):
      """ 
          Cette fonction représente le réel valeur comme une chaîne de caractères
          sous forme mantisse exposant si nécessaire cad si le nombre contient plus de 5 caractères
          NB : valeur est un réel au format Python ou une chaîne de caractères représentant un réel
      """
      if type(valeur) == types.StringType : valeur = eval(valeur)
      if valeur == 0. : return '0.0'
      if abs(valeur) > 1. :
        if abs(valeur) < 10000. : return repr(valeur)
      else :
        if abs(valeur) > 0.01 : return repr(valeur)
      t=repr(valeur)
      if string.find(t,'e') != -1 or string.find(t,'E') != -1 :
        # le réel est déjà sous forme mantisse exposant !
        # --> on remplace e par E
        t=string.replace(t,'e','E')
        # --> on doit encore vérifier que la mantisse contient bien un '.'
        if string.find(t,'.')!= -1:
          return t
        else:
          # -->il faut rajouter le point avant le E
          t=string.replace(t,'E','.E')
          return t
      s=''
      neg = 0
      if t[0]=='-':
        s=s+t[0]
        t=t[1:]
      cpt = 0
      if string.atof(t[0]) == 0.:
        # réel plus petit que 1
        neg = 1
        t=t[2:]
        cpt=1
        while string.atof(t[0]) == 0. :
          cpt = cpt+1
          t=t[1:]
        s=s+t[0]+'.'
        for c in t[1:]:
          s=s+c
      else:
        # réel plus grand que 1
        s=s+t[0]+'.'
        if string.atof(t[1:]) == 0.:
          l=string.split(t[1:],'.')
          cpt = len(l[0])
        else:
          r=0
          pt=0
          for c in t[1:]:
            r=r+1
            if c != '.' :
              if pt != 1 : cpt = cpt + 1
              s=s+c
            else:
              pt = 1
              if r+1 == len(t) or string.atof(t[r+1:]) == 0.:break
      s=s+'E'+neg*'-'+repr(cpt)
      return s

   def generASSD(self,obj):
      """
          Convertit un objet dérivé d'ASSD en une chaine de caractères à la
          syntaxe asterv5
      """
      return obj.get_name()

   def generMCFACT(self,obj):
      """
          Convertit un objet MCFACT en une liste de chaines de caractères à la
          syntaxe asterv5
      """
      l=[]
      label=obj.nom + ':('
      l.append(label)
      for v in obj.mc_liste:
        if isinstance(v,MCBLOC) or isinstance(v,MCList):
          liste=self.generator(v)
          for mocle in liste :
            l.append(mocle)
        else:
          l.append(self.generator(v))
      l.append(')')
      return l

   def generMCList(self,obj):
      """
          Convertit un objet MCList en une liste de chaines de caractères à la
          syntaxe asterv5
      """
      l=[]
      for mcfact in obj.data:
         l.append(self.generator(mcfact))
      return l

   def generMCBLOC(self,obj):
      """
          Convertit un objet MCBLOC en une liste de chaines de caractères à la
          syntaxe asterv5
      """
      l=[]
      for v in obj.mc_liste:
        if isinstance(v,MCBLOC) or isinstance(v,MCList):
          liste=self.generator(v)
          for mocle in liste :
            l.append(mocle)
        else:
          l.append(self.generator(v))
      return l

