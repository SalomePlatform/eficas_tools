# -*- coding: utf-8 -*-
# Copyright (C) 2007-2013   EDF R&D
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
"""
    Ce module contient le plugin generateur de fichier
    au format ini pour EFICAS.


"""
import traceback
import types,string
from Extensions.i18n import tr
from Extensions.eficas_exception import EficasException


from Noyau import N_CR
from Accas import MCSIMP,MCFACT,MCList

def entryPoint():
   """
       Retourne les informations n�cessaires pour le chargeur de plugins
       Ces informations sont retourn�es dans un dictionnaire
   """
   return {
        # Le nom du plugin
          'name' : 'ini',
        # La factory pour cr�er une instance du plugin
          'factory' : IniGenerator,
          }


class IniGenerator:
   """
       Ce generateur parcourt un objet de type MCFACT et produit
       un fichier au format ini 
       L'acquisition et le parcours sont r�alis�s par le m�thode
       generator.gener(objet_mcfact)
       L'�criture du fichier au format ini par appel de la m�thode
       generator.writefile(nom_fichier)

       Ses caract�ristiques principales sont expos�es dans des attributs 
       de classe :
         - extensions : qui donne une liste d'extensions de fichier pr�conis�es

   """
   # Les extensions de fichier pr�conis�es
   extensions=('.ini','.conf')

   def __init__(self,cr=None):
      # Si l'objet compte-rendu n'est pas fourni, on utilise le compte-rendu standard
      if cr :
         self.cr=cr
      else:
         self.cr=N_CR.CR(debut='CR generateur format ini',
                         fin='fin CR format ini')
      # Le texte au format ini est stock� dans l'attribut text
      self.text=''

   def writefile(self,filename):
      fp=open(filename,'w')
      fp.write(self.text)
      fp.close()

   def gener(self,obj,config=None):
      """
         Tous les mots-cl�s simples du niveau haut sont mis dans la section DEFAUT
         Tous les mots-cl�s facteurs sont convertis en sections
         Un mot-cl� facteur ne peut contenir que des mots-cl�s simples. Sinon => erreur
      """
      liste_mcfact=[]
      sect_defaut=''
      if isinstance(obj,MCList):
        if len(obj.data) > 1:
          raise EficasException(tr("Pas supporte"))
        else:
          obj=obj.data[0]

      for mocle in obj.mc_liste:
        if isinstance(mocle,MCList):
          if len(mocle.data) > 1:
            raise EficasException(tr("Pas supporte"))
          else:
            liste_mcfact.append(self.generMCFACT(mocle.data[0]))
        elif isinstance(mocle,MCFACT):
          liste_mcfact.append(self.generMCFACT(mocle))
        elif isinstance(mocle,MCSIMP):
          sect_defaut=sect_defaut+self.generMCSIMP(mocle)
        else:
          self.cr.fatal(tr("Entite inconnue ou interdite :%s",`mocle`))

      self.text=''
      if sect_defaut != '':
         self.text="[DEFAULT]\n"+sect_defaut
      self.text=self.text + string.join(liste_mcfact,'\n')
      return self.text

   def generMCFACT(self,obj):
      """
         Cette m�thode convertit un mot-cl� facteur ne contenant que des mots-cl�s
         simples en une chaine de caract�res
      """
      sect_text='[%s]\n' % obj.nom
      for mocle in obj.mc_liste:
         if isinstance(mocle,MCSIMP):
            sect_text=sect_text+self.generMCSIMP(mocle)
         else:
            self.cr.fatal(tr("Entite inconnue ou interdite :%s. Elle est ignoree",`mocle`))
      return sect_text

   def generMCSIMP(self,obj):
      """
         Cette m�thode convertit un mot-cl� simple en une chaine de caract�res
         au format ini
      """
      s=''
      if type(obj.valeur) == types.TupleType :
         self.cr.fatal(tr("Les tuples ne sont pas support�s pour le format ini :%s ", obj.nom))
         s="%s = %s\n" % (obj.nom,"ERREUR")
      else :
         try:
            s="%s = %s\n" % (obj.nom,obj.valeur)
         except Exception as e :
            self.cr.fatal(tr("Type de valeur non support� par le format ini :%(nom)s\n%(exception)s", \
                                         {'nom': obj.nom, 'exception': str(e)}))
      return s

