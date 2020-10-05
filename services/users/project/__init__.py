# services/users/project/__init__.py


from flask import Flask, jsonify
from flask_restful import Resource, Api


# instanciado la app
app = Flask(__name__)

api = Api(app)


# estableciendo configuración
app.config.from_object("project.config.DevelopmentConfig")  # nuevo


class UsersPing(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}


api.add_resource(UsersPing, "/users/ping")
