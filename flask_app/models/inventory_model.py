from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
import re

class Inventory:
    def __init__(self, data):
        self.id = data['id']
        self.item = data['item']
        self.quantity = data['quantity']
        self.price = data['price']
        self.character_id = data['character_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_one(cls, id):
        data = {
        "id":id
        }

        query = """
            SELECT * FROM inventories WHERE id = %(id)s
        """
        results = connectToMySQL(DB).query_db(query, data)

        if results:
            row = results[0]
            new_inventory = cls(row)
            return new_inventory


    @classmethod
    def get_by_character_id(cls,id):
        query = 'SELECT * FROM inventories WHERE character_id = %(id)s'
        results = connectToMySQL(DB).query_db(query,{"id" : id})
        
        inventory_row = []
        for row in results:
            new_inventory = cls(row)


            inventory_row.append(new_inventory)
        
        return inventory_row
    



    @classmethod
    def calculate_sale(cls, item_price, seller_coins, buyer_coins):
        seller_new_coins = (seller_coins + item_price)
        buyer_new_coins = (buyer_coins - item_price)

        return (seller_new_coins, buyer_new_coins)


    @classmethod
    def sell(cls, id, rita_id, buyer_new_coins, seller_new_coins):

        if buyer_new_coins < 0:
                flash("Sorry I can't pay you what that's worth!", "login")
                return

        data = {
            "id":id,
            "rita_id":rita_id
        }

        query = """
            UPDATE inventories
            SET character_id = %(rita_id)s 
            WHERE id = %(id)s;
        """
        connectToMySQL(DB).query_db(query, data)

        data2 = {
            "buyer_new_coins":buyer_new_coins
        }

        query = """
            UPDATE characters
            SET coins = %(buyer_new_coins)s
            WHERE id = 4;
        """
        connectToMySQL(DB).query_db(query, data2)

        data3 = {
            "seller_new_coins":seller_new_coins
        }

        query = """
            UPDATE characters
            SET coins = %(seller_new_coins)s
            WHERE id = 1
        """
        connectToMySQL(DB).query_db(query, data3)

    @classmethod
    def buy(cls, id, buyer_new_coins, seller_new_coins):

        if buyer_new_coins < 0:
                flash("Looks like you're coin pouch is a little light, honey.", "login")
                return

        data = {
            "id":id,
        }

        query = """
            UPDATE inventories
            SET character_id = 1 
            WHERE id = %(id)s;
        """
        connectToMySQL(DB).query_db(query, data)

        data2 = {
            "seller_new_coins":seller_new_coins
        }

        query = """
            UPDATE characters
            SET coins = %(seller_new_coins)s
            WHERE id = 4;
        """
        connectToMySQL(DB).query_db(query, data2)

        data3 = {
            "buyer_new_coins":buyer_new_coins
        }

        query = """
            UPDATE characters
            SET coins = %(buyer_new_coins)s
            WHERE id = 1
        """
        connectToMySQL(DB).query_db(query, data3)