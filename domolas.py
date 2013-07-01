#!/usr/bin/python3
# -*-coding:Utf-8 -*

import log
from composants import *

def main():
    logger = log.customLogger('')

    logger.info('============================================================')
    logger.info('Démarrage Domolas')
    captTemp = TempHumi(17)
    print ("Température recuperée = {}, humidite = {}".format(captTemp.temp, captTemp.humidite))
    print ("Température recuperée = {}, humidite = {}".format(captTemp.temp, captTemp.humidite))
    captTemp1 = TempHumi(17)
    print ("Température recuperée = {}, humidite = {}".format(captTemp1.temp, captTemp1.humidite))
    print ("Température recuperée = {}, humidite = {}".format(captTemp1.temp, captTemp1.humidite))
    logger.info('Arret Domolas')

if __name__ == '__main__':
    main()
