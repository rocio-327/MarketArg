import sqlite3
from src.webserver import create_app
from src.domain.seller import SellerRepository
from src.domain.product import ProductRepository


database_path = "data/database.db"

repositories = {
    "sellers": SellerRepository(database_path),
    "products": ProductRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
