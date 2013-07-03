#!/usr/bin/python3
# -*-coding:Utf-8 -*

import logging

logger = logging.getLogger('')

d_temphumi = "CREATE TABLE IF NOT EXISTS d_temphumi (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), temp INTEGER, humidity INTEGER, time TIMESTAMP);"


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

    def save2DB(self, c, conn, sql):
        """
        allow to save object data to sql base (sqlite by default)
        execute sql query on domolas db
        """

        c.execute(d_temphumi)

        c.execute(sql)
        conn.commit()

