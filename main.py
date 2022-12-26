from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask("PokeApi")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("name", required=True)

pokemon = {
    "1": {"name": "Charizard", "type": "Fire/Flying"},
    "2": {"name": "Blastoise", "type": "Water"},
    "3": {"name": "Venasaur", "type": "Poison/Grass"},
}


class Pokemon(Resource):
    def get(self, id):
        return pokemon[id]


api.add_resource(Pokemon, "/<id>")


if __name__ == "__main__":
    app.run()
