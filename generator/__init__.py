"""
   Ce package contient tous les g�n�rateurs de formats de sortie
   � partir des objets d' EFICAS.

   Ces g�n�rateurs sont impl�ment�s sous forme de plugins
"""

from Extensions import pluginloader

import generator

plugins=pluginloader.PluginLoader(generator)

