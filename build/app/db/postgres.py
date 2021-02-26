#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2


conn = psycopg2.connect(dbname='database', user='db_user',
                        password='mypassword', host='localhost')
cursor = conn.cursor()
