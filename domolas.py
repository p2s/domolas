#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sqlite3
import log
from components import *

databasePath = "db"
def init():
    global conn
    global c
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()

logger = log.customLogger('')

def main():

    logger.info('============================================================')
    logger.info('Start Domolas')
    tempSensor = TempHumi(17)
    print ("Temperature = {}, humidity = {}".format(tempSensor.temp, tempSensor.humidity))
    print ("Temperature = {}, humidity = {}".format(tempSensor.temp, tempSensor.humidity))
    tempSensor1 = TempHumi(17)
    print ("Temperature = {}, humidity = {}".format(tempSensor1.temp, tempSensor1.humidity))
    print ("Temperature = {}, humidity = {}".format(tempSensor1.temp, tempSensor1.humidity))
    logger.info('Stop Domolas')

if __name__ == '__main__':
    main()
