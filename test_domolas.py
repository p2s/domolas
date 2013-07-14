#!/usr/bin/python3
# -*-coding:Utf-8 -*

import domolas.util.global_util as gu
import domolas.components as comp

def main():

    gu.logger.info('============================================================')
    gu.logger.info('Start Domolas')

    teleInfo = comp.TeleInfo(15)
    print ("TeleInfo HC = {}, HP = {}".format(teleInfo.indexHC, teleInfo.indexHP))
    teleInfo.save2DB();

    tempSensor = comp.TempHumi(17)
    print ("Temperature = {}, humidity = {}".format(tempSensor.temp, tempSensor.humidity))
    tempSensor.save2DB();
    gu.logger.info('Stop Domolas')

if __name__ == '__main__':
    main()
