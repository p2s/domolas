#!/usr/bin/python3
# -*-coding:Utf-8 -*

import logging

logger = logging.getLogger('')

class Composant:
    """Classe abstraite comprenant la base des composants"""
    def __init__(self,pin,nom):
        """
        indiquer le nom du composant et le numéro de pin sur laquelle il est branché
        """
        self.pin = pin
        self.nom = nom
        logger.debug("Composant \"{}\" sur pin {}".format(self.nom, self.pin))
    def __str__(self):
        return "Composant \"{}\" branché sur la GPIO n° {}".format(self.nom, self.pin)
