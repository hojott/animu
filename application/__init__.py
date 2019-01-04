from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
# Käytetään candidates.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///candidates.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.candidates import models
from application.candidates import views

from application.auth import models
from application.auth import views

db.create_all()
