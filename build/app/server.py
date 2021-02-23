import uvicorn
import yaml


async def app(scope, receive, send):
    ...


def get_default_port():
    return 5000


try:
    with open('settings.yml') as f:
        settings = yaml.safe_load(f)
    app_port = settings['server']['container-port']
    if type(app_port) != int:
        app_port = get_default_port()
        print("Settings file is corrupted: port value is not a number. Using default port: " + str(app_port))
except FileNotFoundError:
    app_port = get_default_port()
    print("File not found. Using default port: " + str(app_port))
except KeyError:
    app_port = get_default_port()
    print("Settings file is corrupted: port key not found. Using default port: " + str(app_port))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=app_port, log_level="info")
