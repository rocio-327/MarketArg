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
    def get_sellers():
        sellers = repositories["sellers"].get_all_sellers()
        return object_to_json(sellers)

    @app.route("/api/sellers/products/<id>", methods=["GET"])
    def get_product_by_seller_id(id):
        seller = repositories["products"].get_product_by_seller_id(id)
        return object_to_json(seller)

    @app.route("/api/sellers/<id>", methods=["GET"])
    def get_sellers_by_id(id):
        sellers = repositories["sellers"].get_sellers_by_id(id)
        return object_to_json(sellers)

    return app
