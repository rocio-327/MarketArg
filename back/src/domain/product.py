import sqlite3


class Product:
    def __init__(
        self,
        seller_id,
        product_id,
        product_description,
        product_name,
        product_price,
        product_img,
    ):
        self.seller_id = seller_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_img = product_img

    def to_dict(self):
        return {
            "seller_id": self.seller_id,
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_description": self.product_description,
            "product_img": self.product_img,
            "product_price": self.product_price,
        }


class ProductRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists products (
                seller_id varchar,
                product_id varchar PRIMARY KEY,
                product_name varchar,
                product_description varchar,
                product_img varchar,
                product_price varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_products(self):
        sql = """select * from products"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        products = []
        for item in data:
            product = product(**item)
            products.append(product)

        return products

    def search_by_product_name(self, product_name):
        sql = """SELECT * FROM products WHERE product_name=:product_name"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"product_name": product_name})

        data = cursor.fetchall()

        products = []
        for item in data:
            products = product(**item)
            products.append(product)

        return products

    def get_product_by_seller_id(self, seller_id):
        sql = """SELECT * FROM products WHERE seller_id=:seller_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"seller_id": seller_id})

        data = cursor.fetchall()

        products = []
        for item in data:
            product = Product(**item)
            products.append(product)
        return products

        if data is not None:
            product = product(**data)
        else:
            product = None

        return product

    def save(self, product):
        sql = """insert OR REPLACE into products (seller_id, product_id, product_name, product_description, product_img,product_price) values (
            :seller_id, :product_id, :product_name, :product_description, :product_img,:product_price
        ) """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            product.to_dict(),
        )
        conn.commit()
