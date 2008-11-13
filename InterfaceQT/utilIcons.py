# -*- coding: utf-8 -*-

from qt import QPixmap
import os

class PixmapCache:
    """
    Class implementing a pixmap cache for icons.
    """
    def __init__(self):
        """
        Constructor
        """
        self.pixmapCache = {}

    def getPixmap(self, key):
        """
        Public method to retrieve a pixmap.
        
        @param key name of the wanted pixmap (string)
        @return the requested pixmap (QPixmap)
        """
        try:
            return self.pixmapCache[key]
        except KeyError:
            self.pixmapCache[key] = QPixmap.fromMimeSource(key)
            return self.pixmapCache[key]
            
pixCache = PixmapCache()

def getPixmap(key, cache = pixCache):
    """
    Module function to retrieve a pixmap.
    
    @param key name of the wanted pixmap (string)
    @return the requested pixmap (QPixmap)
    """
    return cache.getPixmap(key)
    
    

from qt import QMimeSourceFactory

def initializeMimeSourceFactory():
    """
    Function to initialize the default mime source factory.
    
    """
    defaultFactory = QMimeSourceFactory.defaultFactory()
    repini=os.path.dirname(os.path.abspath(__file__))
    defaultFactory.addFilePath(repini+"/../Editeur/icons") #CS_pbruno todo (config)
    
