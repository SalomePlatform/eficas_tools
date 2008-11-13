# -*- coding: utf-8 -*-

from PyQt4.QtGui import QPixmap, QIcon
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
        if (1==1):
        #try:
            key="/local/pnoyret/Install_Eficas/EficasV1/InterfaceQT/icons/"+key
            return QPixmap(key)
            #return self.pixmapCache[key]
        #except KeyError:
        else :
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
    
def getIcon(key):
    key="/local/pnoyret/Install_Eficas/EficasV1/InterfaceQT/icons/"+key
    return QIcon(key)
    

#from PyQt4.Qt3Support import Q3MimeSourceFactory

#def initializeMimeSourceFactory():
    """
    Function to initialize the default mime source factory.
    
    """
#    defaultFactory = Q3MimeSourceFactory.defaultFactory()
#    repini=os.path.dirname(os.path.abspath(__file__))
#    defaultFactory.addFilePath(repini+"/../Editeur/icons") #CS_pbruno todo (config)
    
