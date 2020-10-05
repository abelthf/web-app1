# services/users/project/__init__.py

import os  # nuevo

from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy  # nuevo


# instanciado la app
app = Flask(__name__)

api = Api(app)


# estableciendo configuración
app_settings = os.getenv("APP_SETTINGS")  # nuevo
app.config.from_object(app_settings)  # nuevo


# incializando la db
db = SQLAlchemy(app)  # nuevo


# modelo
class User(db.Model):  # nuevo
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UsersPing(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


api.add_resource(UsersPing, "/users/ping")
