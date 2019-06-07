from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS

from config import Config
from db import db
from resources.user import *

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
jwt = JWTManager(app)
api = Api(app)
db.init_app(app)


# Route
api.add_resource(UserEndPoint, "/register")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
