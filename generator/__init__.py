"""
   Ce package contient tous les générateurs de formats de sortie
   à partir des objets d' EFICAS.

   Ces générateurs sont implémentés sous forme de plugins
"""

from Extensions import pluginloader

import generator

plugins=pluginloader.PluginLoader(generator)

