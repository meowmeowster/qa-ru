#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from read_env import read_env


def get_value(key):
    try:
        read_env()
        return os.environ[key]
    except FileNotFoundError:
        print("Dotenv file not found")
        return None
    except Exception:
        print("Other exception")
        return None
