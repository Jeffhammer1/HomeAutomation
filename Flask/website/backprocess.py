from multiprocessing.sharedctypes import Value
import time
from pynput import keyboard
from . import db
import keyboard
from .api import auto_status
from datetime import datetime 
import requests
import json
from . import classes

def backend(stat):
    i=0
    bootup_time = datetime.now()
    day_old = bootup_time
    wetter_daten = read_weather_data()
    while i == 0:
        try:
            if (stat.value == 1):
                t = new_day(day_old, wetter_daten)
                day_old = t[1]
                wetter_daten = t[0]
            else:
                pass
            time.sleep(1)
        finally:
            if keyboard.is_pressed("q"):
                print("Der Prozess wurde beendet.")
                break

        
def data_process():
    pass

def read_hue_data():
    hue_key = classes.API_Keys.hue_api_key()
    r = requests.get(url = "http://192.168.1.10/api/" + hue_key)
    hue_data = r.json()
    url = "http://192.168.1.10/api/"+ hue_key +"/lights/2/state"
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
    if hue_data["lights"]["1"]["state"]["reachable"] == True & hue_data["lights"]["1"]["state"]["on"] == True:
        payload = " {\"on\":true}"
        r = requests.put(url, data = payload, headers=headers)
    else:
        payload = " {\"on\":false}"
        r = requests.put(url, data = payload, headers=headers)
    pass

def read_weather_data():
    owm_key = classes.API_Keys.owm_api_key()
    api_url = "https://api.openweathermap.org/data/2.5/onecall?lat=47.1921&lon=7.3959&appid="
    r = requests.get(url = api_url + owm_key + "&units=metric")
    data = r.json()
    return data

def new_day(old, wetter_data):
    new = datetime.now()
    if new.day > old.day:
        data = read_weather_data()
        print("neue daten wurden übertragen")
        return data , new
    else:
        print("Es wurden keine neuen Daten geladen")
        return wetter_data, old
    pass