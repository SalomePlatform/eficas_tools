# -*- coding: utf-8 -*-

import re
from compiler import visitor

class MatchFinder:
    """Visiteur de base : gestion des matches """
    def reset(self,line):
        self.matches = []
        self.words = re.split("(\w+)", line) # every other one is a non word
        self.positions = []
        i = 0
        for word in self.words:
            self.positions.append(i)
            i+=len(word)
        self.index = 0

    def popWordsUpTo(self, word):
        if word == "*":
            return        # won't be able to find this
        posInWords = self.words.index(word)
        idx = self.positions[posInWords]
        self.words = self.words[posInWords+1:]
        self.positions = self.positions[posInWords+1:]

    def appendMatch(self,name):
        idx = self.getNextIndexOfWord(name)
        self.matches.append((idx, name))

    def getNextIndexOfWord(self,name):
        return self.positions[self.words.index(name)]


class KeywordFinder(MatchFinder):
    """Visiteur pour les keywords d'une commande """

    def visitKeyword(self,node):
        idx = self.getNextIndexOfWord(node.name)
        #self.appendMatch(node.name)
        self.popWordsUpTo(node.name)
        prevmatches=self.matches
        self.matches = []
        for child in node.getChildNodes():
            self.visit(child)
        prevmatches.append((idx, node.name,self.matches))
        self.matches=prevmatches

    def visitTuple(self,node):
        matchlist=[]
        for child in node.getChildNodes():
            self.matches = []
            self.visit(child)
            if self.matches:
                #Pour eviter les tuples et listes ordinaires, on ne garde que les visites fructueuses
                matchlist.append(self.matches)
        self.matches=matchlist

    visitList=visitTuple

    def visitName(self,node):
        self.popWordsUpTo(node.name)
    def visitAssName(self,node):
        self.popWordsUpTo(node.name)
