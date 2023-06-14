from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app import app

class Cookie_order:
    #connect to database
    DB = "cookies"
    
    def __init__(self, cookie_order):
        #match SQL ['column name']
        self.id = cookie_order['id']
        self.name = cookie_order['name']
        self.cookie_type = cookie_order['cookie_type']
        self.num_boxes = cookie_order['num_boxes']
        self.created_at = cookie_order['created_at']
        self.updated_at = cookie_order['updated_at']
        
        
#CREATE
    @classmethod
    def create_cookie_order(cls, user_cookie_order):
        query = """"
        INSERT INTO cookies (name, cookie_type, num_boxes)
        VALUES (%(names)s, %(cookie_type)s, %(num_boxes)s)
        ;"""
        result = connectToMySQL(cls.DB).query_db(query, user_cookie_order)
        return result
        
#READ
    @classmethod
    def show_orders(cls):
        query = """
        SELECT * FROM cookies
        ;"""
        orders_info = connectToMySQL(cls.DB).query_db(query)
        #returns a list of dictionaries
        orders = []
        for order in orders_info:
            orders.append(cls(order)) #pass in specific order to database
        return orders

    @staticmethod
    def validate_order(cookie_order):
        valid = True
        
        if len(cookie_order["name"]) < 2:
            valid = False
            flash("Name needs to be at least 2 characters")
        if len(cookie_order['cookie_type']) < 2:
            valid = False
            flash("Name needs to be at least 2 characters")
        if (cookie_order['num_boxes']) <= 0:
            valid = False
            flash("Please select at least one box")
        return valid