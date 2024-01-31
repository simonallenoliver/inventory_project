from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.character_model import Character
from flask_app.models.inventory_model import Inventory




@app.route('/')
def index():
        sid = Character.get_by_id(1)
        print("this is sid", sid.name)
        return render_template("index.html", sid=sid)


@app.route('/start/<int:id>')
def start(id):
        current_character = Character.get_by_id(id)
        current_inventory = Inventory.get_by_character_id(id)
        rita_inventory = Inventory.get_by_character_id(4)
        print("this is current character",current_character.name)
        print("this is inventory", current_inventory)

        session['character_id'] = current_character.id
        return render_template("start.html", current_character = current_character, current_inventory = current_inventory, rita = rita_inventory)


@app.route('/buy/<int:id>')
def buy(id):
        character_id= session['character_id']
        Inventory.buy(id, character_id)

        return redirect('/start/1')

@app.route('/sell/<int:id>')
def sell(id):
        rita_id = 4
        Inventory.sell(id, rita_id)

        return redirect('/start/1')
