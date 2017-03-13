from __future__ import absolute_import
from __future__ import print_function
try :
   from builtins import object
except : pass

import os

class envQT(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(envQT, cls).__new__(
                                cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        if hasattr(self,'inQt5') : return
        if 'PYQT_ROOT_DIR' in os.environ: qt=os.environ['PYQT_ROOT_DIR']
        else : qt="Pyqt4"
        if 'Pyqt-5' in qt : self.inQt5=True
        else              : self.inQt5=False


monEnvQT5=envQT().inQt5
if __name__=='__main__':
     inQt5_1=envQT().inQt5
     inQt5_2=envQT().inQt5
     print (inQt5_1)
