"""
   Ce package contient tous les convertisseurs de formats d'entrée
   en objets compréhensibles par EFICAS.

   Ces convertisseurs sont implémentés sous forme de plugins
"""

from Extensions import pluginloader

import convert

plugins=pluginloader.PluginLoader(convert)

