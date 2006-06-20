# -*- coding: utf-8 -*-

import re

def indexToCoordinates(src, index):
    """return le numero de la colonne (x) et le numero de la ligne (y) dans src"""
    y = src[: index].count("\n")
    startOfLineIdx = src.rfind("\n", 0, index)+1
    x = index-startOfLineIdx
    return x, y

def linetodict(line):
    """Transforme une ligne (string) en un dictionnaire de mots repérés par le numéro de la colonne"""

    words = re.split("(\w+)", line)
    h = {};i = 0
    for word in words:
        h[i] = word
        i+=len(word)
    return h

def dicttoline(d):
    """Transformation inverse: à partir d'un dictionnaire retourne une ligne"""
    cols = d.keys()
    cols.sort()
    return "".join([d[colno]for colno in cols])
