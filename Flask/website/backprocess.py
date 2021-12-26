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


#Notiz:
#payload = " {\"on\":true}"
#r = requests.put(url, data = payload, headers=headers)

def backend(stat):
    arbeitconfig = classes.HUE_config.arbeit()
    bootuptime = datetime.now()
    time_old = bootuptime
    wetter_daten = get_data("owm")

    #Variablen erstellen
    sunrise = wetter_daten["current"]["sunrise"]
    sunset = wetter_daten["current"]["sunset"]

    while True:
        try:
            if (stat.value == 1):
                #Daten initialisieren
                all_hue_data = get_data("hue")
                time_now = datetime.now().replace(microsecond=0)

                #Tageswechsel
                if (time_now.second != time_old.second):
                    wetter_daten = get_data("owm")
                    sunrise = wetter_daten["current"]["sunrise"]
                    sunrise = datetime.fromtimestamp(sunrise)
                    sunset = wetter_daten["current"]["sunset"]
                    sunset = datetime.fromtimestamp(sunset)
                    time_old = datetime.now()
                else:
                    pass


                #controll sunrise and sunnset
                if (sunset == time_now):
                    for x in arbeitconfig:
                        control_hue_light(x)
                elif(sunrise == time_now):
                    for x in arbeitconfig:
                        control_hue_light(x, 254, 8417)
                    pass



                print("Auto")
            else:
                pass
            time.sleep(1)
        finally:
            if keyboard.is_pressed("q"):
                print("Der Prozess wurde beendet.")
                break


def get_data(source):
    if (source == "hue"):
        url = "http://192.168.1.10/api/" + classes.API_Keys.hue_api_key()
    elif (source == "owm"):
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=47.1921&lon=7.3959&appid=" + classes.API_Keys.owm_api_key()
    else:
        print("Fehler in Parameter Source")
    r = requests.get(url)
    data = r.json()
    return data

def control_hue_light(nummer, brighness, color):
    payload = " {\"on\":true}"
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
    nummer = str(nummer)
    url = "http://192.168.1.10/api/" + classes.API_Keys.hue_api_key() + "/lights/" + nummer + "/state"
    r = requests.put(url, data=payload, headers=headers)
    print(r.json())
    pass