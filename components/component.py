#!/usr/bin/python3
# -*-coding:Utf-8 -*
import util.global_util as gu

d_temphumi = "CREATE TABLE IF NOT EXISTS d_temphumi (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), temp INTEGER, humidity INTEGER, time TIMESTAMP);"


class Component:
    """components base"""
    def __init__(self,pin,nom):
        """
        specify the component name and his pin number
        """
        self.pin = pin
        self.nom = nom
        gu.logger.debug("\"{}\" component on pin {}".format(self.nom, self.pin))
    def __str__(self):
        return "\"{}\" component plugged on GPIO n° {}".format(self.nom, self.pin)

    def save2DB(self, sql):
        """
        allow to save object data to sql base (sqlite by default)
        execute sql query on domolas db
        """

        gu.c.execute(d_temphumi)

        gu.c.execute(sql)
        gu.conn.commit()

