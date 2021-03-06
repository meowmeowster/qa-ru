#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from read_env import read_env
import logging
from log_service import set_logs


logger = set_logs()


def get_value(key):
    try:
        read_env()
        return os.environ[key]
    except FileNotFoundError:
        #logger.error("Dotenv file not found")
        return None
    except Exception:
        #logging.error("Other exception")
        return None
