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
        #logger.info("Connected to the database!")
        return conn
    except psycopg2.OperationalError:
        #logger.error("Failed connecting to the database on" + hostname + ": " + db_port)
        return None
    except IndentationError:
        #logger.error("Failed to connect with current credentials")
        return None


def execute_sql(conn, address, catalog=True, getresult=False):
    result = []
    cursor = conn.cursor()
    conn.autocommit = True
    work_dir = address
    #logger.debug("Executing SQL files at " + address)
    if catalog:
        #logger.debug("Directory mode")
        for file in os.listdir(work_dir):
            if file.endswith(".sql"):
                cursor.execute(open(work_dir + file).read())
                if getresult:
                    result.append(cursor.fetchall())
    else:
        #logger.debug("Single file mode")
        cursor.execute(open(work_dir).read())
        if getresult:
            result.append(cursor.fetchall())
    if getresult:
        #logger.debug("Requested script result")
        return result


def cleanup(conn):
    try:
        execute_sql(conn, "./db/ddl/drop/")
    except psycopg2.Error:
        print("Unable to drop all schemas")
        #logger.error("Unable to drop all schemas")


def construct(conn):
    execute_sql(conn, "./db/ddl/create/")


def fill(conn):
    execute_sql(conn, "./db/initial/insert/")


def read_sql(conn, string, catalog):
    return execute_sql(conn, string, catalog, True)


def conn_close(conn):
    cursor = conn.cursor()
    cursor.close()
    conn.close()
