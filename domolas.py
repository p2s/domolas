#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sqlite3
import configparser
from log import log
from components import *

configFile = "conf/domolas.ini"

cfg = None
c = None
conn = None

def init():
    global cfg
    cfg = configparser.ConfigParser()
    cfg.read(configFile)
    logger.debug("config read BasePath = {}".format(cfg['DEFAULT']['BasePath']))

    global c
    global conn
    conn = sqlite3.connect(cfg['DEFAULT']['DBPath'])
    c = conn.cursor()

logger = log.customLogger('')

def main():

    logger.info('============================================================')
    logger.info('Start Domolas')

    init()

    tempSensor = TempHumi(17)
    print ("Temperature = {}, humidity = {}".format(tempSensor.temp, tempSensor.humidity))
    tempSensor.save2DB(c, conn);
    logger.info('Stop Domolas')

if __name__ == '__main__':
    main()
