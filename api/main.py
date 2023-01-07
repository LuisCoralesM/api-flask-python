from flask import Flask, request

app = Flask(__name__)

pokemon = {
    1: {"name": "Charizard", "type": "Fire/Flying"},
    2: {"name": "Blastoise", "type": "Water"},
    3: {"name": "Venasaur", "type": "Poison/Grass"},
}


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
