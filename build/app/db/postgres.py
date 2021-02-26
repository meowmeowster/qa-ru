#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
from auth import safe
import logging
import datetime


def connect():
    db_app = safe.get_value('DB_APP')
    db_user = safe.get_value('DB_USER')
    db_password = safe.get_value('DB_PASSWORD')
    db_local_port = safe.get_value('DB_LOCAL_PORT')

    conn = psycopg2.connect(dbname=db_app, user=db_user,
                            password=db_password, host="localhost", port=db_local_port)
    cursor = conn.cursor()
