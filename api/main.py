from flask import Flask, request
from utils import *


app = Flask(__name__)

pokemon = {
    1: {"name": "Charizard", "type": "Fire/Flying"},
    2: {"name": "Blastoise", "type": "Water"},
    3: {"name": "Venasaur", "type": "Poison/Grass"},
}


@app.get("/pokemon/all")
def get_all_pokemon():
    try:
        r = request_all_pokemon()
        return r.json()
    except Exception as err:
        print(err)
        return err


@app.get("/pokemon/<string:id>")
def get_pokemon_by_id(id):
    try:
        r = request_pokemon_by_id(id)
        return r.json()
    except Exception as err:
        print(err)
        return err


@app.get("/mypokemon")
def get_pokemon():
    return pokemon


@app.post("/mypokemon")
def add_pokemon():
    pokemon[list(pokemon)[-1] +
            1] = {"name": request.json["name"], "type": request.json["type"]}
    return pokemon


if __name__ == '__main__':
    app.run(debug=True, port=5000)
