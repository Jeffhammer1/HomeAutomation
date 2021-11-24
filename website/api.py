from datetime import time
from flask import Blueprint, jsonify, request
import flask
import multiprocessing
import requests
import time

#test

from website.classes import API_Keys

api = Blueprint("api", __name__)

auto_status = multiprocessing.Value("i")

#Hue API
hue_ip = "192.168.1.10"

#Wetter API
api_url = "https://api.openweathermap.org/data/2.5/onecall?lat=47.1921&lon=7.3959&appid="

@api.route("/readwetterdata", methods=["GET", "POST"])
def readwetterdata():
    key = API_Keys.owm_api_key()
    r = requests.get(url = api_url + key + "&units=metric")
    data = r.json()
    return (data)

@api.route("/readhuedata", methods=["GET", "POST"])
def readhuedata():
    key = API_Keys.hue_api_key()
    r = requests.get(url= "http://" + hue_ip + "/api/" + key)
    data = r.json()
    return data

@api.route("/status", methods=["GET", "POST"])
def status():
    a = auto_status.value
    if flask.request.method == "GET":
        x = {"status":a}
        return jsonify(x)
    elif flask.request.method == "POST":
        if a == 1:
            a = 0
            auto_status.value = 0
            x = {"status":a}
            return jsonify(x)
        elif a == 0:
            a = 1
            auto_status.value = 1
            x = {"status":a}
            return jsonify(x)
