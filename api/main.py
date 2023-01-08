from flask import Flask, request
import requests

api_url = "https://pokeapi.co/api/v2/pokemon/"
headers = {'Accept': 'application/json'}

app = Flask(__name__)

pokemon = {
    1: {"name": "Charizard", "type": "Fire/Flying"},
    2: {"name": "Blastoise", "type": "Water"},
    3: {"name": "Venasaur", "type": "Poison/Grass"},
}


@app.get("/pokemon/all")
def get_all_pokemon():
    try:
        r = requests.get(url=api_url, headers=headers)
        return r.json()
    except Exception as err:
        print(err)


@app.get('/')
def index():
    return 'Index Page'


@app.get("/pokemon")
def get_pokemon():
    return pokemon


@app.get("/pokemon/<int:id>")
def get_pokemon_by_id(id):
    return pokemon[id]


@app.post("/pokemon")
def add_pokemon():
    pokemon[list(pokemon)[-1] +
            1] = {"name": request.json["name"], "type": request.json["type"]}
    return pokemon
