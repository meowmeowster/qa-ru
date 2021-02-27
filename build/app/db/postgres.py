#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
from auth import safe
from log_service import set_logs


logger = set_logs()


def connect():
    db_app = safe.get_value('DB_APP')
    db_user = safe.get_value('DB_USER')
    db_password = safe.get_value('DB_PASSWORD')
    db_local_port = safe.get_value('DB_LOCAL_PORT')
    try:
        conn = psycopg2.connect(dbname=db_app, user=db_user,
                                password=db_password, host="localhost", port=db_local_port)
        cursor = conn.cursor()
        logger.info("Connected to the database!")
        return cursor
    except psycopg2.OperationalError:
        logger.error("Failed connecting to the database on localhost:"+db_local_port)
        return None
    except IndentationError:
        logger.error("Failed to connect with current credentials")
        return None
