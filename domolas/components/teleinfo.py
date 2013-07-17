#!/usr/bin/python3
# -*-coding:Utf-8 -*

import util.global_util as gu

import re
import time
import logging
from . import component
import serial
import string



class TeleInfo(component.Component):
    """
    This class handle TeleInfo entry
    for more informations about TeleInfo see:
        http://vesta.homelinux.free.fr/site/wiki/demodulateur_teleinformation_edf.html#D.C3.A9tail_des_trames_t.C3.A9l.C3.A9information
    """

    nbTeleInfoSensor = 0

    def __init__(self,pin):
        """
        Require the component pin number
        """

        component.Component.__init__(self, pin, "TeleInfo n° {}".format(TeleInfo.nbTeleInfoSensor))
        TeleInfo.nbTeleInfoSensor += 1
        self._ageMax = 1000 #on indique l'age maximum de la valeur = 1000 ms
        self._eMeasure = time.time() - self._ageMax - 10
        self._HP = 0
        self._HC = 0
        gu.logger.debug("creation TeleInfo named \"{}\" on pin {}".format(self.nom, self.pin))

    def readValue(self):
        """
        Read teleinfo values
        stock values in property
        """

        self._ser = serial.Serial(  port='/dev/ttyAMA0',
                  baudrate=1200,
                  parity=serial.PARITY_EVEN,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.SEVENBITS)
        valuesRead = set()
        tempCt = 0
        prevSetLength = 0
        while tempCt < 3:
            if (len(valuesRead) > 0) and (len(valuesRead) == prevSetLength):
                tempCt += 1
            else:
                tempCt = 0
            prevSetLength = len(valuesRead)

            tiLine = str(self._ser.readline(), "utf-8")
            print("set len = {} // read {}".format(len(valuesRead), tiLine))
            if (tiLine.find('ADCO ') == 0):
                if (tiLine[5:17].isdigit() == True):
                    self._idMeter = int(tiLine[5:17])
                    valuesRead.add("_idMeter")
            if (tiLine.find('OPTARIF ') == 0):
                self._opTarif = tiLine[8:10]
                valuesRead.add("_opTarif")
            if (tiLine.find('ISOUSC ') == 0):
                if (tiLine[7:9].isdigit() == True):
                    self._iSousc = int(tiLine[7:9])
                    valuesRead.add("_iSousc")
            if (tiLine.find('HCHC ') == 0):
                if (tiLine[5:14].isdigit() == True):
                    self._indexHC = int(tiLine[5:14])
                    valuesRead.add("_indexHC")
            if (tiLine.find('HCHP ') == 0):
                if (tiLine[5:14].isdigit() == True):
                    self._indexHP = int(tiLine[5:14])
                    valuesRead.add("_indexHP")
            if (tiLine.find('PTEC ') == 0):
                self._pTarif = tiLine[5:7]
                valuesRead.add("_pTarif")
            if (tiLine.find('IINST ') == 0):
                if (tiLine[6:9].isdigit() == True):
                    self._iInst = int(tiLine[6:9])
                    valuesRead.add("_iInst")
            if (tiLine.find('IMAX ') == 0):
                if (tiLine[5:8].isdigit() == True):
                    self._iMax = int(tiLine[5:8])
                    valuesRead.add("_iMax")
            #if (tiLine.find('HHPHC ') == 0):
            #    self._pTarif = tiLine[6:7]
            #    valuesRead.add("_pTarif")


        self._eMeasure = time.time()

        gu.logger.debug("HP: {} WH ".format(self._indexHP))
        gu.logger.debug("HC: {} WH ".format(self._indexHC))

    @property
    def indexHP(self):
        """
        return the actual temperature
        if the temp property is older than ageMax, the readValue method is called
        """
        #gu.logger.debug("[getTemp]time({}) -._eMeasure({}) = {} > _ageMax({})".format(time.time(), self._eMeasure, time.time() - self._eMeasure, self._ageMax))
        if (time.time() - self._eMeasure > self._ageMax):
            self.readValue()

        return self._indexHP

    @property
    def indexHC(self):
        """
        return the actual humidity
        if the humidity property is older than ageMax, the readValue method is called
        """
        if (time.time() - self._eMeasure > self._ageMax):
            self.readValue()

        return self._indexHC

    @property
    def periode(self):
        """
        return the actual humidity
        if the humidity property is older than ageMax, the readValue method is called
        """
        if (time.time() - self._eMeasure > self._ageMax):
            self.readValue()

        return self._pTarif

    @property
    def iInst(self):
        """
        return the actual humidity
        if the humidity property is older than ageMax, the readValue method is called
        """
        if (time.time() - self._eMeasure > self._ageMax):
            self.readValue()

        return self._iInst


    def save2DB(self):
        sql = "INSERT INTO {} (`name`, `indexHP`, `indexHC`, `periode`, `iInst`, `time`) VALUES ({},{},{},'{}',{},{})".format(gu.cfg['DEFAULT']['DBTeleInfoName'], self.nbTeleInfoSensor, self.indexHP, self.indexHC, self.periode, self.iInst, time.time())
        print("save2DB teleingo = {}".format(sql))
        gu.logger.debug("[save2DB][{}]".format(sql))
        super().save2DB(sql)

