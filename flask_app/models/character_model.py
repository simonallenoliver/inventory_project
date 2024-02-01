from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
import re



class Character:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.coins = data['coins']
        self.expo = data['expo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    
    @classmethod
    def get_by_id(cls,id):
        query = 'SELECT * FROM characters WHERE id = %(id)s'
        results = connectToMySQL(DB).query_db(query,{"id" : id})
        
        if not results:
            return None
        
        return Character(results[0])