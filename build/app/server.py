import uvicorn
import os
from os.path import join, dirname
from dotenv import load_dotenv


async def app(scope, receive, send):
    ...


def get_default_port():
    return 5000


try:
    env_path = join(dirname(__file__), '.env')
    load_dotenv(env_path)
    app_port = os.getenv('CONTAINER_PORT')
    if type(app_port) != int:
        app_port = get_default_port()
        print("Dotenv error: port value is not a number. Using default port: " + str(app_port))
except FileNotFoundError:
    app_port = get_default_port()
    print("Dotenv file not found. Using default port: " + str(app_port))


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=app_port, log_level="info")
