#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uvicorn
from auth import safe
from db import postgres
import logging
import datetime


async def app(scope, receive, send):
    ...


def get_default_port():
    return 5000


logging.basicConfig(filename="./logs/"+str(datetime.date.today())+".log", level=logging.DEBUG)
app_port = safe.get_value('CONTAINER_PORT')
logging.debug("Trying to get env info: " + str(app_port))
if app_port is None:
    app_port = get_default_port()
    logging.error("Env getting failed. Using default port: " + str(app_port))

if __name__ == "__main__":
    postgres.connect()
    uvicorn.run("main:app", host="0.0.0.0", port=int(app_port), log_level="info")
