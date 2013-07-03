#!/usr/bin/python3
# -*-coding:Utf-8 -*

import util.global_util as gu

import subprocess
import re
import sys
import time
import logging
from . import component

dbTableName = "d_temphumi"

class TempHumi(component.Component):
    """
    This class handle the temperature and humidity sensor
    It handle AM2303 based component.
    It required a C program to read data, you can find info about it at this location :
    http://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logger/software-install
    """

    nbTempSensor = 0

    def __init__(self,pin):
        """
        Require the component pin number
        """

        component.Component.__init__(self, pin, "t° sensor n° {}".format(TempHumi.nbTempSensor))
        TempHumi.nbTempSensor += 1
        self._ageMax = 5000 #on indique l'age maximum de la valeur = 5000 ms
        self._timeMeasure = time.time() - self._ageMax - 10
        self._temp = 0
        self._humidity = 0
        gu.logger.debug("creation temperature and humidity sensor named \"{}\" on pin {}".format(self.nom, self.pin))

    def readValue(self):
        """
        Read temperature and humidity values
        stock values in property
        """
        #global cfg
        print("config check : {}".format(gu.cfg['DEFAULT']['BasePath']))
        output = subprocess.check_output([gu.cfg['DEFAULT']['TempSensorBinFullPath'], gu.cfg['DEFAULT']['TempSensorModel'], "{}".format(self.pin)]);
        gu.logger.debug("trame readValue = {}".format(output))

        matches = re.search(b"Temp =\s+([0-9.]+)", output)
        if (not matches):
            gu.logger.debug("[readValue][temp not match]")
            time.sleep(3)
            self.readValue()
            return
        self._temp = float(matches.group(1))

        # search for humidity printout
        matches = re.search(b"Hum =\s+([0-9.]+)", output)
        if (not matches):
            gu.logger.debug("[readValue][humidite not match]")
            time.sleep(3)
            self.readValue()
            return
        self._humidity = float(matches.group(1))

        self._timeMeasure = time.time()

        gu.logger.debug("Temperature: %.1f C" % self._temp)
        gu.logger.debug("Humidity:    %.1f %%" % self._humidity)

    @property
    def temp(self):
        """
        return the actual temperature
        if the temp property is older than ageMax, the readValue method is called
        """
        #gu.logger.debug("[getTemp]time({}) - _timeMeasure({}) = {} > _ageMax({})".format(time.time(), self._timeMeasure, time.time() - self._timeMeasure, self._ageMax))
        if (time.time() - self._timeMeasure > self._ageMax):
            self.readValue()

        return self._temp

    @property
    def humidity(self):
        """
        return the actual humidity
        if the humidity property is older than ageMax, the readValue method is called
        """
        if (time.time() - self._timeMeasure > self._ageMax):
            self.readValue()

        return self._humidity

    def save2DB(self):
        sql = "INSERT INTO {} (name, temp, humidity, time) VALUES ({},{},{},{})".format(gu.cfg['DEFAULT']['DBTempHumiName'], self.nbTempSensor, self.temp, self.humidity, time.time())
        gu.logger.debug("[save2DB][{}]".format(sql))
        super().save2DB(sql)




