#!/usr/bin/python3
# -*-coding:Utf-8 -*

import subprocess
import re
import sys
import time
import logging
from . import composant


logger = logging.getLogger('')

class TempHumi(composant.Composant):
    """
    Cette classe gere le capteur de température et d'humidité AM2303
    Il lis les infos à partir d'un programm en C disponible ici :
    http://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logger/software-install
    """

    nbCapteurTemp = 0

    def __init__(self,pin):
        """
        indiquer le numéro de pin sur laquelle la pate du composant est branché
        """

        composant.Composant.__init__(self, pin, "capteur t° n° {}".format(TempHumi.nbCapteurTemp))
        TempHumi.nbCapteurTemp += 1
        self._ageMax = 5000 #on indique l'age maximum de la valeur = 5000 ms
        self._timeMesure = time.time() - self._ageMax - 10
        self._temp = 0
        self._humidite = 0
        logger.debug("création capteur de température et humidité  \"{}\" sur pin {}".format(self.nom, self.pin))

    def lireValeur(self):
        """
        Lis les valeurs de la température et de l'humidité
        les données sont stockées en attributs
        """
        output = subprocess.check_output(["./Adafruit_DHT", "2302", "{}".format(self.pin)]);
        logger.debug("trame lireValeur = {}".format(output))

        matches = re.search(b"Temp =\s+([0-9.]+)", output)
        if (not matches):
            logger.debug("[lireValeur][temp not match]")
            time.sleep(3)
            self.lireValeur()
            return
        self._temp = float(matches.group(1))

        # search for humidity printout
        matches = re.search(b"Hum =\s+([0-9.]+)", output)
        if (not matches):
            logger.debug("[lireValeur][humidite not match]")
            time.sleep(3)
            self.lireValeur()
            return
        self._humidite = float(matches.group(1))

        self._timeMesure = time.time()

        logger.debug("Temperature: %.1f C" % self._temp)
        logger.debug("Humidité:    %.1f %%" % self._humidite)

    @property
    def temp(self):
        """
        renvoit la température actuelle
        si la derniere mesure est plus vielle que l'ageMax on relis les valeurs
        """
        #logger.debug("[getTemp]time({}) - _timeMesure({}) = {} > _ageMax({})".format(time.time(), self._timeMesure, time.time() - self._timeMesure, self._ageMax))
        if (time.time() - self._timeMesure > self._ageMax):
            self.lireValeur()

        return self._temp

    @property
    def humidite(self):
        """
        renvoit l'humidité actuelle
        si la derniere mesure est plus vielle que l'ageMax on relis les valeurs
        """
        if (time.time() - self._timeMesure > self._ageMax):
            self.lireValeur()

        return self._humidite




