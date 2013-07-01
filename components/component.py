#!/usr/bin/python3
# -*-coding:Utf-8 -*

import logging

logger = logging.getLogger('')

class Component:
    """components base"""
    def __init__(self,pin,nom):
        """
        specify the component name and his pin number
        """
        self.pin = pin
        self.nom = nom
        logger.debug("\"{}\" component on pin {}".format(self.nom, self.pin))
    def __str__(self):
        return "\"{}\" component plugged on GPIO n° {}".format(self.nom, self.pin)

    def save2DB(self):
        """
        allow to save object data to sql base (sqlite by default)
        """

