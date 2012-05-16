# -*- coding: iso-8859-1 -*-
# Copyright (C) 2007-2012   EDF R&D
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

# Attention : cet import permet d'avoir, en Python, le comportement
# de la division r�elle pour les entiers, et non la division enti�re
# 1/2=0.5 (et non 0). Comportement par d�faut dans Python 3.0.
from __future__ import division

from N_ASSD import ASSD
from N_info import message, SUPERV

class FONCTION(ASSD):
    pass

class formule(ASSD):
    def __init__(self, *args, **kwargs):
        ASSD.__init__(self, *args, **kwargs)
        self.nompar = None
        self.expression = None
        ctxt = {}
        ctxt.update(getattr(self.parent, 'const_context', {}))
        ctxt.update(getattr(self.parent, 'macro_const_context', {}))
        self.parent_context = self.filter_context(ctxt)
        #message.debug(SUPERV, "add parent_context %s %s", self.nom, self.parent_context)

    def __call__(self, *val):
        """Evaluation de la formule"""
        from math import sin, cos, tan, asin, acos, atan2, atan, sinh, cosh, tanh
        from math import pi ,exp,log, log10, sqrt
        context = locals().copy()
        # en POURSUITE, self.parent_context is None, on essaie de reprendre const_context
        context.update(getattr(self, 'parent_context') \
                    or getattr(self.parent, 'const_context', {}))
        for param, value in zip(self.nompar, val):
            context[param] = value
        try:
            res = eval(self.expression, context)
        except Exception, exc:
            message.error(SUPERV, "ERREUR LORS DE L'�VALUATION DE LA FORMULE '%s' " \
                          ":\n>> %s",self.nom, str(exc))
            raise
        return res

    def setFormule(self, nom_para, texte):
        """Cette methode sert a initialiser les attributs
        nompar, expression et code qui sont utilis�s
        dans l'�valuation de la formule."""
        self.nompar = nom_para
        self.expression = texte
        try :
            self.code = compile(texte, texte, 'eval')
        except SyntaxError, exc:
            message.error(SUPERV, "ERREUR LORS DE LA CREATION DE LA FORMULE '%s' " \
                          ":\n>> %s", self.nom, str(exc))
            raise

    def __setstate__(self,state):
        """Cette methode sert a restaurer l'attribut code lors d'un unpickle."""
        self.__dict__.update(state)                   # update attributes
        self.setFormule(self.nompar, self.expression) # restore code attribute

    def __getstate__(self):
        """Pour les formules, il faut enlever l'attribut code qui n'est
        pas picklable."""
        d = ASSD.__getstate__(self)
        del d['code']
        return d

    def supprime(self, force=False):
        """
        Cassage des boucles de r�f�rences pour destruction du JDC.
        'force' est utilis�e pour faire des suppressions compl�mentaires.
        
        Pour �tre �valu�es, les formules ont besoin du contexte des "constantes"
        (objets autres que les concepts) qui sont soit dans (jdc).const_context,
        soit dans (macro).macro_const_context.
        On le stocke dans 'parent_context'.
        Deux pr�cautions valent mieux qu'une : on retire tous les concepts.
        
        Lors de la suppression du concept, 'supprime' est appel�e par
        'build_detruire' avec force=True afin de supprimer le "const_context"
        conserv�.
        """
        if force:
            for ctxt in ('parent_context', 'g_context'):
                if hasattr(self, ctxt):
                    setattr(self, ctxt, None)
        ASSD.supprime(self, force)

    def Parametres(self):
        """Equivalent de fonction.Parametres pour pouvoir utiliser des formules
        � la place de fonctions dans certaines macro-commandes.
        """
        from SD.sd_fonction import sd_formule
        from Utilitai.Utmess import UTMESS
        if self.accessible():
            TypeProl={ 'E':'EXCLU', 'L':'LINEAIRE', 'C':'CONSTANT', 'I':'INTERPRE' }
            sd = sd_formule(self.get_name())
            prol = sd.PROL.get()
            nova = sd.NOVA.get()
            if prol is None or nova is None:
                UTMESS('F', 'SDVERI_2', valk=[objev])
            dico={
                'INTERPOL'    : ['LIN','LIN'],
                'NOM_PARA'    : [s.strip() for s in nova],
                'NOM_RESU'    : prol[3][0:16].strip(),
                'PROL_DROITE' : TypeProl['E'],
                'PROL_GAUCHE' : TypeProl['E'],
            }
        else:
            raise Accas.AsException("Erreur dans fonction.Parametres en PAR_LOT='OUI'")
        return dico


class formule_c(formule):
    pass


