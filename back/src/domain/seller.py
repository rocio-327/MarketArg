import sqlite3


class Seller:
    def __init__(
        self, seller_id, seller_name, seller_description, seller_logo, seller_email
    ):
        self.seller_id = seller_id
        self.seller_name = seller_name
        self.seller_description = seller_description
        self.seller_logo = seller_logo
        self.seller_email = seller_email

    def to_dict(self):
        return {
            "seller_id": self.seller_id,
            "seller_name": self.seller_name,
            "seller_description": self.seller_description,
            "seller_logo": self.seller_logo,
            "seller_email": self.seller_email,
        }


class SellerRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists sellers (
                seller_id varchar PRIMARY KEY,
                seller_name varchar,
                seller_description varchar,
                seller_logo varchar,
                seller_email varchar
            )
        """

        sql_user_request = """
            create table if not exists request (
                seller_id varchar PRIMARY KEY,
                user_email varchar,
                user_request varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.execute(sql_user_request)

        conn.commit()

    def get_all_sellers(self):
        sql = """select * from sellers"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        sellers = []
        for item in data:
            seller = Seller(**item)
            sellers.append(seller)

        return sellers

    def search_by_seller_name(self, seller_name):
        sql = """SELECT * FROM sellers WHERE seller_name=:seller_name"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"seller_name": seller_name})

        data = cursor.fetchall()

        sellers = []
        for item in data:
            sellers = Seller(**item)
            sellers.append(sellers)

        return sellers

    def get_sellers_by_id(self, seller_id):
        sql = """SELECT * FROM sellers WHERE seller_id=:seller_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"seller_id": seller_id})

        data = cursor.fetchone()

        if data is not None:
            seller = Seller(**data)
        else:
            seller = None

        return seller

    def save(self, seller):
        sql = """insert OR REPLACE into sellers (seller_id, seller_name, seller_description, seller_email, seller_logo) values (
            :seller_id, :seller_name, :seller_description, :seller_email, :seller_logo
        ) """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            seller.to_dict(),
        )
        conn.commit()

    def save_request(self, data):
        sql = """insert OR REPLACE into request (seller_id, user_email, user_request) values (
            :seller_id, :user_email, :user_request
        ) """

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "seller_id": data["seller_id"],
                "user_email": data["user_email"],
                "user_request": data["user_request"],
            },
        )
        conn.commit()
