#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from read_env import read_env
import logging
import datetime


logging.basicConfig(filename="./logs/"+str(datetime.date.today())+".log", level=logging.DEBUG)


def get_value(key):
    try:
        read_env()
        return os.environ[key]
    except FileNotFoundError:
        logging.error("Dotenv file not found")
        return None
    except Exception:
        logging.error("Other exception")
        return None
