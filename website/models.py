from . import db

class devices (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)

class wetter_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)