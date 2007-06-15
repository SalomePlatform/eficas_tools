# -*- coding: utf-8 -*-

import logging
import os
logger=logging.getLogger()

def initialise(flog=None):
    if flog == None : 
          MonHome=os.environ['HOME']
          MaDir=MonHome+"/Eficas_install"
          try :
            os.mkdir(MaDir)
          except :
            pass
          try :
            os.listdir(MaDir)
            flog=MaDir+"/convert.log"
          except :
            flog='/tmp/convert.log'

    hdlr=logging.FileHandler(flog,'w')
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.INFO)
    return hdlr


def ferme (hdlr) :
    logger.removeHandler(hdlr)
