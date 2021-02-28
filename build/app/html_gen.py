#!/usr/bin/env python
# -*- coding: utf-8 -*-

from airium import Airium
from auth import instance
from db import postgres


def homepage():
    connection = postgres.connect(instance.db_host())
    response = postgres.read_sql(connection, "./db/get/user.sql", False)
    username = response[0][0][1]
    balance = response[0][0][3]

    code = Airium()

    code('<!DOCTYPE html>')
    with code.html(lang="ru"):
        with code.head():
            code.meta(charset="utf-8")
            code.title(_t="Test")

        with code.body():
            with code.h3(id="id01", klass='main_header'):
                code("Привет, " + str(username) + ", твой баланс составляет " + str(balance) + " ежей.")
    return str(code)
