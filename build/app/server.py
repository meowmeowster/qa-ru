#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uvicorn
from auth import safe
import logging
import datetime


async def app(scope, receive, send):
    ...


def get_default_port():
    return 5000


logging.basicConfig(filename="./logs/"+str(datetime.date.today())+".log", level=logging.DEBUG)
app_port = int(safe.get_value('CONTAINER_PORT'))
logging.debug("Trying to get env info: " + str(app_port))
if app_port is None:
    app_port = get_default_port()
    logging.debug("Using default port: " + str(app_port))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=app_port, log_level="info")
