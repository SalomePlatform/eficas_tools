# Management of EFICAS version numbering.
# A version has at least major and minor numbers, for easier comparison.

__version = {
    'major': 8,
    'minor': 2
    }

def getEficasVersion():
    """
    Return the EFICAS current version number.
    """
    return "%s.%s"%(getMajor(),getMinor())
#

def getSalomeVersion():
    """
    Return the SALOME version number to which current EFICAS version is related.
    """
    return getEficasVersion()
#

def getMajor():
    return __version['major']
#

def getMinor():
    return __version['minor']
#

def getBaseVersion():
    """
    Returns [ major, minor ] array of integers.
    """
    return [ getMajor(), getMinor() ]
#
