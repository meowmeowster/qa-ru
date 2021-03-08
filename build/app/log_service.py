#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import datetime
import coloredlogs


def set_logs():
    try:
        logging.basicConfig(filename="./logs/"+str(datetime.date.today())+".log", level=logging.DEBUG)
        logger_init = logging.getLogger(__name__)
        coloredlogs.install()
        return logger_init
    except FileNotFoundError:
        print("Can't write file")
        return None
