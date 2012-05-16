# -*- coding: utf-8 -*-
# Copyright (C) 2007-2012   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

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
    
