from multiprocessing.sharedctypes import Value
import time
from pynput import keyboard
from . import db
import keyboard
from .api import auto_status
from datetime import datetime 
import requests
import json



def backend(stat):
    i=0
    bootup_time = datetime.now()
    while i == 0:
        try:
            if (stat.value == 1):
                data_process()
            else:
                pass
            time.sleep(1)
        finally:
            if keyboard.is_pressed("q"):
                print("Der Prozess wurde beendet.")
                break

        
def data_process():
    pass 