from flask import Flask
from flask_restful import Resource, Api

app = Flask("PokeApi")
api = Api(app)


class Pokemon(Resource):
    def get(self):
        return "Charizard"


api.add_resource(Pokemon, "/")

if __name__ == "__main__":
    app.run()
