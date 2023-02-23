from flask import Flask, request, Response
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


@app.get("/pokemon_lbyl/<string:name>")
def get_pokemon_by_name_lbyl(name):
    try:
        r = request_pokemon_by_name(name)
        data = r.json()

        if r.status_code == 404:
            raise Exception("Pokemon not found")

        if r.status_code != 200:
            raise Exception("Unsuccessful request")

        if data is None:
            raise Exception("Pokemon not found")

        return data
    except Exception as err:
        return Response(str(err), status=500)


@app.get("/pokemon_eapf/<string:name>")
def get_pokemon_by_name_eapf(name):
    try:
        r = request_pokemon_by_name(name)
        return r.json()
    except requests.exceptions.Timeout as err:
        # Custom message and try again
        # Log error
        return err
    except requests.exceptions.HTTPError as err:
        # Custom message and try again
        # Log error
        return err
    except requests.exceptions.RequestException as err:
        # Custom error handling
        # Check status code, etc
        print(err)
        return Response(str("Request error"))


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
