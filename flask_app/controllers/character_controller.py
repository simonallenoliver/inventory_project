from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.character_model import Character
from flask_app.models.inventory_model import Inventory


@app.route('/')
def index():
        sid = Character.get_by_id(1)
        print("this is sid", sid.name)
        return render_template("index.html", sid=sid)

@app.route('/choose')
def choose():
        sid = Character.get_by_id(1)
        print("this is sid", sid.name)
        return render_template("choose.html", sid=sid)


@app.route('/start/<int:id>')
def start(id):
        current_character = Character.get_by_id(id)
        current_inventory = Inventory.get_by_character_id(id)
        rita_character = Character.get_by_id(4)
        rita_inventory = Inventory.get_by_character_id(4)
        print("this is current character",current_character.name)
        print("this is inventory", current_inventory)

        session['character_id'] = current_character.id
        return render_template("start.html", current_character = current_character, current_inventory = current_inventory, rita = rita_inventory, rita_character = rita_character)


@app.route('/ritas/<int:id>')
def rita(id):
        current_character = Character.get_by_id(id)
        current_inventory = Inventory.get_by_character_id(id)
        rita_character = Character.get_by_id(4)
        rita_inventory = Inventory.get_by_character_id(4)
        print("this is current character",current_character.name)
        print("this is inventory", current_inventory)

        session['character_id'] = current_character.id
        return render_template("ritas.html", current_character = current_character, current_inventory = current_inventory, rita = rita_inventory, rita_character = rita_character)


@app.route('/buy/<int:id>')
def buy(id):

        sale_item = Inventory.get_one(id)
        item_price = sale_item.price
        character_id = session['character_id']
        sid = Character.get_by_id(character_id)
        rita = Character.get_by_id(4)
        seller_coins = rita.coins
        buyer_coins = sid.coins
        new_coins = Inventory.calculate_sale(item_price, seller_coins, buyer_coins)
        print("this is new coins", new_coins)
        seller_new_coins = int(new_coins[0])
        buyer_new_coins = int(new_coins[1])

        character_id= session['character_id']
        Inventory.buy(id, buyer_new_coins, seller_new_coins)

        return redirect('/ritas/1')

@app.route('/sell/<int:id>')
def sell(id):
        rita_id = 4
        sale_item = Inventory.get_one(id)
        item_price = sale_item.price
        character_id = session['character_id']
        sid = Character.get_by_id(character_id)
        seller_coins = sid.coins
        rita = Character.get_by_id(4)
        buyer_coins = rita.coins
        new_coins = Inventory.calculate_sale(item_price, seller_coins, buyer_coins)
        print("this is new coins", new_coins)
        seller_new_coins = int(new_coins[1])
        buyer_new_coins = int(new_coins[0])
        Inventory.sell(id, rita_id, seller_new_coins, buyer_new_coins)
        return redirect('/ritas/1')


@app.route('/travel/<int:id>')
def travel(id):
        current_character = Character.get_by_id(id)
        current_inventory = Inventory.get_by_character_id(id)
        print("this is current character",current_character.name)
        print("this is inventory", current_inventory)

        session['character_id'] = current_character.id
        return render_template("travel.html", current_character = current_character, current_inventory = current_inventory,)

@app.route('/end_session')
def end_session():
        session.clear()
        return redirect("/")