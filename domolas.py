#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sqlite3
from log import log
from components import *

databasePath = "/home/pi/dev/domolas/db/domolas.db"
def init():
    global c
    global conn
    conn = sqlite3.connect(databasePath)
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
