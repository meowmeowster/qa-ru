#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import datetime
import coloredlogs


def set_logs():
    logging.basicConfig(filename="./logs/"+str(datetime.date.today())+".log", level=logging.DEBUG)
    logger_init = logging.getLogger(__name__)
    coloredlogs.install()
    return logger_init
