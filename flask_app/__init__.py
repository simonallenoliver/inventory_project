# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"

#replace the name once a proper database is created
DB = "inventory_db"