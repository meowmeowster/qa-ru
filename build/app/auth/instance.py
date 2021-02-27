#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def db_host():
    workdir = "/"
    for file in os.listdir(workdir):
        if file.endswith(".dockerenv"):
            return "database"
    return "localhost"
