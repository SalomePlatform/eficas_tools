# -*- coding: utf-8 -*-

import logging
logger=logging.getLogger()
hdlr=logging.FileHandler('convert.log','w')
#formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
formatter = logging.Formatter('%(levelname)s: %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)
