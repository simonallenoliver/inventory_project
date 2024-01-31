from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
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
    def get_by_character_id(cls,id):
        query = 'SELECT * FROM inventories WHERE character_id = %(id)s'
        results = connectToMySQL(DB).query_db(query,{"id" : id})
        
        inventory_row = []
        for row in results:
            new_inventory = cls(row)


            inventory_row.append(new_inventory)
        
        return inventory_row
    

    
    @classmethod
    def buy(cls, id, character_id):

        data = {
            "id":id,
            "character_id":character_id,
        }

        query = """
            UPDATE inventories
            SET character_id = %(character_id)s
            WHERE id = %(id)s
        """
        connectToMySQL(DB).query_db(query, data)


    @classmethod
    def sell(cls, id, rita_id):

        data = {
            "id":id,
            "rita_id":rita_id,
        }

        query = """
            UPDATE inventories
            SET character_id = %(rita_id)s
            WHERE id = %(id)s
        """
        connectToMySQL(DB).query_db(query, data)