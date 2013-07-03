#!/usr/bin/python3
# -*-coding:Utf-8 -*

import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("current working director = {}".format(os.getcwd()))
sys.path.insert(0,parentdir)
from log import log

import sqlite3
import configparser

global logger
logger = log.customLogger('')

configFile = parentdir + "/conf/domolas.ini"

global cfg
cfg = configparser.ConfigParser()
cfg.read(configFile)
logger.debug("config read BasePath = {}".format(cfg['DEFAULT']['BasePath']))

global c
global conn
conn = sqlite3.connect(cfg['DEFAULT']['DBPath'])
c = conn.cursor()

