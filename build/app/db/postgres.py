#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import os
from auth import safe
from log_service import set_logs


logger = set_logs()


def connect(hostname):
    db_app = safe.get_value('DB_APP')
    db_user = safe.get_value('DB_USER')
    db_password = safe.get_value('DB_PASSWORD')
    db_port = safe.get_value('DB_LOCAL_PORT')
    try:
        conn = psycopg2.connect(dbname=db_app, user=db_user,
                                password=db_password, host=hostname, port=db_port)
        logger.info("Connected to the database!")
        return conn
    except psycopg2.OperationalError:
        logger.error("Failed connecting to the database on" + hostname + ": " + db_port)
        return None
    except IndentationError:
        logger.error("Failed to connect with current credentials")
        return None


def execute_sql(conn, addr):
    cursor = conn.cursor()
    conn.autocommit = True

    workdir = addr
    for file in os.listdir(workdir):
        if file.endswith(".sql"):
            cursor.execute(open(workdir+file).read())


def cleanup(conn):
    try:
        execute_sql(conn, "./db/ddl/drop/")
    except psycopg2.Error:
        logger.error("Unable to drop all schemas")


def construct(conn):
    execute_sql(conn, "./db/ddl/create/")


def fill(conn):
    execute_sql(conn, "./db/initial/insert/")


def conn_close(conn):
    cursor = conn.cursor()
    cursor.close()
    conn.close()
