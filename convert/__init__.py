"""
   Ce package contient tous les convertisseurs de formats d'entr�e
   en objets compr�hensibles par EFICAS.

   Ces convertisseurs sont impl�ment�s sous forme de plugins
"""

from Extensions import pluginloader

import convert

plugins=pluginloader.PluginLoader(convert)

