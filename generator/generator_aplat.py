"""
    Ce module contient le plugin generateur de fichier au format 
    aplat pour EFICAS.

"""
import traceback
import types,string,re

from Noyau import N_CR
from Noyau.N_utils import repr_float
from Accas import ETAPE,PROC_ETAPE,MACRO_ETAPE,ETAPE_NIVEAU,JDC,FORM_ETAPE
from Accas import MCSIMP,MCFACT,MCBLOC,MCList,EVAL
from Accas import GEOM,ASSD,MCNUPLET
from Accas import COMMENTAIRE,PARAMETRE, PARAMETRE_EVAL,COMMANDE_COMM

def entryPoint():
   """
       Retourne les informations n�cessaires pour le chargeur de plugins

       Ces informations sont retourn�es dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'aplat',
        # La factory pour cr�er une instance du plugin
          'factory' : AplatGenerator,
          }


class AplatGenerator:
   """
       Ce generateur parcourt un objet de type JDC et produit
       un fichier au format aplat 

       L'acquisition et le parcours sont r�alis�s par la m�thode
       generator.gener(objet_jdc,format)

       L'�criture du fichier au format ini par appel de la m�thode
       generator.writefile(nom_fichier)

       Ses caract�ristiques principales sont expos�es dans des attributs 
       de classe :

       - extensions : qui donne une liste d'extensions de fichier pr�conis�es

   """
   # Les extensions de fichier pr�conis�es
   extensions=('.*',)

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR generateur format aplat pour eficas',
                         fin='fin CR format aplat pour eficas')
      self.init=''
      # Le s�parateur utiis�
      self.sep='//'
      # Le texte au format aplat est stock� dans l'attribut text
      self.text=''

   def writefile(self,filename):
      fp=open(filename,'w')
      fp.write(self.text)
      fp.close()

   def gener(self,obj,format='brut'):
      """
          Retourne une repr�sentation du JDC obj sous une
          forme qui est param�tr�e par format.
          Si format vaut 'brut', 'standard' ou 'beautifie', retourne le texte issu
                       de generator
      """
      liste= self.generator(obj)
      if format == 'brut':
         self.text=liste
      elif format == 'standard':
         self.text=liste
      elif format == 'beautifie':
         self.text=liste
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
      # Attention doit etre plac� avant PARAMETRE (raison : h�ritage)
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
      elif isinstance(obj,MCNUPLET):
         return self.generMCNUPLET(obj)
      else:
         raise "Type d'objet non pr�vu",obj

   def generJDC(self,obj):
      """
         Cette m�thode convertit un objet JDC en une chaine de
         caract�res � la syntaxe aplat
      """
      text=''
      if obj.definition.l_niveaux == ():
         # Il n'y a pas de niveaux
         for etape in obj.etapes:
            text=text+self.generator(etape)+'\n'
      else:
         # Il y a des niveaux
         for etape_niveau in obj.etapes_niveaux:
            text=text+self.generator(etape_niveau)+'\n'
      return text

   def generCOMMANDE_COMM(self,obj):
      """
         Cette m�thode convertit un COMMANDE_COMM
         en une chaine de caract�res � la syntaxe aplat 
      """
      l_lignes = string.split(obj.valeur,'\n')
      txt=''
      for ligne in l_lignes:
          txt = txt + '##'+ligne+'\n'
      return txt

   def generEVAL(self,obj):
      """
         Cette m�thode convertit un EVAL
         en une chaine de caract�res � la syntaxe aplat 
      """
      return 'EVAL("""'+ obj.valeur +'""")'

   def generCOMMENTAIRE(self,obj):
      """
         Cette m�thode convertit un COMMENTAIRE
         en une chaine de caract�res � la syntaxe aplat  
      """
      l_lignes = string.split(obj.valeur,'\n')
      txt=''
      for ligne in l_lignes:
        txt = txt + '#'+ligne+'\n'
      return txt

   def generPARAMETRE_EVAL(self,obj):
      """
         Cette m�thode convertit un PARAMETRE_EVAL
         en une chaine de caract�res � la syntaxe aplat 
      """
      if obj.valeur == None:
         return obj.nom + ' = None ;\n'
      else:
         return obj.nom + ' = '+ self.generator(obj.valeur) +';\n'

   def generPARAMETRE(self,obj):
      """
         Cette m�thode convertit un PARAMETRE
         en une chaine de caract�res � la syntaxe aplat 
      """
      if type(obj.valeur) == types.StringType:
        return obj.nom + " = '" + obj.valeur + "';\n"
      else:
        return obj.nom + ' = ' + str(obj.valeur) + ';\n'

   def generETAPE_NIVEAU(self,obj):
      """
         Cette m�thode convertit une �tape niveau
         en une chaine de caract�res � la syntaxe aplat 
      """
      text=''
      if obj.etapes_niveaux == []:
        for etape in obj.etapes:
          text=text+self.generator(etape)+'\n'
      else:
        for etape_niveau in obj.etapes_niveaux:
          text=text+self.generator(etape_niveau)+'\n'
      return text

   def gener_etape(self,obj):
      """
         Cette m�thode est utilis� pour convertir les objets etape
         en une chaine de caract�res � la syntaxe aplat 
      """
      text=''
      for v in obj.mc_liste:
         text=text + self.generator(v)
      if text=='':
         return self.init+'\n'
      else:
         return text

   def generETAPE(self,obj):
      """
         Cette m�thode convertit une �tape
         en une chaine de caract�res � la syntaxe aplat 
      """
      try:
        sdname= self.generator(obj.sd)
      except:
        sdname='sansnom'
      self.init = sdname + self.sep + obj.nom
      return self.gener_etape(obj)

   def generMACRO_ETAPE(self,obj):
      """
         Cette m�thode convertit une macro-�tape
         en une chaine de caract�res � la syntaxe aplat 
      """
      try:
        if obj.sd == None:
          self.init = obj.nom
        else:
          sdname= self.generator(obj.sd)
          self.init = sdname + self.sep + obj.nom
      except:
        self.init = 'sansnom' + self.sep + obj.nom

      return self.gener_etape(obj)

   generPROC_ETAPE = generMACRO_ETAPE

   generFORM_ETAPE = generMACRO_ETAPE

   def generASSD(self,obj):
      """
          Convertit un objet d�riv� d'ASSD en une chaine de caract�res � la
          syntaxe aplat 
      """
      return obj.get_name()

   def generMCList(self,obj):
      """
          Convertit un objet MCList en une chaine de caract�res � la
          syntaxe aplat
      """
      i=0
      text = ''
      init = self.init + self.sep + obj.nom
      old_init=self.init
      for data in self.data :
        i=i+1
        self.init = init + self.sep + "occurrence n�"+`i`
        text = text + self.generator(data)
      self.init=old_init
      return text

   def generMCSIMP(self,obj) :
      """
          Convertit un objet MCSIMP en une chaine de caract�res � la
          syntaxe aplat 
      """
      if type(obj.valeur) in (types.TupleType,types.ListType) :
         # On est en pr�sence d'une liste de valeur
         rep = '('
         for val in self.valeur:
           if type(val) == types.InstanceType :
             rep = rep + self.generator(val) +','
           else:
             rep = rep + `val`+','
         rep = rep + ')'
      elif type(obj.valeur) == types.InstanceType :
         # On est en pr�sence d'une valeur unique de type instance
         rep = self.generator(obj.valeur)
      else :
         # On est en pr�sence d'une valeur unique
         rep = `obj.valeur`
      return self.init + self.sep + obj.nom + ' :' + rep + '\n'

   def generMCCOMPO(self,obj):
      """
          Convertit un objet MCCOMPO en une chaine de caract�res � la
          syntaxe aplat
      """
      text = ''
      old_init=self.init
      self.init = self.init + self.sep + obj.nom
      for mocle in obj.mc_liste :
        text = text + self.generator(mocle)
      self.init=old_init
      return text

   generMCFACT=generMCCOMPO

   generMCBLOC=generMCCOMPO

   generMCNUPLET=generMCCOMPO


