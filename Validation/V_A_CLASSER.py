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



from __future__ import print_function
from __future__ import absolute_import
try :
  from builtins import str
  from builtins import object
except : 
  pass

class A_CLASSER(object):

    """
       La regle A_CLASSER verifie que ...

    """

    def __init__(self, *args):
        if len(args) > 2:
            print ("Erreur a la creation de la regle A_CLASSER(%s)" % str(args))
            return
        self.args = args
        if type(args[0]) == tuple: self.args0 = args[0]
        elif type(args[0]) == str: self.args0 = (args[0],)
        else:
            print ( "Le premier argument de : %s doit etre un tuple ou une chaine" % str(args))
        if type(args[1]) == tuple:
            self.args1 = args[1]
        elif type(args[1]) == str:
            self.args1 = (args[1],)
        else:
            print ("Le deuxieme argument de : %s doit etre un tuple ou une chaine" % str(args))
        # creation de la liste des mcs
        liste = []
        liste.extend(self.args0)
        liste.extend(self.args1)
        self.mcs = liste
        self.init_couples_permis()

    def init_couples_permis(self):
        """ Cree la liste des couples permis parmi les self.args, cad pour chaque element
            de self.args0 cree tous les couples possibles avec un element de self.args1"""
        liste = []
        for arg0 in self.args0:
            for arg1 in self.args1:
                liste.append((arg0, arg1))
        self.liste_couples = liste

    def verif(self, args):
        """
            args peut etre un dictionnaire ou une liste. Les elements de args
            sont soit les elements de la liste soit les cles du dictionnaire.
        """
        # creation de la liste des couples presents dans le fichier de
        # commandes
        l_couples = []
        couple = []
        text = u''
        test = 1
        for nom in args:
            if nom in self.mcs:
                couple.append(nom)
                if len(couple) == 2:
                    l_couples.append(tuple(couple))
                    couple = [nom, ]
        if len(couple) > 0:
            l_couples.append(tuple(couple))
        # l_couples peut etre vide si l'on n'a pas reussi a trouver au moins un
        # element de self.mcs
        if len(l_couples) == 0:
            message = "- Il faut qu'au moins un objet de la liste : %s  soit suivi d'au moins un objet de la liste %s : " % (self.args0,self.args1)
            return message, 0
        # A ce stade, on a trouve des couples : il faut verifier qu'ils sont
        # tous licites
        num = 0
        for couple in l_couples:
            num = num + 1
            if len(couple) == 1:
                # on a un 'faux' couple
                if couple[0] not in self.args1:
                    text = text + "- L'objet : %s doit etre suivi d'un objet de la liste : %r\n" %(couple[0], self.args1)
                    test = 0
                else:
                    if num > 1:
                        # ce n'est pas le seul couple --> licite
                        break
                    else:
                        text = text + "- L'objet : %s doit etre precede d'un objet de la liste : %r\n" %(couple[0], self.args0)
                        test = 0
            elif couple not in self.liste_couples:
                text = text + "- L'objet : %s ne peut etre suivi de : %s\n" %(couple[0], couple[1])
                test = 0
        return text, test
