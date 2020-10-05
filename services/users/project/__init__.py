# services/users/project/__init__.py

import os  # nuevo

from flask import Flask, jsonify
from flask_restful import Resource, Api


# instanciado la app
app = Flask(__name__)

api = Api(app)


# estableciendo configuración
app_settings = os.getenv("APP_SETTINGS")  # nuevo
app.config.from_object(app_settings)  # nuevo


class UsersPing(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


api.add_resource(UsersPing, "/users/ping")
