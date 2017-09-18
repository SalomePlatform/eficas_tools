# coding=utf-8
# person_in_charge: mathieu.courtois at edf.fr
# ======================================================================
# COPYRIGHT (C) 1991 - 2017  EDF R&D                  WWW.CODE-ASTER.ORG
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


from __future__ import absolute_import
try : 
   from builtins import object
except : pass

class AU_MOINS_UN(object):

    """
       La regle AU_MOINS_UN verifie que l'on trouve au moins un des mots-cles
       de la regle parmi les arguments d'un OBJECT.

       Ces arguments sont transmis a la regle pour validation sous la forme
       d'une liste de noms de mots-cles ou d'un dictionnaire dont
       les cles sont des noms de mots-cles.
    """

    def verif(self, args):
        """
            La methode verif verifie que l'on trouve au moins un des mos-cles
            de la liste self.mcs parmi les elements de args

            args peut etre un dictionnaire ou une liste. Les elements de args
            sont soit les elements de la liste soit les cles du dictionnaire.
        """
        #  on compte le nombre de mots cles presents
        text = ''
        count = 0
        args = self.liste_to_dico(args)
        for mc in self.mcs:
            if mc in args :
                count = count + 1
        if count == 0:
            text = "- Il faut au moins un mot-cle parmi : " + repr(self.mcs)+'\n'
            return text, 0
        return text, 1
