#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uvicorn
from auth import safe, instance
from db import postgres
from log_service import set_logs

logger = set_logs()


async def app(scope, receive, send):
    ...


def get_default_port():
    return 5000


def get_port():
    port = safe.get_value('CONTAINER_PORT')
    logger.debug("Trying to get env info: " + str(port))
    if port is None:
        port = get_default_port()
        logger.warning("Env getting failed. Using default port: " + str(port))
    return int(port)


if __name__ == "__main__":
    app_port = get_port()
    connection = postgres.connect(instance.db_host())
    if connection is not None:
        postgres.construct(connection)
        postgres.conn_close(connection)
    uvicorn.run("main:app", host="0.0.0.0", port=app_port, log_level="debug")

