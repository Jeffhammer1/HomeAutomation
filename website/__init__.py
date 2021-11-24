import threading
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from multiprocessing import Process
import multiprocessing
import time
import configparser

db = SQLAlchemy()
DB_NAME = "database.db"

CONFIG_NAME = "config.ini"
config = configparser.ConfigParser()

def start_server():

    stat = 0

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hndjuiahdui9ahdn"
    app.config["SQLALCHEMY_DATABASE_URI"]= f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    from .views import views
    from .api import api, auto_status
    from .models import devices, wetter_data
    from .backprocess import backend


    if stat == 1:
        @app.before_first_request
        def startup():
            p = Process(target=backend, args=(auto_status,))
            p.start()

    create_database(app)
    create_config_file()

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(api, url_prefix="/")

    return app

def create_database(app):
    if path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Create Database")
        return db

def create_config_file():
    if path.exists("website/" + CONFIG_NAME):
        pass
    else:
        f = open("website/config.ini", "x")
        f.write("")
        f.close()
        config["DEFAULT"] = {}
        config["API-KEYS"] = {"Openweathermap": "", "Hue": ""}
        with open("website/config.ini", "w") as configfile:
            config.write(configfile)
        print("Config datei wurde erzeugt")



