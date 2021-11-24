from multiprocessing.sharedctypes import Value
import time
from pynput import keyboard
from . import db
import keyboard
from .api import auto_status

def backend(stat):
    i=0
    while i == 0:
        try:
            if (stat.value == 1):
                pass
            else:
                pass
            time.sleep(1)
        finally:
            if keyboard.is_pressed("q"):
                print("Der Prozess wurde beendet.")
                break