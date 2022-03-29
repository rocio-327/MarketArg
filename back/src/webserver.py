from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/sellers", methods=["GET"])
    def sellers_get():
        sellers = repositories["sellers"].get_all_sellers()
        return object_to_json(sellers)

    return app
