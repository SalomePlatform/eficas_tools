# -*- coding: utf-8 -*-

import logging
logger=logging.getLogger()

def initialise() :
    hdlr=logging.FileHandler('/tmp/convert.log','w')
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.INFO)
    return hdlr


def ferme (hdlr) :
    logger.removeHandler(hdlr)
