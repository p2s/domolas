import logging
import logging.config

def customLogger(name):
    logging.config.fileConfig('conf/logging.conf')
    logger = logging.getLogger(name)
    return logger
