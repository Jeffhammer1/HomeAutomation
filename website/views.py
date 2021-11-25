from flask import Blueprint, render_template, redirect, url_for
import time
import flask
from requests.api import request

from multiprocessing.sharedctypes import Value

from website.classes import API_Keys
from . import config
from requests.sessions import Request
import website
from .classes import API_Keys

views = Blueprint("views", __name__)

#Init Startup variable
startup = 0

@views.route("/")
def home():
    return redirect(url_for("views.dashboard"))

@views.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@views.route("/menu", methods=["GET", "POST"])
def menu():
    if flask.request.method == "POST":
        config.read("website/config.ini")
        hue = flask.request.form.get("hue-key-input")
        owm = flask.request.form.get("owm-key-input")
        if not owm:
            pass
        else:
            config.set("API-KEYS", "openweathermap", str(owm))
        if not hue:
            pass
        else:
            config.set("API-KEYS", "hue", str(hue))
        with open("website/config.ini", "w") as configfile:
            config.write(configfile)
    return render_template("menu.html")

@views.route("/wetter")
def wetter():
    return render_template("wetter.html")

@views.route("/light")
def light():
    return render_template("light.html")
