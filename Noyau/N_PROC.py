# -*- coding: iso-8859-1 -*-
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
    Ce module contient la classe de definition PROC
    qui permet de sp�cifier les caract�ristiques d'une proc�dure
"""

import types,string,traceback

import N_ENTITE
import N_PROC_ETAPE
from strfunc import ufmt

class PROC(N_ENTITE.ENTITE):
   """
    Classe pour definir un op�rateur

    Cette classe a deux attributs de classe

    - class_instance qui indique la classe qui devra etre utilis�e
            pour cr�er l'objet qui servira � controler la conformit� d'un
            op�rateur avec sa d�finition

    - label qui indique la nature de l'objet de d�finition (ici, PROC)


    et les attributs d'instance suivants :

    - nom   : son nom

    - op   : le num�ro d'op�rateur

    - reentrant : vaut 'n' ou 'o'. Indique si l'op�rateur est r�entrant ou pas. Un op�rateur
                        r�entrant peut modifier un concept d'entr�e et le produire comme concept de sortie

    - repetable : vaut 'n' ou 'o'. Indique si l'op�rateur est r�petable ou pas. Un op�rateur
                        non r�p�table ne doit apparaitre qu'une fois dans une ex�cution. C'est du ressort
                        de l'objet g�rant le contexte d'ex�cution de v�rifier cette contrainte.

    - fr   : commentaire associ� en francais

    - ang : commentaire associ� en anglais

    - docu : cl� de documentation associ�e

    - regles : liste des r�gles associ�es

    - op_init : cet attribut vaut None ou une fonction. Si cet attribut ne vaut pas None, cette
                      fonction est ex�cut�e lors des phases d'initialisation de l'�tape associ�e.

    - niveau : indique le niveau dans lequel est rang� l'op�rateur. Les op�rateurs peuvent etre
                     rang�s par niveau. Ils apparaissent alors exclusivement dans leur niveau de rangement.
                     Si niveau vaut None, l'op�rateur est rang� au niveau global.

    - entites : dictionnaire dans lequel sont stock�s les sous entit�s de l'op�rateur. Il s'agit
                      des entit�s de d�finition pour les mots-cl�s : FACT, BLOC, SIMP. Cet attribut
                      est initialis� avec args, c'est � dire les arguments d'appel restants.


   """
   class_instance = N_PROC_ETAPE.PROC_ETAPE
   label = 'PROC'

   def __init__(self,nom,op,reentrant='n',repetable='o',fr="",ang="",
                docu="",regles=(),op_init=None,niveau = None,UIinfo=None,**args):
      """
         M�thode d'initialisation de l'objet PROC. Les arguments sont utilis�s pour initialiser
         les attributs de meme nom
      """
      self.nom=nom
      self.op=op
      self.reentrant=reentrant
      self.repetable = repetable
      self.fr=fr
      self.ang=ang
      self.docu=docu
      if type(regles)== types.TupleType:
          self.regles=regles
      else:
          self.regles=(regles,)
      # Attribut op_init : Fonction a appeler a la construction de l operateur sauf si == None
      self.op_init=op_init
      self.entites=args
      current_cata=CONTEXT.get_current_cata()
      if niveau == None:
         self.niveau=None
         current_cata.enregistre(self)
      else:
         self.niveau=current_cata.get_niveau(niveau)
         self.niveau.enregistre(self)
      self.UIinfo=UIinfo
      self.affecter_parente()
      self.check_definition(self.nom)

   def __call__(self,**args):
      """
          Construit l'objet PROC_ETAPE a partir de sa definition (self),
          puis demande la construction de ses sous-objets et du concept produit.
      """
      etape= self.class_instance(oper=self,args=args)
      etape.McBuild()
      return etape.Build_sd()

   def make_objet(self,mc_list='oui'):
      """
           Cette m�thode cr�e l'objet PROC_ETAPE dont la d�finition est self sans
            l'enregistrer ni cr�er sa sdprod.
           Si l'argument mc_list vaut 'oui', elle d�clenche en plus la construction
           des objets MCxxx.
      """
      etape= self.class_instance(oper=self,args={})
      if mc_list == 'oui':etape.McBuild()
      return etape

   def verif_cata(self):
      """
          M�thode de v�rification des attributs de d�finition
      """
      self.check_regles()
      self.check_fr()
      self.check_reentrant()
      self.check_docu()
      self.check_nom()
      self.check_op(valmin=0)
      self.verif_cata_regles()

   def supprime(self):
      """
          M�thode pour supprimer les r�f�rences arri�res susceptibles de provoquer
          des cycles de r�f�rences
      """
      self.niveau=None


