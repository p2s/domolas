import logging
import logging.config

def customLogger(name):
    logging.config.fileConfig('/home/pi/dev/domolas/conf/logging.conf')
    logger = logging.getLogger(name)
    return logger
