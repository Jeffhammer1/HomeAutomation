from . import config

class API_Keys():
    def __init__(self, key) -> None:
        pass

    def hue_api_key():
        config.read("website/config.ini")
        hue_key = config["API-KEYS"]["hue"]
        return hue_key

    def owm_api_key():
        config.read("website/config.ini")
        owm_key = config["API-KEYS"]["openweathermap"]
        return owm_key